<script setup>
import { computed } from 'vue'
import { useRoute } from 'vitepress'

const route = useRoute()
const isNote = computed(() => route.path.startsWith('/notes/'))
const name = computed(() => {
  const clean = route.path.replace(/\.html$/, '').replace(/\/$/, '')
  return clean.split('/').pop() || ''
})
</script>

<template>
  <div v-if="isNote" class="original-box">
    <p class="ob-title">原文保留</p>
    <a :href="`/originals/${name}.md`" target="_blank" rel="noopener">查看 Markdown 原文</a>
    <a :href="`/originals/${name}.md`" :download="`${name}.md`">下载原文</a>
  </div>
</template>
