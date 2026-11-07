import { json, getUser, verifyPassword, createSession, sessionCookie } from '../../_helpers.js'

const EMAIL_RE = /^[^@\s]+@[^@\s]+\.[^@\s]+$/

export async function onRequest(context) {
  const { request, env } = context
  if (request.method !== 'POST') return json({ error: 'method not allowed' }, 405)

  const body = await request.json().catch(() => ({}))
  const email = (body.email || '').trim().toLowerCase()
  const password = body.password || ''

  if (!EMAIL_RE.test(email)) return json({ error: '邮箱格式不正确' }, 400)
  if (!password) return json({ error: '请输入口令' }, 400)

  const user = await getUser(env, email)
  if (!user) return json({ error: '账号不存在，请先注册' }, 401)
  const ok = await verifyPassword(password, user.salt, user.hash)
  if (!ok) return json({ error: '口令不正确' }, 401)

  const token = await createSession(env, email)
  return new Response(JSON.stringify({ ok: true, email }), {
    status: 200,
    headers: {
      'content-type': 'application/json; charset=utf-8',
      'set-cookie': sessionCookie(token)
    }
  })
}
