<script setup>
import { ref, computed, onMounted, onBeforeUnmount } from 'vue'
import { useData, useRouter } from 'vitepress'

const { theme } = useData()
const router = useRouter()
const favIds = ref([])

function visitorId() {
  let id = localStorage.getItem('kb_visitor_id')
  if (!id) {
    id = 'v_' + (crypto.randomUUID ? crypto.randomUUID() : String(Math.random()).slice(2))
    localStorage.setItem('kb_visitor_id', id)
  }
  return id
}

// 从主题配置的 sidebar 中提取 笔记ID -> { 标题, 链接 }
// 这样新增笔记时收藏夹会自动同步，无需手改
const noteMap = computed(() => {
  const map = {}
  const sb = theme.value && theme.value.sidebar
  if (Array.isArray(sb)) {
    for (const group of sb) {
      const items = group.items || []
      for (const it of items) {
        const m = String(it.link || '').match(/\/notes\/([^/]+)\.html$/)
        if (m) map[m[1]] = { id: m[1], title: it.text, link: it.link }
      }
    }
  }
  return map
})

const favList = computed(() =>
  favIds.value.map((id) => noteMap.value[id]).filter(Boolean)
)

async function load() {
  try {
    const res = await fetch('/api/favorites', {
      headers: { 'x-visitor-id': visitorId() }
    })
    if (res.ok) {
      const data = await res.json()
      favIds.value = Array.isArray(data) ? data : []
    }
  } catch (e) {
    /* 离线或后端未绑定时忽略，列表为空 */
  }
}

function go(link) {
  router.go(link)
}

function onChange() {
  load()
}

onMounted(() => {
  load()
  window.addEventListener('kb-fav-changed', onChange)
})
onBeforeUnmount(() => window.removeEventListener('kb-fav-changed', onChange))
</script>

<template>
  <div class="kb-fav-box">
    <div class="kb-fav-head">★ 收藏夹</div>
    <ul v-if="favList.length" class="kb-fav-list">
      <li v-for="f in favList" :key="f.id">
        <a :href="f.link" @click.prevent="go(f.link)">{{ f.title }}</a>
      </li>
    </ul>
    <p v-else class="kb-fav-empty">暂无收藏，点笔记页「☆ 收藏」即可加入</p>
  </div>
</template>

<style scoped>
.kb-fav-box {
  margin: 0 0 16px;
  padding: 10px 12px;
  background: var(--vp-c-bg-soft, #f6f8fc);
  border: 1px solid var(--vp-c-divider, #e2e6ef);
  border-radius: 10px;
  box-sizing: border-box;
  max-width: 100%;
  overflow-wrap: anywhere;
}

.kb-fav-head {
  /* 随一级目录宽度收敛，拖窄时不拥挤、拖宽时同步变大 */
  font-size: clamp(11.5px, calc(8px + var(--kb-side-w) * 0.017), 14.5px);
  font-weight: 600;
  color: var(--vp-c-brand-1, #3451b2);
  margin-bottom: 6px;
}

.kb-fav-list {
  list-style: none;
  margin: 0;
  padding: 0;
}

.kb-fav-list li {
  margin: 2px 0;
}

.kb-fav-list a {
  display: block;
  padding: 5px 8px;
  font-size: clamp(11.5px, calc(8px + var(--kb-side-w) * 0.017), 14.5px);
  color: var(--vp-c-text-1, #1f2328);
  text-decoration: none;
  overflow-wrap: anywhere;
  border-radius: 6px;
  transition: background 0.15s, color 0.15s;
}

.kb-fav-list a:hover {
  background: var(--vp-c-brand-1, #3451b2);
  color: #fff;
}

.kb-fav-empty {
  margin: 0;
  font-size: clamp(11px, calc(7.5px + var(--kb-side-w) * 0.015), 13.5px);
  line-height: 1.5;
  color: var(--vp-c-text-2, #8a8f98);
}
</style>
