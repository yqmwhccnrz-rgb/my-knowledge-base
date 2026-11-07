import { json, getUser, putUser, hashPassword, createSession, sessionCookie } from '../../_helpers.js'

const EMAIL_RE = /^[^@\s]+@[^@\s]+\.[^@\s]+$/

export async function onRequest(context) {
  const { request, env } = context
  if (request.method !== 'POST') return json({ error: 'method not allowed' }, 405)

  const body = await request.json().catch(() => ({}))
  const email = (body.email || '').trim().toLowerCase()
  const password = body.password || ''
  const invite = body.invite || ''

  if (!EMAIL_RE.test(email)) return json({ error: '邮箱格式不正确' }, 400)
  if (password.length < 6) return json({ error: '口令至少 6 位' }, 400)

  // 邀请码：若站长在 Cloudflare 仪表盘设置了 KB_INVITE_CODE，则必须匹配才允许注册。
  if (env.KB_INVITE_CODE && invite !== env.KB_INVITE_CODE) {
    return json({ error: '邀请码不正确' }, 403)
  }

  if (await getUser(env, email)) return json({ error: '该邮箱已注册' }, 409)

  const { salt, hash } = await hashPassword(password)
  await putUser(env, email, salt, hash)

  // 注册成功直接登录
  const token = await createSession(env, email)
  return new Response(JSON.stringify({ ok: true, email }), {
    status: 200,
    headers: {
      'content-type': 'application/json; charset=utf-8',
      'set-cookie': sessionCookie(token)
    }
  })
}
