<template>
  <section class="hn">
    <div class="hn-head">
      <h2 class="hn-title">课程笔记</h2>
      <p class="hn-sub">左右滑动浏览，或点箭头 / 圆点切换</p>
    </div>

    <div class="hn-stage">
      <button
        class="hn-arrow"
        type="button"
        :disabled="index <= 0"
        aria-label="上一篇笔记"
        @click="go(index - 1)"
      >‹</button>

      <div
        ref="track"
        class="hn-track"
        @scroll.passive="onScroll"
        @pointerdown="onDown"
        @pointermove="onMove"
        @pointerup="onUp"
        @pointercancel="onUp"
      >
        <div v-for="(c, i) in cards" :key="i" class="hn-slide">
          <a
            class="hn-card"
            :href="c.link"
            @click="onClickCard"
          >
            <span class="hn-no">{{ String(i + 1).padStart(2, '0') }}</span>
            <h3 class="hn-card-title">{{ c.title }}</h3>
            <p class="hn-card-details">{{ c.details }}</p>
            <span class="hn-card-link">{{ c.linkText || '阅读笔记' }} →</span>
          </a>
        </div>
      </div>

      <button
        class="hn-arrow"
        type="button"
        :disabled="index >= cards.length - 1"
        aria-label="下一篇笔记"
        @click="go(index + 1)"
      >›</button>
    </div>

    <div class="hn-dots">
      <button
        v-for="(c, i) in cards"
        :key="'d' + i"
        class="hn-dot"
        type="button"
        :class="{ active: i === index }"
        :aria-label="'第 ' + (i + 1) + ' 张'"
        @click="go(i)"
      ></button>
    </div>
  </section>
</template>

<script setup>
import { ref, nextTick, onMounted } from 'vue'

const props = defineProps({
  cards: { type: Array, default: () => [] }
})

const track = ref(null)
const index = ref(0)
const dragged = ref(false)
let startX = 0
let isDown = false

function slideStep() {
  const el = track.value
  if (!el) return el ? el.clientWidth : 0
  return el.clientWidth
}

function go(i) {
  const max = props.cards.length - 1
  i = Math.max(0, Math.min(max, i))
  index.value = i
  const el = track.value
  if (el) el.scrollTo({ left: i * slideStep(), behavior: 'smooth' })
}

function onScroll() {
  const el = track.value
  if (!el) return
  const step = slideStep()
  if (step > 0) {
    const idx = Math.round(el.scrollLeft / step)
    index.value = Math.max(0, Math.min(props.cards.length - 1, idx))
  }
}

// 滑动后松手再点击不应触发跳转，避免误触
function onDown(e) {
  startX = e.clientX
  isDown = true
  dragged.value = false
}
function onMove(e) {
  if (isDown && Math.abs(e.clientX - startX) > 8) dragged.value = true
}
function onUp() {
  isDown = false
  setTimeout(() => { dragged.value = false }, 0)
}
function onClickCard(e) {
  if (dragged.value) {
    e.preventDefault()
    e.stopPropagation()
  }
}

onMounted(() => {
  nextTick(() => {
    if (track.value) track.value.scrollLeft = 0
  })
})
</script>

<style scoped>
.hn {
  max-width: 960px;
  margin: 0 auto;
  padding: 8px 0 16px;
  box-sizing: border-box;
}

.hn-head {
  text-align: center;
  padding: 0 16px;
  margin-bottom: 16px;
}
.hn-title {
  margin: 0;
  font-size: 22px;
  font-weight: 600;
  color: var(--vp-c-text-1);
}
.hn-sub {
  margin: 6px 0 0;
  font-size: 13px;
  color: var(--vp-c-text-2);
}

.hn-stage {
  display: flex;
  align-items: center;
  gap: 8px;
}

.hn-arrow {
  flex: 0 0 auto;
  width: 40px;
  height: 40px;
  border-radius: 50%;
  border: 1px solid var(--vp-c-divider);
  background: var(--vp-c-bg);
  color: var(--vp-c-text-1);
  font-size: 22px;
  line-height: 1;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: border-color 0.2s, color 0.2s, background 0.2s;
}
.hn-arrow:hover:not(:disabled) {
  border-color: var(--vp-c-brand-1);
  color: var(--vp-c-brand-1);
}
.hn-arrow:disabled {
  opacity: 0.35;
  cursor: default;
}

.hn-track {
  flex: 1 1 auto;
  display: flex;
  overflow-x: auto;
  scroll-snap-type: x mandatory;
  scroll-behavior: smooth;
  -webkit-overflow-scrolling: touch;
  /* 隐藏滚动条，保持轮播纯净 */
  scrollbar-width: none;
}
.hn-track::-webkit-scrollbar {
  display: none;
}

.hn-slide {
  flex: 0 0 100%;
  scroll-snap-align: center;
  display: flex;
  justify-content: center;
  padding: 4px 14px;
  box-sizing: border-box;
}

.hn-card {
  display: block;
  width: 100%;
  max-width: 460px;
  box-sizing: border-box;
  padding: 24px 22px;
  background: var(--vp-c-bg);
  border: 1px solid var(--vp-c-divider);
  border-radius: 14px;
  text-decoration: none;
  color: inherit;
  transition: border-color 0.2s, box-shadow 0.2s, transform 0.2s;
}
.hn-card:hover {
  border-color: var(--vp-c-brand-1);
  box-shadow: 0 6px 20px rgba(0, 0, 0, 0.06);
  transform: translateY(-2px);
}

.hn-no {
  display: inline-block;
  font-size: 12px;
  font-weight: 600;
  letter-spacing: 0.06em;
  color: var(--vp-c-brand-1);
  background: var(--vp-c-bg-soft);
  border-radius: 6px;
  padding: 2px 8px;
  margin-bottom: 12px;
}
.hn-card-title {
  margin: 0 0 10px;
  font-size: 18px;
  font-weight: 600;
  color: var(--vp-c-text-1);
}
.hn-card-details {
  margin: 0 0 16px;
  font-size: 14px;
  line-height: 1.7;
  color: var(--vp-c-text-2);
}
.hn-card-link {
  font-size: 13px;
  font-weight: 600;
  color: var(--vp-c-brand-1);
}

.hn-dots {
  display: flex;
  justify-content: center;
  gap: 8px;
  margin-top: 18px;
}
.hn-dot {
  width: 8px;
  height: 8px;
  padding: 0;
  border: none;
  border-radius: 50%;
  background: var(--vp-c-divider);
  cursor: pointer;
  transition: background 0.2s, transform 0.2s;
}
.hn-dot.active {
  background: var(--vp-c-brand-1);
  transform: scale(1.25);
}

@media (max-width: 480px) {
  .hn-arrow {
    width: 34px;
    height: 34px;
    font-size: 18px;
  }
  .hn-card {
    padding: 20px 18px;
  }
}
</style>
