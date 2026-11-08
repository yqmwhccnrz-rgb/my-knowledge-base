<script setup>
import { ref, onMounted, watch } from 'vue'
import { useData } from 'vitepress'

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

function visitorId() {
  let id = localStorage.getItem('kb_visitor_id')
  if (!id) {
    id = 'v_' + (crypto.randomUUID ? crypto.randomUUID() : String(Math.random()).slice(2))
    localStorage.setItem('kb_visitor_id', id)
  }
  return id
}

async function load() {
  const id = currentNoteId()
  noteId.value = id
  if (!id) return
  try {
    const res = await fetch('/api/favorites', { headers: { 'x-visitor-id': visitorId() } })
    if (res.ok) {
      const data = await res.json()
      favorited.value = Array.isArray(data) && data.includes(id)
    }
  } catch (e) {
    /* 离线或后端未绑定时静默忽略 */
  }
}

async function toggle() {
  if (!noteId.value || loading.value) return
  loading.value = true
  try {
    const res = await fetch('/api/favorites', {
      method: 'POST',
      headers: { 'content-type': 'application/json', 'x-visitor-id': visitorId() },
      body: JSON.stringify({ id: noteId.value, action: favorited.value ? 'remove' : 'add' })
    })
    if (res.ok) {
      const data = await res.json()
      favorited.value = Array.isArray(data.favorites) && data.favorites.includes(noteId.value)
      // 通知侧边栏收藏夹刷新
      window.dispatchEvent(new Event('kb-fav-changed'))
    }
  } catch (e) {
    /* 忽略 */
  } finally {
    loading.value = false
  }
}

onMounted(load)
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
</template>

<style scoped>
.kb-fav-btn {
  display: inline-flex;
  align-items: center;
  gap: 4px;
  margin: 4px 0 12px;
  padding: 5px 14px;
  font-size: 13px;
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
</style>
