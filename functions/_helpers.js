// Cloudflare Pages Functions 共享工具
// 用户标识：优先使用 Cloudflare Access 登录邮箱；否则使用前端传来的匿名访客 ID。

export function getUserId(request) {
  const email = request.headers.get('Cf-Access-Authenticated-User-Email')
  if (email) return 'email:' + email
  const vid = request.headers.get('x-visitor-id') || 'anon'
  return 'vid:' + vid
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

export function json(data, status = 200) {
  return new Response(JSON.stringify(data), {
    status,
    headers: { 'content-type': 'application/json; charset=utf-8' }
  })
}
