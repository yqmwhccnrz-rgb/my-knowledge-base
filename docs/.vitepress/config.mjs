import { defineConfig } from 'vitepress'
import fs from 'node:fs'
import path from 'node:path'
import { fileURLToPath } from 'node:url'

const here = path.dirname(fileURLToPath(import.meta.url))
const notesDir = path.resolve(here, '../notes')

function readTitle(file) {
  const raw = fs.readFileSync(path.join(notesDir, file), 'utf8')
  const match = raw.match(/^#\s+(.+)$/m)
  return match ? match[1].trim() : file.replace(/\.md$/, '')
}

function noteLinks() {
  if (!fs.existsSync(notesDir)) return []
  // 导读排最前，其余按文件名顺序；「原件下载」页已移除，不进导航
  const rank = (f) => (f === 'welcome.md' ? 0 : 1)
  return fs.readdirSync(notesDir)
    .filter((f) => f.endsWith('.md') && f !== 'library.md')
    .sort((a, b) => rank(a) - rank(b) || a.localeCompare(b))
    .map((f) => ({
      text: readTitle(f),
      link: `/notes/${f.replace(/\.md$/, '')}.html`
    }))
}

// 从每篇笔记里提取最关键信息，作为首页卡片的简要内容
function readSummary(file) {
  const raw = fs.readFileSync(path.join(notesDir, file), 'utf8')
  const frontmatter = raw.match(/^---\n([\s\S]*?)\n---/)
  const own = frontmatter?.[1].match(/^summary:\s*(.+)$/m)
  if (own) return own[1].trim().replace(/^["']|["']$/g, '')

  // 优先「笔记概要」里的核心内容，其次取第一段正文
  const core = raw.match(/\*\*核心内容\*\*[：:]\s*(.+)/)
  let text = core ? core[1] : ''
  if (!text) {
    const para = raw.split(/\n\s*\n/).find((p) => {
      const t = p.trim()
      return t && !/^(#|>|:::|\||---|\*\*)/.test(t)
    })
    text = para || ''
  }
  text = text
    .replace(/\[([^\]]+)\]\([^)]*\)/g, '$1')
    .replace(/[`*_]/g, '')
    .replace(/\s+/g, ' ')
    .trim()
  return text.length > 78 ? `${text.slice(0, 76)}…` : text
}

// 首页三个方框：一篇笔记一个，笔记不足时其余留空
function featureCards() {
  if (!fs.existsSync(notesDir)) return []
  const files = fs.readdirSync(notesDir)
    .filter((f) => f.endsWith('.md') && f !== 'library.md')
    .sort((a, b) => (a === 'welcome.md' ? -1 : b === 'welcome.md' ? 1 : a.localeCompare(b)))
  const cards = files.slice(0, 3).map((f) => ({
    title: readTitle(f),
    details: readSummary(f),
    link: `/notes/${f.replace(/\.md$/, '')}.html`,
    linkText: '阅读笔记'
  }))
  while (cards.length < 3) cards.push({ title: '', details: '' })
  return cards
}

const notes = noteLinks()

export default defineConfig({
  title: '我的知识库',
  description: '笔记与习题测试',
  lang: 'zh-CN',
  lastUpdated: true,
  // PWA：可安装为 App + 离线缓存已访问页面
  head: [
    ['link', { rel: 'manifest', href: '/manifest.webmanifest' }],
    ['meta', { name: 'theme-color', content: '#3451b2' }],
    ['meta', { name: 'apple-mobile-web-app-capable', content: 'yes' }],
    ['meta', { name: 'apple-mobile-web-app-status-bar-style', content: 'default' }],
    ['link', { rel: 'apple-touch-icon', href: '/icon-192.png' }],
    ['script', { src: '/register-sw.js' }]
  ],
  // 固定灰白浅色主调，不跟随访客系统的深色模式
  appearance: false,
  ignoreDeadLinks: true,
  srcExclude: ['public/**'],
  // 首页卡片由 docs/notes 自动生成，新增笔记后无需手改首页
  transformPageData(pageData) {
    if (pageData.relativePath === 'index.md' && pageData.frontmatter.layout === 'home') {
      pageData.frontmatter.features = featureCards()
    }
  },
  themeConfig: {
    nav: [
      { text: '首页', link: '/' },
      { text: '笔记', link: notes[0]?.link ?? '/' },
      { text: '习题测试', link: '/quiz.html' },
      { text: '听力训练', link: '/dictation.html' }
    ],
    sidebar: [
      // 英语听力已归入笔记板块
      { text: '笔记', items: [...notes, { text: '英语听力', link: '/listening' }] },
      {
        text: '练习',
        items: [
          { text: '习题测试', link: '/quiz' },
          { text: '听力训练', link: '/dictation' }
        ]
      }
    ],
    search: { provider: 'local' },
    outline: { level: [2, 3], label: '本页目录' },
    docFooter: { prev: false, next: false },
    returnToTopLabel: '回到顶部',
    sidebarMenuLabel: '目录',
    darkModeSwitchLabel: '外观',
    lightModeSwitchTitle: '切换到浅色',
    darkModeSwitchTitle: '切换到深色',
    skipToContentLabel: '跳到正文'
  }
})
