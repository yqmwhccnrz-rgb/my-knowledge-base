import fs from 'node:fs'
import path from 'node:path'
import { fileURLToPath } from 'node:url'

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..')
const src = path.join(root, 'docs', 'notes')
const dst = path.join(root, 'docs', 'public', 'originals')
const filesDir = path.join(root, 'docs', 'public', 'files')
const imagesDir = path.join(root, 'docs', 'public', 'images')
const libraryFile = 'library.md'

fs.mkdirSync(dst, { recursive: true })

const notes = fs.readdirSync(src)
  .filter((f) => f.endsWith('.md') && f !== libraryFile)
for (const f of notes) {
  fs.copyFileSync(path.join(src, f), path.join(dst, f))
}

// 笔记被删除时，同步清掉它留下的原文副本
for (const f of fs.readdirSync(dst)) {
  if (f.endsWith('.md') && !notes.includes(f)) {
    fs.unlinkSync(path.join(dst, f))
  }
}

const safeLabel = (name) => name.replace(/[\[\]]/g, '')
const urlOf = (base, name) => `${base}/${encodeURIComponent(name)}`

const pdfs = fs.existsSync(filesDir)
  ? fs.readdirSync(filesDir).filter((f) => /\.pdf$/i.test(f)).sort()
  : []
const images = fs.existsSync(imagesDir)
  ? fs.readdirSync(imagesDir).filter((f) => /\.(png|jpe?g|gif|svg|webp)$/i.test(f)).sort()
  : []

const lines = [
  '# 原件下载',
  '',
  '这一页由构建脚本自动生成：PDF 里的知识点已重排成左侧各章笔记，并做了补充与订正。这里只保留原文件供下载，不做在线预览。',
  ''
]

if (pdfs.length) {
  lines.push('## PDF 原件', '')
  for (const f of pdfs) {
    lines.push(`- [${safeLabel(f)}](${urlOf('/files', f)}) — 点击在线打开，或右键另存为下载`)
  }
  lines.push('')
}

if (images.length) {
  lines.push('## 图片', '')
  for (const f of images) {
    lines.push(`**${safeLabel(f)}**`, '', `![${safeLabel(f)}](${urlOf('/images', f)})`, '')
  }
}

if (!pdfs.length && !images.length) {
  lines.push('目前还没有 PDF 或图片。把文件拖进桌面对应文件夹并推送后，这里会自动出现。', '')
}
fs.writeFileSync(path.join(src, libraryFile), lines.join('\n'), 'utf8')

console.log(`[sync] 已保留 ${notes.length} 份 Markdown 原文；资料库页收录 ${pdfs.length} 个 PDF / ${images.length} 张图片`)
