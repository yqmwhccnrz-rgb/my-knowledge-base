const CACHE = 'kb-cache-v4'
const OFFLINE = '/offline.html'
const PRECACHE = ['/', '/offline.html', '/manifest.webmanifest', '/icon.svg']
// 音频/视频体积大且浏览器会用 Range 分段请求：不进离线缓存，交给网络原生处理，
// 否则会把 Cache Storage 撑满，还可能导致 206 分片播放异常。
const MEDIA_RE = /\.(m4a|mp3|wav|ogg|aac|flac|mp4|webm)$/i
// 不带内容 hash、但会随版本变化的静态资源：必须网络优先，否则「缓存优先」会让
// 用户永远拿到旧图标/旧 manifest/旧离线页，只能靠手动升 CACHE 版本才能刷新。
const FRESH_RE = /\/(icon\.svg|icon-192\.png|icon-512\.png|manifest\.webmanifest|offline\.html|register-sw\.js|sw\.js)$/

self.addEventListener('install', (event) => {
  event.waitUntil(
    caches.open(CACHE).then((c) => c.addAll(PRECACHE)).then(() => self.skipWaiting())
  )
})

self.addEventListener('activate', (event) => {
  event.waitUntil(
    caches.keys().then((keys) =>
      Promise.all(keys.filter((k) => k !== CACHE).map((k) => caches.delete(k)))
    ).then(() => self.clients.claim())
  )
})

// 前端检测到新版本时会发 SKIP_WAITING，这里必须真的处理
self.addEventListener('message', (event) => {
  if (event.data && event.data.type === 'SKIP_WAITING') self.skipWaiting()
})

self.addEventListener('fetch', (event) => {
  const req = event.request
  if (req.method !== 'GET') return
  const url = new URL(req.url)
  if (url.origin !== self.location.origin) return
  // 后端 API 不缓存，直接走网络
  if (url.pathname.startsWith('/api/')) return
  // 媒体资源不缓存（大文件 + Range 请求）
  if (MEDIA_RE.test(url.pathname)) return

  // 导航 HTML 与易变静态资源：网络优先，失败回落缓存（离线仍可用）
  if (req.mode === 'navigate' || FRESH_RE.test(url.pathname)) {
    event.respondWith(
      fetch(req)
        .then((res) => {
          putInCache(req, res.clone())
          return res
        })
        .catch(async () => {
          const cached = await caches.match(req)
          if (cached) return cached
          if (req.mode === 'navigate') {
            return (await caches.match(OFFLINE)) || Response.error()
          }
          return Response.error()
        })
    )
    return
  }

  // 带内容 hash 的构建资源：缓存优先，回退网络并写入缓存
  event.respondWith(
    caches.match(req).then(
      (cached) =>
        cached ||
        fetch(req)
          .then((res) => {
            putInCache(req, res.clone())
            return res
          })
          .catch(() => cached)
    )
  )
})

function putInCache(req, res) {
  if (res && res.status === 200 && res.type === 'basic') {
    caches.open(CACHE).then((c) => c.put(req, res))
  }
}
