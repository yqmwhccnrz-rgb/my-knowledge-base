<script setup>
import { ref, reactive, computed, onMounted } from 'vue'

// 题库放在 /data/ 下由浏览器原生 fetch 加载，不打进 JS chunk；仅本页会实例化。
const dataPromise = import.meta.env.SSR
  ? Promise.resolve(null)
  : fetch('/data/reading.json').then((r) => r.json()).catch(() => null)

const phrases = ref([])
const readings = ref([])
const writings = ref([])
const translations = ref([])
const ready = ref(false)

// 题型：phrase=词组填空，reading=短篇阅读，writing=写作练习，translation=翻译练习；难度：all / CET-4 / CET-6
const mode = ref('phrase')
const level = ref('all')

// 当前练习在对应列表中的下标，用于「换一组」
const idx = ref(0)
// 作答状态：phrase 用 { 空号: 选项字母 }，reading 用 { 题号: 选项下标 }
const answers = reactive({})
const submitted = ref(false)
// 写作/翻译为主观题：草稿文本与「对照参考」开关，不自动判分
const draft = ref('')
const revealed = ref(false)

onMounted(async () => {
  const d = await dataPromise
  if (d && Array.isArray(d.phrase)) phrases.value = d.phrase
  if (d && Array.isArray(d.reading)) readings.value = d.reading
  if (d && Array.isArray(d.writing)) writings.value = d.writing
  if (d && Array.isArray(d.translation)) translations.value = d.translation
  ready.value = true
  pick(0)
})

const SRC = { phrase: phrases, reading: readings, writing: writings, translation: translations }
const list = computed(() => {
  const src = (SRC[mode.value] || phrases).value
  return level.value === 'all' ? src : src.filter((x) => x.level === level.value)
})
const current = computed(() => list.value[idx.value] || null)

function pick(n) {
  const len = list.value.length
  idx.value = len ? ((n % len) + len) % len : 0
  submitted.value = false
  revealed.value = false
  draft.value = ''
  for (const k of Object.keys(answers)) delete answers[k]
}
function next() { pick(idx.value + 1) }
function prev() { pick(idx.value - 1) }

function switchMode(m) {
  if (mode.value === m) return
  mode.value = m
  pick(0)
}
function onLevel() { pick(0) }

function submit() { submitted.value = true }
function reset() {
  submitted.value = false
  revealed.value = false
  draft.value = ''
  for (const k of Object.keys(answers)) delete answers[k]
}

// 主观题（写作/翻译）字数统计：英文按单词、中文按字
function draftWords() {
  const t = draft.value.trim()
  if (!t) return 0
  const en = t.match(/[A-Za-z']+/g)
  return en ? en.length : 0
}
const MODE_NAME = { phrase: '词组填空', reading: '短篇阅读', writing: '写作练习', translation: '翻译练习' }

// ---------- 词组填空 ----------
const blanks = computed(() => {
  if (!current.value || mode.value !== 'phrase') return []
  return Object.keys(current.value.answers).map(Number).sort((a, b) => a - b)
})
function bankMap(item) {
  const m = {}
  for (const b of item.bank) m[b.key] = b
  return m
}
function blankRight(item, n) {
  return submitted.value && answers[n] === item.answers[n]
}
function phraseAnswered() {
  return blanks.value.every((n) => answers[n] !== undefined)
}
function phraseScore(item) {
  return blanks.value.filter((n) => answers[n] === item.answers[n]).length
}
// 把 passage 里的 {1}{2} 拆成文本段与空格段
function segments(text) {
  return text.split(/(\{\d+\})/).map((s) => {
    const m = /^\{(\d+)\}$/.exec(s)
    return m ? { blank: Number(m[1]) } : { text: s }
  })
}

// ---------- 短篇阅读 ----------
function readingAnswered(item) {
  return item.questions.every((_, j) => answers[j] !== undefined)
}
function readingScore(item) {
  return item.questions.filter((q, j) => answers[j] === q.answer).length
}
function letter(k) { return String.fromCharCode(65 + k) }
const QTYPE = { detail: '细节理解', inference: '推理判断', vocab: '词义猜测', main: '主旨大意', attitude: '观点态度' }
</script>

<template>
  <div class="rd">
    <!-- 筛选栏 -->
    <div class="rd-bar">
      <div class="rd-tabs" role="tablist">
        <button type="button" :class="{ on: mode === 'phrase' }" @click="switchMode('phrase')">词组填空</button>
        <button type="button" :class="{ on: mode === 'reading' }" @click="switchMode('reading')">短篇阅读</button>
        <button type="button" :class="{ on: mode === 'writing' }" @click="switchMode('writing')">写作练习</button>
        <button type="button" :class="{ on: mode === 'translation' }" @click="switchMode('translation')">翻译练习</button>
      </div>
      <label class="rd-level">
        难度
        <select v-model="level" @change="onLevel">
          <option value="all">全部</option>
          <option value="CET-4">英语四级 CET-4</option>
          <option value="CET-6">英语六级 CET-6</option>
        </select>
      </label>
      <div class="rd-nav">
        <button class="rd-btn" type="button" :disabled="list.length < 2" @click="prev">‹ 上一组</button>
        <span class="rd-pos">{{ list.length ? idx + 1 : 0 }} / {{ list.length }}</span>
        <button class="rd-btn" type="button" :disabled="list.length < 2" @click="next">下一组 ›</button>
      </div>
    </div>

    <p v-if="!ready" class="rd-tip">题库加载中，请稍候…</p>
    <p v-else-if="!current" class="rd-tip">该难度下暂无题目，请切换难度或题型。</p>

    <template v-else>
      <!-- 说明条 -->
      <p class="rd-tip">
        <strong>{{ MODE_NAME[mode] }}</strong>
        · <span class="rd-badge" :class="current.level === 'CET-6' ? 'c6' : 'c4'">{{ current.level }}</span>
        · {{ current.topic }} · 共 {{ list.length }} {{ mode === 'phrase' ? '段' : mode === 'reading' ? '篇' : '题' }}
        <span v-if="mode === 'phrase'"> · 本段 {{ blanks.length }} 空</span>
        <span v-else-if="mode === 'reading'"> · 本篇 {{ current.questions.length }} 题 · 约 {{ current.passage.split(' ').length }} 词</span>
        <span v-else-if="mode === 'writing'"> · 建议用时 10 分钟</span>
        <span v-else> · 建议用时 5 分钟</span>
      </p>

      <!-- ============ 词组填空 ============ -->
      <div v-if="mode === 'phrase'" class="rd-card">
        <h3 class="rd-title">{{ current.title }}</h3>
        <p class="rd-hint">从下方词组库中选择合适的词组填入空格（填字母即可，部分词组可重复使用）。</p>

        <div class="rd-passage">
          <template v-for="(seg, si) in segments(current.passage)" :key="si">
            <span v-if="seg.text !== undefined">{{ seg.text }}</span>
            <select
              v-else
              class="rd-blank"
              :class="{
                ok: submitted && blankRight(current, seg.blank),
                bad: submitted && !blankRight(current, seg.blank)
              }"
              :aria-label="`第 ${seg.blank} 空`"
              :disabled="submitted"
              :value="answers[seg.blank] || ''"
              @change="answers[seg.blank] = $event.target.value || undefined"
            >
              <option value="" disabled>__{{ seg.blank }}__</option>
              <option v-for="b in current.bank" :key="b.key" :value="b.key">{{ b.key }}. {{ b.en }}</option>
            </select>
          </template>
        </div>

        <div class="rd-bank">
          <div class="rd-bank-t">词组库 Word Bank</div>
          <div class="rd-bank-list">
            <span v-for="b in current.bank" :key="b.key" class="rd-bank-item">
              <b>{{ b.key }}.</b> {{ b.en }}
              <em v-if="submitted"> {{ b.zh }}</em>
            </span>
          </div>
          <p v-if="!submitted" class="rd-bank-note">作答时不显示中文释义，提交后统一揭晓。</p>
        </div>

        <div v-if="submitted" class="rd-score">
          本段答对 <strong>{{ phraseScore(current) }}</strong> / {{ blanks.length }} 空
        </div>
        <div v-if="submitted" class="rd-explains">
          <div v-for="n in blanks" :key="n" class="rd-explain" :class="blankRight(current, n) ? 'ok' : 'bad'">
            <span class="rd-ex-no">{{ n }}</span>
            <div>
              <strong>{{ blankRight(current, n) ? '正确' : '答错' }}</strong>
              · 答案 {{ current.answers[n] }}. {{ bankMap(current)[current.answers[n]].en }}
              <span class="rd-zh">{{ bankMap(current)[current.answers[n]].zh }}</span>
              <p>{{ current.explain[n] }}</p>
            </div>
          </div>
        </div>

        <div class="rd-footer">
          <button v-if="!submitted" class="rd-btn primary" type="button" :disabled="!phraseAnswered()" @click="submit">
            提交判分
          </button>
          <template v-else>
            <button class="rd-btn" type="button" @click="reset">重做本段</button>
            <button class="rd-btn primary" type="button" @click="next">下一组 ›</button>
          </template>
          <span v-if="!submitted && !phraseAnswered()" class="rd-foot-hint">请填完所有空格</span>
        </div>
      </div>

      <!-- ============ 短篇阅读 ============ -->
      <div v-else-if="mode === 'reading'" class="rd-card">
        <h3 class="rd-title">{{ current.title }}</h3>
        <p class="rd-hint">先通读短文，再回答后面的选择题。</p>

        <div class="rd-article">{{ current.passage }}</div>

        <details v-if="current.glossary && current.glossary.length" class="rd-gloss">
          <summary>生词注释（{{ current.glossary.length }}）</summary>
          <div class="rd-gloss-list">
            <span v-for="(g, gi) in current.glossary" :key="gi"><b>{{ g.en }}</b> {{ g.zh }}</span>
          </div>
        </details>

        <div v-for="(q, j) in current.questions" :key="j" class="rd-q">
          <div class="rd-q-head">
            <span class="rd-no">{{ j + 1 }}</span>
            <span class="rd-qtype">{{ QTYPE[q.type] || '阅读理解' }}</span>
            <p class="rd-q-text">{{ q.q }}</p>
          </div>
          <div class="rd-options">
            <label
              v-for="(opt, k) in q.options"
              :key="k"
              :class="{
                ok: submitted && k === q.answer,
                bad: submitted && answers[j] === k && k !== q.answer,
                dim: submitted && k !== q.answer && answers[j] !== k
              }"
            >
              <input
                type="radio"
                :name="`rd-${current.id}-${j}`"
                :value="k"
                :checked="answers[j] === k"
                :disabled="submitted"
                @change="answers[j] = k"
              />
              <span>{{ letter(k) }}. {{ opt }}</span>
            </label>
          </div>
          <div v-if="submitted" class="rd-q-result" :class="answers[j] === q.answer ? 'ok' : 'bad'">
            <strong>{{ answers[j] === q.answer ? '答对了' : '答错了' }}</strong>
            正确答案 {{ letter(q.answer) }} · {{ q.explain }}
          </div>
        </div>

        <div v-if="submitted" class="rd-score">
          本篇答对 <strong>{{ readingScore(current) }}</strong> / {{ current.questions.length }} 题
        </div>

        <div class="rd-footer">
          <button v-if="!submitted" class="rd-btn primary" type="button" :disabled="!readingAnswered(current)" @click="submit">
            提交判分
          </button>
          <template v-else>
            <button class="rd-btn" type="button" @click="reset">重做本篇</button>
            <button class="rd-btn primary" type="button" @click="next">下一篇 ›</button>
          </template>
          <span v-if="!submitted && !readingAnswered(current)" class="rd-foot-hint">请完成所有题目</span>
        </div>
      </div>

      <!-- ============ 写作练习 ============ -->
      <div v-else-if="mode === 'writing'" class="rd-card">
        <h3 class="rd-title">{{ current.title }}</h3>
        <p class="rd-hint">先审题列提纲，再在下方写 2–3 段短文；写完可对照思路提纲与参考范文自查。</p>

        <div class="rd-prompt">{{ current.prompt }}</div>
        <p v-if="current.promptZh" class="rd-prompt-zh">题意：{{ current.promptZh }}</p>

        <details class="rd-gloss">
          <summary>写作思路提纲（{{ current.outline.length }} 条）</summary>
          <ol class="rd-outline">
            <li v-for="(o, oi) in current.outline" :key="oi">{{ o }}</li>
          </ol>
        </details>

        <div class="rd-write">
          <div class="rd-write-head">
            <span>我的作文</span>
            <span class="rd-count">已写约 {{ draftWords() }} 词</span>
          </div>
          <textarea
            v-model="draft"
            class="rd-textarea"
            rows="10"
            placeholder="在这里写下你的短文（建议 80–120 词）…"
          ></textarea>
        </div>

        <div class="rd-footer">
          <button v-if="!revealed" class="rd-btn primary" type="button" :disabled="!draft.trim()" @click="revealed = true">
            写完，对照参考
          </button>
          <template v-else>
            <button class="rd-btn" type="button" @click="revealed = false">收起参考</button>
            <button class="rd-btn primary" type="button" @click="next">下一题 ›</button>
          </template>
          <span v-if="!revealed && !draft.trim()" class="rd-foot-hint">先写几句再对照参考</span>
        </div>

        <div v-if="revealed" class="rd-ref">
          <div class="rd-ref-t">参考范文 Model Essay</div>
          <div class="rd-article">{{ current.model }}</div>
          <div class="rd-bank">
            <div class="rd-bank-t">亮点表达 Expressions</div>
            <div class="rd-bank-list">
              <span v-for="(e, ei) in current.expressions" :key="ei" class="rd-bank-item">
                <b>{{ e.en }}</b> <em>{{ e.zh }}</em>
              </span>
            </div>
          </div>
        </div>
      </div>

      <!-- ============ 翻译练习 ============ -->
      <div v-else class="rd-card">
        <h3 class="rd-title">{{ current.title }}</h3>
        <p class="rd-hint">将下面的中文段落译成英文（2–3 句）；可先查看关键词组提示，再对照参考译文与考点。</p>

        <div class="rd-source">{{ current.source }}</div>

        <details class="rd-gloss" open>
          <summary>关键词组提示（{{ current.hints.length }}）</summary>
          <div class="rd-gloss-list">
            <span v-for="(h, hi) in current.hints" :key="hi"><b>{{ h.zh }}</b> {{ h.en }}</span>
          </div>
        </details>

        <div class="rd-write">
          <div class="rd-write-head">
            <span>我的译文</span>
            <span class="rd-count">已写约 {{ draftWords() }} 词</span>
          </div>
          <textarea
            v-model="draft"
            class="rd-textarea"
            rows="6"
            placeholder="在这里写下你的英文译文…"
          ></textarea>
        </div>

        <div class="rd-footer">
          <button v-if="!revealed" class="rd-btn primary" type="button" :disabled="!draft.trim()" @click="revealed = true">
            译完，对照参考
          </button>
          <template v-else>
            <button class="rd-btn" type="button" @click="revealed = false">收起参考</button>
            <button class="rd-btn primary" type="button" @click="next">下一题 ›</button>
          </template>
          <span v-if="!revealed && !draft.trim()" class="rd-foot-hint">先译出来再对照参考</span>
        </div>

        <div v-if="revealed" class="rd-ref">
          <div class="rd-ref-t">参考译文 Reference Translation</div>
          <div class="rd-article">{{ current.ref }}</div>
          <div class="rd-bank">
            <div class="rd-bank-t">考点点拨 Key Points</div>
            <ol class="rd-outline">
              <li v-for="(p, pi) in current.points" :key="pi">{{ p }}</li>
            </ol>
          </div>
        </div>
      </div>
    </template>
  </div>
</template>

<style scoped>
.rd { margin-top: 24px; }
.rd-bar {
  display: flex; flex-wrap: wrap; align-items: center; gap: 12px;
  padding: 12px 16px; background: var(--vp-c-bg-soft, #f4f4f2);
  border: 1px solid var(--vp-c-divider, rgba(0,0,0,.085)); border-radius: 10px;
}
.rd-tabs { display: inline-flex; border: 1px solid var(--vp-c-divider); border-radius: 8px; overflow: hidden; }
.rd-tabs button {
  padding: 7px 16px; font-size: 13px; cursor: pointer; border: none;
  background: var(--vp-c-bg, #fff); color: var(--vp-c-text-2, #626463);
}
.rd-tabs button + button { border-left: 1px solid var(--vp-c-divider); }
.rd-tabs button.on { background: var(--vp-c-brand-1, #3f403f); color: #fff; font-weight: 600; }
.rd-level { font-size: 13px; color: var(--vp-c-text-2); }
.rd-level select {
  margin-left: 8px; padding: 6px 10px; font-size: 13px;
  color: var(--vp-c-text-1); background: var(--vp-c-bg, #fff);
  border: 1px solid var(--vp-c-divider); border-radius: 6px;
}
.rd-nav { margin-left: auto; display: flex; align-items: center; gap: 10px; }
.rd-pos { font-size: 13px; color: var(--vp-c-text-2); white-space: nowrap; }
.rd-btn {
  padding: 7px 14px; font-size: 13px; color: var(--vp-c-brand-1, #3f403f);
  background: var(--vp-c-bg, #fff); border: 1px solid var(--vp-c-brand-1, #3f403f);
  border-radius: 6px; cursor: pointer;
}
.rd-btn.primary { color: #fff; background: var(--vp-c-brand-1, #3f403f); padding: 10px 20px; }
.rd-btn:disabled { opacity: .45; cursor: not-allowed; }
.rd-tip { margin: 14px 0 18px; font-size: 13px; color: var(--vp-c-text-2); }
.rd-tip strong { color: var(--vp-c-text-1); }
.rd-badge {
  display: inline-block; padding: 1px 8px; border-radius: 999px; font-size: 11px;
  border: 1px solid var(--vp-c-divider);
}
.rd-badge.c4 { color: #2f6b4f; background: rgba(47,107,79,.08); border-color: rgba(47,107,79,.25); }
.rd-badge.c6 { color: #8a5a1f; background: rgba(138,90,31,.08); border-color: rgba(138,90,31,.25); }

.rd-card {
  padding: 20px 22px; background: var(--vp-c-bg, #fff);
  border: 1px solid var(--vp-c-divider); border-radius: 12px;
}
.rd-title { margin: 0 0 4px; font-size: 18px; font-weight: 650; color: var(--vp-c-text-1); }
.rd-hint { margin: 0 0 16px; font-size: 12.5px; color: var(--vp-c-text-3, #8d8f8d); }

.rd-passage {
  font-size: 15px; line-height: 2.15; color: var(--vp-c-text-1);
  padding: 16px 18px; background: var(--vp-c-bg-soft, #f4f4f2);
  border: 1px solid var(--vp-c-divider); border-radius: 10px;
}
.rd-blank {
  display: inline-block; margin: 0 3px; padding: 2px 6px; min-width: 92px;
  font-size: 13px; font-family: inherit; line-height: 1.6; vertical-align: baseline;
  color: var(--vp-c-text-1); background: var(--vp-c-bg, #fff);
  border: 1px solid var(--vp-c-brand-1, #3f403f); border-radius: 6px; cursor: pointer;
}
.rd-blank.ok { color: #2f6b4f; background: rgba(47,107,79,.10); border-color: #2f6b4f; }
.rd-blank.bad { color: #b23b3b; background: rgba(178,59,59,.10); border-color: #b23b3b; }
.rd-blank:disabled { cursor: default; opacity: 1; }

.rd-bank { margin-top: 16px; }
.rd-bank-t { font-size: 12px; font-weight: 600; color: var(--vp-c-text-2); margin-bottom: 8px; letter-spacing: .02em; }
.rd-bank-list { display: flex; flex-wrap: wrap; gap: 8px 18px; }
.rd-bank-item { font-size: 13px; color: var(--vp-c-text-1); }
.rd-bank-item b { color: var(--vp-c-brand-1); }
.rd-bank-item em { color: var(--vp-c-text-2); font-style: normal; font-size: 12px; }
.rd-bank-note { margin: 8px 0 0; font-size: 11.5px; color: var(--vp-c-text-3); }

.rd-article {
  font-size: 14.5px; line-height: 1.95; color: var(--vp-c-text-1);
  padding: 16px 18px; background: var(--vp-c-bg-soft, #f4f4f2);
  border: 1px solid var(--vp-c-divider); border-radius: 10px;
}
.rd-prompt {
  font-size: 14.5px; line-height: 1.95; color: var(--vp-c-text-1);
  padding: 14px 18px; background: var(--vp-c-bg-soft, #f4f4f2);
  border: 1px solid var(--vp-c-divider); border-left: 3px solid var(--vp-c-brand-1, #3f403f);
  border-radius: 10px; white-space: pre-line;
}
.rd-prompt-zh { margin: 10px 2px 0; font-size: 12.5px; color: var(--vp-c-text-2); }
.rd-source {
  font-size: 15.5px; line-height: 2.1; color: var(--vp-c-text-1);
  padding: 16px 18px; background: var(--vp-c-bg-soft, #f4f4f2);
  border: 1px solid var(--vp-c-divider); border-left: 3px solid var(--vp-c-brand-1, #3f403f);
  border-radius: 10px;
}
.rd-outline { margin: 10px 4px 4px; padding-left: 20px; font-size: 13px; line-height: 1.9; color: var(--vp-c-text-1); }
.rd-write { margin-top: 16px; }
.rd-write-head {
  display: flex; justify-content: space-between; align-items: baseline;
  margin-bottom: 8px; font-size: 12.5px; font-weight: 600; color: var(--vp-c-text-2);
}
.rd-count { font-weight: 400; color: var(--vp-c-text-3); }
.rd-textarea {
  width: 100%; padding: 12px 14px; font-size: 14px; line-height: 1.9;
  font-family: inherit; color: var(--vp-c-text-1);
  background: var(--vp-c-bg, #fff); border: 1px solid var(--vp-c-divider);
  border-radius: 10px; resize: vertical; outline: none;
}
.rd-textarea:focus { border-color: var(--vp-c-brand-1, #3f403f); }
.rd-ref { margin-top: 18px; }
.rd-ref-t { margin-bottom: 8px; font-size: 12.5px; font-weight: 600; color: var(--vp-c-brand-1, #3f403f); letter-spacing: .02em; }
.rd-gloss { margin: 12px 0 4px; font-size: 12.5px; color: var(--vp-c-text-2); }
.rd-gloss summary { cursor: pointer; }
.rd-gloss-list { display: flex; flex-wrap: wrap; gap: 6px 20px; padding: 10px 4px; }
.rd-gloss-list b { color: var(--vp-c-text-1); }

.rd-q { margin-top: 22px; }
.rd-q-head { display: flex; flex-wrap: wrap; align-items: baseline; gap: 8px; }
.rd-no {
  display: inline-flex; align-items: center; justify-content: center;
  width: 22px; height: 22px; border-radius: 50%; font-size: 12px; font-weight: 600;
  color: #fff; background: var(--vp-c-brand-1, #3f403f); flex: none;
}
.rd-qtype { font-size: 11px; color: var(--vp-c-text-3); border: 1px solid var(--vp-c-divider); border-radius: 999px; padding: 1px 8px; }
.rd-q-text { flex: 1 1 100%; margin: 4px 0 8px; font-size: 14px; font-weight: 500; color: var(--vp-c-text-1); }
.rd-options { display: flex; flex-direction: column; gap: 6px; }
.rd-options label {
  display: flex; align-items: flex-start; gap: 8px; padding: 8px 12px;
  font-size: 13.5px; line-height: 1.6; color: var(--vp-c-text-1);
  border: 1px solid var(--vp-c-divider); border-radius: 8px; cursor: pointer;
  transition: background .15s, border-color .15s;
}
.rd-options label:hover { background: var(--vp-c-bg-soft); }
.rd-options input { margin-top: 4px; flex: none; }
.rd-options label.ok { background: rgba(47,107,79,.10); border-color: #2f6b4f; color: #2f6b4f; }
.rd-options label.bad { background: rgba(178,59,59,.10); border-color: #b23b3b; color: #b23b3b; }
.rd-options label.dim { opacity: .6; }
.rd-q-result { margin-top: 8px; padding: 8px 12px; font-size: 12.5px; line-height: 1.7; border-radius: 8px; }
.rd-q-result.ok { background: rgba(47,107,79,.08); color: #2f6b4f; }
.rd-q-result.bad { background: rgba(178,59,59,.08); color: #b23b3b; }

.rd-explains { margin-top: 14px; display: flex; flex-direction: column; gap: 8px; }
.rd-explain { display: flex; gap: 10px; padding: 10px 12px; font-size: 12.5px; line-height: 1.7; border-radius: 8px; }
.rd-explain.ok { background: rgba(47,107,79,.07); }
.rd-explain.bad { background: rgba(178,59,59,.07); }
.rd-ex-no { flex: none; width: 20px; height: 20px; border-radius: 50%; display: inline-flex; align-items: center; justify-content: center; font-size: 11px; color: #fff; background: var(--vp-c-text-3); }
.rd-explain strong { color: var(--vp-c-text-1); }
.rd-explain p { margin: 2px 0 0; color: var(--vp-c-text-2); }
.rd-zh { color: var(--vp-c-text-2); }

.rd-score {
  margin-top: 18px; padding: 10px 14px; font-size: 14px; color: var(--vp-c-text-1);
  background: var(--vp-c-bg-soft); border: 1px solid var(--vp-c-divider); border-radius: 8px;
}
.rd-score strong { color: var(--vp-c-brand-1); font-size: 17px; }
.rd-footer { display: flex; flex-wrap: wrap; align-items: center; gap: 12px; margin-top: 20px; }
.rd-foot-hint { font-size: 12px; color: var(--vp-c-text-3); }

@media (max-width: 640px) {
  .rd-card { padding: 16px 14px; }
  .rd-nav { margin-left: 0; width: 100%; justify-content: space-between; }
  .rd-passage, .rd-article { font-size: 14px; padding: 12px 13px; }
  .rd-blank { min-width: 76px; }
}
</style>
