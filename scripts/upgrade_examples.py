#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""批2（KB-203）：旧式例题块升级为三段式卡片（题头 kb-q / 解答 kb-sol / 结论 kb-answer）。

只做呈现层包裹：块内文本逐字保留，不增删改任何字符；仅插入包裹 div 行。
规则（确定性）：
  - 已含 kb-q/kb-sol 的块跳过；
  - 无「解：」开头的段落（纯陈述块）跳过；
  - kb-q   = 首段（**例 N** 起）到「解：」段之前的全部段落；
  - kb-sol = 「解：」段到「答：/答案：」段之前的全部段落；
  - kb-answer = 「答：/答案：」段起至块尾（没有则不建，答案留在 kb-sol 内）。
用法：
  python3 scripts/upgrade_examples.py --dry            # 全部文件预览
  python3 scripts/upgrade_examples.py --apply interest # 应用单文件
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent / "docs" / "notes"
FILES = ["interest.md", "securities.md", "finance.md", "macro.md"]

OPEN = re.compile(r'^<div class="kb-example">\s*$')
SOL = re.compile(r'^(解[：:]|\*\*解\*\*[：:])')
ANS = re.compile(r'^(答[案]?[：:]|\*\*答案?\*\*[：:]|\*\*答案\*\*)')


def split_blocks(text):
    """按嵌套深度切出 kb-example 块（计数任意 <div 开 / </div> 闭，兼容内嵌 solution-block），
    返回 [(start_line, end_line_inclusive)]"""
    blocks, depth, start = [], 0, None
    for i, line in enumerate(text.split("\n")):
        if OPEN.match(line):
            if depth == 0:
                start = i
            depth += 1
        elif "<div" in line and depth > 0:
            depth += 1
        elif line.strip() == "</div>" and depth > 0:
            depth -= 1
            if depth == 0:
                blocks.append((start, i))
    return blocks


def is_old(block_lines):
    return not any("kb-q" in l or "kb-sol" in l or "kb-answer" in l for l in block_lines)


def paragraphs(lines):
    """块内正文行 → 段落列表（每段为行列表），剔除首尾空行"""
    core = lines[:]
    while core and not core[0].strip():
        core.pop(0)
    while core and not core[-1].strip():
        core.pop()
    paras, cur = [], []
    for l in core:
        if l.strip() == "":
            if cur:
                paras.append(cur)
                cur = []
        else:
            cur.append(l)
    if cur:
        paras.append(cur)
    return paras


def upgrade(lines):
    """返回 (新行列表, 变化描述) 或 None"""
    paras = paragraphs(lines)
    if not paras:
        return None
    # 找解段与答段索引
    sol_i = next((i for i, p in enumerate(paras) if SOL.match(p[0].strip())), None)
    ans_i = next((i for i, p in enumerate(paras) if ANS.match(p[0].strip())), None)
    if sol_i is None or sol_i == 0:
        return None  # 纯陈述块 / 无解，跳过
    if ans_i is not None and ans_i < sol_i:
        ans_i = None  # 异常顺序，保守起见不建答框
    q = [p for p in paras[:sol_i]]
    sol = [p for p in paras[sol_i:ans_i]] if ans_i is not None else [p for p in paras[sol_i:]]
    ans = [p for p in paras[ans_i:]] if ans_i is not None else []

    def emit(paras_):
        out = []
        for p in paras_:
            out.extend(p)
            out.append("")
        return out

    body = ["<div class=\"kb-q\">", ""]
    body += emit(q)
    body += ["</div>", "<div class=\"kb-sol\">", ""]
    body += emit(sol)
    body += ["</div>"]
    if ans:
        body += ["<div class=\"kb-answer\">", ""]
        body += emit(ans)
        body += ["</div>"]
    body += [""]
    return body, f"q={len(q)} sol={len(sol)} ans={len(ans)}"


def process(fname, apply=False):
    path = ROOT / fname
    if not path.exists():
        return None
    text = path.read_text(encoding="utf-8")
    lines = text.split("\n")
    blocks = split_blocks(text)
    changed, skipped_old, skipped_plain = 0, 0, 0
    out = lines[:]
    for (s, e) in reversed(blocks):
        seg = lines[s:e + 1]
        if not is_old(seg):
            skipped_old += 1
            continue
        res = upgrade(seg[1:-1])  # 仅块内行：外层 opener/closer 不参与分段
        if res is None:
            skipped_plain += 1
            continue
        new_body, desc = res
        # 原 seg: <div class="kb-example">\n\n...\n\n</div> → 保持外层 div 与闭合
        new_seg = [seg[0], ""] + new_body + [seg[-1]]
        out[s:e + 1] = new_seg
        changed += 1
        print(f"  {fname} L{s+1}: {desc}")
    if apply and changed:
        path.write_text("\n".join(out), encoding="utf-8")
    return changed, skipped_old, skipped_plain


def main():
    args = sys.argv[1:]
    apply = "--apply" in args
    target = [a for a in args if a.endswith(".md")]
    if apply and target:
        reports = [process(target[0], apply=True)]
        print(f"APPLIED {target[0]}: {reports[0]}")
        return
    total = 0
    for f in FILES:
        r = process(f, apply=False)
        if r:
            print(f"{f}: 升级 {r[0]} 块 / 已是新式 {r[1]} / 纯陈述跳过 {r[2]}")
            total += r[0]
    print("TOTAL upgradeable:", total)


if __name__ == "__main__":
    main()
