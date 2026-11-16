---
summary: "计量经济学 全面详解笔记，共 10 章：绪论、统计学基础、双变量线性回归、多元线性回归、模型建立与估计中的问题及对策、动态经济模型、时间序列分析、联立方程模型、面板数据模型、定性选择模型。覆盖 OLS 推导与高斯-马尔可夫定理、t/F/Wald/LM/LR 检验、异方差与自相关与多重共线性的诊断及修正、工具变量与 2SLS、分布滞后与 Granger 因果、单位根与协整与误差修正、联立方程识别、固定/随机效应与 Hausman 检验、Logit/Probit/Tobit 与边际效应。含 14 张自绘图、大量带完整演算的工作例题与 9 道跨章综合题、对比表、公式速查与 88 条易错点，并对课件中的缺漏与不严谨表述作了补充修正。"
---

# 计量经济学笔记

::: info 笔记概要
- **所属课程**：计量经济学（经济学类 / 统计学类等专业核心基础课）。
- **核心内容**：以「经典线性回归模型」为主线——用经济理论提出可检验的假设，用数据估计参数，用统计推断判断关系是否显著，再检验模型假定是否被破坏、如何修正，最后延伸到时间序列、联立方程、面板数据与离散选择等非标准情形。重点抓三条线：① **模型与假定**（总体回归函数、六大古典假定、高斯-马尔可夫定理）；② **估计与检验**（OLS/ML/GMM、t / F / Wald / LM / LR、置信区间与 p 值）；③ **诊断与对策**（异方差、自相关、多重共线性、内生性各自的后果、检验统计量、修正方法）。
- **学习建议**：每个结论都要能回答「依赖哪个假定、假定被破坏会怎样、用什么检验发现它、用什么方法补救」；所有公式都要能代入小样本手算一遍。
:::

## 全书目录

| 章 | 主题 | 核心考点 | 重要度 |
| --- | --- | --- | --- |
| 1 | 绪论 | 学科定义、方法论八步、数据类型、模型与应用 | ★★ |
| 2 | 统计学基础 | 概率分布、抽样分布、估计量性质、区间估计与假设检验 | ★★★ |
| 3 | 双变量线性回归 | OLS 推导、古典假定、BLUE、R²、t/F 检验与预测 | ★★★ |
| 4 | 多元线性回归 | 偏回归系数、矩阵形式、调整 R²、约束 F 检验、虚拟变量与函数形式 | ★★★ |
| 5 | 模型问题及对策 | 误设定、多重共线性、异方差、自相关、随机解释变量与 IV/2SLS | ★★★ |
| 6 | 动态经济模型 | 分布滞后、阿尔蒙多项式、Koyck/部分调整/适应预期、Granger 因果 | ★★★ |
| 7 | 时间序列分析 | 平稳性、单位根与 ADF、伪回归、协整与 ECM、ARIMA、ARCH/GARCH | ★★★ |
| 8 | 联立方程模型 | 内生/外生/前定、结构式与简化式、识别阶/秩条件、ILS 与 2SLS | ★★ |
| 9 | 面板数据模型 | 混合回归、固定效应、随机效应、Hausman 检验、双向效应与动态面板 | ★★★ |
| 10 | 定性选择模型 | LPM、Logit/Probit、MLE、边际效应与优势比、多项/有序/Tobit | ★★★ |
| 综 | 综合例题精讲 | 9 道跨章大题，含完整手算演算 | 复习用 |
| 附 A / B | 速查 | 公式结论速查表、88 条易错点清单 | 复习用 |

---

## 第 1 章 绪论

### 1.1 什么是计量经济学（★★）

计量经济学（Econometrics）＝**经济理论 + 数学 + 统计推断**，用数据给经济关系以「经验内容」。三个经典定义可作对照：

| 来源 | 定义要点 |
| --- | --- |
| 萨缪尔森等（1954） | 对经济关系给出经验内容 |
| 戈德伯格（1964） | 把经济理论、数学与统计推断应用于经济现象分析的社会科学 |
| 现代教材通行表述 | 以经济理论为先验、以数据为证据，对经济关系进行**估计、检验与预测**的方法论 |

与相关学科的区别：**数理经济学**用数学表述理论但不接触数据；**经济统计学**描述与整理数据但不检验理论；**计量经济学**则把二者连接起来——先将理论写成可检验的**随机**模型，再用样本推断总体参数。

::: tip 为什么模型必须有随机扰动项 u
经济行为不可能被少数几个变量完全解释，必须留一个 `u` 容纳：① 被省略的次要因素；② 测量误差；③ 人类行为的随机性；④ 函数形式的近似误差；⑤ 模型设定误差。正因 `u` 随机，`Y` 也是随机变量，才需要统计推断——这也是计量经济学区别于确定性数学模型的根本点。
:::

### 1.2 计量经济学方法论（★★★）

传统方法论八步：
(1) 理论 / 假设陈述 → (2) 建立数学模型（含随机项）→ (3) 建立计量经济模型 → (4) 获取数据 → (5) 估计参数 → (6) 假设检验（经济 / 统计 / 计量经济检验）→ (7) 模型诊断与修正 → (8) 用于预测或政策评价

| 检验层次 | 检验什么 | 常用工具 |
| --- | --- | --- |
| 经济意义检验 | 系数符号、大小是否符合理论（如需求斜率应为负） | 与经济理论对照 |
| 统计检验 | 拟合优度、参数与方程显著性 | R²、t、F、置信区间 |
| 计量经济检验 | 古典假定是否成立 | 异方差/自相关/多重共线性/内生性检验 |
| 模型稳定性与外推 | 结构是否稳定、能否预测 | Chow 检验、递归残差、样本外预测 |

::: tip 现代研究范式的转变
传统框架「先设定模型、再检验」。现代应用计量更强调 **研究设计（design-based）**：先明确**识别策略**与反事实，再谈估计。核心问题是「这个系数能否被解释为因果效应」，而不只是「显著性星号有几颗」。因此需要掌握潜在结果框架（RCM）、随机对照试验（RCT）、双重差分（DID）、断点回归（RDD）、工具变量（LATE）、合成控制等（详见 5.5 节与 5.7 节）。
:::

### 1.3 数据类型（★★★）

| 类型 | 定义 | 例子 | 主要注意点 |
| --- | --- | --- | --- |
| 横截面数据 | 同一时点、多个个体 | 某年 500 户家庭消费调查 | 异方差常见；个体异质性 |
| 时间序列数据 | 同一个体、多个时期 | 1990–2025 年 GDP | 自相关、非平稳、趋势/季节 |
| **面板数据** | 同一批个体、多个时期 | 4 个产业 × 20 年投资额 | 个体效应、组内/组间变异 |
| 混合数据 pooled | 不同时点不同个体（个体不固定） | 多期独立抽样 | 不能当面板用固定效应 |

![计量经济学方法论与数据类型](/econ/econ-overview.svg)

::: tip 工作示例 · 需求函数的估计与预测
某商品需求函数估计结果为 <img class="fml" src="/formulas/e241297f6a9586.png" alt="\hat{Q}= 76.05- 3.88P" width="153" height="33">，问 `P = 4.50` 时的需求量预测值。



<p class="fml-block"><img class="fml" src="/formulas/bc4f633bdbe85c.png" alt="\hat{Q}= 76.05- 3.88 \times 4.50= 76.05- 17.46= 58.59" width="384" height="33"></p>


延伸：斜率 <img class="fml" src="/formulas/da603dcb97d747.png" alt="- 3.88" width="52" height="33"> 表示价格每上升 1 个单位，需求量平均减少 3.88 个单位；若 `P` 与 `Q` 的单位分别是「元/件」与「万件」，则要看 elasticity 才便于跨商品比较：<img class="fml" src="/formulas/4ed5862aec0a39.png" alt="\epsilon=\left(\frac{dQ}{dP}\right) \cdot\left(\frac{P}{Q}\right)=- 3.88 \times \frac{4.50}{58.59} \approx- 0.298" width="331" height="41">，即价格上升 1%，需求量约下降 0.30%（缺乏弹性）。**注意**：预测只能给出点估计，严格报告还需给预测区间（第 3 章）。
:::

### 1.4 模型、软件与工作流（★★）

- 常见软件：EViews / Stata（教学与实证研究主流）、R（`lm`、`plm`、`fixest`）、Python（`statsmodels`、`linearmodels`）、SAS / SPSS、Gretl。
- 一个可复现的实证流程：数据清洗与描述统计 → 散点图与相关系数 → 设定基准模型 → OLS 估计并报告**系数、标准误、t 值、p 值、R²、n** → 诊断检验 → 稳健性（换设定/换样本/换估计量）→ 结果解释（区分**相关**与**因果**）。
- 报告规范：系数下方括注标准误或 t 值，用 `* / ** / ***` 标注显著性并注明阈值，报告使用的标准误类型（普通 / 异方差稳健 / 聚类稳健）。

::: danger 易错 · 绪论
- 计量经济学**不是**「用统计软件跑回归」：理论设定、识别与诊断比点一个按钮重要得多。
- 「模型通过 t 检验」不等于「模型正确」：可能存在内生性、误设定、样本选择偏差，这些都不会体现在 t 值上。
- 混合数据 ≠ 面板数据：只有**同一批个体**在多个时期都被观测到才是面板，否则不能用固定效应估计量。
:::

### 1.5 软件实操速查（Stata / R / Python）

| 任务 | Stata | R | Python (statsmodels / linearmodels) |
| --- | --- | --- | --- |
| OLS | `reg y x1 x2` | `lm(y ~ x1 + x2)` | `sm.OLS(y, sm.add_constant(X)).fit()` |
| 异方差稳健 SE | `reg y x, vce(robust)` | `lmtest::coeftest(m, vcov=vcovHC)` | `.fit(cov_type='HC1')` |
| 聚类稳健 SE | `reg y x, vce(cluster id)` | `vcovCL(..., cluster=~id)` | `.fit(cov_type='cluster', groups=id)` |
| HAC | `newey y x, lag(4)` | `vcovHAC` | `.fit(cov_type='HAC', cov_kwds={'maxlags':4})` |
| 异方差检验 | `estat hettest` / `estat imtest, white` | `lmtest::bptest` | `statsmodels.stats.diagnostic.het_breuschpagan` |
| 自相关检验 | `estat dwatson` / `estat bgodfrey` | `lmtest::dwtest` / `bgtest` | `durbin_watson(resid)` / `acorr_breusch_godfrey` |
| VIF | `estat vif` | `car::vif(m)` | `variance_inflation_factor` |
| RESET | `estat ovtest` | `lmtest::resettest` | `linear_reset` |
| 2SLS / IV | `ivregress 2sls y (x = z) w` | `AER::ivreg` | `linearmodels.iv.IV2SLS` |
| 固定效应 | `xtreg y x, fe` / `reghdfe ... absorb(id)` | `plm(..., model='within')` / `fixest::feols` | `PanelOLS(..., entity_effects=True)` |
| 随机效应 | `xtreg y x, re` | `plm(..., model='random')` | `RandomEffects` |
| Hausman | `hausman fe re` | `plm::phtest` | `panel_results.compare(...)` |
| ADF | `dfuller y, lags(4)` | `urca::ur.df` / `tseries::adf.test` | `statsmodels.tsa.stattools.adfuller` |
| Logit / Probit | `logit y x` / `probit y x` | `glm(..., family=binomial(link='logit'))` | `sm.Logit` / `sm.Probit` |
| 边际效应 | `margins, dydx(*)` | `margins::margins(m)` | `.get_margeff()` |
| Tobit / Heckman | `tobit` / `heckman` | `AER::tobit` / `sampleSelection` | `HurdleCountModel` / 自定义 |
| DID / 事件研究 | `reghdfe y i.treat##i.post, absorb(id year)` | `fixest::feols(y ~ i(post, treat) | id + year)` | `PanelOLS` + 交互项 |

::: tip 可复现报告清单
① 数据来源、样本期、样本量与缺失处理；② 变量定义与描述统计表；③ 基准模型设定与识别策略（要写明「凭什么能作因果解释」）；④ 系数、标准误类型（普通/稳健/聚类层级）、显著性星号含义、R² 与 n；⑤ 诊断检验结果；⑥ 稳健性（换设定、换样本、安慰剂、预趋势）；⑦ 效应大小的经济含义（弹性、边际效应、货币化）。
:::

---

---

## 第 2 章 计量经济分析的统计学基础

### 2.1 概率、随机变量与常用分布（★★）

| 概念 | 定义 / 结论 |
| --- | --- |
| 期望 `E(X)` | 随机变量分布的集中位置；`E(aX+b)=aE(X)+b` |
| 方差 `Var(X)` | <img class="fml" src="/formulas/79396ca7e7af26.png" alt="E[(X- E(X))^{2}]" width="135" height="33">；<img class="fml" src="/formulas/bacf3b84577197.png" alt="\operatorname{Var}(aX+b)=a^{2}\operatorname{Var}(X)" width="208" height="33"> |
| 协方差 `Cov(X,Y)` | 共变程度；独立 ⇒ 协方差为 0，**反之不成立** |
| 相关系数 <img class="fml" src="/formulas/82feb24cebaa32.png" alt="\rho" width="16" height="33"> | <img class="fml" src="/formulas/1b1463b6508d4f.png" alt="\frac{\operatorname{Cov}(X,Y)}{\sigma_{X} \sigma_{Y}} \in[- 1,1]" width="139" height="35">，只度量**线性**相关 |
| 条件期望 | `E(Y|X)` 是回归分析的数学核心（总体回归函数即条件均值） |

| 分布 | 由谁构造 | 在计量中的用途 |
| --- | --- | --- |
| 标准正态 `N(0,1)` | — | 大样本下 z 检验、渐近推断 |
| <img class="fml" src="/formulas/63a79773f1a12e.png" alt="\chi^{2}(m)" width="55" height="33"> | m 个独立标准正态平方和 | LM 检验、Wald/LR 检验、方差检验 |
| t(m) | <img class="fml" src="/formulas/d876dafa10dbe3.png" alt="\dfrac{Z}{\sqrt{\chi^{2}(m)/m}}" width="102" height="54"> | **单个系数显著性检验**（小样本、未知 σ） |
| F(m, n−k−1) | <img class="fml" src="/formulas/f610f521c898ae.png" alt="\dfrac{\chi^{2}(m)/m}{\chi^{2}(df)/df}" width="92" height="52"> | **多个线性约束的联合检验**、整体显著性 |

::: tip 三大抽样分布的关系
<img class="fml" src="/formulas/dc49e581718791.png" alt="Z \sim N(0,1)" width="100" height="33">、<img class="fml" src="/formulas/e0ecac3eb36a6a.png" alt="V \sim \chi^{2}(m)" width="93" height="33"> 且独立 → <img class="fml" src="/formulas/720278c7a500ec.png" alt="t= \frac{Z}{\sqrt{\frac{V}{m}}} \sim t(m)" width="128" height="41">；<img class="fml" src="/formulas/96cc9501de98f7.png" alt="U \sim \chi^{2}(m)" width="93" height="33">、<img class="fml" src="/formulas/950ff4d5d07e64.png" alt="V \sim \chi^{2}(r)" width="86" height="33"> 独立 → <img class="fml" src="/formulas/e4dcce018f0b5e.png" alt="F= \frac{\frac{U}{m}}{\frac{V}{r}} \sim F(m,r)" width="144" height="42">。由此可得两个常用结论：<img class="fml" src="/formulas/9f5ab34040f4de.png" alt="t^{2}(m)= F(1, m)" width="135" height="34">（单系数 t 检验与 F 检验等价），以及 <img class="fml" src="/formulas/6f177214e95e7c.png" alt="m \cdot F(m, \cdot) \to \chi^{2}(m)" width="168" height="34">（大样本下 LM/Wald/LR 都渐近服从 χ²）。
:::

### 2.2 抽样分布、估计量的性质（★★★）

估计量是样本的函数，因而是**随机变量**，有自己的分布（抽样分布）。

| 性质 | 含义 | 数学表达 |
| --- | --- | --- |
| 无偏性 | 抽样分布均值等于真值（小样本性质） | <img class="fml" src="/formulas/dbb8524d33fbcc.png" alt="E(\hat{\theta})= \theta" width="76" height="34"> |
| 有效性 | 在同类中方差最小 | <img class="fml" src="/formulas/ef05be873e7ecf.png" alt="\operatorname{Var}(\hat{\theta}) \le \operatorname{Var}(\tilde{\theta})" width="135" height="34"> |
| 最小均方误差 | 兼顾偏差与方差 | <img class="fml" src="/formulas/146585c43c9ad8.png" alt="MSE= \operatorname{Var}+ Bias^{2}" width="168" height="34"> |
| **一致性** | 样本增大时依概率收敛到真值（大样本性质） | <img class="fml" src="/formulas/374d9cdb7a366f.png" alt="plim \hat{\theta}= \theta" width="85" height="34"> |
| 渐近正态 | 大样本下可近似用正态分布做推断 | <img class="fml" src="/formulas/f59b395bd3a677.png" alt="\sqrt{n}(\hat{\theta}- \theta) \to N(0, V)" width="175" height="34"> |

![抽样分布、置信区间与假设检验](/econ/econ-inference.svg)

::: danger 易错 · 无偏 ≠ 一致，有效 ≠ 无偏
- **无偏是小样本性质**，与 n 无关；**一致是大样本性质**。无偏但不一致的例子：<img class="fml" src="/formulas/6478e8054e17d6.png" alt="\hat{\theta}= X_{1}" width="62" height="34">（用第一个观测估计均值，无偏但方差不随 n 缩小）；有偏但一致的例子：样本方差用 `1/n` 而非 <img class="fml" src="/formulas/44dd8c77650b0e.png" alt="\frac{1}{n- 1}" width="35" height="34">（有偏，但 n→∞ 时偏差消失）。
- 「有效性」必须在**同类估计量**（如都是线性无偏）内比较；有偏估计量方差可以更小（岭回归、LASSO 正是用偏差换方差）。
- 中心极限定理给的是**估计量的渐近分布**，不是「样本数据的分布变成正态」。
:::

### 2.3 参数估计与区间估计（★★）

| 方法 | 思想 | 例子 |
| --- | --- | --- |
| 矩估计 MM | 用样本矩替代总体矩 | <img class="fml" src="/formulas/4aceb087ef8781.png" alt="\hat{\mu}= \bar{X}" width="57" height="34"> |
| **最小二乘 OLS** | 使残差平方和最小 | 第 3 章 |
| **极大似然 MLE** | 使观测样本出现概率最大 | Logit/Probit、GARCH |
| 广义矩 GMM | 让样本矩条件尽可能接近 0 | 动态面板、工具变量 |

**置信区间**：`θ̂ ± 临界值 × se(θ̂)`。95% 置信度的正确含义是「**反复抽样**构造的区间中约 95% 会覆盖真值」，不是「真值以 95% 概率落在这个已算出的区间里」（频率学派下真值固定、区间随机）。

::: tip 工作示例 · 均值区间估计
`n=25`，样本均值 `X̄=10`，已知总体标准差 <img class="fml" src="/formulas/c80068b6bb66c4.png" alt="\sigma=2" width="51" height="34">：


<p class="fml-block"><img class="fml" src="/formulas/d9302810941ec5.png" alt="\begin{gathered}
se(\bar{X})= \frac{\sigma}{\sqrt{n}}= \frac{2}{5}= 0.4 \\
95\% CI= 10 ± 1.96 \times 0.4=[9.216, 10.784] \\
\text{若} \; \sigma \; \text{未知、样本标准差} \; \text{s=2} \; \text{，改用} \; \text{t(24)} \; \text{临界值} \; \text{2.064} \; \text{：} \\
95\% CI= 10 ± 2.064 \times 0.4=[9.174, 10.826] \; \text{（略宽）}
\end{gathered}" width="452" height="130"></p>


n 越大区间越窄（精度 <img class="fml" src="/formulas/87ecc32b4f22b9.png" alt="\propto \frac{1}{\sqrt{n}}" width="48" height="37">）：要把宽度减半，样本量需增到 4 倍。
:::

### 2.4 假设检验（★★★）

| 概念 | 内容 |
| --- | --- |
| 原假设 <img class="fml" src="/formulas/206d1773898cba.png" alt="H_{0}" width="29" height="34"> 备择 H1 | 通常把「想推翻的」放 H0（如 <img class="fml" src="/formulas/e3735499f11597.png" alt="\beta=0" width="51" height="34">）；检验只在 H0 成立时构造抽样分布 |
| 第一类错误 | H0 为真却拒绝，概率 = **显著性水平 α**（常取 0.05 / 0.01 / 0.10） |
| 第二类错误 | H0 为假却未拒绝，概率 = β；<img class="fml" src="/formulas/dfa10968c0706d.png" alt="1- \beta" width="49" height="34"> 称检验功效（power） |
| **p 值** | H0 成立时，观测到「当前这么极端或更极端」结果的概率；<img class="fml" src="/formulas/be587757365cbb.png" alt="p&lt; \alpha" width="51" height="34"> 则拒绝 |
| 拒绝域 | 双侧 <img class="fml" src="/formulas/9d91a1ae4c41b4.png" alt="\vert t\vert &gt; t_{\frac{\alpha}{2}}" width="65" height="34">；单侧 <img class="fml" src="/formulas/9678fd36e7b1c6.png" alt="t&gt; t_\alpha" width="53" height="34"> 或 <img class="fml" src="/formulas/afc3dfc0d68c9b.png" alt="t&lt;- t_\alpha" width="66" height="34"> |
| 检验流程 | 设 <img class="fml" src="/formulas/79e2f0e16e643b.png" alt="\frac{H_{0}}{H_{1}}" width="27" height="35"> 选统计量与其分布 → 定 α 与临界值 → 算统计量 → 比较或看 p 值 → 用**经济语言**下结论 |

::: tip p 值与置信区间的对偶
- 双侧检验在 α 水平拒绝 H0: <img class="fml" src="/formulas/44431bc10f7094.png" alt="\beta=\beta_{0}" width="59" height="34"> ⟺ <img class="fml" src="/formulas/918cb4aaf5f6e2.png" alt="\beta_{0}" width="25" height="34"> 落在 <img class="fml" src="/formulas/d17e8196edc6bf.png" alt="(1- \alpha)" width="63" height="33"> 置信区间**之外**。
- 「不拒绝 H0」≠「接受 H0 为真」，只表示**证据不足**（尤其小样本、功效低时）。
- 「统计显著」≠「经济显著」：n 很大时微小系数也能 p<0.001，需同时看效应大小与置信区间。
- 多重检验会抬高整体第一类错误率（20 个无关变量平均会「显著」1 个），应做 Bonferroni / FDR 校正或预先注册假设。
:::

::: tip 常用临界值速查
`z: 1.645(单侧5%) / 1.96(双侧5%) / 2.576(双侧1%)`

<img class="fml" src="/formulas/0b9a7a0d4e1914.png" alt="\chi^{2}" width="25" height="33"> 临界值（5%）：df=1 → 3.84；df=2 → 5.99；df=3 → 7.81

`t: 2.064(df=24,双侧5%) / 3.182(df=3,双侧5%) / 1.96(df→∞)`
<img class="fml" src="/formulas/941ee897a511ec.png" alt="F(1, df)=t^{2}(df)" width="143" height="34">；<img class="fml" src="/formulas/afc29149c64af3.png" alt="F(2,26,5\%) \approx 3.37" width="157" height="34">，<img class="fml" src="/formulas/53499f5b59e3af.png" alt="F(3,26,5\%) \approx 2.98" width="157" height="34">。
:::

::: tip 工作示例 · 检验功效计算
设 <img class="fml" src="/formulas/c0a4807c453cc7.png" alt="\hat{\theta} \sim N(\theta, 1)" width="95" height="34">，双侧检验 <img class="fml" src="/formulas/333d7583f6b29c.png" alt="H_{0}: \theta=0" width="86" height="34">，<img class="fml" src="/formulas/5b6d66e517449f.png" alt="\alpha=0.05" width="74" height="33">（拒绝域 <img class="fml" src="/formulas/beff32eb19d3d9.png" alt="|\hat{\theta}|&gt; 1.96" width="81" height="34">），真实 <img class="fml" src="/formulas/b8bcb94b083446.png" alt="\theta=2" width="49" height="34">：


<p class="fml-block"><img class="fml" src="/formulas/5ebefb548ac103.png" alt="\begin{gathered}
\text{功效} \; = P(\hat{\theta}&gt; 1.96| \theta=2)+ P(\hat{\theta}&lt;- 1.96| \theta=2) \\
= P(Z&gt;- 0.04)+ P(Z&lt;- 3.96)= 0.5160+ 0.00004 \approx 0.516
\end{gathered}" width="487" height="60"></p>


含义：真效应为 2 个标准误时，重复抽样仍有约 **48% 的概率检不出来**（第二类错误）。要提高到 80%，需 <img class="fml" src="/formulas/53ff67233514c1.png" alt="\theta \approx 2.8" width="62" height="34"> 个标准误（即把样本量约增到 2 倍）——**「不显著」经常只是样本不够**。
:::

---

## 第 3 章 双变量线性回归模型

### 3.1 总体回归函数与样本回归函数（★★★）

| 概念 | 表达式 | 说明 |
| --- | --- | --- |
| 总体回归函数 PRF | <img class="fml" src="/formulas/5b6a9eca866a37.png" alt="Y_{i}= \beta_{0}+ \beta_{1}X_{i}+ u_{i}" width="160" height="34"> | <img class="fml" src="/formulas/76248e6a2c6317.png" alt="E(Y_{i}\vert X_{i})= \beta_{0}+\beta_{1}X_{i}" width="176" height="34">，β 是**未知常数**，u 是总体扰动 |
| 样本回归函数 SRF | <img class="fml" src="/formulas/189d7444a61672.png" alt="\hat{Y}_{i}= \hat{\beta}_{0}+ \hat{\beta}_{1}X_{i}" width="122" height="34"> | β̂ 是**估计量/估计值**（随机变量） |
| 残差 | <img class="fml" src="/formulas/7360056765bc70.png" alt="e_{i}= Y_{i}- \hat{Y}_{i}" width="97" height="34"> | e 是 u 的**估计**，二者不可混用：`u` 不可观测、`e` 可计算 |

「双变量」指只有**一个解释变量 + 一个被解释变量**（不含常数项），又称一元 / 简单线性回归。

![OLS 最小二乘原理与拟合](/econ/econ-ols.svg)

### 3.2 古典（高斯-马尔可夫）假定（★★★）

| # | 假定 | 数学表达 | 被破坏的后果 |
| --- | --- | --- | --- |
| A1 | 参数线性 | <img class="fml" src="/formulas/5b59d892dc2a94.png" alt="Y= \beta_{0}+ \beta_{1}X+ u" width="150" height="34"> | 需改用非线性最小二乘 / 变换 |
| A2 | X 非随机（或与 u 不相关） | `Cov(X_i, u_i) = 0` | **内生性 → 有偏且不一致**（第 5 章） |
| A3 | 扰动项零均值 | `E(u_i|X) = 0` | 截距有偏；常数项可吸收非零均值 |
| A4 | **同方差** | <img class="fml" src="/formulas/e61b361a3aacec.png" alt="\operatorname{Var}(u_{i}\vert X)= \sigma^{2}" width="129" height="34"> | 系数仍无偏但**不再有效**，标准误错 |
| A5 | **无自相关** | <img class="fml" src="/formulas/1ecc6dbd6c1223.png" alt="\operatorname{Cov}(u_{i},u_{j})=0\;(i\ne j)" width="183" height="33"> | 标准误错、t/F 失效 |
| A6 | 解释变量有变异、无完全共线 | `Var(X)>0`，n > 参数个数 | 无法识别 |
| （可选 A7） | 正态性 <img class="fml" src="/formulas/379cc6fb3872e9.png" alt="u \sim N(0,\sigma^{2})" width="106" height="34"> | — | 小样本精确 t/F 推断依赖它；大样本可用渐近正态替代 |

![高斯-马尔可夫假定与 BLUE](/econ/econ-gm.svg)

::: tip 高斯-马尔可夫定理
在 <img class="fml" src="/formulas/4f2ce3536534b9.png" alt="A1- A6" width="74" height="34"> 成立时，OLS 估计量是 **BLUE**：**B**est（方差最小）、**L**inear（Y 的线性组合）、**U**nbiased（无偏）、**E**stimator。即「在所有线性无偏估计量中方差最小」。
注意三点：① 定理**不要求正态性**（正态性只用于小样本精确检验）；② 「最佳」仅限**线性无偏**类，有偏估计量（岭回归）方差可以更小；③ 一旦 A2/A4/A5 被破坏，BLUE 结论不再成立。
:::

### 3.3 OLS 估计量的推导（★★★）

最小化 <img class="fml" src="/formulas/a43715b4fa5de0.png" alt="\sum e_{i}^{2}= \sum(Y_{i}- \hat{\beta}_{0}- \hat{\beta}_{1}X_{i})^{2}" width="221" height="34">，对两个参数求偏导并令为 0，得**正规方程**：



<p class="fml-block"><img class="fml" src="/formulas/67be13806dbbf6.png" alt="\begin{gathered}
\sum Y_{i}= n\hat{\beta}_{0}+ \hat{\beta}_{1}\sum X_{i} \\
\sum X_{i}Y_{i}= \hat{\beta}_{0}\sum X_{i}+ \hat{\beta}_{1}\sum X_{i}^{2}
\end{gathered}" width="259" height="72"></p>


解得（小写字母表示离差 <img class="fml" src="/formulas/e279561327d3e5.png" alt="x_{i}= X_{i}- \bar{X}" width="104" height="34">）：



<p class="fml-block"><img class="fml" src="/formulas/0aa27d4f62e902.png" alt="\begin{gathered}
\hat{\beta}_{1}= \frac{\sum x_{i} y_{i}}{\sum x_{i}^{2}}= \frac{Sxy}{Sxx}= \frac{\operatorname{Cov}(X,Y)}{\operatorname{Var}(X)} \\
\hat{\beta}_{0}= \bar{Y}- \hat{\beta}_{1}\bar{X}
\end{gathered}" width="276" height="80"></p>


**OLS 的数值性质**（无论假定是否成立）：① 回归线过样本均值点 `(X̄, Ȳ)`；② <img class="fml" src="/formulas/912ac1f6ccea05.png" alt="\sum e_{i}= 0" width="75" height="34">（含截距时）；③ <img class="fml" src="/formulas/df70390f8588a8.png" alt="\sum e_{i}X_{i}=0" width="95" height="34">（残差与解释变量不相关）；④ `Ȳ = Ŷ̄`；⑤ `SST = SSR + SSE`（总平方和 = 解释平方和 + 残差平方和）。

### 3.4 拟合优度与估计量方差（★★★）



<p class="fml-block"><img class="fml" src="/formulas/bc9f3da72dfd8f.png" alt="\begin{gathered}
R^{2}= \frac{SSR}{SST}= 1- \frac{SSE}{SST} \in[0,1] \; \text{（含截距且用} \; \text{OLS} \; \text{时）} \\
\operatorname{Var}(\hat{\beta}_{1})= \sigma^{2}/Sxx \; \text{，} \; \operatorname{Var}(\hat{\beta}_{0})= \sigma^{2}\left(\frac{1}{n}+ \frac{\bar{X}^{2}}{Sxx}\right) \\
\hat{\sigma}^{2}= \frac{SSE}{n- 2} \leftarrow \; \text{用} \; n- 2 \; \text{是因为估计了两个参数（无偏估计）} \\
se(\hat{\beta}_{1})= \sqrt{\frac{\hat{\sigma}^{2}}{Sxx}}
\end{gathered}" width="482" height="187"></p>


<img class="fml" src="/formulas/b5f2662fd9704d.png" alt="R^{2}" width="27" height="33"> 高不代表模型正确、也不代表因果；<img class="fml" src="/formulas/b5f2662fd9704d.png" alt="R^{2}" width="27" height="33"> 低不代表模型无用（横截面微观数据 <img class="fml" src="/formulas/7cff77cd8210cc.png" alt="R^{2}=0.1" width="74" height="34"> 很常见）。

::: tip 补充考点 · 一元回归中 <img class="fml" src="/formulas/82b0695e41ad7d.png" alt="R^{2}= r^{2}" width="67" height="33">
一元回归的决定系数恰等于 X 与 Y 的**样本相关系数的平方**：<img class="fml" src="/formulas/b805f73fbcee8d.png" alt="R^{2}= r_{XY}^{2}" width="82" height="34">。因此 <img class="fml" src="/formulas/7a330bd0e5c8ea.png" alt="r_{XY}=\pm\sqrt{R^{2}}" width="111" height="34">，符号与 <img class="fml" src="/formulas/680e7c7c1261e8.png" alt="\hat{\beta}_{1}" width="24" height="34"> 一致（如 <img class="fml" src="/formulas/b1123bd267bc67.png" alt="R^{2}=0.81" width="84" height="34">、斜率为负 ⇒ <img class="fml" src="/formulas/f720c14cafa00c.png" alt="r=- 0.9" width="76" height="34">）。这也解释了为什么对 X、Y 做标准化（z 分数）后，回归斜率就等于相关系数。多元回归中此等式不再成立，<img class="fml" src="/formulas/b5f2662fd9704d.png" alt="R^{2}" width="27" height="33"> 应理解为拟合值 `Ŷ` 与 `Y` 的相关系数的平方。
:::

### 3.5 区间估计、t 检验与 F 检验（★★★）



<p class="fml-block"><img class="fml" src="/formulas/55560bf9695d39.png" alt="\begin{gathered}
t= \frac{\hat{\beta}_{1}- \beta_{1},H0}{se(\hat{\beta}_{1})} \sim t(n- 2) \\
95\% CI= \hat{\beta}_{1} ± t_{0.025}(n- 2) \cdot se(\hat{\beta}_{1}) \\
\text{单解释变量时} \; F= t^{2} \; \text{（检验} \; H_{0}: \beta_{1}=0 \; \text{等价于整体显著性检验）}
\end{gathered}" width="522" height="114"></p>



::: tip 工作示例 · OLS 全套手算（务必自己复算一遍）
样本 `n=5`：`X = [1,2,3,4,5]`，`Y = [2,4,5,7,9]`。



<p class="fml-block"><img class="fml" src="/formulas/52c63564885e8b.png" alt="\begin{gathered}
\text{(1)} \; \text{均值：} \; \text{X̄ = 3} \; \text{，} \; \text{Ȳ = 5.4} \\
\text{(2)} \; \text{离差平方与交叉积：} \\
Sxx=(- 2)^{2}+(- 1)^{2}+0^{2}+1^{2}+2^{2}= 10 \\
Sxy=(- 2)(- 3.4)+(- 1)(- 1.4)+0(- 0.4)+1(1.6)+2(3.6)= 17.0 \\
\text{(3)} \; \text{估计：} \; \hat{\beta}_{1}= \frac{17}{10}= 1.7 \; \text{，} \; \hat{\beta}_{0}= 5.4- 1.7 \times 3= 0.3 \\
\text{Ŷ = 0.3 + 1.7X} \\
\text{(4)} \; \text{拟合与残差：} \\
\text{X :  1     2     3     4     5} \\
\text{Ŷ :  2.0   3.7   5.4   7.1   8.8} \\
e : 0.0 0.3- 0.4- 0.1 0.2 \\
\text{(5)} \; \text{平方和：} \; \text{SSE = 0+0.09+0.16+0.01+0.04 = 0.30} \\
\text{SST = 29.20} \; \text{，} \; \text{SSR = 28.90} \\
R^{2}= \frac{28.90}{29.20}= 0.9897 \; \text{调整} \; R^{2}= 0.9863 \\
\text{(6)} \; \text{方差与检验：} \; \hat{\sigma}^{2}= \frac{0.30}{3}= 0.10 \\
se(\hat{\beta}_{1})= \sqrt{\frac{0.10}{10}}= 0.10 \\
\text{t = 1.7/0.10 = 17.0  (&gt; t0.025(3)=3.182} \; \text{，强烈拒绝} \; \text{H0: }\beta \text{1=0)} \\
95\% CI= 1.7 ± 3.182 \times 0.10=[1.382, 2.018] \\
F= t^{2}= 289 \\
\text{(7)} \; \text{预测：} \; \text{X=6} \; \text{时} \; \hat{Y}= 0.3+ 1.7 \times 6= 10.5
\end{gathered}" width="530" height="584"></p>


**检查点**：残差和 <img class="fml" src="/formulas/79cfa79570e966.png" alt="0+0.3- 0.4- 0.1+0.2= 0" width="227" height="34"> ✓；回归线过 `(3, 5.4)` ✓。
:::

### 3.6 预测：均值预测与个别值预测（★★）

| 类型 | 对象 | 标准误 |
| --- | --- | --- |
| 均值预测 | <img class="fml" src="/formulas/be18b71f517c62.png" alt="E(Y\vert X_{0})" width="76" height="34"> | <img class="fml" src="/formulas/ed75e379e05735.png" alt="se_{mean}= \hat{\sigma}\sqrt{\frac{1}{n}+ \frac{(X_{0}- \bar{X})^{2}}{Sxx}}" width="197" height="42"> |
| 个别值预测 | 单个 <img class="fml" src="/formulas/0f1b752d046545.png" alt="Y_{0}" width="25" height="34"> | <img class="fml" src="/formulas/7eec632e71ede7.png" alt="se_{ind}= \hat{\sigma}\sqrt{1+ \frac{1}{n}+ \frac{(X_{0}- \bar{X})^{2}}{Sxx}}" width="216" height="42"> |

个别值预测区间**更宽**（多了扰动项自身的不确定性 <img class="fml" src="/formulas/e58684f3085369.png" alt="\sigma^{2}" width="25" height="34">）。两者都在 <img class="fml" src="/formulas/66bfe3bf68eb74.png" alt="X_{0}= \bar{X}" width="69" height="34"> 处最窄，<img class="fml" src="/formulas/21651e2520369b.png" alt="X_{0}" width="29" height="34"> 离样本中心越远区间越宽；**样本外远推**风险很大（函数形式可能已变）。

::: danger 易错 · 一元回归
- `u` 与 `e` 不同；<img class="fml" src="/formulas/e22a7f214f94f3.png" alt="\operatorname{Var}(\hat{\beta})" width="61" height="34"> 公式里的 <img class="fml" src="/formulas/e58684f3085369.png" alt="\sigma^{2}" width="25" height="34"> 是**扰动项方差**，要用 <img class="fml" src="/formulas/03a5b419ada645.png" alt="\frac{SSE}{n- 2}" width="38" height="34"> 估计，不是 `SSE/n`。
- 「σ̂² 无偏」用 n−2；MLE 估计用 n（有偏但一致）。
- <img class="fml" src="/formulas/b5f2662fd9704d.png" alt="R^{2}" width="27" height="33"> 不能跨不同被解释变量（如线性模型 vs 对数模型）直接比较；加变量 <img class="fml" src="/formulas/b5f2662fd9704d.png" alt="R^{2}" width="27" height="33"> 只增不减，故多元要用调整 R²。
- t 检验显著只说明「线性关联显著」，不能推出「X 导致 Y」。
:::

### 3.7 OLS 无偏性与一致性的证明范式

**无偏性推导**（一元、X 非随机、`E(u_i)=0`）：


<p class="fml-block"><img class="fml" src="/formulas/8d90415aeda4f9.png" alt="\begin{gathered}
\hat{\beta}_{1}= \frac{\sum x_{i}Y_{i}}{Sxx}= \frac{\sum x_{i}(\beta_{0}+\beta_{1}X_{i}+u_{i})}{Sxx} \\
= \beta_{1}+ \frac{\sum x_{i}u_{i}}{Sxx} \; \text{（用} \; \sum x_{i}=0 \; \text{、} \; \sum x_{i}X_{i}=Sxx \; \text{）} \\
E(\hat{\beta}_{1})= \beta_{1}+ \frac{\sum x_{i} E(u_{i})}{Sxx}= \beta_{1} \checkmark \\
\operatorname{Var}(\hat{\beta}_{1})= \frac{\operatorname{Var}\left(\sum x_{i}u_{i}\right)}{Sxx^{2}}= \sigma^{2}\frac{Sxx}{Sxx^{2}}= \sigma^{2}/Sxx \; \text{（用同方差} \; \text{+} \; \text{无自相关）}
\end{gathered}" width="569" height="175"></p>


可见**无偏性只需 A2/A3**，而 <img class="fml" src="/formulas/4335f9e535ad03.png" alt="\operatorname{Var}(\hat{\beta}_{1})=\sigma^{2}/Sxx" width="150" height="33"> 还须 A4/A5。

**一致性**（X 随机但严格外生时）：


<p class="fml-block"><img class="fml" src="/formulas/d602453d705aa9.png" alt="plim \hat{\beta}_{1}= \beta_{1}+ \frac{plim[\left(\frac{1}{n}\right)\sum x_{i}u_{i}]}{plim[\left(\frac{1}{n}\right)\sum x_{i}^{2}]}= \beta_{1}+ \frac{\operatorname{Cov}(X,u)}{\operatorname{Var}(X)}" width="345" height="47"></p>


因此只要 `Cov(X,u)=0` 就一致；这也直接给出**内生性偏误** <img class="fml" src="/formulas/4936a081a05cbb.png" alt="plim \hat{\beta}_{1}- \beta_{1}= \frac{\operatorname{Cov}(X,u)}{\operatorname{Var}(X)}" width="182" height="36">。

---

## 第 4 章 多元线性回归模型

### 4.1 模型与偏回归系数（★★★）



<p class="fml-block"><img class="fml" src="/formulas/01c7a36971d235.png" alt="Y_{i}= \beta_{0}+ \beta_{1}X_{1i}+ \beta_{2}X_{2i}+ \cdots+ \beta_{k}X_{ki}+ u_{i}" width="340" height="34"></p>


<img class="fml" src="/formulas/d533b430bb5b9c.png" alt="\beta_{j}" width="24" height="34"> 是**偏回归系数**：在**保持其它解释变量不变（ceteris paribus）**的前提下，`X_j` 变动 1 单位对 `Y` 的影响。这正是多元回归相对一元回归的核心价值——把「混杂因素」从相关关系中剥离出来。

::: tip 工作示例 · 遗漏变量如何造成偏误
真实模型 <img class="fml" src="/formulas/f806bdab698af0.png" alt="Y= \beta_{0}+ \beta_{1}X_{1}+ \beta_{2}X_{2}+ u" width="216" height="34">，但只回归 `Y` 对 <img class="fml" src="/formulas/318fee4a66121c.png" alt="X_{1}" width="28" height="34">，则
<img class="fml" src="/formulas/8b5c087648b8af.png" alt="plim \tilde{\beta}_{1}= \beta_{1}+ \beta_{2} \cdot \delta_{1}" width="169" height="34">，其中 <img class="fml" src="/formulas/ee5e5fca6c2c83.png" alt="\delta_{1}" width="22" height="34"> 是 <img class="fml" src="/formulas/401f2f741f2b5a.png" alt="X_{2}" width="29" height="34"> 对 <img class="fml" src="/formulas/318fee4a66121c.png" alt="X_{1}" width="28" height="34"> 回归的斜率（辅助回归系数）。
偏误方向 = <img class="fml" src="/formulas/3ea1eb2b1e6e2d.png" alt="sign(\beta_{2}) \times sign(Corr(X_{1},X_{2}))" width="248" height="34">。
经典例子：估计「教育回报率」时遗漏「个人能力」（与教育正相关、且提高工资）→ <img class="fml" src="/formulas/dc60979297b187.png" alt="\beta_{1}" width="25" height="34"> **向上偏误**；解决办法是加入能力代理变量、用双胞胎数据固定效应，或用工具变量（义务教育法、学校距离）。
:::

### 4.2 矩阵形式与估计（★★★）



<p class="fml-block"><img class="fml" src="/formulas/bb9e65cdd42f30.png" alt="\begin{gathered}
\text{y = X}\beta \text{ + u        (X} \; \text{为} \; n \times(k+1) \; \text{矩阵，第一列全} \; \text{1)} \\
\hat{\beta}=(X&#x27;X)^{-1}X&#x27;y \leftarrow \; \text{要求} \; \text{X′X} \; \text{可逆，即无完全多重共线且} \; \text{n &gt; k+1} \\
\operatorname{Var}(\hat{\beta})= \sigma^{2}(X&#x27;X)^{-1} \; \text{，} \; \hat{\sigma}^{2}= e&#x27;\frac{e}{n- k- 1} \\
e= y- X\hat{\beta}= My \; \text{（} \; M= I- X(X&#x27;X)^{-1}X&#x27; \; \text{为「残差制造者」矩阵）}
\end{gathered}" width="557" height="127"></p>



### 4.3 拟合优度、信息准则与整体显著性（★★★）

| 指标 | 公式 | 用途 |
| --- | --- | --- |
| 调整 R² | <img class="fml" src="/formulas/a12a2c7c96bed7.png" alt="\bar{R}^{2}= 1- \frac{(1- R^{2})(n- 1)}{n- k- 1}" width="160" height="36"> | 惩罚加变量；**可能为负**；可比较同被解释变量模型 |
| 整体 F | <img class="fml" src="/formulas/6545ee7109ef9b.png" alt="F= \frac{\frac{R^{2}}{k}}{\frac{1- R^{2}}{n- k- 1}} \sim F(k, n- k- 1)" width="225" height="48"> | 检验 H0: <img class="fml" src="/formulas/90a00f37b08466.png" alt="\beta_{1}= \cdots=\beta_{k}=0" width="143" height="34"> |
| AIC / SC(BIC) | <img class="fml" src="/formulas/06d749325c619c.png" alt="\ln\left(\frac{SSE}{n}\right)+ \frac{2(k+1)}{n}" width="137" height="34"> / <img class="fml" src="/formulas/daa49fa88ed0d4.png" alt="\cdots+ \frac{(k+1)\ln(n)}{n}" width="117" height="34"> | 越小越好；SC 对变量个数惩罚更重 |
| 约束 F | <img class="fml" src="/formulas/94933e7c8323dc.png" alt="\frac{\frac{SSE_{r}- SSE_{u}}{q}}{\frac{SSE_{u}}{n- k- 1}} \sim F(q, n- k- 1)" width="212" height="46"> | q 个线性约束的联合检验 |

**三大检验原理**（大样本渐近等价，小样本可能不同）：`Wald`（只估无约束模型，看约束离 0 多远）、`LM / 得分检验`（只估约束模型，看得分是否接近 0，<img class="fml" src="/formulas/4a319ab61604c8.png" alt="LM= nR^{2}_{aux}" width="108" height="34">）、`LR`（两者都估，比较似然值 <img class="fml" src="/formulas/c33a2248525c71.png" alt="2(lnL_{u}- lnL_{r})" width="124" height="34">），三者均渐近 <img class="fml" src="/formulas/5a62ee3d300fcd.png" alt="\sim \chi^{2}(q)" width="66" height="34">。一般 `Wald > LR > LM`。

::: tip 工作示例 · 约束 F 检验与调整 R²
无约束模型 <img class="fml" src="/formulas/f1f5d2ecd8bd62.png" alt="n=30, k=3, R^{2}_{u}=0.86" width="195" height="34">；施加 `q=2` 个约束后 <img class="fml" src="/formulas/a6caf8f5394f93.png" alt="R^{2}_{r}=0.62" width="84" height="34">。



<p class="fml-block"><img class="fml" src="/formulas/f07666cf9db91e.png" alt="\begin{gathered}
F= \frac{\frac{0.86- 0.62}{2}}{\frac{1- 0.86}{30- 3- 1}} \\
= \frac{0.12}{\frac{0.14}{26}}= \frac{0.12}{0.0053846}= 22.29 \\
F_{0}._{05}(2,26) \approx 3.37 \to \; \text{拒绝约束，说明被排除的两个变量联合显著} \\
\bar{R}^{2}= 1- \frac{(1- 0.86) \times 29}{26}= 1- 0.1562= 0.8438 \\
\text{整体} \; F= \frac{\frac{0.86}{3}}{\frac{0.14}{26}}= 53.24&gt; F_{0}._{05}(3,26) \approx 2.98 \to \; \text{方程整体显著}
\end{gathered}" width="520" height="229"></p>


注意：单个 t 都不显著但整体 F 显著，常是**多重共线性**的信号（第 5 章）。
:::

### 4.4 虚拟变量与函数形式（★★★）

| 设定 | 模型 | 解释 |
| --- | --- | --- |
| 截距虚拟变量 | <img class="fml" src="/formulas/afb13f02a4d375.png" alt="Y= \beta_{0}+ \delta D+ \beta_{1}X+ u" width="195" height="34"> | `D=1` 组相对基准组截距差 δ |
| 斜率虚拟变量（交互） | <img class="fml" src="/formulas/831fabe4f095e1.png" alt="Y= \beta_{0}+ \beta_{1}X+ \delta(D \cdot X)+ u" width="238" height="34"> | 两组斜率差 δ |
| 多重类别 | m 个类别放 <img class="fml" src="/formulas/5666b1e92fb9aa.png" alt="m- 1" width="54" height="34"> 个虚拟变量 | 全放且含截距 ⇒ **虚拟变量陷阱**（完全共线） |
| 结构变动 | Chow 检验 = 约束 F 检验 | 检验两组所有系数是否相同 |
| 线性-对数 | <img class="fml" src="/formulas/9a206adfa9a892.png" alt="Y= \beta_{0}+ \beta_{1}lnX" width="134" height="34"> | X 上升 1% → Y 变动约 <img class="fml" src="/formulas/0820fef3b28f17.png" alt="\beta_{1}/100" width="60" height="33">（即 <img class="fml" src="/formulas/9991ce2b491eef.png" alt="0.01\beta_{1}" width="56" height="33">）单位 |
| 对数-线性 | <img class="fml" src="/formulas/abb3a9cf600ca7.png" alt="lnY= \beta_{0}+ \beta_{1}X" width="134" height="34"> | X 上升 1 单位 → Y 变动约 <img class="fml" src="/formulas/e3dbf2512bcbb0.png" alt="100\beta_{1}\%" width="66" height="34"> |
| **双对数** | <img class="fml" src="/formulas/c87573eff0b199.png" alt="lnY= \beta_{0}+ \beta_{1}lnX" width="150" height="34"> | <img class="fml" src="/formulas/dc60979297b187.png" alt="\beta_{1}" width="25" height="34"> 直接是**弹性**（最常用） |
| 多项式 / 交互 | <img class="fml" src="/formulas/0938cbc25d8e27.png" alt="Y= \beta_{0}+\beta_{1}X+\beta_{2}X^{2}" width="180" height="34"> | 边际效应 <img class="fml" src="/formulas/ce1975103dffde.png" alt="\beta_{1}+2\beta_{2}X" width="88" height="34"> 随 X 变化 |

![多元回归、偏效应与虚拟变量](/econ/econ-multiple.svg)

::: danger 易错 · 多元回归
- 「控制其它变量不变」是**统计上的偏效应**，不代表现实中可以只动一个变量（变量间往往联动）。
- <img class="fml" src="/formulas/1a6e4adc329ad4.png" alt="\hat{\beta}_{j}" width="24" height="34"> 的方差随其它解释变量对 `X_j` 的解释力上升而变大：<img class="fml" src="/formulas/d069de04c0dc15.png" alt="\operatorname{Var}(\hat{\beta}_{j})= \sigma^{2}/[Sxx_{j}(1- R^{2}_{j})]" width="232" height="34">，这就是多重共线性的数学根源。
- 加控制变量要警惕**坏控制（bad control）**：控制受处理影响的变量会阻断因果路径（如估计教育对工资影响时控制「职业」）。
- 对数变换要求变量为正；`lnY` 模型的 <img class="fml" src="/formulas/b5f2662fd9704d.png" alt="R^{2}" width="27" height="33"> 与 `Y` 模型的 <img class="fml" src="/formulas/b5f2662fd9704d.png" alt="R^{2}" width="27" height="33"> **不可直接比较**。
- 交互项显著时，主效应系数只表示「另一变量为 0 时」的效应，别当成平均效应。
:::

::: tip 补充考点 · Chow 检验的完整操作步骤
检验两个子样本（如改革前/后）的回归系数是否发生结构性变化：
① 分别对子样本 1（n1）、子样本 2（n2）与合并样本回归，得 `SSE1、SSE2、SSE_p`（p = pooled）；
② <img class="fml" src="/formulas/4d1e35164cbd96.png" alt="F= \frac{\frac{SSE_{p}-(SSE_{1}+SSE_{2})}{k+1}}{\frac{SSE_{1}+SSE_{2}}{n_{1}+n_{2}- 2(k+1)}} \sim F(k+1, n_{1}+n_{2}- 2k- 2)" width="375" height="51">，<img class="fml" src="/formulas/99f3bf89b9a31d.png" alt="q = k+1" width="80" height="33">（所有系数含截距）；
③ F 大于临界值 ⇒ 结构发生变化，应分段建模或加虚拟变量交互项。
**注意**：任一子样本观测数少于待估参数个数时 Chow 检验失效，改用**虚拟变量法**（D 与各变量交互）等价检验；它本质就是 4.3 节约束 F 检验的特例。
:::

### 4.5 残差几何与 <img class="fml" src="/formulas/f8c1c1ebd87724.png" alt="Frisch- Waugh- Lovell" width="214" height="34"> 定理



<p class="fml-block"><img class="fml" src="/formulas/f1cf52ff3dd15e.png" alt="\begin{gathered}
\text{帽子矩阵} \; H= X(X&#x27;X)^{-1}X&#x27; \; \text{拟合值} \; \text{ŷ = Hy} \\
\text{残差制造者} \; M= I- H \; \text{残差} \; \text{e = My = Mu} \\
\text{性质：} \; \text{H} \; \text{、} \; \text{M} \; \text{对称幂等（} \; H^{2}=H, M^{2}=M \; \text{），} \; \text{HM=0} \; \text{，} \; \text{MX=0} \; \text{，} \; \text{rank(H)=k+1} \\
\text{SSE = e′e = u′Mu} \; \text{；} \; E(SSE)= \sigma^{2} \cdot tr(M)= \sigma^{2}(n- k- 1) \to \hat{\sigma}^{2}=\frac{SSE}{n- k- 1} \; \text{无偏}
\end{gathered}" width="669" height="128"></p>


**FWL 定理**：多元回归 <img class="fml" src="/formulas/73f151514ade90.png" alt="y= X_{1}\beta_{1}+ X_{2}\beta_{2}+ u" width="172" height="33"> 中


<p class="fml-block"><img class="fml" src="/formulas/0ae3e1ae23c284.png" alt="\hat{\beta}_{1}=(X_{1}&#x27;M_{2}X_{1})^{-1}X_{1}&#x27;M_{2}y \; \text{，其中} \; M_{2}= I- X_{2}(X_{2}&#x27;X_{2})^{-1}X_{2}&#x27;" width="464" height="33"></p>


即「先用 y 与 X1 分别对 X2 回归取残差，再用两组残差做简单回归」。这解释了：
- 偏回归系数为何是「**剔除其它变量线性影响后**」的净效应；
- 固定效应（去个体均值）为何等价于加个体虚拟变量；
- 加控制变量后系数变化，本质是 X1 被「净化」了。

### 4.6 函数形式、边际效应与转折点

| 模型 | 系数含义 | 边际效应 |
| --- | --- | --- |
| <img class="fml" src="/formulas/2c9be2a0271277.png" alt="Y= \beta_{0}+\beta_{1}X" width="118" height="33"> | 绝对变化 | <img class="fml" src="/formulas/dc60979297b187.png" alt="\beta_{1}" width="25" height="34">（常数） |
| <img class="fml" src="/formulas/43c501106db5a9.png" alt="lnY= \beta_{0}+\beta_{1}X" width="134" height="33"> | X 增 1 单位 → Y 约变 <img class="fml" src="/formulas/e3dbf2512bcbb0.png" alt="100\beta_{1}\%" width="66" height="34"> | <img class="fml" src="/formulas/931329835d6557.png" alt="\beta_{1} \cdot Y" width="51" height="33">（随 Y 变） |
| <img class="fml" src="/formulas/fbc40ad75c8661.png" alt="Y= \beta_{0}+\beta_{1}lnX" width="134" height="33"> | X 增 1% → Y 变约 <img class="fml" src="/formulas/0820fef3b28f17.png" alt="\beta_{1}/100" width="60" height="33"> 单位 | <img class="fml" src="/formulas/3c92b6a065245e.png" alt="\beta_{1}/X" width="49" height="33"> |
| <img class="fml" src="/formulas/44884b24257143.png" alt="lnY= \beta_{0}+\beta_{1}lnX" width="150" height="33"> | **弹性** | <img class="fml" src="/formulas/dee77d21376101.png" alt="\beta_{1}\cdot Y/X" width="77" height="33"> |
| <img class="fml" src="/formulas/0938cbc25d8e27.png" alt="Y= \beta_{0}+\beta_{1}X+\beta_{2}X^{2}" width="180" height="34"> | 二次（U 型/倒 U 型） | <img class="fml" src="/formulas/ce1975103dffde.png" alt="\beta_{1}+2\beta_{2}X" width="88" height="34"> |

::: tip 工作示例 · 倒 U 型转折点（环境库兹涅茨曲线、经验-工资曲线常用）
估计得 <img class="fml" src="/formulas/772cb92306dd21.png" alt="\hat{Y}= 10+ 2X- 0.1X^{2}" width="177" height="34">：


<p class="fml-block"><img class="fml" src="/formulas/4b487fde6baf3a.png" alt="\begin{gathered}
\text{边际效应} \; \frac{dY}{dX}= 2- 0.2X \\
\text{令其为} \; 0 \to \; \text{转折点} \; X*= \frac{2}{0.2}= 10 \\
\text{X&lt;10} \; \text{时正效应，} \; \text{X&gt;10} \; \text{时负效应（倒} \; \text{U} \; \text{型）}
\end{gathered}" width="368" height="113"></p>


**报告要点**：不能只报 <img class="fml" src="/formulas/08b8744eebec64.png" alt="\beta_{2}" width="24" height="34"> 显著为负就说存在倒 U 型，还须检验转折点是否落在**样本数据支持区间**内（Lind-Mehlum 检验），并检查两端区间是否都有足够数据，否则可能只是单调凹曲线的一段。
:::

---

## 第 5 章 模型的建立与估计中的问题及对策

本章是全课程的核心：**OLS 的优良性质依赖一组假定，实践中的主要工作就是检验假定并修正**。

![五大问题诊断流程](/econ/econ-diagnostics.svg)

### 5.1 误设定（Misspecification）（★★★）

| 错误类型 | 后果 | 检验 / 对策 |
| --- | --- | --- |
| **遗漏相关变量** | 系数**有偏且不一致**（除非遗漏变量与已含变量不相关） | 理论分析、RESET 检验、加入代理变量 / 固定效应 / IV |
| **包含无关变量** | 系数仍无偏一致，但**方差变大**（效率损失） | t 检验、信息准则；不必为了「显著」硬删 |
| 错误的函数形式 | 系数与预测都有偏 | 残差图、RESET、Box-Cox、加平方项/交互项 |
| 测量误差 | 解释变量测量误差 ⇒ **衰减偏误（attenuation）**，系数被压向 0 | 工具变量、多重指标、验证数据 |
| 样本选择 / 同时性 | 选择性偏差、内生性 | Heckman 两阶段、IV |

**Ramsey RESET 检验**：把拟合值的幂 <img class="fml" src="/formulas/85f9336c292ca2.png" alt="\hat{Y}^{2}, \hat{Y}^{3}" width="58" height="34"> 作为附加回归元做 F 检验；显著即提示函数形式误设定。

::: danger 易错 · 误设定与 R²
「加变量让 R² 上升」不能证明模型更好——R² 单调不减，无关变量也会让它上升。判断应看调整 R²、AIC/SC、系数显著性与**理论依据**；反过来，为了得到想要的系数符号而删掉理论上重要的变量，会造成遗漏变量偏误。
:::

### 5.2 多重共线性（Multicollinearity）（★★★）

**完全共线** ⇒ `X′X` 不可逆，OLS 无法计算；**高度（不完全）共线**可估计，但：
① 系数方差与标准误**膨胀** → t 值小、个别不显著而整体 F 显著；
② 系数对样本与设定极敏感、符号可能反常；
③ **预测**（在共线模式继续成立的范围内）仍可可靠。

| 诊断 | 判据 |
| --- | --- |
| 相关系数矩阵 | 两解释变量 `|r| > 0.8` 提示（但无法发现多变量线性组合） |
| **VIF** | <img class="fml" src="/formulas/7d519cb5ca9add.png" alt="VIF_{j}= \frac{1}{1- R^{2}_{j}}" width="108" height="40">，<img class="fml" src="/formulas/1692267feb4cf9.png" alt="R^{2}_{j}" width="28" height="34"> 为 `X_j` 对其余解释变量回归的决定系数；`VIF>10` 通常认为严重 |
| 容忍度 | <img class="fml" src="/formulas/78eb8769740f83.png" alt="Tol= \frac{1}{VIF}" width="88" height="34"> |
| 条件数 / 特征值 | 条件数 > 30 提示严重共线 |

::: tip 工作示例 · VIF 手算
把 <img class="fml" src="/formulas/318fee4a66121c.png" alt="X_{1}" width="28" height="34"> 对其余解释变量做辅助回归得 <img class="fml" src="/formulas/3cb1b87d85a4f6.png" alt="R^{2}_{1}= 0.90" width="84" height="34">，则
<img class="fml" src="/formulas/7d47b3d61a1bed.png" alt="VIF_{1}= \frac{1}{1- 0.90}= 10" width="157" height="34">，即 <img class="fml" src="/formulas/81a94d8daf67c2.png" alt="\operatorname{Var}(\hat{\beta}_{1})" width="67" height="34"> 是**无共线时的 10 倍**（标准误是 <img class="fml" src="/formulas/a6227a1c6dda30.png" alt="\sqrt{10} \approx 3.16" width="95" height="34"> 倍）。
对照：<img class="fml" src="/formulas/f2c6a9e5b9e204.png" alt="R^{2}_{j}= 0.8 \to VIF=5" width="173" height="34">；<img class="fml" src="/formulas/1cf08a7ebf491d.png" alt="0.95 \to 20" width="84" height="34">；<img class="fml" src="/formulas/45e504b28695bf.png" alt="0.99 \to 100" width="94" height="34">。
**补救**：① 增加样本或获取更多信息；② 删去冗余变量（须有理论依据）；③ 变量变换（差分、标准化、取比值）；④ 合并成指数/主成分；⑤ 用有偏估计（岭回归、LASSO）预测；⑥ 若研究目标是**总效应**，直接检验线性组合而不纠结单个系数。
:::

### 5.3 异方差性（Heteroscedasticity）（★★★）

<img class="fml" src="/formulas/6e3acc417aeb34.png" alt="\operatorname{Var}(u_{i}|X)= \sigma_{i}^{2}" width="128" height="34"> 非常数（横截面数据常见，如收入越高消费波动越大）。

| 后果 | 说明 |
| --- | --- |
| 系数 | **仍无偏、一致**（只要 `E(u|X)=0`） |
| 有效性 | 不再 BLUE |
| 方差估计 | <img class="fml" src="/formulas/42a6e557a8efbf.png" alt="\sigma^{2}(X&#x27;X)^{-1}" width="93" height="34"> **有偏** → 标准误、t、F、置信区间全部失效 |
| 预测区间 | 失效 |

| 检验 | 做法 | 统计量 |
| --- | --- | --- |
| 图示法 | 画 <img class="fml" src="/formulas/2527f6eb8bcd70.png" alt="e_{i}^{2}" width="22" height="34"> 或 `|e_i|` 对 `Ŷ_i` / 某解释变量的散点 | 漏斗形、扇形提示异方差 |
| Park / Glejser | <img class="fml" src="/formulas/96a70df4d7927c.png" alt="\ln e^{2}" width="40" height="34"> 或 `|e|` 对变量回归 | t 检验 |
| Goldfeld-Quandt | 按可疑变量排序、去中间 c 个、分别回归两段 | <img class="fml" src="/formulas/3c2dc636a4ce29.png" alt="F= \frac{SSE_{2}}{SSE_{1}}" width="81" height="35"> |
| **Breusch-Pagan / Godfrey** | <img class="fml" src="/formulas/d9e369bc9dbe6d.png" alt="e^{2}" width="22" height="34"> 对全部解释变量辅助回归 | <img class="fml" src="/formulas/e78e6726a357a5.png" alt="LM= n \cdot R^{2}_{aux} \sim \chi^{2}(k)" width="187" height="34"> |
| **White 检验** | 辅助回归含解释变量、平方项与交叉项 | `LM = n·R²_aux ∼ χ²(自由度)`，还能查设定误差 |

::: tip 工作示例 · BP / White 的 LM 检验
`n = 50`，把残差平方对解释变量做辅助回归得 <img class="fml" src="/formulas/dcef2caeb71b83.png" alt="R^{2}_{aux}= 0.12" width="98" height="34">，含 2 个约束：


<p class="fml-block"><img class="fml" src="/formulas/8bc38b9765dcb1.png" alt="\begin{gathered}
LM= n \times R^{2}_{aux}= 50 \times 0.12= 6.00 \\
\chi^{2}_{0}._{05}(2)= 5.99 \to 6.00&gt; 5.99 \; \text{，在} \; \text{5\%} \; \text{水平拒绝同方差（临界，需谨慎下结论）}
\end{gathered}" width="633" height="58"></p>


再如 <img class="fml" src="/formulas/11ec82bf7172f9.png" alt="n=100, R^{2}_{aux}=0.08, df=3" width="228" height="34"> → <img class="fml" src="/formulas/0caea77ad02758.png" alt="LM=8.00&gt; \chi^{2}_{0}._{05}(3)=7.81" width="233" height="34"> → 拒绝。
**注意**：White 检验的辅助回归项数随 k 快速增长，小样本自由度可能不足；此时用简化版（只对 `Ŷ` 与 <img class="fml" src="/formulas/03236d269b2189.png" alt="\hat{Y}^{2}" width="28" height="34"> 回归）。
:::

![异方差的图形与修正](/econ/econ-hetero.svg)

| 修正方法 | 做法 | 适用 |
| --- | --- | --- |
| **异方差稳健标准误**（White / HC0–HC3） | 系数不变，只换标准误 | **现代实证首选**：不需知道异方差具体形式，大样本有效 |
| **WLS 加权最小二乘** | 若 <img class="fml" src="/formulas/cefeb053ba640f.png" alt="\sigma_{i}^{2}= \sigma^{2}w_{i}" width="85" height="34">，两边除以 <img class="fml" src="/formulas/2176583523f5cc.png" alt="\sqrt{w}_{i}" width="40" height="34"> 后 OLS | 已知/可估计方差形式时更有效 |
| FGLS | 先用残差估计 <img class="fml" src="/formulas/7b46743688cd8e.png" alt="\sigma_{i}^{2}" width="25" height="34"> 再 WLS | 可行 GLS |
| 变量变换 | 取对数、用人均/比率形式 | 常能同时缓解异方差与偏态 |

::: danger 易错 · 异方差
- 异方差**不使系数有偏**，只影响**方差估计与推断**；自相关同理。别答成「系数有偏」。
- 稳健标准误**不能**修复模型设定错误或内生性，只修标准误。
- 小样本下 HC0 偏乐观，常用 HC1（Stata `robust` 默认）或 HC3。
- 面板/分组数据还存在**组内相关**，要用**聚类稳健标准误**（cluster-robust），仅用异方差稳健仍会低估标准误。
:::

### 5.4 自相关（Autocorrelation）（★★★）

<img class="fml" src="/formulas/063de6622aa39e.png" alt="\operatorname{Cov}(u_{t}, u_{s})= 0" width="126" height="34">，时间序列常见。最常用模型 **AR(1)**：<img class="fml" src="/formulas/119c8ee915b13f.png" alt="u_{t}= \rho u_{t- 1}+ \epsilon_{t}" width="122" height="34">，<img class="fml" src="/formulas/bcc15622dc22e5.png" alt="\epsilon_{t}" width="19" height="34"> 为白噪声。

| 后果 | 系数仍无偏一致（若解释变量严格外生）；**标准误被低估、t 值虚高**；OLS 不再有效；预测失效 |
| --- | --- |

| 检验 | 判据与局限 |
| --- | --- |
| 残差图 / 自相关图 | 残差呈连续正/负串 |
| **DW 检验** | <img class="fml" src="/formulas/e79b012c354507.png" alt="d= \frac{\sum(e_{t}- e_{t- 1})^{2}}{\sum e_{t}^{2}} \approx 2(1- \hat{\rho})" width="201" height="39">；<img class="fml" src="/formulas/f250a21a772e0e.png" alt="d \approx 2" width="49" height="34"> 无一阶自相关，<img class="fml" src="/formulas/fbe6b0db366284.png" alt="d \to 0" width="52" height="34"> 正相关，<img class="fml" src="/formulas/8f41259f6eb7e4.png" alt="d \to 4" width="52" height="34"> 负相关 |
| **DW 的硬限制** | ① 只检一阶 AR(1)；② **解释变量不能含被解释变量滞后项**（否则用 Durbin h / LM）；③ 需含截距；④ 有不确定区（d_L、d_U）不能判；⑤ 不能有缺失观测 |
| Breusch-Godfrey LM | <img class="fml" src="/formulas/0dcf5184dff81a.png" alt="(n- p)R^{2}_{aux} \sim \chi^{2}(p)" width="162" height="34">，可检高阶、允许滞后被解释变量，**现代首选** |

![自相关与 DW 判据](/econ/econ-autocorr.svg)

::: tip 工作示例 · DW 手算
沿用第 3 章例题残差 <img class="fml" src="/formulas/30b753124eadf8.png" alt="e=[0, 0.3,- 0.4,- 0.1, 0.2]" width="209" height="34">，`SSE = 0.30`：


<p class="fml-block"><img class="fml" src="/formulas/ba7e6cac7a53b6.png" alt="\begin{gathered}
\sum(e_{t}- e_{t- 1})^{2}= 0.3^{2}+(- 0.7)^{2}+ 0.3^{2}+ 0.3^{2} \\
\text{= 0.09 + 0.49 + 0.09 + 0.09 = 0.76} \\
d= \frac{0.76}{0.30}= 2.533 \\
\hat{\rho}= 1- \frac{d}{2}=- 0.267 \to \; \text{轻微负一阶自相关（} \; \text{n=5} \; \text{仅演示算法，实际不可据此判断）}
\end{gathered}" width="667" height="147"></p>


对照：<img class="fml" src="/formulas/5b1cdccbd375be.png" alt="d=0.8 \to \hat{\rho}=0.60" width="155" height="34">（明显正自相关）；<img class="fml" src="/formulas/d60bfed7bb9404.png" alt="d=1.5 \to 0.25" width="122" height="34">；<img class="fml" src="/formulas/fdcc4f8c4d5cd0.png" alt="d=2.0 \to 0" width="100" height="34">；<img class="fml" src="/formulas/236483faedfad4.png" alt="d=2.6 \to- 0.30" width="136" height="34">；<img class="fml" src="/formulas/0b1296ba8a04da.png" alt="d=3.4 \to- 0.70" width="137" height="34">。
:::

| 修正 | 做法 |
| --- | --- |
| **广义差分 / Cochrane-Orcutt** | 估计 ρ̂ 后做 <img class="fml" src="/formulas/c2c57fa6545179.png" alt="Y_{t}- \hat{\rho}Y_{t- 1}" width="85" height="34"> 对 <img class="fml" src="/formulas/3b91f2cfa95d54.png" alt="X_{t}- \hat{\rho}X_{t- 1}" width="95" height="34"> 回归，迭代至收敛；第一观测用 Prais-Winsten 补回 |
| **Newey-West (HAC)** | 系数不变，标准误对异方差 + 自相关都稳健（不需设定 AR 阶数） |
| FGLS / 加入滞后项 | 若自相关源于**模型动态设定不足**，应补上滞后变量而非只修误差 |
| 差分 / 取增长率 | 注意会改变经济含义并可能丢失长期信息 |

::: danger 易错 · 自相关与「伪自相关」
DW 显著偏低未必是误差自相关，也可能是**遗漏了滞后变量或函数形式错**（「伪自相关」）。先检查模型设定，再决定是否做 GLS；否则会把设定误差硬塞进误差项。
:::

::: tip 补充考点 · DW 检验的五区判定规则
给定样本量 n 与解释变量个数 k，查表得下临界值 `d_L` 与上临界值 `d_U`（如 n=30、k=2、5% 时约 `d_L=1.28, d_U=1.57`）：
`0 < d < d_L` ⇒ 存在**正自相关**（拒绝）；<img class="fml" src="/formulas/5bbcd958a66c8a.png" alt="d_{L} \le d \le d_{U}" width="102" height="34"> ⇒ **不能判定**；<img class="fml" src="/formulas/d9677c7fa9f8e3.png" alt="d_{U}&lt; d&lt; 4- d_{U}" width="135" height="34"> ⇒ 无（一阶）自相关（不拒绝）；<img class="fml" src="/formulas/a4a54fc699ad31.png" alt="4- d_{U} \le d \le 4- d_{L}" width="164" height="34"> ⇒ 不能判定；<img class="fml" src="/formulas/26ef09cc119f28.png" alt="4- d_{L}&lt; d&lt; 4" width="122" height="34"> ⇒ 存在**负自相关**。
两个「不能判定区」是 DW 检验的固有缺陷，此时应改用 Breusch-Godfrey LM 检验（无不确定区、可检高阶）。
:::

### 5.5 随机解释变量与内生性（★★★）

<img class="fml" src="/formulas/699ce9c2333208.png" alt="\operatorname{Cov}(X, u)\ne 0" width="119" height="33">（内生性）是 OLS 最致命的问题：**有偏且不一致**（增大样本也不能救）。三大来源：
① **遗漏变量**（与 X 相关的因素被留在 u 中）；
② **联立性 / 反向因果**（Y 也影响 X）；
③ **测量误差**（X 的经典测量误差使系数衰减偏误）。

**工具变量 IV / 两阶段最小二乘 2SLS**：找一个 `Z` 满足
- **相关性**（<img class="fml" src="/formulas/36f6dfcfe2a4e3.png" alt="\operatorname{Cov}(Z,X)\ne 0" width="123" height="33">，第一阶段足够强）；
- **外生性 / 排他性**（`Cov(Z,u)=0`，Z 只通过 X 影响 Y）。



<p class="fml-block"><img class="fml" src="/formulas/efccefa4bf8b49.png" alt="\begin{gathered}
\text{第一阶段：} \; X= \pi_{0}+ \pi_{1}Z+ \; \text{其它外生变量} \; + v \to \; \text{得} \; \text{X̂} \\
\text{第二阶段：} \; Y= \beta_{0}+ \beta_{1}\hat{X}+ \cdots+ u \to \; \text{得} \; \text{2SLS} \; \text{估计}
\end{gathered}" width="450" height="61"></p>



| 诊断 / 概念 | 结论 |
| --- | --- |
| 恰好识别 / 过度识别 | 工具数 = / > 内生变量数 |
| 弱工具变量 | 第一阶段 F < 10（经验规则）<img class="fml" src="/formulas/e667a8be113ba1.png" alt="\Rightarrow" width="24" height="34"> 且 Wald 检验失真；用 Kleibergen-Paap / Cragg-Donald 统计量 |
| 过度识别检验 | Sargan / Hansen J：检验「所有工具都外生」，不拒绝才支持工具有效性 |
| 内生性检验 | Durbin-Wu-Hausman：比较 OLS 与 IV，显著则确有内生性 |
| LATE | 异质效应下 IV 识别的是「被工具撬动的那群人（compliers）」的局部平均处理效应，不是全样本 ATE |

::: tip 现代因果推断工具箱
在工具变量法之外，现代实证研究还须掌握：
- **潜在结果框架（RCM）**：<img class="fml" src="/formulas/e0871db986809f.png" alt="\tau_{i}= Y_{i}(1)- Y_{i}(0)" width="143" height="34">，根本问题是同一对象不能同时观测两种结果；识别靠随机化或可忽略性假设。
- **DID 双重差分**：处理组前后变化减去对照组前后变化，**平行趋势假定**是关键；用事件研究图检验预趋势；双向固定效应（TWFE）在交错处理时可能偏误，需 Callaway-Sant'Anna / Sun-Abraham 等稳健估计量。
- **RDD 断点回归**：断点附近局部随机化，识别局部因果效应。
- **合成控制、匹配、倾向得分**：构造可比对照组。
- **标准误**：按处理分配层级聚类；DID 常用「处理组层面聚类 + 小样本 wild bootstrap」。
:::

### 5.6 五大问题速查对照表

| 问题 | 系数无偏? | 方差估计? | 主要检验 | 首选对策 |
| --- | --- | --- | --- | --- |
| 遗漏变量 / 内生性 | **否（有偏且不一致）** | 失效 | RESET、DWH、理论分析 | 加控制/固定效应、IV/2SLS、实验或准实验 |
| 多重共线性 | 是 | 变大（t 小） | VIF、条件数 | 增样本、删冗余、变换、岭回归 |
| 异方差 | 是 | 失效 | BP/Godfrey、White、GQ | **稳健标准误**、WLS/FGLS |
| 自相关 | 是（严格外生下） | 失效 | DW、BG-LM | **HAC/Newey-West**、Cochrane-Orcutt |
| 误设定函数形式 | 否 | 失效 | RESET、残差图 | 加平方项/交互、Box-Cox |

### 5.7 稳健标准误、衰减偏误与双重差分



<p class="fml-block"><img class="fml" src="/formulas/d86536bc436b6b.png" alt="\begin{gathered}
\text{OLS} \; \text{方差（同方差）：} \; \operatorname{Var}(\hat{\beta})= \sigma^{2}(X&#x27;X)^{-1} \\
\text{HC0} \; \text{异方差稳健：} \; \operatorname{Var}(\hat{\beta})=(X&#x27;X)^{-1}[\sum e_{i}^{2} x_{i} x_{i}&#x27;](X&#x27;X)^{-1} \\
\text{HC1} \; \text{（} \; \text{Stata robust} \; \text{默认）：乘} \; \frac{n}{n- k- 1} \; \text{小样本校正} \\
\text{HC3} \; \text{：} \; \text{用} \; \frac{e_{i}^{2}}{(1- h_{i})^{2}} \; \text{，小样本表现最好} \\
\text{聚类稳健：} \; \text{按个体} \; \text{g} \; \text{分组求和} \; \sum_{g}\left(\sum_{i \in g} e_{i} x_{i}\right)\left(\sum_{i \in g} e_{i} x_{i}\right)&#x27;
\end{gathered}" width="461" height="219"></p>



::: tip 工作示例 · 测量误差衰减偏误与 <img class="fml" src="/formulas/e17fc71e34f68d.png" alt="2 \times 2" width="46" height="34">
**衰减偏误**：真实 X 方差 <img class="fml" src="/formulas/de88797aee0f59.png" alt="\sigma^{2}_{x}=9" width="58" height="34">，测量误差方差 <img class="fml" src="/formulas/cebbf9deaf8621.png" alt="\sigma^{2}_{v}=1" width="58" height="34">，则 <img class="fml" src="/formulas/0263d60091e158.png" alt="plim \hat{\beta}= \beta \frac{\cdot 9}{9+1}= 0.9\beta" width="173" height="34">，系数被**压向 0 约 10%**。这与遗漏变量偏误方向不确定不同：经典测量误差一定造成衰减。

**DID 2×2 表**：

| | 政策前 | 政策后 | 变化 |
| --- | --- | --- | --- |
| 处理组 | 10 | 14 | +4 |
| 对照组 | 8 | 10 | +2 |
| 差异 | +2 | +4 | — |



<p class="fml-block"><img class="fml" src="/formulas/2264356ef9a284.png" alt="DID=(14- 10)-(10- 8)= 4- 2= 2" width="323" height="33"></p>


等价于回归 <img class="fml" src="/formulas/52f4c68f7d0906.png" alt="Y= \alpha+ \beta \cdot Treat+ \gamma \cdot Post+ \delta(Treat \times Post)+ u" width="411" height="33"> 中的 <img class="fml" src="/formulas/030b4649142f76.png" alt="\hat{\delta}" width="16" height="33">。成立前提是**平行趋势**（无政策时两组变化相同），必须用政策前多期数据画事件研究图检验；标准误要按处理分配层级聚类。
:::

---

## 第 6 章 动态经济模型

### 6.1 分布滞后与自回归模型（★★★）

经济行为常有**时滞**（投资到产出、政策到效果），需在模型里引入滞后变量。

| 模型 | 形式 | 说明 |
| --- | --- | --- |
| **分布滞后模型** | <img class="fml" src="/formulas/4cd2c1a062189b.png" alt="Y_{t}= \alpha+ \beta_{0}X_{t}+ \beta_{1}X_{t- 1}+ \cdots+ \beta_{s}X_{t-s}+ u_{t}" width="347" height="33"> | 解释变量的现期与多期滞后同时出现 |
| **自回归模型** | <img class="fml" src="/formulas/4e40050387fc20.png" alt="Y_{t}= \alpha+ \beta_{0}X_{t}+ \lambda Y_{t- 1}+ u_{t}" width="219" height="33"> | 含**被解释变量滞后项** |
| 短期乘数 | <img class="fml" src="/formulas/918cb4aaf5f6e2.png" alt="\beta_{0}" width="25" height="34"> | X 当期变动 1 单位对 Y 的当期影响 |
| 延迟乘数 | <img class="fml" src="/formulas/aaa28d910f915d.png" alt="\beta_{1}, \beta_{2}, \cdots" width="78" height="33"> | 各滞后期的额外影响 |
| **长期乘数（长期弹性）** | <img class="fml" src="/formulas/f88144714ab1fd.png" alt="\sum \beta_{i}" width="44" height="33"> | X 永久变动 1 单位后 Y 的总变化 |

直接估计分布滞后会遇到：滞后长度 s 难定、自由度损失、滞后项间**高度共线**。

![分布滞后、自回归与长期乘数](/econ/econ-lag.svg)

### 6.2 阿尔蒙多项式分布滞后（★★）

假设滞后系数 <img class="fml" src="/formulas/46efb263633b7c.png" alt="\beta_{i}" width="22" height="33"> 可由低阶多项式近似：<img class="fml" src="/formulas/c2ac67ee1abb20.png" alt="\beta_{i}= a_{0}+ a_{1}i+ a_{2}i^{2}+ \cdots+ a_{p} i^p(p&lt; s)" width="309" height="33">。把原模型改写为对**构造变量** <img class="fml" src="/formulas/482b57cdbb373c.png" alt="Z_{0t}=\sum X_{t- i}" width="111" height="33">、<img class="fml" src="/formulas/065b88d4f8e437.png" alt="Z_{1t}=\sum i \cdot X_{t- i}" width="129" height="33">、<img class="fml" src="/formulas/20a147bd466d3f.png" alt="Z_{2t}=\sum i^{2} \cdot X_{t- i}" width="137" height="33"> 的回归，估计出 `a_j` 后回代得到各期 <img class="fml" src="/formulas/46efb263633b7c.png" alt="\beta_{i}" width="22" height="33">。
优点：大幅减少待估参数、缓解共线；代价：对多项式阶数与端点约束（常设 <img class="fml" src="/formulas/dad9b658ae2961.png" alt="\beta_{- 1}=\beta_{s+1}=0" width="123" height="33">）敏感。

### 6.3 Koyck 变换、部分调整与适应预期（★★★）

| 模型 | 经济动机 | 变换后的共同形式 |
| --- | --- | --- |
| **Koyck 几何滞后** | <img class="fml" src="/formulas/a08c3e2af541e7.png" alt="\beta_{i}= \beta_{0}\lambda^i, 0&lt;\lambda&lt;1" width="162" height="33">（远期影响几何衰减） | <img class="fml" src="/formulas/b490afb065d6df.png" alt="Y_{t}= \alpha(1- \lambda)+ \beta_{0}X_{t}+ \lambda Y_{t- 1}+ v_{t}" width="273" height="33">，<img class="fml" src="/formulas/4f970fd17767a2.png" alt="v_{t}= u_{t}- \lambda u_{t- 1}" width="124" height="33"> |
| **部分调整 PAM** | 实际调整只完成期望调整的一部分（有调整成本） | 同上形式，长期乘数 <img class="fml" src="/formulas/aae34718f79168.png" alt="= \beta_{0}/(1- \lambda)" width="107" height="33"> |
| **适应预期 AE** | 预期按误差逐步修正 <img class="fml" src="/formulas/1f5c37b90ab90f.png" alt="X^e_{t}- X^e_{t- 1}= \gamma(X_{t}- X^e_{t- 1})" width="214" height="33"> | 同上形式，<img class="fml" src="/formulas/6577dc3ea0000f.png" alt="\lambda= 1- \gamma" width="82" height="33"> |

三者数学形式几乎一样，**经济含义与扰动项结构不同**，不能只凭回归式区分。

::: tip 工作示例 · 长期乘数手算
设部分调整模型估计得 <img class="fml" src="/formulas/2e9eb012bb3502.png" alt="\beta_{0}= 0.5" width="71" height="33">，<img class="fml" src="/formulas/af42b5b61ad6f4.png" alt="\lambda= 0.6" width="64" height="33">（每期完成 60% 的调整）：


<p class="fml-block"><img class="fml" src="/formulas/5a612e79a11e6c.png" alt="\begin{gathered}
\text{短期乘数} \; \text{= 0.5} \\
\text{长期乘数} \; = \beta_{0}/(1- \lambda)= \frac{0.5}{0.4}= 1.25 \\
\text{含义：} \; \text{X} \; \text{永久增加} \; \text{1} \; \text{单位，当期} \; \text{Y} \; \text{只增} \; \text{0.5} \; \text{，但累积最终增} \; \text{1.25} \\
\text{调整速度：} \; \lambda=0.4 \to \; \text{长期乘数} \; \text{0.833} \; \text{；} \; \lambda=0.8 \to 2.50 \; \text{（} \; \lambda \; \text{越大，长期效应越大、调整越慢）} \\
\text{平均滞后} \; \approx \frac{\lambda}{1- \lambda} \; \text{：} \; \lambda=0.6 \to 1.5 \; \text{期}
\end{gathered}" width="763" height="169"></p>


:::

### 6.4 自回归模型的估计问题（★★★）

含 <img class="fml" src="/formulas/6e0c6113102043.png" alt="Y_{t- 1}" width="38" height="34"> 时：
- 若 `u_t` 存在自相关，则 <img class="fml" src="/formulas/6e0c6113102043.png" alt="Y_{t- 1}" width="38" height="34"> 与 `u_t` **相关**（因为 <img class="fml" src="/formulas/6e0c6113102043.png" alt="Y_{t- 1}" width="38" height="34"> 含 <img class="fml" src="/formulas/5da2506fb88180.png" alt="u_{t- 1}" width="39" height="34">）→ OLS **有偏且不一致**；
- **DW 检验失效**（偏向 2，倾向于「检不出」自相关）→ 改用 **Durbin h 检验**（<img class="fml" src="/formulas/05ab42e2f36bce.png" alt="h= \hat{\rho}\sqrt{\frac{n}{1- n \cdot \operatorname{Var}(\hat{\lambda})}} \sim N(0,1)" width="217" height="42">）或 **Breusch-Godfrey LM**；
- 小样本下 <img class="fml" src="/formulas/2eb07f2b5faa23.png" alt="\hat{\lambda}" width="17" height="34"> 有向下偏误（动态面板中即 Nickell 偏误，第 9 章）。

### 6.5 Granger 因果关系检验（★★★）

「X Granger 引起 Y」＝**X 的滞后项对 Y 有增量预测能力**（在控制 Y 自身滞后之后），这是**预测意义上的因果**，不等于哲学/结构意义上的因果。



<p class="fml-block"><img class="fml" src="/formulas/2da1ddca26e5be.png" alt="\begin{gathered}
\text{无约束：} \; Y_{t}= \alpha+ \sum a_{i} Y_{t- i}+ \sum b_{j} X_{t- j}+ u_{t} \to SSE_{u} \\
\text{受约束：} \; \text{Y\_t = α + Σa\_i Y\_{t−i} + u\_t  (H0:} \; \text{全部} \; \text{b\_j = 0) → SSE\_r} \\
F= \frac{\frac{SSE_{r}- SSE_{u}}{q}}{\frac{SSE_{u}}{n- k}} \sim F(q, n- k)
\end{gathered}" width="527" height="122"></p>



::: tip 工作示例 · Granger F 统计量
`SSE_r = 1200`，`SSE_u = 900`，滞后阶 `q=2`，`n=60`，无约束模型参数 `k=5`：


<p class="fml-block"><img class="fml" src="/formulas/e4bc6a3eb570ad.png" alt="\begin{gathered}
F= \frac{\frac{1200- 900}{2}}{\frac{900}{60- 5}}= \frac{150}{16.364}= 9.17 \\
F_{0}._{05}(2,55) \approx 3.17 \to \; \text{拒绝} \; H_{0} \; \text{，} \; \text{X Granger} \; \text{引起} \; \text{Y}
\end{gathered}" width="412" height="84"></p>


**三个前提**：① 变量平稳（非平稳须先差分或做协整/VECM）；② 滞后阶数由 AIC/SC 选，结论可能对阶数敏感；③ 存在共同原因、预期先行、遗漏第三变量时「Granger 因果」会被误读。反向也须检验（Y 是否 Granger 引起 X），可能出现双向反馈。
:::

### 6.6 滞后长度选择（★★）

- **由一般到特殊**：从较大阶数逐步删不显著滞后项，配合 AIC/SC 与残差白噪声检验。
- **由特殊到一般**易犯设定错误；数据驱动逐步删项会扭曲 t 统计量的分布（预检验偏误），结论宜作稳健性报告。
- AIC 倾向选大阶（预测导向），SC/BIC 一致地选真阶（更重的惩罚）。

::: danger 易错 · 动态模型
- Koyck 变换后的扰动项是 MA(1)，与 <img class="fml" src="/formulas/6e0c6113102043.png" alt="Y_{t- 1}" width="38" height="34"> 相关 <img class="fml" src="/formulas/e667a8be113ba1.png" alt="\Rightarrow" width="24" height="34"> 不一致，需用 IV/GMM 或显式建模误差结构。
- 「Granger 因果」≠「真因果」：太阳黑子可能 Granger 引起产出，只反映预测信息。
- 非平稳序列直接做 Granger 检验可能产生伪显著，须先做单位根检验（第 7 章）。
:::

### 6.7 阿尔蒙多项式的构造与滞后阶选择

设滞后长度 `s=4`、多项式阶 `p=2`，令 <img class="fml" src="/formulas/fe6dda3454502a.png" alt="\beta_{i}= a_{0}+ a_{1}i+ a_{2}i^{2}(i=0 \cdots 4)" width="247" height="34">：


<p class="fml-block"><img class="fml" src="/formulas/45d2f480796357.png" alt="\begin{gathered}
Z_{0}t= X_{t}+ X_{t- 1}+ X_{t- 2}+ X_{t- 3}+ X_{t- 4} \\
Z_{1}t= X_{t- 1}+ 2X_{t- 2}+ 3X_{t- 3}+ 4X_{t- 4} \\
Z_{2}t= X_{t- 1}+ 4X_{t- 2}+ 9X_{t- 3}+ 16X_{t- 4} \\
\text{回归} \; Y_{t}= \alpha+ a_{0}Z_{0}t+ a_{1}Z_{1}t+ a_{2}Z_{2}t+ u_{t} \\
\text{回代：} \; \hat{\beta}_{i}= \hat{a}_{0}+ \hat{a}_{1}i+ \hat{a}_{2}i^{2} \; \text{，长期乘数} \; = \sum \hat{\beta}_{i}
\end{gathered}" width="385" height="144"></p>


原来要估 5 个 β，现在只估 3 个 a；端点约束（如 <img class="fml" src="/formulas/1a12fb65327554.png" alt="\beta_{5}=0" width="57" height="34"> 或 <img class="fml" src="/formulas/832f7c8b843e6d.png" alt="\beta_{- 1}=0" width="66" height="34">）可再减 1 个参数，但约束是**先验信息**，设错会系统性扭曲滞后结构。

::: tip 工作示例 · AIC / SC 选阶
`n=100`，两个候选模型：


<p class="fml-block"><img class="fml" src="/formulas/273f6544a47e0d.png" alt="\begin{gathered}
k=3, SSE=180 \to AIC= \ln(1.80)+ \frac{8}{100}= 0.6678 \; \text{；} \; SC= \ln(1.80)+ \frac{4 \cdot \ln(100)}{100}= 0.7720 \\
k=4, SSE=178 \to AIC= \ln(1.78)+ \frac{10}{100}= 0.6766 \; \text{；} \; SC= \ln(1.78)+ \frac{5 \cdot \ln(100)}{100}= 0.8069 \\
\text{两者都选} \; \text{k=3} \; \text{（更简洁的模型）}
\end{gathered}" width="737" height="116"></p>


SC 的惩罚项 `(k+1)ln n` 比 AIC 的 `2(k+1)` 随样本增长更快，因此在临界情形**更倾向小模型**；AIC 以提高预测精度为目标，SC 具有「真模型若在其中则一致选中它」的性质。
:::

---

## 第 7 章 时间序列分析

### 7.1 平稳性与常用过程（★★★）

| 概念 | 定义 |
| --- | --- |
| **严格平稳** | 任意 k 个时点的联合分布不随时间平移而改变 |
| **弱（协方差）平稳** | <img class="fml" src="/formulas/d89438c015df56.png" alt="E(Y_{t})=\mu" width="85" height="34">（常数）、<img class="fml" src="/formulas/0d316486c5cd41.png" alt="\operatorname{Var}(Y_{t})=\sigma^{2}" width="108" height="34">（常数）、<img class="fml" src="/formulas/caae5b88646d8a.png" alt="\operatorname{Cov}(Y_{t},Y_{t- k})=\gamma_{k}" width="149" height="34"> 只依赖间隔 k 而非 t |
| 白噪声 | <img class="fml" src="/formulas/2356131d892fd4.png" alt="E(\epsilon_{t})=0" width="81" height="34">、<img class="fml" src="/formulas/740f8d6c343c53.png" alt="\operatorname{Var}=\sigma^{2}" width="78" height="34">、<img class="fml" src="/formulas/4b1821adbf7762.png" alt="\operatorname{Cov}(\epsilon_{t},\epsilon_{s})=0(t=s)" width="172" height="34"> |
| 随机游走 | <img class="fml" src="/formulas/91786bb7c82a62.png" alt="Y_{t}= Y_{t- 1}+ \epsilon_{t}" width="113" height="34">（无漂移）/ <img class="fml" src="/formulas/c5cfa085c4cacb.png" alt="Y_{t}= \mu+ Y_{t- 1}+ \epsilon_{t}" width="145" height="34">（带漂移）；**非平稳**、`Var` 随 t 线性增长 |
| AR(1) | <img class="fml" src="/formulas/c5f28bb3698830.png" alt="Y_{t}= c+ \phi Y_{t- 1}+ \epsilon_{t}" width="153" height="34">；<img class="fml" src="/formulas/da253f240ad45b.png" alt="\vert \phi\vert &lt;1" width="60" height="34"> 平稳，<img class="fml" src="/formulas/abe859aced2e63.png" alt="\phi=1" width="51" height="34"> 为单位根 |
| MA(q) / ARMA(p,q) | 用过去扰动 / 过去值与扰动的组合刻画序列相关 |
| ARIMA(p,d,q) | 差分 d 次后为 ARMA；`d` 为单整阶数 |

![平稳性、单位根与差分](/econ/econ-stationary.svg)

::: danger 易错 · 平稳性
- 「均值恒定」不够：方差或自协方差随时间变也不平稳（如异方差的金融收益率）。
- 确定性趋势（如 <img class="fml" src="/formulas/57a0d57eaaf0e2.png" alt="Y_{t}= a+ bt+ \epsilon_{t}" width="126" height="34">）**不是**平稳，但**去趋势后**平稳，称**趋势平稳**；与单位根过程的本质区别是：趋势平稳的冲击是暂时的，单位根的冲击**永久**改变水平。
- 伪回归：两个独立的随机游走互相回归，常得到高 R² 与显著 t 值（<img class="fml" src="/formulas/e849a53ff0c551.png" alt="Granger- Newbold" width="167" height="34"> 发现），实际上毫无关系。判别信号：<img class="fml" src="/formulas/d58e2c62910be4.png" alt="R^{2}&gt; DW" width="86" height="34">、残差高度自相关。
:::

### 7.2 单位根检验（★★★）



<p class="fml-block"><img class="fml" src="/formulas/eef9c4e82e323e.png" alt="\begin{gathered}
\text{DF} \; \text{检验：} \; \Delta Y_{t}=(\rho- 1)Y_{t- 1}+ \epsilon_{t} \; \text{，检验} \; H_{0}: \rho=1 \; \text{（有单位根，非平稳）} \\
\text{ADF} \; \text{：加入滞后差分项} \; \Delta Y_{t- i} \; \text{以消除残差自相关} \\
\Delta Y_{t}= \alpha+ \beta t+ \gamma Y_{t- 1}+ \sum \delta_{i}\Delta Y_{t- i}+ \epsilon_{t} \; \text{，} \; H_{0}: \gamma= 0
\end{gathered}" width="596" height="91"></p>


**关键点**：检验统计量在原假设下**不服从标准 t 分布**，必须用 **DF / MacKinnon 临界值**（更负，如 5% 约 <img class="fml" src="/formulas/010cc9000c9895.png" alt="- 2.86" width="53" height="34">（含截距）、<img class="fml" src="/formulas/58b6af4ef0fd95.png" alt="- 3.41" width="52" height="34">（含截距和趋势））；`t` 值要**比临界值更负**才能拒绝非平稳。

| 检验 | 原假设 | 备注 |
| --- | --- | --- |
| ADF | 有单位根 | 最常用；滞后阶数由 AIC/SC 选 |
| PP (Phillips-Perron) | 有单位根 | 非参数修正自相关与异方差 |
| KPSS | **平稳**（与 ADF 相反） | 常与 ADF 联合使用做确认 |
| ADF-GLS / ERS | 有单位根 | 功效更高 |
| 结构突变单位根 | 有单位根（允许断点） | Perron、Zivot-Andrews；普通 ADF 遇结构突变易误判 |

**单整**：<img class="fml" src="/formulas/80c4adbffa1f88.png" alt="Y_{t} \sim I(d)" width="79" height="34"> 表示差分 d 次后平稳；`I(0)` 平稳，`I(1)` 一阶单整（多数宏观总量），`I(2)` 少见。

### 7.3 协整与误差修正模型（★★★）

**协整**：若 <img class="fml" src="/formulas/14c405b122287d.png" alt="Y_{t} \sim I(1)" width="79" height="34">、<img class="fml" src="/formulas/7a83799f14e076.png" alt="X_{t} \sim I(1)" width="83" height="34">，但存在 β 使 <img class="fml" src="/formulas/296c18e6cf1b35.png" alt="u_{t}= Y_{t}- \beta_{0}- \beta_{1}X_{t} \sim I(0)" width="216" height="34">，则二者协整，β 称**协整向量**，代表变量间的**长期均衡关系**。

**Engle-Granger 两步法**：


<p class="fml-block"><img class="fml" src="/formulas/0a32342c85ee7f.png" alt="\begin{gathered}
\text{(1)} \; \text{用} \; \text{OLS} \; \text{估计长期静态回归} \; Y_{t}= \beta_{0}+ \beta_{1}X_{t}+ u_{t} \; \text{，取残差} \; \text{û\_t} \\
\text{(2)} \; \text{对} \; \text{û\_t} \; \text{做} \; \text{ADF} \; \text{检验（不含趋势，临界值为} \; \text{AEG/EG} \; \text{专用，比普通} \; \text{ADF} \; \text{更负）} \\
\text{拒绝「} \; \text{û\_t} \; \text{有单位根」} \; \Rightarrow \; \text{协整成立} \\
\text{(3)} \; \text{若协整，建立误差修正模型：} \\
\Delta Y_{t}= \alpha+ \gamma \cdot ECM_{t- 1}+ \sum \delta_{i}\Delta X_{t- i}+ \sum \theta_{j}\Delta Y_{t- j}+ \epsilon_{t} \\
\text{其中} \; ECM_{t- 1}= \hat{u}_{t- 1}= Y_{t- 1}- \hat{\beta}_{0}- \hat{\beta}_{1}X_{t- 1}
\end{gathered}" width="663" height="174"></p>


**Granger 表述定理**：协整 ⇒ 一定存在 ECM 表示。<img class="fml" src="/formulas/68923f20821012.png" alt="\gamma" width="17" height="34"> 是**调整速度**（应为负），<img class="fml" src="/formulas/411a269ab20d95.png" alt="|\gamma|" width="28" height="34"> 越大，偏离长期均衡后修复越快；例如 <img class="fml" src="/formulas/a97704ef9d9e07.png" alt="\gamma=- 0.3" width="77" height="34"> 表示每期约修正 30% 的偏离。

![协整、长期均衡与误差修正](/econ/econ-cointegration.svg)

::: tip 工作示例 · AEG 检验与 ECM 解读
典型例中对协整残差做 ADF 型检验得到 <img class="fml" src="/formulas/41e0095526a385.png" alt="AEG=- 4.99" width="118" height="34">，而 5% 临界值约 <img class="fml" src="/formulas/de7fb287ff9b11.png" alt="- 3.01" width="53" height="34">（或 <img class="fml" src="/formulas/55ff5f240b260a.png" alt="- 3.4" width="44" height="34"> 视设定）：<img class="fml" src="/formulas/ef1f485bccf81f.png" alt="-4.99&lt;- 3.01" width="122" height="34"> ⇒ **拒绝非平稳，协整成立**。
配套对照：对原序列水平值检验 <img class="fml" src="/formulas/6aa9f3a2488abd.png" alt="t=- 1.71&gt;- 3.01" width="152" height="34">、<img class="fml" src="/formulas/9eaa7f23be9cc4.png" alt="- 0.72&gt;- 1.96" width="122" height="34"> 等 ⇒ 不能拒绝单位根（非平稳）；<img class="fml" src="/formulas/8bea99c34628c8.png" alt="- 3.68&lt;- 1.96" width="122" height="34">、<img class="fml" src="/formulas/3025d7eb0cb4fc.png" alt="- 3.49&lt;- 1.96" width="122" height="34"> ⇒ 一阶差分后平稳。这正是「`I(1)` 且协整」的典型证据链。
若 ECM 估计得 <img class="fml" src="/formulas/99334f65a5e47b.png" alt="\hat{\gamma}=- 0.25" width="87" height="34">，含义是上期偏离均衡 1 单位，本期 Y 反向调整 0.25 单位，半衰期约 <img class="fml" src="/formulas/50f2cbf8b9dbcd.png" alt="\frac{\ln 0.5}{\ln 0.75} \approx 2.4" width="93" height="34"> 期。
:::

| 方法 | 适用 | 优点 | 局限 |
| --- | --- | --- | --- |
| EG 两步法 | 单方程、一个协整关系 | 简单直观 | 第一步 OLS 小样本有偏；只能找一个协整向量；检验功效低 |
| **Johansen 检验** | 多变量 VAR、多个协整关系 | 迹统计量 / 最大特征值统计量，可定协整秩 r | 需设定 VAR 阶数与确定性项，对设定敏感 |
| ARDL / Pesaran 边界检验 | 变量可混合 `I(0)/I(1)` | 不要求同阶单整，小样本表现好 | 不能有 `I(2)` |
| VECM | 协整系统 | 同时刻画长期均衡与短期动态、可做 Granger 因果与脉冲响应 | 系统较复杂 |

### 7.4 ARIMA / Box-Jenkins 与波动率模型（★★）

**Box-Jenkins 三步**：① 识别（用 ADF 定 d，用 ACF/PACF 定 p、q：AR(p) 的 PACF 在 p 阶截尾、ACF 拖尾；MA(q) 反之）；② 估计（MLE / 条件最小二乘）；③ 诊断（残差应为白噪声，Ljung-Box Q 检验不显著），必要时回到 ①。

| 补充模型 | 用途 |
| --- | --- |
| **ARCH / GARCH** | 金融收益率「波动聚集」：<img class="fml" src="/formulas/d2240bbcb426c4.png" alt="\sigma^{2}_{t}= \omega+ \alpha \epsilon^{2}_{t- 1}+ \beta \sigma^{2}_{t- 1}" width="186" height="34">，<img class="fml" src="/formulas/464b73d9c78f40.png" alt="\alpha+\beta" width="52" height="34"> 接近 1 表示冲击持久；EGARCH / GJR 刻画杠杆效应（坏消息放大波动） |
| VAR | 把所有变量都当内生，每个变量对自身与其它变量滞后回归；用脉冲响应、方差分解分析动态传导 |
| 季节调整 / SARIMA | 含季节周期的数据 |

::: danger 易错 · 时间序列
- ADF 的 H0 是「**有单位根（非平稳）**」，拒绝才是平稳；KPSS 恰好相反，别记反。
- 协整要求变量**同阶单整**（EG 框架下）；`I(0)` 与 `I(1)` 混合应考虑 ARDL 边界检验。
- 协整 ≠ 因果：协整只说明存在长期共同运动，方向要靠 ECM/Granger 或理论识别。
- 差分会丢掉**长期水平信息**，因此有协整时必须用 VECM，不能简单全差分。
- 对非平稳序列直接做 t 检验 / Granger 检验易得伪结论；先检验平稳性。
:::

### 7.5 ACF/PACF 定阶、VAR 与 Johansen 检验

| 过程 | ACF | PACF |
| --- | --- | --- |
| AR(p) | 拖尾（指数/阻尼振荡衰减） | **p 阶截尾** |
| MA(q) | **q 阶截尾** | 拖尾 |
| ARMA(p,q) | 拖尾 | 拖尾 |
| 白噪声 | 所有 k>0 均不显著 | 同左 |

Ljung-Box <img class="fml" src="/formulas/df4a77f33799bb.png" alt="Q= n(n+2)\sum \frac{\hat{\rho}_{k}^{2}}{n- k} \sim \chi^{2}(m)" width="236" height="36"> 检验残差是否白噪声；显著说明还有结构没提取。

**VAR(p)**：每个变量对**所有**变量的 1…p 期滞后回归；要求各变量平稳（协整则用 VECM）。产出主要是**脉冲响应函数 IRF**（一个变量一单位冲击对其它变量的动态影响）与**方差分解**（各冲击对预测误差方差的贡献）。VAR 的滞后阶由 AIC/SC/LR 定，且需检验特征根是否在单位圆内（稳定性）。

**Johansen 协整检验**流程：① 定 VAR 阶数；② 确定确定性项（截距/趋势）设定；③ 用**迹统计量**（<img class="fml" src="/formulas/b8453c087c1241.png" alt="H_{0}: r \le r_{0}" width="91" height="34"> vs <img class="fml" src="/formulas/9e92f8c31c1f0d.png" alt="r&gt; r_{0}" width="55" height="34">）与**最大特征值统计量**（<img class="fml" src="/formulas/c9ed810249562a.png" alt="H_{0}: r= r_{0}" width="91" height="34">）逐个判断协整秩 r；④ 得 r 后写 VECM，施加并检验长期约束（如 <img class="fml" src="/formulas/feee3917200d66.png" alt="\beta=(1,- 1)" width="95" height="34"> 表示一价定律）。

---

## 第 8 章 联立方程模型

### 8.1 为什么 OLS 会失效（★★★）

经济系统里变量常**互为因果**。经典宏观例子：


<p class="fml-block"><img class="fml" src="/formulas/1dc512a3c16976.png" alt="\begin{gathered}
\text{消费函数：} \; C_{t}= \alpha+ \beta Y_{t}+ u_{t} \; \text{（行为方程）} \\
\text{收入恒等：} \; \text{Y\_t = C\_t + I\_t} \; \text{（恒等式）}
\end{gathered}" width="353" height="58"></p>


把第二式代入第一式整理可得 <img class="fml" src="/formulas/b7c377793b2a15.png" alt="Y_{t}= \frac{\alpha+I_{t}+u_{t}}{1- \beta}" width="99" height="36">，于是 `Y_t` 含 `u_t` ⇒ <img class="fml" src="/formulas/e9458c071d33ff.png" alt="\operatorname{Cov}(Y_{t}, u_{t})\ne 0" width="125" height="33">。用 OLS 估计消费函数得到的 <img class="fml" src="/formulas/38e1ef139b243c.png" alt="\hat{\beta}" width="18" height="34"> **既有偏又不一致**（称**联立性偏误 / 同时方程偏误**），且样本增大也不消失。

![联立方程、简化式与识别](/econ/econ-simultaneous.svg)

| 概念 | 定义 |
| --- | --- |
| **内生变量** | 由模型内部决定（C、Y） |
| **外生变量** | 模型外部给定（I、政策变量） |
| **前定变量** | 外生变量 + 滞后内生变量（本期已确定） |
| 行为方程 | 描述经济主体行为，含随机扰动与待估参数 |
| 恒等式 | 定义式 / 均衡条件，无待估参数（如 `Y=C+I`） |
| **结构式** | 按经济理论直接写出的方程，系数是结构参数 |
| **简化式** | 每个内生变量只用**前定变量**表示，可直接用 OLS 一致估计 |

### 8.2 识别问题（★★★）

「识别」问的是：能否从**可估计的简化式参数**唯一地解出**结构参数**。设模型共 `G` 个内生变量（方程数）、`K` 个前定变量；某方程含 `g` 个内生变量、`k` 个前定变量，则该方程**排除**了 <img class="fml" src="/formulas/b6ec49bc11a773.png" alt="G- g" width="52" height="34"> 个内生变量与 <img class="fml" src="/formulas/bb8f0efc9a1919.png" alt="K- k" width="55" height="34"> 个前定变量。

| 判据 | 内容 |
| --- | --- |
| **阶条件（必要非充分）** | 被该方程排除的前定变量数 <img class="fml" src="/formulas/a9b094da01dd25.png" alt="K- k \ge g- 1" width="119" height="34">（该方程包含的内生变量数 −1） |
| 恰好识别 | <img class="fml" src="/formulas/51beba67600b67.png" alt="K- k= g- 1" width="119" height="34"> → 可用**间接最小二乘 ILS** |
| 过度识别 | <img class="fml" src="/formulas/56288793024d75.png" alt="K- k&gt; g- 1" width="118" height="34"> → 用 **2SLS / LIML / GMM** |
| 不可识别 | <img class="fml" src="/formulas/a3ba62730543db.png" alt="K- k&lt; g- 1" width="119" height="34"> → 任何方法都救不了，必须改模型或加外生变量 |
| **秩条件（充要）** | 被排除变量在其它方程中的系数矩阵存在非零 <img class="fml" src="/formulas/00b68d8e5f69a3.png" alt="G- 1" width="52" height="34"> 阶行列式；实际由软件或矩阵秩判断 |

::: tip 工作示例 · 阶条件判断
沿用 8.1 宏观模型：`G=2` 个内生变量（C、Y），`K=2` 个前定变量（常数、I）。
- **消费方程** <img class="fml" src="/formulas/78922243e34423.png" alt="C= \alpha+\beta Y+u" width="135" height="34">：含 `g=2` 个内生（C、Y）、`k=1` 个前定（常数），排除了 <img class="fml" src="/formulas/c5c25dc1fc7817.png" alt="K- k=1" width="88" height="34"> 个前定变量（I）。<img class="fml" src="/formulas/e32f6fd61db03a.png" alt="1 \ge g- 1= 1" width="113" height="34"> ✓ **恰好识别** → ILS 或 2SLS 均可。
- **收入恒等式** `Y = C+I`：恒等式无需识别。
- 若消费方程改为 <img class="fml" src="/formulas/4ad6f7afeb24bf.png" alt="C= \alpha+\beta Y+\gamma C_{- 1}+u" width="197" height="34">（把 <img class="fml" src="/formulas/ccab1895b0ae36.png" alt="C_{- 1}" width="36" height="34"> 作为前定变量纳入，则 `K=3`）：`k=2`（常数、C₋1），<img class="fml" src="/formulas/64e433b35d42ff.png" alt="K- k=1= g- 1" width="152" height="34"> 仍恰好识别。
- 若模型再引入政府支出 G 与税收 T 两个外生变量且都不进消费方程：<img class="fml" src="/formulas/2e04f6fd7ca010.png" alt="K- k= 3&gt; 1" width="120" height="34"> → **过度识别**，须用 2SLS。

**直觉**：要让一个方程可识别，必须有「别的方程里有、但这个方程里没有」的外生变量充当**工具**——这正是 2SLS 第一阶段用全部前定变量做回归的原因。
:::

### 8.3 估计方法（★★）

| 方法 | 适用 | 要点 |
| --- | --- | --- |
| ILS 间接最小二乘 | 恰好识别 | 先 OLS 估简化式，再代数解回结构参数；过度识别时会得到多个解 |
| **2SLS 两阶段最小二乘** | 恰好 / 过度识别，单方程 | 第一阶段用**全部前定变量**回归每个内生解释变量得拟合值；第二阶段用拟合值替代，等价于 IV；最常用 |
| 3SLS / FIML | 系统估计 | 同时利用跨方程扰动相关，效率更高，但一个方程设定错会污染全系统 |
| LIML / GMM | 弱工具、异方差情形 | LIML 对弱工具更稳健；GMM 可处理异方差与自相关 |

::: danger 易错 · 联立方程
- 阶条件**只是必要**条件：满足阶条件仍可能因秩条件不满足而不可识别（如某变量虽被排除，但在其它方程系数全为 0）。
- 恒等式**没有随机扰动、无需估计**，但仍算一个方程、计入 `G`。
- 2SLS 第二阶段的标准误须用**修正后的残差**（含原始内生变量），直接用拟合值算会低估标准误；软件会自动处理，手算要小心。
- 「简化式系数」不是「结构系数」：简化式给的是外生变量对内生变量的**总效应**（含乘数），例如 <img class="fml" src="/formulas/a737e5df1559ea.png" alt="\frac{1}{1- \beta}" width="35" height="36"> 就是投资乘数。
:::

### 8.4 简化式求解与 2SLS 的 IV 等价性

沿用 8.1 的宏观模型：


<p class="fml-block"><img class="fml" src="/formulas/3817a1de23a042.png" alt="\begin{gathered}
C_{t}= \alpha+ \beta Y_{t}+ u_{t} \; \text{；} \; \text{Y\_t = C\_t + I\_t} \\
\text{代入：} \; Y_{t}= \alpha+ \beta Y_{t}+ u_{t}+ I_{t} \\
\to Y_{t}= \frac{\alpha}{1- \beta}+ \frac{I_{t}}{1- \beta}+ \frac{u_{t}}{1- \beta} \; \text{（简化式）} \\
\to C_{t}= \frac{\alpha}{1- \beta}+ \frac{\beta I_{t}}{1- \beta}+ \frac{u_{t}}{1- \beta}
\end{gathered}" width="346" height="148"></p>


<img class="fml" src="/formulas/04c072634f5062.png" alt="\frac{\partial Y_{t}}{\partial I_{t}}= \frac{1}{1- \beta}" width="82" height="36"> 就是**投资乘数**。若 <img class="fml" src="/formulas/705d9f9e9ea688.png" alt="\beta=0.8" width="64" height="34">，乘数 = 5。由简化式可解出 <img class="fml" src="/formulas/67023af945f094.png" alt="\beta=\dfrac{\pi_{2}}{1+\pi_{2}}" width="94" height="44">（<img class="fml" src="/formulas/34f7210df88994.png" alt="\pi_{2}" width="25" height="34"> 为 I 在 C 方程简化式中的系数），这正是 **ILS 间接最小二乘**：先 OLS 估简化式（前定变量外生，一致），再代数反解结构参数。

**2SLS 与 IV 等价**：第一阶段 <img class="fml" src="/formulas/700b72ab521e74.png" alt="X= Z\hat{\Pi}+ v" width="105" height="34"> 得 `X̂ = P_Z X`（`P_Z` 为对全部前定变量的投影矩阵），第二阶段 <img class="fml" src="/formulas/d03f5796e48df9.png" alt="\hat{\beta}_2SLS=(X&#x27;P_{Z} X)^{-1}X&#x27;P_{Z} y" width="225" height="34">，恰是以 `Z` 为工具的 IV 估计量。当工具数 = 内生变量数时 <img class="fml" src="/formulas/ee91b996557e15.png" alt="X&#x27;P_{Z} X= X&#x27;Z(Z&#x27;Z)^{-1}Z&#x27;X" width="219" height="34">，退化为标准 IV 公式。

---

## 第 9 章 面板数据模型

### 9.1 面板数据及其优势（★★★）

面板数据＝**同一批个体**（地区、企业、家庭）在**多个时期**都被观测。设 <img class="fml" src="/formulas/17815650020b2f.png" alt="i= 1 \cdots N" width="89" height="34"> 个个体、<img class="fml" src="/formulas/b7b52ca29725e9.png" alt="t= 1 \cdots T" width="85" height="34"> 期，总观测 `NT`。

| 优势 | 说明 |
| --- | --- |
| 控制不可观测的个体异质性 | 用个体固定效应吸收不随时间变的遗漏因素（文化、地理位置、企业基因）→ 大幅缓解遗漏变量偏误 |
| 更多变异、更大自由度 | 同时含**组间（between）**与**组内（within）**变异 |
| 可研究动态 | 能识别滞后效应、调整过程 |
| 可做更可信的因果设计 | DID、事件研究、个体固定效应 |

代价：面板常有**组内相关**（同一个体跨期误差相关）、**异方差与截面相关**、**样本流失（attrition）**、测量误差；普通 OLS 标准误会严重低估。



<p class="fml-block"><img class="fml" src="/formulas/69ac21492f423b.png" alt="\begin{gathered}
\text{通用设定：} \; y_{it}= \alpha+ \beta &#x27;x_{it}+ \mu_{i}+ \lambda_{t}+ \epsilon_{it} \\
\mu_{i} \; \text{：个体效应（不随时间变）；} \; \lambda_{t} \; \text{：时间效应（不随个体变）；} \; \epsilon_{it} \; \text{：特异误差}
\end{gathered}" width="616" height="58"></p>



![面板数据三种模型与 Hausman 检验](/econ/econ-panel.svg)

### 9.2 三类基本模型（★★★）

| 模型 | 设定 | 估计 | 关键假定 |
| --- | --- | --- | --- |
| **混合回归 Pooled OLS** | 忽略 μ_i，把所有观测堆在一起 | OLS | <img class="fml" src="/formulas/9f7799f27b2459.png" alt="\mu_{i}= 0" width="55" height="34">（无个体效应）；通常不成立 |
| **固定效应 FE** | <img class="fml" src="/formulas/38b4177264bfaa.png" alt="\mu_{i}" width="23" height="34"> 视为待估参数，允许与 x 相关 | **LSDV**（加 N−1 个个体虚拟变量）／**组内去均值（within）**／一阶差分 FD | 允许 <img class="fml" src="/formulas/44d47786caf215.png" alt="\operatorname{Cov}(\mu_{i}, x_{it})\ne 0" width="129" height="33">；一致性更强 |
| **随机效应 RE** | <img class="fml" src="/formulas/38b4177264bfaa.png" alt="\mu_{i}" width="23" height="34"> 视为随机且与 x **不相关**，并入复合误差 | FGLS（拟去均值 <img class="fml" src="/formulas/0eab0c36c71939.png" alt="y_{it}- \theta \bar{y}_{i}" width="70" height="34">） | <img class="fml" src="/formulas/34162485b900b7.png" alt="\operatorname{Cov}(\mu_{i}, x_{it})= 0" width="129" height="34">；若成立则更有效，且能估**不随时间变**的变量 |

**组内变换**：<img class="fml" src="/formulas/4869c44f08397c.png" alt="y_{it}- \bar{y}_{i}= \beta &#x27;(x_{it}- \bar{x}_{i})+(\epsilon_{it}- \bar{\epsilon}_{i})" width="259" height="34">，μ_i 被相减消掉。
- FE **无法估计**不随时间变化的变量（性别、地区固定属性）——它们被去均值消掉。
- FE 的一致性强，但当 T 小、组内变异少时标准误大；RE 效率更高但依赖强假定。
- **双向固定效应 TWFE**：同时加个体与时间虚拟变量，控制共同宏观冲击。

### 9.3 Hausman 检验（★★★）



<p class="fml-block"><img class="fml" src="/formulas/f4ab67d91cd961.png" alt="\begin{gathered}
H_{0}: \; \text{个体效应与解释变量不相关（} \; \text{RE} \; \text{一致且有效）} \; \to \; \text{选} \; \text{RE} \\
H_{1}: \; \text{相关（} \; \text{RE} \; \text{不一致，} \; \text{FE} \; \text{仍一致）} \; \to \; \text{选} \; \text{FE} \\
H=(\hat{\beta}_{FE}- \hat{\beta}_{RE})&#x27;[\operatorname{Var}(\hat{\beta}_{FE})- \operatorname{Var}(\hat{\beta}_{RE})]^{-1}(\hat{\beta}_{FE}- \hat{\beta}_{RE}) \sim \chi^{2}(k)
\end{gathered}" width="509" height="86"></p>


显著（H 大于临界值）⇒ 拒绝 <img class="fml" src="/formulas/890470bde99fdc.png" alt="H_{0} \Rightarrow" width="51" height="34"> **用 FE**；不显著 ⇒ 可用 RE（更有效）。

::: tip 工作示例 · Hausman 手算（单系数）
设 <img class="fml" src="/formulas/fee47398434f55.png" alt="\hat{\beta}_{FE}= 0.62, \operatorname{Var}= 0.004" width="195" height="34">；<img class="fml" src="/formulas/f172ae6322dd55.png" alt="\hat{\beta}_{RE}= 0.45, \operatorname{Var}= 0.001" width="195" height="34">：


<p class="fml-block"><img class="fml" src="/formulas/bbb419e178c778.png" alt="\begin{gathered}
H= \frac{(0.62- 0.45)^{2}}{0.004- 0.001}= \frac{0.0289}{0.003}= 9.63 \\
\chi^{2}_{0}._{05}(1)= 3.84 \to 9.63&gt; 3.84 \Rightarrow \; \text{拒绝} \; \text{RE} \; \text{，应选固定效应}
\end{gathered}" width="466" height="76"></p>


**注意**：① 检验只比较**时变变量**的系数（FE 估不了时不变变量）；② 若 <img class="fml" src="/formulas/d333703eff8a25.png" alt="\operatorname{Var}(\hat{\beta}_{FE})- \operatorname{Var}(\hat{\beta}_{RE})" width="176" height="34"> 非正定（小样本常见），H 可能为负，需改用稳健版或 `suest`；③ 即便 Hausman 不显著，只要理论上怀疑个体效应与 x 相关（如研究企业效率），多数应用计量仍优先 FE；④ 现代做法常用 **Mundlak / 相关随机效应（CRE）**：把组内均值 `x̄_i` 加入 RE 模型，既保留时不变变量又能检验并缓解相关性。
:::

### 9.4 面板标准误与现代扩展（★★）

| 补充主题 | 要点 |
| --- | --- |
| **聚类稳健标准误** | 按个体聚类（允许任意组内自相关与异方差）；DID 常按处理分配层级聚类；聚类数少（< 40）须用 wild cluster bootstrap |
| 双向聚类 / Driscoll-Kraay | 同时处理截面相关与时间相关 |
| **动态面板与 Nickell 偏误** | 含 <img class="fml" src="/formulas/c8f0c96d516c6e.png" alt="y_{i,t- 1}" width="45" height="34"> 且 T 小时，FE 估计不一致（偏误约 <img class="fml" src="/formulas/d06bad634893b6.png" alt="- \frac{1}{T}" width="34" height="34">）；用 **Arellano-Bond 差分 GMM / Blundell-Bond 系统 GMM**，并做 AR(2) 与 Hansen 检验 |
| 交互固定效应 / 因子结构 | 控制随时间变化但有共同因子的不可观测异质性 |
| 交错处理 DID 的 TWFE 偏误 | 处理时点不同且效应异质时 TWFE 可能给错权重；用 <img class="fml" src="/formulas/212e8b57c51a56.png" alt="Callaway- Sant" width="144" height="34">'Anna、<img class="fml" src="/formulas/54f0c113017c94.png" alt="Sun- Abraham" width="136" height="34">、Borusyak 等稳健估计量 |
| 面板单位根 / 面板协整 | LLC、IPS、Fisher-ADF；Pedroni / Kao 协整检验 |

::: danger 易错 · 面板数据
- 「混合数据 pooled」≠「面板数据」：只有**同一批**个体跨期追踪才是面板，否则不能做组内变换。
- FE 不能估时不变变量的系数，但**能**控制它们（被吸收）；别写成「FE 无法控制性别」。
- RE 的一致性依赖 <img class="fml" src="/formulas/4a4faf6a1c2fc4.png" alt="\operatorname{Cov}(\mu_{i}, x_{it})=0" width="128" height="34">，这个假定通常可疑；Hausman 检验功效有限，「没拒绝」不等于「成立」。
- 面板不等于能自动识别因果：仍可能有随时间变化的遗漏变量、反向因果。
- 用 LSDV 时标准误要按 <img class="fml" src="/formulas/2ea0e6833caeed.png" alt="NT- N- k" width="106" height="34"> 自由度调整，否则会低估；含很多虚拟变量时直接用组内估计量更高效。
:::

::: tip 补充考点 · 平衡面板与非平衡面板
**平衡面板**：每个个体观测期数相同（N×T 完整矩形）；**非平衡面板**：个体进入/退出、缺失导致期数不齐。非平衡数据不必强行删成平衡：FE/RE 都能直接估计，但**样本流失若非随机**（如经营差的企业退出），会造成**选择性偏差**，结论只适用于"留存者"；Hausman 检验在非平衡面板下的解释也要谨慎。答题时先报告面板是否平衡、N 与 T 各是多少。
:::

### 9.5 面板的三种变异与 Mundlak 设定



<p class="fml-block"><img class="fml" src="/formulas/c2349632ed8a2e.png" alt="\begin{gathered}
\text{总变异} \; \text{overall} \; \text{：} \; y_{it}- \bar{y} \; \text{（混合} \; \text{OLS} \; \text{用）} \\
\text{组内变异} \; \text{within} \; \text{：} \; y_{it}- \bar{y}_{i} \; \text{（} \; \text{FE} \; \text{用，只识别时变变量的效应）} \\
\text{组间变异} \; \text{between} \; \text{：} \; \bar{y}_{i}- \bar{y} \; \text{（} \; \text{BE} \; \text{用，易受个体异质性污染）} \\
\text{RE =} \; \text{组内与组间估计量的加权平均，权重} \; \theta \; \text{由} \; \sigma^{2}_\mu \; \text{与} \; \sigma^{2}_\epsilon \; \text{、} \; \text{T} \; \text{决定}
\end{gathered}" width="529" height="111"></p>


**Mundlak / 相关随机效应 CRE**：在 RE 模型中加入各时变变量的**个体均值** `x̄_i`：


<p class="fml-block"><img class="fml" src="/formulas/84c98e0827bd31.png" alt="y_{it}= \alpha+ \beta &#x27;x_{it}+ \gamma &#x27;\bar{x}_{i}+ \mu_{i}+ \epsilon_{it}" width="246" height="34"></p>


若 <img class="fml" src="/formulas/8568b8c12e1b5b.png" alt="\gamma= 0" width="50" height="34"> 则 RE 假定成立；否则该设定给出与 FE 相同的 <img class="fml" src="/formulas/38e1ef139b243c.png" alt="\hat{\beta}" width="18" height="34">，同时仍能估计时不变变量，且可做 Hausman 检验的等价 Wald 版本。**这是现代应用计量中常被推荐的折中做法**。

DID 在面板中即 <img class="fml" src="/formulas/9f4f3634d56244.png" alt="y_{it}= \alpha+ \mu_{i}+ \lambda_{t}+ \delta \cdot D_{it}+ \epsilon_{it}" width="243" height="34">（双向固定效应）；<img class="fml" src="/formulas/869e038d830c1d.png" alt="D_{it}= Treat_{i} \times Post_{t}" width="171" height="34">。交错处理时点 + 异质效应下 <img class="fml" src="/formulas/030b4649142f76.png" alt="\hat{\delta}" width="16" height="33"> 是各 <img class="fml" src="/formulas/e17fc71e34f68d.png" alt="2 \times 2" width="46" height="34"> 的加权平均且权重可能为负，这就是 **TWFE 偏误**。

---

## 第 10 章 定性选择模型

### 10.1 线性概率模型 LPM（★★★）

被解释变量是 **0/1**（是否就业、是否违约、选择公交还是自驾）时，直接用 OLS：


<p class="fml-block"><img class="fml" src="/formulas/d0db963948b070.png" alt="P(Y_{i}=1|X_{i})= \beta_{0}+ \beta &#x27;X_{i} \; \text{（把条件期望当作概率）}" width="407" height="34"></p>


| 问题 | 说明 |
| --- | --- |
| 预测值越界 | <img class="fml" src="/formulas/2d3b624862d895.png" alt="X\beta" width="34" height="34"> 可能 <0 或 >1，「概率」无意义 |
| 异方差 | <img class="fml" src="/formulas/9be2c51320bb4e.png" alt="\operatorname{Var}(u\vert X)= p(1- p)" width="168" height="34"> 依赖 X ⇒ 标准误须用稳健标准误 |
| 非正态误差 | u 只能取两个值；小样本 t/F 只是渐近有效 |
| 边际效应恒定 | 隐含「X 对概率的影响处处相同」，通常不合经济直觉 |

**唯一优点**：系数可直接解释为「X 增 1 单位，概率变动 β」，简单、可作基准；在概率集中于 0.2–0.8 时近似尚可。

### 10.2 Logit 与 Probit（★★★）

用**潜变量**框架：<img class="fml" src="/formulas/b50597a76c1ed8.png" alt="y*= \beta &#x27;X+ u" width="113" height="34">，`y = 1[y* > 0]`；对 u 的分布作假定即得到不同模型，用**极大似然 MLE** 估计。

| 模型 | 分布 | `P(Y=1|X)` | 边际效应 | 系数换算 |
| --- | --- | --- | --- | --- |
| **Logit** | 逻辑分布 | <img class="fml" src="/formulas/560b4c5a54287f.png" alt="\Lambda(z)= \frac{1}{1+e^{- z}}" width="105" height="35"> | <img class="fml" src="/formulas/47f1d587297db5.png" alt="\beta_{j} \cdot P(1- P)" width="109" height="34"> | <img class="fml" src="/formulas/d759b0f0f08eed.png" alt="e^{\beta_{j}}" width="28" height="34"> = **优势比 odds ratio** |
| **Probit** | 标准正态 | <img class="fml" src="/formulas/bdbd99a06b3b40.png" alt="\Phi(z)" width="43" height="34"> | <img class="fml" src="/formulas/db4bc0e8e8fbe5.png" alt="\beta_{j} \cdot \phi(z)" width="71" height="34"> | 与 Logit 系数约差 1.6 倍：<img class="fml" src="/formulas/9d0dd7acdaa75c.png" alt="\beta_{Logit} \approx 1.6 \beta_{Probit}" width="141" height="34"> |
| LPM | — | `z`（线性） | <img class="fml" src="/formulas/d533b430bb5b9c.png" alt="\beta_{j}" width="24" height="34">（常数） | 直接是概率变化 |

![LPM、Logit 与 Probit 曲线](/econ/econ-logit.svg)

::: tip 工作示例 · Logit 概率、边际效应与优势比（完整演算）
设估计得 <img class="fml" src="/formulas/f53e9034bee567.png" alt="z=- 1+ 0.5x" width="118" height="34">（<img class="fml" src="/formulas/25ed694f691ba3.png" alt="\beta_{0}=- 1" width="70" height="34">，<img class="fml" src="/formulas/7e94e2533d47fe.png" alt="\beta_{1}=0.5" width="71" height="34">）：



<p class="fml-block"><img class="fml" src="/formulas/16919c722719ee.png" alt="\begin{gathered}
x=2 \to z=0 \to P= \frac{1}{1+e^{0}}= 0.5000 \; \text{，边际效应} \; = 0.5 \times 0.5 \times 0.5= 0.1250 \; \text{（最大）} \\
x=4 \to z=1 \to P= \frac{1}{1+e^{-1}}= 0.7311 \; \text{，边际效应} \; = 0.5 \times 0.7311 \times 0.2689= 0.0983 \\
x=6 \to z=2 \to P= 0.8808 \; \text{，边际效应} \; = 0.5 \times 0.8808 \times 0.1192= 0.0525 \\
x=0 \to z=- 1 \to P= 0.2689 \; \text{，边际效应} \; \text{= 0.0983} \\
\text{优势比} \; \text{OR = e(0.5) = 1.649} \; \text{：} \; \text{x} \; \text{每增} \; \text{1} \; \text{单位，发生比（} \; \frac{P}{1- P} \; \text{）乘以} \; \text{1.649} \; \text{（约} \; \text{+64.9\%} \; \text{）}
\end{gathered}" width="732" height="185"></p>


**读法**：① 系数符号决定概率随 x 增减的方向，但**大小不是概率变化**；② 边际效应随 x 变化，在 <img class="fml" src="/formulas/2e5495f00bdcde.png" alt="P \approx 0.5" width="68" height="34"> 处最大、两端趋于 0（S 形曲线）；③ 报告结果应给**平均边际效应 AME** 或指定 x 处的 MEM，而非只报 β；④ Probit 在 z=1 时 <img class="fml" src="/formulas/c3b1533ddfd669.png" alt="\Phi(1)=0.8413" width="116" height="34">，边际效应 <img class="fml" src="/formulas/8996da2ff422b0.png" alt="0.5 \times \phi(1)=0.5 \times 0.2420=0.1210" width="276" height="33">。
:::

### 10.3 估计、检验与拟合优度（★★）



<p class="fml-block"><img class="fml" src="/formulas/7efe00d2f37c3e.png" alt="\text{对数似然：} \; lnL= \sum[ y_{i} \ln F(z_{i})+(1- y_{i}) \ln(1- F(z_{i}))]" width="443" height="33"></p>


因 MLE 最大化数值，软件用迭代（Newton-Raphson / BHHH）；不收敛、完全分离（某 X 完美预测 y）会导致系数发散，须检查。

| 检验 / 指标 | 说明 |
| --- | --- |
| Wald / z 检验 | 单个系数显著性（渐近正态） |
| **似然比 LR** | <img class="fml" src="/formulas/2da2482702881a.png" alt="LR= 2(lnL_{u}- lnL_{r}) \sim \chi^{2}(q)" width="238" height="33">，比较嵌套模型，最可靠 |
| LM（得分）检验 | 只需估约束模型 |
| 伪 R²（McFadden） | <img class="fml" src="/formulas/7c20f1111a993c.png" alt="1- \frac{lnL_{u}}{lnL_{r}}" width="68" height="34">，**不能**与 OLS 的 R² 比大小，0.2–0.4 已算不错 |
| 分类表 / ROC-AUC / Hosmer-Lemeshow | 预测准确度与校准度；不平衡样本要看 PR-AUC 与阈值选择 |

### 10.4 扩展模型（★★★）

| 模型 | 适用情形 |
| --- | --- |
| **多项 Logit / Probit** | 因变量多个无序类别（公交/自驾/骑车）；须满足 **IIA 无关选项独立性**（用 Hausman-McFadden 检验），否则用嵌套 Logit / 混合 Logit |
| **有序 Logit / Probit** | 因变量有序（满意度 1–5 级）；假定**平行线（比例优势）**，违反则用广义有序模型 |
| **Tobit（删失回归）** | 因变量在 0 处**角点堆积**（消费支出、工作时间），OLS 会有偏；用 MLE 同时刻画「是否参与」与「参与多少」 |
| **Heckman 两阶段（样本选择）** | 样本非随机进入（只有就业者才有工资）→ 选择偏差；第一阶段选择方程算逆米尔斯比 λ，第二阶段纳入修正；须有**排除变量**才识别 |
| Poisson / 负二项 | 计数因变量（专利数、就诊次数）；过度离散时用负二项或稳健标准误 |
| 生存分析 / Cox | 持续时间数据（失业持续期） |

::: danger 易错 · 定性选择模型
- Logit/Probit 的 β **不是边际效应**；且边际效应依赖 X 取值，不能只报一个 β 就解释。
- 「优势比 1.65」是**发生比**变化 65%，不是「概率增加 65%」。
- 伪 R² 与 OLS 的 R² 不可比；分类准确率高也可能是因为样本极度不平衡（全部预测为多数类）。
- 非线性模型中的**交互项**符号与显著性不能只看乘积项系数（<img class="fml" src="/formulas/45e602082c43a4.png" alt="Ai- Norton" width="107" height="33"> 问题），须计算交互边际效应。
- 完全分离 / 稀有事件会让 MLE 偏误，可用 Firth 校正或精确 Logit。
:::

### 10.5 Tobit 的边际效应与 Heckman 两阶段

Tobit（潜变量 <img class="fml" src="/formulas/1d15bf897f24d4.png" alt="y*= \beta &#x27;x+u" width="107" height="33">，观测 <img class="fml" src="/formulas/1d9f61504a301a.png" alt="y= \max(0, y*)" width="123" height="33">）中 β 有三种不同的边际效应，**必须明确报的是哪一个**：


<p class="fml-block"><img class="fml" src="/formulas/b59cba677889e0.png" alt="\begin{gathered}
\text{(1)} \; \text{潜变量：} \; \frac{\partial E(y*|x)}{\partial x_{j}}= \beta_{j} \\
\text{(2)} \; \text{观测到的} \; \text{y} \; \text{：} \; \frac{\partial E(y|x)}{\partial x_{j}}= \beta_{j} \cdot \Phi\left(\beta &#x27;\frac{x}{\sigma}\right) \\
\text{(3)} \; \text{参与概率：} \; \frac{\partial P(y&gt;0|x)}{\partial x_{j}}= \phi\left(\beta &#x27;x/\sigma\right) \cdot \beta_{j}/\sigma \\
\text{(4)} \; \text{条件于} \; \text{y&gt;0} \; \text{：} \; \frac{\partial E(y|y&gt;0,x)}{\partial x_{j}}= \beta_{j} \cdot[1- z\lambda(z)- \lambda(z)^{2}] \; \text{，} \; z=\beta &#x27;\frac{x}{\sigma}
\end{gathered}" width="561" height="196"></p>



**Heckman 两阶段（样本选择）**：


<p class="fml-block"><img class="fml" src="/formulas/e1fea15df7d3a1.png" alt="\begin{gathered}
\text{(1)} \; \text{选择方程（全样本} \; \text{Probit} \; \text{）：} \; P(s_{i}=1|z_{i})=\Phi(\gamma &#x27;z_{i}) \; \text{，估} \; \hat{\gamma} \\
\text{(2)} \; \text{对每个被选中的样本算逆米尔斯比} \; \lambda_{i}= \dfrac{\phi(\hat{\gamma}&#x27;z_{i})}{\Phi(\hat{\gamma}&#x27;z_{i})} \\
\text{(3)} \; \text{结果方程（仅选中样本）：} \; y_{i}= \beta &#x27;x_{i}+ \rho \sigma \lambda_{i}+ e_{i} \\
\lambda \; \text{显著} \; \Rightarrow \; \text{存在选择偏差；} \; \rho \; \text{为选择与结果误差的相关系数}
\end{gathered}" width="496" height="132"></p>


**识别关键**：`z` 中至少要有一个**排除变量**（影响是否进入样本、但不直接影响结果），否则 λ 与 x 高度共线、修正不可靠。

---

## 综合例题精讲（跨章）

> 按「读题 → 列条件 → 完整演算 → 结论」展开，所有数值均已独立复算，适合闭卷手算练习。

### 综 1 · 一元 OLS 全套手算（第 2、3 章）

**题**：`X=[1,2,3,4,5]`，`Y=[2,4,5,7,9]`。求 OLS 估计式、R²、调整 R²、σ̂²、<img class="fml" src="/formulas/67627fc6345cdc.png" alt="se(\hat{\beta}_{1})" width="55" height="33">、t 值、95% 置信区间、整体 F 值与 `X=6` 的点预测。

**解**：


<p class="fml-block"><img class="fml" src="/formulas/d65f997d0cbe19.png" alt="\begin{gathered}
\text{(1) X̄=3, Ȳ=5.4} \; \text{；} \; \text{Sxx=10, Sxy=17} \\
(2) \hat{\beta}_{1}= \frac{17}{10}= 1.7 \; \text{；} \; \hat{\beta}_{0}= 5.4- 1.7 \times 3= 0.3 \to \hat{Y}= 0.3+ 1.7X \\
\text{(3)} \; \text{拟合值} \; \text{[2.0, 3.7, 5.4, 7.1, 8.8]} \; \text{；残差} \; [0, 0.3,- 0.4,- 0.1, 0.2] \; \text{（和为} \; \text{0 }\checkmark \; \text{）} \\
\text{(4) SSE = 0.30, SST = 29.20, SSR = 28.90} \\
R^{2}= \frac{28.90}{29.20}= 0.9897 \; \text{；} \; \bar{R}^{2}= 1- \frac{(1- 0.9897) \times 4}{3}= 0.9863 \\
(5) \hat{\sigma}^{2}= \frac{SSE}{n- 2}= \frac{0.30}{3}= 0.10 \\
se(\hat{\beta}_{1})= \sqrt{\frac{0.10}{10}}= 0.10 \\
(6) t= \frac{1.7}{0.10}= 17.0&gt; t_{0}._{025}(3)=3.182 \to \; \text{拒绝} \; H_{0}: \beta_{1}=0 \\
95\% CI= 1.7 ± 3.182 \times 0.10=[1.382, 2.018] \\
F= t^{2}= 289 \\
(7) X=6 \to \hat{Y}= 0.3+ 1.7 \times 6= 10.5
\end{gathered}" width="602" height="385"></p>


**易错**：σ̂² 用 <img class="fml" src="/formulas/3486b4ca05ed88.png" alt="n- 2" width="49" height="33"> 而不是 `n`；个别值预测区间比均值预测区间多一个 `1`；本例 n=5 过小，t 检验依赖正态性假定。

### 综 2 · 多元回归的约束检验与调整 R²（第 4 章）

**题**：无约束模型 <img class="fml" src="/formulas/f1f5d2ecd8bd62.png" alt="n=30, k=3, R^{2}_{u}=0.86" width="195" height="34">；施加 2 个线性约束后 <img class="fml" src="/formulas/a6caf8f5394f93.png" alt="R^{2}_{r}=0.62" width="84" height="34">。检验约束是否成立，求调整 R² 与整体 F。

**解**：


<p class="fml-block"><img class="fml" src="/formulas/d32a5266aee4b8.png" alt="\begin{gathered}
F= \frac{\frac{R^{2}_{u}- R^{2}_{r}}{q}}{\frac{1- R^{2}_{u}}{n- k- 1}} \\
= \frac{\frac{0.86- 0.62}{2}}{\frac{0.14}{26}}= \frac{0.12}{0.0053846}= 22.29 \\
F_{0}._{05}(2,26) \approx 3.37 \to \; \text{拒绝约束（被排除变量联合显著）} \\
\bar{R}^{2}= 1- \frac{(1- 0.86) \times 29}{26}= 0.8438 \\
\text{整体} \; F= \frac{\frac{0.86}{3}}{\frac{0.14}{26}}= 53.24&gt; F_{0}._{05}(3,26) \approx 2.98 \to \; \text{方程整体显著}
\end{gathered}" width="485" height="244"></p>


**延伸**：若各系数 t 值都很小但整体 F 很大，首先怀疑**多重共线性**；若单个系数符号与经济理论相反且标准误很大，同样指向共线或样本不足。

### 综 3 · 异方差的检验与修正（第 5 章）

**题**：`n=50`，残差平方对解释变量的辅助回归 <img class="fml" src="/formulas/99f1f36ccd49e2.png" alt="R^{2}_{aux}=0.12" width="98" height="33">（2 个约束）。判断是否存在异方差，并给出两套处理方案。

**解**：


<p class="fml-block"><img class="fml" src="/formulas/2f81c389b2d1f1.png" alt="\begin{gathered}
LM= n \cdot R^{2}_{aux}= 50 \times 0.12= 6.00 \; \text{；} \; \chi^{2}_{0}._{05}(2)=5.99 \to 6.00&gt; 5.99 \; \text{，勉强拒绝同方差} \\
\text{（结论应谨慎：贴近临界值，宜结合残差图与} \; \text{White} \; \text{检验；} \; \text{White} \; \text{的} \; \text{df} \; \text{更大，可能不拒绝）}
\end{gathered}" width="737" height="57"></p>


- **方案 A（现代实证首选）**：保留 OLS 系数，改用**异方差稳健标准误**（HC1/HC3）重算 t 与置信区间。优点是不需设定 <img class="fml" src="/formulas/7b46743688cd8e.png" alt="\sigma_{i}^{2}" width="25" height="34"> 的具体形式。
- **方案 B（效率优先）**：若已知 <img class="fml" src="/formulas/f8c6fddfc27593.png" alt="\operatorname{Var}(u_{i})=\sigma^{2}X_{i}^{2}" width="131" height="33">，两边同除 `X_i` 得 WLS；若 <img class="fml" src="/formulas/7b46743688cd8e.png" alt="\sigma_{i}^{2}" width="25" height="34"> 未知，先用残差估计再做 FGLS。
- **提醒**：异方差下 <img class="fml" src="/formulas/b5f2662fd9704d.png" alt="R^{2}" width="27" height="33">、系数点估计仍可用；失效的是标准误与一切基于它的推断。若数据按个体/地区分组，还要改用**聚类稳健标准误**。

### 综 4 · 自相关 DW 与 Cochrane-Orcutt（第 3、5 章）

**题**：残差 <img class="fml" src="/formulas/30b753124eadf8.png" alt="e=[0, 0.3,- 0.4,- 0.1, 0.2]" width="209" height="34">。计算 DW、估计 ρ̂；若另一研究发现 `d=0.8`，说明后果与修正步骤。

**解**：


<p class="fml-block"><img class="fml" src="/formulas/5bc8702d705c0b.png" alt="\begin{gathered}
\sum(e_{t}- e_{t- 1})^{2}= 0.09+0.49+0.09+0.09= 0.76 \; \text{；} \; \sum e_{t}^{2}= 0.30 \\
d= \frac{0.76}{0.30}= 2.533 \to \hat{\rho}= 1- \frac{d}{2}=- 0.267 \; \text{（轻微负相关；} \; \text{n=5} \; \text{仅演示算法）} \\
\text{若} \; d= 0.8 \to \hat{\rho}= 0.60 \; \text{，明显正自相关}
\end{gathered}" width="603" height="107"></p>


后果：系数（严格外生下）仍无偏，但 OLS 标准误被**低估**，t 值虚高 → 假阳性；OLS 不再有效。
修正（Cochrane-Orcutt 迭代）：


<p class="fml-block"><img class="fml" src="/formulas/74fa7e68aaf618.png" alt="\begin{gathered}
\text{(1)} \; \text{由残差回归} \; e_{t}= \rho e_{t- 1}+ v_{t} \; \text{得} \; \hat{\rho} \\
\text{(2)} \; \text{广义差分：} \; Y_{t}- \hat{\rho}Y_{t- 1}= \beta_{0}(1- \hat{\rho})+ \beta_{1}(X_{t}- \hat{\rho}X_{t- 1})+ v_{t} \\
\text{(3)} \; \text{对变换后模型做} \; \text{OLS} \; \text{，用新残差重估} \; \hat{\rho} \; \text{，迭代至收敛} \\
\text{(4)} \; \text{第一个观测可用} \; \text{Prais-Winsten} \; \text{变换} \; \left(\sqrt{1- \hat{\rho}^{2}}Y_{1}\right) \; \text{补回，避免损失样本}
\end{gathered}" width="597" height="121"></p>


**更稳妥的现代做法**：直接报告 **Newey-West HAC 标准误**；或先检查是否因**遗漏滞后变量**造成「伪自相关」。

### 综 5 · 多重共线性 VIF（第 4、5 章）

**题**：把 <img class="fml" src="/formulas/318fee4a66121c.png" alt="X_{1}" width="28" height="34"> 对其余解释变量辅助回归得 <img class="fml" src="/formulas/93980a6e43990a.png" alt="R^{2}_{1}=0.90" width="83" height="33">。求 VIF，说明对标准误与 t 值的影响。

**解**：


<p class="fml-block"><img class="fml" src="/formulas/f589261e8066d6.png" alt="\begin{gathered}
VIF_{1}= \frac{1}{1- 0.90}= 10 \\
\operatorname{Var}(\hat{\beta}_{1})= \sigma^{2}/[Sxx_{1}(1- R^{2}_{1})]= 10 \times \; \text{（无共线时的方差）} \\
se(\hat{\beta}_{1})= \sqrt{10} \approx 3.16 \; \text{倍} \; \to t \; \text{值约降为} \; \text{1/3.16}
\end{gathered}" width="461" height="103"></p>


典型症状：整体 F 显著、R² 高，但单个 t 多数不显著；增删少量样本系数剧变甚至符号反转。
**注意**：共线并不使系数有偏，也不必然损害**样本内共线模式延续时**的预测；若只是要检验「两个变量的联合效应」，直接用 F 检验线性组合即可，不必逐个纠结 t 值。

### 综 6 · 动态模型的长期乘数与 Granger 检验（第 6 章）

**题**：部分调整模型估计得 <img class="fml" src="/formulas/53142f59e237ab.png" alt="\beta_{0}=0.5, \lambda=0.6" width="136" height="33">；另 `SSE_r=1200, SSE_u=900, q=2, n=60, k=5`。求长期乘数、平均滞后与 Granger F 统计量并解读。

**解**：


<p class="fml-block"><img class="fml" src="/formulas/2e3c9947d17876.png" alt="\begin{gathered}
\text{短期乘数} \; \text{= 0.5} \\
\text{长期乘数} \; = \beta_{0}/(1- \lambda)= \frac{0.5}{0.4}= 1.25 \\
\text{平均滞后} \; \approx \frac{\lambda}{1- \lambda}= 1.5 \; \text{期（调整较慢）} \\
F= \frac{\frac{1200- 900}{2}}{\frac{900}{60- 5}}= \frac{150}{16.364}= 9.17&gt; F_{0}._{05}(2,55) \approx 3.17 \\
\to \; \text{拒绝「} \; \text{X} \; \text{的滞后项联合为} \; \text{0} \; \text{」，} \; \text{X Granger} \; \text{引起} \; \text{Y}
\end{gathered}" width="427" height="196"></p>


**解读边界**：这只是**增量预测能力**，不等于结构因果；若变量非平稳需先差分或做 VECM；滞后阶数换一档结论可能改变，应报告稳健性。

### 综 7 · 单位根、协整与 ECM（第 7 章）

**题**：对 `Y_t`、`X_t` 的水平值 ADF 检验统计量分别为 <img class="fml" src="/formulas/8c9edd553e12ca.png" alt="- 1.71" width="53" height="33">、<img class="fml" src="/formulas/44d60db542a584.png" alt="- 0.72" width="53" height="33">（5% 临界值 <img class="fml" src="/formulas/de7fb287ff9b11.png" alt="- 3.01" width="53" height="34">）；一阶差分后为 <img class="fml" src="/formulas/5dbb266270a560.png" alt="- 3.68" width="52" height="33">、<img class="fml" src="/formulas/0c674230ad23a4.png" alt="- 3.49" width="53" height="33">（5% 临界值 <img class="fml" src="/formulas/3e093e0481c50a.png" alt="- 1.96" width="52" height="33">）；协整残差的 AEG 统计量为 <img class="fml" src="/formulas/6540416cf14365.png" alt="- 4.99" width="53" height="33">（5% 临界值 <img class="fml" src="/formulas/de7fb287ff9b11.png" alt="- 3.01" width="53" height="34">）。判断单整阶、是否协整，并解释 ECM 中 <img class="fml" src="/formulas/99334f65a5e47b.png" alt="\hat{\gamma}=- 0.25" width="87" height="34"> 的含义。

**解**：


<p class="fml-block"><img class="fml" src="/formulas/cc1067e2a4ccd2.png" alt="\begin{gathered}
\text{水平值：} \; - 1.71&gt;- 3.01 \; \text{、} \; - 0.72&gt;- 3.01 \to \; \text{均不能拒绝单位根} \; \Rightarrow Y, X \sim I(1) \\
\text{一阶差分：} \; - 3.68&lt;- 1.96 \; \text{、} \; - 3.49&lt;- 1.96 \to \; \text{拒绝单位根} \; \Rightarrow \; \text{差分后平稳，确为} \; \text{I(1)} \\
\text{协整残差：} \; AEG=- 4.99&lt;- 3.01 \to \; \text{拒绝「残差有单位根」} \; \Rightarrow \; \text{二者协整，存在长期均衡}
\end{gathered}" width="726" height="84"></p>


因此不能简单把两变量差分后回归（会丢长期信息），应建立 **VECM / ECM**：



<p class="fml-block"><img class="fml" src="/formulas/9ab4024944695e.png" alt="\Delta Y_{t}= \alpha+ \gamma(Y_{t- 1}- \hat{\beta}_{0}- \hat{\beta}_{1}X_{t- 1})+ \sum \delta_{i}\Delta X_{t- i}+ \epsilon_{t}" width="406" height="33"></p>



<img class="fml" src="/formulas/99334f65a5e47b.png" alt="\hat{\gamma}=- 0.25" width="87" height="34"> 表示上期偏离长期均衡 1 单位，本期 Y 反向调整 0.25 单位（约修正 25%），半衰期 <img class="fml" src="/formulas/50f2cbf8b9dbcd.png" alt="\frac{\ln 0.5}{\ln 0.75} \approx 2.4" width="93" height="34"> 期；γ 必须显著为负，否则误差修正机制不成立。

### 综 8 · 面板 FE / RE 与 Hausman 检验（第 9 章）

**题**：<img class="fml" src="/formulas/dc75f399ccd881.png" alt="\hat{\beta}_{FE}=0.62(\operatorname{Var}=0.004)" width="201" height="33">，<img class="fml" src="/formulas/36b93991d03e07.png" alt="\hat{\beta}_{RE}=0.45(\operatorname{Var}=0.001)" width="200" height="33">。做 Hausman 检验并说明选哪个模型，以及 FE 的两个局限。

**解**：


<p class="fml-block"><img class="fml" src="/formulas/cf16003a99ddd1.png" alt="\begin{gathered}
H= \frac{(0.62- 0.45)^{2}}{0.004- 0.001}= \frac{0.0289}{0.003}= 9.63&gt; \chi^{2}_{0}._{05}(1)=3.84 \\
\to \; \text{拒绝「个体效应与解释变量不相关」，} \; \text{RE} \; \text{不一致，应选固定效应} \; \text{FE}
\end{gathered}" width="572" height="76"></p>


FE 的局限：① **不能估计**不随时间变化的变量（性别、地区固定属性）的系数（但能控制它们）；② 当 T 小、组内变异少时估计噪声大；③ 含被解释变量滞后项时产生 Nickell 偏误，需 GMM。
报告时还须使用**按个体聚类的稳健标准误**；可用 Mundlak-CRE 作为兼顾时不变变量与相关性的折中方案。

### 综 9 · Logit 概率、边际效应与优势比（第 10 章）

**题**：Logit 模型估计得 <img class="fml" src="/formulas/f53e9034bee567.png" alt="z=- 1+ 0.5x" width="118" height="34">。求 `x=2,4,6` 处的预测概率与边际效应、优势比，并说明为何系数不能直接当边际效应。

**解**：


<p class="fml-block"><img class="fml" src="/formulas/a63451e5cd61c1.png" alt="\begin{gathered}
P= \frac{1}{1+e^{- z}} \; \text{，边际效应} \; ME= \beta_{1} \cdot P(1- P) \\
x=2 \to z=0 \to P=0.5000 \; \text{，} \; ME=0.5 \times 0.25=0.1250 \; \text{（最大）} \\
x=4 \to z=1 \to P=0.7311 \; \text{，} \; ME=0.5 \times 0.7311 \times 0.2689=0.0983 \\
x=6 \to z=2 \to P=0.8808 \; \text{，} \; ME=0.5 \times 0.8808 \times 0.1192=0.0525 \\
OR= e^{0.5}= 1.649 \to x \; \text{每增} \; \text{1} \; \text{单位，发生比} \; \frac{P}{1- P} \; \text{变为} \; \text{1.649} \; \text{倍（} \; \text{+64.9\%} \; \text{）}
\end{gathered}" width="622" height="170"></p>


系数 β 只决定对数发生比的斜率与方向；因为连接函数是 **S 形非线性**，概率变化随 x 而变（<img class="fml" src="/formulas/2e5495f00bdcde.png" alt="P \approx 0.5" width="68" height="34"> 处最陡、两端趋平）。因此实证论文应报告 **平均边际效应 AME** 或指定点的 MEM，而非只报 β；OR 描述的是**发生比**变化，不是概率变化 64.9%。

### 易混概念对照表（速记）

| A | B | 关键区别 |
| --- | --- | --- |
| 总体扰动 u | 残差 e | 不可观测 vs 可计算；<img class="fml" src="/formulas/e58684f3085369.png" alt="\sigma^{2}" width="25" height="34"> 用 <img class="fml" src="/formulas/91da51082325af.png" alt="\frac{SSE}{n- k- 1}" width="51" height="34"> 估计 |
| 无偏性 | 一致性 | 小样本性质 vs 大样本性质，互不蕴含 |
| 异方差 | 自相关 | 方差随 i 变 vs 误差跨期相关；都不使系数有偏，但都毁掉标准误 |
| 异方差稳健 SE | 聚类稳健 SE | 只放宽同方差 vs 允许组内任意相关（面板必需） |
| 多重共线性 | 内生性 | 方差变大但无偏 vs **有偏且不一致**（更严重） |
| 遗漏变量 | 包含无关变量 | 有偏不一致 vs 无偏但效率损失 |
| R² | 调整 R² | 只增不减 vs 惩罚变量个数、可能为负、可跨模型比 |
| t 检验 | F 检验 | 单个约束 vs 多个联合约束；<img class="fml" src="/formulas/8b33403ee1b693.png" alt="t^{2}= F(1,df)" width="109" height="33"> |
| Wald | LM / LR | 只估无约束 / 只估约束 / 两者都估；大样本渐近等价 |
| 统计显著 | 经济显著 | p 值大小 vs 效应大小与政策含义 |
| 严格平稳 | 弱平稳 | 全部分布不变 vs 仅一阶二阶矩不变 |
| 趋势平稳 | 单位根过程 | 冲击暂时 vs 冲击永久；前者去趋势，后者差分 |
| ADF 的 H0 | KPSS 的 H0 | 有单位根（非平稳）vs 平稳；方向相反 |
| 协整 | Granger 因果 | 长期共同运动 vs 短期增量预测；都不等于结构因果 |
| 固定效应 | 随机效应 | 允许 μ_i 与 x 相关（一致）vs 假定不相关（更有效但可能不一致） |
| Logit 系数 | 边际效应 / OR | 对数发生比斜率 vs 概率变化 / 发生比倍数 |
| 伪 R² | OLS 的 R² | 基于似然，数值不可直接横向比较 |
| 相关关系 | 因果效应 | 条件期望的关联 vs 反事实框架下的处理效应 |

## 附录 A 公式与结论速查

| # | 主题 | 公式 / 结论 |
| --- | --- | --- |
| 1 | 总体 / 样本回归 | <img class="fml" src="/formulas/377720983ddaa6.png" alt="Y=\beta_{0}+\beta_{1}X+u" width="149" height="33">；<img class="fml" src="/formulas/eb65bfd8cbd5a8.png" alt="\hat{Y}=\hat{\beta}_{0}+\hat{\beta}_{1}X" width="118" height="33">；<img class="fml" src="/formulas/1332691600e606.png" alt="E(Y\vert X)=\beta_{0}+\beta_{1}X" width="167" height="33"> |
| 2 | OLS 估计量 | <img class="fml" src="/formulas/d35068135eef98.png" alt="\hat{\beta}_{1}= \frac{Sxy}{Sxx}= \frac{\operatorname{Cov}(X,Y)}{\operatorname{Var}(X)}" width="159" height="36">；<img class="fml" src="/formulas/3ff24ed77246f3.png" alt="\hat{\beta}_{0}= \bar{Y}- \hat{\beta}_{1}\bar{X}" width="118" height="33"> |
| 3 | 矩阵形式 | <img class="fml" src="/formulas/a04b256b344e56.png" alt="\hat{\beta}=(X&#x27;X)^{-1}X&#x27;y" width="139" height="33">；<img class="fml" src="/formulas/0865b36a8d57f4.png" alt="\operatorname{Var}(\hat{\beta})=\sigma^{2}(X&#x27;X)^{-1}" width="170" height="33"> |
| 4 | σ² 无偏估计 | <img class="fml" src="/formulas/517b88f0839479.png" alt="\hat{\sigma}^{2}= \frac{SSE}{n- k- 1}" width="94" height="34">（一元时 n−2） |
| 5 | 分解式 | `SST = SSR + SSE`；<img class="fml" src="/formulas/ca7f32b8d79545.png" alt="R^{2}= \frac{SSR}{SST}= 1- \frac{SSE}{SST}" width="167" height="33"> |
| 6 | 调整 R² | <img class="fml" src="/formulas/a12a2c7c96bed7.png" alt="\bar{R}^{2}= 1- \frac{(1- R^{2})(n- 1)}{n- k- 1}" width="160" height="36"> |
| 7 | 系数标准误 | <img class="fml" src="/formulas/15ddb8995e927d.png" alt="se(\hat{\beta}_{1})=\sqrt{\frac{\hat{\sigma}^{2}}{Sxx}}" width="124" height="42">；多元取 <img class="fml" src="/formulas/d957dda7507115.png" alt="\hat{\sigma}^{2}(X&#x27;X)^{-1}" width="92" height="33"> 对角元开方 |
| 8 | t 检验 | <img class="fml" src="/formulas/17208cc04e6ae0.png" alt="t=\frac{\hat{\beta}- \beta_{H0}}{se(\hat{\beta})} \sim t(n- k- 1)" width="197" height="40">；<img class="fml" src="/formulas/058c772a1f1204.png" alt="F=t^{2}" width="58" height="33"> |
| 9 | 置信区间 | <img class="fml" src="/formulas/1e0db6031f16a4.png" alt="\hat{\beta} ± t_{\frac{\alpha}{2}} \cdot se(\hat{\beta})" width="112" height="34">；大样本用 1.96 |
| 10 | 整体 F | <img class="fml" src="/formulas/b7e51834a18176.png" alt="F= \frac{\frac{R^{2}}{k}}{\frac{1- R^{2}}{n- k- 1}}" width="82" height="47"> |
| 11 | 约束 F | <img class="fml" src="/formulas/db11dd296567b0.png" alt="F= \frac{\frac{SSE_{r}- SSE_{u}}{q}}{\frac{SSE_{u}}{n- k- 1}}" width="109" height="46"> |
| 12 | 三大检验 | Wald / LM / LR 渐近 <img class="fml" src="/formulas/5a62ee3d300fcd.png" alt="\sim \chi^{2}(q)" width="66" height="34">；<img class="fml" src="/formulas/9a3c5929d23279.png" alt="LM= n \cdot R^{2}_{aux}" width="121" height="33"> |
| 13 | 信息准则 | <img class="fml" src="/formulas/ae0ea0264cfe57.png" alt="AIC= \ln\left(\frac{SSE}{n}\right)+\frac{2(k+1)}{n}" width="197" height="33">；<img class="fml" src="/formulas/a5f049e4fdc239.png" alt="SC= \ln\left(\frac{SSE}{n}\right)+\frac{(k+1)\ln(n)}{n}" width="211" height="33"> |
| 14 | 遗漏变量偏误 | <img class="fml" src="/formulas/8b5c087648b8af.png" alt="plim \tilde{\beta}_{1}= \beta_{1}+ \beta_{2} \cdot \delta_{1}" width="169" height="34">（δ1 为 X2 对 X1 辅助回归斜率） |
| 15 | 弹性 | 双对数模型 <img class="fml" src="/formulas/459fa3cec78d9d.png" alt="\beta_{1}= \frac{dlnY}{dlnX}" width="82" height="33">；<img class="fml" src="/formulas/03f4e3b04f45ff.png" alt="\epsilon=\left(\frac{dY}{dX}\right)\left(\frac{X}{Y}\right)" width="111" height="33"> |
| 16 | 均值 / 个别值预测 SE | <img class="fml" src="/formulas/4c4ce8e3555522.png" alt="\hat{\sigma}\sqrt{\frac{1}{n}+ \frac{(X_{0}- \bar{X})^{2}}{Sxx}}" width="126" height="41"> / <img class="fml" src="/formulas/6c1cac4645a522.png" alt="\hat{\sigma}\sqrt{1+ \frac{1}{n}+ \frac{(X_{0}- \bar{X})^{2}}{Sxx}}" width="156" height="41"> |
| 17 | VIF | <img class="fml" src="/formulas/7d519cb5ca9add.png" alt="VIF_{j}= \frac{1}{1- R^{2}_{j}}" width="108" height="40">；<img class="fml" src="/formulas/310fb78b8bc0dd.png" alt="\operatorname{Var}(\hat{\beta}_{j})=\sigma^{2}/[Sxx_{j}(1- R^{2}_{j})]" width="232" height="34">；>10 严重 |
| 18 | BP / White 检验 | <img class="fml" src="/formulas/b8bc79ab68e87c.png" alt="LM= n \cdot R^{2}_{aux} \sim \chi^{2}(df)" width="197" height="33">；<img class="fml" src="/formulas/566741a9168d4b.png" alt="\chi^{2}_{0}._{05}(1)=3.84,(2)=5.99,(3)=7.81" width="295" height="33"> |
| 19 | Goldfeld-Quandt | <img class="fml" src="/formulas/3c2dc636a4ce29.png" alt="F= \frac{SSE_{2}}{SSE_{1}}" width="81" height="35">（按可疑变量排序、去中间段） |
| 20 | WLS | <img class="fml" src="/formulas/eb8f7f81e3bdd9.png" alt="\operatorname{Var}(u_{i})=\sigma^{2}w_{i}" width="125" height="33"> ⇒ 两边除 <img class="fml" src="/formulas/2176583523f5cc.png" alt="\sqrt{w}_{i}" width="40" height="34"> 后 OLS |
| 21 | 稳健标准误 | <img class="fml" src="/formulas/d35bc4b48857f2.png" alt="HC0- HC3" width="108" height="33"> 修异方差；Newey-West(HAC) 同时修异方差与自相关 |
| 22 | DW | <img class="fml" src="/formulas/e79b012c354507.png" alt="d= \frac{\sum(e_{t}- e_{t- 1})^{2}}{\sum e_{t}^{2}} \approx 2(1- \hat{\rho})" width="201" height="39">；d≈2 无自相关 |
| 23 | BG-LM | <img class="fml" src="/formulas/0dcf5184dff81a.png" alt="(n- p)R^{2}_{aux} \sim \chi^{2}(p)" width="162" height="34">，可检高阶、允许滞后被解释变量 |
| 24 | 广义差分 | <img class="fml" src="/formulas/92d6a86b54141d.png" alt="Y_{t}- \rho Y_{t- 1}= \beta_{0}(1- \rho)+\beta_{1}(X_{t}- \rho X_{t- 1})+v_{t}" width="356" height="33"> |
| 25 | 2SLS | 第一阶段 <img class="fml" src="/formulas/c2d637fe3c5ce0.png" alt="X=\Pi Z+v" width="105" height="33"> 得 X̂；第二阶段 `Y` 对 X̂ 回归 |
| 26 | 弱工具判据 | 第一阶段 F < 10 提示弱工具；Hansen J 检验过度识别 |
| 27 | 分布滞后 | <img class="fml" src="/formulas/24972142d0868c.png" alt="Y_{t}=\alpha+\sum \beta_{i}X_{t-i}+u_{t}" width="189" height="33">；长期乘数 <img class="fml" src="/formulas/f88144714ab1fd.png" alt="\sum \beta_{i}" width="44" height="33"> |
| 28 | Koyck / 部分调整 | <img class="fml" src="/formulas/eeca1c7376df76.png" alt="Y_{t}=\alpha(1- \lambda)+\beta_{0}X_{t}+\lambda Y_{t- 1}+v_{t}" width="272" height="33">；长期乘数 <img class="fml" src="/formulas/ea678a39bbb918.png" alt="\beta_{0}/(1- \lambda)" width="88" height="33"> |
| 29 | 平均滞后 | <img class="fml" src="/formulas/21dd925deaca92.png" alt="\approx \frac{\lambda}{1- \lambda}" width="54" height="34"> |
| 30 | Granger F | <img class="fml" src="/formulas/d7f31d5c04ec29.png" alt="F=\frac{\frac{SSE_{r}- SSE_{u}}{q}}{\frac{SSE_{u}}{n- k}}" width="108" height="46"> |
| 31 | AR(1) 平稳 | <img class="fml" src="/formulas/da253f240ad45b.png" alt="\vert \phi\vert &lt;1" width="60" height="34">；<img class="fml" src="/formulas/abe859aced2e63.png" alt="\phi=1" width="51" height="34"> 为单位根 |
| 32 | ADF | <img class="fml" src="/formulas/3244c14aa9f8bc.png" alt="\Delta Y_{t}=\alpha+\beta t+\gamma Y_{t- 1}+\sum \delta_{i}\Delta Y_{t- i}+\epsilon_{t}" width="311" height="34">；<img class="fml" src="/formulas/e28af2fdb3f16f.png" alt="H_{0}: \gamma=0" width="87" height="33">，用 MacKinnon 临界值 |
| 33 | 单整 | <img class="fml" src="/formulas/6952fb27654c4c.png" alt="Y \sim I(d)" width="78" height="34"> 表示差分 d 次平稳 |
| 34 | 协整 | <img class="fml" src="/formulas/72e41878104488.png" alt="u_{t}=Y_{t}- \beta_{0}- \beta_{1}X_{t} \sim I(0)" width="216" height="34">；EG 两步 + AEG 检验 |
| 35 | ECM | <img class="fml" src="/formulas/c86b189f73c542.png" alt="\Delta Y_{t}=\alpha+\gamma \cdot ECM_{t- 1}+\sum \delta_{i}\Delta X_{t- i}+\epsilon_{t}" width="325" height="34">，<img class="fml" src="/formulas/fe170df363e532.png" alt="\gamma&lt;0" width="49" height="34"> 为调整速度 |
| 36 | 半衰期 | <img class="fml" src="/formulas/b37d2d02961dc2.png" alt="\dfrac{\ln(0.5)}{\ln(1+\gamma)}" width="81" height="51">（γ<0 时） |
| 37 | GARCH(1,1) | <img class="fml" src="/formulas/90eed318dc10d2.png" alt="\sigma^{2}_{t}=\omega+\alpha \epsilon^{2}_{t- 1}+\beta \sigma^{2}_{t- 1}" width="187" height="34">；<img class="fml" src="/formulas/b7dcc33d2e28aa.png" alt="\alpha+\beta \approx 1" width="84" height="34"> 波动持久 |
| 38 | 联立性偏误 | <img class="fml" src="/formulas/d39ae79b031976.png" alt="\operatorname{Cov}(Y_{t},u_{t})\ne 0" width="125" height="33"> <img class="fml" src="/formulas/e667a8be113ba1.png" alt="\Rightarrow" width="24" height="34"> 有偏且不一致（乘数 <img class="fml" src="/formulas/a737e5df1559ea.png" alt="\frac{1}{1- \beta}" width="35" height="36">） |
| 39 | 识别阶条件 | <img class="fml" src="/formulas/a9b094da01dd25.png" alt="K- k \ge g- 1" width="119" height="34">（排除的前定变量数 ≥ 方程内内生变量数 −1） |
| 40 | 秩条件 | 被排除变量系数矩阵存在非零 <img class="fml" src="/formulas/00b68d8e5f69a3.png" alt="G- 1" width="52" height="34"> 阶行列式（充要） |
| 41 | ILS / 2SLS | 恰好识别用 ILS；过度识别用 2SLS / LIML / GMM |
| 42 | 面板设定 | <img class="fml" src="/formulas/c4909a88cf8b78.png" alt="y_{it}=\alpha+\beta &#x27;x_{it}+\mu_{i}+\lambda_{t}+\epsilon_{it}" width="232" height="34"> |
| 43 | 组内变换 | <img class="fml" src="/formulas/4869c44f08397c.png" alt="y_{it}- \bar{y}_{i}= \beta &#x27;(x_{it}- \bar{x}_{i})+(\epsilon_{it}- \bar{\epsilon}_{i})" width="259" height="34">，消去 μ_i |
| 44 | RE 拟去均值 | <img class="fml" src="/formulas/0eab0c36c71939.png" alt="y_{it}- \theta \bar{y}_{i}" width="70" height="34">，<img class="fml" src="/formulas/2ee7ba1ec47769.png" alt="\theta=1- \frac{\sigma_\epsilon}{\sqrt{\sigma_\epsilon^{2}+T\sigma_\mu^{2}}}" width="135" height="42"> |
| 45 | Hausman | <img class="fml" src="/formulas/f036350273e111.png" alt="H=(\hat{\beta}_{FE}- \hat{\beta}_{RE})&#x27;[\operatorname{Var}(\hat{\beta}_{FE})- \operatorname{Var}(\hat{\beta}_{RE})]^{-1}(\hat{\beta}_{FE}- \hat{\beta}_{RE}) \sim \chi^{2}(k)" width="507" height="34"> |
| 46 | 例题数值 | `H=9.63>3.84` ⇒ 选 FE；`H=1.63<3.84` ⇒ 不拒绝 RE |
| 47 | Logit | <img class="fml" src="/formulas/6038dd34743ee9.png" alt="P=\frac{1}{1+e^{- z}}" width="83" height="35">，<img class="fml" src="/formulas/af13c99886a75e.png" alt="z=\beta &#x27;X" width="72" height="34">；<img class="fml" src="/formulas/aaa490e2ad67a3.png" alt="ME_{j}=\beta_{j} P(1- P)" width="159" height="34">；<img class="fml" src="/formulas/b6ac046b6d4ea4.png" alt="OR=e^{\beta_{j}}" width="80" height="34"> |
| 48 | Probit | <img class="fml" src="/formulas/56b6d709f4b162.png" alt="P=\Phi(z)" width="81" height="34">；<img class="fml" src="/formulas/280f3d1d3473e9.png" alt="ME_{j}=\beta_{j} \phi(z)" width="120" height="34">；<img class="fml" src="/formulas/32d7d5d140e426.png" alt="\phi(1)=0.2420" width="114" height="34"> |
| 49 | 对数似然 | <img class="fml" src="/formulas/a489861cf84025.png" alt="lnL=\sum[y_{i} lnF(z_{i})+(1- y_{i})\ln(1- F(z_{i}))]" width="344" height="34"> |
| 50 | LR 检验 / 伪 R² | <img class="fml" src="/formulas/c0df6293868b2a.png" alt="LR=2(lnL_{u}- lnL_{r}) \sim \chi^{2}(q)" width="238" height="34">；<img class="fml" src="/formulas/beace343bf32c9.png" alt="McFadden R^{2}=1- \frac{lnL_{u}}{lnL_{r}}" width="201" height="35"> |
| 51 | Logit 例题 | <img class="fml" src="/formulas/38699b5314d2f0.png" alt="z=- 1+0.5x" width="117" height="34">：<img class="fml" src="/formulas/efca97b999f829.png" alt="x=4 \Rightarrow P=0.7311" width="166" height="34">，ME=0.0983，OR=1.649 |
| 52 | 常用临界值 | z: 1.96(双侧5%)；t(3)=3.182；<img class="fml" src="/formulas/50b6279492f20e.png" alt="\chi^{2}(1)=3.84" width="103" height="34">；<img class="fml" src="/formulas/0cf70ded114bd8.png" alt="F(2,26) \approx 3.37" width="125" height="34"> |

## 附录 B 易错点速查

1. 计量经济学不是「跑回归软件」：理论设定、识别策略与诊断比估计命令更重要。
2. 随机扰动项 u 不可观测；残差 e 是它的估计，二者不能混用。
3. 混合数据（不同时点不同个体）≠ 面板数据（同一批个体跨期追踪）。
4. 高 R² 不等于模型正确、更不等于因果；低 R² 也不等于模型无用。
5. 点预测之外应给预测区间；样本外远推风险很大。
6. 「统计显著」与「经济显著」是两回事，n 很大时微小系数也会显著。

7. 抽样分布是**估计量**的分布，不是样本数据的分布。
8. 无偏是小样本性质，一致是大样本性质；二者互不蕴含。
9. 有效性只在「同类（线性无偏）」估计量内比较；有偏估计方差可以更小。
10. <img class="fml" src="/formulas/bacf3b84577197.png" alt="\operatorname{Var}(aX+b)=a^{2}\operatorname{Var}(X)" width="208" height="33">；常数项不影响方差但影响期望。
11. 协方差为 0 只说明无**线性**相关，不能推出独立。
12. t 分布来自 <img class="fml" src="/formulas/5613bb168cdfaa.png" alt="\frac{Z}{\sqrt{\chi^{2} m}}" width="51" height="42">；F 来自两个独立 χ² 之比除以各自自由度。
13. <img class="fml" src="/formulas/8e0d43b0d67dc2.png" alt="t^{2}(m)=F(1,m)" width="134" height="34">；大样本下 `Wald/LM/LR` 都渐近 <img class="fml" src="/formulas/34f6bdc4fc1236.png" alt="\chi^{2}(q)" width="48" height="34">。
14. 95% 置信区间是「反复抽样区间覆盖真值的频率」，不是「真值有 95% 概率落在此区间」。
15. 第一类错误概率 = α；第二类错误概率 = β，功效 <img class="fml" src="/formulas/dfa10968c0706d.png" alt="1- \beta" width="49" height="34">；α 与 β 此消彼长。
16. 「不拒绝 H0」≠「接受 H0」；p 值不是「H0 为真的概率」。

17. OLS 的「线性」指对**参数**线性，<img class="fml" src="/formulas/2a12cfac2e9f64.png" alt="Y=\beta_{0}+\beta_{1}X^{2}+u" width="157" height="34"> 仍属线性回归。
18. 高斯-马尔可夫定理**不要求正态性**；正态性只用于小样本精确 t/F 推断。
19. BLUE 的「最佳」限于线性无偏类，且 <img class="fml" src="/formulas/4f2ce3536534b9.png" alt="A1- A6" width="74" height="34"> 任一被破坏结论即失效。
20. <img class="fml" src="/formulas/517b88f0839479.png" alt="\hat{\sigma}^{2}= \frac{SSE}{n- k- 1}" width="94" height="34"> 的分母是自由度，不是 n；MLE 用 n 但有偏。
21. `SST=SSR+SSE` 只在**含截距且用 OLS** 时成立，无截距模型不成立。
22. 回归线必过 `(X̄, Ȳ)`；含截距时残差和为 0、残差与 X 不相关。
23. <img class="fml" src="/formulas/b5f2662fd9704d.png" alt="R^{2}" width="27" height="33"> 单调不减，不能跨不同被解释变量（线性 vs 对数）比较。
24. 调整 R² 可能为负；加变量后要同时看调整 R²、AIC/SC 与理论依据。
25. t 检验显著只能说明线性关联，不能推出因果关系。
26. 个别值预测区间**宽于**均值预测区间（多一个扰动项方差）。
27. 小样本 t/F 推断依赖误差正态性；大样本可用渐近正态与稳健标准误。
28. 遗漏变量会导致系数有偏且不一致；包含无关变量只损失效率。

29. 偏回归系数必须带「其它变量不变」的前提。
30. 遗漏变量偏误方向 = <img class="fml" src="/formulas/3ea1eb2b1e6e2d.png" alt="sign(\beta_{2}) \times sign(Corr(X_{1},X_{2}))" width="248" height="34">。
31. 控制「受处理影响」的变量（坏控制）会阻断因果路径，制造偏误。
32. 虚拟变量 m 类只放 m−1 个；全放且含截距 ⇒ 虚拟变量陷阱（完全共线）。
33. 交互项显著时，主效应只代表「另一变量为 0」时的效应。
34. 双对数模型系数是弹性；线性-对数、对数-线性的解释各不相同。
35. 对数变换要求变量取正值；零值不能直接取对数。
36. 单个 t 不显著而整体 F 显著，常是多重共线性的信号。

37. 异方差与自相关**不使系数有偏**，只毁掉标准误、t/F 与置信区间。
38. 内生性（遗漏变量、反向因果、测量误差）才使系数**有偏且不一致**。
39. 增大样本能救不一致之外的多数问题，但**救不了内生性**。
40. VIF = <img class="fml" src="/formulas/bf5c9005fa9318.png" alt="\frac{1}{1- R^{2}_{j}}" width="42" height="40">；VIF=10 意味着标准误约为 <img class="fml" src="/formulas/a6227a1c6dda30.png" alt="\sqrt{10} \approx 3.16" width="95" height="34"> 倍。
41. 多重共线下**预测**在共线模式延续时仍可可靠，只是单个系数不可靠。
42. 稳健标准误只修标准误，不修设定错误、不修内生性。
43. 面板 / 分组数据要用**聚类稳健标准误**，仅用异方差稳健仍会低估。
44. DW 只检一阶 AR(1)，且要求解释变量**不含被解释变量滞后项**、含截距、无缺失值。
45. 含 <img class="fml" src="/formulas/6e0c6113102043.png" alt="Y_{t- 1}" width="38" height="34"> 时 DW 偏向 2 易漏检，应改用 Durbin h 或 Breusch-Godfrey LM。
46. DW 有「不可判定区」（d_L、d_U），不能只凭 d≈2 下结论。
47. <img class="fml" src="/formulas/76a3e1d3423ad1.png" alt="d=0.8 \to \hat{\rho}=0.6" width="146" height="34">；<img class="fml" src="/formulas/5e6b37fcff9587.png" alt="d=2 \to \hat{\rho}=0" width="119" height="34">；<img class="fml" src="/formulas/9a31bc2e4b4151.png" alt="d=3.4 \to \hat{\rho}=- 0.7" width="160" height="34">。
48. DW 偏低也可能是**遗漏滞后变量**造成的伪自相关，先查设定再修误差。
49. 工具变量必须同时满足相关性与**排他性**（只通过 X 影响 Y）。
50. 弱工具（第一阶段 F<10）会让 2SLS 偏误且 Wald 检验失真。
51. IV 在异质效应下识别的是 **LATE**（compliers 的局部平均效应），不是全样本 ATE。
52. RESET 显著提示函数形式误设定，但不告诉你要加什么变量。

53. 分布滞后模型的长期乘数是 <img class="fml" src="/formulas/f88144714ab1fd.png" alt="\sum \beta_{i}" width="44" height="33">，不是当期系数 β0。
54. Koyck / 部分调整 / 适应预期的回归式相似，但经济含义与扰动结构不同。
55. Koyck 变换后扰动为 MA(1) 且与 <img class="fml" src="/formulas/6e0c6113102043.png" alt="Y_{t- 1}" width="38" height="34"> 相关 <img class="fml" src="/formulas/e667a8be113ba1.png" alt="\Rightarrow" width="24" height="34"> 不一致。
56. 「Granger 因果」是增量**预测**能力，不是结构因果；反向因果也要检验。
57. Granger 检验前须处理非平稳性，且结论对滞后阶数敏感。
58. 滞后阶数用 AIC/SC 选；逐步删项的预检验会扭曲 t 统计量的分布。

59. 弱平稳要求均值、方差**与**自协方差都只依赖间隔而非时点。
60. 确定性趋势序列不平稳，但去趋势后平稳（趋势平稳），与单位根过程不同。
61. 单位根过程的冲击有**永久**效应，趋势平稳的冲击是暂时的。
62. 两个独立随机游走互相回归会产生**伪回归**（高 R²、显著 t、低 DW）。
63. ADF 的 H0 是「有单位根」，要用 MacKinnon 临界值，不是标准 t 的 1.96。
64. KPSS 的原假设与 ADF 相反（平稳），可联合使用确认。
65. 协整要求同阶单整（EG 框架）；`I(0)/I(1)` 混合用 ARDL 边界检验。
66. 协整 ⇒ 必存在 ECM 表示；<img class="fml" src="/formulas/fe170df363e532.png" alt="\gamma&lt;0" width="49" height="34"> 才是向均衡回调，且差分过大会丢长期信息。

67. 联立方程中内生变量与扰动相关 <img class="fml" src="/formulas/e667a8be113ba1.png" alt="\Rightarrow" width="24" height="34"> 有偏且**不一致**。
68. 恒等式没有待估参数，但仍计入方程总数 G。
69. 识别阶条件只是**必要**条件，秩条件才是充要条件。
70. 恰好识别可用 ILS；过度识别须用 2SLS / LIML / GMM。
71. 2SLS 第二阶段标准误要用原始内生变量计算的残差修正，不能直接用拟合值。
72. 简化式系数是总效应（含乘数 <img class="fml" src="/formulas/a737e5df1559ea.png" alt="\frac{1}{1- \beta}" width="35" height="36">），不等于结构系数。

73. FE 用组内变换消去 μ_i，允许 <img class="fml" src="/formulas/0396ada14c269a.png" alt="\operatorname{Cov}(\mu_{i},x)=0" width="120" height="34">，一致性更强。
74. FE **不能估计**时不变变量的系数，但能控制它们的影响。
75. RE 更有效的代价是强假定 <img class="fml" src="/formulas/0396ada14c269a.png" alt="\operatorname{Cov}(\mu_{i},x)=0" width="120" height="34">，违反则不一致。
76. Hausman 显著 ⇒ 拒绝 RE、选 FE；不显著只表示「证据不足」，不等于假定成立。
77. 含滞后被解释变量的短面板 FE 有 **Nickell 偏误**（约 <img class="fml" src="/formulas/d06bad634893b6.png" alt="- \frac{1}{T}" width="34" height="34">），须用系统 GMM。
78. 面板标准误必须按个体聚类；聚类数少时用 wild cluster bootstrap。
79. 交错处理时点的 TWFE 在异质效应下可能偏误，需专用稳健估计量。

80. LPM 的预测概率可能越出 [0,1]，且必然异方差（<img class="fml" src="/formulas/69cc84c730d957.png" alt="p(1- p)" width="69" height="34">）。
81. Logit/Probit 的 β **不是**边际效应；边际效应随 X 变化。
82. 优势比 <img class="fml" src="/formulas/2979c42ee7f4a8.png" alt="e^\beta" width="24" height="34"> 描述的是**发生比**变化，不是概率变化。
83. <img class="fml" src="/formulas/9d0dd7acdaa75c.png" alt="\beta_{Logit} \approx 1.6 \beta_{Probit}" width="141" height="34">（因分布方差不同），系数数值不可直接比较。
84. 伪 R² 与 OLS 的 R² 不可比；不平衡样本下高分类准确率可能是假象。
85. 多项 Logit 须满足 **IIA**，有序模型须满足**平行线假定**，都要检验。
86. Tobit 处理角点堆积（删失），Heckman 处理非随机样本选择，二者不是一回事。
87. 非线性模型交互项的显著性不能只看乘积项系数（<img class="fml" src="/formulas/45e602082c43a4.png" alt="Ai- Norton" width="107" height="33"> 问题）。

88. 「相关 ≠ 因果」贯穿全书：系数能作因果解释的前提是**识别成立**（外生性、无遗漏、无同时性、样本无选择性偏差），而不是 t 值够大。

