<template>
  <section class="hn">
    <div class="hn-head">
      <h2 class="hn-title">课程笔记</h2>
      <p class="hn-sub">左右滑动浏览，或点箭头 / 圆点切换（首尾相接循环）</p>
    </div>

    <div class="hn-stage">
      <button
        class="hn-arrow"
        type="button"
        :disabled="cards.length <= 1"
        aria-label="上一篇笔记"
        @click="prev"
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
        <!-- 首尾各放一张克隆卡片，实现无缝循环；真实卡片在中间 -->
        <div v-for="(c, i) in extended" :key="i" class="hn-slide">
          <a class="hn-card" :href="c.link" @click="onClickCard">
            <span class="hn-no">{{ String((i === 0 ? cards.length : (i === cards.length + 1 ? 1 : i))).padStart(2, '0') }}</span>
            <h3 class="hn-card-title">{{ c.title }}</h3>
            <p class="hn-card-details">{{ c.details }}</p>
            <span class="hn-card-link">{{ c.linkText || '阅读笔记' }} →</span>
          </a>
        </div>
      </div>

      <button
        class="hn-arrow"
        type="button"
        :disabled="cards.length <= 1"
        aria-label="下一篇笔记"
        @click="next"
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
        @click="goDot(i)"
      ></button>
    </div>
  </section>
</template>

<script setup>
import { ref, computed, nextTick, onMounted, onBeforeUnmount } from 'vue'

const props = defineProps({
  cards: { type: Array, default: () => [] }
})

const track = ref(null)
const index = ref(0)        // 真实卡片下标 0..n-1（圆点 / 判断用）
const extPos = ref(1)       // 扩展序列位置：1..n 为真实卡片，0=克隆末张，n+1=克隆首张
let settleTimer = null

const realCount = computed(() => props.cards.length)

// 扩展序列：[末张克隆, 0, 1, ..., n-1, 首张克隆]；单张时不克隆
const extended = computed(() => {
  const c = props.cards
  if (c.length <= 1) return c
  return [c[c.length - 1], ...c, c[0]]
})

function slideStep() {
  const el = track.value
  return el ? el.clientWidth : 0
}

// 扩展位置 → 真实下标（克隆位置映射到对应真实卡）
function realIndexOf(p) {
  const n = realCount.value
  if (p === 0) return n - 1
  if (p === n + 1) return 0
  return p - 1
}

function scrollToPos(p, smooth = true) {
  const el = track.value
  if (!el) return
  extPos.value = p
  index.value = realIndexOf(p)
  el.scrollTo({ left: p * slideStep(), behavior: smooth ? 'smooth' : 'auto' })
}

function next() {
  if (realCount.value <= 1) return
  scrollToPos(extPos.value + 1, true)
}
function prev() {
  if (realCount.value <= 1) return
  scrollToPos(extPos.value - 1, true)
}
function goDot(i) {
  if (realCount.value <= 1) return
  scrollToPos(i + 1, true)
}

function onScroll() {
  const el = track.value
  if (!el) return
  const step = slideStep()
  if (step <= 0) return
  const p = Math.round(el.scrollLeft / step)
  index.value = realIndexOf(p) // 实时高亮圆点

  // 滚动停止后，若停在克隆卡片上，瞬间跳回对应的真实卡片（内容相同，肉眼无感）
  clearTimeout(settleTimer)
  settleTimer = setTimeout(() => {
    const e = track.value
    if (!e) return
    const s = slideStep()
    const pp = Math.round(e.scrollLeft / s)
    const n = realCount.value
    if (pp === 0) {
      e.scrollTo({ left: n * s, behavior: 'auto' })
      extPos.value = n
      index.value = n - 1
    } else if (pp === n + 1) {
      e.scrollTo({ left: 1 * s, behavior: 'auto' })
      extPos.value = 1
      index.value = 0
    } else {
      extPos.value = pp
      index.value = pp - 1
    }
  }, 120)
}

// 滑动后松手再点击不应触发跳转，避免误触
let startX = 0
let isDown = false
const dragged = ref(false)
function onDown(e) { startX = e.clientX; isDown = true; dragged.value = false }
function onMove(e) { if (isDown && Math.abs(e.clientX - startX) > 8) dragged.value = true }
function onUp() { isDown = false; setTimeout(() => { dragged.value = false }, 0) }
function onClickCard(e) { if (dragged.value) { e.preventDefault(); e.stopPropagation() } }

onMounted(() => {
  nextTick(() => {
    if (track.value) {
      // 起始停在真实第一张（扩展位置 1），而非克隆首张
      track.value.scrollLeft = 1 * slideStep()
      extPos.value = 1
      index.value = 0
    }
  })
})

onBeforeUnmount(() => clearTimeout(settleTimer))
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
