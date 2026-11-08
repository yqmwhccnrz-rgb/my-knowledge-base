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
        // 仅当「已有旧 SW 被新版本替换」时才刷新；首次接管（原本没有 controller）
        // 页面用的就是最新资源，无需刷新——以前这里会在首次进入时整页 reload 一次，
        // 造成「登进去慢/闪一下」。另外在答题/听写页不自动刷新，避免丢失未保存的作答。
        let reloaded = false
        const hadController = !!navigator.serviceWorker.controller
        navigator.serviceWorker.addEventListener('controllerchange', function () {
          if (reloaded || !hadController) return
          if (document.querySelector('.quiz, .dict-wrap, .listen')) return
          reloaded = true
          window.location.reload()
        })
      })
      .catch(function () {})
  })
}
