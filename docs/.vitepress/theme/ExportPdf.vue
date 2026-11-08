<script setup>
import { ref, computed, onMounted, onBeforeUnmount, watch } from 'vue'
import { useData } from 'vitepress'

const { page } = useData()
const hint = ref(false)
let hintTimer = null
let savedTitle = ''
let busy = false
let printMQ = null

// 只在「笔记」页显示（docs/notes/*.md），首页/习题/听力页不显示
const isNote = computed(() => (page.value.relativePath || '').startsWith('notes/'))

// 打印时把页面标题换成笔记名：这样「另存为 PDF」默认文件名干净，页眉也显示笔记名
function cleanTitle() {
  if (savedTitle) return
  savedTitle = document.title
  const t = (page.value.title || '笔记').replace(/[\\/:*?"<>|]/g, '').trim()
  document.title = t || '笔记'
}
function restoreTitle() {
  if (!savedTitle) return
  document.title = savedTitle
  savedTitle = ''
}
function onPrintChange(e) {
  if (e.matches) cleanTitle()
  else restoreTitle()
}
function showHint() {
  hint.value = true
  clearTimeout(hintTimer)
  hintTimer = setTimeout(() => { hint.value = false }, 7000)
}

// 打印前确保所有矢量插图已解码，避免 PDF 中出现空白图
async function waitForImages() {
  const imgs = Array.from(document.querySelectorAll('.vp-doc img'))
  await Promise.all(imgs.map((img) => {
    if (img.complete && img.naturalWidth > 0) return Promise.resolve()
    if (typeof img.decode === 'function') return img.decode().catch(() => {})
    return new Promise((resolve) => {
      img.addEventListener('load', resolve, { once: true })
      img.addEventListener('error', resolve, { once: true })
    })
  }))
}

async function exportPdf() {
  if (busy) return
  busy = true
  showHint()
  try {
    await waitForImages()
    cleanTitle()
    window.print()
  } finally {
    busy = false
  }
}

onMounted(() => {
  window.addEventListener('beforeprint', cleanTitle)
  window.addEventListener('afterprint', restoreTitle)
  printMQ = window.matchMedia && window.matchMedia('print')
  if (printMQ && printMQ.addEventListener) printMQ.addEventListener('change', onPrintChange)
})
onBeforeUnmount(() => {
  window.removeEventListener('beforeprint', cleanTitle)
  window.removeEventListener('afterprint', restoreTitle)
  if (printMQ && printMQ.removeEventListener) printMQ.removeEventListener('change', onPrintChange)
  clearTimeout(hintTimer)
  restoreTitle()
})
// 切到别的笔记时重置标题标记，VitePress 会自行更新 document.title
watch(() => page.value.relativePath, () => { savedTitle = '' })
</script>

<template>
  <!-- 多根片段：按钮与提示条直接成为外层 .kb-doc-actions 的 flex 项，
       与「收藏」按钮共享同一基线行，避免嵌套容器导致错位 -->
  <template v-if="isNote">
    <button
      class="kb-export-btn"
      type="button"
      @click="exportPdf"
      title="把这篇笔记导出为 PDF（在打印窗口选择「另存为 PDF」）"
    >
      <svg viewBox="0 0 24 24" width="14" height="14" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
        <path d="M6 9V2h12v7" />
        <path d="M6 18H4a2 2 0 0 1-2-2v-5a2 2 0 0 1 2-2h16a2 2 0 0 1 2 2v5a2 2 0 0 1-2 2h-2" />
        <rect x="6" y="14" width="12" height="8" rx="1" />
      </svg>
      导出 PDF
    </button>
    <span v-if="hint" class="kb-export-hint" role="status">
      在打印窗口把「目标」选为 <b>另存为 PDF</b>；可取消勾选「页眉和页脚」让版面更干净
    </span>
  </template>
</template>

<style scoped>
.kb-export-btn {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 5px;
  /* 尺寸交给外层 .kb-doc-actions 统一，与「收藏」按钮完全一致 */
  margin: 0;
  height: 32px;
  box-sizing: border-box;
  padding: 0 14px;
  font-size: 13px;
  line-height: 1;
  color: var(--vp-c-brand-1, #3f403f);
  background: var(--vp-c-default-soft, #f4f4f2);
  border: 1px solid var(--vp-c-brand-1, #3f403f);
  border-radius: 999px;
  cursor: pointer;
  transition: all 0.15s ease;
  white-space: nowrap;
}
.kb-export-btn:hover {
  background: var(--vp-c-brand-1, #3f403f);
  color: #fff;
}
.kb-export-hint {
  /* 提示条占满整行，自动换到按钮下方，不挤歪按钮行 */
  flex-basis: 100%;
  margin: 0;
  font-size: 12px;
  line-height: 1.5;
  color: var(--vp-c-text-2, #626463);
  background: var(--vp-c-bg-soft, #f4f4f2);
  border: 1px solid var(--vp-c-divider, rgba(0,0,0,0.085));
  border-radius: 8px;
  padding: 6px 10px;
}
.kb-export-hint b {
  color: var(--vp-c-brand-1, #3f403f);
}
</style>
