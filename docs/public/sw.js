const CACHE = 'kb-cache-v4'
const OFFLINE = '/offline.html'
const PRECACHE = ['/', '/offline.html', '/manifest.webmanifest', '/icon.svg']
// 音频/视频体积大且浏览器会用 Range 分段请求：不进离线缓存，交给网络原生处理，
// 否则会把 Cache Storage 撑满，还可能导致 206 分片播放异常。
const MEDIA_RE = /\.(m4a|mp3|wav|ogg|aac|flac|mp4|webm)$/i
// 不带内容 hash、但会随版本变化的静态资源：必须网络优先，否则「缓存优先」会让
// 用户永远拿到旧图标/旧 manifest/旧离线页，只能靠手动升 CACHE 版本才能刷新。
const FRESH_RE = /\/(icon\.svg|icon-192\.png|icon-512\.png|manifest\.webmanifest|offline\.html|register-sw\.js|sw\.js)$/
// 题库 / 听力 / 听写等数据 JSON：文件名固定无 hash，也走网络优先（在线取最新、
// 失败后回落旧缓存供离线使用），避免「缓存优先」让用户永远拿到旧数据。
const DATA_RE = /^\/data\//

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

  // 导航 HTML：网络优先，但【不写缓存】。否则登出后离线访问会回落到已登录的页面
  // 正文，绕过 Cloudflare Access 登录保护（共享设备 / 离线场景下的隐私泄露）。
  // 离线时直接回落到预缓存的离线页，宁可看不到内容也绝不泄露已登录数据。
  if (req.mode === 'navigate') {
    event.respondWith(
      fetch(req).catch(async () => {
        const offline = await caches.match(OFFLINE)
        return offline || Response.error()
      })
    )
    return
  }

  // 易变静态资源（图标 / manifest / 离线页 / sw 自身）：网络优先并写缓存，避免旧版本残留
  if (FRESH_RE.test(url.pathname)) {
    event.respondWith(
      fetch(req)
        .then((res) => {
          putInCache(req, res.clone())
          return res
        })
        .catch(() => caches.match(req))
    )
    return
  }

  // 数据 JSON（/data/*）：网络优先，成功写缓存供离线回退，但永远先问网络拿最新
  if (DATA_RE.test(url.pathname)) {
    event.respondWith(
      fetch(req)
        .then((res) => {
          putInCache(req, res.clone())
          return res
        })
        .catch(() => caches.match(req))
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
