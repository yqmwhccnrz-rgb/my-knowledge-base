<script setup>
import { ref, onMounted, onBeforeUnmount } from 'vue'

// 一级目录（左侧全部笔记）/ 二级目录（本页目录）宽度可拖拽调整。
// 相比旧版：抬高下限避免中文标题被压成竖排，放宽上限让字号变化有空间，
// 并始终把正文留在 CONTENT_MIN 以上，防止正文被固定目录栏挤没。
const SIDE_DEFAULT = 272
const OUTLINE_DEFAULT = 220
const SIDE_MIN = 210
const SIDE_MAX = 420
const OUTLINE_MIN = 180
const OUTLINE_MAX = 360
const CONTENT_MIN = 480
const MIN_VIEWPORT = 1280
// v2 独立存储：不读取旧版可能存在的极端窄栏值（旧 v1 由 LayoutFix 清理）
const STORE_KEY = 'kb-column-widths-v2'

const dragging = ref('')
const sideW = ref(SIDE_DEFAULT)
const outlineW = ref(OUTLINE_DEFAULT)
let startX = 0
let startSide = 0
let startOutline = 0

const clamp = (n, lo, hi) => Math.min(hi, Math.max(lo, n))
const maxSide = (o) => clamp(window.innerWidth - o - CONTENT_MIN, SIDE_MIN, SIDE_MAX)
const maxOutline = (s) => clamp(window.innerWidth - s - CONTENT_MIN, OUTLINE_MIN, OUTLINE_MAX)

function apply() {
  const root = document.documentElement.style
  root.setProperty('--kb-side-w', `${sideW.value}px`)
  root.setProperty('--kb-outline-w', `${outlineW.value}px`)
}

function save() {
  try {
    localStorage.setItem(
      STORE_KEY,
      JSON.stringify({ sideW: sideW.value, outlineW: outlineW.value })
    )
  } catch (e) {
    /* 隐私模式下忽略 */
  }
}

// 窗口变化或恢复旧设置时，把两列重新收进允许范围，避免挤掉正文
function revalidate() {
  if (window.innerWidth < MIN_VIEWPORT) return
  outlineW.value = clamp(outlineW.value, OUTLINE_MIN, maxOutline(sideW.value))
  sideW.value = clamp(sideW.value, SIDE_MIN, maxSide(outlineW.value))
  apply()
}

function start(e, which) {
  if (window.innerWidth < MIN_VIEWPORT || e.button > 0) return
  dragging.value = which
  startX = e.clientX
  startSide = sideW.value
  startOutline = outlineW.value
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
    sideW.value = clamp(startSide + dx, SIDE_MIN, maxSide(startOutline))
  } else {
    outlineW.value = clamp(startOutline + dx, OUTLINE_MIN, maxOutline(startSide))
  }
  apply()
}

function end() {
  if (!dragging.value) return
  dragging.value = ''
  document.body.classList.remove('kb-resizing')
  save()
  removeListeners()
}

// 双击分隔条恢复默认宽度
function reset() {
  sideW.value = SIDE_DEFAULT
  outlineW.value = OUTLINE_DEFAULT
  revalidate()
  apply()
  save()
}

function removeListeners() {
  window.removeEventListener('pointermove', move)
  window.removeEventListener('pointerup', end)
  window.removeEventListener('pointercancel', end)
}

function onResize() {
  revalidate()
}

onMounted(() => {
  try {
    const saved = JSON.parse(localStorage.getItem(STORE_KEY) || 'null')
    if (
      saved &&
      Number.isFinite(Number(saved.sideW)) &&
      Number.isFinite(Number(saved.outlineW))
    ) {
      sideW.value = Number(saved.sideW)
      outlineW.value = Number(saved.outlineW)
    }
  } catch (e) {
    /* 读取失败则用默认值 */
  }
  revalidate()
  apply()
  window.addEventListener('resize', onResize)
})

onBeforeUnmount(() => {
  removeListeners()
  window.removeEventListener('resize', onResize)
  document.body.classList.remove('kb-resizing')
})
</script>

<template>
  <div class="kb-resizers" :class="{ 'is-dragging': !!dragging }">
    <div
      class="kb-resizer kb-resizer-side"
      :class="{ active: dragging === 'sidebar' }"
      role="separator" aria-orientation="vertical" aria-label="调整全部目录宽度"
      title="拖动调整一级目录宽度 · 双击恢复默认"
      @pointerdown="start($event, 'sidebar')" @dblclick="reset"
    >
      <span class="kb-grip"></span>
      <span v-if="dragging === 'sidebar'" class="kb-width-tip">{{ sideW }}px</span>
    </div>
    <div
      class="kb-resizer kb-resizer-outline"
      :class="{ active: dragging === 'outline' }"
      role="separator" aria-orientation="vertical" aria-label="调整本页目录宽度"
      title="拖动调整二级目录宽度 · 双击恢复默认"
      @pointerdown="start($event, 'outline')" @dblclick="reset"
    >
      <span class="kb-grip"></span>
      <span v-if="dragging === 'outline'" class="kb-width-tip">{{ outlineW }}px</span>
    </div>
  </div>
</template>
