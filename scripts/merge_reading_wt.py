#!/usr/bin/env python3
"""把 /tmp/writing_items.json 与 /tmp/translation_items.json 合并进 docs/public/data/reading.json。

- 保留原有 phrase / reading 两个键不变；
- 新增 writing / translation 两个键；
- 校验字段完整性、id 唯一、级别分布。
"""
import json
import sys

BASE = '/Users/longtianzhi/WorkBuddy/Claw/knowledge-site/docs/public/data/reading.json'
W = '/tmp/writing_items.json'
T = '/tmp/translation_items.json'

REQ_W = {'id', 'level', 'topic', 'title', 'prompt', 'promptZh', 'outline', 'model', 'expressions'}
REQ_T = {'id', 'level', 'topic', 'title', 'source', 'hints', 'ref', 'points'}


def load(p):
    with open(p, encoding='utf-8') as f:
        return json.load(f)


def check(items, req, tag):
    ids = set()
    n4 = n6 = 0
    for i, it in enumerate(items):
        miss = req - set(it.keys())
        assert not miss, f'{tag}[{i}] 缺字段 {miss}'
        assert it['id'] not in ids, f'{tag}[{i}] id 重复 {it["id"]}'
        ids.add(it['id'])
        assert it['level'] in ('CET-4', 'CET-6'), f'{tag}[{i}] level 非法'
        for k in req:
            v = it[k]
            if isinstance(v, str):
                assert v.strip(), f'{tag}[{i}] 字段 {k} 为空'
            elif isinstance(v, list):
                assert len(v) > 0, f'{tag}[{i}] 字段 {k} 为空列表'
        if it['level'] == 'CET-4':
            n4 += 1
        else:
            n6 += 1
    return n4, n6


def main():
    data = load(BASE)
    w = load(W)
    t = load(T)
    w4, w6 = check(w, REQ_W, 'writing')
    t4, t6 = check(t, REQ_T, 'translation')
    data['writing'] = w
    data['translation'] = t
    with open(BASE, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=1)
    print(f'OK phrase={len(data["phrase"])} reading={len(data["reading"])} '
          f'writing={len(w)}(4:{w4}/6:{w6}) translation={len(t)}(4:{t4}/6:{t6})')


if __name__ == '__main__':
    sys.exit(main())
