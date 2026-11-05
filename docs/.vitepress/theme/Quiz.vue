<script setup>
import { ref, computed } from 'vue'
import bank from './data/questions.json'

const size = ref(3)
const picked = ref([])
const answers = ref({})
const submitted = ref(false)

const topicCount = computed(() => new Set(bank.map((q) => q.topic)).size)

function shuffle(list) {
  const arr = [...list]
  for (let i = arr.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1))
    ;[arr[i], arr[j]] = [arr[j], arr[i]]
  }
  return arr
}

function start() {
  const n = Math.min(Number(size.value), bank.length)
  picked.value = shuffle(bank).slice(0, n)
  answers.value = {}
  submitted.value = false
}

const score = computed(() =>
  picked.value.reduce(
    (total, q, i) => total + (answers.value[i] === q.answer ? 1 : 0),
    0
  )
)

const allAnswered = computed(() =>
  picked.value.every((_, i) => answers.value[i] !== undefined)
)

function letter(n) {
  return String.fromCharCode(65 + n)
}

start()
</script>

<template>
  <div class="quiz">
    <div class="quiz-bar">
      <label>
        每次抽题
        <select v-model.number="size">
          <option :value="3">3 题</option>
          <option :value="5">5 题</option>
          <option :value="bank.length">全部</option>
        </select>
      </label>
      <button class="quiz-btn" type="button" @click="start">重新抽一组</button>
    </div>

    <p class="quiz-tip">
      题目从题库随机抽取，当前共 {{ bank.length }} 道，覆盖 {{ topicCount }} 个知识点方向。
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
            'is-wrong': submitted && answers[i] === k && k !== q.answer
          }"
        >
          <input
            type="radio"
            :name="`q-${q.id}`"
            :value="k"
            v-model="answers[i]"
            :disabled="submitted"
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
    </div>

    <div class="quiz-footer">
      <button
        v-if="!submitted"
        class="quiz-btn primary"
        type="button"
        :disabled="!allAnswered"
        @click="submit"
      >
        提交并查看解析
      </button>
      <div v-else class="quiz-score">
        本次得分 <strong>{{ score }} / {{ picked.length }}</strong>
      </div>
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
.quiz-options label.is-right {
  border-color: var(--vp-c-brand-1);
  background: var(--vp-c-brand-soft);
}
.quiz-options label.is-wrong {
  border-color: #c0392b;
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
.quiz-footer {
  margin-top: 20px;
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
</style>
