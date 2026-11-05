<script setup>
import { ref, onMounted } from 'vue'

const KEY = 'kb_auth_v1'
const ACCOUNTS = [
  { user: 'friend', pass: 'kb2026' },
  { user: 'owner', pass: 'kb2026' }
]

const authed = ref(false)
const username = ref('')
const password = ref('')
const error = ref('')

onMounted(() => {
  authed.value = localStorage.getItem(KEY) === '1'
})

function login() {
  error.value = ''
  const ok = ACCOUNTS.some(
    (a) => a.user === username.value.trim() && a.pass === password.value
  )
  if (!ok) {
    error.value = '账号或口令不对，请再试一次'
    return
  }
  localStorage.setItem(KEY, '1')
  authed.value = true
}

function logout() {
  localStorage.removeItem(KEY)
  authed.value = false
}
</script>

<template>
  <div v-if="!authed" class="gate-screen">
    <div class="gate-card">
      <div class="gate-brand">
        <span class="gate-mark">K</span>
        <span>我的知识库</span>
      </div>
      <h1 class="gate-title">欢迎回来</h1>
      <p class="gate-desc">这里目前只对几位朋友开放，请输入账号和口令。</p>
      <form class="gate-form" @submit.prevent="login">
        <label>
          <span>账号</span>
          <input v-model="username" type="text" autocomplete="username" placeholder="请输入账号" />
        </label>
        <label>
          <span>口令</span>
          <input v-model="password" type="password" autocomplete="current-password" placeholder="请输入口令" />
        </label>
        <p v-if="error" class="gate-error">{{ error }}</p>
        <button type="submit" class="gate-btn">进入站点</button>
      </form>
      <p class="gate-foot">账号与口令请向站点主人索取</p>
    </div>
  </div>
  <template v-else>
    <slot />
    <button class="gate-logout" type="button" @click="logout">退出登录</button>
  </template>
</template>
