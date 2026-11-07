const CACHE = 'kb-cache-v3'
const OFFLINE = '/offline.html'
const PRECACHE = ['/', '/offline.html', '/manifest.webmanifest', '/icon.svg']
// 音频/视频体积大且浏览器会用 Range 分段请求：不进离线缓存，交给网络原生处理，
// 否则会把 Cache Storage 撑满，还可能导致 206 分片播放异常。
const MEDIA_RE = /\.(m4a|mp3|wav|ogg|aac|flac|mp4|webm)$/i

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

// 只有带会话 cookie 的请求才允许读写缓存，避免未登录/已登出用户
// 从 Service Worker 缓存里读到已登录时才有的内容（内容泄露）。
function hasSession(req) {
  const c = req.headers.get('Cookie') || ''
  return /(^|;\s*)kb_sid=/.test(c)
}

self.addEventListener('fetch', (event) => {
  const req = event.request
  if (req.method !== 'GET') return
  const url = new URL(req.url)
  if (url.origin !== self.location.origin) return
  // 后端 API 不缓存，直接走网络
  if (url.pathname.startsWith('/api/')) return
  // 媒体资源不缓存（大文件 + Range 请求）
  if (MEDIA_RE.test(url.pathname)) return

  // 无会话：纯网络，不读不写缓存（安全优先）
  if (!hasSession(req)) {
    event.respondWith(fetch(req).catch(() => caches.match(OFFLINE)))
    return
  }

  if (req.mode === 'navigate') {
    event.respondWith(
      fetch(req)
        .then((res) => {
          putInCache(req, res.clone())
          return res
        })
        .catch(() => caches.match(req).then((r) => r || caches.match(OFFLINE)))
    )
    return
  }

  // 静态资源：缓存优先，回退网络并写入缓存
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
