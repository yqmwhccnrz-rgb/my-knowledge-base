# -*- coding: utf-8 -*-
"""公司战略笔记与习题：一键完成「校验 → 双仓库同步 → 构建 → 提交」。

用途：WorkBuddy 的命令执行服务（沙箱）不可用时，在你自己的终端跑这一条命令，
即可把本次新增的笔记、7 张自绘图、154 道习题与两处配置改动同步到部署仓库，
并完成构建验证与本地提交。

运行：
    python3 /Users/longtianzhi/WorkBuddy/Claw/knowledge-site/scripts/finish_strategy.py

之后到「知识网站」目录执行 git push origin main 即可上线。
"""
import os
import shutil
import subprocess
import sys

ROOT = "/Users/longtianzhi/WorkBuddy/Claw"
DRAFT = os.path.join(ROOT, "knowledge-site")   # 草稿（无远端）
DEPLOY = os.path.join(ROOT, "知识网站")          # 部署源（带 origin）

FILES = [
    "docs/notes/strategy.md",
    "docs/public/data/questions.json",
    "docs/.vitepress/theme/Quiz.vue",
    "docs/.vitepress/config.mjs",
    "scripts/gen_strategy_questions.py",
]
SVG_SRC = os.path.join(DRAFT, "docs/public/strategy")
SVG_DST = os.path.join(DEPLOY, "docs/public/strategy")

COMMIT_MSG = "新增 CPA 公司战略与风险管理笔记（8 章 + 7 张自绘图 + 资料勘误）与 154 道配套习题"


def run(cmd, cwd, optional=False):
    print("\n>>> %s   (在 %s)" % (cmd, os.path.basename(cwd)))
    p = subprocess.run(cmd, shell=True, cwd=cwd, text=True,
                       capture_output=True)
    if p.stdout:
        print(p.stdout.strip()[-3000:])
    if p.stderr:
        print("[stderr]", p.stderr.strip()[-1500:])
    if p.returncode != 0 and not optional:
        print("!! 命令失败（退出码 %d），已停止" % p.returncode)
        sys.exit(1)
    return p


def main():
    for d in (DRAFT, DEPLOY):
        if not os.path.isdir(d):
            print("找不到目录：", d)
            sys.exit(1)

    # 1) 校验题库 JSON 并做安全答案均衡（会原地写回草稿的 questions.json）
    print("=" * 60)
    print("步骤 1/5：校验题库并均衡答案分布")
    run("python3 scripts/gen_strategy_questions.py", DRAFT)

    # 2) 把改动同步到部署源
    print("=" * 60)
    print("步骤 2/5：同步文件到部署源「知识网站」")
    for rel in FILES:
        src = os.path.join(DRAFT, rel)
        dst = os.path.join(DEPLOY, rel)
        os.makedirs(os.path.dirname(dst), exist_ok=True)
        shutil.copy2(src, dst)
        print("  复制", rel)
    if os.path.isdir(SVG_SRC):
        os.makedirs(SVG_DST, exist_ok=True)
        for name in sorted(os.listdir(SVG_SRC)):
            if name.endswith(".svg"):
                shutil.copy2(os.path.join(SVG_SRC, name),
                             os.path.join(SVG_DST, name))
                print("  复制 docs/public/strategy/" + name)

    # 3) 构建验证（两个仓库都跑，确保部署源也能编译）
    print("=" * 60)
    print("步骤 3/5：构建验证")
    run("npm run build", DRAFT)
    run("npm run build", DEPLOY)

    # 4) 提交（两处各自提交，保持历史一致）
    print("=" * 60)
    print("步骤 4/5：提交到两个仓库")
    rels = " ".join(FILES + ["docs/public/strategy"])
    for repo in (DRAFT, DEPLOY):
        run("git add %s" % rels, repo)
        # 若没有差异则跳过 commit，避免报错
        status = subprocess.run("git status --porcelain", shell=True, cwd=repo,
                                text=True, capture_output=True)
        if status.stdout.strip():
            run('git commit -m "%s"' % COMMIT_MSG, repo)
        else:
            print("  %s 无改动，跳过提交" % os.path.basename(repo))
        run("git log --oneline -1", repo, optional=True)

    # 5) 结果提示
    print("=" * 60)
    print("全部完成 ✓")
    print("请到「知识网站」目录执行：  git push origin main")
    print("Cloudflare Pages 会自动重新构建部署，约 1-3 分钟后硬刷新即可看到新笔记。")


if __name__ == "__main__":
    main()
