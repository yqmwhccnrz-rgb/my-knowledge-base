<script setup>
import { nextTick, onBeforeUnmount, onMounted, watch } from 'vue'
import { useRoute } from 'vitepress'

// 宽度拖拽由 ColumnResizer.vue 负责（新存储 kb-column-widths-v2）。
// 本组件只做两件事：清除更早一版残留在本地的极端宽度值、去掉目录链接多余的原生 title 提示。
const LEGACY_STORE_KEY = 'kb-column-widths-v1'
const route = useRoute()
let observer = null

function stripTitles() {
  document.querySelectorAll('.VPDocAsideOutline .outline-link[title]')
    .forEach((el) => el.removeAttribute('title'))
}

function watchOutline() {
  if (observer) observer.disconnect()
  const target = document.querySelector('.VPDocAsideOutline')
  if (!target) return
  stripTitles()
  observer = new MutationObserver(stripTitles)
  observer.observe(target, { childList: true, subtree: true })
}

onMounted(() => {
  try {
    localStorage.removeItem(LEGACY_STORE_KEY)
  } catch (e) {
    /* 隐私模式下忽略 */
  }
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
