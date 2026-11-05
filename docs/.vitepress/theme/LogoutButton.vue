<script setup>
function logout() {
  if (!location.hostname.endsWith('.pages.dev')) {
    window.alert('退出登录只在正式网址上生效（本地预览没有 Cloudflare 登录）')
    return
  }
  window.location.assign('/cdn-cgi/access/logout')
}
</script>

<template>
  <button class="logout-btn" type="button" @click="logout">退出登录</button>
</template>
