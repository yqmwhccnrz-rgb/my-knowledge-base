import { json, getSessionUser } from '../../_helpers.js'

export async function onRequest(context) {
  const { request, env } = context
  const email = await getSessionUser(request, env)
  if (!email) return json({ error: 'unauthenticated' }, 401)
  return json({ email })
}
