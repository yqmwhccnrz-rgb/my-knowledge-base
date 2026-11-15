#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
把笔记源码里「没写成 $...$ 的纯文本等式」规范化成 LaTeX，
之后由 render_formulas.py 统一渲染成静态图片。

只处理数学等式，跳过：
  - frontmatter / 代码块 / 已有 $...$ 与 $$...$$
  - 代码赋值（seed=42、alpha=1.0、数组下标 a[4]=13、含 == <= >= 等）
  - 括号不配对的残缺片段、纯参数名、中文

用法：
  python3 scripts/wrap_bare_equations.py --dry   # 只打印将要转换的清单
  python3 scripts/wrap_bare_equations.py         # 写回 scripts/notes_source/
"""
import argparse
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "scripts" / "notes_source"

MATH = re.compile(r"\$\$[\s\S]*?\$\$|(?<!\$)\$(?!\$)[^$\n]+\$(?!\$)")
CODE = re.compile(r"```[\s\S]*?```|`[^`\n]*`")
PROTECT = re.compile(r"```[\s\S]*?```|`[^`\n]*`|\$\$[\s\S]*?\$\$|(?<!\$)\$(?!\$)[^$\n]+\$(?!\$)")

# 等号两侧只允许数学字符，遇到中文/中文标点自动断开。
# 刻意不含 `*`（markdown 粗体标记会污染片段），乘号用 ×。
BARE = re.compile(
    r"(?<![\w$\\])"
    r"([A-Za-z][A-Za-z0-9_\^\{\}\(\)\[\]\.\s\+\-/÷×²³ⁿ≈≤≥]{1,45}"
    r"=\s*[A-Za-z0-9_\^\{\}\(\)\[\]\.\s\+\-/÷×²³ⁿ≈≤≥]{1,80})"
)

BLOCK = {
    "seed", "alpha", "type", "ttl", "id", "port", "bias", "dpi", "url", "key",
    "mode", "size", "shape", "dtype", "axis", "index", "columns", "step", "eps",
    "lr", "batch", "epoch", "ratio", "tol", "max_iter", "random_state",
}
# 片段里出现这些英文词，说明是代码/术语说明而非数学公式
WORD_BLOCK = re.compile(
    r"\b(?:class|price|pooled|over|HTTP|HTTPS|TLS|Max|Need|Allocation|ACF|"
    r"select|from|where|null|true|false|name|value|data|count|self|this|"
    r"error|lambda|array|string|result|input|output|default|return)\b", re.I)


def normalize(s):
    s = s.replace("×", r"\times ").replace("÷", r"\div ")
    s = s.replace("²", "^{2}").replace("³", "^{3}").replace("ⁿ", "^{n}")
    s = s.replace("≈", r"\approx ").replace("≤", r"\leq ").replace("≥", r"\geq ")
    # 数字/数字（含小数）与 标识符/标识符 → 垂直分式；边界保证不切进小数
    s = re.sub(r"(?<![\w.\\])(\d+(?:\.\d+)?)\s*/\s*(\d+(?:\.\d+)?)(?![\w.])",
               lambda m: r"\frac{%s}{%s}" % (m.group(1), m.group(2)), s)
    s = re.sub(r"(?<![\w.\\])([A-Za-z][A-Za-z0-9]*)\s*/\s*([A-Za-z][A-Za-z0-9]*)(?![\w.])",
               lambda m: r"\frac{%s}{%s}" % (m.group(1), m.group(2)), s)
    return re.sub(r"\s+", " ", s).strip()


def valid(s):
    if not 4 <= len(s) <= 130 or "=" not in s:
        return False
    if re.search(r"[\u4e00-\u9fff]", s) or re.search(r"==|<=|>=|!=|<>", s):
        return False
    if s.count("(") != s.count(")") or s.count("[") != s.count("]"):
        return False
    if s.count("{") != s.count("}"):
        return False
    lhs, rhs = s.split("=", 1)
    lhs, rhs = lhs.strip(), rhs.strip()
    if not lhs or not rhs:
        return False
    if lhs.lower() in BLOCK or "[" in lhs:
        return False
    if re.search(r"[\+\-/÷×]\s*$", lhs):        # 变量名以运算符收尾，非公式
        return False
    if "**" in s:                                   # 粗体标记混进来了
        return False
    if re.search(r"[\+\-/÷×≈≤≥]\s*$", rhs):        # 右侧以运算符收尾（被截断）
        return False
    # 右侧是「数字 + 单位」或纯数字：属于参数赋值/标量说明，不是公式
    if re.fullmatch(r"[\d\.\s]+", rhs):
        # 左侧本身是表达式（含运算符）时才算公式，如 ian + vⁿ = 1
        return bool(re.search(r"[\+\-/÷×^²³ⁿ]", lhs))
    if re.fullmatch(r"\d+(?:\.\d+)?\s*[A-Za-z][A-Za-z0-9/]*", rhs):
        return False
    if not re.search(r"\d|[+\-/÷×()]", s):
        # 纯字母等式也是公式，如 MV = PT、MRS = MRT、M = kPy；
        # 但排除英文单词/代码（class = price、HTTPS = HTTP over TLS 等）
        if WORD_BLOCK.search(s):
            return False
        return bool(re.fullmatch(
            r"[A-Za-z][A-Za-z0-9_\s\+\-/]*=\s*[A-Za-z][A-Za-z0-9_\s\+\-/]*", s))
    if WORD_BLOCK.search(s):
        return False
    return True


def wrap(text):
    fm = ""
    if text.startswith("---\n"):
        end = text.find("\n---", 4)
        if end > 0:
            fm, text = text[: end + 4], text[end + 4 :]

    saved = {}

    def prot(m):
        key = "\x00P%d\x00" % len(saved)
        saved[key] = m.group(0)
        return key

    t = PROTECT.sub(prot, text)
    hits = []

    def repl(m):
        s = m.group(1).strip().rstrip("*").strip()
        if not valid(s):
            return m.group(0)
        tex = normalize(s)
        hits.append((s, tex))
        return "$" + tex + "$"

    t = BARE.sub(repl, t)
    for k, v in saved.items():
        t = t.replace(k, v)
    return fm + t, hits


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry", action="store_true")
    args = ap.parse_args()
    total = 0
    for f in sorted(SRC.glob("*.md")):
        s = f.read_text(encoding="utf-8")
        out, hits = wrap(s)
        if not hits:
            continue
        total += len(hits)
        print("=== %s: %d 处 ===" % (f.name, len(hits)))
        for a, b in hits[:8]:
            print("   %-46s -> $%s$" % (a[:46], b[:70]))
        if len(hits) > 8:
            print("   ... 另 %d 处" % (len(hits) - 8))
        if not args.dry and out != s:
            f.write_text(out, encoding="utf-8")
    print("\n合计:", total, "处", "(仅预览)" if args.dry else "(已写回源笔记)")


if __name__ == "__main__":
    main()
