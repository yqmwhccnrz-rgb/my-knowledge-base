<script setup>
import { ref, reactive, computed, onMounted, onBeforeUnmount, watch, nextTick } from 'vue'

const bank = ref([])
const ready = ref(false)
const activeUnit = ref(1)
const activeGroup = ref(1)
const drafts = reactive({})
const answerOpen = reactive({})

let saveTimer = null

// 组件 setup 阶段就发起下载（仅听写页会实例化），与页面渲染并行；
// 数据放在 /data/ 下由浏览器原生 fetch + JSON.parse，不再打进 JS chunk。
const bankPromise = import.meta.env.SSR
  ? Promise.resolve([])
  : fetch('/data/dictation.json').then((r) => r.json()).catch(() => [])

onMounted(async () => {
  bank.value = await bankPromise
  try {
    Object.assign(drafts, JSON.parse(localStorage.getItem('dictation_drafts') || '{}'))
    const pos = JSON.parse(localStorage.getItem('dictation_pos') || '{}')
    if (pos.unit) activeUnit.value = pos.unit
    if (pos.group) activeGroup.value = pos.group
  } catch (e) {}
  ready.value = true
})

const units = computed(() => {
  const seen = new Map()
  for (const it of bank.value) {
    if (!seen.has(it.unit)) seen.set(it.unit, { n: it.unit, cn: it.unitCn, en: it.unitEn })
  }
  return [...seen.values()].sort((a, b) => a.n - b.n)
})

const groups = computed(() => {
  const u = bank.value.filter((x) => x.unit === activeUnit.value)
  const max = Math.ceil(u.length / 10)
  return Array.from({ length: max }, (_, i) => ({
    n: i + 1,
    label: `${i * 10 + 1}–${Math.min(i * 10 + 10, u.length)}`
  }))
})

const currentItems = computed(() =>
  bank.value.filter((x) => x.unit === activeUnit.value && x.group === activeGroup.value)
)

const currentUnit = computed(() => units.value.find((u) => u.n === activeUnit.value))

const answeredCount = computed(
  () => currentItems.value.filter((it) => (drafts[it.id] || '').trim()).length
)

function pickUnit(n) {
  if (n === activeUnit.value) return
  stopAll()
  activeUnit.value = n
  activeGroup.value = 1
  savePos()
}
function pickGroup(n) {
  if (n === activeGroup.value) return
  stopAll()
  activeGroup.value = n
  savePos()
}
function savePos() {
  try {
    localStorage.setItem('dictation_pos', JSON.stringify({ unit: activeUnit.value, group: activeGroup.value }))
  } catch (e) {}
}
function onInput(id, v) {
  drafts[id] = v
  clearTimeout(saveTimer)
  saveTimer = setTimeout(() => {
    try { localStorage.setItem('dictation_drafts', JSON.stringify(drafts)) } catch (e) {}
  }, 300)
}
function clearDraft(id) {
  drafts[id] = ''
  try { localStorage.setItem('dictation_drafts', JSON.stringify(drafts)) } catch (e) {}
}

// ---------- 播放 ----------
const playingId = ref(null)
const isPlaying = ref(false)
const audios = new Map()
const states = reactive({}) // id -> { time, dur }

function fmt(t) {
  if (!isFinite(t) || t < 0) t = 0
  const m = Math.floor(t / 60)
  const s = Math.floor(t % 60)
  return `${m}:${String(s).padStart(2, '0')}`
}
function audioFor(it) {
  if (audios.has(it.id)) return audios.get(it.id)
  const a = new Audio(it.audio)
  a.preload = 'metadata'
  a.addEventListener('loadedmetadata', () => {
    states[it.id] = { time: a.currentTime || 0, dur: a.duration || 0 }
  })
  a.addEventListener('timeupdate', () => {
    const st = states[it.id] || { dur: a.duration || 0 }
    states[it.id] = { time: a.currentTime, dur: st.dur || a.duration || 0 }
  })
  a.addEventListener('ended', () => {
    if (playingId.value === it.id) isPlaying.value = false
  })
  audios.set(it.id, a)
  return a
}
function stopAll() {
  audios.forEach((a) => a.pause())
  playingId.value = null
  isPlaying.value = false
}
function toggle(it) {
  const a = audioFor(it)
  if (playingId.value === it.id) {
    if (isPlaying.value) {
      a.pause(); isPlaying.value = false
    } else {
      a.play().catch(() => {}); isPlaying.value = true
    }
    return
  }
  audios.forEach((x) => x.pause())
  playingId.value = it.id
  a.play().catch(() => {})
  isPlaying.value = true
}
function replay(it) {
  const a = audioFor(it)
  a.currentTime = 0
  playingId.value = it.id
  a.play().catch(() => {})
  isPlaying.value = true
}
function progress(it) {
  const st = states[it.id]
  if (!st || !st.dur) return 0
  return Math.min(100, (st.time / st.dur) * 100)
}
function seek(it, e) {
  const a = audioFor(it)
  if (!a.duration) return
  const r = e.currentTarget.getBoundingClientRect()
  a.currentTime = Math.max(0, Math.min(a.duration, ((e.clientX - r.left) / r.width) * a.duration))
}
// 进度条支持键盘：左右方向键 ±5 秒（Shift 为 ±10 秒），Home/End 跳到首尾
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
  states[it.id] = { time: a.currentTime, dur: a.duration }
}

// 进入分组即预加载本组 10 条音频的元数据，避免显示 0:00 / 0:00；
// 同时释放上一组的音频对象，200 段音频不会全部常驻内存
watch([ready, activeUnit, activeGroup], () => {
  if (!ready.value) return
  nextTick(() => {
    const keep = new Set(currentItems.value.map((x) => x.id))
    for (const [id, a] of audios) {
      if (keep.has(id)) continue
      a.pause()
      a.removeAttribute('src')
      a.load()
      audios.delete(id)
    }
    for (const it of currentItems.value) audioFor(it).load()
  })
})
onBeforeUnmount(stopAll)

// ---------- 答案 ----------
function toggleAnswer(id) {
  answerOpen[id] = !answerOpen[id]
  // v-show 重新显示后需重新判断渐隐状态
  nextTick(refreshHints)
}
// 答案区限高滚动：内容不足一屏或滚到底时去掉底部渐隐
function updateHint(el) {
  const noScroll = el.scrollHeight <= el.clientHeight + 2
  const atBottom = el.scrollTop + el.clientHeight >= el.scrollHeight - 2
  el.classList.toggle('is-bottom', noScroll || atBottom)
}
function refreshHints() {
  document.querySelectorAll('.dict-scroll').forEach((el) => {
    if (el.offsetParent !== null) updateHint(el)
  })
}
// 切换单元/分组、首次渲染答案时都刷新一次渐隐状态
watch([activeUnit, activeGroup, answerOpen, ready], () => nextTick(refreshHints), { deep: true })

// ---------- 听写比对（显示答案时给出正确率与漏词） ----------
function tokens(s) {
  return (s || '')
    .toLowerCase()
    .replace(/[^a-z0-9'\s]/g, ' ')
    .replace(/\s+/g, ' ')
    .trim()
    .split(' ')
    .filter(Boolean)
}
function compare(en, input) {
  const a = tokens(en)
  const b = tokens(input)
  if (!a.length || !b.length) return null
  const n = a.length, m = b.length
  const dp = Array.from({ length: n + 1 }, () => new Uint16Array(m + 1))
  for (let i = 1; i <= n; i++) {
    for (let j = 1; j <= m; j++) {
      dp[i][j] = a[i - 1] === b[j - 1]
        ? dp[i - 1][j - 1] + 1
        : Math.max(dp[i - 1][j], dp[i][j - 1])
    }
  }
  let i = n, j = m
  const hit = new Set()
  while (i > 0 && j > 0) {
    if (a[i - 1] === b[j - 1]) { hit.add(i - 1); i--; j-- }
    else if (dp[i - 1][j] >= dp[i][j - 1]) i--
    else j--
  }
  const missed = []
  for (let k = 0; k < n; k++) if (!hit.has(k)) missed.push(a[k])
  return {
    rate: Math.round((hit.size / n) * 100),
    hit: hit.size,
    total: n,
    missed: [...new Set(missed)].slice(0, 24)
  }
}

// 只为已展开答案的题目计算一次，避免模板重复跑对齐
const scores = computed(() => {
  const m = {}
  for (const it of currentItems.value) {
    if (answerOpen[it.id]) m[it.id] = compare(it.en, drafts[it.id])
  }
  return m
})
</script>

<template>
  <div class="dict-wrap">
    <div v-if="!ready" class="dict-loading">听写题库加载中…</div>

    <template v-else>
      <div class="dict-filter">
        <div class="dict-label">训练单元</div>
        <div class="dict-chip-row">
          <button
            v-for="u in units" :key="u.n" type="button"
            class="dict-chip" :class="{ active: activeUnit === u.n }"
            @click="pickUnit(u.n)"
          >
            <span class="chip-main">{{ u.cn }}</span>
            <span class="chip-sub">{{ u.en }}</span>
          </button>
        </div>

        <div class="dict-label">题目分组</div>
        <div class="dict-chip-row">
          <button
            v-for="g in groups" :key="g.n" type="button"
            class="dict-chip dict-chip-sm" :class="{ active: activeGroup === g.n }"
            @click="pickGroup(g.n)"
          >{{ g.label }}</button>
        </div>
      </div>

      <div class="dict-bar">
        <span class="dict-total">共 {{ bank.length }} 题 · 当前 {{ currentItems.length }} 题 · 已作答 {{ answeredCount }} 题</span>
        <span class="dict-hint">先听录音 → 在框里写出英文 → 再点「显示答案」对照</span>
      </div>

      <div class="dict-unit-title">{{ currentUnit?.cn }} <span>· {{ currentUnit?.en }}</span></div>

      <article v-for="it in currentItems" :key="it.id" class="dict-card">
        <div class="dict-head">
          <span class="dict-no">{{ it.no }}</span>
          <span class="dict-meta">{{ it.words }} 词 · 盲听后写出原文，再对照答案</span>
        </div>

        <div class="dict-player">
          <button class="dict-play" type="button" :aria-label="playingId === it.id && isPlaying ? '暂停' : '播放'" @click="toggle(it)">
            <svg v-if="!(playingId === it.id && isPlaying)" viewBox="0 0 24 24" width="18" height="18"><path fill="currentColor" d="M8 5v14l11-7z"/></svg>
            <svg v-else viewBox="0 0 24 24" width="18" height="18"><path fill="currentColor" d="M6 5h4v14H6zM14 5h4v14h-4z"/></svg>
          </button>
          <div
            class="dict-track"
            role="slider"
            tabindex="0"
            aria-label="播放进度"
            :aria-valuemin="0"
            :aria-valuemax="100"
            :aria-valuenow="Math.round(progress(it))"
            @click="seek(it, $event)"
            @keydown="onTrackKey(it, $event)"
          >
            <div class="dict-track-fill" :style="{ width: progress(it) + '%' }"></div>
          </div>
          <span class="dict-time">{{ fmt(states[it.id]?.time || 0) }} / {{ fmt(states[it.id]?.dur || 0) }}</span>
          <button class="dict-replay" type="button" @click="replay(it)">↺ 重听</button>
        </div>

        <div class="dict-input-box">
          <textarea
            :value="drafts[it.id] || ''"
            @input="onInput(it.id, $event.target.value)"
            class="dict-input"
            rows="3"
            spellcheck="false"
            :aria-label="`第 ${it.no} 题听写作答`"
            placeholder="听录音，把听到的英文逐字打在这里…"
          ></textarea>
          <div class="dict-input-foot">
            <span>已输入 {{ (drafts[it.id] || '').trim() ? (drafts[it.id].trim().split(/\s+/).length) : 0 }} 词</span>
            <button v-if="(drafts[it.id] || '').trim()" type="button" class="dict-clear" @click="clearDraft(it.id)">清空</button>
          </div>
        </div>

        <div class="dict-actions">
          <button class="dict-btn" type="button" @click="toggleAnswer(it.id)">
            {{ answerOpen[it.id] ? '隐藏答案' : '显示答案' }}
          </button>
        </div>

        <div v-show="answerOpen[it.id]" class="dict-answer">
          <template v-if="scores[it.id]">
            <div class="dict-score">
              <span class="score-num">{{ scores[it.id].rate }}%</span>
              <span>听写正确率（{{ scores[it.id].hit }}/{{ scores[it.id].total }} 词）</span>
            </div>
            <div v-if="scores[it.id].missed.length" class="dict-missed">
              <span class="missed-label">漏写 / 写错的词：</span>
              <span v-for="(w, i) in scores[it.id].missed" :key="i" class="missed-word">{{ w }}</span>
            </div>
          </template>

          <div class="ans-label">参考答案 · English</div>
          <p class="ans-en dict-scroll" @scroll="updateHint($event.target)">{{ it.en }}</p>
          <div class="ans-label">中文翻译</div>
          <p class="ans-zh dict-scroll" @scroll="updateHint($event.target)">{{ it.zh }}</p>
        </div>
      </article>
    </template>
  </div>
</template>

<style>
.dict-wrap { margin: 8px 0 40px; }
.dict-loading { padding: 30px 0; color: var(--vp-c-text-2); }

.dict-filter { margin-bottom: 18px; }
.dict-label {
  margin: 12px 0 7px;
  font-size: 12px;
  font-weight: 600;
  letter-spacing: 0.04em;
  color: var(--vp-c-text-3);
}
.dict-chip-row { display: flex; flex-wrap: wrap; gap: 8px; }
.dict-chip {
  padding: 7px 13px;
  font-size: 13px;
  line-height: 1.35;
  color: var(--vp-c-text-1);
  background: var(--vp-c-bg-soft);
  border: 1px solid var(--vp-c-divider);
  border-radius: 8px;
  cursor: pointer;
  text-align: left;
  transition: background-color 0.18s ease, border-color 0.18s ease, color 0.18s ease;
}
.dict-chip:hover { border-color: var(--vp-c-brand-1); }
.dict-chip.active {
  color: #fff;
  background: var(--vp-c-brand-1);
  border-color: var(--vp-c-brand-1);
}
.chip-main { display: block; font-weight: 600; }
.chip-sub { display: block; font-size: 11px; opacity: 0.75; }
.dict-chip-sm { padding: 6px 14px; font-size: 13px; font-weight: 600; }

.dict-bar {
  display: flex; flex-wrap: wrap; gap: 10px; justify-content: space-between; align-items: center;
  padding: 10px 12px; margin-bottom: 18px;
  background: var(--vp-c-bg-soft); border-radius: 8px; font-size: 13px;
}
.dict-total { color: var(--vp-c-text-1); font-weight: 600; }
.dict-hint { color: var(--vp-c-text-3); font-size: 12px; }
.dict-unit-title {
  margin: 0 0 14px; padding-left: 10px; font-size: 15px; font-weight: 600;
  color: var(--vp-c-text-1); border-left: 3px solid var(--vp-c-brand-1);
}
.dict-unit-title span { font-size: 12px; font-weight: 400; color: var(--vp-c-text-3); }

.dict-card {
  padding: 16px 18px; margin-bottom: 16px;
  background: var(--vp-c-bg); border: 1px solid var(--vp-c-divider);
  border-radius: 10px; box-shadow: 0 1px 3px rgba(0, 0, 0, 0.04);
}
.dict-head { display: flex; align-items: center; gap: 10px; margin-bottom: 12px; }
.dict-no {
  display: inline-flex; align-items: center; justify-content: center;
  min-width: 26px; height: 26px; padding: 0 6px;
  font-size: 13px; font-weight: 700; color: #fff;
  background: var(--vp-c-brand-1); border-radius: 7px;
}
.dict-meta { font-size: 12px; color: var(--vp-c-text-3); }

.dict-player { display: flex; align-items: center; gap: 10px; margin-bottom: 12px; }
.dict-play {
  display: inline-flex; align-items: center; justify-content: center;
  width: 34px; height: 34px; flex: none; padding: 0;
  color: #fff; background: var(--vp-c-brand-1); border: none;
  border-radius: 50%; cursor: pointer;
}
.dict-play:hover { opacity: 0.88; }
.dict-track {
  flex: 1; height: 6px; min-width: 60px;
  background: var(--vp-c-bg-soft); border: 1px solid var(--vp-c-divider);
  border-radius: 4px; cursor: pointer; overflow: hidden;
}
.dict-track:focus-visible {
  outline: 2px solid var(--vp-c-brand-1);
  outline-offset: 3px;
}
.dict-track-fill { height: 100%; background: var(--vp-c-brand-1); transition: width 0.15s linear; }
.dict-time { font-size: 12px; color: var(--vp-c-text-2); white-space: nowrap; font-variant-numeric: tabular-nums; }
.dict-replay {
  flex: none; padding: 4px 8px; font-size: 12px;
  color: var(--vp-c-text-2); background: transparent;
  border: 1px solid var(--vp-c-divider); border-radius: 6px; cursor: pointer;
}
.dict-replay:hover { color: var(--vp-c-brand-1); border-color: var(--vp-c-brand-1); }

.dict-input-box { margin-bottom: 10px; }
.dict-input {
  width: 100%; box-sizing: border-box; padding: 10px 12px;
  font-size: 14px; line-height: 1.7; color: var(--vp-c-text-1);
  background: var(--vp-c-bg-soft); border: 1px solid var(--vp-c-divider);
  border-radius: 8px; resize: vertical; outline: none;
  font-family: inherit;
}
.dict-input:focus { border-color: var(--vp-c-brand-1); background: var(--vp-c-bg); }
.dict-input::placeholder { color: var(--vp-c-text-3); }
.dict-input-foot {
  display: flex; justify-content: space-between; align-items: center;
  margin-top: 5px; font-size: 12px; color: var(--vp-c-text-3);
}
.dict-clear {
  padding: 0; font-size: 12px; color: var(--vp-c-text-3);
  background: none; border: none; cursor: pointer; text-decoration: underline;
}
.dict-clear:hover { color: var(--vp-c-brand-1); }

.dict-actions { display: flex; flex-wrap: wrap; gap: 8px; }
.dict-btn {
  padding: 6px 14px; font-size: 13px; font-weight: 600;
  color: var(--vp-c-brand-1); background: var(--vp-c-bg);
  border: 1px solid var(--vp-c-brand-1); border-radius: 7px; cursor: pointer;
  transition: background-color 0.18s ease, color 0.18s ease;
}
.dict-btn:hover { color: #fff; background: var(--vp-c-brand-1); }

.dict-answer {
  margin-top: 12px; padding: 12px 14px;
  background: var(--vp-c-bg-soft); border-radius: 8px;
  border-left: 3px solid var(--vp-c-brand-1);
}
.ans-label {
  margin: 10px 0 5px; font-size: 12px; font-weight: 700;
  letter-spacing: 0.03em; color: var(--vp-c-brand-1);
}
.ans-label:first-child { margin-top: 0; }
.ans-en, .ans-zh {
  margin: 0; font-size: 14px; line-height: 1.85;
  color: var(--vp-c-text-1); white-space: pre-wrap;
}
.ans-zh { color: var(--vp-c-text-2); }

/* 参考答案 / 中文翻译：限制高度在框内滚动，避免「显示答案」后整段撑满屏幕 */
.dict-scroll {
  max-height: 200px; overflow-y: auto; overscroll-behavior: contain;
  padding-right: 14px;
  scrollbar-width: thin; scrollbar-color: var(--vp-c-text-3, #8d8f8d) transparent;
  -webkit-mask-image: linear-gradient(to bottom, #000 calc(100% - 12px), rgba(0, 0, 0, 0.82));
  mask-image: linear-gradient(to bottom, #000 calc(100% - 12px), rgba(0, 0, 0, 0.82));
}
.dict-scroll::-webkit-scrollbar { width: 8px; }
.dict-scroll::-webkit-scrollbar-track { background: var(--vp-c-bg-soft, #f4f4f2); border-radius: 4px; }
.dict-scroll::-webkit-scrollbar-thumb { background: var(--vp-c-text-3, #8d8f8d); border-radius: 4px; opacity: .55; }
.dict-scroll.is-bottom { -webkit-mask-image: none; mask-image: none; }
@media (max-width: 640px) { .dict-scroll { max-height: 160px; } }
@media print {
  .dict-scroll {
    max-height: none !important; overflow: visible !important;
    -webkit-mask-image: none !important; mask-image: none !important;
  }
}

.dict-score {
  display: flex; align-items: baseline; gap: 8px;
  padding: 8px 10px; margin-bottom: 10px;
  background: var(--vp-c-bg); border-radius: 6px;
  font-size: 12px; color: var(--vp-c-text-2);
}
.score-num { font-size: 20px; font-weight: 700; color: var(--vp-c-brand-1); }
.dict-missed { margin-bottom: 12px; font-size: 12px; line-height: 2; }
.missed-label { color: var(--vp-c-text-3); }
.missed-word {
  display: inline-block; margin: 0 4px 2px 0; padding: 1px 6px;
  font-size: 12px; color: #c0392b; background: rgba(192, 57, 43, 0.08);
  border-radius: 4px;
}

@media (max-width: 640px) {
  .dict-card { padding: 13px; }
  .dict-hint { display: none; }
  .dict-replay { display: none; }
}
</style>
