<script setup>
import { ref, onMounted } from 'vue'

const email = ref('')
const busy = ref(false)

onMounted(async () => {
  try {
    const r = await fetch('/api/auth/me', { credentials: 'same-origin' })
    if (r.ok) {
      const data = await r.json()
      email.value = data.email || ''
    }
  } catch {
    /* 忽略：会话可能刚过期 */
  }
})

async function logout() {
  if (busy.value) return
  busy.value = true
  try {
    await fetch('/api/auth/logout', { method: 'POST', credentials: 'same-origin' })
  } catch {
    /* 忽略网络错误，仍跳转 */
  }
  // 清除 Service Worker 缓存，避免登出后从缓存读到已登录内容
  if ('caches' in window) {
    try {
      const names = await caches.keys()
      await Promise.all(names.map((n) => caches.delete(n)))
    } catch {}
  }
  window.location.assign('/')
}
</script>

<template>
  <button class="logout-btn" type="button" :disabled="busy" @click="logout">
    退出登录<span v-if="email"> · {{ email }}</span>
  </button>
</template>
