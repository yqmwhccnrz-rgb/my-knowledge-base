<script setup>
import { ref, onMounted, onBeforeUnmount, watch, nextTick } from 'vue'
import { useRoute } from 'vitepress'

const SIDE_DEFAULT = 272
const OUTLINE_DEFAULT = 220
const SIDE_MIN = 150
const SIDE_MAX = 340
const OUTLINE_MIN = 170
const OUTLINE_MAX = 340
const CONTENT_MIN = 440
const MIN_VIEWPORT = 1280
const STORE_KEY = 'kb-column-widths-v1'

const dragging = ref('')
let sideW = SIDE_DEFAULT
let outlineW = OUTLINE_DEFAULT
let startX = 0
let startSide = 0
let startOutline = 0

const clamp = (n, lo, hi) => Math.min(hi, Math.max(lo, n))
const maxSide = (o) => clamp(window.innerWidth - o - CONTENT_MIN, SIDE_MIN, SIDE_MAX)
const maxOutline = (s) => clamp(window.innerWidth - s - CONTENT_MIN, OUTLINE_MIN, OUTLINE_MAX)

function apply() {
  const r = document.documentElement
  r.style.setProperty('--kb-side-w', `${sideW}px`)
  r.style.setProperty('--kb-outline-w', `${outlineW}px`)
}

function save() {
  try {
    localStorage.setItem(STORE_KEY, JSON.stringify({ sideW, outlineW }))
  } catch (e) {
    /* 隐私模式下忽略 */
  }
}

// 窗口变化或恢复旧设置时，重新把两列收进允许范围，避免挤掉正文
function revalidate() {
  if (window.innerWidth < MIN_VIEWPORT) return
  outlineW = clamp(outlineW, OUTLINE_MIN, maxOutline(sideW))
  sideW = clamp(sideW, SIDE_MIN, maxSide(outlineW))
  apply()
}

function start(e, which) {
  if (window.innerWidth < MIN_VIEWPORT) return
  dragging.value = which
  startX = e.clientX
  startSide = sideW
  startOutline = outlineW
  document.body.classList.add('kb-resizing')
  e.preventDefault()
  window.addEventListener('pointermove', move)
  window.addEventListener('pointerup', end)
  window.addEventListener('pointercancel', end)
}

function move(e) {
  if (!dragging.value) return
  const dx = e.clientX - startX
  if (dragging.value === 'sidebar') {
    sideW = clamp(startSide + dx, SIDE_MIN, maxSide(startOutline))
  } else {
    outlineW = clamp(startOutline + dx, OUTLINE_MIN, maxOutline(startSide))
  }
  apply()
}

function end() {
  if (!dragging.value) return
  dragging.value = ''
  document.body.classList.remove('kb-resizing')
  save()
  window.removeEventListener('pointermove', move)
  window.removeEventListener('pointerup', end)
  window.removeEventListener('pointercancel', end)
}

function reset() {
  sideW = SIDE_DEFAULT
  outlineW = OUTLINE_DEFAULT
  revalidate()
  apply()
  save()
}

// VitePress 默认给目录链接加 title，悬停会弹出黑色原生提示；标题现在完整换行，不需要它
const route = useRoute()
let outlineObserver = null
function stripTitles() {
  document.querySelectorAll('.VPDocAsideOutline .outline-link[title]')
    .forEach((el) => el.removeAttribute('title'))
}
function watchOutline() {
  if (outlineObserver) outlineObserver.disconnect()
  const target = document.querySelector('.VPDocAsideOutline')
  if (!target) return
  stripTitles()
  outlineObserver = new MutationObserver(stripTitles)
  outlineObserver.observe(target, { childList: true, subtree: true })
}
watch(() => route.path, () => nextTick(watchOutline))

function onResize() {
  revalidate()
}

onMounted(() => {
  try {
    const saved = JSON.parse(localStorage.getItem(STORE_KEY) || 'null')
    if (saved) {
      sideW = Number(saved.sideW) || SIDE_DEFAULT
      outlineW = Number(saved.outlineW) || OUTLINE_DEFAULT
    }
  } catch (e) {
    /* 读取失败则用默认值 */
  }
  revalidate()
  apply()
  watchOutline()
  window.addEventListener('resize', onResize)
})

onBeforeUnmount(() => {
  if (outlineObserver) outlineObserver.disconnect()
  window.removeEventListener('resize', onResize)
  window.removeEventListener('pointermove', move)
  window.removeEventListener('pointerup', end)
  window.removeEventListener('pointercancel', end)
  document.body.classList.remove('kb-resizing')
})
</script>

<template>
  <div class="kb-resizers" :class="{ 'is-dragging': dragging }">
    <div
      class="kb-resizer kb-resizer-side"
      :class="{ active: dragging === 'sidebar' }"
      role="separator" aria-orientation="vertical" aria-label="调整全部目录宽度"
      title="拖动调整宽度 · 双击恢复默认"
      @pointerdown="start($event, 'sidebar')" @dblclick="reset"
    ><span></span></div>
    <div
      class="kb-resizer kb-resizer-outline"
      :class="{ active: dragging === 'outline' }"
      role="separator" aria-orientation="vertical" aria-label="调整本页目录宽度"
      title="拖动调整宽度 · 双击恢复默认"
      @pointerdown="start($event, 'outline')" @dblclick="reset"
    ><span></span></div>
  </div>
</template>
