// Cloudflare Pages Functions 共享工具
// 自建登录体系：会话存于 KV（kb_sid cookie → sess:<token> → email），密码用 PBKDF2 哈希。
// 彻底替代 Cloudflare Access，人数无上限、零费用。

const SESSION_COOKIE = 'kb_sid'
const SESSION_TTL = 60 * 60 * 24 * 7 // 7 天（秒）
// Cloudflare Web Crypto 限制 PBKDF2 迭代次数上限为 100000，超过会抛 NotSupportedError。
const PBKDF2_ITER = 100000

export function json(data, status = 200) {
  return new Response(JSON.stringify(data), {
    status,
    headers: { 'content-type': 'application/json; charset=utf-8' }
  })
}

export async function readJSON(kv, key, fallback) {
  const v = await kv.get(key)
  if (!v) return fallback
  try {
    return JSON.parse(v)
  } catch {
    return fallback
  }
}

// ---------- 会话 ----------

export function sessionCookie(token) {
  return `${SESSION_COOKIE}=${encodeURIComponent(token)}; Path=/; HttpOnly; Secure; SameSite=Lax; Max-Age=${SESSION_TTL}`
}

export function clearSessionCookie() {
  return `${SESSION_COOKIE}=; Path=/; HttpOnly; Secure; SameSite=Lax; Max-Age=0`
}

function readToken(request) {
  const cookie = request.headers.get('Cookie') || ''
  const m = cookie.match(/(?:^|;\s*)kb_sid=([^;]+)/)
  return m ? decodeURIComponent(m[1]) : null
}

// 读取并校验会话，返回 email 或 null
export async function getSessionUser(request, env) {
  const token = readToken(request)
  if (!token) return null
  const sess = await readJSON(env.KB_KV, 'sess:' + token, null)
  if (!sess || !sess.email) return null
  if (sess.exp && sess.exp < Date.now()) {
    await env.KB_KV.delete('sess:' + token).catch(() => {})
    return null
  }
  return sess.email
}

export async function createSession(env, email) {
  const token = crypto.randomUUID()
  const exp = Date.now() + SESSION_TTL * 1000
  await env.KB_KV.put('sess:' + token, JSON.stringify({ email, exp }), {
    expirationTtl: SESSION_TTL
  })
  return token
}

export async function destroySession(request, env) {
  const token = readToken(request)
  if (token) await env.KB_KV.delete('sess:' + token).catch(() => {})
}

// ---------- 账号 ----------

export async function getUser(env, email) {
  return readJSON(env.KB_KV, 'user:' + email.toLowerCase(), null)
}

export async function putUser(env, email, salt, hash) {
  await env.KB_KV.put(
    'user:' + email.toLowerCase(),
    JSON.stringify({ email, salt, hash, created: Date.now() })
  )
}

// ---------- 密码哈希（PBKDF2-SHA256，无第三方依赖） ----------

function toHex(buf) {
  return [...new Uint8Array(buf)].map((b) => b.toString(16).padStart(2, '0')).join('')
}

function hexToBytes(hex) {
  const a = new Uint8Array(hex.length / 2)
  for (let i = 0; i < a.length; i++) a[i] = parseInt(hex.substr(i * 2, 2), 16)
  return a
}

export async function hashPassword(pw, saltHex) {
  const enc = new TextEncoder()
  const salt = saltHex
    ? hexToBytes(saltHex)
    : crypto.getRandomValues(new Uint8Array(16))
  const keyMat = await crypto.subtle.importKey('raw', enc.encode(pw), 'PBKDF2', false, [
    'deriveBits'
  ])
  const bits = await crypto.subtle.deriveBits(
    { name: 'PBKDF2', salt, iterations: PBKDF2_ITER, hash: 'SHA-256' },
    keyMat,
    256
  )
  return { salt: toHex(salt), hash: toHex(bits) }
}

export async function verifyPassword(pw, saltHex, hashHex) {
  const { hash } = await hashPassword(pw, saltHex)
  return timingSafeEqual(hash, hashHex)
}

export function timingSafeEqual(a, b) {
  if (a.length !== b.length) return false
  let diff = 0
  for (let i = 0; i < a.length; i++) diff |= a.charCodeAt(i) ^ b.charCodeAt(i)
  return diff === 0
}

// ---------- 兼容旧调用：返回当前用户标识（email 或 null） ----------

export async function getUserId(request, env) {
  return getSessionUser(request, env)
}

// 校验是否已登录，未登录返回 401 Response（或 null 表示已登录）
export async function requireAuth(request, env) {
  const email = await getSessionUser(request, env)
  if (!email) return json({ error: 'unauthenticated' }, 401)
  return email
}
