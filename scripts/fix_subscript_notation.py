#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""批1（KB-101）：把正文里的数学记号 X_Y 从纯文本转为数学模式 $X_Y$。

只处理「正文非数学段」；已处于 $...$ / $$...$$ 内的内容绝不改动。
技术标识符（pivot_table / AS_PATH / io_uring 等）不在白名单，保持原样。
替换仅包裹 token 本身，token 字符零改动；多字符下标补 {} 以正确渲染。
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent / "docs" / "notes"

MATH_RE = re.compile(r"\$\$[\s\S]*?\$\$|(?<!\$)\$(?!\$)[^$\n]+\$(?!\$)")
CODE_RE = re.compile(r"```[\s\S]*?```|`[^`\n]*`")

# 每文件白名单：按 token 长度降序应用；目标串为渲染用包裹（多字符下标加 {}）
PLAN = {
    "macro.md": [
        ("k_TR", "$k_{TR}$"), ("k_I", "$k_I$"), ("k_G", "$k_G$"),
        ("k_T", "$k_T$"), ("k_F", "$k_F$"),
        ("Y_f", "$Y_f$"), ("G_A", "$G_A$"), ("G_W", "$G_W$"),
        ("G_N", "$G_N$"), ("v_r", "$v_r$"),
    ],
    "securities.md": [
        ("P_i1", "$P_{i1}$"), ("P_i0", "$P_{i0}$"), ("W_i", "$W_i$"),
        ("S_T", "$S_T$"), ("D_i", "$D_i$"),
        ("r_f", "$r_f$"), ("r_P", "$r_P$"),
    ],
    "interest.md": [
        ("PV_C", "$PV_C$"), ("PV_D", "$PV_D$"), ("PV_B", "$PV_B$"),
        ("D_L", "$D_L$"),
    ],
    "finmgr.md": [("R_f", "$R_f$"), ("r_c", "$r_c$"), ("K_c", "$K_c$")],
    "econometrics.md": [("d_L", "$d_L$"), ("d_U", "$d_U$")],
    "network.md": [("d_min", "$d_{min}$"), ("CW_max", "$CW_{max}$"), ("T_D", "$T_D$")],
    "coa.md": [("C_n", "$C_n$")],
    "database.md": [("F_min", "$F_{min}$")],
    "ml.md": [("N_w", "$N_w$")],
}

TOK = "[A-Za-z0-9]"


def protect(text):
    """把数学段与代码段替换为占位符，返回 (保护后文本, 恢复函数)"""
    spans = []

    def stash(m):
        spans.append(m.group(0))
        return f"\x00{len(spans)-1}\x00"

    text = CODE_RE.sub(stash, text)
    text = MATH_RE.sub(stash, text)
    return text, spans


def restore(text, spans):
    # 数学段内可能嵌有先暂存的行内代码占位符（如 $\text{`1 KB`}$），
    # re.sub 不会重扫替换结果，需循环展开直到无占位符
    for _ in range(10):
        if not re.search(r"\x00\d+\x00", text):
            break
        text = re.sub(r"\x00(\d+)\x00", lambda m: spans[int(m.group(1))], text)
    return text


def main():
    dry = "--dry" in sys.argv
    total = 0
    for fname, tokens in PLAN.items():
        path = ROOT / fname
        raw = path.read_text(encoding="utf-8")
        protected, spans = protect(raw)
        counts = []
        for tok, repl in sorted(tokens, key=lambda x: -len(x[0])):
            pat = re.compile(rf"(?<!{TOK}){re.escape(tok)}(?!{TOK})")
            protected, n = pat.subn(repl, protected)
            counts.append(f"{tok}={n}")
        out = restore(protected, spans)
        n_file = sum(int(c.split("=")[1]) for c in counts)
        total += n_file
        print(f"{fname}: {n_file} ({', '.join(counts)})")
        if not dry and n_file:
            path.write_text(out, encoding="utf-8")
    print("TOTAL", total)


if __name__ == "__main__":
    main()
