#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
把笔记里的「例题」段落整块包成 <div class="kb-example">，
不改变任何文字、顺序与内部结构，只在外层加一个包裹容器。

规则：
  - 例题起点：以 **例 <数字> 开头的行
  - 例题终点：下一个 Markdown 标题(^#{1,6} ) 或 下一个例题起点（取先到者）
  - 小优化：若例题与终点之间出现「独立粗体小标题 + 紧随表格」，则在该小标题前截断
    （如利息理论例2 后面的「计息天数规则」表，属于独立知识点，不应算进例题）
  - HTML 块前后各留一个空行，保证 markdown-it 正确解析块内内容
  - 只处理源笔记 scripts/notes_source/*.md；重新运行 render_formulas.py 会同步到 docs/notes
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "scripts" / "notes_source"

START_RE = re.compile(r'^\*\*例\s*\d+')
HEADING_RE = re.compile(r'^#{1,6}\s')
# 解答/收尾引导词：这些粗体段落属于例题内部，不能在其前截断
SOLUTION_WORDS = ('解', '解法', '故', '要点', '答案', '说明', '提示', '小结', '结论', '注意')
# 独立小标题：独占一行的 **xxx**，且下一非空行是表格
BOLD_TITLE_RE = re.compile(r'^\*\*[^*]+\*\*\s*[:：]?\s*$|^\*\*[^*]+\*\*（')


def is_standalone_table_title(lines, i, end):
    """判断 lines[i] 是否为「独立粗体小标题 + 紧随表格」的开头。"""
    line = lines[i]
    if not line.startswith('**'):
        return False
    # 解答引导词开头不算独立标题
    stripped = line[2:]
    if any(stripped.startswith(w) for w in SOLUTION_WORDS):
        return False
    if not BOLD_TITLE_RE.match(line):
        return False
    # 向后找第一个非空行，必须是表格
    j = i + 1
    while j < end and not lines[j].strip():
        j += 1
    return j < end and lines[j].lstrip().startswith('|')


def wrap_file(text):
    lines = text.split('\n')
    starts = [i for i, l in enumerate(lines) if START_RE.match(l)]
    if not starts:
        return text, 0

    # 先算出每个例题的 (start, end) 半开区间
    blocks = []
    for k, s in enumerate(starts):
        nxt = starts[k + 1] if k + 1 < len(starts) else len(lines)
        heading = next((i for i in range(s + 1, nxt) if HEADING_RE.match(lines[i])), nxt)
        end = min(nxt, heading)
        # 小优化：在独立小标题+表格前截断
        for i in range(s + 1, end):
            if is_standalone_table_title(lines, i, end):
                end = i
                break
        blocks.append((s, end))

    # 从后往前插入，避免行号偏移
    for s, end in reversed(blocks):
        # 去掉块首尾的空行，让 div 紧贴内容
        a, b = s, end
        while a < b and not lines[a].strip():
            a += 1
        while b > a and not lines[b - 1].strip():
            b -= 1
        inner = lines[a:b]
        new = ['<div class="kb-example">', ''] + inner + ['', '</div>']
        lines[s:end] = new

    return '\n'.join(lines), len(blocks)


def main():
    dry = '--dry' in sys.argv
    only = None
    if '--only' in sys.argv:
        only = sys.argv[sys.argv.index('--only') + 1]
    files = [SRC / only] if only else sorted(SRC.glob('*.md'))
    total = 0
    for f in files:
        text = f.read_text(encoding='utf-8')
        new, n = wrap_file(text)
        if n:
            total += n
            print(f'{f.name}: 包裹 {n} 个例题 {("(预演)" if dry else "")}')
            if not dry:
                f.write_text(new, encoding='utf-8')
    print(f'合计 {total} 个例题 {("(仅预演，未写回)" if dry else "(已写回源笔记)")}')


if __name__ == '__main__':
    main()
