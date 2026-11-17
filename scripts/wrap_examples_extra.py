#!/usr/bin/env python3
"""把源笔记中剩余的「例题 / 习题」整块包裹成带样式的 div。

与 wrap_examples.py 的分工：
- wrap_examples.py 已处理 interest.md(50) 与 securities.md 末尾 3 个连排例题；
- 本脚本处理其余散落的 **例**：/ **例（...）**： 形式，以及 welcome.md 的
  「附录 练习题」下每个 ### N. 题名 小节。

边界规则（保证不拆分板块内部内容、不误吞下一知识点）：
- 起点：**例... 行，或「### N. 题名」行（仅附录范围）；
- 终点：下一个标题 / 下一个例题 / 下一个「### N. 题名」；
- 中途遇到「新的加粗知识点小标题」或「引用块」即结束（它们属于正文讲解，
  不属于例题本身）。

用法：
  python3 scripts/wrap_examples_extra.py --dry     # 只打印将包裹的块
  python3 scripts/wrap_examples_extra.py           # 写回源笔记
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "scripts" / "notes_source"

OPEN = '<div class="kb-example">'
OPEN_EX = '<div class="kb-exercise">'
CLOSE = '</div>'

START_RE = re.compile(r'^\*\*例(?:\s*\d+|[（(]|\*\*[：:]|[：:])')
HEADING_RE = re.compile(r'^#{1,6}\s')
EX_ITEM_RE = re.compile(r'^###\s*\d+\.\s')
NEW_BOLD_RE = re.compile(r'^\*\*[^*]+\*\*')
SOLUTION_WORDS = ('解', '解法', '故', '要点', '答案', '说明', '提示', '小结',
                  '结论', '注意', '推导', '证明', '解析')


def in_div_flags(lines):
    """标记哪些行已处在 kb-example / kb-exercise 容器内部。"""
    flags = [False] * len(lines)
    inside = False
    for i, l in enumerate(lines):
        if l.strip() in (OPEN, OPEN_EX):
            inside = True
            flags[i] = True
            continue
        if inside and l.strip() == CLOSE:
            flags[i] = True
            inside = False
            continue
        if inside:
            flags[i] = True
    return flags


def find_end(lines, start, limit, item_mode=False):
    """返回 [start, end) 的 end。"""
    end = limit
    for i in range(start + 1, limit):
        l = lines[i]
        if HEADING_RE.match(l):
            end = i
            break
        if item_mode and EX_ITEM_RE.match(l):
            end = i
            break
        if not item_mode and START_RE.match(l):
            end = i
            break
        # 新知识点小标题 / 引用块：正文讲解，不并入例题
        # 习题小节里「**思路**、**代码**」属于题目本身，不能在此截断
        if not item_mode:
            if NEW_BOLD_RE.match(l):
                bold = re.match(r'^\*\*([^*]+)\*\*', l).group(1)
                if any(bold.startswith(w) for w in SOLUTION_WORDS):
                    continue
                end = i
                break
            if l.lstrip().startswith('>'):
                end = i
                break
    return end


def wrap_examples(text):
    lines = text.split('\n')
    flags = in_div_flags(lines)
    starts = [i for i, l in enumerate(lines) if not flags[i] and START_RE.match(l)]
    if not starts:
        return text, []

    blocks = []
    for k, s in enumerate(starts):
        nxt = starts[k + 1] if k + 1 < len(starts) else len(lines)
        end = find_end(lines, s, nxt, item_mode=False)
        blocks.append((s, end))

    # 去掉尾部空行，再插入 div；倒序处理避免行号漂移
    out = list(lines)
    for s, end in reversed(blocks):
        a, b = s, end
        while b > a and not out[b - 1].strip():
            b -= 1
        inner = out[a:b]
        out[a:b] = [OPEN, ''] + inner + ['', CLOSE]
    return '\n'.join(out), blocks


def wrap_exercise_items(text):
    lines = text.split('\n')
    flags = in_div_flags(lines)
    # 只在「附录 练习题」标题之后处理
    anchor = next((i for i, l in enumerate(lines) if l.startswith('## 附录 练习题')), None)
    if anchor is None:
        return text, []
    starts = [i for i in range(anchor + 1, len(lines))
              if not flags[i] and EX_ITEM_RE.match(lines[i])]
    if not starts:
        return text, []

    blocks = []
    for k, s in enumerate(starts):
        nxt = starts[k + 1] if k + 1 < len(starts) else len(lines)
        end = find_end(lines, s, nxt, item_mode=True)
        blocks.append((s, end))

    out = list(lines)
    for s, end in reversed(blocks):
        a, b = s, end
        while b > a and not out[b - 1].strip():
            b -= 1
        inner = out[a:b]
        out[a:b] = [OPEN_EX, ''] + inner + ['', CLOSE]
    return '\n'.join(out), blocks


def main():
    dry = '--dry' in sys.argv
    total_e = total_x = 0
    for f in sorted(SRC.glob('*.md')):
        text = f.read_text(encoding='utf-8')
        new, eb = wrap_examples(text)
        new, xb = wrap_exercise_items(new)
        if not eb and not xb:
            continue
        total_e += len(eb)
        total_x += len(xb)
        print(f'{f.name:20} 例题 {len(eb):3}  习题 {len(xb):3}')
        for s, end in eb:
            print(f'    例题 行 {s+1}-{end}: {text.splitlines()[s][:66]}')
        for s, end in xb:
            print(f'    习题 行 {s+1}-{end}: {text.splitlines()[s][:66]}')
        if not dry:
            f.write_text(new, encoding='utf-8')
    print(f'合计: 例题 {total_e}, 习题 {total_x}' + ('  (dry-run, 未写回)' if dry else '  (已写回源笔记)'))


if __name__ == '__main__':
    main()
