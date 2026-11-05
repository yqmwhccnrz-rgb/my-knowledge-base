import fs from 'node:fs'
import path from 'node:path'
import { fileURLToPath } from 'node:url'

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..')
const src = path.join(root, 'docs', 'notes')
const dst = path.join(root, 'docs', 'public', 'originals')

fs.mkdirSync(dst, { recursive: true })

const files = fs.readdirSync(src).filter((f) => f.endsWith('.md'))
for (const f of files) {
  fs.copyFileSync(path.join(src, f), path.join(dst, f))
}

console.log(`[sync] 已保留 ${files.length} 份 Markdown 原文`)
