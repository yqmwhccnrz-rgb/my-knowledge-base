---
summary: "孟生旺《利息理论及其应用》（第4版）7 章精要笔记：利息度量（累积函数/实际利率/名义利率/贴现率/利息力）→ 等额年金 → 变额年金（递增/递减/复递增/连续）→ 收益率与收益分配（IRR/币值加权/时间加权/MIRR）→ 债务偿还（分期偿还/偿债基金）→ 债券价值分析（四大定价公式/账面值/可赎回债券）→ 利率风险管理（久期/凸度/免疫/现金流配比）；按考点重排为表格与短条目，补全公式推导与计算例题，配 5 张自绘结构图。"
---

# 利息理论笔记

::: info 笔记概要
- **所属课程**：《利息理论》（孟生旺《利息理论及其应用》第 4 版，中国人民大学出版社，2021）
- **核心内容**：利息度量工具 → 等额年金 → 变额年金 → 收益率与收益分配 → 债务偿还方法 → 债券价值分析 → 利率风险管理
- **学习建议**：全书是一条公式链——一切从累积函数 a(t) 出发，年金的现值/终值是一切应用的地基，债券定价与久期凸度是年金的综合应用；计算题主线是「列价值方程 → 选对年金符号 → 利率换算」，务必熟记 i、d、v、δ、<img class="fml" src="/formulas/fab53528f38d07.png" alt="i^{(m)}" width="35" height="33">、<img class="fml" src="/formulas/12e414056d789a.png" alt="d^{(m)}" width="37" height="33"> 六者互换
- **考试题型**：计算题占绝对主导（每章 20+ 道习题），辅以概念辨析（单利 vs 复利、币值加权 vs 时间加权、麦考利 vs 修正久期）
- **关键词**：累积函数、实际利率、名义利率、实际贴现率、利息力、等额年金、变额年金、价值方程、收益率、净现值、分期偿还、偿债基金、债券定价、溢价折价、久期、凸度、免疫
:::

## 全书目录

| 章节 | 主要内容 | 重要度 |
| --- | --- | --- |
| 第 1 章 | 利息度量：累积函数、单利复利、实际/名义利率、实际/名义贴现率、利息力 | ★★★ 一切公式的地基 |
| 第 2 章 | 等额年金：现值、终值、任意时点价值、每年支付 m 次、连续支付、价值方程 | ★★★ 计算题核心 |
| 第 3 章 | 变额年金：递增、递减、复递增、每年 m 次变额、连续变额、一般现金流积分 | ★★★ 计算高频 |
| 第 4 章 | 收益率和收益分配：IRR 与净现值、币值加权、时间加权、修正收益率、投资年度法 | ★★★ 概念 + 计算 |
| 第 5 章 | 债务偿还方法：等额分期偿还、等额偿债基金、变额分期、变额偿债基金 | ★★★ 计算题主线 |
| 第 6 章 | 债券价值分析：四大定价公式、溢价折价、账面值、任意时点价格、可赎回债券 | ★★★ 计算高频 |
| 第 7 章 | 利率风险管理：麦考利/修正/有效久期、凸度、Redington 免疫、完全免疫、现金流配比 | ★★★ 计算 + 简答 |

![利息度量工具换算网络](/int/int-measures.svg)

---

## 第1章 利息度量

**利息**是借款人为获得资金使用权向贷款人支付的款项：对借款人是成本，对贷款人是推迟消费的补偿。三种解释：资金是稀缺资源须付成本；出借资金推迟当期消费应获补偿；资金作为生产要素参与成果分配。

本章符号表（全书通用）：

| 符号 | 含义 |
| --- | --- |
| a(t) | 累积函数：时刻 0 的 1 单位本金在时刻 t 的价值 |
| <img class="fml" src="/formulas/101b50c873d0ce.png" alt="a^{-1}(t)" width="54" height="33"> | 贴现函数：时刻 t 的 1 单位本金在时刻 0 的价值 |
| i | 实际利率（有效利率）：1 单位本金一个时期末产生的利息 |
| d | 实际贴现率 |
| <img class="fml" src="/formulas/fab53528f38d07.png" alt="i^{(m)}" width="35" height="33"> / <img class="fml" src="/formulas/12e414056d789a.png" alt="d^{(m)}" width="37" height="33"> | 每年复利/贴现 m 次的名义利率、名义贴现率 |
| δ | 利息力（连续复利）；<img class="fml" src="/formulas/b9a1240560ebce.png" alt="\delta(t)" width="36" height="33"> 为时刻 t 的利息力 |
| v | 贴现因子，<img class="fml" src="/formulas/9bd09a95d133f7.png" alt="v= \frac{1}{1+i}= 1- d" width="129" height="34"> |

### 1.1 累积函数与实际利率（★★★）

**累积函数 a(t)** 是期初 1 单位本金在时刻 t 的累积值，是一切利息度量工具的母体。三条性质：

1. a(0) = 1；
2. a(t) 通常递增（利息非负；投资亏本时可能递减）；
3. 连续计息时 a(t) 连续。

**金额函数**：期初本金为 A(0) 时，<img class="fml" src="/formulas/1209dce5258911.png" alt="A(t)= A(0) \cdot a(t)" width="143" height="33">；反之 <img class="fml" src="/formulas/afed9eb8ccf40c.png" alt="a(t)= \frac{A(t)}{A(0)}" width="90" height="36">。利息额 <img class="fml" src="/formulas/51206169f0c403.png" alt="I(t)= A(t)- A(0)" width="152" height="33">。

**实际利率**（effective rate of interest）：1 单位本金在一个时期末赚取的利息金额。

**时期 <img class="fml" src="/formulas/b5b066e79b633a.png" alt="(t-1, t)" width="73" height="33"> 的实际利率**：



<p class="fml-block"><img class="fml" src="/formulas/f24c4ef07328a2.png" alt="i_{t}=\frac{a(t)-a(t-1)}{a(t-1)}=\frac{A(t)-A(t-1)}{A(t-1)}" width="215" height="36"></p>



- **第一期**：<img class="fml" src="/formulas/d3134fd5179040.png" alt="i=a(1)-1" width="100" height="33">，故 <img class="fml" src="/formulas/2e17daa5af11f6.png" alt="a(1)=1+i" width="100" height="33">
- **支付时点**：实际利率产生的利息只能在**期末一次性支付**

<div class="kb-example">

**例 1**（教材例 1-1）：累积函数 <img class="fml" src="/formulas/aa8ee392773bed.png" alt="a(t)= 1.2^{t}+ 0.05t" width="149" height="33">，求 t=2 时的 500 万元在 t=3 时的价值。
解：从 t=2 到 t=3 的价值比为



<p class="fml-block"><img class="fml" src="/formulas/5c71e089a90850.png" alt="\frac{a(3)}{a(2)}=\frac{1.728+0.15}{1.44+0.10}=\frac{1.878}{1.54}" width="179" height="36"></p>



故 <img class="fml" src="/formulas/80a832c81fdb2d.png" alt="500\times\frac{1.878}{1.54}=609.74\,\text{万元}" width="200" height="33">。

（要点：不同时刻之间换算资金价值一律用 <img class="fml" src="/formulas/9b6a08a0a7d98e.png" alt="\frac{a(t_{2})}{a(t_{1})}" width="38" height="36"> 这个比值。）

</div>
### 1.2 单利与复利（★★★ 辨析高频）

| 项目 | 单利 | 复利 |
| --- | --- | --- |
| 累积函数 | <img class="fml" src="/formulas/6b8b488127a33f.png" alt="a(t) = 1+it" width="104" height="33">（线性） | <img class="fml" src="/formulas/00a20e5d48105d.png" alt="a(t)=(1+i)^{t}" width="116" height="33">（几何级数） |
| 利息是否再生息 | 否 | 是（自动再投资） |
| 实际利率 it | <img class="fml" src="/formulas/0eadc83d8256a4.png" alt="\frac{i}{1+i(t-1)}" width="62" height="36">，随 t **递减** | 恒等于 i（**一致性**） |
| 分段投资 | 段数越多利息越多（缺陷） | 与分段无关 |
| 0<t<1 | 累积值 > 复利 | — |
| t>1 | 累积值 < 复利 | — |
| t=0 或 1 | 两者相等 | 两者相等 |

利率较低且期限不足 1 年时可用单利近似复利：<img class="fml" src="/formulas/d987c9b96092e1.png" alt="(1+i)^{t}" width="63" height="33">。

<div class="kb-example">

**例 2**：借款 20 000 元，4 年后还 25 249.54 元，求年复利利率。
解：<img class="fml" src="/formulas/2325f54212678c.png" alt="20000(1+i)^{4}= 25249.54 \to(1+i)^{4}= 1.262477" width="377" height="33"> **i = 6%**。

</div>
**计息天数规则**（t = 投资天数 / 一年天数）：

| 规则 | 投资天数 | 一年天数 | 特点 |
| --- | --- | --- | --- |
| 实际/365 | 实际天数 | 365 | 精确 |
| 实际/360（银行家规则） | 实际天数 | 360 | 利息最大 |
| 30/360 | 每月按 30 天 | 360 | 利息最小；<img class="fml" src="/formulas/d0706059dc7948.png" alt="360(Y_{2}- Y_{1})+30(M_{2}- M_{1})+(D_{2}- D_{1})" width="330" height="33">，另有 4 条日期调整细则 |

<div class="kb-example">

**例 3**：2014-6-14 存 10 000 元，2015-2-7 取出，年单利 8%。实际天数 238：
- 实际/365：<img class="fml" src="/formulas/3a5951ff8be44f.png" alt="\frac{10000 \times 0.08 \times 238}{365}=521.6\,\text{元}" width="189" height="33">
- 实际/360：<img class="fml" src="/formulas/57dbdea15b93e1.png" alt="\frac{10000 \times 0.08 \times 238}{360}=528.9\,\text{元}" width="188" height="33">
- 30/360：天数 = <img class="fml" src="/formulas/9008445bd40b4c.png" alt="360 \times 1+30 \times(2- 6)+(7- 14)= 233" width="314" height="33">，利息 = **517.8 元**

</div>
### 1.3 贴现函数与实际贴现率（★★★）

**贴现函数** <img class="fml" src="/formulas/779124f26e5bf6.png" alt="a^{-1}(t)= \frac{1}{a(t)}" width="103" height="36">，用于求现值。单利贴现函数 <img class="fml" src="/formulas/b5407b3530e40e.png" alt="(1+it)^{-1}" width="81" height="33">；复利贴现函数 <img class="fml" src="/formulas/81445208c9fccb.png" alt="(1+i)^{-t}=(1- d)^{t}" width="156" height="33">。

**实际贴现率**（effective rate of discount）：一定时期内产生的利息与**期末累积值**之比（注意定义仍用累积函数）：

- <img class="fml" src="/formulas/fa434c8a5bcec5.png" alt="d_{t}= \frac{a(t)- a(t- 1)}{a(t)}" width="117" height="36">；复利下 <img class="fml" src="/formulas/92dab4b66e0735.png" alt="d= \frac{i}{1+i}= iv" width="104" height="34">
- 期初的 1−d 元期末累积为 1 元 → <img class="fml" src="/formulas/79760246d8819c.png" alt="a(t)=(1- d)^{-t}" width="130" height="33">
- <img class="fml" src="/formulas/0626247ccd6fe8.png" alt="i= \frac{d}{1- d}" width="64" height="34">

**利率 vs 贴现率**：利率以本金（期初值）为计算基础，贴现率以累积值（期末值）为计算基础。换算：利率 = 贴现率/(1−贴现率)。

**四大等价关系**（简答高频，务必背熟）：

1. <img class="fml" src="/formulas/fefe058af83d62.png" alt="d= i \cdot v" width="68" height="33">（实际贴现率 = 实际利率的现值）
2. <img class="fml" src="/formulas/14d55555338efc.png" alt="i- d= id" width="84" height="33">（利率与贴现率之差 = 它们的乘积）
3. <img class="fml" src="/formulas/fbe2949b048775.png" alt="d= 1- v" width="80" height="33">
4. <img class="fml" src="/formulas/0626247ccd6fe8.png" alt="i= \frac{d}{1- d}" width="64" height="34">，<img class="fml" src="/formulas/65deefefe25e19.png" alt="d= \frac{i}{1+i}" width="64" height="34">

**数值范围**：<img class="fml" src="/formulas/58f4170b125792.png" alt="i \in(0,+ \infty)" width="98" height="33">，<img class="fml" src="/formulas/b006c02b9633c8.png" alt="d \in(0, 1)" width="78" height="33">；i→∞ 时 d→1。利率增大时贴现率增长幅度越来越小。

**单贴现率**：<img class="fml" src="/formulas/18ff96d5cdb1f0.png" alt="a^{-1}(t)= 1- dt" width="124" height="33">（<img class="fml" src="/formulas/97cfd411f56f8a.png" alt="0 \le t&lt; \frac{1}{d}" width="80" height="33">），应用有限；贴现期不足 1 年时单贴现现值 > 复贴现现值，超过 1 年时相反；使用单贴现率时**贴现期不能超过 1/d**。

<div class="kb-example">

**例 4**：一年期零息债券面值 100 元、发行价 90 元。利率 <img class="fml" src="/formulas/cbe2196358d457.png" alt="=\frac{10}{90}=11.11\%" width="122" height="33">，贴现率 <img class="fml" src="/formulas/5da828dcbed9cf.png" alt="=\frac{10}{100}=10\%" width="106" height="33">。

</div>
### 1.4 名义利率与名义贴现率（★★★）

**名义利率 <img class="fml" src="/formulas/fab53528f38d07.png" alt="i^{(m)}" width="35" height="33">**：一年复利 m 次（或多年复利一次）的利率；每 <img class="fml" src="/formulas/50ce2dc9bc4d1b.png" alt="1/m" width="40" height="33"> 年的实际利率为 <img class="fml" src="/formulas/fe5a49be0115c0.png" alt="\frac{i^{(m)}}{m}" width="32" height="34">。**只说"名义利率 12%"没有意义，必须说明复利次数**。

核心等价方程（一切换算的总纲）：



<p class="fml-block"><img class="fml" src="/formulas/4321a9e9eb81a4.png" alt="1+ i=\left(1+ \frac{i^{(m)}}{m}\right)^{m}=\left(1- \frac{d^{(n)}}{n}\right)^{-n}= e^\delta" width="313" height="44"></p>



- <img class="fml" src="/formulas/1946b4a4bc2f06.png" alt="i=\left(1+ \frac{i^{(m)}}{m}\right)^{m}- 1" width="156" height="42">；<img class="fml" src="/formulas/b08d39a21dfeec.png" alt="i^{(m)}= m[(1+i)^{\frac{1}{m}}- 1]" width="178" height="33">
- 名义利率的另一解释：每 <img class="fml" src="/formulas/50ce2dc9bc4d1b.png" alt="1/m" width="40" height="33"> 年按 <img class="fml" src="/formulas/fe5a49be0115c0.png" alt="\frac{i^{(m)}}{m}" width="32" height="34"> 计息，与按年实际利率 i 复利计息等价：<img class="fml" src="/formulas/5d84df3e4d9650.png" alt="1+\frac{i^{(m)}}{m}=(1+i)^{\frac{1}{m}}" width="150" height="34">，即按 <img class="fml" src="/formulas/fab53528f38d07.png" alt="i^{(m)}" width="35" height="33"> 单利计息与按 i 复利计息等价
- k 年复利一次的名义利率 = 每年复利 <img class="fml" src="/formulas/06de0c1eabfcbb.png" alt="m= \frac{1}{k}" width="58" height="33"> 次的情形，公式依然成立

**名义贴现率 <img class="fml" src="/formulas/12e414056d789a.png" alt="d^{(m)}" width="37" height="33">**：度量不足一年的一个时间区间内的实际贴现率，每 <img class="fml" src="/formulas/50ce2dc9bc4d1b.png" alt="1/m" width="40" height="33"> 年实际贴现率为 <img class="fml" src="/formulas/4d421c8c282ca8.png" alt="\frac{d^{(m)}}{m}" width="33" height="34">。

- <img class="fml" src="/formulas/97279fd893c87b.png" alt="d= 1-\left(1- \frac{d^{(m)}}{m}\right)^{m}" width="161" height="42">；<img class="fml" src="/formulas/46d53fffc3c0b7.png" alt="d^{(m)}= m[1-(1- d)^{\frac{1}{m}}]" width="185" height="34">

**名义利率与名义贴现率互换**：

**互换关系**（同频次 <img class="fml" src="/formulas/9b374de4e90a7c.png" alt="m=n" width="57" height="34">）：



<p class="fml-block"><img class="fml" src="/formulas/da091c5215a2d4.png" alt="\begin{aligned}
\left(1+\frac{i^{(m)}}{m}\right)\left(1-\frac{d^{(m)}}{m}\right)&amp;=1,\\[4pt]
\frac{i^{(m)}}{m}-\frac{d^{(m)}}{m}&amp;=\frac{i^{(m)}d^{(m)}}{m^{2}},\\[4pt]
\frac{1}{d^{(m)}}-\frac{1}{i^{(m)}}&amp;=\frac{1}{m}.
\end{aligned}" width="283" height="142"></p>



**等价时恒有名义利率 > 名义贴现率**（利率期末付、贴现率期初收）。

**单调性结论**（选择题高频）：

- 名义利率 <img class="fml" src="/formulas/fab53528f38d07.png" alt="i^{(m)}" width="35" height="33"> 给定 → 复利次数 <img class="fml" src="/formulas/d0fa7c3b5984b6.png" alt="m" width="23" height="34"> 越多，年实际利率**越大**，极限为 <img class="fml" src="/formulas/f58632e1154dbb.png" alt="e^{i^{(m)}}-1" width="67" height="34">（即连续复利下的利息力 <img class="fml" src="/formulas/8de607292a6775.png" alt="\delta" width="15" height="34">）
- 名义贴现率 <img class="fml" src="/formulas/12e414056d789a.png" alt="d^{(m)}" width="37" height="33"> 给定 → 贴现次数 <img class="fml" src="/formulas/d0fa7c3b5984b6.png" alt="m" width="23" height="34"> 越多，年实际贴现率**越小**

<div class="kb-example">

**例 5**：2000 元按每年复利 4 次的年名义利率 6% 投资 2.5 年。
解法一：季度实际利率 1.5%，共 10 个季度：<img class="fml" src="/formulas/89e0305d0c7600.png" alt="2000 \times 1.015^{10}=2321.08\,\text{元}" width="222" height="34">。
解法二：年实际利率 = <img class="fml" src="/formulas/c14dea8cd7dd80.png" alt="1.015^{4}- 1= 6.1364" width="159" height="34">%，<img class="fml" src="/formulas/0a054882e94fe5.png" alt="2000 \times 1.061364^2.5=2321.08\,\text{元}" width="256" height="34">。

**银行存款利率就是名义利率**：3 个月期 1.8% 意味着季度实际利率 0.45%，等价年利率 1.812%；3 年期 3.69% 意味着 3 年实际利率 11.07%，等价年利率 3.562%。规律：期限 < 1 年时名义利率 < 等价实际利率；期限 > 1 年时名义利率 > 等价实际利率，且期限越长差异越大。

</div>
### 1.5 利息力（★★★ 计算高频）

**利息力 δ(t)**（force of interest，连续复利）：资本在**每一时点**上的利息增长强度：

- <img class="fml" src="/formulas/99d1f9157c6250.png" alt="\delta(t)= a" width="69" height="34">′<img class="fml" src="/formulas/6bf34090050df5.png" alt="\frac{t}{a(t)}=[\ln a(t)]" width="114" height="37">′ = A′(t)/A(t)
- 累积函数反推：<img class="fml" src="/formulas/a6b3ccc007565d.png" alt="a(t)= \exp\left( \int_{0}^{t} \delta(s)ds\right)" width="181" height="41">
- 复利下 <img class="fml" src="/formulas/ee20c9a011f5d0.png" alt="\delta= \ln(1+i)" width="105" height="34"> 为常数；<img class="fml" src="/formulas/7ea48f15671425.png" alt="i= e^\delta- 1" width="83" height="34">
- 单利下 <img class="fml" src="/formulas/e437344dc0fe72.png" alt="\delta(t)= \frac{i}{1+it}" width="89" height="35">，随 t 递减
- <img class="fml" src="/formulas/1e0bdbd8539119.png" alt="\delta= \lim i^{(m)}= \lim d^{(m)}" width="177" height="34">（m→∞），即利息力是名义利率/名义贴现率的共同极限
- δ 是常数 ⟹ i 常数；反之不成立（i 是时期平均强度，δ 是时点强度）

**贴现力**：<img class="fml" src="/formulas/82777efb8effc0.png" alt="\delta(t)=-[a^{-1}(t)]" width="130" height="34">′<img class="fml" src="/formulas/101b50c873d0ce.png" alt="a^{-1}(t)" width="54" height="33">；可证**贴现力 = 利息力**（时点概念，期初期末重叠），实务中只用利息力。

**六者换算总表**（知道任意一个可求其余）：

| 已知 | i | d | v | δ |
| --- | --- | --- | --- | --- |
| i | — | i/(1+i) | 1/(1+i) | ln(1+i) |
| d | <img class="fml" src="/formulas/e7e3df4ffac997.png" alt="\frac{d}{1- d}" width="34" height="35"> | — | 1−d | <img class="fml" src="/formulas/57448ae9afc209.png" alt="- \ln(1- d)" width="93" height="34"> |
| v | <img class="fml" src="/formulas/e2dc2ecbc4a75d.png" alt="\frac{1}{v}- 1" width="48" height="34"> | 1−v | — | <img class="fml" src="/formulas/e64ff2fac72536.png" alt="- \ln v" width="51" height="34"> |
| δ | <img class="fml" src="/formulas/b240bb3d93d2b1.png" alt="e^\delta- 1" width="53" height="34"> | <img class="fml" src="/formulas/638c850877b8a4.png" alt="1- e^- \delta" width="66" height="34"> | <img class="fml" src="/formulas/1e1c62e66ba9d8.png" alt="e^- \delta" width="34" height="34"> | — |

**等价工具数值大小关系**（m<n）：<img class="fml" src="/formulas/2dd874284d862f.png" alt="d \le d^{(n)} \le d^{(m)} \le \delta \le i^{(m)} \le i^{(n)} \le i" width="284" height="34">
记忆：支付越早数值越小——贴现率年初预收最小，利率年末支付最大，利息力连续居中；复利/贴现次数越多越靠近 δ。

<div class="kb-example">

**例 6**：金额函数 <img class="fml" src="/formulas/920bd5dc0c40fd.png" alt="A(t)= 8t^{2}+2t+100" width="173" height="34">，求 t=0.5 的利息力。
解：<img class="fml" src="/formulas/12780228d5981a.png" alt="\delta(t)= A" width="73" height="34">′<img class="fml" src="/formulas/4d81a2de6908c0.png" alt="\frac{t}{A(t)}= \frac{16t+2}{8t^{2}+2t+100}" width="128" height="37">，<img class="fml" src="/formulas/ff9a6df90ccd77.png" alt="\delta(0.5)= \frac{10}{103}=9.71\%" width="170" height="34">。

</div>
<div class="kb-example">

**例 7**：投资者 A 按单利 10% 计息，投资者 B 按利息力 <img class="fml" src="/formulas/52956ecfa85ad9.png" alt="\delta(t)= \frac{t}{120}+ k" width="114" height="34"> 计息，第 4 年末到第 8 年末两人利息相等，求 k。
解：A 的利息 = <img class="fml" src="/formulas/149c0c8aeea0e8.png" alt="1.8X- 1.4X" width="107" height="34">；B 的利息 = <img class="fml" src="/formulas/0a78c9611ce1ca.png" alt="X\left(e^{\int_{4}^{8}\delta}- 1\right)= X\left(e^{\frac{24}{120}+4k}- 1\right)= X(e^{0.2+4k}- 1)" width="387" height="42">。
令 <img class="fml" src="/formulas/852266e2d3459a.png" alt="0.4= e^{0.2+4k}- 1 \to e^{0.2+4k}= 1.4 \to 4k= \ln 1.4- 0.2= 0.1365" width="483" height="34"> <img class="fml" src="/formulas/54b49ed20fb248.png" alt="k \approx 0.0341" width="91" height="34">（教材例 1-22 中 <img class="fml" src="/formulas/48de83738f026b.png" alt="k= \frac{1}{120}" width="63" height="34"> 相应形式，方法一致：分段积分 + 令利息相等）。

</div>
### 1.6 利率概念辨析（★★ 简答）

**本书 vs 经济学中的"实际/名义利率"完全是两码事**：

| 语境 | 实际利率 | 名义利率 |
| --- | --- | --- |
| 本书（精算） | 每度量期复利一次的利率 | 一期内复利多次/多期复利一次 |
| 经济学 | 扣除通胀后的利率 r | 未扣除通胀的利率 i |

经济学关系（费雪方程）：<img class="fml" src="/formulas/43545ab4c82f9a.png" alt="1+i=(1+r)(1+\pi)" width="177" height="34">，近似 <img class="fml" src="/formulas/1dc6a2934d0535.png" alt="i \approx r+ \pi" width="78" height="34">（实际利率 ≈ 名义利率 − 通胀率）。预期通胀率 > 名义利率时贷款人实际获得负利息收入。

### 1.7 易错点

- 单利**不满足一致性**：实际利率随时间递减、分段投资会多赚利息；复利满足一致性。
- 实际贴现率定义的分母是**期末累积值**不是期初本金—<img class="fml" src="/formulas/bfd9c2b353e25b.png" alt="- d= iv" width="69" height="34"> 而非 <img class="fml" src="/formulas/2cf773e71a593a.png" alt="d = i" width="46" height="33">。
- 名义利率/名义贴现率**必须与复利（贴现）次数配对**，单独一个数字无意义。
- <img class="fml" src="/formulas/fab53528f38d07.png" alt="i^{(m)}" width="35" height="33"> 与 <img class="fml" src="/formulas/12e414056d789a.png" alt="d^{(m)}" width="37" height="33"> 等价时 <img class="fml" src="/formulas/4d3778d769d806.png" alt="i^{(m)}&gt; d^{(m)}" width="90" height="34"> 恒成立。
- 复利次数 m 增大：等价年实际利率 i **增大**、年实际贴现率 d **减小**（方向相反，常考选择题）。
- 单贴现率只能用于 t < 1/d 的期限，否则现值为负。
- δ 为常数 ⟺ 复利；i 为常数 ⇏  δ 为常数。

---

## 第2章 等额年金

**年金**（annuity）：一系列付款或收款。六种分类（名词解释常考）：

| 分类角度 | 类型 |
| --- | --- |
| 支付时间金额是否确定 | 确定年金 / 风险年金（如终身生存年金） |
| 支付期限 | 定期年金 / 永续年金（无到期日债券利息、优先股股息） |
| 支付周期 | 每年一次 / 每季 / 每月 / 连续年金 |
| 支付时点 | 期初付（annuity-due）/ 期末付（annuity-immediate） |
| 首次支付时间 | 即期年金 / 延期年金 |
| 付款金额 | 等额年金 / 变额年金 |

![年金公式树](/int/int-annuity.svg)

### 2.1 年金现值（★★★ 全书地基）

**期末付定期年金**（n 期，每期末付 1 元）：



<p class="fml-block"><img class="fml" src="/formulas/07177192a084e9.png" alt="a_{n}= v+ v^{2}+ \cdots+ v^{n}= \frac{1- v^{n}}{i}" width="235" height="34"></p>



证明思路：写出现值和，两边乘 (1+i) 相减（等比数列错位相减）。

**恒等式 <img class="fml" src="/formulas/5e3815f8c1d4be.png" alt="ian + v^{n} = 1" width="105" height="33">** 的经济解释：期初 1 元本金 = 每期利息 i 的现值 <img class="fml" src="/formulas/e170c17a0e8345.png" alt="ia_{n}" width="31" height="34"> 期末收回本金的现值 vⁿ。

**期初付定期年金**（每期初付 1 元）：



<p class="fml-block"><img class="fml" src="/formulas/daf62fb38a6cf4.png" alt="\ddot{a}_{n}= \frac{1- v^{n}}{d}=(1+i) \cdot a_{n}= 1+ a_{(n-1)}" width="285" height="34"></p>



（期初付比期末付每笔都提前一期，故乘 (1+i)；n 次期初付款 = 时刻 0 的 1 元 + 后 n−1 次期末付款。）

**期末付永续年金**：<img class="fml" src="/formulas/9f633a76f59b0c.png" alt="a_{\infty}= \frac{1}{i}" width="64" height="34">（n→∞ 的极限）。经济含义：期初存 1/i 元，本金不动可永远每期末取出 1 元利息。
**期初付永续年金**：<img class="fml" src="/formulas/f0f3c383e51c87.png" alt="\ddot{a}_{\infty}= \frac{1}{d}= \frac{1+i}{i}" width="113" height="34">。

<div class="kb-example">

**例 8**：一笔年金 20 年内每年末付 4，另一笔 10 年内每年末付 5，现值相等，求投资翻番所需年数 n。
解：<img class="fml" src="/formulas/abd722c17c2225.png" alt="4a_{20}= 5a_{10} \to 4(1- v^{20})= 5(1- v^{10})" width="298" height="34">，令 <img class="fml" src="/formulas/637c6a8561fbb4.png" alt="x= v^{10}" width="64" height="34">：<img class="fml" src="/formulas/1ae0ed73362ceb.png" alt="4x^{2}- 5x+1= 0 \to x= \frac{1}{4}" width="210" height="34">（x=1 舍去）→ <img class="fml" src="/formulas/4904ed920bf4e7.png" alt="v^{10}= 0.25" width="85" height="34">，<img class="fml" src="/formulas/25af19bc357aa5.png" alt="i= 0.25^{- \frac{1}{10}}- 1= 14.87" width="188" height="34">%。翻番：<img class="fml" src="/formulas/e11d043fe8118c.png" alt="(1+i)^{n}= 2" width="99" height="34"> **n = 5**。

</div>
<div class="kb-example">

**例 9**：永续年金由 A、B、C、D 分享，A 得前 n 次、B 得第 2 个 n 次、C 得第 3 个 n 次、D 得之后全部。已知 PV_C : PV_D = 1，求 PV_B : PV_D。
解：<img class="fml" src="/formulas/88077f430f7c4a.png" alt="PV_{C}= v^{2n} \cdot a_{n}" width="121" height="34">，<img class="fml" src="/formulas/0e6acabca05b74.png" alt="PV_{D}= \dfrac{v^{3n}}{i}" width="95" height="48">。由 <img class="fml" src="/formulas/224d2cb3ee6de7.png" alt="PV_{C}=PV_{D}" width="102" height="33"> 即 <img class="fml" src="/formulas/6cb887600507f3.png" alt="v^{2n}\cdot\dfrac{1- v^{n}}{i}= \dfrac{v^{3n}}{i}" width="149" height="48"> 得 <img class="fml" src="/formulas/1da7a0e6f67d5c.png" alt="1- v^{n}= v^{n}" width="97" height="33">，解得 <img class="fml" src="/formulas/5c7c647e71a7f1.png" alt="v^{n}= 0.5" width="71" height="34">。<img class="fml" src="/formulas/3f37b045cd962d.png" alt="PV_{B}:PV_{D}= \dfrac{v^{n}a_{n}}{\frac{v^{3n}}{i}}= \dfrac{(1- v^{n})v^{n}}{v^{3n}}= \dfrac{1- v^{n}}{v^{2n}}= \dfrac{1- v^{n}}{(v^{n})^{2}}=2" width="450" height="55">（代入 <img class="fml" src="/formulas/507d1b21a0ddba.png" alt="v^{n}=0.5" width="71" height="34"> 得 <img class="fml" src="/formulas/73b1d8f59cde8a.png" alt="0.5/0.25=2" width="103" height="33">）。

</div>
### 2.2 年金终值（★★★）

> <img class="fml" src="/formulas/de9d800c054f86.png" alt="s_{n}= a_{n}(1+i)^{n}= \frac{(1+i)^{n}- 1}{i}" width="205" height="34">（期末付）
> <img class="fml" src="/formulas/da41a0a86a7d06.png" alt="\ddot{s}_{n}= s_{n}(1+i)= \frac{(1+i)^{n}- 1}{d}" width="195" height="34">（期初付）= <img class="fml" src="/formulas/096449c497aa47.png" alt="s_{(n+1)}- 1" width="80" height="34">

永续年金**没有终值**（发散）。

**恒等式 <img class="fml" src="/formulas/b832f67f518b70.png" alt="(1+i)^{n}=1+i\cdot s_{n}" width="157" height="34">** 的解释：期初 1 元的终值 = 每期利息的终值 + 期末收回的本金。

<div class="kb-example">

**例 10**：前 5 年每年末存 2 万，后 5 年每年末存 4 万，i = 5%，求第 10 年末累积值。
解：拆成「2 万的 10 年年金 + 2 万的延期 5 年 5 年年金」：<img class="fml" src="/formulas/1b3dfb1dd35c57.png" alt="2s_{10}+ 2s_{5}= 2 \times 12.5779+ 2 \times 5.5256=36.21\,\text{万元}" width="402" height="34">。

</div>
<div class="kb-example">

**例 11**：每年初存 1000 元共 20 年，单利 i 计息时第 20 年末累积 28 400 元；求按同利率复利计息的累积值。
解：单利累积值 <img class="fml" src="/formulas/87d34e57c7db3f.png" alt="=1000\left[20+i(1+2+\cdots+20)\right]=20000+210000i=28400\to i=4\%" width="556" height="34">。
复利：<img class="fml" src="/formulas/94f69d6cf977b3.png" alt="1000\cdot\ddot{s}_{20}=1000\times\frac{1.04^{20}-1}{0.04}\times 1.04=30\,970\,\text{元}" width="357" height="34">。

</div>
### 2.3 现值与终值的关系（★★）

| 关系 | 公式 |
| --- | --- |
| 终值 = 现值累积 n 期 | <img class="fml" src="/formulas/a4d2880df318c9.png" alt="s_{n}= a_{n}(1+i)^{n}" width="125" height="34">；<img class="fml" src="/formulas/d7a4e998b8586f.png" alt="a_{n}= s_{n}(1+i)^{-n}" width="134" height="34"> |
| 倒数关系（期末付） | <img class="fml" src="/formulas/34513675239656.png" alt="\frac{1}{a_{n}}= \frac{1}{s_{n}}+ i" width="92" height="35"> |
| 倒数关系（期初付） | <img class="fml" src="/formulas/925b936c0da1c0.png" alt="\frac{1}{\ddot{a}_{n}}= \frac{1}{\ddot{s}_{n}}+ d" width="96" height="35"> |

倒数关系的记忆：<img class="fml" src="/formulas/8fe2a351b411f9.png" alt="\frac{1}{a_{n}}- \frac{1}{s_{n}}= i" width="92" height="35">，即「现值倒数减终值倒数等于利率」。

### 2.4 年金在任意时点上的值（★★★）

三种情形，**无需新公式**，全靠拆解：

1. **支付期开始前**（延期年金）：m|<img class="fml" src="/formulas/14a3b9946af0f0.png" alt="a_{n}= v^{m} \cdot a_{n}= a_{(m+n)}- a_{m}" width="216" height="34">；期初付：m|<img class="fml" src="/formulas/b36f9c1478a9f2.png" alt="\ddot{a}_{n}= v^{m} \cdot \ddot{a}_{n}" width="100" height="34">；延期永续：m|<img class="fml" src="/formulas/2b344757a959b7.png" alt="a_{\infty}= \frac{v^{m}}{i}" width="73" height="34">
   - m 可以为**任意正实数**（非整数延期照样用 vᵐ）
2. **支付期限内任意时点 t**：拆成「前段付款的终值 + 后段付款的现值」
3. **支付期结束后任意时点**：先求终值再往后累积

<div class="kb-example">

**例 12**：贷款年利率 8%，前 10 年不还，第 11–20 年每年末还 2000 元，求本金。
解：<img class="fml" src="/formulas/c56b4357d74f35.png" alt="2000 \cdot_{10}" width="61" height="34">|<img class="fml" src="/formulas/5f67b5cdfa8644.png" alt="a_{10}= 2000 \times v^{10} \times a_{10}= 2000 \times 0.46319 \times 6.7101=6216\,\text{元}" width="470" height="34">；
或 <img class="fml" src="/formulas/dc36a8963d670e.png" alt="2000 \times(a_{20}- a_{10})= 2000 \times(9.8181- 6.7101)=6216\,\text{元}" width="443" height="34">。

</div>
<div class="kb-example">

**例 13**：贷款年利率 6%，每年末还 20 000 元共 10 年，求第 5 年零 3 个月末一次付清的金额。
解：<img class="fml" src="/formulas/15dfe3fe28eaaa.png" alt="20000 \times(s_{5}+a_{5}) \times 1.06^0.25= 20000 \times(5.6371+4.2124) \times 1.0147=199\,880\,\text{元}" width="622" height="34">。

</div>
### 2.5 每年支付 m 次的等额年金（★★★）

设每年总付款额为 1，分 m 次支付（每次 1/m）。**核心结论：付款时间提前 ⟹ 价值上升为 <img class="fml" src="/formulas/329c314d7f4583.png" alt="\frac{i}{i^{(m)}}" width="31" height="34"> 倍**：

| 类型 | 现值 | 终值 |
| --- | --- | --- |
| 期末付 m 次 | <img class="fml" src="/formulas/c065e52a12bffa.png" alt="a_{n}^{(m)}= \frac{1- v^{n}}{i^{(m)}}=\left(\frac{i}{i^{(m)}}\right) \cdot a_{n}" width="190" height="34"> | <img class="fml" src="/formulas/2c417d3c096e92.png" alt="s_{n}^{(m)}= \frac{(1+i)^{n}- 1}{i^{(m)}}=\left(\frac{i}{i^{(m)}}\right) \cdot s_{n}" width="212" height="34"> |
| 期初付 m 次 | <img class="fml" src="/formulas/f54160b061069b.png" alt="\ddot{a}_{n}^{(m)}= \frac{1- v^{n}}{d^{(m)}}=\left(\frac{i}{d^{(m)}}\right) \cdot a_{n}" width="192" height="34"> | <img class="fml" src="/formulas/391132d5a173fd.png" alt="\ddot{s}_{n}^{(m)}= \frac{(1+i)^{n}- 1}{d^{(m)}}=\left(\frac{i}{d^{(m)}}\right) \cdot s_{n}" width="213" height="34"> |
| 永续 | <img class="fml" src="/formulas/2afde353acb9f8.png" alt="a_{\infty}^{(m)}= \frac{1}{i^{(m)}}\;;\quad \ddot{a}_{\infty}^{(m)}= \frac{1}{d^{(m)}}" width="198" height="34"> | — |



<p class="fml-block"><img class="fml" src="/formulas/253a5a85ae0316.png" alt="\ddot{a}_{n}^{(m)}=(1+i)^{\frac{1}{m}} \cdot a_{n}^{(m)}" width="170" height="34"></p>



- **注意**：公式假设「每年付款总额为 1」；若每次付 X 元、每年 m 次，则年总额为 mX，现值 = <img class="fml" src="/formulas/2f6a31ad400e9d.png" alt="mX \cdot a_{n}^{(m)}" width="83" height="34">
- 期末付年金分 m 次支付后价值上升（付款提前）；期初付分 m 次后价值**下降**为 <img class="fml" src="/formulas/18ca0eaca1ce54.png" alt="\frac{i}{d^{(m)}}" width="33" height="34"> 倍相对期末——方向别搞反

<div class="kb-example">

**例 14**：50 万贷款 5 年内按月等额偿还，年实际利率 6%，求每月还款额。
解：月实际利率 <img class="fml" src="/formulas/67f97b1cfc6571.png" alt="j= 1.06^{\frac{1}{12}}- 1= 0.004868" width="207" height="34">；<img class="fml" src="/formulas/e96c64793728bc.png" alt="500000= X \cdot a_{60|j} \to X" width="190" height="34"> = **9629.62 元**。
（用 <img class="fml" src="/formulas/3680c486317a86.png" alt="a_{n}^{(m)}" width="38" height="34"> 公式：<img class="fml" src="/formulas/3e5291738af232.png" alt="500000= 12X \cdot a_{5}^{(12)}" width="164" height="34">，结果相同。）

</div>
<div class="kb-example">

**例 15**：每月初存 1000 元，年实际利率 5%，求 5 年末累积值。
解：<img class="fml" src="/formulas/edc21cc56fbe07.png" alt="12000 \cdot \ddot{s}_{5}^{(12)}= 12000 \times\left(\frac{i}{d^{(12)}}\right) \times s_{5}= 12000 \times\left(\dfrac{0.05}{0.04869}\right) \times 5.5256\approx 68\,090\,\text{元}" width="611" height="52">。

</div>
### 2.6 连续支付的等额年金（★★★）

每年付款总额为 1、连续支付（<img class="fml" src="/formulas/50cbe589d0796e.png" alt="m\to\infty,\; i^{(m)}\to\delta" width="146" height="34">）：



<p class="fml-block"><img class="fml" src="/formulas/06a37feb35aec9.png" alt="\begin{aligned}
\bar{a}_{n}&amp;=\frac{1-v^{n}}{\delta}=\frac{i}{\delta}\,a_{n},\\[4pt]
\bar{s}_{n}&amp;=\frac{(1+i)^{n}-1}{\delta}=\frac{i}{\delta}\,s_{n},\\[4pt]
\bar{a}_{\infty}&amp;=\frac{1}{\delta}.
\end{aligned}" width="209" height="132"></p>



积分推导：时刻 <img class="fml" src="/formulas/6e57d6c47d2302.png" alt="t" width="13" height="34"> 付 <img class="fml" src="/formulas/1024d5c8aec780.png" alt="\mathrm{d}t" width="24" height="34"> 元，现值为



<p class="fml-block"><img class="fml" src="/formulas/d32c90a47da914.png" alt="\int_{0}^{n} v^{t}\,\mathrm{d}t=\frac{1-v^{n}}{\delta}" width="121" height="34"></p>



**支付频率与价值**：每年付款总额不变时，支付次数越多——期末付年金现值**越大**（平均付款时间提前）；期初付年金现值**越小**（平均付款时间推迟）；两者都收敛到连续年金。

<div class="kb-example">

**例 16**：i = 10%，每年支付 1 元的 20 年期年金现值随支付频率变化：
每年 1 次 8.5136 → 每季 8.8265 → 每月 8.8971 → 每天 8.9313 → 连续 8.9325（= <img class="fml" src="/formulas/25208aa372c64c.png" alt="\frac{a_{20} \times i}{\delta}= \frac{8.5136 \times 0.1}{\ln 1.1}" width="130" height="34">）。

</div>
<div class="kb-example">

**例 17**：年实际贴现率 5%，第 5 年末到第 7 年末之间每年连续支付 1000 元，求第 2 年末的现值。
解：<img class="fml" src="/formulas/b936eb0ed72766.png" alt="d= 0.05 \to v= 0.95" width="165" height="34">，<img class="fml" src="/formulas/1742dd4b043bc7.png" alt="\delta=- \ln 0.95" width="105" height="34">。现值 = <img class="fml" src="/formulas/b489aab0fb98e2.png" alt="1000 \cdot \bar{a}_{2} \cdot v^{3}= \frac{1000 \times(1- 0.95^{2})}{(- \ln 0.95) \times 0.95^{3}}=1629.73\,\text{元}" width="326" height="38">。

</div>
### 2.7 价值方程及其应用（★★★ 方法论）

**价值方程**（equation of value）：基于「现金流入现值 = 现金流出现值」建立的方程。年金问题三变量——现值/终值、支付次数 n、利率 i——知二求一。

- 求 n：解析解 <img class="fml" src="/formulas/df2299f65ce15e.png" alt="n= \dfrac{\ln[\cdots]}{\ln(1+i)}" width="111" height="51">，结果常非整数 → 处理「最后一次非正规付款」：
  - 提前到前一期末付：金额最小
  - 按理论时间（非整数）付：居中
  - 推迟到下一期末付：金额最大
- 求 i：高次方程无解析解，用 EXCEL RATE 函数 / 单变量求解 / 插值法
- EXCEL 对照：PV、FV、PMT、RATE、NPER；IRR/XIRR、NPV/XNPV

<div class="kb-example">

**例 18**：20 万元存基金，每年末领 1 万，年收益率 4.5%，能领多久？
解：<img class="fml" src="/formulas/d05af8cc3b8745.png" alt="20= 1 \times a_{n} \to(1.045)^{-n}= 0.1 \to n= 52.31" width="347" height="34"> 年。前 52 年每年领 1 万 + 第 53 年领小额 W：
- 第 53 年内第 114 天领：W = **3067 元**；提前到第 52 年末：X = **3025 元**；推迟到第 53 年末：Y = **3161 元**
- 若收益率 ≥ 5%，可无限期领取（<img class="fml" src="/formulas/fe0bf4dcdf10a5.png" alt="\frac{1}{0.05}=20" width="75" height="34"> 万正好是永续年金现值）

</div>
### 2.8 易错点

- <img class="fml" src="/formulas/1c6cb586f29f57.png" alt="a_{n}" width="25" height="34"> 与 än 差一个 (1+i) 因子；sn 与 s̈n 同理——先判断期初还是期末付。
- <img class="fml" src="/formulas/3680c486317a86.png" alt="a_{n}^{(m)}" width="38" height="34"> 公式中「每年总付款 = 1」的隐含假设，代入实际金额时别忘乘 m。
- 永续年金没有终值；延期非整数期照样用 vᵐ。
- 倒数关系 <img class="fml" src="/formulas/34513675239656.png" alt="\frac{1}{a_{n}}= \frac{1}{s_{n}}+ i" width="92" height="35"> 中是 **+i**（期末付）；期初付是 **+d**。
- 计算任意时点价值时，先画现金流图再拆分，不要硬套公式。

---

## 第3章 变额年金

变额年金 = 付款金额有规律变化的年金。两大类：**离散变额**（算术级数递增/递减、几何级数复递增）与**连续变额**。核心方法：**任何变额年金都可以拆成「等额年金 ± 标准变额年金」的组合**。

### 3.1 递增年金（★★★）

**期末付标准递增年金** <img class="fml" src="/formulas/29351adc4197f8.png" alt="(Ia)_{n}" width="47" height="33">：第 1 期末付 1、第 2 期末付 2、…、第 n 期末付 n：



<p class="fml-block"><img class="fml" src="/formulas/e91c80ba9f1eb9.png" alt="(Ia)_{n}= \frac{\ddot{a}_{n}- nv^{n}}{i}" width="118" height="33"></p>



证明：现值和 = <img class="fml" src="/formulas/44cc8249ee98d6.png" alt="v+2v^{2}+ \cdots+nv^{n}" width="157" height="33">，乘 (1+i) 错位相减 → <img class="fml" src="/formulas/b9b4e3f5f1203e.png" alt="i(Ia)_{n}= \ddot{a}_{n}- nv^{n}" width="146" height="33">。
分解视角：<img class="fml" src="/formulas/6d48c7ce5ee3fd.png" alt="(Ia)_{n}= a_{n}+ v \cdot a_{(n-1)}+ v^{2}a_{(n-2)}+ \cdots+ v^{n-1}a_{1}" width="374" height="33">（n 个延期等额年金之和）。

**终值**：<img class="fml" src="/formulas/9a1e7d3a959c8f.png" alt="(Is)_{n}=(1+i)^{n}(Ia)_{n}= \frac{\ddot{s}_{n}- n}{i}" width="228" height="33">

**期初付**：<img class="fml" src="/formulas/9178e1e07eb45c.png" alt="(I\ddot{a})_{n}=(1+i)(Ia)_{n}= \frac{\ddot{a}_{n}- nv^{n}}{d}" width="234" height="33">；<img class="fml" src="/formulas/51fb9927105f49.png" alt="(I\ddot{s})_{n}= \frac{\ddot{s}_{n}- n}{d}" width="105" height="33">

**递增永续年金**（对 <img class="fml" src="/formulas/057115dad200cf.png" alt="\frac{\ddot{a}_{n}- nv^{n}}{i}" width="54" height="33"> 取极限，<img class="fml" src="/formulas/771842c34e730d.png" alt="nv^{n} \to 0" width="72" height="33">）：



<p class="fml-block"><img class="fml" src="/formulas/1420ee5c6bc5cc.png" alt="\begin{aligned}
(Ia)_{\infty}&amp;=\frac{\ddot{a}_{\infty}}{i}=\frac{1+i}{i^{2}}=\frac{1}{id},\\[4pt]
(I\ddot{a})_{\infty}&amp;=(1+i)(Ia)_{\infty}=\frac{(1+i)^{2}}{i^{2}}=\frac{1}{d^{2}}.
\end{aligned}" width="309" height="90"></p>



**通用递增年金拆解模板**（教材例 3-1 模式，考试最常考）：
第 1 期付 P、每期递增 Q 的 n 期年金 = **P′ 元等额年金 + Q 元标准递增年金**，其中 P′ = <img class="fml" src="/formulas/64d990aa67ec8f.png" alt="P- Q" width="57" height="33">：
现值 = <img class="fml" src="/formulas/286f2bad71f30f.png" alt="(P- Q) \cdot a_{n}+ Q \cdot(Ia)_{n}" width="191" height="33">

<div class="kb-example">

**例 19**：20 年期年金第 1 年末付 650、以后每年递增 50（末次 1600），i = 6%，求现值。
解：拆成 600 元等额年金 + 50 元标准递增年金：
<img class="fml" src="/formulas/5945736bad89e3.png" alt="600a_{20}+ 50(Ia)_{20}= 600 \times 11.4699+ \frac{50 \times(\ddot{a}_{20}- 20v^{20})}{0.06}" width="386" height="35">，其中 <img class="fml" src="/formulas/addb4c65671b5c.png" alt="\ddot{a}_{20}= 12.1581" width="113" height="33">、<img class="fml" src="/formulas/9cc2459d451b04.png" alt="v^{20}= 0.3118" width="103" height="33">：
= <img class="fml" src="/formulas/92884fa4a04791.png" alt="6882+ \frac{50 \times(12.1581- 6.236)}{0.06}= 6882+ 50 \times 98.70= 6882+ 4935=11\,817\,\text{元}" width="550" height="33">（教材例 3-1 值）。

</div>
<div class="kb-example">

**例 20**：递增年金第 1 年末付 300、每次递增 20、末次 600，i = 5%，求最后支付时点的终值。
解：次数 <img class="fml" src="/formulas/e8d95b9bc8a061.png" alt="n= \frac{600- 300}{20}+1= 16" width="166" height="33">。拆成 280 元等额 + 20 元递增：


<p class="fml-block"><img class="fml" src="/formulas/8330a100ba3175.png" alt="280s_{16}+ 20(Is)_{16}= 280 \times 23.6575+ \frac{20 \times(\ddot{s}_{16}- 16)}{0.05}= 6624.10+ 20 \times 176.81=10\,160.26\,\text{元}" width="675" height="34"></p>



</div>
### 3.2 递减年金（★★★）

**期末付标准递减年金** <img class="fml" src="/formulas/ad8e60f904495f.png" alt="(Da)_{n}" width="54" height="34">：第 1 期末付 n、第 2 期末付 n−1、…、第 n 期末付 1：



<p class="fml-block"><img class="fml" src="/formulas/3056675bec3382.png" alt="(Da)_{n}= \frac{n- a_{n}}{i}" width="112" height="34"></p>



证明一：递增 + 递减 = 每期 (n+1) 的等额年金 → <img class="fml" src="/formulas/4b5c7ced40d181.png" alt="(Da)_{n}=(n+1)a_{n}-(Ia)_{n}" width="213" height="34">。
证明二：分解成 n 个不同期限的等额年金之和。

- 终值：<img class="fml" src="/formulas/cffc8282b6b109.png" alt="(Ds)_{n}=(1+i)^{n}(Da)_{n}= \frac{n(1+i)^{n}- s_{n}}{i}" width="276" height="34">
- 期初付：<img class="fml" src="/formulas/23492e7a6ab6f4.png" alt="(D\ddot{a})_{n}=(1+i)(Da)_{n}= \frac{n- a_{n}}{d}" width="234" height="34">；<img class="fml" src="/formulas/0af190de99270e.png" alt="(D\ddot{s})_{n}= \frac{n(1+i)^{n}- s_{n}}{d}" width="146" height="34">

<div class="kb-example">

**例 21**：10 年期递减年金第 1 年初付 100、以后每年减 10（第 10 年初付 10），i = 6%，求第 10 年末终值。
解：<img class="fml" src="/formulas/e1ab8968221dcc.png" alt="10 \times(D\ddot{s})_{10}= \dfrac{10 \times[10 \times 1.06^{10}- s_{10}]}{d}= \dfrac{10 \times(17.9085- 13.1808)}{0.0566}=835.22\,\text{元}" width="618" height="48">。

**山形年金**（先增后减，<img class="fml" src="/formulas/5fa9fbb7dbae45.png" alt="1,2, \cdots,n,n- 1,...,1" width="175" height="34"> 共 <img class="fml" src="/formulas/b648de892ffc4a.png" alt="2n- 1" width="58" height="34"> 期）：现值 = <img class="fml" src="/formulas/aacc79568b9e1c.png" alt="(Ia)_{n}+ v^{n}(Da)_{(n-1)}= a_{n}\cdot \ddot{a}_{n}" width="233" height="34">（教材例 3-7 优美结论，证明题考点）。

</div>
### 3.3 复递增年金（★★★）

付款按**几何级数**增长：第 1 期末付 1，以后每年按 r 增长（第 t 期末付 <img class="fml" src="/formulas/21b58449daa73c.png" alt="(1+r)^{t-1}" width="82" height="34">）。

**期末付复递增年金现值**：

> **<img class="fml" src="/formulas/182ce759bc60b9.png" alt="(Ca)_{n}=\dfrac{1-(1+j)^{-n}}{(1+r)\,j}" width="183" height="52">，其中 <img class="fml" src="/formulas/71b2e73d4b2f1f.png" alt="j=\dfrac{i-r}{1+r}" width="82" height="47">（净利率）**

- 推导：每笔现金流除以 <img class="fml" src="/formulas/d987c9b96092e1.png" alt="(1+i)^{t}" width="63" height="33"> 后成为按 j 贴现的等额年金；(1+r)v = 1/(1+j)
- **<img class="fml" src="/formulas/54d38100a03a6a.png" alt="r=i" width="46" height="34"> 时：<img class="fml" src="/formulas/9f9647fe743550.png" alt="(Ca)_{n}=\dfrac{n}{1+i}" width="118" height="43">**（每笔现值都是 <img class="fml" src="/formulas/d1fb8ffd72883b.png" alt="\dfrac{1}{1+i}" width="48" height="47">）
- 期初付：<img class="fml" src="/formulas/b3c0c5982d7420.png" alt="(C\ddot{a})_{n}=(1+i)(Ca)_{n}= \dfrac{(1+i)\left[1-(1+j)^{-n}\right]}{(1+r)j}" width="367" height="52">
- **复递增永续年金存在条件：i > r**，此时 <img class="fml" src="/formulas/cf65d426b4168e.png" alt="(Ca)_{\infty}= \frac{1}{i- r}" width="106" height="34">（由公式取极限）；期初付 <img class="fml" src="/formulas/1ee42a4dd10896.png" alt="(C\ddot{a})_{\infty}= \frac{1+i}{i- r}" width="106" height="34">

<div class="kb-example">

**例 22**：10 年期期末付年金第 1 年末付 1000、每年增长 5%，i = 11.3%，求现值。
解：<img class="fml" src="/formulas/c06109cae55e41.png" alt="j= \frac{0.113- 0.05}{1.05}= 0.06" width="159" height="34">。<img class="fml" src="/formulas/6ab738d6bbe24b.png" alt="PV= \frac{1000 \times[1- 1.06^{-10}]}{1.05 \times 0.06}= \frac{1000 \times 7.3601}{1.05}=7009.61\,\text{元}" width="361" height="36">。

</div>
<div class="kb-example">

**例 23**：永续年金从第 2 年末开始首次支付 5000、每年增长 5%，i = 8%，求现值。
解：增长永续在首次支付前一期（第 1 年末）的价值 <img class="fml" src="/formulas/53676d1cd265e8.png" alt="= \dfrac{5000}{0.08- 0.05}= 166 667" width="192" height="46">，再贴现 1 期得 <img class="fml" src="/formulas/93aca732b3152c.png" alt="PV=166667\times 1.08^{-1}=154\,321\,\text{元}" width="285" height="34">；若首次支付在第 3 年末（教材原题口径），则需贴现 2 期：<img class="fml" src="/formulas/9199c97621a808.png" alt="PV=166667\times 1.08^{-2}=142\,890\,\text{元}" width="284" height="34">（教材 142 889.8）。

</div>
### 3.4 每年支付 m 次的变额年金（★★）

与等额年金同样的放大规律：

- 每年 m 次期末付变额年金 = **<img class="fml" src="/formulas/720be72297ba0f.png" alt="\frac{i}{i^{(m)}}\times" width="45" height="34"> 每年 1 次期末付变额年金**
- 每年 m 次期初付变额年金 = **<img class="fml" src="/formulas/f63973a7f3f1b5.png" alt="\frac{i}{d^{(m)}}\times" width="47" height="34"> 每年 1 次期初付变额年金**
- 连续支付变额年金 = **(i/δ) × 每年 1 次期末付变额年金**

即 <img class="fml" src="/formulas/d194c18cb73dbf.png" alt="(Ia)_{n}^{(m)}=\left(\frac{i}{i^{(m)}}\right)(Ia)_{n}" width="170" height="34">、<img class="fml" src="/formulas/33dd5d1717890c.png" alt="(Da)_{n}^{(m)}=\left(\frac{i}{i^{(m)}}\right)(Da)_{n}" width="182" height="34">、<img class="fml" src="/formulas/e92c06124954af.png" alt="(Ca)_{n}^{(m)}=\left(\frac{i}{i^{(m)}}\right)(Ca)_{n}" width="179" height="34">，期初付把 <img class="fml" src="/formulas/fab53528f38d07.png" alt="i^{(m)}" width="35" height="33"> 换成 <img class="fml" src="/formulas/12e414056d789a.png" alt="d^{(m)}" width="37" height="33">；连续支付（上划线）把系数换成 i/δ：
<img class="fml" src="/formulas/3af689380bf8ee.png" alt="(I\bar{a})_{n}= \frac{\bar{a}_{n}- nv^{n}}{\delta}" width="119" height="34">、<img class="fml" src="/formulas/85088af6696e2b.png" alt="(D\bar{a})_{n}= \frac{n- \bar{a}_{n}}{\delta}" width="112" height="34">、<img class="fml" src="/formulas/9ddad928145e65.png" alt="(C\bar{a})_{n}=\left(\frac{i}{\delta}\right)(Ca)_{n}" width="152" height="34">。

<div class="kb-example">

**例 24**：第 1 年每月末付 2000、第 2 年每月末付 2100、…、第 10 年每月末付 2900，i = 5%，求现值。
解：每年付款总额 = <img class="fml" src="/formulas/29fe55bb6d4d45.png" alt="12 \times(1900+100t)" width="151" height="34">，拆成「<img class="fml" src="/formulas/e1f9717ab3850a.png" alt="1900 \times 12" width="82" height="34"> 元等额 + <img class="fml" src="/formulas/d34e8e3df04360.png" alt="100 \times 12" width="73" height="34"> 元递增」，再乘 m 次支付放大因子 <img class="fml" src="/formulas/cb721a924d5adb.png" alt="\frac{i}{i^{(12)}}= \frac{0.05}{0.04889}= 1.0227" width="175" height="34">：


<p class="fml-block"><img class="fml" src="/formulas/63b3b10b9f1adb.png" alt="PV= 1.0227 \times[22800 \times a_{10}+ 1200 \times(Ia)_{10}]= 1.0227 \times[22800 \times 7.7217+ 1200 \times 39.375]=228\,373\,\text{元}" width="806" height="34"></p>



（教材例 3-12）。

</div>
### 3.5 连续变化现金流（★★ 压轴计算）

注意区分两类符号（横线位置不同，含义完全不同）：

**（一）连续支付的变额年金**（每年付款额离散变化、年内连续支付，只有 a 上有横线）——由 3.4 的极限规律「连续 = 每年 1 次 × <img class="fml" src="/formulas/572ce4e7352430.png" alt="\frac{i}{\delta}" width="17" height="34">」直接得到：

> <img class="fml" src="/formulas/22aef2f1147610.png" alt="(I\bar{a})_{n}=\left(\frac{i}{\delta}\right)(Ia)_{n}= \frac{\ddot{a}_{n}- nv^{n}}{\delta}" width="214" height="34">（第 1 年连续付 1、第 2 年连续付 2、…）
> <img class="fml" src="/formulas/19b13f84b7377d.png" alt="(D\bar{a})_{n}=\left(\frac{i}{\delta}\right)(Da)_{n}= \frac{n- a_{n}}{\delta}" width="212" height="34">（第 1 年连续付 n、…、第 n 年连续付 1）
> <img class="fml" src="/formulas/9ddad928145e65.png" alt="(C\bar{a})_{n}=\left(\frac{i}{\delta}\right)(Ca)_{n}" width="152" height="34">；连续支付递增永续：<img class="fml" src="/formulas/04648657d6010f.png" alt="(I\bar{a})_{\infty}=\left(\frac{i}{\delta}\right)(Ia)_{\infty}= \frac{1+i}{i\delta}= \frac{\ddot{a}_{\infty}}{\delta}" width="245" height="34">

**（二）连续递增/递减年金**（付款**率**也随时间连续变化，I、a 上都有横线）——积分求得：

> <img class="fml" src="/formulas/8c08abaebffaca.png" alt="(\bar{I}\bar{a})_{n}" width="48" height="34">（时刻 t 付款率为 t）：= <img class="fml" src="/formulas/571dbc3de2c41b.png" alt="\int_{0}^{n} t \cdot e^{- \delta t}dt" width="95" height="34"> <img class="fml" src="/formulas/2fe24e7c5acf7e.png" alt="\frac{\bar{a}_{n}- nv^{n}}{\delta}" width="54" height="34">
> <img class="fml" src="/formulas/e8f4640f86bdd8.png" alt="(\bar{I}\bar{s})_{n}" width="47" height="34"> = <img class="fml" src="/formulas/c6ecebb64d5cbe.png" alt="\dfrac{(1+i)^{n}- 1- n\delta}{\delta^{2}}" width="142" height="47">（现值累积 n 年）
> **连续递增永续：(Īā)∞ = 1/δ²**
> <img class="fml" src="/formulas/2c488522e64895.png" alt="(\bar{D}\bar{a})_{n}" width="54" height="34">（时刻 t 付款率为 n−t）：= <img class="fml" src="/formulas/c0be81726e042b.png" alt="n \cdot \bar{a}_{n}-(\bar{I}\bar{a})_{n}" width="111" height="34"> <img class="fml" src="/formulas/5b96fd12986900.png" alt="n \cdot \bar{a}_{n}- \frac{\bar{a}_{n}- nv^{n}}{\delta}" width="118" height="34">

**一般连续现金流**（付款期 [a,b]，付款率 p(t)，利息力 <img class="fml" src="/formulas/b9a1240560ebce.png" alt="\delta(t)" width="36" height="33">）——终极公式：



<p class="fml-block"><img class="fml" src="/formulas/6a1989a669f296.png" alt="PV_{0}= \int_{a}^{b} p(t) \cdot \exp[- \int_{0}^{t} \delta(s)ds] \cdot dt" width="277" height="34"></p>





<p class="fml-block"><img class="fml" src="/formulas/2aeacaaee6c3e1.png" alt="FV_{c}= \int_{a}^{b} p(t) \cdot \exp[ \int_{t}^{c} \delta(s)ds] \cdot dt" width="260" height="34"></p>



<div class="kb-example">

**例 25**：付款期 [0, 0.5]，<img class="fml" src="/formulas/da11c7bba711ef.png" alt="p(t) = 10t+3" width="115" height="33">，<img class="fml" src="/formulas/b9a1240560ebce.png" alt="\delta(t)" width="36" height="33">，求现值。
解：<img class="fml" src="/formulas/84730a425aab2e.png" alt="\int_{0}^0.5(10t+3)e^{- 0.1t^{2}- 0.06t}dt" width="209" height="33">。令 <img class="fml" src="/formulas/436084c4848864.png" alt="u=- 0.1t^{2}- 0.06t" width="151" height="33">，则 <img class="fml" src="/formulas/aef2524ad16690.png" alt="du=-(0.2t+0.06)dt=- 2(0.1t+0.03)dt" width="336" height="33">，注意 10t+3 = 100(0.1t+0.03)：
<img class="fml" src="/formulas/4fe80eb72f9a2e.png" alt="PV=- 50 \int e^u du=- 50[e^{- 0.055}- 1]=2.68\,\text{元}" width="365" height="33">（教材例 3-22，凑微分是关键技巧）。

</div>
<div class="kb-example">

**例 26**：10 年期年金时刻 t 付款率 9t+6，<img class="fml" src="/formulas/b8eaecd8d26523.png" alt="\delta= 9" width="48" height="33">%，求现值。
解：<img class="fml" src="/formulas/e7bd80a7517dd3.png" alt="i= e^0.09- 1= 9.4174" width="179" height="33">%。付款率 9t 是连续递增部分、6 是连续等额部分：<img class="fml" src="/formulas/cf14452b8bcc9b.png" alt="PV= 9(\bar{I}\bar{a})_{10}+ 6\bar{a}_{10}" width="168" height="33">，其中 <img class="fml" src="/formulas/8835dd12e51cd6.png" alt="\bar{a}_{10}= \frac{1- 1.094174^{-10}}{0.09}= 6.5937" width="211" height="33">，<img class="fml" src="/formulas/a8155650bea5fa.png" alt="(\bar{I}\bar{a})_{10}= \frac{\bar{a}_{10}- 10v^{10}}{\delta}= \frac{6.5937- 10 \times 1.094174^{-10}}{0.09}= 28.0886" width="377" height="34">。<img class="fml" src="/formulas/03594749c9110e.png" alt="PV= 9 \times 28.0886+6 \times 6.5937=292.36\,\text{元}" width="345" height="33">。

</div>
### 3.6 易错点

- 递增年金 <img class="fml" src="/formulas/29351adc4197f8.png" alt="(Ia)_{n}" width="47" height="33"> 公式分子是 <img class="fml" src="/formulas/478fd402c52d44.png" alt="\ddot{a}_{n}" width="25" height="33">（期初付年金）不是 an——最常见的符号错误。
- 非标准递增（首期 P、递增 Q）先拆成 <img class="fml" src="/formulas/866724e08b046f.png" alt="(P- Q)" width="71" height="33"> 等额 + Q 标准递增，不要硬套。
- 复递增年金 <img class="fml" src="/formulas/d47d8fae925a65.png" alt="r = i" width="46" height="33">时公式退化为 n/(1+i)（分母 j = 0 不能用一般式）。
- 复递增**永续**年金只有 i > r 时现值才存在（收敛条件）。
- 连续支付符号上划线含义：a 上横线 = 连续支付；I 上横线 = 连续递增（付款率连续变化）；(Iā) 两者都有 = 连续支付且连续递增。
- 一般现金流积分时 <img class="fml" src="/formulas/b9a1240560ebce.png" alt="\delta(t)" width="36" height="33"> 分段函数要分段积分；变上限积分别丢负号。

---

## 第4章 收益率和收益分配

![收益率体系](/int/int-yield.svg)

### 4.1 收益率与净现值（★★★）

**收益率**（yield rate / 内部报酬率 IRR）：使**资金流入现值 = 资金流出现值**的利率；等价定义：使**净现值 NPV = 0** 的利率。

**净现值**：<img class="fml" src="/formulas/41d21c8db1286d.png" alt="NPV(i)= \sum R_{t}v^{t}" width="151" height="33">（Rt 为时刻 t 的净现金流，流入为正流出为负）。

- NPV 是利率的**减函数**（常规情况下）：利率越高 NPV 越小
- 决策规则：收益率 ≥ 投资者要求的最低收益率（≈ 筹资利率）⟹ 项目可行；NPV ≥ 0 ⟹ 可行
- 收益率法与净现值法结论一致

**多重收益率**：现金流符号改变多次时，NPV(i)=0 可能有多个解（如净流入 <img class="fml" src="/formulas/e6e87d6f6e085e.png" alt="- 10000,+21500,- 11550" width="198" height="33"> 有 5% 和 10% 两个收益率）。此时 NPV 不再是单调函数，收益率法与净现值法都失效 → 改用**修正收益率**。

**收益率唯一性两准则**（简答高频）：

1. **准则一**：资金净流入只改变过一次符号 → 收益率唯一
2. **准则二**：按该收益率计算的资金净流入累积值**始终为负、直到最后一期才为零** → 该收益率唯一（准则一失效时用）

**收益率不存在**：方程解为虚数时（如净流入 <img class="fml" src="/formulas/05b96bfbc2ba9b.png" alt="- 10000,+20000,- 11550" width="198" height="33">），只能画 NPV 曲线判断——若 NPV 恒 < 0 则放弃投资。

<div class="kb-example">

**例 27**：项目初始投资 3000 万，第 2 年初追加 1000 万，第 1 年末收入 2000 万、第 2 年末收入 4000 万，收益率形如 1/n，求 n。
解：<img class="fml" src="/formulas/0d9ba5e112f532.png" alt="- 3000+ 1000v+ 4000v^{2}= 0 \to 4v^{2}+v- 3= 0 \to v= \frac{3}{4}" width="450" height="33">（负根舍）→ <img class="fml" src="/formulas/b15c72736a4366.png" alt="1+i= \frac{4}{3}" width="78" height="33">，<img class="fml" src="/formulas/3521a7910b8aee.png" alt="i= \frac{1}{3}" width="47" height="34"> **n = 3**。

</div>
### 4.2 币值加权收益率（★★★ 计算高频）

**币值加权收益率**（dollar-weighted rate of return）= IRR，衡量**投资者个人**的实际收益（受本金增减时机影响）。

精确方程：<img class="fml" src="/formulas/5a0abeae5d9db4.png" alt="A_{0}(1+i)+ \sum C_{t}(1+i)^{1- t}= A_{1}" width="257" height="34">（Ct 为时刻 t 的新增投资，可为负）

**近似公式**（用单利近似不足一期的复利）：

> <img class="fml" src="/formulas/6116b3fdf671a9.png" alt="i \approx \frac{I}{A_{0}+ \sum C_{t}(1- t_{t})}" width="128" height="37">，其中 <img class="fml" src="/formulas/069f3f1e349637.png" alt="I= A_{1}-\left(A_{0}+ \sum C_{t}\right)" width="179" height="34"> 为当期利息收入

- 分母是**按计息时间加权的平均本金余额**
- 若再假设新增投资平均发生在期中（t=0.5）：<img class="fml" src="/formulas/c2c10b9d65d023.png" alt="i \approx \frac{2I}{A_{0}+A_{1}- I}" width="97" height="35">（更粗糙）

<div class="kb-example">

**例 28**：期初余额 100 万；4 月 1 日投入前余额 120 万…（教材例 4-4：期初 100，4/1 取出 20，9/1 存入 30，期末 120）
解：<img class="fml" src="/formulas/891b501288f6b3.png" alt="I= 120-(100- 20+30)= 10" width="250" height="34">。加权本金（30/360 规则）= <img class="fml" src="/formulas/8f8b95df1f2271.png" alt="100- 20 \times\left(\frac{8}{12}\right)+ 30 \times\left(\frac{4}{12}\right)= 96.67" width="287" height="34">。<img class="fml" src="/formulas/6da7689fcda4f9.png" alt="i \approx \dfrac{10}{96.67}=10.34\%" width="161" height="45">；精确解（XIRR，实际/365）= **10.547%**。

</div>
### 4.3 时间加权收益率（★★★ 概念辨析高频）

**时间加权收益率**（time-weighted rate of return）：扣除资金增减影响、在**本金恒定**基础上计算的收益率，衡量**基金经理**业绩。

做法：每次新增投资**前**对基金估值，把投资期切成 n+1 个子区间：

> <img class="fml" src="/formulas/74b804c4b75502.png" alt="1+ i=(1+j_{1})(1+j_{2}) \cdots(1+j_{n+1})" width="290" height="34">，<img class="fml" src="/formulas/5333b2173add42.png" alt="j_{k}= A_{k}" width="67" height="34">′<img class="fml" src="/formulas/91f388fa262ce1.png" alt="(A_{k-1}+C_{k-1})- 1" width="147" height="34">

**两法对比**（简答必考）：

| | 币值加权 | 时间加权 |
| --- | --- | --- |
| 衡量对象 | 投资者个人收益 | 基金经理业绩 |
| 受申赎时机影响 | 是 | 否 |
| 数据要求 | 只需期初期末 + 现金流 | 每次申赎前都要估值（成本高） |
| 低点加仓的投资者 | 收益率被拉高 | 不受影响 |

<div class="kb-example">

**例 29**（教材例 4-8 精髓）：A 基金 2013 年 <img class="fml" src="/formulas/b53f4cf8e4cc79.png" alt="1000 \to 2000" width="106" height="34"> 万（+100%），2014 年初新增 2 亿后 <img class="fml" src="/formulas/1f3655c3b3814b.png" alt="22000 \to 22000" width="124" height="34"> 万（0%）；两年时间加权 = <img class="fml" src="/formulas/152f304aca70ad.png" alt="\sqrt{2 \times 1}- 1=41.4\%" width="163" height="34">，但币值加权只有 **4.5%**（大资金恰好买在「不涨」的年份）。B 基金相反：时间加权 3.9% < 币值加权 15.6%。**结论：市场低迷时追加投资会拉低币值加权收益率；时间加权收益率才反映经理真实水平**。

</div>
### 4.4 再投资与修正收益率（★★★）

**再投资风险**：利息再投资利率 j ≠ 原投资利率 i 时，实际总收益被拉低（j < i 时）。

- 期初投 1 元、n 年、利率 i、利息按 j 再投资：终值 = <img class="fml" src="/formulas/f6c9a6c7abf5a1.png" alt="1+ i \cdot s_{n}|_{j}" width="85" height="34">；年平均收益率 z = (1+i·sn|j)^(1/n) − 1
- <img class="fml" src="/formulas/5311e2bc512618.png" alt="j = i" width="45" height="33">时退化为复利 <img class="fml" src="/formulas/37e2e689fa4962.png" alt="(1+i)^{n}" width="66" height="34">
- 每年末付 1 元的 n 年年金、利息按 j 再投资：终值 = <img class="fml" src="/formulas/0c860ef8369868.png" alt="n+ i(Is)_{(n-1)}|_{j}" width="123" height="34">（本金序列 n 元 + 利息构成递增年金）

**修正收益率 MIRR**（modified internal rate of return）：项目收入再投资利率 ≠ 筹资利率时使用（也用于多重收益率场景）：

> **(1+MIRR)ⁿ = 流入按再投资利率 j 计算的累积值 ÷ 流出按筹资利率计算的现值**

<div class="kb-example">

**例 30**：期初投 10 000，以后 3 年每年末收入 4000。IRR = 9.7%；若收入只能按 5% 再投资：<img class="fml" src="/formulas/f9ba6406af996a.png" alt="10000(1+MIRR)^{3}= 4000s_{3}|_{0.05}= 12 610=8.04\%" width="401" height="34">。（EXCEL：=MIRR({-10000,4000,4000,4000}, 0, 5%)）

</div>
<div class="kb-example">

**例 31**（债券比较）：债券 A 5 年期利率 8%、债券 B 8 年期利率 7%，均到期一次还本付息。A 到期后 3 年再投资利率需 > **5.354%** 才优于 B：<img class="fml" src="/formulas/e8f194711c1545.png" alt="(1.08)^{5}(1+i)^{3}=(1.07)^{8}" width="195" height="34">。**期限不同的项目比较必须考虑再投资利率**。

</div>
### 4.5 收益分配（★★ 概念）

多投资者共享基金收益的两种方法：

| 方法 | 规则 | 适用环境 |
| --- | --- | --- |
| **组合方法** | 所有投资者按基金**平均收益率**分配，不论投资早晚 | 利率平稳/**下降**期（平均收益率高于当前市场利率，吸引新投资者） |
| **投资年度方法** | 新增投资头几年按**投资年度利率**（与投入年份挂钩，对角线元素）分配；超过一定年数（如 5 年）后改按**组合利率** | 利率**上升**期（新资金拿到高利率，吸引新投资者） |

投资年度利率表读法：上标 = 投资发生年度，上标+下标 = 分配收益年度；组合利率 = 相应各投资年度利率的几何平均。

### 4.6 易错点

- 收益率 = IRR = 使 NPV=0 的利率，三个说法是一回事。
- 净现值 NPV 函数**不含**期初现金流、XNPV **必须含**期初现金流；IRR 对应规则现金流、XIRR 对应不规则日期。
- 多重收益率时**收益率法和净现值法都失效**，用 MIRR。
- 币值加权近似公式的分母是「加权平均本金」：期初本金权重 1，时刻 t 新增权重 <img class="fml" src="/formulas/0f419b7579cc32.png" alt="(1- t)" width="58" height="34">。
- 时间加权收益率必须**在每次新增投资发生前**估值，新增投资本身不参与子区间收益率计算。
- 比较期限不同的项目：短期限项目的再投资收益必须计入。

---

## 第5章 债务偿还方法

两种基本方法：**分期偿还法**（amortization，每期还款含利息+部分本金）与**偿债基金法**（sinking fund，每期只付利息+往基金存钱，到期基金还本）。

![债务偿还双轨制](/int/int-loan.svg)

### 5.1 等额分期偿还（★★★ 计算题主力）

贷款本金 L0、期限 n、利率 i、每年末等额偿还 R：

| 量 | 公式 |
| --- | --- |
| 每期偿还额 | <img class="fml" src="/formulas/5c47a4c314ff68.png" alt="R= \frac{L_{0}}{a_{n}}" width="63" height="35"> |
| 第 k 期利息 | <img class="fml" src="/formulas/59e28f49a77344.png" alt="I_{k}= iL_{k-1}= R(1- v^{n- k+1})" width="220" height="34">（逐期递减） |
| 第 k 期偿还本金 | <img class="fml" src="/formulas/4dd896723910fc.png" alt="P_{k}= R \cdot v^{n- k+1}" width="126" height="34">（等比递增，公比 1+i） |
| 第 k 期末本金余额（过去法） | <img class="fml" src="/formulas/4922cb01cfae6d.png" alt="L_{k}= L_{0}(1+i)^{k}- R \cdot s_{k}" width="194" height="34"> |
| 第 k 期末本金余额（将来法） | <img class="fml" src="/formulas/7f62d9882b51ca.png" alt="L_{k}= R \cdot a_{(n-k)}" width="121" height="34"> |

- **过去法 vs 将来法等价**；未来付款额和次数已知时用将来法简便，否则用过去法
- <img class="fml" src="/formulas/1355a46301c0fd.png" alt="P_{k+1}= P_{k}(1+i)" width="136" height="34">：每期偿还本金按 (1+i) 递增
- 利息总额 = <img class="fml" src="/formulas/90ba5db64be91f.png" alt="nR- L_{0}" width="72" height="34">；每 1 元还款额对应的「利息/本金比」= <img class="fml" src="/formulas/4d901c1cc5705c.png" alt="\frac{n- a_{n}}{a_{n}}" width="41" height="35">，是期限 n 的**增函数且加速增长**
- 贷款期限越长，利息总额相对本金越多（i=10% 时 <img class="fml" src="/formulas/d2b771a7ccf808.png" alt="n \approx 15.38" width="83" height="34"> 年利息总额恰好等于本金）

**分期偿还表**（构造题模板）：年份 | 还款额 R | 当年利息 <img class="fml" src="/formulas/722755e31be2b9.png" alt="iL_{k-1}" width="49" height="34"> | 偿还本金 R−利息 | 期末余额

<div class="kb-example">

**例 32**：10 万元贷款 5 年、i=6%、每年末等额偿还。<img class="fml" src="/formulas/2876727e15026b.png" alt="R= \frac{100000}{a_{5}}= \frac{100000 \times 0.06}{1- 1.06^{-5}}=23\,739.64\,\text{元}" width="298" height="35">。第 3 年：利息 = <img class="fml" src="/formulas/68e06265b6fb9e.png" alt="23739.64 \times(1- 1.06^{-3})= 3807.38" width="272" height="34">，本金 = 19 932.26，余额 <img class="fml" src="/formulas/c07fabbaf517cf.png" alt="L_{3}= R \cdot a_{2}=43\,524.08\,\text{元}" width="209" height="34">。

</div>
<div class="kb-example">

**例 33**（利率中途变化）：10 万元保险金按月领取 25 年，月利率由年实际 8% 换算；10 年后利率升到 10%，求每月可多领多少。
解：原月领 <img class="fml" src="/formulas/89d6395026b0e8.png" alt="R_{1}= \frac{100000}{a_{300}}|_{0.006434}= 753.42" width="219" height="35">；过去法算 10 年末余额 <img class="fml" src="/formulas/d30849ed0ad9c8.png" alt="L_{120}= 100000 \times 1.006434^{120}- 753.42 \times s_{120}= 80 183.27" width="438" height="34">；新月利率 0.007974，<img class="fml" src="/formulas/aafce805cbd2e4.png" alt="R_{2}= \frac{80183.27}{a_{180}}= 840.63" width="176" height="35"> 每月多领 **87.21 元**。

</div>
### 5.2 等额偿债基金（★★★）

贷款利率 i、偿债基金利率 j（通常 j < i）、期限 n：

| 量 | 公式 |
| --- | --- |
| 每期付息 | <img class="fml" src="/formulas/349e68aa1a266a.png" alt="I= i \cdot L_{0}" width="78" height="34">（**恒定**） |
| 每期向基金存款 | <img class="fml" src="/formulas/d81901a0ce04e1.png" alt="D=\dfrac{L_{0}}{s_{n}}\big\vert_{j}" width="83" height="48"> |
| 每期付款总额 | <img class="fml" src="/formulas/f7d6d93a03cefa.png" alt="R= iL_{0}+ \frac{L_{0}}{s_{n}}" width="110" height="35">|j |
| 第 k 期末贷款净额 | <img class="fml" src="/formulas/f440dbf2c8aba5.png" alt="L_{k}= L_{0}- D \cdot s_{k}\vert _{j}" width="148" height="34"> |

**核心结论**：

- **<img class="fml" src="/formulas/5311e2bc512618.png" alt="j = i" width="45" height="33">时偿债基金法 ≡ 分期偿还法**：<img class="fml" src="/formulas/796f9010520062.png" alt="iL_{0}+ \frac{L_{0}}{s_{n}}= \frac{L_{0}}{a_{n}}" width="114" height="35">（用 <img class="fml" src="/formulas/34513675239656.png" alt="\frac{1}{a_{n}}= \frac{1}{s_{n}}+ i" width="92" height="35">），且 <img class="fml" src="/formulas/98e3fe9438bc63.png" alt="L_{0}- Ds_{k}= Ra_{(n-k)}" width="161" height="34">
- j < i 时偿债基金法总付款**更大**（等价于以更高利率借款）
- **等价分期利率近似**：<img class="fml" src="/formulas/346160b4b6d5ec.png" alt="r \approx i+ 0.5(i- j)" width="141" height="34">（基金平均余额约为本金一半，每元损失 <img class="fml" src="/formulas/3bca22f012de4a.png" alt="(i- j)" width="57" height="34"> 的利息差）

<div class="kb-example">

**例 34**：10 万贷款 5 年、贷款利率 10%、基金利率 8%。<img class="fml" src="/formulas/64652f0345e771.png" alt="D= \frac{100000}{s_{5}}|_{0.08}= \frac{100000}{5.8666}=17\,045.65" width="275" height="35">；年总付款 = 10000+17045.65 = **27 045.65** > 分期偿还法的 26 379.75。第 2 年末净额 = <img class="fml" src="/formulas/780a4b3c5e6341.png" alt="100000- 17045.65 \times s_{2}|_{0.08}=64\,545.06\,\text{元}" width="331" height="34">。

</div>
<div class="kb-example">

**例 35**（两笔贷款等价）：贷款一（偿债基金法：i=6%，j=5%）与贷款二（分期偿还，利率 r）等价时：<img class="fml" src="/formulas/0c2e8b397bd5f7.png" alt="10000 \times 0.06+ \frac{10000}{s_{5}}|_{0.05}= \frac{10000}{a_{5}}|_{r} \to r=6.552\%" width="377" height="35">（近似公式给 6.5%）。

</div>
### 5.3 变额分期偿还（★★）

每期还款额 Rt 不等：<img class="fml" src="/formulas/f1495492cdd8cd.png" alt="L_{0}= \sum R_{t}v^{t}" width="106" height="34">。最常见**等额本金偿还法**：每期本金相等 → 利息递减 → 总还款额**逐期递减**。

**负偿还**：当期还款 < 当期应付利息时，差额**资本化**（本金余额增加），按贷款利率计息。变额分期偿还中负偿还可与正偿还同样处理（直接代入方程）。

<div class="kb-example">

**例 36**：贷款 5 年、i=6%，还款依次 20000/18000/16000/14000/12000。
解：拆成 10000 等额 + 2000 递减：



<p class="fml-block"><img class="fml" src="/formulas/894d87bb7d6897.png" alt="L_{0}= 10000a_{5}+ 2000(Da)_{5}= 10000 \times 4.2124+ \frac{2000 \times(5- 4.2124)}{0.06}= 42124+ 26253=68\,377.33\,\text{元}" width="725" height="34"></p>



第 3 年利息 = <img class="fml" src="/formulas/2b4f697d78eeaa.png" alt="0.06 \times L_{2}" width="80" height="34">，<img class="fml" src="/formulas/c3a4c7e3eaadbd.png" alt="L_{2}= 10000a_{3}+2000(Da)_{3}= 26730+10000 \times \cdots= 37 630 \to I_{3}=2257.80" width="585" height="34">，<img class="fml" src="/formulas/c6e9f5ab6e6e44.png" alt="P_{3}= 16000- 2257.80=13\,742.20\,\text{元}" width="290" height="34">。

</div>
### 5.4 变额偿债基金（★★ 难点）

每期总还款 Rt 变化 → 每期存款 = <img class="fml" src="/formulas/369e483e3b85c6.png" alt="R_{t}- iL_{0}" width="73" height="34"> 变化。

**贷款本金公式**（由偿债基金期末本利和 = 贷款本金反解）：

> <img class="fml" src="/formulas/e1aca428e9a85d.png" alt="L_{0}= \sum \frac{R_{t}(1+j)^{-t}}{1+(i- j) \cdot a_{n}|_{j}}" width="147" height="38">（分子按基金利率贴现，分母修正贷款利率与基金利率之差）

**关键陷阱——负储蓄**：若某期还款 < 应付利息，向基金储蓄为**负**（从基金取钱 = 增加贷款本金）。此时**负储蓄必须按贷款利率 i 资本化，而不能按基金利率 j 计息**！处理方法：先跳过负储蓄期，从基金能正常积累的第一期起建立价值方程，反推出该期初的本金余额，再往前推原始本金。（与变额分期偿还中「负偿还可直接代方程」形成对比——考试最爱考这个差别。）

### 5.5 易错点

- 分期偿还法利息逐期**递减**、本金逐期**递增**、总额恒定；等额本金法总额**递减**。
- 过去法/将来法算出的余额相同，选计算量小的。
- <img class="fml" src="/formulas/f74f5037507d49.png" alt="\frac{P_{k+1}}{P_{k}}" width="36" height="36">（偿还本金等比数列）——选择题常用。
- 偿债基金法每期**付息恒定**（iL0），与分期偿还的递减利息不同；但扣除基金自身利息收入后「净利息」也是递减的，两法本质等价（j=i 时）。
- <img class="fml" src="/formulas/5311e2bc512618.png" alt="j = i" width="45" height="33">⟺ 两法等价；j < i ⟹ 偿债基金法更贵。
- 等价利率近似 <img class="fml" src="/formulas/346160b4b6d5ec.png" alt="r \approx i+ 0.5(i- j)" width="141" height="34"> 只对「基金平均余额 ≈ 本金一半」的情形成立。
- 变额偿债基金的负储蓄按**贷款利率**资本化（不是基金利率）——最容易错的点。

---

## 第6章 债券价值分析

**金融市场分类**（名词解释）：债务市场（债券）vs 股权市场（股票，剩余权益索取权在后）；货币市场（≤1 年短期债务工具，流动性高）vs 资本市场（>1 年）；一级市场（发行新证券，投资银行协助）vs 二级市场（流通已发行证券，提供流动性和价格发现）。

**债券分类**：按付息方式——零息债券（贴现发行、面值偿还）/ 附息债券（定期付息票）；按期限——短（≤1 年）/ 中（1–10 年）/ 长（>10 年）；按发行主体——国债（无违约风险）/ 地方政府债 / 公司债（担保债券、信用债券、垃圾债券——评级低于 BBB 的投机级）。

![债券定价与利率风险](/int/int-bond-risk.svg)

### 6.1 债券定价四大公式（★★★ 计算核心）

符号：P 价格、i 到期收益率（YTM）、F 面值、C 偿还值（通常 C=F）、r 息票率、rF 每期息票收入、<img class="fml" src="/formulas/d413e2fffe2888.png" alt="g= \frac{rF}{C}" width="60" height="34"> 修正息票率、n 付息次数、i꜀ = rF/P 当期收益率。

| 公式 | 表达式 | 适用场景 |
| --- | --- | --- |
| **基本公式** | <img class="fml" src="/formulas/c781ccc7c08f96.png" alt="P= rF \cdot a_{n}+ C \cdot v^{n}" width="165" height="34"> | 万能 |
| **溢价公式** | <img class="fml" src="/formulas/9d679eb5cb3d70.png" alt="P= C[1+(g- i)a_{n}]" width="168" height="34"> | 判断溢价/折价最方便 |
| **基价公式** | <img class="fml" src="/formulas/785d27a0985105.png" alt="P= G+(C- G)v^{n}" width="162" height="34">，<img class="fml" src="/formulas/443918cc898d8c.png" alt="G= \frac{rF}{i}" width="65" height="34"> | 基价 G 是「产生与息票等额的周期收益所需投资」；<img class="fml" src="/formulas/4115b44a3e070d.png" alt="i= \frac{rF}{G}" width="57" height="34"> |
| **Makeham** | <img class="fml" src="/formulas/a93f0edb9aa28b.png" alt="P=\left(\frac{g}{i}\right)(C- K)+ K" width="179" height="34">，<img class="fml" src="/formulas/fc338bc8e1f294.png" alt="K= Cv^{n}" width="79" height="34"> | 分期偿还债券（拆成多个子债券，g 相同时 <img class="fml" src="/formulas/34a902c881f73d.png" alt="P=\left(\frac{g}{i}\right)\left(\sum C- \sum K\right)+\sum K" width="245" height="34">） |

**价格性质**（简答高频）：

- P 是 i 的**减函数**：收益率越高价格越低
- P 是 i 的**凸函数**（下凸）：收益率下降时价格加速上升、上升时减速下降——**同样幅度的收益率变化，涨价幅度 > 下跌幅度**，对投资者有利
- 可赎回债券在低收益率区间可能**上凸**（对投资者不利）
- 平价发行（P=C=F）⟺ <img class="fml" src="/formulas/0ecf8c9f731c5d.png" alt="i = r" width="46" height="33">；n→∞ 时当期收益率 = 到期收益率
- 当期收益率 i꜀ = rF/P 与到期收益率**同向变化**；期限越长越接近 YTM

### 6.2 溢价、折价与账面值（★★★）

- **溢价** = <img class="fml" src="/formulas/328fe0b7ec112e.png" alt="P- C= C(g- i)a_{n}" width="163" height="34">（g > i 时）；**折价** = <img class="fml" src="/formulas/45fca92d8ac8e9.png" alt="C- P" width="57" height="34">（g < i 时，即负溢价）
- **账面值**（book value）：按购买时收益率计算的投资余额。<img class="fml" src="/formulas/f834ead07d0473.png" alt="V_{0}= P" width="62" height="34">；<img class="fml" src="/formulas/6ed71254cf19bf.png" alt="V_{n}= C" width="64" height="34">
  - 将来法：<img class="fml" src="/formulas/2b48bc82f64264.png" alt="V_{t}= C[1+(g- i)a_{(n-t)}]" width="194" height="34"> = <img class="fml" src="/formulas/65bfa5f2c3716d.png" alt="rF \cdot a_{(n-t)}+ Cv^{n-t}" width="152" height="34">
  - 过去法：<img class="fml" src="/formulas/a3f19024fcaef3.png" alt="V_{t}= P(1+i)^{t}- rF \cdot s_{t}" width="188" height="34">
  - 递推：<img class="fml" src="/formulas/8071b821effb3f.png" alt="V_{t}= V_{t-1}(1+i)- rF" width="173" height="33">
- 账面值 ≠ 市场价格：账面值基于**固定**的到期收益率，不随市场利率变化
- **溢价分摊**（amortization of premium）：每期息票收入超过应得利息（<img class="fml" src="/formulas/a4a21a5872d4bf.png" alt="iV_{t-1}" width="45" height="33">）的部分 = <img class="fml" src="/formulas/f72b5fedc9a3f3.png" alt="V_{t-1}- V_{t}= C(g- i)v^{n- t+1}" width="213" height="33">，逐期**递增**；溢价逐期摊入息票，账面值从 P 递减到 C
- **折价累积**（accumulation of discount）：应得利息超过息票的部分，账面值从 P 递增到 C；折价累积 = 负的溢价分摊
- 溢价债券：实得息票 > 应得利息；折价债券：实得息票 < 应得利息

<div class="kb-example">

**例 37**：面值 1000、息票率 6%、3 年期、YTM 5%。<img class="fml" src="/formulas/9857ee1d0b57e8.png" alt="P= 1000[1+(0.06- 0.05)a_{3}]= 1000 \times(1+0.01 \times 2.7232)=1027.23\,\text{元}" width="569" height="33">（溢价 27.23）。第 1 年：应得利息 = <img class="fml" src="/formulas/98ff2c488b2eb5.png" alt="1027.23 \times 0.05= 51.36" width="184" height="33">，实得息票 60，溢价分摊 8.64，年末账面值 **1018.59**；第 2 年分摊 <img class="fml" src="/formulas/f222e497da88f7.png" alt="9.07 \to 1009.52" width="125" height="33">；第 3 年分摊 <img class="fml" src="/formulas/7fc9b147b4b1a5.png" alt="9.52 \to 1000" width="102" height="33">。分摊之和 = 溢价总额。

</div>
<div class="kb-example">

**例 38**：同上但 YTM 8% → P = **948.46**（折价 51.54）；账面值 <img class="fml" src="/formulas/8606c9553f7cca.png" alt="948.46 \to 964.34 \to 981.49 \to 1000" width="275" height="33">（折价累积 15.88/17.15/18.52）。

</div>
### 6.3 任意时点的价格与账面值（★★）

两个息票日之间（0<t<1，P0 为上一息票日价格）：

- **价格**（含应计息票，全价）：<img class="fml" src="/formulas/b45033b84a557c.png" alt="P_{t}=(1+i)^{t} \cdot P_{0}" width="135" height="33">；或从下一息票日反推 <img class="fml" src="/formulas/024e2fc4ea0539.png" alt="P_{t}=(1+i)^{t- 1}(rF+P_{1})" width="197" height="33">
- 下一息票日价格：<img class="fml" src="/formulas/b5f08150bf7509.png" alt="P_{1}= P_{0}(1+i)- rF" width="163" height="33">
- **账面值** = 价格 − 应计息票收入，三种方法：

| 方法 | 公式 | 特点 |
| --- | --- | --- |
| 理论方法 | <img class="fml" src="/formulas/ecc0d98a28355a.png" alt="V_{t}=(1+i)^{t}P_{0}- \frac{rF[(1+i)^{t}- 1]}{i}" width="220" height="35"> | 累积与息票都按复利，最精确 |
| 半理论方法 | <img class="fml" src="/formulas/a51913661a7c65.png" alt="V_{t}=(1+i)^{t}P_{0}- t \cdot rF" width="185" height="33"> | 息票按单利、累积按复利 |
| 实践方法 | <img class="fml" src="/formulas/8382c831d4b5ef.png" alt="V_{t}=(1+ti)P_{0}- t \cdot rF" width="187" height="33"> | 全按单利，最简单、应用最广 |

三法结果非常接近，在息票日完全相等。价格呈**阶梯形**上升（息票支付日跌落），账面值**平滑**变化。

### 6.4 可赎回债券（★★★ 概念+计算）

**可赎回债券**（callable bond）：含赎回条款，发行人有权在特定条件下按约定赎回价提前回购。赎回条款**有利于发行人**（利率下降时赎回旧债、发低息新债，降低融资成本；解除限制性条款；调整资产结构），因此可赎回债券预期收益率**较高**、价格**较低**（相比不含赎回条款的同类债券）。通常有赎回保护期（5–10 年），赎回价通常 ≥ 面值（高出的部分约为 1 年利息）。

**定价原则**：投资者愿意支付的最高价格 = **所有可能赎回时点上的最低价格**（发行人会在对自己最有利 = 对投资者最不利的时点赎回）。

- 若各赎回时点偿还值 C 相同：**g > i 时期限越短价格越低**（选最早赎回日）；**g < i 时期限越长价格越低**（选到期日）
- 赎回价不同则逐点计算取最小；可能赎回时点无穷多时用溢价公式分析单调性

<div class="kb-example">

**例 39**：面值 1000、息票率 12%、8 年期、保护期 5 年；第 5/6/7 年末赎回价 1050/1030/1010、到期偿还 1000；要求收益率 10%。
解：<img class="fml" src="/formulas/7674db0a2c1fbe.png" alt="P_{5}= 1050+(120- 105)a_{5}= 1106.86" width="295" height="33">；<img class="fml" src="/formulas/c16ce9d522a58f.png" alt="P_{6}= 1030+(120- 103)a_{6}= 1104.04" width="295" height="33">；<img class="fml" src="/formulas/cf0e90a62945ff.png" alt="P_{7}= 1010+(120- 101)a_{7}=1102.50" width="295" height="33">（最低）；<img class="fml" src="/formulas/57f6de995e04d8.png" alt="P_{8}= 1106.70" width="108" height="33">。投资者最高出价 **1102.50 元**——若按 1106.70 买而发行人第 7 年赎回，实际收益率只有 9.92% < 10%。

</div>
### 6.5 易错点

- 溢价公式中 <img class="fml" src="/formulas/d413e2fffe2888.png" alt="g= \frac{rF}{C}" width="60" height="34"> 是**修正息票率**（除以偿还值 C），息票率 r 除以面值 <img class="fml" src="/formulas/b12b9ac52d77a5.png" alt="F-- C= F" width="108" height="33"> 时两者不同。
- 溢价分摊额逐期**递增**（不是递减）：<img class="fml" src="/formulas/142ad155e270d1.png" alt="C(g- i)v^{n- t+1}" width="120" height="33"> 中 t 越大 v 的幂越小。
- 账面值基于购买时 YTM 固定不变，**市场价格**才随利率波动。
- 分期偿还债券用 Makeham 公式的前提：拆分后各子债券 **g 相同**。
- 可赎回债券取「最低价」而非「最高价」——站在**投资者保护**角度。
- g > i（溢价债）时发行人倾向**早赎回**；g < i（折价债）时倾向**不赎回**（拖到期）。
- 两个息票日之间的「价格」含应计利息（全价/脏价），账面值 = 价格 − 应计息票。

---

## 第7章 利率风险管理

利率风险 = 债券价格因收益率波动而产生的不确定性。度量工具：**久期**（一阶敏感度）与**凸度**（二阶修正）。原理同样适用于任何已知现金流的资产/负债及整个公司。

### 7.1 麦考利久期（★★★）

**麦考利久期 Dᴹ**（Macaulay duration）：现金流到期时间的**加权平均数**，权数 = 各现金流现值占总现值的比重：



<p class="fml-block"><img class="fml" src="/formulas/b0f59ac30bd2b8.png" alt="D^{M}= \sum \frac{t \cdot R_{t}(1+i)^{-t}}{P}= \sum \frac{t \cdot R_{t}e^{- \delta t}}{P(\delta)}=- P&#x27;\frac{\delta}{P(\delta)}" width="327" height="38"></p>



- 是**时间**概念（单位：年），也等于「价格对利息力的单位变化速率」
- <img class="fml" src="/formulas/c24754a59c1478.png" alt="D^{M}" width="36" height="34"> 越大 → 价格对利率越敏感 → 利率风险越高
- 到期时间只能粗糙衡量利率风险：同期限的零息债券比附息债券风险大（加权回收时间更长）

**典型值**（选择题高频，均基于年实际收益率 i）：

| 现金流 | 麦考利久期 Dᴹ |
| --- | --- |
| n 年零息债券 | **n** |
| n 年期等额分期偿还贷款 | <img class="fml" src="/formulas/23fbad26992903.png" alt="\frac{1+i}{i}- \frac{n}{(1+i)^{n}- 1}" width="110" height="36">（与本金、还款额无关，只取决于 n、i） |
| 期末付永续年金 | <img class="fml" src="/formulas/6deb9619daf6a0.png" alt="\frac{1+i}{i}= \frac{1}{d}" width="66" height="34"> |
| 期初付永续年金 | **1/i**（现值 <img class="fml" src="/formulas/99fc2a0e55d5f4.png" alt="\ddot{a}_{\infty}=\frac{1+i}{i}" width="78" height="34">，用 <img class="fml" src="/formulas/15e257c12f3d73.png" alt="D^{M}=- P" width="89" height="34">′<img class="fml" src="/formulas/98eef6628bca9d.png" alt="\frac{\delta}{P}" width="21" height="34"> 求导即得） |
| n 年期平价附息债券（r=i） | <img class="fml" src="/formulas/ac99fa844dd0db.png" alt="\ddot{a}_{n}= \frac{1- v^{n}}{d}" width="81" height="34">（教材式 7.12） |

**性质**：

- <img class="fml" src="/formulas/c24754a59c1478.png" alt="D^{M}" width="36" height="34"> 是收益率的**减函数**（<img class="fml" src="/formulas/c0d939b20b1d56.png" alt="\frac{dD^{M}}{d\delta}=- \sigma^{2}&lt; 0" width="128" height="35">，σ² 为现金流时间方差）——收益率越高久期越小
- 期限越长久期**不一定**越大：低息票率+高收益率的长期债券，久期可能先升后降（教材图 7-2 反例：息票率 5%、收益率 15%，超过约 20 年后久期反而下降）
- 息票率越高久期越小（递减速度放缓）

<div class="kb-example">

**例 40**：3 年期债券面值 1000、息票率 10%、年收益率 10%（平价）。
<img class="fml" src="/formulas/b72ddab03064af.png" alt="D^{M}= \frac{1 \times 90.91+ 2 \times 82.64+ 3 \times 826.45}{1000}=2.74\,\text{年}" width="300" height="34">。平价债券（r=i）可直接用 <img class="fml" src="/formulas/33096d7d6204e2.png" alt="\ddot{a}_{3}= \frac{1- 1.1^{-3}}{d}=2.74" width="151" height="34">。

</div>
<div class="kb-example">

**例 41**：15 年期按月等额偿还贷款，每月复利一次年名义利率 12%（月利率 1%，n=180）。
用教材式 <img class="fml" src="/formulas/34a90d067c8d42.png" alt="D^{M}= \frac{1+i}{i}- \frac{n \cdot v^{n}}{1- v^{n}}" width="140" height="34">：<img class="fml" src="/formulas/c429969e609ca4.png" alt="v^{180}= 1.01^{-180} \approx 0.1683" width="194" height="34">，代入得 <img class="fml" src="/formulas/95dbc48036599e.png" alt="101- \frac{180 \times 0.1683}{0.8317}" width="123" height="34"> **64.5 月 ≈ 5.4 年**（教材值 64.97 月，中间值取整导致的小差异，方法一致）。

</div>
### 7.2 修正久期（★★★ 计算高频）

**修正久期 D**（modified duration）：价格关于**名义收益率 y** 的单位变化速率（强度概念，非时间）：

> <img class="fml" src="/formulas/90c3c630fe7c30.png" alt="D=- P&#x27;\frac{y}{P(y)}= \frac{D^{M}}{1+ \frac{y}{m}}" width="165" height="38">（m 为年复利次数；<img class="fml" src="/formulas/e7e9b9e7ecb4c5.png" alt="y = i" width="46" height="33">时 <img class="fml" src="/formulas/cad1a35dc25aa2.png" alt="D= \frac{D^{M}}{1+i}" width="72" height="35">）

- D 越大 → 价格波动越大 → 利率风险越大
- **价格近似**：<img class="fml" src="/formulas/a90d072594cd17.png" alt="\frac{\Delta P}{P} \approx- D \cdot \Delta y" width="121" height="34">（收益率变化 Δy 用基点表示，1 bp = 0.01%）
- <img class="fml" src="/formulas/8e6441a1e383bb.png" alt="m \to \infty" width="67" height="33"> 时 <img class="fml" src="/formulas/38455d8a7394c2.png" alt="D \to D^{M}" width="80" height="34">（麦考利久期是修正久期的连续复利极限）
- D 也是收益率的减函数
- 基于不同收益率口径（名义 vs 实际）的修正久期**数值不同、含义不同**，必须说明口径

<div class="kb-example">

**例 42**：2 年期零息债券，<img class="fml" src="/formulas/9ecbc62d260e63.png" alt="i^{(12)}= 12" width="78" height="34">%。<img class="fml" src="/formulas/ac6168f969daba.png" alt="D^{M}= 2" width="69" height="34">。
基于名义收益率：<img class="fml" src="/formulas/845f8309a9987a.png" alt="D = 2/(1+\frac{0.12}{12})" width="136" height="33">= **1.98**；基于年实际收益率 12.68%：<img class="fml" src="/formulas/1d04ff9af4c9d1.png" alt="D= \frac{2}{1.1268}=1.77" width="141" height="34">。

</div>
<div class="kb-example">

**例 43**：债券价格 115.92、YTM 7%、修正久期 8.37，YTM 升到 7.05% 时价格 <img class="fml" src="/formulas/6b53b4d53e0216.png" alt="\approx 115.92\times(1-8.37\times 0.0005)=115.92\times(1-0.42\%)=115.43\,\text{元}" width="525" height="34">（精确值还要加凸度修正）。

**n 年期期末付复递增年金**（增长率 r，净利率 <img class="fml" src="/formulas/56dd1601474aa6.png" alt="j= \frac{i- r}{1+r}" width="66" height="34">）的修正久期：<img class="fml" src="/formulas/239aa7c162dfff.png" alt="D= \frac{\frac{1}{j}- \frac{n(1+j)^{-n}}{1-(1+j)^{-n}}}{1+i}" width="120" height="44">（教材式 7.18，考频低，理解链式求导思路即可）。

</div>
### 7.3 有效久期（★★）

现金流**不确定**（可赎回债券等利率敏感型资产）时无法解析求导，用**割线斜率**近似：



<p class="fml-block"><img class="fml" src="/formulas/c6b9a374da3f0c.png" alt="D^{E}= \frac{P_{-}- P_{+}}{2 \cdot P_{0} \cdot \Delta y}" width="105" height="36"></p>



<img class="fml" src="/formulas/bac0cdfa5e2e09.png" alt="\frac{P_{+}}{P_{-}}" width="27" height="36"> 收益率升/降 Δy 后的价格。用 Δδ 代替 Δy 则近似的是麦考利久期。

<div class="kb-example">

**例 44**：可赎回债券 <img class="fml" src="/formulas/4b33f8f320ece0.png" alt="P_{0}=100" width="76" height="34">，收益率 ±100bp 时 <img class="fml" src="/formulas/4985c2e54d3054.png" alt="P_{+}=95.87" width="94" height="34">、<img class="fml" src="/formulas/45b70ff313fc97.png" alt="P_{-}=104.76" width="102" height="34">。
<img class="fml" src="/formulas/82000cd420b888.png" alt="D^{E}= \frac{104.76- 95.87}{2 \times 100 \times 0.01}=4.445" width="199" height="34">。收益率升 50bp 时价格 ≈ <img class="fml" src="/formulas/6e4fe2689b1c24.png" alt="100 \times(1- 4.445 \times 0.005)=97.78\,\text{元}" width="288" height="34">（只用久期；加凸度修正后 97.86）。

</div>
### 7.4 凸度家族（★★★）

**凸度 C**（convexity）：价格关于名义收益率的**二阶导数**与价格之比，度量久期线性近似的误差：

> <img class="fml" src="/formulas/9a60be1ada25b5.png" alt="C=\frac{P&#x27;&#x27;(y)}{P(y)}= \sum \frac{t(t+1)R_{t}v^{t+2}}{P \cdot\left(1+\frac{y}{m}\right)^{2}}" width="201" height="45">；m=1 时 <img class="fml" src="/formulas/6de1311cdeaf39.png" alt="C= \frac{\sum t(t+1)R_{t}(1+i)^{-t-2}}{P}" width="165" height="36">

**麦考利凸度 <img class="fml" src="/formulas/1164cfbd5b1c7d.png" alt="C^{M}" width="35" height="34">**：基于利息力，= 现金流时间**平方的加权平均**：<img class="fml" src="/formulas/de5e37c7c6fd55.png" alt="C^{M}=\frac{P&#x27;&#x27;(\delta)}{P(\delta)}=\frac{\sum t^{2}R_{t}e^{-\delta t}}{P}" width="184" height="38">

三个重要关系（计算题跳板）：

1. <img class="fml" src="/formulas/c96fb744a4412c.png" alt="C^{M}=(D^{M})^{2}+ \sigma^{2}" width="149" height="34">（σ² 为现金流时间方差）⟹ <img class="fml" src="/formulas/f43d79fe5306b8.png" alt="C^{M} \ge(D^{M})^{2}" width="110" height="34">
2. <img class="fml" src="/formulas/b24d84854d8e5c.png" alt="C=(D^{M}+ C^{M})(1+i)^{-2}" width="206" height="34">（用麦考利久期凸度算凸度的捷径）
3. n 年零息债券：<img class="fml" src="/formulas/c74c6a06754fb8.png" alt="D^{M}= n" width="72" height="34">、<img class="fml" src="/formulas/a36935338beb2a.png" alt="C^{M}= n^{2}" width="77" height="34">、<img class="fml" src="/formulas/3d8219c65be452.png" alt="C= n(n+1)(1+i)^{-2}" width="178" height="34">

**有效凸度**：<img class="fml" src="/formulas/058a860cda1158.png" alt="C^{E}= \frac{P_{+}+ P_{-}- 2P_{0}}{P_{0} \cdot(\Delta y)^{2}}" width="131" height="36">

<div class="kb-example">

**例 45**：10 年期年金每年末付 1、i=5%。<img class="fml" src="/formulas/3a375a61db782c.png" alt="P= a_{10}= 7.7217" width="141" height="34">；修正久期 D = 4.86；<img class="fml" src="/formulas/6514458997651f.png" alt="C= \frac{\sum t(t+1)v^{t+2}}{P}= \frac{274.91}{7.72}=35.61" width="249" height="36">；<img class="fml" src="/formulas/19edabec3d535d.png" alt="C^{M}= \frac{\sum t^{2}v^{t}}{P}= \frac{263.72}{7.72}=34.16" width="227" height="36">。
验证关系式 <img class="fml" src="/formulas/7ea5a93716c140.png" alt="C=(D^{M}+C^{M})(1+i)^{-2}" width="206" height="34">：<img class="fml" src="/formulas/2dbd2cbd6d2a6d.png" alt="D^{M}= D(1+i)= 5.10" width="182" height="34">，(5.10+34.16)/1.1025 = 39.26/1.1025 = **35.6** ✓。

</div>
<div class="kb-example">

**例 46**：期初付永续年金（i 常数）：<img class="fml" src="/formulas/67c7a5af5a7c97.png" alt="P(\delta)= \ddot{a}_{\infty}= \frac{1}{1- e^{- \delta}}" width="152" height="34">。令 <img class="fml" src="/formulas/e06c2e1c815154.png" alt="x= v= e^{- \delta}" width="99" height="34">，则 <img class="fml" src="/formulas/f2d6e1f0084fb1.png" alt="P= \frac{1}{1- x}" width="72" height="34">：
- 一阶：<img class="fml" src="/formulas/15e257c12f3d73.png" alt="D^{M}=- P" width="89" height="34">′<img class="fml" src="/formulas/90ce1b9a0774b7.png" alt="\frac{\delta}{P}=1\,\text{/i}" width="71" height="34">
- 二阶：<img class="fml" src="/formulas/13f2d24ef06083.png" alt="P&#x27;&#x27;(\delta)=\frac{x(1+x)}{(1-x)^{3}}" width="119" height="36"> <img class="fml" src="/formulas/6410f6923edc3e.png" alt="C^{M}= \frac{x(1+x)}{(1- x)^{2}}= \frac{v(1+v)}{d^{2}}= \frac{2+i}{i^{2}}" width="219" height="36">

验证 <img class="fml" src="/formulas/c96fb744a4412c.png" alt="C^{M}=(D^{M})^{2}+ \sigma^{2}" width="149" height="34">：<img class="fml" src="/formulas/2ead57b1957e40.png" alt="\sigma^{2}= \frac{v}{d^{2}}" width="65" height="34">（如 i=5% 时 <img class="fml" src="/formulas/7ec038882241d1.png" alt="C^{M}= 820" width="86" height="34">、<img class="fml" src="/formulas/59bb5becb1e9b4.png" alt="(D^{M})^{2}= 400" width="108" height="34">、<img class="fml" src="/formulas/19097ea65d671d.png" alt="\sigma^{2}= 420" width="76" height="34"> ✓）。

</div>
### 7.5 久期凸度的应用：价格变化估计（★★★）

泰勒展开保留二阶项：

> <img class="fml" src="/formulas/3a3fa474ab2ef8.png" alt="\frac{\Delta P}{P} \approx- D \cdot \Delta y+ \frac{1}{2} \cdot C \cdot(\Delta y)^{2}" width="239" height="34">（名义收益率口径：修正久期 + 凸度配对）
> <img class="fml" src="/formulas/9146d6f2220a80.png" alt="\frac{\Delta P}{P} \approx- D^{M} \cdot \Delta \delta+ \frac{1}{2} \cdot C^{M} \cdot(\Delta \delta)^{2}" width="266" height="34">（利息力口径：麦考利久期 + 麦考利凸度配对）

**久期与凸度的配对使用**（简答易错）：用名义收益率就配「修正久期+凸度」；用利息力就配「麦考利久期+麦考利凸度」；现金流不确定就配「有效久期+有效凸度」。

<div class="kb-example">

**例 47**：15 年期债券面值 1000、息票率 11%、YTM 12%。<img class="fml" src="/formulas/a095a57fb4f9fa.png" alt="P= 110a_{15}+1000v^{15}=931.89" width="247" height="33">；<img class="fml" src="/formulas/a6ab5c4ad38ff2.png" alt="D^{M}= \frac{7220.86}{931.89}=7.75" width="162" height="33">；<img class="fml" src="/formulas/9680b437dc07d0.png" alt="D = \frac{7.75}{1.12}" width="72" height="33">= **6.92**；<img class="fml" src="/formulas/42179ff3f9acaa.png" alt="C = \frac{69585.71}{931.89}" width="96" height="33">= **74.67**。
YTM 升 50bp 到 12.5%：真实价格 900.51（<img class="fml" src="/formulas/ced4615e53564b.png" alt="- 3.37" width="52" height="33">%）；只用久期：<img class="fml" src="/formulas/e9805acdd5c5d6.png" alt="- 6.92 \times 0.005=- 3.46" width="185" height="33">%（低估）；久期+凸度：<img class="fml" src="/formulas/61665955da212d.png" alt="- 3.46" width="52" height="33">% + ½×<img class="fml" src="/formulas/76dc68f2c56eff.png" alt="74.67 \times 0.005^{2}=- 3.46" width="186" height="33">%+0.093% = <img class="fml" src="/formulas/943191ef22fa70.png" alt="- 3.37\%" width="68" height="33"> ✓（几乎精确）。

**组合久期/凸度** = 各成分以**市值为权**的加权平均：<img class="fml" src="/formulas/b779ecd62a0bd7.png" alt="D= \sum\left(\frac{P_{k}}{P}\right)D_{k}" width="128" height="33">。
**久期的局限**（简答）：假设收益率曲线平坦且只平移；实际上短端波动大于长端、曲线可能扭曲（短升长降），组合久期失效，必须定期再调整。

**理想债券**：久期小 + 凸度大——凸度对投资者**总是有利**（涨得多跌得少），久期是双刃剑。

</div>
### 7.6 免疫策略（★★★ 简答 + 计算）

**Redington 免疫**三条件（负债给定、调整资产，使盈余 <img class="fml" src="/formulas/19163083558f66.png" alt="S= PV(A)- PV(L)" width="174" height="33"> 在利率微小变动时不减少）：

1. **<img class="fml" src="/formulas/4e5a782fa5dd4d.png" alt="PV(A) = PV(L)" width="141" height="33">**（现值相等）
2. **<img class="fml" src="/formulas/534ba62ca300d1.png" alt="D(A) = D(L)" width="115" height="33">**（久期相等 ⟹ S′(y) = 0）
3. **C(A) > C(L)**（凸度更大 ⟹ S″(y) > 0，S 取极小值 0）

泰勒展开：<img class="fml" src="/formulas/4c295043734f3f.png" alt="S(y+\Delta y)\approx S+S&#x27;\Delta y+\frac{1}{2}S&#x27;&#x27;(\Delta y)^{2}=0+0+\text{正项}&gt;0" width="438" height="33"> ⟹ 利率无论微升微降盈余都增加。
**前提**：收益率曲线平坦且只发生**微小平移**；久期凸度随时间漂移，需**定期再调整**；条件三若总能满足意味着无风险套利，实践中很难。

<div class="kb-example">

**例 48**（教材例 7-20 精髓）：负债 200 万、10 年后到期、利率 6%（D_L = 10，麦考利凸度 = 100）。三种债券：A（10 年、息票 6.7%、<img class="fml" src="/formulas/26e288199d81dd.png" alt="D^{M}=7.67" width="92" height="33">）、B（15 年、息票 6.988%、<img class="fml" src="/formulas/57645d2c52625e.png" alt="D^{M}=10" width="78" height="33">、<img class="fml" src="/formulas/c492cac919f388.png" alt="C^{M}=126.5" width="100" height="33">）、C（30 年、息票 5.9%、<img class="fml" src="/formulas/3a69dfe5b3793f.png" alt="D^{M}=14.64" width="101" height="33">）。
- 只有 **B 满足久期匹配**（<img class="fml" src="/formulas/57645d2c52625e.png" alt="D^{M}=10" width="78" height="33">）且 <img class="fml" src="/formulas/4070540d5b02f0.png" alt="C^{M}=126.5&gt; 100" width="151" height="33"> 无论利率升降第 10 年末累积值 ≥ 358.17 万（免疫 ✓）
- 利率降到 5% 时：A 累积 350.49 万（不足！）、B 358.61、C 376.04
- **A+C 组合**：66.5%A + 33.5%C 使组合久期 = <img class="fml" src="/formulas/ae727a1ff84422.png" alt="7.67p+14.64(1- p)= 10" width="205" height="33">，组合凸度 = <img class="fml" src="/formulas/7771909991135a.png" alt="0.665 \times 68.73+0.335 \times 318.11" width="244" height="33"> **152.27 > B 的 126.5** → 免疫能力更强（杠铃策略优于子弹策略）

**完全免疫**（full immunization）：收益率曲线发生**任意大小**的平移时盈余都不减少。三条件：

1. <img class="fml" src="/formulas/e05ff27ba0e712.png" alt="PV(A) = PV(L) 2. D(A)" width="197" height="33">= D(L)
3. **负债到期时间 t 夹在两笔资产到期时间之间：t−a < t < t+b**

（满足完全免疫 ⟹ 必满足 Redington 免疫：单笔负债 <img class="fml" src="/formulas/afc3c000597619.png" alt="\sigma^{2}=0" width="58" height="33">、两笔资产 <img class="fml" src="/formulas/5dcbd948048705.png" alt="\sigma^{2}&gt;0" width="58" height="33"> ⟹ <img class="fml" src="/formulas/bdd588207bf25b.png" alt="C^{M}(A)= t^{2}+\sigma^{2}&gt; t^{2}= C^{M}(L)" width="255" height="33">。）

</div>
<div class="kb-example">

**例 49**：10 年末负债 2000 万，持有 5 年期零息债（到期值 620.92 万）+ 15 年期零息债（到期值 1610.51 万），i=10%。
验证：<img class="fml" src="/formulas/6d426ec09b68f8.png" alt="PV(A)= \frac{620.92}{1.1^{5}}+ \frac{1610.51}{1.1^{15}}= 385.54+385.54= 771.09" width="411" height="34"> 万 = <img class="fml" src="/formulas/69b3f1faa83505.png" alt="PV(L)= \frac{2000}{1.1^{10}}" width="115" height="33"> ✓；<img class="fml" src="/formulas/fc9488e4300257.png" alt="D^{M}(A)= 10" width="106" height="33"> ✓；5<10<15 ✓ → **完全免疫**。利率升到 12%：盈余 = +2.6 万 > 0（利率任意变动盈余都增加）。

</div>
### 7.7 现金流配比（★★）

**现金流配比**（cash flow matching / dedication）：对每笔未来负债安排**相同到期时间、相同金额**的资产逐一匹配。

- 优点：无需不断调整组合（免疫需要动态再平衡）
- 缺点：限制投资选择灵活性；找不到匹配资产就只能放弃
- 有各期限零息债券时最简单；只有附息债券时**从最长期限负债开始倒序配比**：先买足匹配最远负债的债券，扣除其全部现金流（含中途息票），再配比次远负债，递推至全部匹配

<div class="kb-example">

**例 50**（教材例 7-22）：负债（万元）：第 1–5 年 4090/6790/3550/36550/5250。可选：2 年期 20% 息票、4 年期 10%、5 年期 5%（面值均 100）。
- 第 5 年末负债 5250 ÷ 5 年债到期现金流 105 = **50 万份** 5 年期债（其息票每年 250 抵减前 4 年负债）
- 剩余负债最远在第 4 年末 36300 ÷ 110 = **330 万份** 4 年期债（息票每年 3300）
- 剩余最远第 2 年末 3240 ÷ 120 = **27 万份** 2 年期债 → 全部配比完成

</div>
### 7.8 易错点

- 麦考利久期是**时间**、修正久期是**强度**；<img class="fml" src="/formulas/7d5eb0a8cfccab.png" alt="D= \frac{D^{M}}{1+\frac{y}{m}}" width="78" height="38">，m=1 时 <img class="fml" src="/formulas/cad1a35dc25aa2.png" alt="D= \frac{D^{M}}{1+i}" width="72" height="35">。
- 久期匹配必须**口径一致**：名义收益率配修正久期，利息力配麦考利久期。
- 零息债券：<img class="fml" src="/formulas/c74c6a06754fb8.png" alt="D^{M}= n" width="72" height="34">（到期时间）但 <img class="fml" src="/formulas/1a281ecba8bd76.png" alt="D= \frac{n}{(1+i)^\cdots}" width="92" height="36">（按口径折算）；<img class="fml" src="/formulas/a3399ca7dff1e0.png" alt="C= \frac{n(n+1)}{(1+i)^{2}}" width="90" height="36">。
- 期限长 ≠ 久期大（低息票 + 高收益率的超长期债券久期可能回落）。
- 凸度对投资者永远有利；「久期小 + 凸度大」是最理想组合。
- Redington 免疫第三条件是 C(A) **>** C(L)（严格大于）；完全免疫第三条件是**时间夹逼**。
- 完全免疫 ⟹ Redington 免疫，反之不然。
- 现金流配比从**最长期限**负债开始倒推，不是从最短。
- 免疫是时点状态，久期随时间和利率漂移 → 必须定期再调整。

---

## 附：全书高频名词解释速查

| 名词 | 一句话定义 |
| --- | --- |
| 累积函数 a(t) | 期初 1 单位本金在时刻 t 的累积值，一切利息度量的母体 |
| 实际利率 | 1 单位本金在一个时期末赚取的利息金额（期末付） |
| 实际贴现率 | 一定时期内产生的利息与期末累积值之比（期初预收） |
| 名义利率 <img class="fml" src="/formulas/fab53528f38d07.png" alt="i^{(m)}" width="35" height="33"> | 一年复利 m 次（或多年复利一次）的利率，每期实际利率 <img class="fml" src="/formulas/fe5a49be0115c0.png" alt="\frac{i^{(m)}}{m}" width="32" height="34"> |
| 利息力 δ | 资本在每一时点上的利息增长强度，<img class="fml" src="/formulas/ee20c9a011f5d0.png" alt="\delta= \ln(1+i)" width="105" height="34">，连续复利 |
| 单利 | 只对本金计息，<img class="fml" src="/formulas/0dc3b1edb88318.png" alt="a(t)=1+it" width="104" height="33">，不满足一致性 |
| 复利 | 利息再生息，<img class="fml" src="/formulas/00a20e5d48105d.png" alt="a(t)=(1+i)^{t}" width="116" height="33">，实际利率恒定 |
| 年金 | 一系列付款或收款；等额/变额、期初/期末、定期/永续、即期/延期 |
| 永续年金 | 无限期支付的年金，<img class="fml" src="/formulas/9f633a76f59b0c.png" alt="a_{\infty}= \frac{1}{i}" width="64" height="34">，没有终值 |
| 延期年金 | 经过一定时期后才开始支付的年金，m\|<img class="fml" src="/formulas/07d670d7d86787.png" alt="a_{n}= v^{m}a_{n}" width="87" height="33"> |
| 价值方程 | 基于现金流入现值 = 现金流出现值建立的方程 |
| 收益率（IRR） | 使资金流入现值 = 流出现值（NPV=0）的利率 |
| 净现值 NPV | 资金净流入的现值，利率的减函数（常规现金流） |
| 多重收益率 | 现金流符号多次改变时 NPV=0 有多个解，两法均失效 |
| 币值加权收益率 | 考虑本金增减时机的 IRR，衡量投资者个人收益 |
| 时间加权收益率 | 剔除资金进出影响的几何平均收益率，衡量基金经理业绩 |
| 修正收益率 MIRR | 流入按再投资利率、流出按筹资利率分别折算后的收益率 |
| 组合方法 | 按基金平均收益率给所有投资者分配收益 |
| 投资年度方法 | 新投资头几年按投资年度利率、之后按组合利率分配 |
| 分期偿还法 | 每期还款含利息 + 部分本金，余额逐期递减 |
| 偿债基金法 | 每期付息 + 存基金，到期基金一次还本 |
| 过去法 / 将来法 | 用已还款项累积值 / 未来还款现值计算未偿还本金余额（等价） |
| 负偿还 | 当期还款不足付息，差额资本化增加本金余额 |
| 债券当期收益率 | 息票收入 / 债券价格，YTM 的近似 |
| 修正息票率 g | 息票收入 / 偿还值，<img class="fml" src="/formulas/d413e2fffe2888.png" alt="g= \frac{rF}{C}" width="60" height="34"> |
| 溢价 / 折价 | 价格高于 / 低于偿还值；溢价 = <img class="fml" src="/formulas/bbea99caebcd6c.png" alt="C(g- i)a_{n}" width="90" height="33"> |
| 账面值 | 按购买时收益率计算的投资余额，<img class="fml" src="/formulas/8071b821effb3f.png" alt="V_{t}= V_{t-1}(1+i)- rF" width="173" height="33"> |
| 溢价分摊 | 每期息票超过应得利息的部分，逐期递增，冲减账面值 |
| 基价 G | 产生与息票等额周期收益所需的投资，<img class="fml" src="/formulas/443918cc898d8c.png" alt="G= \frac{rF}{i}" width="65" height="34"> |
| Makeham 公式 | <img class="fml" src="/formulas/70b03bd8552999.png" alt="P=\left(\frac{g}{i}\right)(C- K)+K" width="179" height="34">，适合分期偿还债券 |
| 可赎回债券 | 发行人有权按约定价格提前赎回，价格取各赎回日最低价 |
| 麦考利久期 | 现金流到期时间的现值加权平均，= <img class="fml" src="/formulas/f9347809d921ac.png" alt="- P" width="34" height="34">′<img class="fml" src="/formulas/98eef6628bca9d.png" alt="\frac{\delta}{P}" width="21" height="34"> |
| 修正久期 | 价格对名义收益率的单位变化速率，= <img class="fml" src="/formulas/528726879026bd.png" alt="\frac{D^{M}}{1+\frac{y}{m}}" width="40" height="38"> |
| 有效久期 | 现金流不确定时用割线斜率近似的久期 <img class="fml" src="/formulas/785654f14caca5.png" alt="\frac{P_{-}- P_{+}}{2P_{0}\Delta y}" width="53" height="36"> |
| 凸度 | 价格对收益率的二阶导数与价格之比，度量线性近似误差 |
| 麦考利凸度 | 现金流时间平方的加权平均 = <img class="fml" src="/formulas/cf9f3988508475.png" alt="(D^{M})^{2}+\sigma^{2}" width="97" height="34"> |
| 基点 | 0.01%，100 bp = 1% |
| Redington 免疫 | 现值相等 + 久期相等 + 资产凸度更大，抵御微小利率平移 |
| 完全免疫 | 前两条件 + 负债到期日夹在两笔资产到期日之间，抵御任意平移 |
| 现金流配比 | 每笔负债匹配同期限同金额资产，从最长期限倒序配置 |
