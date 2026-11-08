<script setup>
import { ref, onMounted, onBeforeUnmount } from 'vue'

const deferredPrompt = ref(null)
const canInstall = ref(false)
const showHelp = ref(false)
// 已以独立 App 形式运行（已安装）时隐藏安装入口
const isStandalone = ref(false)

function onBeforeInstallPrompt(e) {
  // 拦截浏览器默认的小气泡，改由本站按钮统一触发
  e.preventDefault()
  deferredPrompt.value = e
  canInstall.value = true
}

function install() {
  if (deferredPrompt.value) {
    deferredPrompt.value.prompt()
    deferredPrompt.value.userChoice.finally(() => {
      deferredPrompt.value = null
      canInstall.value = false
    })
  } else {
    // 浏览器未提供安装提示（如 iOS Safari、已安装、或策略限制）→ 弹出图文指引
    showHelp.value = true
  }
}

function closeHelp() {
  showHelp.value = false
}

function onKeydown(e) {
  if (e.key === 'Escape' && showHelp.value) closeHelp()
}

onMounted(() => {
  window.addEventListener('beforeinstallprompt', onBeforeInstallPrompt)
  window.addEventListener('keydown', onKeydown)
  // 若已经以独立应用（standalone）模式运行，则隐藏安装入口
  const standalone =
    (window.matchMedia && window.matchMedia('(display-mode: standalone)').matches) ||
    window.navigator.standalone === true
  isStandalone.value = !!standalone
  if (standalone) canInstall.value = false
})

onBeforeUnmount(() => {
  window.removeEventListener('beforeinstallprompt', onBeforeInstallPrompt)
  window.removeEventListener('keydown', onKeydown)
})
</script>

<template>
  <div class="install-app">
    <button v-if="!isStandalone" class="install-btn" type="button" @click="install" title="将本站安装到手机或电脑桌面">
      <svg class="install-ico" viewBox="0 0 24 24" width="15" height="15" aria-hidden="true">
        <path
          fill="currentColor"
          d="M12 3a1 1 0 0 1 .7.3l4 4a1 1 0 0 1-1.4 1.4L13 6.42V15a1 1 0 1 1-2 0V6.41L8.7 8.7A1 1 0 0 1 7.3 7.3l4-4A1 1 0 0 1 12 3Zm-7 13a1 1 0 0 1 1 1v2h14v-2a1 1 0 1 1 2 0v3a1 1 0 0 1-1 1H4a1 1 0 0 1-1-1v-3a1 1 0 0 1 1-1Z"
        />
      </svg>
      <span>安装 App</span>
    </button>

    <div v-if="showHelp" class="install-mask" @click="closeHelp">
      <div class="install-modal" role="dialog" aria-modal="true" aria-label="将本站安装到设备" @click.stop>
        <h3 class="install-title">将本站安装到设备</h3>
        <p class="install-desc">
          本站是 PWA 应用，<strong>无需从应用商店下载</strong>。按下列方式即可像 App 一样使用：
        </p>

        <div class="install-block">
          <div class="install-sub">💻 电脑（Chrome / Edge）</div>
          <p>
            点击地址栏右侧的「安装」图标（⊕），或在浏览器右上角菜单中选择
            <strong>「安装 我的知识库」</strong>。
          </p>
        </div>

        <div class="install-block">
          <div class="install-sub">📱 iPhone / iPad（Safari）</div>
          <p>点底部「分享」按钮 → 选择 <strong>「添加到主屏幕」</strong> → 点「添加」。</p>
        </div>

        <div class="install-block">
          <div class="install-sub">🤖 安卓（Chrome）</div>
          <p>点右上角菜单 → <strong>「安装应用」</strong> 或「添加到主屏幕」。</p>
        </div>

        <button class="install-close" type="button" @click="closeHelp">知道了</button>
      </div>
    </div>
  </div>
</template>

<style scoped>
.install-app {
  display: inline-flex;
  align-items: center;
  margin-left: 8px;
}

.install-btn {
  display: inline-flex;
  align-items: center;
  gap: 5px;
  height: 32px;
  padding: 0 12px;
  font-size: 13px;
  font-weight: 500;
  color: #fff;
  background: var(--vp-c-brand-1, #3f403f);
  border: none;
  border-radius: 16px;
  cursor: pointer;
  transition: background 0.2s, transform 0.1s;
}

.install-btn:hover {
  background: var(--vp-c-brand-2, #5d5f5e);
}

.install-btn:active {
  transform: scale(0.96);
}

.install-ico {
  flex: none;
}

/* 弹窗 */
.install-mask {
  position: fixed;
  inset: 0;
  z-index: 1000;
  display: flex;
  align-items: center;
  justify-content: center;
  background: rgba(0, 0, 0, 0.45);
  padding: 16px;
}

.install-modal {
  width: 100%;
  max-width: 420px;
  background: #fff;
  border-radius: 12px;
  padding: 22px 22px 18px;
  box-shadow: 0 12px 40px rgba(0, 0, 0, 0.25);
  color: #2e2f2e;
}

.install-title {
  margin: 0 0 8px;
  font-size: 18px;
  font-weight: 600;
}

.install-desc {
  margin: 0 0 14px;
  font-size: 13px;
  line-height: 1.6;
  color: #555;
}

.install-block {
  margin-bottom: 12px;
  padding: 10px 12px;
  background: #f4f4f2;
  border-radius: 8px;
}

.install-block p {
  margin: 4px 0 0;
  font-size: 13px;
  line-height: 1.6;
  color: #444;
}

.install-sub {
  font-size: 14px;
  font-weight: 600;
  color: var(--vp-c-brand-1, #3f403f);
}

.install-close {
  display: block;
  width: 100%;
  height: 38px;
  margin-top: 6px;
  font-size: 14px;
  font-weight: 500;
  color: #fff;
  background: var(--vp-c-brand-1, #3f403f);
  border: none;
  border-radius: 8px;
  cursor: pointer;
}

.install-close:hover {
  background: var(--vp-c-brand-2, #5d5f5e);
}

/* 窄屏：按钮文字隐藏，仅留图标，避免挤压导航 */
@media (max-width: 768px) {
  .install-btn span {
    display: none;
  }
  .install-btn {
    padding: 0 9px;
  }
}
</style>
