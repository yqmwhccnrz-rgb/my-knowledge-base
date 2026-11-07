import { json, destroySession, clearSessionCookie } from '../../_helpers.js'

export async function onRequest(context) {
  const { request, env } = context
  if (request.method !== 'POST') return json({ error: 'method not allowed' }, 405)
  await destroySession(request, env)
  return new Response(JSON.stringify({ ok: true }), {
    status: 200,
    headers: {
      'content-type': 'application/json; charset=utf-8',
      'set-cookie': clearSessionCookie()
    }
  })
}
