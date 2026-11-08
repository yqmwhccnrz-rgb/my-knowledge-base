<script setup>
import { ref, onMounted, onBeforeUnmount, watch } from 'vue'
import { useData } from 'vitepress'
import {
  getFavorites,
  setFavorites,
  currentVisitorId,
  fetchJson,
  notifyAuthExpired,
  LoginExpiredError
} from './favoritesApi.js'

const { page } = useData()
const favorited = ref(false)
const loading = ref(false)
const noteId = ref('')

function currentNoteId() {
  const rp = page.value.relativePath || ''
  if (!rp.startsWith('notes/')) return ''
  return rp
    .replace(/^notes\//, '')
    .replace(/\.md$/, '')
    .replace(/\.html$/, '')
}

// 先同步确定 noteId 让按钮立即出现，再异步取收藏状态（命中共享缓存时几乎无等待）
async function load() {
  const id = currentNoteId()
  noteId.value = id
  if (!id) return
  const list = await getFavorites()
  favorited.value = list.includes(id)
}

async function toggle() {
  if (!noteId.value || loading.value) return
  loading.value = true
  try {
    const res = await fetchJson('/api/favorites', {
      method: 'POST',
      headers: { 'content-type': 'application/json', 'x-visitor-id': currentVisitorId() },
      body: JSON.stringify({ id: noteId.value, action: favorited.value ? 'remove' : 'add' })
    })
    const list = Array.isArray(res.favorites) ? res.favorites : []
    favorited.value = list.includes(noteId.value)
    // 更新共享缓存并通知侧边栏；两者都不需要再打后端
    setFavorites(list)
    window.dispatchEvent(new Event('kb-fav-changed'))
  } catch (e) {
    // 登录过期：给出明确提示；其他网络错误静默（不影响阅读）
    if (e instanceof LoginExpiredError) {
      notifyAuthExpired()
      authExpired.value = true
    }
  } finally {
    loading.value = false
  }
}

const authExpired = ref(false)
function relogin() {
  window.location.reload()
}
function onAuthExpired() {
  authExpired.value = true
}
onMounted(() => {
  load()
  window.addEventListener('kb-auth-expired', onAuthExpired)
})
onBeforeUnmount(() => window.removeEventListener('kb-auth-expired', onAuthExpired))
watch(() => page.value.relativePath, load)
</script>

<template>
  <button
    v-if="noteId"
    class="kb-fav-btn"
    :class="{ active: favorited }"
    :disabled="loading"
    @click="toggle"
    :title="favorited ? '取消收藏' : '收藏这篇笔记'"
  >
    {{ favorited ? '★ 已收藏' : '☆ 收藏' }}
  </button>
  <p v-if="authExpired" class="kb-auth-tip">
    登录已过期，<a href="#" @click.prevent="relogin">点此重新登录</a>后可继续收藏
  </p>
</template>

<style scoped>
.kb-fav-btn {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 4px;
  /* 尺寸交给外层 .kb-doc-actions 统一，这里不设 margin，避免与导出按钮基线错位 */
  margin: 0;
  height: 32px;
  box-sizing: border-box;
  padding: 0 14px;
  font-size: 13px;
  line-height: 1;
  white-space: nowrap;
  color: var(--vp-c-brand-1, #3f403f);
  background: var(--vp-c-default-soft, #f4f4f2);
  border: 1px solid var(--vp-c-brand-1, #3f403f);
  border-radius: 999px;
  cursor: pointer;
  transition: all 0.15s ease;
}
.kb-fav-btn:hover {
  background: var(--vp-c-brand-1, #3f403f);
  color: #fff;
}
.kb-fav-btn.active {
  background: var(--vp-c-brand-1, #3f403f);
  color: #fff;
}
.kb-fav-btn:disabled {
  opacity: 0.6;
  cursor: default;
}
.kb-auth-tip {
  margin: 6px 0 0;
  font-size: 12px;
  line-height: 1.4;
  color: var(--vp-c-text-2, #626463);
}
.kb-auth-tip a {
  color: var(--vp-c-brand-1, #3f403f);
  text-decoration: underline;
}
</style>
