import fs from 'node:fs'
import path from 'node:path'
import { fileURLToPath } from 'node:url'

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..')
const notesDir = path.join(root, 'docs', 'notes')
const filesDir = path.join(root, 'docs', 'public', 'files')
const imagesDir = path.join(root, 'docs', 'public', 'images')

// 「原件下载」页已移除：清掉历史自动生成的文件，避免它重新出现在导航里
const legacy = path.join(notesDir, 'library.md')
if (fs.existsSync(legacy)) fs.unlinkSync(legacy)

const pdfs = fs.existsSync(filesDir)
  ? fs.readdirSync(filesDir).filter((f) => /\.pdf$/i.test(f)).sort()
  : []
const images = fs.existsSync(imagesDir)
  ? fs.readdirSync(imagesDir).filter((f) => /\.(png|jpe?g|gif|svg|webp)$/i.test(f)).sort()
  : []

console.log(`[sync] 资源检查：${pdfs.length} 份 PDF / ${images.length} 张图片（放在 docs/public 下，可在笔记中引用）`)
