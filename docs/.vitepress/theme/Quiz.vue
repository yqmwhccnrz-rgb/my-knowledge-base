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

const score = computed(() =>
  picked.value.reduce(
    (total, q, i) => total + (answers.value[i] === q.answer ? 1 : 0),
    0
  )
)

const allAnswered = computed(() =>
  picked.value.every((_, i) => answers.value[i] !== undefined)
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
          <option :value="3">3 题</option>
          <option :value="5">5 题</option>
          <option :value="bankForNote.length">全部</option>
        </select>
      </label>
      <button class="quiz-btn" type="button" @click="start">换一组题</button>
    </div>

    <p class="quiz-tip">
      当前展示 <strong>{{ noteLabel }}</strong> 的习题，题库共
      {{ bankForNote.length }} 道，覆盖 {{ topicCount }} 个知识点方向；本次随机抽取
      {{ picked.length }} 道。
    </p>

    <div v-for="(q, i) in picked" :key="q.id" class="quiz-card">
      <div class="quiz-q">
        <span class="quiz-no">{{ i + 1 }}</span>
        <span class="quiz-topic">{{ q.topic }}</span>
        <p class="quiz-text">{{ q.question }}</p>
      </div>
      <div class="quiz-options">
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
      <div
        v-if="submitted"
        class="quiz-result"
        :class="answers[i] === q.answer ? 'ok' : 'bad'"
      >
        <strong>{{ answers[i] === q.answer ? '答对了' : '答错了' }}</strong>
        正确答案 {{ letter(q.answer) }} · {{ q.explanation }}
      </div>
      <p v-else-if="answers[i] === undefined" class="quiz-empty-hint">
        请选择一个答案
      </p>
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
      </template>
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
.quiz-topic {
  font-size: 12px;
  color: var(--vp-c-text-2);
}
.quiz-text {
  margin: 10px 0 0;
  font-size: 15px;
  line-height: 1.7;
  color: var(--vp-c-text-1);
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
</style>
