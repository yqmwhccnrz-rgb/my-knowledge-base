// 本地预览不启用 Service Worker：dev 资源没有内容哈希，缓存旧 chunk 会导致
// 改了代码却看不到效果。正式站点（含 *.pages.dev）才注册。
const isLocal = /^(localhost|127\.0\.0\.1|\[::1\])$/.test(location.hostname)

if (isLocal && 'serviceWorker' in navigator) {
  navigator.serviceWorker.getRegistrations().then((regs) => {
    if (!regs.length) return
    Promise.all(regs.map((r) => r.unregister())).then(() => {
      if (!sessionStorage.getItem('kb-sw-dev-cleared')) {
        sessionStorage.setItem('kb-sw-dev-cleared', '1')
        window.location.reload()
      }
    })
  })
}

if (!isLocal && 'serviceWorker' in navigator) {
  window.addEventListener('load', function () {
    navigator.serviceWorker
      .register('/sw.js')
      .then(function (reg) {
        // 检测到新版本 Service Worker 时，主动刷新页面以加载新内容
        if (reg.waiting) {
          reg.waiting.postMessage({ type: 'SKIP_WAITING' })
        }
        reg.addEventListener('updatefound', function () {
          const newWorker = reg.installing
          if (newWorker) {
            newWorker.addEventListener('statechange', function () {
              if (newWorker.state === 'installed' && navigator.serviceWorker.controller) {
                newWorker.postMessage({ type: 'SKIP_WAITING' })
              }
            })
          }
        })
        // Service Worker 接管控制权后，刷新一次以使用最新资源
        let reloaded = false
        navigator.serviceWorker.addEventListener('controllerchange', function () {
          if (reloaded) return
          reloaded = true
          window.location.reload()
        })
      })
      .catch(function () {})
  })
}
