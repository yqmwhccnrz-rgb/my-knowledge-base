<script setup>
import { ref, computed, watch, onMounted, onBeforeUnmount } from 'vue'
import { fetchJson, LoginExpiredError, notifyAuthExpired } from './favoritesApi.js'
// 题库近 1MB，异步加载：只有真正打开习题页时才拉取，不拖慢其他笔记页
const bank = ref([])
const bankReady = ref(false)
const authExpired = ref(false)
function relogin() {
  window.location.reload()
}
function onAuthExpired() {
  authExpired.value = true
}
onMounted(() => window.addEventListener('kb-auth-expired', onAuthExpired))
onBeforeUnmount(() => window.removeEventListener('kb-auth-expired', onAuthExpired))

const noteOptions = [
  { key: 'all', label: '全部笔记' },
  { key: 'C', label: 'C 语言笔记' },
  { key: 'Python', label: 'Python 数据分析笔记' },
  { key: 'ML', label: 'Python 机器学习笔记' },
  { key: 'Matlab', label: 'Matlab 笔记' },
  { key: 'Tax', label: '税法笔记（CPA）' },
  { key: 'Accounting', label: '会计笔记（CPA）' },
  { key: 'Strategy', label: '公司战略笔记（CPA）' },
  { key: 'EconLaw', label: '经济法笔记（CPA）' },
  { key: 'Audit', label: '审计笔记（CPA）' },
  { key: 'Finance', label: '金融学笔记' },
  { key: 'FCM', label: '财务成本管理笔记（CPA）' },
  { key: 'Macro', label: '宏观经济学笔记' },
  { key: 'DataStructure', label: '数据结构笔记' },
  { key: 'Java', label: 'Java 程序设计笔记' },
  { key: 'Network', label: '计算机网络笔记' },
  { key: 'COA', label: '计算机组成与系统结构笔记' },
  { key: 'OS', label: '计算机操作系统笔记' },
  { key: 'Econometrics', label: '计量经济学笔记' },
  { key: 'Database', label: '数据库原理及应用笔记' }
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
    ? bank.value
    : bank.value.filter((q) => q.note === selectedNote.value)
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
  // 题库里存在少量「题干相同、选项/考点不同」的变体题。同一组练习若同时抽到，
  // 用户会误以为是重复出错题，这里按题干去重；若去重后不足 n 题，再用剩余题补足。
  const seen = new Set()
  const unique = []
  const rest = []
  for (const item of shuffle(bankForNote.value)) {
    const key = String(item.question || '').trim()
    if (seen.has(key)) rest.push(item)
    else { seen.add(key); unique.push(item) }
  }
  picked.value = unique.concat(rest).slice(0, n)
  answers.value = {}
  submitted.value = false
}

// 切换笔记或题量时自动重新抽题
watch([selectedNote, size], start)

// 组件 setup 阶段（仅习题页会实例化）就发起下载，与页面渲染并行；
// 比放在 onMounted 少等一次挂载往返。SSR 构建期不发请求。
const bankPromise = import.meta.env.SSR
  ? Promise.resolve([])
  : fetch('/data/questions.json').then((r) => r.json()).catch(() => [])

onMounted(async () => {
  bank.value = await bankPromise
  bankReady.value = true
  start()
})

function normalize(s) {
  return String(s).trim().toLowerCase()
}

// 填空题 / 程序设计题：答案支持多个可接受写法，忽略大小写与首尾空格
function isFillCorrect(blank, a) {
  const got = normalize(a)
  return (blank.answer || []).some((ans) => normalize(ans) === got)
}

function isSelected(q, i, k) {
  const a = answers.value[i]
  return Array.isArray(a) ? a.includes(k) : a === k
}

function answerIncludes(q, k) {
  return Array.isArray(q.answer) && q.answer.includes(k)
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
  if (q.type === 'multi') {
    if (!Array.isArray(a) || !Array.isArray(q.answer)) return false
    const norm = (x) => [...x].sort((m, n) => m - n).join(',')
    return norm(a) === norm(q.answer)
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
  if (q.type === 'multi') return (q.answer || []).map(letter).join('、')
  if (q.type === 'judge') return q.options[q.answer]
  return letter(q.answer)
}

// 多选题：点击勾选 / 取消
function toggleMulti(i, k) {
  const cur = Array.isArray(answers.value[i]) ? [...answers.value[i]] : []
  const pos = cur.indexOf(k)
  if (pos >= 0) cur.splice(pos, 1)
  else cur.push(k)
  answers.value[i] = cur
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

const gradableCount = computed(
  () => picked.value.filter((q) => q.type !== 'essay').length
)
const score = computed(() =>
  picked.value.reduce(
    (total, q, i) => total + (q.type === 'essay' ? 0 : isRight(q, i) ? 1 : 0),
    0
  )
)

const allAnswered = computed(() =>
  picked.value.every((q, i) => {
    const a = answers.value[i]
    if (q.type === 'fill' || q.type === 'essay') {
      return typeof a === 'string' && a.trim() !== ''
    }
    if (q.type === 'program') {
      if (!a) return false
      return (q.blanks || []).every(
        (_, b) => typeof a[b] === 'string' && a[b].trim() !== ''
      )
    }
    if (q.type === 'multi') return Array.isArray(a) && a.length > 0
    return a !== undefined
  })
)

const accuracy = computed(() => {
  if (!gradableCount.value) return 0
  return Math.round((score.value / gradableCount.value) * 100)
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
        // 计算分析题不计分，满分应为可判分题数，否则记录里会出现「4 / 5」这种永远拿不到的满分
        total: gradableCount.value
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
    recordsList.value = await fetchJson('/api/records', { headers: { 'x-visitor-id': visitorId() } })
  } catch (e) {
    // 登录过期：给出明确提示，而不是让成绩区默默空白
    if (e instanceof LoginExpiredError) {
      notifyAuthExpired()
      authExpired.value = true
    }
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
      <p v-if="authExpired" style="font-size:12px;line-height:1.5;color:var(--vp-c-text-2,#626463);margin:8px 0 12px">登录已过期，<a href="#" @click.prevent="relogin" style="color:var(--vp-c-brand-1,#3f403f);text-decoration:underline">点此重新登录</a>后成绩与收藏会恢复</p>
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
      <span class="quiz-total">
        {{ bankReady ? `本笔记题库共 ${bankForNote.length} 题` : '题库加载中…' }}
      </span>
    </div>

    <p v-if="!bankReady" class="quiz-tip">题库加载中，请稍候…</p>
    <p v-else class="quiz-tip">
      <strong>{{ noteLabel }}</strong> · 题库 {{ bankForNote.length }} 题 ·
      {{ topicCount }} 个知识点 · 本组随机 {{ picked.length }} 题
    </p>

    <div v-for="(q, i) in picked" :key="q.id" class="quiz-card">
      <div class="quiz-q">
        <span class="quiz-no">{{ i + 1 }}</span>
        <span class="quiz-note">{{ noteName(q.note) }}</span>
        <span class="quiz-topic">{{ q.topic }}</span>
        <p
          v-if="q.type !== 'program'"
          class="quiz-text"
          :class="{ 'is-code': q.topic && q.topic.includes('代码') }"
        >
          {{ q.question }}
        </p>
        <div v-else class="quiz-text is-code">
          <template v-for="(seg, si) in segments(q)" :key="si">
            <span v-if="seg.text">{{ seg.text }}</span>
            <input
              v-else
              class="quiz-blank"
              :aria-label="`第 ${seg.blank + 1} 空`"
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

      <!-- 单选 / 判断题 -->
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

      <!-- 多选题：可勾选多个选项 -->
      <div v-else-if="q.type === 'multi'" class="quiz-options">
        <label
          v-for="(opt, k) in q.options"
          :key="k"
          :class="{
            'is-right': submitted && answerIncludes(q, k),
            'is-wrong': submitted && isSelected(q, i, k) && !answerIncludes(q, k),
            'is-empty': !submitted && !isSelected(q, i, k)
          }"
        >
          <input
            type="checkbox"
            :checked="isSelected(q, i, k)"
            @change="toggleMulti(i, k)"
          />
          <span>{{ letter(k) }}. {{ opt }}</span>
        </label>
      </div>

      <!-- 计算分析题：写出解答过程 -->
      <textarea
        v-else-if="q.type === 'essay'"
        class="quiz-essay"
        rows="5"
        aria-label="计算分析题作答区域"
        v-model="answers[i]"
        placeholder="请写出你的计算过程与结论"
      ></textarea>

      <!-- 填空题：文本输入 -->
      <input
        v-else-if="q.type === 'fill'"
        class="quiz-fill"
        type="text"
        aria-label="填空题答案"
        v-model="answers[i]"
        placeholder="请输入答案"
      />

      <!-- 自动判分题（单选 / 判断 / 多选 / 填空 / 代码） -->
      <div
        v-if="submitted && q.type !== 'essay'"
        class="quiz-result"
        :class="isRight(q, i) ? 'ok' : 'bad'"
      >
        <strong>{{ isRight(q, i) ? '答对了' : '答错了' }}</strong>
        正确答案 {{ correctText(q) }} · {{ q.explanation }}
      </div>

      <!-- 计算分析题：展示参考答案（不计分） -->
      <div v-else-if="submitted && q.type === 'essay'" class="quiz-result self">
        <strong>参考答案</strong>
        <div v-if="q.answer" class="quiz-ref">{{ q.answer }}</div>
        <div v-if="q.explanation" class="quiz-ref">{{ q.explanation }}</div>
      </div>

      <template v-else>
        <p v-if="q.type === 'program'" class="quiz-empty-hint">
          请在框内输入答案
        </p>
        <p v-else-if="q.type === 'essay'" class="quiz-empty-hint">
          请在框内写出你的解答
        </p>
        <p
          v-else-if="q.type === 'multi' && (!Array.isArray(answers[i]) || !answers[i].length)"
          class="quiz-empty-hint"
        >
          请选择至少一个选项（可多选）
        </p>
        <p
          v-else-if="q.type === 'fill' && (!answers[i] || !answers[i].trim())"
          class="quiz-empty-hint"
        >
          请填写答案
        </p>
        <p
          v-else-if="(!q.type || q.type === 'choice' || q.type === 'judge') && answers[i] === undefined"
          class="quiz-empty-hint"
        >
          请选择一个答案
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
          本次得分 <strong>{{ score }} / {{ gradableCount }}</strong>
          <span class="quiz-acc">正确率 {{ accuracy }}%</span>
          <span v-if="picked.length > gradableCount" class="quiz-acc">
            计算分析题仅展示参考答案，不计分
          </span>
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
/* 与英语听力 / 听力训练页保持同一套卡片观感 */
.quiz-card {
  margin-bottom: 16px;
  padding: 18px 20px;
  background: var(--vp-c-bg);
  border: 1px solid var(--vp-c-divider);
  border-radius: 10px;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.04);
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
  background: var(--vp-c-bg-alt, #f4f4f2);
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
.quiz-essay {
  width: 100%;
  box-sizing: border-box;
  padding: 10px 14px;
  font-size: 14px;
  line-height: 1.7;
  font-family: inherit;
  color: var(--vp-c-text-1);
  background: var(--vp-c-bg);
  border: 1px solid var(--vp-c-divider);
  border-radius: 8px;
  resize: vertical;
}
.quiz-essay:focus {
  outline: none;
  border-color: var(--vp-c-brand-1);
}
.quiz-result.self {
  color: var(--vp-c-text-1);
  background: var(--vp-c-bg);
  border: 1px solid var(--vp-c-divider);
}
.quiz-ref {
  margin-top: 8px;
  padding: 10px 12px;
  font-size: 13px;
  line-height: 1.75;
  white-space: pre-wrap;
  overflow-wrap: anywhere;
  color: var(--vp-c-text-1);
  background: var(--vp-c-bg-soft);
  border-radius: 6px;
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

@media (max-width: 640px) {
  .quiz { margin-top: 16px; }
  .quiz-bar { padding: 12px; gap: 10px; }
  .quiz-bar label { display: inline-flex; align-items: center; }
  .quiz-total { width: 100%; margin-left: 0; }
  .quiz-card { padding: 14px; }
  .quiz-footer { gap: 10px; }
  .quiz-score { width: 100%; box-sizing: border-box; }
  .quiz-acc { display: inline-block; margin: 4px 0 0; }
  .quiz-records-list li { flex-wrap: wrap; gap: 6px; }
  .rk-date { width: 100%; margin-left: 0; }
}
</style>
