if ('serviceWorker' in navigator) {
  window.addEventListener('load', function () {
    navigator.serviceWorker
      .register('/sw.js')
      .then(function (reg) {
        // 检测到新版本 Service Worker 时，主动刷新页面以加载新内容
        // 这样已安装的 PWA App 打开时也能无缝更新，无需手动关掉重开
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
