// 临时诊断：分别验证 crypto.randomUUID / crypto.subtle / KV.put 是否可用。修复后删除。
export async function onRequest(context) {
  const { env } = context
  const out = {}
  try {
    out.hasCrypto = typeof crypto !== 'undefined'
    out.hasSubtle = !!(crypto && crypto.subtle)
    out.hasRandomUUID = typeof crypto.randomUUID === 'function'
    out.randomUUID = crypto.randomUUID ? crypto.randomUUID() : 'NO'
  } catch (e) { out.cryptoPhase = 'ERR: ' + e.message }

  try {
    const enc = new TextEncoder()
    const keyMat = await crypto.subtle.importKey('raw', enc.encode('test123'), 'PBKDF2', false, ['deriveBits'])
    const bits = await crypto.subtle.deriveBits(
      { name: 'PBKDF2', salt: crypto.getRandomValues(new Uint8Array(16)), iterations: 150000, hash: 'SHA-256' },
      keyMat, 256
    )
    out.subtle = 'OK len=' + bits.byteLength
  } catch (e) { out.subtle = 'ERR: ' + e.message }

  try {
    if (!env.KB_KV) out.kv = 'NO_KB_KV_BINDING'
    else {
      await env.KB_KV.put('diag:test', JSON.stringify({ t: 1 }), { expirationTtl: 60 })
      const v = await env.KB_KV.get('diag:test')
      out.kv = v ? 'PUT+GET OK' : 'PUT OK but GET null'
    }
  } catch (e) { out.kv = 'ERR: ' + e.message }

  return new Response(JSON.stringify(out, null, 2), {
    status: 200,
    headers: { 'content-type': 'application/json; charset=utf-8' }
  })
}
