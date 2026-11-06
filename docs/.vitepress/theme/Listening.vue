<script setup>
import { ref, reactive, computed, onMounted, onBeforeUnmount } from 'vue'

const bank = ref([])
const ready = ref(false)

onMounted(async () => {
  const mod = await import('./data/listening.json')
  bank.value = mod.default
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

// ---------- 音频播放 ----------
const playingId = ref(null)
const audios = new Map()
const states = reactive({}) // id -> { time, dur }

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
    if (playingId.value === it.id) playingId.value = null
  })
  audios.set(it.id, a)
  return a
}

function toggle(it) {
  const a = audioFor(it)
  if (playingId.value === it.id) {
    a.pause()
    playingId.value = null
    return
  }
  audios.forEach((x, id) => {
    if (id !== it.id) x.pause()
  })
  a.play().catch(() => {})
  playingId.value = it.id
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

// ---------- 中文翻译显示/隐藏 ----------
const zhOpen = reactive({}) // id -> bool
const allZh = ref(false)

function toggleZh(id) {
  zhOpen[id] = !zhOpen[id]
}

function toggleAllZh() {
  allZh.value = !allZh.value
  for (const it of bank.value) zhOpen[it.id] = allZh.value
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
        <span class="listen-total">共 {{ bank.length }} 段录音</span>
        <button class="zh-all-btn" type="button" @click="toggleAllZh">
          {{ allZh ? '全部隐藏中文' : '全部显示中文' }}
        </button>
      </div>

      <section v-for="g in groups" :key="g.chapter" class="listen-group">
        <h3 class="listen-chapter">{{ g.chapter }}</h3>

        <article v-for="(it, i) in g.items" :key="it.id" class="listen-card">
          <div class="listen-head">
            <span class="listen-no">{{ i + 1 }}</span>
            <span class="listen-title">{{ it.title }}</span>
          </div>

          <div class="listen-player">
            <button
              class="play-btn"
              type="button"
              :class="{ playing: playingId === it.id }"
              :aria-label="playingId === it.id ? '暂停' : '播放'"
              @click="toggle(it)"
            >
              <svg v-if="playingId !== it.id" viewBox="0 0 24 24" width="18" height="18"><path fill="currentColor" d="M8 5v14l11-7z"/></svg>
              <svg v-else viewBox="0 0 24 24" width="18" height="18"><path fill="currentColor" d="M6 5h4v14H6zM14 5h4v14h-4z"/></svg>
            </button>
            <div class="track" @click="seek(it, $event)">
              <div class="track-fill" :style="{ width: progress(it) + '%' }"></div>
            </div>
            <span class="time">
              {{ fmt(states[it.id] && states[it.id].time) }} / {{ fmt(states[it.id] && states[it.id].dur) }}
            </span>
          </div>

          <p class="en">{{ it.en }}</p>

          <button class="zh-btn" type="button" @click="toggleZh(it.id)">
            {{ zhOpen[it.id] ? '隐藏中文翻译' : '显示中文翻译' }}
          </button>
          <p v-show="zhOpen[it.id]" class="zh">{{ it.zh }}</p>
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
.listen-chapter {
  margin: 0 0 12px;
  padding-left: 10px;
  font-size: 15px;
  color: var(--vp-c-text-1);
  border-left: 3px solid var(--vp-c-brand-1);
}
.listen-card {
  margin-bottom: 14px;
  padding: 16px 18px;
  background: var(--vp-c-bg-soft);
  border: 1px solid var(--vp-c-divider);
  border-radius: 10px;
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
.en {
  margin: 0 0 10px;
  font-size: 15px;
  line-height: 1.75;
  color: var(--vp-c-text-1);
  white-space: pre-wrap;
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
