#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""修正笔记源文件中已核实的概念/计算/表述错误（精确替换 + 计数断言）。
用法： python3 scripts/fix_content_errors.py [--dry]
"""
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SRC = ROOT / "notes_source"
DRY = "--dry" in sys.argv

# (文件, old, new, 期望出现次数)
E = []

def add(f, old, new, n=1):
    E.append((f, old, new, n))

# ---------------- interest.md ----------------
# 例1：题面累积函数漏写 +0.05t，与解及既有答案 609.74 自相矛盾（答案 609.74 为既有刻意修正，保留）
add("interest.md",
    "累积函数 $a(t)= 1.2^{t}$，求 t=2 时的 500 万元在 t=3 时的价值。",
    "累积函数 $a(t)= 1.2^{t}+ 0.05t$，求 t=2 时的 500 万元在 t=3 时的价值。")
# 例9：清理未规范化的 … 占位推导，给出完整正确推导（v^n=0.5, 比值=2）
add("interest.md",
    "解：$PV_{C}= v^{2n} \\cdot a_{n}$，$PV_{D}= \\frac{v^{3n}}{i}$。由 $v^{2n}a_{n}= \\frac{v^{3n}}{i}$ 及 $a_{n}= \\frac{1- v^{n}}{i}$ 得 $v^{n}(1- v^{n})= v^{n} \\cdot \\cdots$解得 $v^{n}= 0.5$。$PV_{B} : PV_{D}= \\frac{v^{n}a_{n}}{\\frac{v^{3n}}{i}}= \\frac{(1- v^{n})v^{n}}{v^{3n} \\cdot} \\cdots=2$（教材例 2-4：比值 = $\\frac{1- v^{n}}{v^{n} \\cdot v^{n-3n}}$ 化简后代入 $v^{n}=0.5$ 得 2）。",
    "解：$PV_{C}= v^{2n} \\cdot a_{n}$，$PV_{D}= \\dfrac{v^{3n}}{i}$。由 $PV_{C}=PV_{D}$ 即 $v^{2n}\\cdot\\dfrac{1- v^{n}}{i}= \\dfrac{v^{3n}}{i}$ 得 $1- v^{n}= v^{n}$，解得 $v^{n}= 0.5$。$PV_{B}:PV_{D}= \\dfrac{v^{n}a_{n}}{\\frac{v^{3n}}{i}}= \\dfrac{(1- v^{n})v^{n}}{v^{3n}}= \\dfrac{1- v^{n}}{v^{2n}}= \\dfrac{1- v^{n}}{(v^{n})^{2}}=2$（代入 $v^{n}=0.5$ 得 $0.5/0.25=2$）。")
# 例15：分母误用名义利率 i^(12)=0.04889，应为名义贴现率 d^(12)=0.04869；终值随之修正
add("interest.md",
    "12000 \\times\\left(\\frac{0.05}{0.04889}\\right) \\times 5.5256=67\\,813.74\\,\\text{元}",
    "12000 \\times\\left(\\dfrac{0.05}{0.04869}\\right) \\times 5.5256\\approx 68\\,090\\,\\text{元}")
# 求 n 的解析式分母残缺
add("interest.md",
    "n= \\frac{\\ln[ \\cdots]}{\\ln}(1+i)",
    "n= \\dfrac{\\ln[\\cdots]}{\\ln(1+i)}")
# 例20：中间一步把 (Is)_16 误写成 24.8404（那是 s_16），应为 176.81
add("interest.md",
    "= 6624.10+ 20 \\times 24.8404=10\\,160.26\\,\\text{元}",
    "= 6624.10+ 20 \\times 176.81=10\\,160.26\\,\\text{元}")
# 例21：期初付递减终值公式分母应为 d 而非 i；括号内是 s_10 而非 s̈_10
add("interest.md",
    "$10 \\times(D\\ddot{s})_{10}= \\frac{10 \\times[10 \\times 1.06^{10}- \\ddot{s}_{10}]}{0.06}= \\frac{10 \\times(17.9085- 13.1808)}{0.06}=835.22\\,\\text{元}$。",
    "$10 \\times(D\\ddot{s})_{10}= \\dfrac{10 \\times[10 \\times 1.06^{10}- s_{10}]}{d}= \\dfrac{10 \\times(17.9085- 13.1808)}{0.0566}=835.22\\,\\text{元}$。")
# 山形年金现值：两个结论并列无连接，补等号
add("interest.md",
    "现值 = $(Ia)_{n}+ v^{n}(Da)_{(n-1)}$ $a_{n} \\cdot \\ddot{a}_{n}$（教材例 3-7 优美结论，证明题考点）。",
    "现值 = $(Ia)_{n}+ v^{n}(Da)_{(n-1)}= a_{n}\\cdot \\ddot{a}_{n}$（教材例 3-7 优美结论，证明题考点）。")
# 连续递增年金终值：平方应在分母 δ 上
add("interest.md",
    "$(\\bar{I}\\bar{s})_{n}$ = $\\frac{(1+i)^{n}- 1- n\\delta}{\\delta}^{2}$（现值累积 n 年）",
    "$(\\bar{I}\\bar{s})_{n}$ = $\\dfrac{(1+i)^{n}- 1- n\\delta}{\\delta^{2}}$（现值累积 n 年）")
# 期初付复递增年金乱码分式
add("interest.md",
    "- 期初付：$(C\\ddot{a})_{n}=(1+i)(Ca)_{n}= \\frac{\\frac{1-(1+j)^{-n}}{j \\cdot}(1+r)}{1+r}$ $(C\\ddot{a})_{n}= \\frac{1+i}{(1+r) \\cdot}(Ca)_{n}$",
    "- 期初付：$(C\\ddot{a})_{n}=(1+i)(Ca)_{n}= \\dfrac{(1+i)\\left[1-(1+j)^{-n}\\right]}{(1+r)j}$")
# 例23：增长永续首次支付前一期价值只贴现 1 期；保留教材第 3 年末口径作为对照
add("interest.md",
    "解：先算第 2 年末价值 $\\frac{5000}{0.08- 0.05}= 166 667$，再贴现：$PV= 166667 \\times 1.08^{-2}=142\\,890\\,\\text{元}$（教材 142 889.8）。",
    "解：增长永续在首次支付前一期（第 1 年末）的价值 $= \\dfrac{5000}{0.08- 0.05}= 166 667$，再贴现 1 期得 $PV=166667\\times 1.08^{-1}=154\\,321\\,\\text{元}$；若首次支付在第 3 年末（教材原题口径），则需贴现 2 期：$PV=166667\\times 1.08^{-2}=142\\,890\\,\\text{元}$（教材 142 889.8）。")
# 变额偿债基金：清理残缺的 … 变形
add("interest.md",
    "**贷款本金公式**：L0 = Σ Rt(1+j)^(n−t) / [1 + i·sn|j] = ΣRtvj^(n−t)… 变形：",
    "**贷款本金公式**（由偿债基金期末本利和 = 贷款本金反解）：")
# 例28：10/96.67=10.34%（非 10.53%）
add("interest.md",
    "$i \\approx \\frac{10}{96.67}=10.53\\%$",
    "$i \\approx \\dfrac{10}{96.67}=10.34\\%$")
# 例49：分项现值各自应为 385.54（对称设计），非 400.0 与 371.1
add("interest.md",
    "= 400.0+371.1= 771.09",
    "= 385.54+385.54= 771.09")

# ---------------- securities.md ----------------
add("securities.md",
    "\\frac{8 \\times 10000+9 \\times 8000+7.6 \\times 5000}{5 \\times 10000+6 \\times 8000+3 \\times 5000} \\times 1000=1830.77",
    "\\frac{8 \\times 10000+9 \\times 8000+7.6 \\times 5000}{5 \\times 10000+6 \\times 8000+3 \\times 5000} \\times 1000=1681.42")
add("securities.md",
    "加权平均（计算期市值/总股数 = **8.43 元**）",
    "加权平均（计算期市值/总股数 = **8.26 元**）")
add("securities.md",
    "新除数 = 拆股后总价格 ÷ 拆股前平均数 $=\\dfrac{8.2+3.4+7.8}{8.2}=2.2683$；修正平均股价 $=\\dfrac{19.4}{2.2683}\\approx 8.55\\,\\text{元}$。",
    "新除数 = 拆股后总价格 ÷ 拆股前平均股价 $=\\dfrac{8.2+3.4+7.8}{8.73}\\approx 2.22$；修正平均股价 $=\\dfrac{19.4}{2.22}\\approx 8.73\\,\\text{元}$。")
add("securities.md",
    "$\\sigma_{P} \\approx 22.6$%",
    "$\\sigma_{P} \\approx 19.3$%")
add("securities.md",
    "$\\beta_{i}= \\frac{\\operatorname{Cov}(r_{i},r_{M})}{\\sigma_{M}^{2}}= \\rho_{iM} \\times \\sigma_{i} \\sigma_{M}$",
    "$\\beta_{i}= \\frac{\\operatorname{Cov}(r_{i},r_{M})}{\\sigma_{M}^{2}}= \\rho_{iM}\\dfrac{\\sigma_{i}}{\\sigma_{M}}$")
add("securities.md",
    "解得 $\\lambda_{1} \\approx 5.98$%、$\\lambda_{2} \\approx 5.99$% ≈ 6%，即 $E(r)= 5\\%+ 5.98\\%\\beta_{1}+ 5.99\\%\\beta_{2}$。",
    "解得 $\\lambda_{1} \\approx 9.17$%、$\\lambda_{2} \\approx 4.44$%，即 $E(r)= 5\\%+ 9.17\\%\\beta_{1}+ 4.44\\%\\beta_{2}$。")
add("securities.md",
    "- 期权价格 $C=(0.6 \\times 3+ 0.4 \\times 0)$%×2/12) = 1.8/1.01 ≈ **1.78 元**",
    "- 期权价格 $C=\\dfrac{0.6\\times 3+ 0.4\\times 0}{1+ 6\\%\\times 2/12}= \\dfrac{1.8}{1.01}\\approx$ **1.78 元**")
add("securities.md",
    "$S_{P}= \\frac{E(r_{P})- r_{f}}{\\sigma}_{P}$",
    "$S_{P}= \\frac{E(r_{P})- r_{f}}{\\sigma_{P}}$")
add("securities.md",
    "$T_{P}= \\frac{E(r_{P})- r_{f}}{\\beta}_{P}$",
    "$T_{P}= \\frac{E(r_{P})- r_{f}}{\\beta_{P}}$")
add("securities.md",
    "$IR= \\alpha_{P} \\sigma(\\epsilon_{P})$",
    "$IR= \\dfrac{\\alpha_{P}}{\\sigma(\\epsilon_{P})}$")
add("securities.md",
    "$N= \\frac{100000 \\times 9}{108 \\times 8.8}$ **94.7 → 卖空约 95 手**",
    "$N= \\dfrac{100000 \\times 9}{108 \\times 8.8}\\approx 947$ **手 → 卖空约 947 手**")

# ---------------- finmgr.md ----------------
add("finmgr.md",
    "- 固定增长模型：P0 ＝ $D_{1}$（$r_{s}- g$）＝ D0（1＋g）÷（$r_{s}- g$）",
    "- 固定增长模型：$P_{0}=\\dfrac{D_{1}}{r_{s}- g}=\\dfrac{D_{0}(1+g)}{r_{s}- g}$")
add("finmgr.md",
    "| 股利现金流量模型 | 股利 | 股权价值 ＝ $\\sum D_{t}$（1＋rs）ᵗ |",
    "| 股利现金流量模型 | 股利 | 股权价值 $=\\sum \\dfrac{D_{t}}{(1+r_{s})^{t}}$ |")
add("finmgr.md",
    "| 实体现金流 FCFF | 实体自由现金流 | 实体价值 ＝ $\\sum FCFF_{t}$（1＋WACC）ᵗ；股权价值＝实体价值−净债务 |",
    "| 实体现金流 FCFF | 实体自由现金流 | 实体价值 $=\\sum \\dfrac{FCFF_{t}}{(1+WACC)^{t}}$；股权价值＝实体价值−净债务 |")
add("finmgr.md",
    "| 年金现值 | P＝A×[1−(1＋i)-ⁿ]/i |",
    "| 年金现值 | $P=A\\cdot\\dfrac{1-(1+i)^{-n}}{i}$ |")

# ---------------- tax.md ----------------
add("tax.md",
    "按**纳税年度**（公历 $\\frac{1}{1}- \\frac{12}{31}$）计算",
    "按**纳税年度**（公历 1 月 1 日至 12 月 31 日）计算")
add("tax.md",
    "纳税年度为公历 $\\frac{1}{1}- \\frac{12}{31}$",
    "纳税年度为公历 1 月 1 日至 12 月 31 日")

# ---------------- coa.md ----------------
add("coa.md",
    "\\frac{00}{11} \\to \\; \\text{部分积不变，仅算术右移} \\; \\text{1} \\; \\text{位}",
    "\\text{00、11} \\to \\; \\text{部分积不变，仅算术右移} \\; \\text{1} \\; \\text{位}")
add("coa.md",
    "开源、模块化扩展（$\\frac{\\frac{\\frac{\\frac{\\frac{I}{M}}{A}}{F}}{D}}{C \\cdots}$）",
    "开源、模块化扩展（I/M/A/F/D/C 等，如 RV32IMAFDC）")

# ---------------- econometrics.md ----------------
add("econometrics.md", "| t(m) | $\\frac{Z}{\\sqrt{\\chi^{2}\\frac{m}{m}}}$ |", "| t(m) | $\\dfrac{Z}{\\sqrt{\\chi^{2}(m)/m}}$ |")
add("econometrics.md", "| F(m, n−k−1) | $\\frac{\\chi^{2}\\frac{m}{m}}{\\chi^{2}\\frac{df}{df}}$ |", "| F(m, n−k−1) | $\\dfrac{\\chi^{2}(m)/m}{\\chi^{2}(df)/df}$ |")
add("econometrics.md", "$$\\chi^{2}: \\frac{\\frac{3.84(df=1,5\\%)}{5.99(df=2,5\\%)}}{7.81(df=3,5\\%)}$$", "$\\chi^{2}$ 临界值（5%）：df=1 → 3.84；df=2 → 5.99；df=3 → 7.81")
add("econometrics.md", "$\\operatorname{Cov}(u_{i},u_{j})=0(i=j)$", "$\\operatorname{Cov}(u_{i},u_{j})=0\\;(i\\ne j)$")
add("econometrics.md", "\\operatorname{Var}(\\hat{\\beta}_{1})= \\sigma^{2} Sxx", "\\operatorname{Var}(\\hat{\\beta}_{1})= \\sigma^{2}/Sxx")
add("econometrics.md", "X 上升 1% → Y 变动 $\\beta_{1} 100$ 单位", "X 上升 1% → Y 变动约 $\\beta_{1}/100$（即 $0.01\\beta_{1}$）单位")
add("econometrics.md", "$\\operatorname{Var}(\\hat{\\beta}_{j})= \\sigma^{2}[Sxx_{j}(1- R^{2}_{j})]$", "$\\operatorname{Var}(\\hat{\\beta}_{j})= \\sigma^{2}/[Sxx_{j}(1- R^{2}_{j})]$")
add("econometrics.md", "$\\operatorname{Var}(\\hat{\\beta}_{j})=\\sigma^{2}[Sxx_{j}(1- R^{2}_{j})]$", "$\\operatorname{Var}(\\hat{\\beta}_{j})=\\sigma^{2}/[Sxx_{j}(1- R^{2}_{j})]$")
add("econometrics.md", "X 增 1% → Y 变 $\\beta_{1} 100$ 单位 | $\\beta_{1} X$", "X 增 1% → Y 变约 $\\beta_{1}/100$ 单位 | $\\beta_{1}/X$")
add("econometrics.md", "$\\beta_{1}\\frac{\\cdot Y}{X}$", "$\\beta_{1}\\cdot Y/X$")
add("econometrics.md", "$\\operatorname{Cov}(X, u)= 0$ 是 OLS 最致命的问题", "$\\operatorname{Cov}(X, u)\\ne 0$（内生性）是 OLS 最致命的问题")
add("econometrics.md", "- **相关性**（$\\operatorname{Cov}(Z,X)= 0$，第一阶段足够强）；", "- **相关性**（$\\operatorname{Cov}(Z,X)\\ne 0$，第一阶段足够强）；")
add("econometrics.md", "长期乘数 $= \\beta_{0}(1- \\lambda)$ |", "长期乘数 $= \\beta_{0}/(1- \\lambda)$ |")
add("econometrics.md", "\\text{长期乘数} \\; = \\beta_{0}(1- \\lambda)= \\frac{0.5}{0.4}= 1.25 \\\\", "\\text{长期乘数} \\; = \\beta_{0}/(1- \\lambda)= \\frac{0.5}{0.4}= 1.25 \\\\", 2)
add("econometrics.md", "⇒ $\\operatorname{Cov}(Y_{t}, u_{t})= 0$。用 OLS", "⇒ $\\operatorname{Cov}(Y_{t}, u_{t})\\ne 0$。用 OLS")
add("econometrics.md", "$\\beta= \\pi_{2}(1+\\pi_{2})$", "$\\beta=\\dfrac{\\pi_{2}}{1+\\pi_{2}}$")
add("econometrics.md", "允许 $\\operatorname{Cov}(\\mu_{i}, x_{it})= 0$；一致性更强", "允许 $\\operatorname{Cov}(\\mu_{i}, x_{it})\\ne 0$；一致性更强")
add("econometrics.md", "\\phi\\left(\\beta '\\frac{x}{\\sigma}\\right) \\cdot \\beta_{j} \\sigma \\\\", "\\phi\\left(\\beta 'x/\\sigma\\right) \\cdot \\beta_{j}/\\sigma \\\\")
add("econometrics.md", "\\lambda_{i}= \\frac{\\phi(\\hat{\\gamma}'z_{i})}{\\Phi}(\\hat{\\gamma}'z_{i}) \\\\", "\\lambda_{i}= \\dfrac{\\phi(\\hat{\\gamma}'z_{i})}{\\Phi(\\hat{\\gamma}'z_{i})} \\\\")
add("econometrics.md", "长期乘数 $\\beta_{0}(1- \\lambda)$ |", "长期乘数 $\\beta_{0}/(1- \\lambda)$ |")
add("econometrics.md", "$\\frac{\\ln(0.5)}{\\ln}(1+\\gamma)$", "$\\dfrac{\\ln(0.5)}{\\ln(1+\\gamma)}$")
add("econometrics.md", "$\\operatorname{Cov}(Y_{t},u_{t})=0$ $\\Rightarrow$ 有偏且不一致", "$\\operatorname{Cov}(Y_{t},u_{t})\\ne 0$ $\\Rightarrow$ 有偏且不一致")
add("econometrics.md", "加变量后要同时看调整 $\\frac{\\frac{R^{2}}{AIC}}{SC}$ 与理论依据。", "加变量后要同时看调整 R²、AIC/SC 与理论依据。")

# ---------------- macro.md ----------------
add("macro.md", "分母再加 m：$Y= \\frac{\\cdots}{1- b(1- t)+ m}$ |", "分母再加 m：$Y= \\dfrac{a- bT_{0}+ bTR_{0}+ I_{0}+ G_{0}+ X_{0}- M_{0}}{1- b(1- t)+ m}$ |")
add("macro.md", "$\\frac{\\Delta A}{A}= \\frac{\\Delta Y}{Y}- \\alpha \\frac{\\cdot \\Delta K}{K}- \\beta \\frac{\\cdot \\Delta L}{L}$", "$\\dfrac{\\Delta A}{A}= \\dfrac{\\Delta Y}{Y}-\\alpha\\dfrac{\\Delta K}{K}-\\beta\\dfrac{\\Delta L}{L}$")
add("macro.md", "$\\frac{\\Delta Y}{Y}= \\frac{\\Delta A}{A}+ \\alpha \\frac{\\cdot \\Delta K}{K}+ \\beta \\frac{\\cdot \\Delta L}{L}$", "$\\dfrac{\\Delta Y}{Y}= \\dfrac{\\Delta A}{A}+\\alpha\\dfrac{\\Delta K}{K}+\\beta\\dfrac{\\Delta L}{L}$")

# ---------------- micro.md ----------------
add("micro.md", "$\\frac{dPs}{dt}=-\\lvert E_d\\rvert(eS+\\lvert E_d\\rvert)$", "$\\dfrac{dP_{s}}{dt}=-\\dfrac{|E_{d}|}{e_{S}+|E_{d}|}$")
add("micro.md", "$\\lvert E_d\\rvert=\\left(\\frac{1}{2}\\right) \\cdot\\left(\\frac{12}{26}\\right) \\cdot 2= \\frac{12}{13} \\approx 0.923$", "$|E_{d}|=2\\times\\dfrac{12}{26}=\\dfrac{12}{13}\\approx 0.923$")
add("micro.md", "$DWL \\approx \\frac{1}{2} \\cdot t^{2} \\cdot(Q* P*) \\cdot[\\lvert E_d\\rvert \\frac{\\cdot eS}{\\lvert E_d\\rvert+eS}]$", "$DWL\\approx\\dfrac{1}{2}\\,t^{2}\\,\\dfrac{Q^{*}}{P^{*}}\\cdot\\dfrac{|E_{d}|\\,e_{S}}{|E_{d}|+e_{S}}$")
add("micro.md", "$\\frac{MPL}{w}= \\frac{MPK}{r}= \\lambda$，其中 $\\lambda= \\frac{1}{MC}$，即**拉格朗日乘子就是边际成本的倒数**。", "$\\dfrac{MPL}{w}= \\dfrac{MPK}{r}= \\dfrac{1}{MC}$（按 $L=wL+rK+\\lambda(Q_{0}-f)$ 的约定，乘子 $\\lambda=MC$，公共比值为 $1/\\lambda=1/MC$，即边际成本的倒数）。")
add("micro.md", "$P_{1}(1- 1|E_{1}|)= P_{2}(1- 1|E_{2}|)= MC$", "$P_{1}\\left(1-\\dfrac{1}{|E_{1}|}\\right)=P_{2}\\left(1-\\dfrac{1}{|E_{2}|}\\right)=MC$")
add("micro.md", "$\\frac{\\pi C}{1- \\delta} \\ge \\pi D+ \\delta \\frac{\\cdot \\pi N}{1- \\delta}$ ⇔ $\\delta \\ge \\frac{\\pi D- \\pi C}{\\pi D- \\pi N}$", "$\\dfrac{\\pi_{C}}{1-\\delta}\\ \\ge\\ \\pi_{D}+\\delta\\dfrac{\\pi_{N}}{1-\\delta}$ ⇔ $\\delta \\ge \\dfrac{\\pi_{D}-\\pi_{C}}{\\pi_{D}-\\pi_{N}}$")
add("micro.md", "对同比例的收入整体平移不敏感", "对所有人收入同比例缩放（同乘一个系数）不敏感")
add("micro.md", "- **无限次重复 / 贴现率足够高**：", "- **无限次重复 / 贴现因子 δ 足够高（贴现率足够低）**：")
add("micro.md", "\\Delta Q=+10, \\Delta P=- 1 \\to-(10- 1)= 10 \\\\", "\\Delta Q=+10,\\ \\Delta P=-1\\ \\Rightarrow\\ -\\dfrac{\\Delta Q}{\\Delta P}=-\\dfrac{10}{-1}=10 \\\\")
add("micro.md", "$\\alpha+\\beta> 1= 1< 1$", "$\\alpha+\\beta>1$、$\\alpha+\\beta=1$、$\\alpha+\\beta<1$")
add("micro.md", "$P_{1}(1- 1\\vert E_{1}\\vert )= P_{2}(1- 1\\vert E_{2}\\vert )= MC$", "$P_{i}\\left(1-\\dfrac{1}{|E_{i}|}\\right)=MC$")

# ---------------- math.md ----------------
# 全文下标错乱：\to_{\infty} → \to \infty
add("math.md", "\\to_{\\infty}", "\\to \\infty", 10)
add("math.md", "$\\lim_{x \\to 0} \\sin \\frac{x}{x}= 1$；$\\lim_{x \\to \\infty}\\left(1+\\frac{1}{x}\\right)^{x}= e$", "$\\lim_{x \\to 0} \\dfrac{\\sin x}{x}= 1$；$\\lim_{x \\to \\infty}\\left(1+\\frac{1}{x}\\right)^{x}= e$", 2)
add("math.md", "$\\lim_{x \\to 0} \\sin \\frac{3x}{5x}= \\frac{3}{5}$", "$\\lim_{x \\to 0} \\dfrac{\\sin 3x}{5x}= \\dfrac{3}{5}$")
add("math.md", "$\\left(\\frac{1}{x+a}\\right)^{(n)}=(- 1)^{n} n!(x+a)^{n+1}$", "$\\left(\\dfrac{1}{x+a}\\right)^{(n)}=\\dfrac{(-1)^{n}\\,n!}{(x+a)^{n+1}}$")
add("math.md", "$\\left(\\frac{1}{x+a}\\right)^{(n)}=(- 1)^{n}n!(x+a)^{n+1}$", "$\\left(\\dfrac{1}{x+a}\\right)^{(n)}=\\dfrac{(-1)^{n}\\,n!}{(x+a)^{n+1}}$")
add("math.md", "**曲率** $\\kappa=|y''|(1+y'^{2})^{\\frac{3}{2}}$", "**曲率** $\\kappa=\\dfrac{|y''|}{(1+y'^{2})^{\\frac{3}{2}}}$")
add("math.md", "`n` 偶 ⇒ $(n- 1)!! n!! \\cdot \\frac{\\pi}{2}$；`n` 奇 ⇒ $(n- 1)!! n!!$", "`n` 偶 ⇒ $\\dfrac{(n-1)!!}{n!!}\\cdot\\dfrac{\\pi}{2}$；`n` 奇 ⇒ $\\dfrac{(n-1)!!}{n!!}$")
add("math.md", "$\\kappa=\\vert y''\\vert (1+y'^{2})^{\\frac{3}{2}}$", "$\\kappa=\\dfrac{\\vert y''\\vert}{(1+y'^{2})^{\\frac{3}{2}}}$")
add("math.md", "$\\frac{f(b)- f(a)}{g(b)- g(a)}=f'\\frac{\\xi}{g}'(\\xi)$", "$\\dfrac{f(b)- f(a)}{g(b)- g(a)}=\\dfrac{f'(\\xi)}{g'(\\xi)}$")
add("math.md", "$\\lim \\frac{f}{g}= \\lim f' g'$", "$\\lim \\dfrac{f}{g}=\\lim \\dfrac{f'}{g'}$")
add("math.md", "$\\int x^a dx=\\frac{x^{a+1}}{a+1}+C(a=- 1)$", "$\\int x^{a}\\,dx=\\dfrac{x^{a+1}}{a+1}+C\\ (a\\ne -1)$")
add("math.md", "$I_{n}=\\frac{n- 1}{n \\cdot I_{n-2}}$；偶 $(n- 1)!! n!! \\frac{\\cdot \\pi}{2}$，奇 $(n- 1)!! n!!$", "$I_{n}=\\dfrac{n-1}{n}\\,I_{n-2}$；偶 $\\dfrac{(n-1)!!}{n!!}\\cdot\\dfrac{\\pi}{2}$，奇 $\\dfrac{(n-1)!!}{n!!}$")
add("math.md", "$\\frac{dx}{dy}=\\frac{1}{y}'$", "$\\dfrac{dx}{dy}=\\dfrac{1}{y'}$")
add("math.md", "$I_{2}= \\frac{1}{2} \\frac{\\cdot \\pi}{2}= \\frac{\\pi}{4}$", "$I_{2}= \\dfrac{1}{2}\\cdot\\dfrac{\\pi}{2}= \\dfrac{\\pi}{4}$")
add("math.md", "$f' g'= 1+\\cos x$", "$f'/g'= 1+\\cos x$")
# 占位符 / 乱码（工作例题块内）
add("math.md", "\\text{(2) 三重积分\\_{} \\; \\text{上半球} \\; \\text{x2+y2+z2≤1, z≥0} z dV} \\\\", "\\text{(2) 上半球} \\; \\iiint_{\\Omega} z\\,dV \\; (\\Omega: x^{2}+y^{2}+z^{2}\\le 1,\\, z\\ge 0) \\\\")
add("math.md", "\\text{(2)} \\; \\text{奇点陷阱：} \\; \\text{环积分\\_{} \\; \\text{单位圆} \\; \\text{} (x dy−y dx)/(x2+y2) = 2π} \\\\", "\\text{(2)} \\; \\text{奇点陷阱：} \\; \\oint_{L}\\dfrac{x\\,dy-y\\,dx}{x^{2}+y^{2}} = 2\\pi \\\\")
add("math.md", "(1) \\int_{0}^{\\frac{\\pi}{2}} \\sin^{2}x dx= \\int_{0}\\frac{^{\\frac{\\pi}{2}}(1- \\cos 2x)}{2 dx} \\\\", "(1)\\; \\int_{0}^{\\frac{\\pi}{2}}\\sin^{2}x\\,dx=\\int_{0}^{\\frac{\\pi}{2}}\\dfrac{1-\\cos 2x}{2}\\,dx \\\\")
add("math.md", "\\int_{0}\\frac{^{1} dx}{x^{p}}", "\\int_{0}^{1}\\dfrac{dx}{x^{p}}", 2)
add("math.md", "\\text{(4) 三重积分\\_{} \\; \\text{上半球} \\; \\text{} z dV = 积分0(2π)dθ积分0(π/2)sinφ cosφ dφ积分01ρ3dρ} \\\\", "\\text{(4)} \\; \\iiint_{\\text{上半球}} z\\,dV=\\int_{0}^{2\\pi}\\!d\\theta\\int_{0}^{\\pi/2}\\!\\sin\\phi\\cos\\phi\\,d\\phi\\int_{0}^{1}\\!\\rho^{3}d\\rho \\\\")
add("math.md", "\\text{(5) 三重积分\\_{} \\; \\text{单位球} \\; \\text{} 1 dV = 4π/3 ≈ 4.188790}", "\\text{(5) 单位球} \\; \\iiint_{\\Omega} 1\\,dV=\\dfrac{4\\pi}{3}\\approx 4.188790")
add("math.md", "\\text{(2)} \\; \\text{奇点陷阱：} \\; \\text{环积分\\_{} \\; \\text{单位圆} \\; \\text{}(x dy−y dx)/(x2+y2)} \\\\", "\\text{(2)} \\; \\text{奇点陷阱：} \\; \\oint_{L}\\dfrac{x\\,dy-y\\,dx}{x^{2}+y^{2}} \\\\")
add("math.md", "\\text{(1) I2 = (积分 0 到无穷 e(−x2)dx)(积分 0 到无穷 e(−y2)dy) = 二重积分\\_{} \\; \\text{第一象限} \\; \\text{} e(−(x2+y2))dxdy} \\\\", "\\text{(1)} \\; I^{2}=\\left(\\int_{0}^{\\infty}e^{-x^{2}}dx\\right)\\left(\\int_{0}^{\\infty}e^{-y^{2}}dy\\right)=\\iint_{\\text{第一象限}}e^{-(x^{2}+y^{2})}\\,dxdy \\\\")
add("math.md", "\\text{，代入} \\; (- A \\cdot ?) \\; \\text{计算：} \\\\", "\\text{，代入方程} \\; y*''- y*= e^{x} \\; \\text{计算：} \\\\")
add("math.md", "\\oint \\frac{_{L}(x dy- y dx)}{2}", "\\oint_{L}\\dfrac{x\\,dy-y\\,dx}{2}")

# ---------------- mltheory.md ----------------
add("mltheory.md", "\\to_{\\infty}", "\\to \\infty", 4)
add("mltheory.md", "$\\frac{\\hat{y} \\to 0}{1}$ 使 R→0", "$\\hat y\\to 0$ 或 $\\hat y\\to 1$ 使 $R\\to 0$")
add("mltheory.md", "\\sqrt{d}_{k}", "\\sqrt{d_{k}}", 7)
add("mltheory.md", "\\frac{1- \\epsilon_{t}}{\\epsilon}_{t}", "\\dfrac{1-\\epsilon_{t}}{\\epsilon_{t}}", 5)
add("mltheory.md", "\\exp\\left(- \\| x- z \\| \\frac{^{2}}{2\\sigma^{2}}\\right)", "\\exp\\left(-\\dfrac{\\|x-z\\|^{2}}{2\\sigma^{2}}\\right)", 2)
add("mltheory.md", "$x_{t}=\\sqrt{\\alpha}_{t}x_{t-1}+\\sqrt{1- \\alpha_{t}}\\epsilon$", "$x_{t}=\\sqrt{\\alpha_{t}}\\,x_{t-1}+\\sqrt{1-\\alpha_{t}}\\,\\epsilon$")


def main():
    ok = bad = 0
    cache = {}
    for f, old, new, n in E:
        p = SRC / f
        if f not in cache:
            cache[f] = p.read_text(encoding="utf-8")
        txt = cache[f]
        c = txt.count(old)
        if c != n:
            print("FAIL %-18s 期望 %d 处, 实际 %d 处 | %s" % (f, n, c, old[:55]))
            bad += 1
            continue
        # 始终在内存副本上模拟替换，保证 --dry 与真实执行行为一致
        cache[f] = txt.replace(old, new)
        ok += 1
    print("\n成功 %d 条, 失败 %d 条 %s" % (ok, bad, "(仅预演)" if DRY else "(已写回源文件)"))
    if not DRY:
        for f, txt in cache.items():
            (SRC / f).write_text(txt, encoding="utf-8")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
