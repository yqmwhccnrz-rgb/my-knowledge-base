<script setup>
import { ref, computed, watch } from 'vue'
import bank from './data/questions.json'

const noteOptions = [
  { key: 'all', label: '全部笔记' },
  { key: 'C', label: 'C 语言笔记' },
  { key: 'Python', label: 'Python 数据分析笔记' }
]
const selectedNote = ref('all')
const size = ref(5)
const picked = ref([])
const answers = ref({})
const submitted = ref(false)

const noteLabel = computed(
  () => (noteOptions.find((n) => n.key === selectedNote.value) || {}).label || ''
)

// 单题归属的笔记名称（用于卡片上标注）
function noteName(note) {
  const m = noteOptions.find((o) => o.key === note)
  return m ? m.label : note
}

// 按所选笔记过滤题库；「全部笔记」展示所有题
const bankForNote = computed(() =>
  selectedNote.value === 'all'
    ? bank
    : bank.filter((q) => q.note === selectedNote.value)
)
const topicCount = computed(
  () => new Set(bankForNote.value.map((q) => q.topic)).size
)

function shuffle(list) {
  const arr = [...list]
  for (let i = arr.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1))
    ;[arr[i], arr[j]] = [arr[j], arr[i]]
  }
  return arr
}

function start() {
  const n = Math.min(Number(size.value), bankForNote.value.length)
  picked.value = shuffle(bankForNote.value).slice(0, n)
  answers.value = {}
  submitted.value = false
}

// 切换笔记或题量时自动重新抽题
watch([selectedNote, size], start)
start()

function normalize(s) {
  return String(s).trim().toLowerCase()
}

// 填空题 / 程序设计题：答案支持多个可接受写法，忽略大小写与首尾空格
function isFillCorrect(blank, a) {
  const got = normalize(a)
  return (blank.answer || []).some((ans) => normalize(ans) === got)
}

function isRight(q, i) {
  const a = answers.value[i]
  if (q.type === 'fill') return a != null && isFillCorrect(q, a)
  if (q.type === 'program') {
    if (!a) return false
    return (q.blanks || []).every(
      (blk, b) => a[b] != null && isFillCorrect(blk, a[b])
    )
  }
  return a === q.answer
}

function correctText(q) {
  if (q.type === 'fill') return (q.answer || []).join(' / ')
  if (q.type === 'program') {
    return (q.blanks || [])
      .map((blk, b) => `空${b + 1}: ${(blk.answer || []).join(' / ')}`)
      .join('；')
  }
  if (q.type === 'judge') return q.options[q.answer]
  return letter(q.answer)
}

// 程序设计题：把题目中的 __N__ 占位符解析成「文本片段 + 填空位」
const BLANK_RE = /__(\d+)__/g
function segments(q) {
  if (q.type !== 'program') return []
  const out = []
  let last = 0
  let m
  BLANK_RE.lastIndex = 0
  while ((m = BLANK_RE.exec(q.question)) !== null) {
    if (m.index > last) out.push({ text: q.question.slice(last, m.index) })
    out.push({ blank: Number(m[1]) - 1 })
    last = m.index + m[0].length
  }
  if (last < q.question.length) out.push({ text: q.question.slice(last) })
  return out
}

function setBlank(i, b, val) {
  if (!answers.value[i]) answers.value[i] = {}
  answers.value[i][b] = val
}

function blankRight(q, i, b) {
  const a = answers.value[i]
  const val = a && a[b]
  const blk = q.blanks && q.blanks[b]
  return val != null && blk && isFillCorrect(blk, val)
}

const score = computed(() =>
  picked.value.reduce((total, q, i) => total + (isRight(q, i) ? 1 : 0), 0)
)

const allAnswered = computed(() =>
  picked.value.every((q, i) => {
    const a = answers.value[i]
    if (q.type === 'fill') return typeof a === 'string' && a.trim() !== ''
    if (q.type === 'program') {
      if (!a) return false
      return (q.blanks || []).every(
        (_, b) => typeof a[b] === 'string' && a[b].trim() !== ''
      )
    }
    return a !== undefined
  })
)

const accuracy = computed(() => {
  if (!picked.value.length) return 0
  return Math.round((score.value / picked.value.length) * 100)
})

function letter(n) {
  return String.fromCharCode(65 + n)
}

function submit() {
  if (!allAnswered.value) return
  submitted.value = true
}

// 重新作答：清空已选答案，保留当前这组题，可重新作答
function retry() {
  answers.value = {}
  submitted.value = false
}

// ---- 答题记录（B 后端：Cloudflare Pages Functions + KV）----
const saving = ref(false)
const savedMsg = ref('')
const showRecords = ref(false)
const recordsList = ref([])

function visitorId() {
  let id = localStorage.getItem('kb_visitor_id')
  if (!id) {
    id = 'v_' + (crypto.randomUUID ? crypto.randomUUID() : String(Math.random()).slice(2))
    localStorage.setItem('kb_visitor_id', id)
  }
  return id
}

async function saveRecord() {
  if (!submitted.value) return
  saving.value = true
  savedMsg.value = ''
  try {
    const res = await fetch('/api/records', {
      method: 'POST',
      headers: { 'content-type': 'application/json', 'x-visitor-id': visitorId() },
      body: JSON.stringify({
        note: selectedNote.value,
        score: score.value,
        total: picked.value.length
      })
    })
    if (res.ok) {
      savedMsg.value = '已保存本次成绩'
      await loadRecords()
    } else {
      savedMsg.value = '保存失败（请确认后端 KV 已绑定）'
    }
  } catch (e) {
    savedMsg.value = '保存失败（离线或后端未配置）'
  } finally {
    saving.value = false
  }
}

async function loadRecords() {
  try {
    const res = await fetch('/api/records', { headers: { 'x-visitor-id': visitorId() } })
    if (res.ok) recordsList.value = await res.json()
  } catch (e) {
    recordsList.value = []
  }
}

function toggleRecords() {
  showRecords.value = !showRecords.value
  if (showRecords.value) loadRecords()
}

function fmtDate(iso) {
  const d = new Date(iso)
  if (isNaN(d.getTime())) return iso
  const p = (n) => String(n).padStart(2, '0')
  return `${d.getFullYear()}-${p(d.getMonth() + 1)}-${p(d.getDate())} ${p(d.getHours())}:${p(d.getMinutes())}`
}
</script>

<template>
  <div class="quiz">
    <div class="quiz-bar">
      <label>
        选择笔记
        <select v-model="selectedNote">
          <option v-for="n in noteOptions" :key="n.key" :value="n.key">
            {{ n.label }}
          </option>
        </select>
      </label>
      <label>
        每次抽题
        <select v-model.number="size">
          <option :value="5">5 题</option>
          <option :value="10">10 题</option>
        </select>
      </label>
      <button class="quiz-btn" type="button" @click="start">换一组题</button>
      <span class="quiz-total">本笔记题库共 {{ bankForNote.length }} 题</span>
    </div>

    <p class="quiz-tip">
      当前展示 <strong>{{ noteLabel }}</strong> 的习题，题库共
      {{ bankForNote.length }} 道，覆盖 {{ topicCount }} 个知识点方向；本次随机抽取
      {{ picked.length }} 道（含选择 / 判断 / 填空 / 代码 / 程序设计题）。
    </p>

    <div v-for="(q, i) in picked" :key="q.id" class="quiz-card">
      <div class="quiz-q">
        <span class="quiz-no">{{ i + 1 }}</span>
        <span class="quiz-note">{{ noteName(q.note) }}</span>
        <span class="quiz-topic">{{ q.topic }}</span>
        <p
          v-if="q.type !== 'program'"
          class="quiz-text"
          :class="{ 'is-code': q.topic === '代码' }"
        >
          {{ q.question }}
        </p>
        <div v-else class="quiz-text is-code">
          <template v-for="(seg, si) in segments(q)" :key="si">
            <span v-if="seg.text">{{ seg.text }}</span>
            <input
              v-else
              class="quiz-blank"
              :class="{
                'is-wrong': submitted && !blankRight(q, i, seg.blank),
                'is-right': submitted && blankRight(q, i, seg.blank)
              }"
              :value="(answers[i] && answers[i][seg.blank]) || ''"
              @input="setBlank(i, seg.blank, $event.target.value)"
            />
          </template>
        </div>
      </div>

      <!-- 选择 / 判断题：单选 -->
      <div
        v-if="!q.type || q.type === 'choice' || q.type === 'judge'"
        class="quiz-options"
      >
        <label
          v-for="(opt, k) in q.options"
          :key="k"
          :class="{
            'is-right': submitted && k === q.answer,
            'is-wrong': submitted && answers[i] === k && k !== q.answer,
            'is-empty': !submitted && answers[i] === undefined
          }"
        >
          <input
            type="radio"
            :name="`q-${q.id}`"
            :value="k"
            v-model="answers[i]"
          />
          <span>{{ letter(k) }}. {{ opt }}</span>
        </label>
      </div>

      <!-- 填空题：文本输入 -->
      <input
        v-else-if="q.type === 'fill'"
        class="quiz-fill"
        type="text"
        v-model="answers[i]"
        placeholder="请输入答案"
      />

      <div
        v-if="submitted"
        class="quiz-result"
        :class="isRight(q, i) ? 'ok' : 'bad'"
      >
        <strong>{{ isRight(q, i) ? '答对了' : '答错了' }}</strong>
        正确答案 {{ correctText(q) }} · {{ q.explanation }}
      </div>
      <template v-else>
        <p v-if="q.type === 'program'" class="quiz-empty-hint">
          请在框内输入答案
        </p>
        <p
          v-else-if="(!q.type || q.type !== 'fill') && answers[i] === undefined"
          class="quiz-empty-hint"
        >
          请选择一个答案
        </p>
        <p
          v-else-if="q.type === 'fill' && (!answers[i] || !answers[i].trim())"
          class="quiz-empty-hint"
        >
          请填写答案
        </p>
      </template>
    </div>

    <div class="quiz-footer">
      <template v-if="!submitted">
        <button
          class="quiz-btn primary"
          type="button"
          :disabled="!allAnswered"
          @click="submit"
        >
          提交并查看解析
        </button>
        <span v-if="!allAnswered" class="quiz-foot-hint">
          还有未作答的题目
        </span>
      </template>
      <template v-else>
        <div class="quiz-score">
          本次得分 <strong>{{ score }} / {{ picked.length }}</strong>
          <span class="quiz-acc">正确率 {{ accuracy }}%</span>
        </div>
        <button class="quiz-btn" type="button" @click="retry">
          重新作答
        </button>
        <button class="quiz-btn" type="button" :disabled="saving" @click="saveRecord">
          {{ saving ? '保存中…' : '保存成绩' }}
        </button>
        <button class="quiz-btn" type="button" @click="toggleRecords">
          {{ showRecords ? '隐藏记录' : '我的记录' }}
        </button>
        <span v-if="savedMsg" class="quiz-saved">{{ savedMsg }}</span>
      </template>
    </div>

    <div v-if="showRecords" class="quiz-records">
      <h4 class="quiz-records-title">我的答题记录</h4>
      <p v-if="!recordsList.length" class="quiz-records-empty">暂无记录</p>
      <ul v-else class="quiz-records-list">
        <li v-for="(r, idx) in recordsList" :key="idx">
          <span class="rk-note">{{ noteName(r.note) }}</span>
          <span class="rk-score">{{ r.score }} / {{ r.total }}</span>
          <span class="rk-date">{{ fmtDate(r.date) }}</span>
        </li>
      </ul>
    </div>
  </div>
</template>

<style scoped>
.quiz {
  margin-top: 24px;
}
.quiz-bar {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: 12px;
  padding: 14px 16px;
  background: var(--vp-c-bg-soft);
  border: 1px solid var(--vp-c-divider);
  border-radius: 10px;
}
.quiz-bar label {
  font-size: 13px;
  color: var(--vp-c-text-2);
}
.quiz-bar select {
  margin-left: 8px;
  padding: 6px 10px;
  font-size: 13px;
  color: var(--vp-c-text-1);
  background: var(--vp-c-bg);
  border: 1px solid var(--vp-c-divider);
  border-radius: 6px;
}
.quiz-btn {
  padding: 7px 14px;
  font-size: 13px;
  color: var(--vp-c-brand-1);
  background: var(--vp-c-bg);
  border: 1px solid var(--vp-c-brand-1);
  border-radius: 6px;
  cursor: pointer;
}
.quiz-btn.primary {
  color: #fff;
  background: var(--vp-c-brand-1);
  padding: 10px 20px;
}
.quiz-btn:disabled {
  opacity: 0.45;
  cursor: not-allowed;
}
.quiz-total {
  margin-left: auto;
  font-size: 13px;
  color: var(--vp-c-text-2);
  white-space: nowrap;
}
.quiz-tip {
  margin: 14px 0 20px;
  font-size: 13px;
  color: var(--vp-c-text-2);
}
.quiz-tip strong {
  color: var(--vp-c-text-1);
}
.quiz-card {
  margin-bottom: 16px;
  padding: 18px 20px;
  background: var(--vp-c-bg-soft);
  border: 1px solid var(--vp-c-divider);
  border-radius: 10px;
}
.quiz-q {
  margin-bottom: 14px;
}
.quiz-no {
  display: inline-flex;
  width: 22px;
  height: 22px;
  align-items: center;
  justify-content: center;
  margin-right: 8px;
  font-size: 12px;
  color: #fff;
  background: var(--vp-c-brand-1);
  border-radius: 6px;
}
.quiz-note {
  margin-right: 8px;
  padding: 2px 8px;
  font-size: 12px;
  color: var(--vp-c-brand-1);
  background: var(--vp-c-brand-soft);
  border: 1px solid var(--vp-c-brand-1);
  border-radius: 6px;
  white-space: nowrap;
}
.quiz-topic {
  font-size: 12px;
  color: var(--vp-c-text-2);
}
.quiz-text {
  margin: 10px 0 0;
  font-size: 15px;
  line-height: 1.7;
  color: var(--vp-c-text-1);
  white-space: pre-wrap;
}
.quiz-text.is-code {
  font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace;
  font-size: 13px;
  background: var(--vp-c-bg-alt, #f6f8fa);
  border: 1px solid var(--vp-c-divider);
  border-radius: 8px;
  padding: 12px 14px;
  overflow-x: auto;
}
.quiz-blank {
  font-family: inherit;
  font-size: 13px;
  padding: 2px 6px;
  margin: 0 2px;
  color: var(--vp-c-text-1);
  background: var(--vp-c-bg);
  border: 1px solid var(--vp-c-brand-1);
  border-radius: 4px;
  width: 110px;
  text-align: center;
}
.quiz-blank.is-wrong {
  border-color: #c0392b;
  background: rgba(192, 57, 43, 0.06);
}
.quiz-blank.is-right {
  border-color: var(--vp-c-brand-1);
  background: var(--vp-c-brand-soft);
}
.quiz-options {
  display: flex;
  flex-direction: column;
  gap: 8px;
}
.quiz-options label {
  display: flex;
  align-items: flex-start;
  gap: 10px;
  padding: 9px 12px;
  font-size: 14px;
  line-height: 1.6;
  color: var(--vp-c-text-1);
  background: var(--vp-c-bg);
  border: 1px solid var(--vp-c-divider);
  border-radius: 8px;
  cursor: pointer;
}
.quiz-options label:hover {
  border-color: var(--vp-c-brand-1);
}
.quiz-options label.is-right {
  border-color: var(--vp-c-brand-1);
  background: var(--vp-c-brand-soft);
}
.quiz-options label.is-wrong {
  border-color: #c0392b;
}
.quiz-options label.is-empty {
  border-style: dashed;
}
.quiz-fill {
  width: 100%;
  box-sizing: border-box;
  padding: 10px 14px;
  font-size: 15px;
  color: var(--vp-c-text-1);
  background: var(--vp-c-bg);
  border: 1px solid var(--vp-c-divider);
  border-radius: 8px;
}
.quiz-fill:focus {
  outline: none;
  border-color: var(--vp-c-brand-1);
}
.quiz-result {
  margin-top: 12px;
  padding: 10px 12px;
  font-size: 13px;
  line-height: 1.7;
  border-radius: 8px;
}
.quiz-result.ok {
  color: var(--vp-c-brand-1);
  background: var(--vp-c-brand-soft);
}
.quiz-result.bad {
  color: #c0392b;
  background: rgba(192, 57, 43, 0.08);
}
.quiz-empty-hint {
  margin: 10px 0 0;
  font-size: 12px;
  color: var(--vp-c-text-2);
}
.quiz-footer {
  margin-top: 20px;
  display: flex;
  align-items: center;
  gap: 14px;
  flex-wrap: wrap;
}
.quiz-foot-hint {
  font-size: 12px;
  color: var(--vp-c-text-2);
}
.quiz-score {
  padding: 14px 18px;
  font-size: 15px;
  color: var(--vp-c-text-1);
  background: var(--vp-c-bg-soft);
  border: 1px solid var(--vp-c-divider);
  border-radius: 10px;
}
.quiz-score strong {
  color: var(--vp-c-brand-1);
  font-size: 20px;
}
.quiz-acc {
  margin-left: 12px;
  font-size: 13px;
  color: var(--vp-c-text-2);
}
.quiz-saved {
  font-size: 12px;
  color: var(--vp-c-brand-1);
}
.quiz-records {
  margin-top: 22px;
  padding: 16px 18px;
  background: var(--vp-c-bg-soft);
  border: 1px solid var(--vp-c-divider);
  border-radius: 10px;
}
.quiz-records-title {
  margin: 0 0 10px;
  font-size: 14px;
  color: var(--vp-c-text-1);
}
.quiz-records-empty {
  margin: 0;
  font-size: 13px;
  color: var(--vp-c-text-2);
}
.quiz-records-list {
  margin: 0;
  padding: 0;
  list-style: none;
  display: flex;
  flex-direction: column;
  gap: 8px;
}
.quiz-records-list li {
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 8px 12px;
  font-size: 13px;
  background: var(--vp-c-bg);
  border: 1px solid var(--vp-c-divider);
  border-radius: 8px;
}
.rk-note {
  color: var(--vp-c-brand-1);
  white-space: nowrap;
}
.rk-score {
  font-weight: 600;
  color: var(--vp-c-text-1);
}
.rk-date {
  margin-left: auto;
  color: var(--vp-c-text-2);
  white-space: nowrap;
}
</style>
