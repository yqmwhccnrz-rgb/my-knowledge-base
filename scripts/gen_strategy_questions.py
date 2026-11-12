# -*- coding: utf-8 -*-
"""公司战略笔记（CPA）配套题库：校验 + 安全答案均衡 + 写回。

背景：154 道公司战略题已按 questions.json 的既有格式（indent=1）追加到
docs/public/data/questions.json，note = "Strategy"，id 为 strq001~strq154。

均衡的安全约束：部分题目的解析中明确引用了选项字母
（如「D 属于新兴产业的发展障碍」「C 是分权型结构的优点」），
一旦交换选项位置解析就会错位。因此只对「解析与题干都不含独立 A/B/C/D 字样」
的单选题做均衡，其余保持原样；用固定种子保证幂等，只交换正确项与目标位两项。

运行：python3 scripts/gen_strategy_questions.py
  - 校验失败：打印原因、非零码退出，不写回
  - 校验通过：均衡后以 indent=1 + 尾部换行写回，并打印统计
"""
import json
import os
import random
import re
import sys
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.normpath(os.path.join(HERE, "..", "docs", "public", "data", "questions.json"))

NOTE = "Strategy"
# 独立出现的选项字母（前后都不是英文字母），用于识别「解析引用了字母」的题目
LETTER_REF = re.compile(r"(?<![A-Za-z])[ABCD](?![A-Za-z])")


def validate(bank, strategy):
    errs = []
    ids = [x.get("id", "?") for x in bank]
    dup = [k for k, v in Counter(ids).items() if v > 1]
    if dup:
        errs.append("题库 id 重复: %s" % dup[:5])

    seen_q = {}
    for q in strategy:
        qid = q.get("id", "?")
        if not q.get("question") or not q.get("explanation"):
            errs.append("%s 缺题干/解析" % qid)
        if q.get("note") != NOTE or not q.get("topic"):
            errs.append("%s note/topic 异常" % qid)
        t = q.get("type")
        o = q.get("options")
        a = q.get("answer")
        if t in ("choice", "judge", "multi"):
            if not isinstance(o, list) or len(o) < 2:
                errs.append("%s 选项数异常" % qid)
            elif len(o) != len(set(o)):
                errs.append("%s 选项重复" % qid)
            if t in ("choice", "judge"):
                if not isinstance(a, int) or not (0 <= a < len(o)):
                    errs.append("%s 单选/判断答案越界" % qid)
            else:
                if not isinstance(a, list) or len(a) < 2:
                    errs.append("%s 多选答案应至少 2 项" % qid)
                elif any(not isinstance(k, int) or not (0 <= k < len(o)) for k in a):
                    errs.append("%s 多选答案越界" % qid)
        elif t == "essay":
            if not isinstance(a, str) or not a.strip():
                errs.append("%s 简答题参考答案为空" % qid)
        elif t == "fill":
            if not isinstance(a, list) or not a:
                errs.append("%s 填空题答案应为非空列表" % qid)
        else:
            errs.append("%s 未知题型 %r" % (qid, t))
        seen_q.setdefault(q.get("question", "").strip(), []).append(qid)

    for text, group in seen_q.items():
        if len(group) > 1:
            errs.append("题干重复: %s" % group)
    return errs


def balance(strategy):
    """确定性均衡：只处理解析/题干不引用选项字母的单选题。"""
    singles = [
        q for q in strategy
        if q.get("type") == "choice"
        and not LETTER_REF.search(q.get("explanation", ""))
        and not LETTER_REF.search(q.get("question", ""))
    ]
    rng = random.Random(20271111)  # 固定种子，重复运行结果一致
    rng.shuffle(singles)
    moved = 0
    for idx, q in enumerate(singles):
        target = idx % 4
        cur = q["answer"]
        if cur == target:
            continue
        opts = q["options"]
        opts[cur], opts[target] = opts[target], opts[cur]
        q["answer"] = target
        moved += 1
    return len(singles), moved


def main():
    with open(OUT, encoding="utf-8") as f:
        bank = json.load(f)
    strategy = [q for q in bank if q.get("note") == NOTE]

    errs = validate(bank, strategy)
    if errs:
        print("校验失败:")
        for e in errs:
            print("  -", e)
        sys.exit(1)

    n, moved = balance(strategy)
    with open(OUT, "w", encoding="utf-8") as f:
        json.dump(bank, f, ensure_ascii=False, indent=1)
        f.write("\n")

    print("校验通过 ✓")
    print("公司战略题 %d 道，题型分布: %s" % (
        len(strategy), dict(Counter(x["type"] for x in strategy))))
    print("可均衡单选题 %d 道，本次调整 %d 道" % (n, moved))
    print("单选题答案分布: %s" % dict(sorted(Counter(
        x["answer"] for x in strategy if x["type"] == "choice").items())))
    print("题库合计 %d 道，科目分布: %s" % (
        len(bank), dict(Counter(x["note"] for x in bank))))
    print("知识点数: %d" % len({x["topic"] for x in strategy}))
    print("章节覆盖: %s" % sorted({x["topic"].split(" ")[0] for x in strategy}))
    print("已写回: %s" % OUT)


if __name__ == "__main__":
    main()
