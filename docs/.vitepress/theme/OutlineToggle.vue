<script setup>
import { ref, onMounted } from 'vue'

// 二级目录（本页目录）收起 / 展开。
// 状态挂在 <html> 的 class 上，CSS 直接读取；不改 ColumnResizer 写入的
// --kb-side-w / --kb-outline-w 变量，所以展开后能恢复用户拖好的宽度。
const STORE_KEY = 'kb-outline-collapsed'
const collapsed = ref(false)

function apply() {
  document.documentElement.classList.toggle('kb-outline-collapsed', collapsed.value)
}

function toggle() {
  collapsed.value = !collapsed.value
  apply()
  try {
    localStorage.setItem(STORE_KEY, collapsed.value ? '1' : '0')
  } catch (e) {
    /* 隐私模式下忽略 */
  }
}

onMounted(() => {
  try {
    collapsed.value = localStorage.getItem(STORE_KEY) === '1'
  } catch (e) {
    /* 读取失败则默认展开 */
  }
  apply()
})
</script>

<template>
  <button
    class="kb-outline-toggle"
    type="button"
    :aria-expanded="!collapsed"
    :aria-label="collapsed ? '展开本页目录' : '收起本页目录'"
    :title="collapsed ? '展开本页目录' : '收起本页目录'"
    @click="toggle"
  >
    <span aria-hidden="true">{{ collapsed ? '›' : '‹' }}</span>
  </button>
</template>
