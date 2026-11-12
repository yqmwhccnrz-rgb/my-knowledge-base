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

// 首页卡片覆盖全部笔记，避免只有按字母序的前三篇能被首页直达。
// 顺序与侧栏一致（welcome.md 导读排最前，其余按文件名）。生成的卡片由
// HomeNotes 组件以左右滑动轮播展示（一次一张），不再走 VitePress 默认网格。
function featureCards() {
  if (!fs.existsSync(notesDir)) return []
  const files = fs.readdirSync(notesDir)
    .filter((f) => f.endsWith('.md') && f !== 'library.md')
    .sort((a, b) => {
      const rank = (x) => (x === 'welcome.md' ? 0 : 1)
      return rank(a) - rank(b) || a.localeCompare(b)
    })
  return files.map((f) => ({
    title: readTitle(f),
    details: readSummary(f),
    link: `/notes/${f.replace(/\.md$/, '')}.html`,
    linkText: '阅读笔记'
  }))
}

// 每页独立的 description，避免全站共用一句站点描述（利于搜索结果与分享卡片）
const PAGE_DESCRIPTIONS = {
  'index.md': '个人知识库：10 门课程精要笔记、1862 道习题、四六级英语阅读、75 段英语听力与 200 题听写训练，能读、能查、能练。',
  'quiz.md': '按 10 门科目随机抽题，覆盖单选、多选、判断、填空、程序设计与计算分析题，提交后即时判分并查看解析。',
  'listening.md': '75 段英语听力真题，按章节与分段筛选，支持逐句高亮对照英文原文与中文翻译。',
  'dictation.md': '200 个听写片段，盲听打字后逐词比对，可逐题查看英文原文与中文翻译。',
  'reading.md': '英语阅读练习：四六级词组填空与短篇阅读选择，含中文释义与逐题解析，可按 CET-4 / CET-6 难度切换。'
}

function readNoteDescription(file) {
  const raw = fs.readFileSync(path.join(notesDir, file), 'utf8')
  const m = raw.match(/^---\n([\s\S]*?)\n---/)
  const own = m?.[1].match(/^summary:\s*(.+)$/m)
  if (!own) return ''
  return own[1].trim().replace(/^["']|["']$/g, '')
}

function pageDescription(relativePath) {
  if (PAGE_DESCRIPTIONS[relativePath]) return PAGE_DESCRIPTIONS[relativePath]
  const name = relativePath.startsWith('notes/') ? relativePath.slice(6) : ''
  if (name.endsWith('.md')) {
    const d = readNoteDescription(name)
    if (d) return d
  }
  return ''
}

function cleanDescription(text) {
  const s = String(text).replace(/\s+/g, ' ').trim()
  return s.length > 150 ? `${s.slice(0, 148)}…` : s
}

const notes = noteLinks()

export default defineConfig({
  title: '我的知识库',
  description: '笔记与习题测试',
  lang: 'zh-CN',
  // 关掉「Last updated」：Cloudflare Pages 用浅克隆构建，git 时间等于构建时间，
  // 各页显示的日期都相同且失真，英文文案也与全站中文不一致，容易误导。
  lastUpdated: false,
  // PWA：可安装为 App + 离线缓存已访问页面
  head: [
    ['link', { rel: 'icon', type: 'image/svg+xml', href: '/icon.svg' }],
    ['link', { rel: 'manifest', href: '/manifest.webmanifest' }],
    // 与站点灰白主调一致（原为 VitePress 默认蓝）
    ['meta', { name: 'theme-color', content: '#fafaf9' }],
    ['meta', { name: 'apple-mobile-web-app-capable', content: 'yes' }],
    ['meta', { name: 'apple-mobile-web-app-title', content: '我的知识库' }],
    ['meta', { name: 'apple-mobile-web-app-status-bar-style', content: 'default' }],
    ['link', { rel: 'apple-touch-icon', href: '/icon-192.png' }],
    ['script', { src: '/register-sw.js', defer: '' }]
  ],
  // 固定灰白浅色主调，不跟随访客系统的深色模式
  appearance: false,
  // 关掉 VitePress 的全站自动预取：侧栏 8 篇笔记链接都在视口内，会一次性预取
  // 约 1.4MB 的完整页面 chunk，与题库/听力数据争抢带宽。站内导航由浏览器 HTTP
  // 缓存与 Service Worker 缓存保障，点击时按需加载即可。
  router: { prefetchLinks: false },
  ignoreDeadLinks: true,
  srcExclude: ['public/**'],
  // 首页笔记卡片由 docs/notes 自动生成，新增笔记后无需手改首页；
  // 数据写入 noteCards（而非默认的 features），这样 VitePress 默认网格不渲染，
  // 改由自定义 HomeNotes 组件以左右滑动轮播形式展示，一次显示一张。
  // 同时为每页写入独立 description（SSR 与客户端路由都会用到）
  transformPageData(pageData) {
    const rp = pageData.relativePath || ''
    if (rp === 'index.md' && pageData.frontmatter.layout === 'home') {
      pageData.frontmatter.noteCards = featureCards()
    }
    const desc = pageDescription(rp)
    if (desc) return { description: cleanDescription(desc) }
  },
  // 去掉 VitePress 默认注入的 Inter 字体 preload 标签：站点已统一用系统字体，
  // 无需下载 66KB 的 woff2（@font-face 的 Inter 也因字体变量被覆盖而不再被引用）。
  async transformHtml(html) {
    return html.replace(/<link rel="preload"[^>]*inter-roman[^>]*>/g, '')
  },
  // 社交分享卡片（Open Graph / Twitter）
  transformHead({ title, description }) {
    const desc = cleanDescription(description || '笔记与习题测试')
    return [
      ['meta', { property: 'og:type', content: 'website' }],
      ['meta', { property: 'og:site_name', content: '我的知识库' }],
      ['meta', { property: 'og:title', content: title }],
      ['meta', { property: 'og:description', content: desc }],
      ['meta', { name: 'twitter:card', content: 'summary' }],
      ['meta', { name: 'twitter:title', content: title }],
      ['meta', { name: 'twitter:description', content: desc }]
    ]
  },
  themeConfig: {
    nav: [
      { text: '首页', link: '/' },
      { text: '笔记', link: notes[0]?.link ?? '/' },
      { text: '习题测试', link: '/quiz.html' },
      { text: '英语阅读', link: '/reading.html' },
      { text: '听力训练', link: '/dictation.html' }
    ],
    sidebar: [
      // 英语听力已归入笔记板块；链接统一带 .html，和 nav 保持一致
      { text: '笔记', items: [...notes, { text: '英语听力', link: '/listening.html' }] },
      {
        text: '练习',
        items: [
          { text: '习题测试', link: '/quiz.html' },
          { text: '英语阅读', link: '/reading.html' },
          { text: '听力训练', link: '/dictation.html' }
        ]
      }
    ],
    search: {
      provider: 'local',
      options: {
        translations: {
          button: { buttonText: '搜索', buttonAriaLabel: '搜索' },
          modal: {
            noResultsText: '没有找到相关内容',
            resetButtonTitle: '清除搜索',
            footer: { selectText: '选择', navigateText: '切换', closeText: '关闭' },
            displayDetails: '显示详情',
            backButtonTitle: '返回'
          }
        }
      }
    },
    outline: { level: [2, 3], label: '本页目录' },
    docFooter: { prev: false, next: false },
    returnToTopLabel: '回到顶部',
    sidebarMenuLabel: '目录',
    skipToContentLabel: '跳到正文',
    // 404 页文案（VitePress 默认英文）
    notFound: {
      title: '页面不存在',
      quote: '这个地址可能已经移动或从未存在过。',
      linkLabel: '返回首页',
      linkText: '回到首页',
      code: '404'
    }
  }
})
