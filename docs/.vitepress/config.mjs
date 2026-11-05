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
  // 导读排最前，自动生成的「原件下载」页排最后，其余按文件名顺序
  const rank = (f) => (f === 'welcome.md' ? 0 : f === 'library.md' ? 2 : 1)
  return fs.readdirSync(notesDir)
    .filter((f) => f.endsWith('.md'))
    .sort((a, b) => rank(a) - rank(b) || a.localeCompare(b))
    .map((f) => ({
      text: readTitle(f),
      link: `/notes/${f.replace(/\.md$/, '')}.html`
    }))
}

const notes = noteLinks()

export default defineConfig({
  title: '我的知识库',
  description: '笔记与习题测试',
  lang: 'zh-CN',
  lastUpdated: true,
  // 固定灰白浅色主调，不跟随访客系统的深色模式
  appearance: false,
  ignoreDeadLinks: true,
  srcExclude: ['public/**'],
  themeConfig: {
    nav: [
      { text: '首页', link: '/' },
      { text: '笔记', link: notes[0]?.link ?? '/' },
      { text: '习题测试', link: '/quiz.html' }
    ],
    sidebar: [
      { text: '笔记', items: notes },
      { text: '练习', items: [{ text: '习题测试', link: '/quiz' }] }
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
