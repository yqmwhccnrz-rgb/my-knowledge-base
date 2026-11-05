import { getUserId, readJSON, json } from '../_helpers.js'

const MAX = 50

export async function onRequest(context) {
  const { request, env } = context
  const userId = getUserId(request)
  const key = 'rec:' + userId

  if (request.method === 'GET') {
    const records = await readJSON(env.KB_KV, key, [])
    return json(records)
  }

  if (request.method === 'POST') {
    const body = await request.json().catch(() => ({}))
    const record = {
      note: (body && body.note) || '',
      score: Number((body && body.score) || 0),
      total: Number((body && body.total) || 0),
      date: new Date().toISOString()
    }
    let records = await readJSON(env.KB_KV, key, [])
    records.unshift(record)
    if (records.length > MAX) records = records.slice(0, MAX)
    await env.KB_KV.put(key, JSON.stringify(records))
    return json({ records })
  }

  return json({ error: 'method not allowed' }, 405)
}
