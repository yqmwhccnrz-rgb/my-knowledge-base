#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
用 Python 生成静态公式图，替换笔记里的 LaTeX 渲染。

流程：
  1. 原始（含 $...$ / $$...$$）笔记保存在 scripts/notes_source/，作为可维护源；
     首次运行时自动从 docs/notes/ 备份。
  2. 抽取全部公式，用内容哈希去重。
  3. 调用本机 Chromium（Playwright）+ KaTeX 把每条公式分批渲染成
     2 倍分辨率、透明背景的 PNG，写入 docs/public/formulas/。
  4. 把 docs/notes/*.md 里的公式替换成 <img class="fml" ...>，
     块级公式包在 <p class="fml-block"> 中居中；alt 保留原 LaTeX 便于检索。
  5. 渲染失败的公式保留原 LaTeX（由 KaTeX 兜底），并打印清单。

用法：
  python3 scripts/render_formulas.py --only interest.md   # 单文件试点
  python3 scripts/render_formulas.py                      # 全站
  python3 scripts/render_formulas.py --restore            # 从源恢复 docs/notes
"""
import argparse
import hashlib
import html
import json
import re
import shutil
import struct
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "scripts" / "notes_source"
DST = ROOT / "docs" / "notes"
IMG = ROOT / "docs" / "public" / "formulas"
LIST_JSON = Path("/tmp/fml_list.json")
SIZE_JSON = Path("/tmp/fml_sizes.json")
NODE_HELPER = Path("/tmp/fml_node_helper.js")

PW_CORE = Path.home() / "lemo-opuscar" / "node_modules" / "playwright-core"
CHROME = Path.home() / "Library/Caches/ms-playwright/chromium_headless_shell-1243/chrome-headless-shell-mac-arm64/chrome-headless-shell"

MATH_RE = re.compile(r"\$\$[\s\S]*?\$\$|(?<!\$)\$(?!\$)[^$\n]+\$(?!\$)")
CODE_RE = re.compile(r"```[\s\S]*?```|`[^`\n]*`")

NODE_CODE = r"""
const fs = require('fs');
const ROOT = process.argv[2], PW = process.argv[3], CHROME = process.argv[4], OUT = process.argv[5];
const katex = require(ROOT + '/node_modules/katex');
const { chromium } = require(PW);
const list = JSON.parse(fs.readFileSync('/tmp/fml_list.json', 'utf8'));
const css = fs.readFileSync(ROOT + '/node_modules/katex/dist/katex.min.css', 'utf8');
// batch 页放进 katex/dist，CSS 里的 fonts/ 相对路径才能加载正确字形
const BATCHFILE = ROOT + '/node_modules/katex/dist/.fml_batch.html';
const HEAD = '<!doctype html><html><head><meta charset="utf-8"><style>' + css
  + '\nhtml,body{margin:0;padding:0;background:transparent;color:#213547}'
  + '\n.f{display:inline-block;padding:4px 3px;white-space:nowrap;font-size:17px;line-height:1.45}'
  + '\n.katex{font-size:1.05em}\n.katex-display{margin:0}\n</style></head><body>';
const BATCH = 180;
(async () => {
  const b = await chromium.launch({ executablePath: CHROME, headless: true, args: ['--no-sandbox'] });
  const p = await b.newPage({ viewport: { width: 4200, height: 900 }, deviceScaleFactor: 2 });
  const sizes = {}, errs = [];
  let done = 0;
  for (let s = 0; s < list.length; s += BATCH) {
    const chunk = list.slice(s, s + BATCH);
    let body = '';
    for (const it of chunk) {
      let h;
      try { h = katex.renderToString(it.tex, { throwOnError: false, displayMode: false }); }
      catch (e) { h = '<span></span>'; }
      body += '<div class="f" id="f_' + it.hash + '">' + h + '</div>\n';
    }
    fs.writeFileSync(BATCHFILE, HEAD + body + '</body></html>');
    await p.goto('file://' + BATCHFILE, { waitUntil: 'load' });
    for (const it of chunk) {
      const el = p.locator('#f_' + it.hash);
      try {
        const box = await el.boundingBox();
        if (!box || box.width < 1 || box.height < 1) { errs.push(it.hash + ' nobox'); continue; }
        await el.screenshot({ path: OUT + '/' + it.hash + '.png', omitBackground: true, timeout: 20000 });
        sizes[it.hash] = { w: Math.max(1, Math.round(box.width)), h: Math.max(1, Math.round(box.height)) };
        done++;
      } catch (e) { if (errs.length < 8) errs.push(it.hash + ': ' + e.message.slice(0, 90)); }
    }
    console.log('  batch ' + (Math.floor(s / BATCH) + 1) + ' done ' + done + ' / ' + list.length);
  }
  fs.writeFileSync('/tmp/fml_sizes.json', JSON.stringify(sizes));
  await b.close();
  console.log('rendered total ' + done + ' / ' + list.length);
  if (errs.length) console.log('errors sample: ' + errs.slice(0, 5).join(' | '));
})().catch(e => { console.error(e.message); process.exit(1); });
"""


def optimize_images():
    """把 RGBA 截图压成 LA（灰度+Alpha）：字形颜色固定为深灰、抗锯齿留在 alpha，
    视觉等价但体积约减半。已是 LA 的跳过，保证幂等。"""
    try:
        from PIL import Image
    except ImportError:
        print("（未安装 Pillow，跳过图片压缩）")
        return
    before = after = n = 0
    for f in IMG.glob("*.png"):
        try:
            im = Image.open(f)
            if im.mode == "LA":
                continue
            rgba = im.convert("RGBA")
            alpha = rgba.getchannel("A")
            la = Image.merge("LA", (Image.new("L", rgba.size, 49), alpha))
            b = f.stat().st_size
            la.save(f, format="PNG", optimize=True)
            a = f.stat().st_size
            before += b; after += a; n += 1
        except Exception:
            pass
    if n:
        print("图片压缩: %d 张, %.1f MB -> %.1f MB" % (n, before/1048576, after/1048576))


def protect_and_extract(text):
    """把代码块换成占位符后抽取公式，返回 (模板, 公式列表)。
    frontmatter 原样保留：里面的 $...$ 多为版本号/记号，替换会破坏 YAML。"""
    fm = ""
    if text.startswith("---\n"):
        end = text.find("\n---", 4)
        if end > 0:
            fm, text = text[: end + 4], text[end + 4 :]

    codes = {}

    def prot(m):
        key = "\x00C%d\x00" % len(codes)
        codes[key] = m.group(0)
        return key

    t = CODE_RE.sub(prot, text)
    items = []

    def repl(m):
        raw = m.group(0)
        display = raw.startswith("$$")
        tex = (raw[2:-2] if display else raw[1:-1]).strip()
        h = hashlib.md5((("B" if display else "I") + tex).encode("utf-8")).hexdigest()[:14]
        items.append({"hash": h, "tex": tex, "display": display})
        return "\x00M%d\x00" % (len(items) - 1)

    t = MATH_RE.sub(repl, t)
    for k, v in codes.items():
        t = t.replace(k, v)
    return fm + t, items


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--only", help="只处理某个 md 文件名，如 interest.md")
    ap.add_argument("--restore", action="store_true", help="从源恢复 docs/notes")
    args = ap.parse_args()

    if not SRC.exists():
        SRC.mkdir(parents=True)
        for f in DST.glob("*.md"):
            shutil.copy2(f, SRC / f.name)
        print("已备份原始笔记到", SRC)
    if args.restore:
        for f in SRC.glob("*.md"):
            shutil.copy2(f, DST / f.name)
        print("已从源恢复 docs/notes/*.md")
        return

    files = [SRC / args.only] if args.only else sorted(SRC.glob("*.md"))
    docs = {}
    all_items = {}
    for f in files:
        text = f.read_text(encoding="utf-8")
        tpl, items = protect_and_extract(text)
        docs[f.name] = (tpl, items)
        for it in items:
            all_items[it["hash"]] = it
    print("公式引用数:", sum(len(x[1]) for x in docs.values()), "| 去重后:", len(all_items))

    IMG.mkdir(parents=True, exist_ok=True)
    todo = [it for h, it in all_items.items() if not (IMG / (h + ".png")).exists()]
    print("待渲染:", len(todo), "| 已有缓存:", len(all_items) - len(todo))

    if todo:
        LIST_JSON.write_text(json.dumps(todo, ensure_ascii=False), encoding="utf-8")
        NODE_HELPER.write_text(NODE_CODE, encoding="utf-8")
        cmd = ["node", str(NODE_HELPER), str(ROOT), str(PW_CORE), str(CHROME), str(IMG)]
        r = subprocess.run(cmd, capture_output=True, text=True)
        print(r.stdout.strip()[-2500:])
        if r.returncode:
            print("NODE STDERR:", r.stderr[-1500:], file=sys.stderr)
            sys.exit(1)

    optimize_images()

    sizes = json.loads(SIZE_JSON.read_text(encoding="utf-8")) if SIZE_JSON.exists() else {}
    # 缓存命中的图片：直接读 PNG 头拿回 CSS 尺寸（图片是 2 倍分辨率）
    for h in all_items:
        if h in sizes:
            continue
        png = IMG / (h + ".png")
        if png.exists():
            try:
                with png.open("rb") as fp:
                    head = fp.read(24)
                pw, ph = struct.unpack(">II", head[16:24])
                sizes[h] = {"w": max(1, pw // 2), "h": max(1, ph // 2)}
            except Exception:
                sizes[h] = {"w": 0, "h": 0}

    failed = []
    for name, (tpl, items) in docs.items():
        out = tpl
        for i, it in enumerate(items):
            h = it["hash"]
            key = "\x00M%d\x00" % i
            if h not in sizes:
                raw = ("$$" + it["tex"] + "$$") if it["display"] else ("$" + it["tex"] + "$")
                out = out.replace(key, raw)
                failed.append((name, it["tex"][:70]))
                continue
            sz = sizes[h]
            wh = ""
            if sz["w"] and sz["h"]:
                wh = ' width="%d" height="%d"' % (sz["w"], sz["h"])
            alt = html.escape(it["tex"], quote=True)
            img = '<img class="fml" src="/formulas/%s.png" alt="%s"%s>' % (h, alt, wh)
            if it["display"]:
                out = out.replace(key, "\n\n<p class=\"fml-block\">" + img + "</p>\n\n")
            else:
                out = out.replace(key, img)
        (DST / name).write_text(out, encoding="utf-8")

    print("已写出", len(docs), "篇笔记 | 失败(保留 LaTeX 兜底):", len(failed))
    for x in failed[:15]:
        print("  ", x)


if __name__ == "__main__":
    main()
