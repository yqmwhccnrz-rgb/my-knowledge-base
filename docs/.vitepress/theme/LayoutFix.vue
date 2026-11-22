<script setup>
import { nextTick, onBeforeUnmount, onMounted, watch } from 'vue'
import { useRoute } from 'vitepress'

// 宽度拖拽由 ColumnResizer.vue 负责（新存储 kb-column-widths-v2）。
// 本组件做三件事：清除更早一版残留在本地的极端宽度值、去掉目录链接多余的原生 title
// 提示、补两处 Lighthouse 可访问性缺陷（首页缺 main 地标、表格缺行表头）。
const LEGACY_STORE_KEY = 'kb-column-widths-v1'
const route = useRoute()
let observer = null

function stripTitles() {
  document.querySelectorAll('.VPDocAsideOutline .outline-link[title]')
    .forEach((el) => el.removeAttribute('title'))
}

function fixSemantics() {
  // VitePress 首页布局没有 <main>，补 landmark（role="main"）
  const home = document.querySelector('.VPHome')
  if (home) home.setAttribute('role', 'main')
  // markdown 表格 tbody 首列是非空数据格时补 scope="row"，建立行表头关联
  document.querySelectorAll('.vp-doc table tbody tr').forEach((tr) => {
    const td = tr.querySelector('td')
    if (td && td.textContent.trim() && !td.hasAttribute('scope')) td.setAttribute('scope', 'row')
  })
}

function watchOutline() {
  if (observer) observer.disconnect()
  const target = document.querySelector('.VPDocAsideOutline')
  stripTitles()
  fixSemantics()
  if (!target) return
  observer = new MutationObserver(() => { stripTitles(); fixSemantics() })
  observer.observe(target, { childList: true, subtree: true })
}

onMounted(() => {
  try {
    localStorage.removeItem(LEGACY_STORE_KEY)
  } catch (e) {
    /* 隐私模式下忽略 */
  }
  fixSemantics()
  watchOutline()
})

watch(() => route.path, () => nextTick(watchOutline))

onBeforeUnmount(() => {
  if (observer) observer.disconnect()
})
</script>

<template>
  <span aria-hidden="true" style="display: none"></span>
</template>
