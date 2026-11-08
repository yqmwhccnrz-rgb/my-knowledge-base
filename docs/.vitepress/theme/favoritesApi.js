// 收藏数据的共享读取层。
// 之前 FavoriteButton 与 Favorites 在同一页面各发一次 /api/favorites，
// 切换笔记时又重复请求；而该接口走 Cloudflare Functions + KV，冷启动较慢。
// 这里做三件事：合并并发请求、SPA 会话内短时缓存、写操作后更新缓存。
//
// 另一职责：检测 Cloudflare Access 会话过期。过期时后端会把请求 302 重定向到
// 登录页（返回 HTML 而非 JSON），若不做区分，res.json() 会抛错被 catch 吞掉，
// 用户看到空收藏 / 空成绩却以为是网站坏了。这里统一识别并广播「登录已过期」事件。

let cache = null
let cacheAt = 0
let inflight = null
const TTL = 60 * 1000

// 登录过期信号：已广播过就不再重复广播，成功拿到一次数据后重置，允许下次再提示
let authNotified = false

function visitorId() {
  let id = localStorage.getItem('kb_visitor_id')
  if (!id) {
    id = 'v_' + (crypto.randomUUID ? crypto.randomUUID() : String(Math.random()).slice(2))
    localStorage.setItem('kb_visitor_id', id)
  }
  return id
}

// Access 会话过期时抛出的错误类型，供调用方区分「登录过期」与「网络/离线」
export class LoginExpiredError extends Error {
  constructor(url) {
    super('登录已过期')
    this.name = 'LoginExpiredError'
    this.url = url
  }
}

// 统一封装需要登录的接口请求：自动识别 Access 302（重定向到登录页）与非 JSON 响应，
// 抛出 LoginExpiredError 让上层给出明确提示，而不是默默失败。
export async function fetchJson(url, init = {}) {
  const res = await fetch(url, init)
  // 两种可靠信号：① 跟随重定向后 res.redirected 为 true（被 Access 拦截）；
  // ② content-type 不是 application/json（拿到的是登录页 HTML）。
  const ct = res.headers.get('content-type') || ''
  if (res.redirected || !ct.includes('application/json')) {
    throw new LoginExpiredError(url)
  }
  if (!res.ok) throw new Error('HTTP ' + res.status)
  return res.json()
}

// 广播「登录已过期」，UI 层监听 kb-auth-expired 显示重新登录提示
export function notifyAuthExpired() {
  if (authNotified) return
  authNotified = true
  if (typeof window !== 'undefined') {
    window.dispatchEvent(new Event('kb-auth-expired'))
  }
}

export function getFavorites(force = false) {
  const fresh = cache && Date.now() - cacheAt < TTL
  if (!force && fresh) return Promise.resolve(cache)
  // 多个组件同时请求时复用同一个 in-flight promise，避免重复往返
  if (inflight) return inflight
  inflight = fetchJson('/api/favorites', { headers: { 'x-visitor-id': visitorId() } })
    .then((data) => {
      cache = Array.isArray(data) ? data : []
      cacheAt = Date.now()
      authNotified = false // 成功一次即可允许下次过期再提示
      return cache
    })
    .catch((err) => {
      if (err instanceof LoginExpiredError) notifyAuthExpired()
      // 离线或后端未绑定时保留旧缓存，避免界面闪烁
      cache = cache || []
      cacheAt = Date.now()
      return cache
    })
    .finally(() => { inflight = null })
  return inflight
}

// 收藏/取消收藏成功后调用，立即更新缓存，其他组件无需再发请求
export function setFavorites(list) {
  cache = Array.isArray(list) ? list : []
  cacheAt = Date.now()
}

export function currentVisitorId() {
  return visitorId()
}
