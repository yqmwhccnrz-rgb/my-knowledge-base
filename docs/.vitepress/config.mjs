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
  return fs.readdirSync(notesDir)
    .filter((f) => f.endsWith('.md'))
    .sort()
    .map((f) => ({
      text: readTitle(f),
      link: `/notes/${f.replace(/\.md$/, '')}.html`
    }))
}

const notes = noteLinks()

export default defineConfig({
  title: '我的知识库',
  description: '笔记、原文与习题测试',
  lang: 'zh-CN',
  lastUpdated: true,
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
    docFooter: { prev: '上一篇', next: '下一篇' },
    returnToTopLabel: '回到顶部',
    sidebarMenuLabel: '目录',
    darkModeSwitchLabel: '外观',
    lightModeSwitchTitle: '切换到浅色',
    darkModeSwitchTitle: '切换到深色',
    skipToContentLabel: '跳到正文'
  }
})
