// 边缘网关：拦截所有非 /api 请求。
// - 未登录：返回登录页（自带样式，不依赖外部资源，避免内容泄露）。
// - 已登录：用 env.ASSETS 转发静态资源（VitePress 产物为 .html 直链，并做 index.html 兜底）。
import { getSessionUser } from './_helpers.js'

const LOGIN_PATH = '/login.html'

export async function onRequest(context) {
  const { request, env } = context
  const url = new URL(request.url)
  const email = await getSessionUser(request, env)

  if (!email) {
    // 未登录：返回登录页
    const loginRes = await env.ASSETS.fetch(new Request(url.origin + LOGIN_PATH))
    if (loginRes.ok) {
      const html = await loginRes.text()
      return new Response(html, {
        status: 200,
        headers: { 'content-type': 'text/html; charset=utf-8', 'cache-control': 'no-store' }
      })
    }
    // 兜底：内联一个最简登录页（正常不会走到这里）
    return new Response(fallbackLogin(url), {
      status: 200,
      headers: { 'content-type': 'text/html; charset=utf-8', 'cache-control': 'no-store' }
    })
  }

  // 已登录：转发静态资源
  let res = await env.ASSETS.fetch(request)
  if (res.status === 404) {
    // 处理干净 URL：/notes/finance → /notes/finance.html；/quiz → /quiz.html；目录 → /index.html
    const alt = await resolveAsset(env, url)
    if (alt) return alt
    const notFound = await env.ASSETS.fetch(new Request(url.origin + '/404.html'))
    if (notFound.ok) {
      return new Response(await notFound.text(), {
        status: 404,
        headers: { 'content-type': 'text/html; charset=utf-8' }
      })
    }
  }
  return res
}

async function resolveAsset(env, url) {
  const path = url.pathname
  const candidates = []
  if (path === '/' || path.endsWith('/')) {
    candidates.push(path + 'index.html')
  } else if (!/\.[a-z0-9]+$/i.test(path)) {
    candidates.push(path + '.html', path + '/index.html')
  }
  for (const c of candidates) {
    const r = await env.ASSETS.fetch(new Request(url.origin + c))
    if (r.ok) return r
  }
  return null
}

function fallbackLogin(url) {
  const next = url.pathname === LOGIN_PATH ? '/' : url.pathname + url.search
  return `<!doctype html><html lang="zh-CN"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>登录 · 我的知识库</title></head><body style="margin:0;font-family:system-ui,sans-serif;background:#eef2ff;display:grid;place-items:center;min-height:100vh">
<div style="background:#fff;padding:32px 28px;border-radius:16px;box-shadow:0 10px 30px rgba(30,58,138,.12);width:320px">
<h1 style="margin:0 0 4px;font-size:20px;color:#1e3a8a">我的知识库</h1>
<p style="margin:0 0 18px;color:#64748b;font-size:13px">请登录以继续</p>
<form method="post" action="/api/auth/login" style="display:flex;flex-direction:column;gap:10px">
<input name="email" type="email" placeholder="邮箱" required style="padding:10px;border:1px solid #cbd5e1;border-radius:8px">
<input name="password" type="password" placeholder="口令" required style="padding:10px;border:1px solid #cbd5e1;border-radius:8px">
<button style="padding:10px;background:#1e3a8a;color:#fff;border:0;border-radius:8px;cursor:pointer">进入站点</button>
</form></div></body></html>`
}
