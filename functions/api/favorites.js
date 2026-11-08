import { getUserId, readJSON, json } from '../_helpers.js'

const MAX = 200

export async function onRequest(context) {
  const { request, env } = context
  const userId = getUserId(request)
  const key = 'fav:' + userId

  if (request.method === 'GET') {
    const favorites = await readJSON(env.KB_KV, key, [])
    return json(favorites)
  }

  if (request.method === 'POST') {
    const body = await request.json().catch(() => ({}))
    const id = body && body.id
    if (!id) return json({ error: 'missing id' }, 400)

    let favorites = await readJSON(env.KB_KV, key, [])
    if (body.action === 'remove') {
      favorites = favorites.filter((x) => x !== id)
    } else {
      if (!favorites.includes(id)) favorites.push(id)
      if (favorites.length > MAX) favorites = favorites.slice(-MAX)
    }
    await env.KB_KV.put(key, JSON.stringify(favorites))
    return json({ favorites })
  }

  return json({ error: 'method not allowed' }, 405)
}
