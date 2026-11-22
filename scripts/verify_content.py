#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""内容零改动校验：对比 git HEAD 与工作树的 docs/notes 指定文件。
剔除空白行与呈现层包裹行（kb-example/kb-q/kb-sol/kb-answer/solution-block 的 div 行）后，
其余行序列必须逐行逐字一致。退出码 0 = 通过。
用法：python3 scripts/verify_content.py interest.md securities.md ...
"""
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
WRAPPER_EXACT = {
    '<div class="kb-example">', '</div>', '<div class="kb-q">', '<div class="kb-sol">',
    '<div class="kb-answer">', '<div class="kb-exercise">', '<div class="solution-block">',
}
ALLOW_SUFFIX = ()  # 预留


def content_lines(text):
    out = []
    for l in text.split("\n"):
        s = l.strip()
        if not s or s in WRAPPER_EXACT:
            continue
        out.append(l)
    return out


def main():
    args = sys.argv[1:]
    base_dir = None
    if "--base" in args:
        i = args.index("--base")
        base_dir = Path(args[i + 1])
        args = args[:i] + args[i + 2:]
    targets = [a for a in args if a.endswith(".md")]
    if not targets:
        targets = [p.name for p in (ROOT / "docs" / "notes").glob("*.md")]
    failed = 0
    for f in targets:
        rel = f"docs/notes/{f}"
        if base_dir:
            src = base_dir / f
            old = src.read_text(encoding="utf-8") if src.exists() else subprocess.run(
                ["git", "-C", str(ROOT), "show", f"HEAD:{rel}"], capture_output=True, text=True).stdout
        else:
            old = subprocess.run(["git", "-C", str(ROOT), "show", f"HEAD:{rel}"],
                                 capture_output=True, text=True).stdout
        new = (ROOT / rel).read_text(encoding="utf-8")
        a, b = content_lines(old), content_lines(new)
        # 结构断言：kb-example opener 数守恒（防包裹重复/块吞并）
        cnt = lambda t, s: sum(1 for l in t.split("\n") if l.strip() == s)
        structural_ok = cnt(old, '<div class="kb-example">') == cnt(new, '<div class="kb-example">')
        if a == b and structural_ok:
            print(f"PASS {f} ({len(a)} 行)")
        else:
            failed += 1
            if not structural_ok:
                print(f"FAIL {f}: kb-example 开闭结构改变（重复包裹或块边界错误）")
            if a != b:
                print(f"FAIL {f}: 旧 {len(a)} 行 / 新 {len(b)} 行")
                for i in range(min(len(a), len(b))):
                    if a[i] != b[i]:
                        print(f"  首个差异 L{i+1}:")
                        print(f"   OLD: {a[i][:120]}")
                        print(f"   NEW: {b[i][:120]}")
                        break
                else:
                    extra = a[len(b):] or b[len(a):]
                    tag = "旧多出" if len(a) > len(b) else "新多出"
                    print(f"  {tag}: {extra[0][:120] if extra else '?'}")
    sys.exit(1 if failed else 0)


if __name__ == "__main__":
    main()
