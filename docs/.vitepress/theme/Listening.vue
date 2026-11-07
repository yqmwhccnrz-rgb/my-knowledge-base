<script setup>
import { ref, reactive, computed, watch, onMounted, onBeforeUnmount } from 'vue'

const bank = ref([])
const ready = ref(false)

const STORE_KEY = 'listen:filter'

onMounted(async () => {
  const mod = await import('./data/listening.json')
  bank.value = mod.default
  // 恢复上次浏览的章节 / 分段
  try {
    const saved = JSON.parse(localStorage.getItem(STORE_KEY) || 'null')
    if (saved && Number.isInteger(saved.c) && saved.c < groups.value.length) {
      activeChapter.value = saved.c
      activePart.value =
        Number.isInteger(saved.p) && saved.p < parts.value.length ? saved.p : 0
    }
  } catch (e) {}
  ready.value = true
})

// ---------- 分组（按章节保持顺序） ----------
const groups = computed(() => {
  const out = []
  const idx = new Map()
  for (const it of bank.value) {
    if (!idx.has(it.chapter)) {
      idx.set(it.chapter, out.length)
      out.push({ chapter: it.chapter, items: [] })
    }
    out[idx.get(it.chapter)].items.push(it)
  }
  return out
})

// ---------- 章节 / 分段筛选 ----------
const activeChapter = ref(0)
const activePart = ref(0)
const playingId = ref(null) // 当前聚焦的音频（暂停时也保留，便于高亮停在暂停处）
const isPlaying = ref(false)
const audios = new Map()
const states = reactive({}) // id -> { time, dur }

const parts = computed(() => {
  const g = groups.value[activeChapter.value]
  if (!g) return []
  const n = g.items.length
  const size = 3
  const out = []
  for (let i = 0; i < n; i += size) {
    const end = Math.min(i + size, n)
    const label = i + 1 === end ? `${end}` : `${i + 1}–${end}`
    out.push({ label, start: i, items: g.items.slice(i, end) })
  }
  return out
})

const currentChapter = computed(() => groups.value[activeChapter.value] || null)
const currentPart = computed(() => parts.value[activePart.value] || null)
const currentItems = computed(() => (currentPart.value ? currentPart.value.items : []))
const chapterShort = (name) => (name || '').split(' ')[0]

function stopAll() {
  audios.forEach((a) => a.pause())
  playingId.value = null
  isPlaying.value = false
}

function pickChapter(i) {
  if (i === activeChapter.value) return
  stopAll()
  activeChapter.value = i
  activePart.value = 0
}

function pickPart(i) {
  if (i === activePart.value) return
  stopAll()
  activePart.value = i
}

watch([activeChapter, activePart], () => {
  try {
    localStorage.setItem(
      STORE_KEY,
      JSON.stringify({ c: activeChapter.value, p: activePart.value })
    )
  } catch (e) {}
})

// ---------- 音频播放 ----------
function audioFor(it) {
  let a = audios.get(it.id)
  if (a) return a
  a = new Audio(it.audio)
  a.preload = 'metadata'
  if (!states[it.id]) states[it.id] = { time: 0, dur: 0 }
  a.addEventListener('loadedmetadata', () => {
    states[it.id].dur = a.duration || 0
  })
  a.addEventListener('timeupdate', () => {
    states[it.id].time = a.currentTime || 0
  })
  a.addEventListener('ended', () => {
    if (playingId.value === it.id) isPlaying.value = false
  })
  audios.set(it.id, a)
  return a
}

function toggle(it) {
  const a = audioFor(it)
  if (playingId.value === it.id) {
    if (isPlaying.value) {
      a.pause()
      isPlaying.value = false
    } else {
      a.play().catch(() => {})
      isPlaying.value = true
    }
    return
  }
  audios.forEach((x) => x.pause())
  playingId.value = it.id
  a.play().catch(() => {})
  isPlaying.value = true
}

function seek(it, ev) {
  const a = audioFor(it)
  const dur = a.duration || 0
  if (!dur) return
  const r = ev.currentTarget.getBoundingClientRect()
  const p = Math.min(1, Math.max(0, (ev.clientX - r.left) / r.width))
  a.currentTime = p * dur
  states[it.id].time = a.currentTime
}

// 进度条支持键盘：左右方向键 ±5 秒（按住 Shift 为 ±10 秒），Home/End 跳到首尾
function onTrackKey(it, ev) {
  const a = audioFor(it)
  if (!a.duration) return
  const step = ev.shiftKey ? 10 : 5
  if (ev.key === 'ArrowRight') a.currentTime = Math.min(a.duration, a.currentTime + step)
  else if (ev.key === 'ArrowLeft') a.currentTime = Math.max(0, a.currentTime - step)
  else if (ev.key === 'Home') a.currentTime = 0
  else if (ev.key === 'End') a.currentTime = a.duration
  else return
  ev.preventDefault()
  states[it.id].time = a.currentTime
}

function fmt(s) {
  if (!s || isNaN(s)) return '0:00'
  const m = Math.floor(s / 60)
  const sec = Math.floor(s % 60)
  return `${m}:${String(sec).padStart(2, '0')}`
}

function progress(it) {
  const st = states[it.id]
  if (!st || !st.dur) return 0
  return Math.min(100, (st.time / st.dur) * 100)
}

// 进入某个分段后预取元数据，让总时长立即显示出来；
// 同时释放上一段的音频对象，避免长音频（第5章单段约 27 分钟）长期占用内存
watch(
  currentItems,
  (items) => {
    const keep = new Set(items.map((x) => x.id))
    for (const [id, a] of audios) {
      if (keep.has(id)) continue
      a.pause()
      a.removeAttribute('src')
      a.load()
      audios.delete(id)
    }
    for (const it of items) audioFor(it)
  },
  { immediate: true }
)

// ---------- 题目 / 听力原文 / 中文翻译 显示隐藏 ----------
const qOpen = reactive({}) // id -> bool，默认隐藏
const enOpen = reactive({}) // id -> bool，默认隐藏
const zhOpen = reactive({}) // id -> bool，默认隐藏

const isQOpen = (id) => qOpen[id] === true

const allZhOn = computed(
  () => currentItems.value.length > 0 && currentItems.value.every((it) => zhOpen[it.id])
)

function toggleQ(id) {
  qOpen[id] = !isQOpen(id)
}

function toggleEn(id) {
  enOpen[id] = !enOpen[id]
}

// ---------- 逐句跟读高亮 ----------
function itemById(id) {
  return bank.value.find((x) => x.id === id)
}

// 把一段英文拆成「段落 -> 句子」结构，并给每句时间区间
// 优先用转写 segs（句级精确时间）；否则用 en 文本按句长比例估算
function paragraphsOf(id) {
  const it = itemById(id)
  if (!it) return []
  if (it.segs && it.segs.length) {
    // 已有精确句时间：按段落分组，句首时间来自转写真实时间
    const out = []
    let curP = null
    let cur = null
    for (const s of it.segs) {
      const p = s.p === undefined ? 0 : s.p
      if (curP !== p) {
        cur = []
        out.push(cur)
        curP = p
      }
      cur.push({ text: s.text + ' ', t0: s.t0, t1: s.t1 })
    }
    return out
  }
  const en = it.en || ''
  const paras = en.split(/\n+/).map((p) => p.trim()).filter(Boolean)
  if (!paras.length) return []
  const totalChars = paras.reduce(
    (a, p) => a + (p.replace(/\s/g, '').length || 1),
    0
  )
  const dur = (states[id] && states[id].dur) || 0
  let cum = 0
  return paras.map((p) => {
    const raw = p.match(/[^.!?]+[.!?]*/g) || [p]
    return raw.map((r) => {
      const clean = r.trim()
      const chars = clean.replace(/\s/g, '').length || 1
      const t0 = (dur * cum) / totalChars
      cum += chars
      const t1 = (dur * cum) / totalChars
      return { text: clean + ' ', t0, t1 }
    })
  })
}

function sentenceCls(id, s) {
  if (id !== playingId.value) return ''
  const st = states[id]
  if (!st) return ''
  const t = st.time
  if (t >= s.t0 && t <= s.t1) return 'sentence-active'
  if (t > s.t1) return 'sentence-done'
  return ''
}

function toggleZh(id) {
  zhOpen[id] = !zhOpen[id]
}

function toggleAllZh() {
  const on = !allZhOn.value
  for (const it of currentItems.value) zhOpen[it.id] = on
}

onBeforeUnmount(() => {
  audios.forEach((a) => a.pause())
  audios.clear()
})
</script>

<template>
  <div class="listen">
    <p v-if="!ready" class="listen-tip">听力题库加载中，请稍候…</p>
    <template v-else>
      <div class="listen-bar">
        <span class="listen-total">
          共 {{ bank.length }} 段录音 · 当前 {{ currentItems.length }} 段
        </span>
        <button class="zh-all-btn" type="button" @click="toggleAllZh">
          {{ allZhOn ? '隐藏中文翻译' : '显示中文翻译' }}
        </button>
      </div>

      <div class="listen-filter">
        <div class="chip-row">
          <button
            v-for="(g, i) in groups"
            :key="g.chapter"
            type="button"
            class="chip"
            :class="{ active: i === activeChapter }"
            :title="g.chapter"
            @click="pickChapter(i)"
          >
            {{ chapterShort(g.chapter) }}
          </button>
        </div>
        <div v-if="parts.length > 1" class="chip-row chip-row-sub">
          <button
            v-for="(p, i) in parts"
            :key="p.label"
            type="button"
            class="chip chip-sub"
            :class="{ active: i === activePart }"
            @click="pickPart(i)"
          >
            {{ p.label }}
          </button>
        </div>
      </div>

      <section v-if="currentChapter" class="listen-group">
        <h3 class="listen-chapter">
          {{ currentChapter.chapter }}
          <span v-if="currentPart" class="listen-range">· {{ currentPart.label }}</span>
        </h3>

        <article v-for="(it, i) in currentItems" :key="it.id" class="listen-card">
          <div class="listen-head">
            <span class="listen-no">{{ currentPart.start + i + 1 }}</span>
            <span class="listen-title">{{ it.title }}</span>
          </div>

          <div class="listen-player">
            <button
              class="play-btn"
              type="button"
              :class="{ playing: playingId === it.id && isPlaying }"
              :aria-label="playingId === it.id && isPlaying ? '暂停' : '播放'"
              @click="toggle(it)"
            >
              <svg v-if="!(playingId === it.id && isPlaying)" viewBox="0 0 24 24" width="18" height="18"><path fill="currentColor" d="M8 5v14l11-7z"/></svg>
              <svg v-else viewBox="0 0 24 24" width="18" height="18"><path fill="currentColor" d="M6 5h4v14H6zM14 5h4v14h-4z"/></svg>
            </button>
            <div
              class="track"
              role="slider"
              tabindex="0"
              aria-label="播放进度"
              :aria-valuemin="0"
              :aria-valuemax="100"
              :aria-valuenow="Math.round(progress(it))"
              @click="seek(it, $event)"
              @keydown="onTrackKey(it, $event)"
            >
              <div class="track-fill" :style="{ width: progress(it) + '%' }"></div>
            </div>
            <span class="time">
              {{ fmt(states[it.id] && states[it.id].time) }} / {{ fmt(states[it.id] && states[it.id].dur) }}
            </span>
          </div>

          <div class="listen-actions">
            <button v-if="it.q" class="zh-btn" type="button" @click="toggleQ(it.id)">
              {{ isQOpen(it.id) ? '隐藏题目' : '显示题目' }}
            </button>
            <button class="zh-btn" type="button" @click="toggleZh(it.id)">
              {{ zhOpen[it.id] ? '隐藏中文翻译' : '显示中文翻译' }}
            </button>
            <button class="zh-btn" type="button" @click="toggleEn(it.id)">
              {{ enOpen[it.id] ? '隐藏听力原文' : '显示听力原文' }}
            </button>
          </div>

          <div v-if="it.q" v-show="isQOpen(it.id)" class="listen-q">
            <div class="q-label">Questions</div>
            <p class="q-body">{{ it.q }}</p>
          </div>
          <p v-show="zhOpen[it.id]" class="zh">{{ it.zh }}</p>
          <p v-if="enOpen[it.id]" class="en">
            <template v-if="paragraphsOf(it.id).length">
              <template v-for="(para, pi) in paragraphsOf(it.id)" :key="'p' + pi">
                <span
                  v-for="(s, si) in para"
                  :key="si"
                  class="sentence"
                  :class="sentenceCls(it.id, s)"
                  >{{ s.text }}</span
                ><br v-if="pi < paragraphsOf(it.id).length - 1" />
              </template>
            </template>
            <template v-else>{{ it.en }}</template>
          </p>
        </article>
      </section>
    </template>
  </div>
</template>

<style scoped>
.listen {
  margin-top: 20px;
}
.listen-tip {
  font-size: 13px;
  color: var(--vp-c-text-2);
}
.listen-bar {
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 12px 16px;
  margin-bottom: 18px;
  background: var(--vp-c-bg-soft);
  border: 1px solid var(--vp-c-divider);
  border-radius: 10px;
}
.listen-total {
  font-size: 13px;
  color: var(--vp-c-text-2);
}
.zh-all-btn {
  margin-left: auto;
  padding: 6px 14px;
  font-size: 13px;
  color: var(--vp-c-brand-1);
  background: var(--vp-c-bg);
  border: 1px solid var(--vp-c-brand-1);
  border-radius: 6px;
  cursor: pointer;
}
.listen-group {
  margin-bottom: 28px;
}
.listen-filter {
  margin-bottom: 18px;
}
.chip-row {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
}
.chip-row-sub {
  margin-top: 8px;
}
.chip {
  padding: 6px 14px;
  font-size: 13px;
  color: var(--vp-c-text-1);
  background: var(--vp-c-bg-soft);
  border: 1px solid var(--vp-c-divider);
  border-radius: 999px;
  cursor: pointer;
  transition: background 0.2s, color 0.2s, border-color 0.2s;
}
.chip:hover {
  border-color: var(--vp-c-brand-1);
  color: var(--vp-c-brand-1);
}
.chip.active {
  color: #fff;
  background: var(--vp-c-brand-1);
  border-color: var(--vp-c-brand-1);
}
.chip-sub {
  padding: 4px 12px;
  font-size: 12px;
  font-variant-numeric: tabular-nums;
}
.listen-chapter {
  margin: 0 0 12px;
  padding-left: 10px;
  font-size: 15px;
  color: var(--vp-c-text-1);
  border-left: 3px solid var(--vp-c-brand-1);
}
.listen-range {
  font-weight: 400;
  color: var(--vp-c-text-2);
}
/* 与习题测试 / 听力训练页保持同一套卡片观感 */
.listen-card {
  margin-bottom: 14px;
  padding: 16px 18px;
  background: var(--vp-c-bg);
  border: 1px solid var(--vp-c-divider);
  border-radius: 10px;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.04);
}
.listen-head {
  display: flex;
  align-items: center;
  gap: 8px;
  margin-bottom: 12px;
}
.listen-no {
  display: inline-flex;
  width: 22px;
  height: 22px;
  align-items: center;
  justify-content: center;
  font-size: 12px;
  color: #fff;
  background: var(--vp-c-brand-1);
  border-radius: 6px;
}
.listen-title {
  font-size: 14px;
  font-weight: 600;
  color: var(--vp-c-text-1);
}
.listen-player {
  display: flex;
  align-items: center;
  gap: 12px;
  margin-bottom: 12px;
}
.play-btn {
  flex: none;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  width: 40px;
  height: 40px;
  color: #fff;
  background: var(--vp-c-brand-1);
  border: none;
  border-radius: 50%;
  cursor: pointer;
}
.play-btn.playing {
  background: var(--vp-c-brand-2, #4c6ef5);
}
.track {
  flex: 1;
  height: 6px;
  background: var(--vp-c-divider);
  border-radius: 3px;
  cursor: pointer;
  overflow: hidden;
}
.track:focus-visible {
  outline: 2px solid var(--vp-c-brand-1);
  outline-offset: 3px;
}
.track-fill {
  height: 100%;
  width: 0;
  background: var(--vp-c-brand-1);
  border-radius: 3px;
}
.time {
  flex: none;
  font-size: 12px;
  color: var(--vp-c-text-2);
  font-variant-numeric: tabular-nums;
}
.listen-q {
  margin-top: 14px;
  padding: 12px 14px;
  background: var(--vp-c-bg);
  border: 1px solid var(--vp-c-divider);
  border-left: 3px solid var(--vp-c-brand-1);
  border-radius: 8px;
}
.q-label {
  margin-bottom: 6px;
  font-size: 12px;
  font-weight: 600;
  letter-spacing: 0.04em;
  text-transform: uppercase;
  color: var(--vp-c-brand-1);
}
.q-body {
  margin: 0;
  font-size: 14.5px;
  line-height: 1.9;
  color: var(--vp-c-text-1);
  white-space: pre-wrap;
}
.listen-actions {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
  margin-top: 14px;
}
.en {
  margin: 10px 0 0;
  padding: 10px 12px;
  font-size: 15px;
  line-height: 1.9;
  color: var(--vp-c-text-1);
  white-space: pre-wrap;
  background: var(--vp-c-bg);
  border-left: 3px solid var(--vp-c-divider);
  border-radius: 6px;
}
.en .sentence {
  transition: color 0.18s ease, background-color 0.18s ease;
  border-radius: 3px;
  padding: 0 1px;
}
.en .sentence-done {
  color: var(--vp-c-text-3);
}
.en .sentence-active {
  font-weight: 700;
  color: var(--vp-c-brand-1);
  background: rgba(76, 110, 245, 0.16);
}
.zh-btn {
  padding: 5px 12px;
  font-size: 12px;
  color: var(--vp-c-brand-1);
  background: var(--vp-c-bg);
  border: 1px solid var(--vp-c-brand-1);
  border-radius: 6px;
  cursor: pointer;
}
.zh {
  margin: 10px 0 0;
  padding: 10px 12px;
  font-size: 14px;
  line-height: 1.75;
  color: var(--vp-c-text-1);
  white-space: pre-wrap;
  background: var(--vp-c-bg);
  border-left: 3px solid var(--vp-c-brand-1);
  border-radius: 6px;
}
</style>
