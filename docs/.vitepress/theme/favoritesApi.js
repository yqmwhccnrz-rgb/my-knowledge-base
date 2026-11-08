// 收藏数据的共享读取层。
// 之前 FavoriteButton 与 Favorites 在同一页面各发一次 /api/favorites，
// 切换笔记时又重复请求；而该接口走 Cloudflare Functions + KV，冷启动较慢。
// 这里做三件事：合并并发请求、SPA 会话内短时缓存、写操作后更新缓存。
let cache = null
let cacheAt = 0
let inflight = null
const TTL = 60 * 1000

function visitorId() {
  let id = localStorage.getItem('kb_visitor_id')
  if (!id) {
    id = 'v_' + (crypto.randomUUID ? crypto.randomUUID() : String(Math.random()).slice(2))
    localStorage.setItem('kb_visitor_id', id)
  }
  return id
}

export function getFavorites(force = false) {
  const fresh = cache && Date.now() - cacheAt < TTL
  if (!force && fresh) return Promise.resolve(cache)
  // 多个组件同时请求时复用同一个 in-flight promise，避免重复往返
  if (inflight) return inflight
  inflight = fetch('/api/favorites', { headers: { 'x-visitor-id': visitorId() } })
    .then((res) => (res.ok ? res.json() : []))
    .then((data) => {
      cache = Array.isArray(data) ? data : []
      cacheAt = Date.now()
      return cache
    })
    .catch(() => {
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
