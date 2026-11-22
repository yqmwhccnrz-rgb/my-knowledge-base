---
summary: "高等数学 全面详解笔记，将上下册内容按知识逻辑综合为 12 章（不分册）：函数极限与连续、导数与微分、微分中值定理与导数应用、不定积分、定积分与反常积分、定积分的应用、常微分方程、向量代数与空间解析几何、多元函数微分学及其应用、重积分、曲线积分与曲面积分及场论、无穷级数。覆盖 ε-δ 定义与两个重要极限、等价无穷小与泰勒公式、中值定理与洛必达、三类积分法与微积分基本定理、微元法、一阶/二阶常系数微分方程、三种向量积与平面直线、偏导数全微分方向导数梯度与拉格朗日乘数、二重三重积分与换序及极柱球坐标、两类线面积分与格林/高斯/斯托克斯公式、常数项级数审敛与幂级数傅里叶级数。含 18 张自绘图、12 道逐步演算代码块、11 组深挖专题、8 个公式推导补遗、8 道跨章综合例题、12 章高频题型清单、50 组易混概念对照、48 条补充与修正汇总、记号与中英术语速查、附录 A 十组公式速查与一页纸解题索引、附录 B 104 条易错点。"
---

# 高等数学笔记

::: info 笔记概要
- **所属课程**：高等数学（理工科 / 经管类等专业公共基础课）。
- **编写说明**：本笔记把两份教材的内容**综合成一条知识链，不分上下册**——先学一元函数微积分（第 1–6 章），再学微分方程（第 7 章），然后引入空间与多元（第 8–11 章），最后以无穷级数收束（第 12 章）。
- **核心内容**：全书只有两条主线。① **极限**：导数是差商的极限、定积分是黎曼和的极限、重积分与线面积分是微元法的极限、级数是部分和的极限；② **互逆与推广**：$\int_{a}^{b} f dx= F(b)- F(a)$ 是牛顿–莱布尼茨公式，格林、高斯、斯托克斯都是它在高维的推广（统一于广义斯托克斯定理）。抓住这两条，12 章就是一个整体。
- **学习建议**：每个定理都要能说清「条件、结论、逆命题是否成立」；每道计算题都要写出「识别类型 → 选方法 → 逐步演算 → 验算」；证明题要掌握辅助函数构造与中值定理的选用。
:::

## 全书目录

| 章 | 主题 | 核心考点 | 重要度 |
| --- | --- | --- | --- |
| 1 | 函数、极限与连续 | 函数四性质、ε-δ 定义、两个重要极限、等价无穷小、间断点分类、闭区间连续性质、泰勒公式 | ★★★ |
| 2 | 导数与微分 | 导数定义、可导连续可微关系、复合/隐函数/参数方程求导、高阶导数与莱布尼茨公式 | ★★★ |
| 3 | 微分中值定理与导数应用 | 罗尔/拉格朗日/柯西/泰勒、洛必达、单调凹凸拐点、极值与最值、渐近线、曲率 | ★★★ |
| 4 | 不定积分 | 原函数、两类换元、分部积分、有理函数/三角有理式/简单无理函数 | ★★★ |
| 5 | 定积分与反常积分 | 黎曼和、积分上限函数、牛顿–莱布尼茨、奇偶周期与区间再现、华里士公式、两类反常积分判敛 | ★★★ |
| 6 | 定积分的应用 | 微元法、面积/体积/弧长、变力做功、液体压力、质心与平均值 | ★★ |
| 7 | 常微分方程 | 可分离变量/齐次/一阶线性/伯努利/全微分、可降阶、二阶常系数齐次与非齐次、欧拉方程 | ★★★ |
| 8 | 向量代数与空间解析几何 | 数量积/向量积/混合积、平面与直线方程、夹角与距离、旋转曲面、二次曲面、投影 | ★★★ |
| 9 | 多元函数微分学及其应用 | 二重极限、偏导数与全微分、链式法则、隐函数、方向导数与梯度、切平面法线、极值、拉格朗日乘数 | ★★★ |
| 10 | 重积分 | 二重积分直角坐标/极坐标/换序、三重积分投影截面法/柱坐标/球坐标、曲面面积与质心 | ★★★ |
| 11 | 曲线积分、曲面积分与场论 | 两类线积分、两类面积分、格林公式、路径无关与全微分求积、高斯公式、斯托克斯公式、散度旋度 | ★★★ |
| 12 | 无穷级数 | 常数项级数审敛、绝对/条件收敛、幂级数收敛半径与和函数、函数展开、傅里叶级数与收敛定理 | ★★★ |
| 演 | 典型计算题逐步演算 | 12 道「识别 → 求解 → 验算」可照抄格式 | ★★★ |
| 图 | 图形读图专题 | 18 张图怎么画、怎么读 + 手绘 Check | ★★ |
| 型 | 各章高频题型与解题套路 | 12 章「见到题目 → 标准动作」操作手册 | ★★★ |
| 推 | 重要公式推导补遗 | 8 个高频公式的「为什么」（华里士、泊松、三大公式统一等） | ★★★ |
| 综 | 综合例题精讲 | 8 道跨章大题（极限→积分→级数→多元完整链条）+ 证明四步模板 | ★★★ |
| 对 | 易混概念对照 | 50 组高频易混概念辨析 | ★★★ |
| 号 | 记号与术语速查 | 数学记号、中英文术语对照 | ★★ |
| 附 A / B | 速查 | 十组公式速查 + 一页纸解题索引、104 条易错点 | 复习用 |

---

## 第 1 章 函数、极限与连续（★★★）

### 1.1 函数的基本概念

![高等数学知识体系总览](/math/math-overview.svg)

![函数四要素、四性质与常见函数族](/math/math-function.svg)

| 概念 | 定义 / 判据 | 要点 |
| --- | --- | --- |
| 函数 | $y= f(x), x \in D$ | **两要素**：定义域 D 与对应规则 f；二者完全相同才是同一函数 |
| 有界 | $\exists M> 0,\vert f(x)\vert  \le M$ | 有界性依赖于所给区间（如 `1/x` 在 (0,1) 无界、在 [1,2] 有界） |
| 单调 | $x_{1}< x_{2} \Rightarrow f(x_{1}) \le f(x_{2})$ | 严格单调是反函数存在的充分条件 |
| 奇偶 | $f(- x)=- f(x)$ / $f(- x)= f(x)$ | 前提：定义域关于原点对称；奇函数若在 0 有定义则 $f(0)=0$ |
| 周期 | $f(x+T)=f(x)$ | $\sin x,\cos x$ 周期 $2\pi$；$\tan x$ 周期 $\pi$；常数函数无最小正周期 |
| 反函数 | 一一对应才有反函数 | $\dfrac{dy}{dx}= \dfrac{1}{\dfrac{dx}{dy}}$；原函数与反函数图像关于 $y=x$ 对称 |
| 复合函数 | $f \circ g$ 要求 $R_g\subseteq D_f$ | 分层拆解是链式求导的前提 |
| 初等函数 | 基本初等函数经有限次四则与复合、且能写成一个式子 | 在定义区间内连续；分段函数一般**不是**初等函数 |

::: danger 易错 · 函数
- 判定奇偶性**第一步**是检查定义域是否关于原点对称，否则直接判「非奇非偶」。
- $\arcsin(\sin x)= x$（仅在 $[- \dfrac{\pi}{2}, \dfrac{\pi}{2}]$ 成立）；$\sqrt{x^{2}}=|x|$，不是 `x`；$\ln(e^{x})=x$ 但 $e^{\ln x}=x$ 需 `x>0`。
- 符号函数 `sgn x`、取整函数 `[x]`、狄利克雷函数、积分上限函数 $\Phi(x)= \int_{a}^{x} f(t)dt$ 都不是初等函数，但常考。
:::

### 1.2 极限的定义与性质

![极限定义、等价无穷小与两个重要极限](/math/math-limit.svg)

**ε–δ 定义**：$\lim_{x \to x_{0}} f(x)= A \Leftrightarrow \forall \epsilon>0, \exists \delta>0, 0<|x- x_{0}|<\delta \Rightarrow|f(x)- A|<\epsilon$。
数列版：$\lim a_{n}= A \Leftrightarrow \forall \epsilon>0, \exists N, n>N \Rightarrow|a_{n}- A|<\epsilon$。
注意定义中 $x= x_{0}$（去心），故 $f(x_{0})$ 可以无定义、也可以不等于 A —— 这正是可去间断点的来源。

| 性质 | 内容 |
| --- | --- |
| 唯一性 | 极限若存在必唯一 |
| 局部有界 / 保号 | $\lim f= A> 0 \Rightarrow$ 去心邻域内 `f > 0`；反之由 $f \ge 0$ 只能得 $A \ge 0$ |
| 四则运算 | 各极限存在且分母极限非零时才可拆分；$\infty- \infty$、$0 \cdot_{\infty}$ 不能直接拆 |
| 左右极限 | $\lim_{x \to x_{0}} f= A \Leftrightarrow f(x_{0}^{-})= f(x_{0}^{+})= A$ |
| 夹逼准则 | $g \le f \le h$ 且 $\lim g= \lim h= A \Rightarrow \lim f= A$ |
| 单调有界准则 | 单调有界数列必有极限（用于递推数列 $a_{n+1}= f(a_{n})$） |
| 两个重要极限 | $\lim_{x \to 0} \dfrac{\sin x}{x}= 1$；$\lim_{x \to \infty}\left(1+\dfrac{1}{x}\right)^{x}= e$、$\lim_{x \to 0}(1+x)^{\dfrac{1}{x}}= e$ |

::: tip 补充 · 海涅定理（归结原则）
$\lim_{x \to x_{0}} f(x)= A$ ⇔ 对任意满足 $x_{n} \to x_{0}$（$x_{n}=x_{0}$）的数列都有 $f(x_{n}) \to A$。它把**函数极限化为数列极限**，两大用途：① 证明极限不存在——找两个收敛到同一点的数列使 $f(x_{n})$ 极限不同（如 $f=\sin\left(\dfrac{1}{x}\right)$ 在 0 处取 $x_{n}=\dfrac{1}{2n\pi}$ 与 $x_{n}=\dfrac{1}{2n\pi+\dfrac{\pi}{2}}$）；② 把数列极限转为函数极限来算（先求 $\lim_{x \to \infty}f(x)$ 得 $\lim a_{n}$，反之不行）。
:::

::: tip 工作例题 · 七类未定式的处理
- $\dfrac{0}{0}$：$\lim_{x \to 0} \dfrac{\sin 3x}{5x}= \dfrac{3}{5}$（重要极限），$\lim_{x \to 0}\dfrac{e^{x}- 1- x}{x^{2}}= \dfrac{1}{2}$（泰勒或洛必达）。
- $1^\infty$：先取对数或用速算 $\lim f^g= e^{\lim g(f- 1)}$；$\lim_{n \to \infty}\left(1+\dfrac{2}{n}\right)^{n}= e^{2} \approx 7.3891$（数值验证：n=10000 时 7.3876）。
- $\infty- \infty$：$\tan x- \sin x$ 型不能逐项替换，$\lim_{x \to 0}\dfrac{\tan x- \sin x}{x^{3}}= \dfrac{1}{2}$（数值验证 0.500000）。
- $0 \cdot_{\infty}$ 化为 $\dfrac{0}{0}$；$0^{0}$、$\infty^{0}$ 取对数；$\dfrac{\infty}{\infty}$ 用洛必达或提最高阶。
:::

**常用等价无穷小**（$x \to 0$，**只能在乘除因子中替换**）：

<div class="kb-tile-2col">

<div class="kb-tile-item kb-tile-wide">

$\sin x \sim \tan x \sim \arcsin x \sim \arctan x \sim \ln(1+x) \sim e^{x}- 1 \sim x$

</div>

<div class="kb-tile-item">

$1-\cos x \sim \dfrac{x^{2}}{2}$

</div>

<div class="kb-tile-item">

$(1+x)^\alpha- 1 \sim \alpha x$

</div>

<div class="kb-tile-item">

$x-\sin x \sim \dfrac{x^{3}}{6}$

</div>

<div class="kb-tile-item">

$\tan x- x \sim \dfrac{x^{3}}{3}$

</div>

<div class="kb-tile-item">

$x-\ln(1+x) \sim \dfrac{x^{2}}{2}$

</div>

</div>

::: danger 易错 · 等价无穷小
「加减项中替换」是最高频错误：$\tan x- \sin x$ 若用 $\sin x\sim x$、$\tan x\sim x$ 相减得 0，主阶被抵消，正确答案需展开到三阶（$\dfrac{x^{3}}{2}$）。判定准则：替换后若结果的主阶未被抵消即可用，否则必须上泰勒。
:::

### 1.3 泰勒公式

![泰勒公式余项、五个麦克劳林展开与求极限](/math/math-taylor.svg)

$f(x)= \sum_{k=0}^{n}\dfrac{f^{(k)}(x_{0})(x- x_{0})^{k}}{k!}+ R_{n}(x)$：
- **佩亚诺余项** $R_{n}= o((x- x_{0})^{n})$：局部性质，用于求极限与判极值，只需 `n` 阶可导。
- **拉格朗日余项** $R_{n}= \dfrac{f^{(n+1)}(\xi)(x- x_{0})^{n+1}}{n+1}!$：整体性质，用于误差估计与不等式证明，需 $n+1$ 阶可导。

| 函数 | 麦克劳林展开（$x \to 0$） |
| --- | --- |
| $e^{x}$ | $1+ x+ \dfrac{x^{2}}{2}!+ \cdots+ \dfrac{x^{n}}{n}!+ o(x^{n})$ |
| `sin x` | $x- \dfrac{x^{3}}{3}!+ \dfrac{x^{5}}{5}!- \cdots$ |
| `cos x` | $1- \dfrac{x^{2}}{2}!+ \dfrac{x^{4}}{4}!- \cdots$ |
| $\ln(1+x)$ | $x- \dfrac{x^{2}}{2}+ \dfrac{x^{3}}{3}- \cdots+ \dfrac{(- 1)^{n-1}x^{n}}{n}$ |
| $(1+x)^\alpha$ | $1+ \alpha x+ \dfrac{\alpha(\alpha- 1)x^{2}}{2}!+ \cdots$ |
| `arctan x` | $x- \dfrac{x^{3}}{3}+ \dfrac{x^{5}}{5}- \cdots$ |

::: tip 工作例题 · 展开到几阶
分母是 $x^{m}$，就把分子展开到「首个非零项恰为 $x^{m}$」：
- $\dfrac{e^{x}- 1- x}{x^{2}}$：$e^{x}= 1+x+\dfrac{x^{2}}{2}+o(x^{2})$ ⇒ 分子 $= \dfrac{x^{2}}{2}+ o(x^{2})$ ⇒ 极限 `1/2`。
- $\dfrac{\tan x- \sin x}{x^{3}}$：$\tan x= x+ \dfrac{x^{3}}{3}$，$\sin x= x- \dfrac{x^{3}}{6}$ ⇒ 差 $= \dfrac{x^{3}}{2}$ ⇒ 极限 `1/2`。
由展开式还可直接读出 $f^{(n)}(0)= n! \cdot a_{n}$；判极值时看「首个非零偶数阶导数」。
:::

**补充 · 严格性说明**：$f$ 有任意阶导数并不保证其泰勒级数收敛到 $f$（经典反例 $f(x)=e^{- \dfrac{1}{x^{2}}}$（x≠0）、$f(0)=0$，在 0 处各阶导数全为 0）。收敛到原函数需拉格朗日余项趋于 0，即函数**解析**。教材多只给展开式，此处补足条件。

### 1.4 连续与间断点

| 类型 | 判据 | 例子 |
| --- | --- | --- |
| 第一类·可去 | 左右极限存在且相等，但 $= f(x_{0})$ 或无定义 | `sin x / x` 在 0 |
| 第一类·跳跃 | 左右极限存在但不等 | `sgn x` 在 0 |
| 第二类·无穷 | 至少一侧极限为 ∞ | `1/x` 在 0 |
| 第二类·振荡 | 极限不存在且不趋于 ∞ | $\sin\left(\dfrac{1}{x}\right)$ 在 0 |

**闭区间上连续函数的四性质**：有界性、最值定理、介值定理、零点定理（$f(a)f(b)<0 \Rightarrow \exists \xi, f(\xi)=0$）。这四条是第 3 章大量证明题的依据。

::: danger 易错 · 连续
- `f` 在 $x_{0}$ 连续要求「极限存在 + 有定义 + 极限等于函数值」三条同时成立。
- 介值定理要求**闭区间上连续**；开区间或不连续时结论可能失效。
- 连续不一定可导（`|x|` 在 0）；可导必连续；导函数可以不连续（但导函数无第一类间断点，即达布定理）。
:::

### 1.5 极限严格化的三个层次

| 层次 | 内容 | 作用 |
| --- | --- | --- |
| 直观 | 「无限逼近」 | 建立直觉，但无法证明 |
| ε–δ / ε–N | 把「任意接近」量化为 $\forall \epsilon \exists \delta$ | 证明极限存在、唯一性、保号性 |
| 拓扑 | 邻域、聚点、完备性、柯西列 | 实数完备性等价于「单调有界必收敛」「柯西列必收敛」 |

**七种等价刻画**：$\lim a_{n}=A$ ⇔ 任意子列收敛到 A（若有子列不收敛或收敛到别的值，则原数列不收敛）。判定发散常用「找两个子列极限不同」，如 $(- 1)^{n}$。
**Stolz 定理**（考研常用）：$b_{n}$ 严格递增趋于 ∞ 时，$\lim \dfrac{a_{n}}{b_{n}}= \lim \dfrac{a_{n+1}- a_{n}}{b_{n+1}- b_{n}}$（离散版洛必达），用于 $\lim \dfrac{1+\dfrac{1}{2}+ \cdots+\dfrac{1}{n}}{\ln} n= 1$ 一类题。

---

## 第 2 章 导数与微分（★★★）

### 2.1 导数的定义与几何意义

![导数定义、几何意义与可导连续关系](/math/math-derivative.svg)

$f'(x_{0})= \lim_{\Delta x \to 0}\dfrac{f(x_{0}+\Delta x)- f(x_{0})}{\Delta x}$，几何上是切线斜率 $\tan \alpha$，物理上是瞬时速度。
**微分** $dy=f'(x)dx$，且 $\Delta y= dy+ o(\Delta x)$ ——「以直代曲」是微元法的理论基础。

| 关系（一元） | 结论 |
| --- | --- |
| 可导 ⇔ 可微 | 等价（多元不再等价） |
| 可导 ⇒ 连续 ⇒ 极限存在 | 反向均不成立：`|x|` 在 0 连续不可导 |
| 可导 ⇔ 左导数 = 右导数（有限） | 分段点必须用定义算 |
| $f'$ 未必连续 | 但由达布定理，$f'$ 无跳跃间断 |

### 2.2 求导法则与特殊函数

| 类型 | 公式 |
| --- | --- |
| 四则 | $(uv)'=u'v+uv'$；$\left(\dfrac{u}{v}\right)'= \dfrac{u'v- uv'}{v^{2}}$ |
| 复合（链式） | $y=f(u), u=g(x) \Rightarrow y'= f'(u)g'(x)$，多层复合逐层相乘 |
| 反函数 | $\dfrac{dx}{dy}= \dfrac{1}{y}'$；$\dfrac{d^{2}x}{dy^{2}}=- y''(y')^{3}$ |
| 隐函数 | $F(x,y)=0 \Rightarrow \dfrac{dy}{dx}=- \dfrac{F_{x}}{F_{y}}$（$F_{y}=0$） |
| 参数方程 | $\dfrac{dy}{dx}= \dfrac{\dot{y}}{\dot{x}}$；$\dfrac{d^{2}y}{dx^{2}}= \dfrac{\dfrac{d}{dt\left(\dfrac{\dot{y}}{\dot{x}}\right)}}{\dot{x}}= \dfrac{\dot{x}\ddot{y}- \ddot{y}\ddot{x}}{\dot{x}^{3}}$（先对 t 求导再除 ẋ） |
| 对数求导 | $y=x^{x} \Rightarrow \ln y= x \ln x \Rightarrow y'= x^{x}(\ln x+ 1)$ |
| 高阶·莱布尼茨 | $(uv)^{(n)}= \sum_{k} C(n,k) u^{(k)} v^{(n-k)}$ |
| 常用 n 阶 | $(\sin x)^{(n)}= \sin\left(x+\dfrac{n\pi}{2}\right)$；$\left(\dfrac{1}{x+a}\right)^{(n)}=\dfrac{(-1)^{n}\,n!}{(x+a)^{n+1}}$ |

::: tip 工作例题 · 分段点与含绝对值因子
$f(x)= x^{2} \sin\left(\dfrac{1}{x}\right)$（$x\ne0$）、$f(0)=0$：在 0 处 $f'(0)= \lim x \sin\left(\dfrac{1}{x}\right)= 0$（可导），但 $f'(x)=2x \sin\left(\dfrac{1}{x}\right)- \cos\left(\dfrac{1}{x}\right)$ 在 0 处极限不存在 ⇒ **导函数不连续**。这是「可导但导函数不连续」的标准反例。
经典结论：$g(x)|x- a|$ 在 $a$ 处可导 $\Leftrightarrow g(a)=0$（此时导数为 0）。
:::

::: danger 易错 · 求导
- 分段函数分界点**必须用定义**求左右导数；直接对两侧表达式求导再代入，只在导函数连续时才等价。
- 参数方程二阶导数是 `(d/dt (dy/dx))/ẋ`，不是 `ÿ/ẍ`（最常见公式错误）。
- 隐函数求二阶导时，要对一阶结果再求导并把 `y′` 代回，不能把 `y` 当常数。
:::

---

## 第 3 章 微分中值定理与导数应用（★★★）

### 3.1 四大中值定理

![罗尔、拉格朗日、柯西与泰勒中值定理](/math/math-mvt.svg)

| 定理 | 条件 | 结论 |
| --- | --- | --- |
| 费马引理 | `f` 在 $x_{0}$ 可导且取极值 | $f'(x_{0})=0$ |
| 罗尔 | $[a,b]$ 连续、$(a,b)$ 可导、$f(a)=f(b)$ | $\exists \xi \in(a,b)$, $f'(\xi)=0$ |
| 拉格朗日 | `[a,b]` 连续、`(a,b)` 可导 | $f(b)- f(a)= f'(\xi)(b- a)$ |
| 柯西 | `f,g` 满足上述条件且 $g'=0$ | $\dfrac{f(b)- f(a)}{g(b)- g(a)}= f'\dfrac{\xi}{g}'(\xi)$ |
| 泰勒 | $n+1$ 阶可导 | 带拉格朗日余项的 $n$ 阶展开（$n=0$ 退化为拉格朗日） |

**逻辑链**：罗尔（特殊）→ 拉格朗日（罗尔 + 辅助函数）→ 柯西（参数形式）→ 泰勒（高阶），而**柯西是洛必达法则的证明基础**。

::: tip 工作例题 · 辅助函数构造三步
证 $\exists \xi : f'(\xi)+ f(\xi)g'(\xi)= 0$：
① 把待证式看成某函数 $F$ 的导数等于 0；② 乘积分因子 $e^{g(x)}$ 得 $F(x)=e^{g(x)}f(x)$；③ 对 $F$ 用罗尔定理。
常见模板：证 $f'(\xi)=k$ ⇒ $F=f- kx$；证 $f'\dfrac{\xi}{g}'(\xi)=k$ ⇒ 柯西；含 $f''$ ⇒ 两次罗尔或对 $f'$ 用拉格朗日；含积分 ⇒ 积分中值定理。
:::

**洛必达法则的四个前提**（常被忽略）：① 属 $\dfrac{0}{0}$ 或 $\dfrac{\infty}{\infty}$；② 去心邻域内 $f'$、$g'$ 存在且 $g'=0$；③ $\lim\dfrac{f'}{g'}$ 存在或为 ∞；④ 若 $\lim\dfrac{f'}{g'}$ 振荡不存在则**法则失效**，须改用定义或泰勒。
反例：$\lim_{x \to \infty}\dfrac{x+\sin x}{x}= 1$，但 $f'/g'= 1+\cos x$ 极限不存在，洛必达给不出结论。

### 3.2 单调性、凹凸性、极值与渐近线

![单调凹凸拐点、三类渐近线与作图流程](/math/math-application.svg)

| 判据 | 结论 |
| --- | --- |
| $f'>0$ / $f'<0$ | 单调递增 / 递减 |
| $f''>0$ / $f''<0$ | 图形凹（∪，下凸）/ 凸（∩，上凸） |
| $f''$ 变号且曲线连续 | 该点为**拐点**（须写成坐标 $(x_{0}, f(x_{0}))$） |
| $f'(x_{0})=0$ 且 $f'$ 变号 | 极值（一阶充分必要判别） |
| $f'(x_{0})=0, f''(x_{0})<0$ / $>0$ | 极大 / 极小；$f''=0$ 时失效，须回到定义或更高阶 |

**三类渐近线**：
- 水平 $y=A$，若 $\lim_{x \to ± \infty} f(x)= A$；
- 铅直 $x= x_{0}$，若 $\lim_{x \to x_{0}} f(x)= \infty$（在无定义点、分段点找）；
- 斜 $y=ax+b$，$a= \lim \dfrac{f(x)}{x}$，$b= \lim[f(x)- ax]$（只需在水平不存在时求），且 $x \to+ \infty$ 与 $x \to- \infty$ 要分别计算。

**曲率** $\kappa=\dfrac{|y''|}{(1+y'^{2})^{\dfrac{3}{2}}}$，曲率半径 $\rho= \dfrac{1}{\kappa}$（直线 $\kappa=0$）。

::: danger 易错 · 导数应用
- 极值是**局部**概念、最值是**全局**概念；闭区间最值必须比较「驻点 + 不可导点 + 端点」。
- $f''(x_{0})=0$ 既非拐点的充分条件也非必要条件：$f=x^{4}$ 在 0 有 $f''=0$ 但不是拐点；$f=x^{\dfrac{1}{3}}$ 在 0 是拐点但二阶导不存在。
- 拐点是曲线上的**点**（要写坐标），极值点是 **x 值**；两者概念维度不同。
- 同一方向水平与斜渐近线至多各一条；若 `a` 不存在（且非 ∞）则无斜渐近线。
:::

**函数作图七步**：定义域与对称性 → 求 $f'$、$f''$ 及其全部零点/不存在点 → 列表分段 → 判单调与极值 → 判凹凸与拐点 → 求渐近线 → 描特殊点连线。列表法（$+/0/-/\text{不存在}$）是最不易失分的格式。

::: tip 补充 · 由单调性得到的常用不等式
构造函数 + 单调性是证明不等式的标准武器，几条「母不等式」值得记住（都可由 `F(x)` 求导证出）：
- $e^{x} \ge 1+x$（等号仅 $x=0$）；
- $\dfrac{x}{1+x} \le \ln(1+x) \le x$（$x>- 1$）；
- `sin x < x < tan x`（$0<x<\dfrac{\pi}{2}$）；
- $1- \dfrac{x^{2}}{2} \le \cos x$。
琴生不等式（凸函数 $f\left(\sum \lambda_{i}x_{i}\right) \le \sum \lambda_{i}f(x_{i})$）则是凹凸性的直接推论，处理「和式/均值型」不等式时优先想到。
:::

### 3.3 中值定理的证明链与反例

```text
费马引理（极值点导数为 0）
   ↓ 加上 f(a)=f(b)
罗尔定理
   ↓ 构造 F(x)=f(x)−f(a)−[(f(b)−f(a))/(b−a)](x−a)
拉格朗日中值定理
   ↓ 参数化 (g(t), f(t)) 或构造含 g 的辅助函数
柯西中值定理
   ↓ 反复应用于余项
泰勒定理（拉格朗日余项）
```
**条件不可省的反例**：$f(x)=|x|$ 在 $[- 1,1]$ 满足连续且 $f(- 1)=f(1)$，但 0 处不可导 ⇒ 不存在 $f'(\xi)=0$ 的点，可见「可导」条件不可去。

---

## 第 4 章 不定积分（★★★）

### 4.1 原函数与基本公式

![三种主要积分法与三类常见可积函数](/math/math-integral.svg)

$\int f(x)dx= F(x)+ C \Leftrightarrow F'(x)=f(x)$。**连续函数必有原函数**（积分上限函数就是一个）；但有第一类间断点的函数没有原函数（导函数无第一类间断点——达布定理）。

| 基本积分 | 结果 |
| --- | --- |
| $\int x^a dx$ | $\dfrac{x^{a+1}}{a+1}+C$（$a\ne-1$）；$a=-1$ 时 $\ln|x|+C$ |
| $\int e^{x}dx$, $\int a^{x}dx$ | $e^{x}+C$, $\dfrac{a^{x}}{\ln} a+C$ |
| $\int \sin x dx$, $\int \cos x dx$ | $- \cos x+C$, `sin x+C` |
| $\dfrac{\int dx}{1+x^{2}}$, $\dfrac{\int dx}{\sqrt{1- x^{2}}}$ | `arctan x+C`, `arcsin x+C` |
| $\int \sec x dx$ | `ln|sec x + tan x|+C` |
| $\dfrac{\int dx}{a^{2}+x^{2}}$, $\dfrac{\int dx}{\sqrt{a^{2}- x^{2}}}$ | $\left(\dfrac{1}{a}\right)\arctan\left(\dfrac{x}{a}\right)+C$, `arcsin(x/a)+C` |
| $\int f'\dfrac{x}{f(x)dx}$ | `ln|f(x)|+C`（最高频凑微分） |

### 4.2 三种主要积分法

**第一换元（凑微分）**：$\int f(\phi(x))\phi '(x)dx= \int f(u)du$，关键是把被积式拆成「函数 × 其导数」。
**第二换元（变量代换）**：令 $x=\psi(t)$ 单调可导，$\int f(x)dx= \int f(\psi(t))\psi '(t)dt$，最后必须**回代**。

| 根式 | 代换 | 恒等式 |
| --- | --- | --- |
| $\sqrt{a^{2}- x^{2}}$ | $x= a \sin t$ | $a^{2}- x^{2}= a^{2}\cos^{2}t$ |
| $\sqrt{a^{2}+x^{2}}$ | $x= a \tan t$ | $a^{2}+x^{2}= a^{2}\sec^{2}t$ |
| $\sqrt{x^{2}- a^{2}}$ | $x= a \sec t$ | $x^{2}- a^{2}= a^{2}\tan^{2}t$ |

**分部积分** $\int u dv= uv- \int v du$，取 `u` 的优先级口诀「**反、对、幂、指、三**」（反三角 → 对数 → 幂 → 指数 → 三角），把容易求导的放在 `u`。
循环型（如 $\int e^{x}\cos x dx$）需两次分部后解方程；递推型（如 $I_{n}= \int \sec^{n}x dx$）建立递推公式。

### 4.3 三类常见可积函数

| 类型 | 方法 |
| --- | --- |
| 有理函数 `P(x)/Q(x)` | 先化为真分式（多项式除法）→ 分母因式分解 → 部分分式（含重根、二次不可约）→ 逐项积分 |
| 三角有理式 `R(sin x, cos x)` | 万能代换 $t=\tan\left(\dfrac{x}{2}\right)$：$\sin x= \dfrac{2t}{1+t^{2}}$，$\cos x= \dfrac{1- t^{2}}{1+t^{2}}$，$dx= \dfrac{2dt}{1+t^{2}}$；有更简对称式时优先用 |
| 简单无理函数 | 根式整体代换：$\int R\left(x,^{n}\sqrt{ax+b}\right)dx$ 令 $t=^{n}\sqrt{ax+b}$；倒代换 $x=\dfrac{1}{t}$ 处理高次分母 |

::: danger 易错 · 不定积分
- **不要漏 `+C`**；分段积分时各段常数须由连续性统一（否则原函数不连续）。
- 三角代换回代时用辅助直角三角形，别把 `t` 直接留在答案里。
- $e^{- x^{2}}$、`sin x / x`、$\dfrac{1}{\ln} x$、$\sqrt{1+k^{2}\sin^{2}x}$ 等**原函数不是初等函数**（刘维尔定理），不要硬算；它们靠级数、变限积分或数值方法处理（见第 5、12 章）。
- $\int\dfrac{dx}{x}=\ln\lvert x\rvert+C$，绝对值不能省。
:::

::: tip 工作例题 · 三个分部积分
$$
\begin{gathered}
(1) \int x e^{x} dx \; \text{：取} \; u=x, dv=e^{x}dx \Rightarrow x e^{x}- \int e^{x}dx=(x- 1)e^{x}+ C \\
\text{验算：} \; [(x- 1)e^{x}]'= e^{x}+(x- 1)e^{x}= x e^{x} \checkmark \\
(2) \int \ln x dx= x \ln x- \int x \cdot\left(\frac{1}{x}\right)dx= x \ln x- x+ C \\
(3) \int x \cos x dx= x \sin x- \int \sin x dx= x \sin x+ \cos x+ C
\end{gathered}
$$
**验算习惯**：对结果求导，看是否回到被积函数（比重新积分快得多）。
:::

### 4.4 积分技巧体系：何时用哪个

| 被积特征 | 首选方法 |
| --- | --- |
| 复合函数 × 内层导数 | 第一换元（凑微分） |
| 含 $\sqrt{a^{2}±x^{2}}$、$\sqrt{x^{2}- a^{2}}$ | 三角代换 |
| 两个不同类函数相乘（幂×指/三/对/反三角） | 分部积分，按「反对幂指三」取 u |
| 有理分式 | 部分分式分解 |
| 三角函数有理式 | 万能代换（有对称性时优先用倍角/降幂） |
| 对称区间 | 先查奇偶性；三角积分可用区间再现 |
| $\int_{0}^{\dfrac{\pi}{2}} \sin^{n}x dx$ | 华里士公式 |
| 变限积分求导 | 通式 + 先换元把参数提出 |

**不可积但要会处理的函数**：$\int e^{- x^{2}}dx$ 用级数展开或误差函数 `erf(x)`；$\int_{0}^{+\infty}\dfrac{\sin x}{x}\,dx=\dfrac{\pi}{2}$（狄利克雷积分，用含参积分或拉普拉斯变换）；$\int_{0}^{\dfrac{\pi}{2}} \ln \sin x dx=-\left(\dfrac{\pi}{2}\right)\ln 2$（用区间再现与倍角）。

---

## 第 5 章 定积分与反常积分（★★★）

### 5.1 定义、性质与微积分基本定理

![黎曼和、微积分基本定理与简化技巧](/math/math-definite.svg)

$\int_{a}^{b} f(x)dx= \lim_{\lambda \to 0} \sum f(\xi_{i})\Delta x_{i}$（$\lambda=\max \Delta x_{i}$）。几何上是曲边梯形的**代数面积**（x 轴下方为负）。
**可积的充分条件**：连续、或单调、或只有有限个第一类间断点；**可积的必要条件**：有界。

| 定理 | 内容 |
| --- | --- |
| 积分中值定理 | `f` 连续 ⇒ $\int_{a}^{b} f dx= f(\xi)(b- a)$ |
| 积分上限函数 | $\Phi(x)= \int_{a}^{x} f(t)dt$；`f` 连续 ⇒ $\Phi '(x)=f(x)$；`f` 可积 ⇒ $\Phi$ 连续（未必可导） |
| 变限求导通式 | $\dfrac{d}{dx} \int_{\alpha(x)}^{\beta(x)} f(t)dt= f(\beta)\beta '- f(\alpha)\alpha '$ |
| **牛顿–莱布尼茨** | $\int_{a}^{b} f dx= F(b)- F(a)$，把求和极限化为原函数增量 |
| 含参变量 | 被积函数含 `x` 时须先换元把 `x` 提到积分号外，再求导 |

::: tip 补充 · 用定积分定义求 n 项和极限
形如 $\lim_{n \to \infty}\dfrac{1}{n}\sum_{k=1}^{n} f\left(\dfrac{k}{n}\right)$ 的极限，正是取 $x_{k}=\dfrac{k}{n}$、$\Delta x=\dfrac{1}{n}$、$\xi_{i}=x_{i}$ 的黎曼和，故等于 $\int_{0}^{1} f(x)dx$。
例：

$$\lim\left(\frac{1}{n}\right)\left(\sqrt{1+\frac{1}{n}}+\sqrt{1+\frac{2}{n}}+ \cdots+\sqrt{1+\frac{n}{n}}\right)= \int_{0}^{1}\sqrt{1+x}dx=\left[ \frac{2}{3}(1+x)^{\frac{3}{2}}\right]_{0}^{1}= \frac{2}{3}\left(2\sqrt{2}- 1\right) \approx 1.2189$$
若和式不是标准 $\left(\dfrac{1}{n}\right)\sum f\left(\dfrac{k}{n}\right)$ 形状，先提出 `1/n` 凑形；凑不出的用夹逼放缩。
:::

### 5.2 计算简化四技巧

::: tip 工作例题 · 五个必记积分
$$
\begin{gathered}
(1) \int_{0}^{\frac{\pi}{2}} \sin^{2}x dx= \int_{0}^{\frac{\pi}{2}} \cos^{2}x dx= \frac{\pi}{4} \approx 0.785398 \\
\text{（用} \; \cos 2x= 1- 2\sin^{2}x \; \text{，或华里士公式} \; I_{2}=\left(\frac{1}{2}\right) \cdot\left(\frac{\pi}{2}\right) \; \text{）} \\
(2) \int_{0}^{1} x e^{x} dx=[(x- 1)e^{x}]_{0}^{1}= 0-(- 1)= 1 \\
(3) \int_{0}^{1}\frac{dx}{1+x^{2}}= \arctan x|_{0}^{1}= \frac{\pi}{4} \\
(4) \int_{0}^\pi x \sin x dx=[- x \cos x+ \sin x]_{0}^\pi= \pi \\
(5) \int_{0}^\infty e^{- x^{2}} dx= \frac{\sqrt{\pi}}{2} \approx 0.886227 \; \text{（泊松积分，用二重积分极坐标证明）}
\end{gathered}
$$
:::

| 技巧 | 公式 / 说明 |
| --- | --- |
| 奇偶性 | 对称区间：`f` 奇 ⇒ 积分为 0；`f` 偶 ⇒ $2 \int_{0}^{a} f dx$ |
| 周期性 | $\int_{a}^{a+T} f dx= \int_{0}^{T} f dx$；$\int_{0}^{nT} f dx= n \int_{0}^{T} f dx$ |
| 区间再现（King） | $\int_{a}^{b} f(x)dx= \int_{a}^{b} f(a+b- x)dx$；用于 $\int_{0}^{\dfrac{\pi}{2}} f(\sin x, \cos x)dx$ 与 $\int_{0}^\pi x f(\sin x)dx=\left(\dfrac{\pi}{2}\right) \int_{0}^\pi f(\sin x)dx$ |
| 华里士公式 | $I_{n}= \int_{0}^{\dfrac{\pi}{2}}\sin^{n}x dx= \int_{0}^{\dfrac{\pi}{2}}\cos^{n}x dx$；`n` 偶 ⇒ $\dfrac{(n-1)!!}{n!!}\cdot\dfrac{\pi}{2}$；`n` 奇 ⇒ $\dfrac{(n-1)!!}{n!!}$；$I_{n}= \dfrac{n- 1}{n} \cdot I_{n-2}$ |

### 5.3 反常积分（广义积分）

| 类型 | 定义 | 收敛判据 |
| --- | --- | --- |
| 无穷区间 | $\int_{a}^\infty f dx= \lim_{b \to \infty} \int_{a}^{b} f dx$ | $\int_{1}^\infty \dfrac{dx}{x^{p}}$ 收敛 ⇔ `p > 1` |
| 无界函数（瑕积分） | 瑕点在端点/内部，须分段取极限 | $\int_{0}^{1}\dfrac{dx}{x^{p}}$ 收敛 ⇔ `p < 1` |

::: danger 易错 · 反常积分
- 两个 `p` 的收敛方向**相反**（无穷区间 `p>1`、瑕积分 `p<1`），是最高频记忆错误。
- 瑕点在区间**内部**时必须拆成两段分别判敛，只要有一段发散即整体发散；不能用「主值」冒充收敛。
- 比较判别法要求非负；一般函数用**绝对收敛**判据（$\int|f|$ 收敛 ⇒ $\int f$ 收敛）。
- 计算反常积分仍可用牛顿–莱布尼茨，但要在无穷/瑕点处取极限，不能把 ∞ 直接代入。
:::

**Γ 函数**（补充）：$\Gamma(s)= \int_{0}^\infty x^{s- 1}e^{- x}dx(s>0)$，满足 $\Gamma(s+1)=s\Gamma(s)$、$\Gamma(n+1)=n!$、$\Gamma\left(\dfrac{1}{2}\right)=\sqrt{\pi}$。它是阶乘的连续延拓，也是 $\int_{0}^\infty e^{- x^{2}}dx= \dfrac{\sqrt{\pi}}{2}$ 的推导工具。

### 5.4 反常积分判敛的完整工具箱

| 判别法 | 陈述 |
| --- | --- |
| 比较判别 | $0 \le f \le g$，$\int g$ 收敛 ⇒ $\int f$ 收敛；$\int f$ 发散 ⇒ $\int g$ 发散 |
| 极限比较 | $\lim \dfrac{f}{g}= c \in(0, \infty)$ ⇒ 同敛散；$c=0$ 且 $\int g$ 收敛 ⇒ $\int f$ 收敛；$c= \infty$ 且 $\int g$ 发散 ⇒ $\int f$ 发散 |
| 柯西判别（p 判别） | $\int_{1}^\infty f(x)dx$：若 $\lim x^{p} f(x)= c$ 且 `p>1` ⇒ 收敛；$p \le 1$ 且 `c>0` ⇒ 发散。瑕积分换用 $\lim(x- a)^{p} f(x)$，`p<1` 收敛 |
| 绝对/条件收敛 | $\int\vert f\vert $ 收敛 ⇒ $\int f$ 收敛；反之称条件收敛（如 $\int_{1}^\infty \sin \dfrac{x}{x dx}$） |
| Γ / B 函数 | $\Gamma(s)$、$B(p,q)=\dfrac{\Gamma(p)\Gamma(q)}{\Gamma}(p+q)$，把许多反常积分化为特殊函数值 |

---

## 第 6 章 定积分的应用（★★）

### 6.1 微元法（元素法）

![微元法、几何与物理应用公式表](/math/math-app-integration.svg)

在 `[x, x+dx]` 上把所求量 $U$ 的局部增量写成 $dU=f(x)dx$，要求 $\Delta U- dU= o(dx)$，则 $U= \int_{a}^{b} f(x)dx$。核心思想是「以直代曲、以匀代变」，且微元必须**可加**。
标准流程：**选积分变量 → 写出微元 → 由区域定上下限 → 积分**。

| 几何量 | 直角坐标 | 极坐标 / 参数式 |
| --- | --- | --- |
| 平面面积 | $A= \int_{a}^{b}\vert f- g\vert dx$ | $A= \dfrac{1}{2} \int_{a}ᵝ r^{2}(\theta)d\theta$ |
| 旋转体体积（绕 x） | $V=\pi \int_{a}^{b} f^{2}(x)dx$ | 绕 y 轴柱壳 $V=2\pi \int_{a}^{b} x f(x)dx$ |
| 已知截面 | $V= \int_{a}^{b} A(x)dx$ | — |
| 弧长 | $s= \int_{a}^{b}\sqrt{1+y'^{2}}dx$ | $s= \int \sqrt{\dot{x}^{2}+\dot{y}^{2}}dt$；$s= \int \sqrt{r^{2}+r'^{2}}d\theta$ |
| 旋转曲面面积 | $S=2\pi \int_{a}^{b} f(x)\sqrt{1+y'^{2}}dx$ | — |

**物理应用**：变力做功 $W= \int F(x)dx$；液体侧压力 $P= \int \rho g h(x)w(x)dx$；质心 $\bar{x}= \dfrac{\int x dm}{\int dm}$；函数平均值 $\bar{f}=\left(\dfrac{1}{b- a}\right) \int_{a}^{b} f dx$；均方根 $\sqrt{\left(\dfrac{1}{b- a}\right) \int f^{2}dx}$（交流电有效值）。

::: tip 工作例题 · 三道几何题（已核算）
$$
\begin{gathered}
(1) y=x^{2}(0 \le x \le 1) \; \text{绕} \; \text{x} \; \text{轴：} \; V= \pi \int_{0}^{1}(x^{2})^{2}dx= \pi \int_{0}^{1}x^{4}dx= \frac{\pi}{5} \approx 0.628319 \\
(2) y=\sin x(0 \le x \le \pi) \; \text{与} \; \text{x} \; \text{轴围成面积：} \; A= \int_{0}^\pi \sin x dx=[- \cos x]_{0}^\pi= 2 \\
\text{(3)} \; \text{星形线} \; x=a \cos^{3}t, y=a \sin^{3}t \; \text{全长} \; \text{= 6a} \; \text{（} \; \text{a=1} \; \text{时为} \; \text{6} \; \text{）；} \\
\text{第一象限弧长} \; = \int_{0}^{\frac{\pi}{2}}3a \sin t \cos t dt= \frac{3a}{2} \; \text{，乘} \; \text{4} \; \text{得} \; \text{6a} \\
\text{(4)} \; \text{抛物线} \; y=x^{2} \; \text{在} \; \text{[0,1]} \; \text{的弧长} \; = \frac{1}{2}[\sqrt{5}+ \frac{1}{2} \ln\left(2+\sqrt{5}\right)]
\end{gathered}
$$
:::

::: danger 易错 · 微元法
- 面积必须加绝对值（或先求交点分段），否则上下曲线交叉时正负抵消。
- 绕 y 轴旋转可用柱壳法或圆盘法，两者积分变量不同，别混用上下限。
- 弧长公式中 $\sqrt{1+y'^{2}}$ 不能写成 `1+y′`；物理量的单位与坐标系要一致。
:::

---

## 第 7 章 常微分方程（★★★）

### 7.1 一阶方程的分类解法

![微分方程分类决策树与标准解法](/math/math-ode.svg)

| 类型 | 标准形式 | 解法 |
| --- | --- | --- |
| 可分离变量 | $y'=f(x)g(y)$ | $\dfrac{\int dy}{g(y)}= \int f(x)dx+ C$ |
| 齐次方程 | $y'=\phi\left(\dfrac{y}{x}\right)$ | 令 $u=\dfrac{y}{x} \Rightarrow y'=u+xu'$，化为可分离 |
| 一阶线性 | $y'+P(x)y=Q(x)$ | 积分因子 $e^{\int P dx}$；$y= e^{- \int P}[ \int Q e^{\int P}dx+ C]$ |
| 伯努利 | $y'+Py=Qy^{n}(n=0,1)$ | 令 $z=y^{1- n}$ 化为线性 |
| 全微分方程 | $M\,dx+N\,dy=0$ 且 $\dfrac{\partial M}{\partial y}= \dfrac{\partial N}{\partial x}$ | 求原函数 $u(x,y)=C$（偏积分法 / 曲线积分） |
| 可降阶 | $y''=f(x)$ / $f(x,y')$ / $f(y,y')$ | 积两次 / 令 $p=y'$ / 令 $p=y'$， $y''=\dfrac{p dp}{dy}$ |

::: tip 工作例题 · 一阶线性
$y'+2y=e^{x}$：积分因子 $e^{2x}$，两边乘后 $(e^{2x}y)'=e^{3x}$，
⇒ $e^{2x}y=\dfrac{1}{3}e^{3x}+C$ ⇒ $y= \dfrac{1}{3} e^{x}+ Ce^{- 2x}$。
验算：$y'+2y= \dfrac{1}{3} e^{x}- 2Ce^{- 2x}+ \dfrac{2}{3} e^{x}+ 2Ce^{- 2x}= e^{x}$ ✓
:::

### 7.2 高阶线性方程与常系数

**解的结构**：`n` 阶线性方程通解含 `n` 个独立任意常数；齐次解的线性组合仍是齐次解；**非齐次通解 = 齐次通解 + 一个特解**；两非齐次解之差是齐次解。

**二阶常系数齐次** `y″+py′+qy=0`，特征方程 $r^{2}+pr+q=0$：

| 特征根 | 通解 |
| --- | --- |
| 两不等实根 $r_{1}=r_{2}$ | $C_{1}e^{r_{1}x}+C_{2}e^{r_{2}x}$ |
| 二重根 `r` | $(C_{1}+C_{2}x)e^{rx}$ |
| 共轭复根 $\alpha ±i\beta$ | $e^{\alpha x}(C_{1}\cos \beta x+C_{2}\sin \beta x)$ |

**非齐次特解（待定系数法）**：
- $f(x)=e^{\lambda x}P_{m}(x)$ ⇒ 设 $y*=x^{k} e^{\lambda x}Q_{m}(x)$，`k` 是 $\lambda$ 作为特征根的重数（0/1/2）；
- $f(x)=e^{\alpha x}[A \cos \beta x+B \sin \beta x]$ ⇒ 设 $y*=x^{k} e^{\alpha x}[C \cos \beta x+D \sin \beta x]$，`k` 由 $\alpha+i\beta$ 是否为特征根决定。

::: tip 工作例题 · 三组方程
$$
\begin{gathered}
(1) y''- 3y'+2y=0 \Rightarrow r^{2}- 3r+2=0 \Rightarrow r=1,2 \Rightarrow y=C_{1}e^{x}+C_{2}e^{2x} \\
(2) y''+4y=0 \Rightarrow r=±2i \Rightarrow y=C_{1}\cos 2x+C_{2}\sin 2x \\
(3) y''+4y=\sin x \; \text{：设} \; y*=A \sin x \Rightarrow- A \sin x+4A \sin x= 3A \sin x= \sin x \\
\Rightarrow A=\frac{1}{3} \Rightarrow y*=\left(\frac{1}{3}\right)\sin x \; \text{，通解} \; y=C_{1}\cos 2x+C_{2}\sin 2x+\left(\frac{1}{3}\right)\sin x \\
\text{(4)} \; \text{若右端改为} \; \sin 2x \; \text{，则与齐次解共振，须设} \; \text{y*=x(A cos2x+B sin2x)}
\end{gathered}
$$
:::

**欧拉方程** $x^{2}y''+pxy'+qy=f(x)$：令 $x=e^{t}$（即 $t=\ln x$）化为常系数；齐次情形也可直接设 $y=x^{k}$ 解指标方程。

::: danger 易错 · 微分方程
- 「齐次」一词有两义：$y'=\phi\left(\dfrac{y}{x}\right)$ 的齐次方程 ≠ 线性方程的齐次（`Q=0`），看上下文。
- 待定系数法漏乘 $x^{k}$ 是最高频失分点：只要 $\lambda$ 是特征根就必须乘。
- 可分离变量时除以 `g(y)` 会丢失 `g(y)=0` 对应的常数解，需单独补回。
- 初值问题要把常数用初始条件定出；通解中的常数个数必须等于方程阶数。
:::

### 7.3 线性微分方程解的结构

$L[y]=y^{(n)}+a_{1}(x)y^{(n-1)}+ \cdots+a_{n}(x)y$ 是**线性算子**，故：
- 齐次解集是 n 维线性空间（基 = 基本解组，朗斯基行列式 $W=0$ 判别线性无关）；
- 非齐次通解 = 齐次通解 + 任一特解；
- 叠加原理：$L[y]=f_{1}+f_{2}$ 的解 = 对应两解之和。

**常数变易法**：已知齐次基本解 $y_{1},y_{2}$，设特解 $y*=C_{1}(x)y_{1}+C_{2}(x)y_{2}$，解方程组 $C_{1}'y_{1}+C_{2}'y_{2}=0$、$C_{1}'y_{1}'+C_{2}'y_{2}'=f$，可处理一般（非常系数）二阶方程 —— 这是待定系数法失效时的通用手段。
**幂级数解法**（选学内容）：在常点附近设 $y=\sum a_{n}x^{n}$ 代入方程递推系数，是勒让德、贝塞尔方程的标准解法；欧拉公式 $e^{ix}=\cos x+i \sin x$ 也由幂级数得到。

---

## 第 8 章 向量代数与空间解析几何（★★★）

### 8.1 三种向量积

![三种积、平面与直线方程](/math/math-vector.svg)

| 运算 | 定义 | 性质与用途 |
| --- | --- | --- |
| 数量积 | $a\cdot b=|a||b|\cos\theta=a_x b_x+a_y b_y+a_z b_z$ | 结果是**标量**；夹角 $\cos\theta=\dfrac{a\cdot b}{|a||b|}$；投影 $Prj_{b} a= a \cdot b\vert b\vert $；垂直 ⇔ $a \cdot b=0$ |
| 向量积 | $a\times b=(a_{y}b_{z}-a_{z}b_{y},\;a_{z}b_{x}-a_{x}b_{z},\;a_{x}b_{y}-a_{y}b_{x})$ | 结果是**向量**，$\bot a$ 且 $\bot b$（右手系）；$\vert a \times b\vert $ = 平行四边形面积；平行 ⇔ $a \times b=0$；**反交换** $a \times b=- b \times a$ |
| 混合积 | $[a b c]=(a \times b) \cdot c$（三阶行列式） | 绝对值 = 平行六面体体积；三向量共面 ⇔ 混合积 = 0；轮换不变、对换变号 |
| 方向余弦 | $\cos \alpha=a_{x}\vert a\vert $ 等 | $\cos^{2}\alpha+\cos^{2}\beta+\cos^{2}\gamma=1$ |

::: tip 工作例题 · 三种积手算
$a=(1,2,- 1)$，`b=(3,0,2)`：

$$a \cdot b= 3+ 0- 2= 1$$

$$a \times b=(2 \cdot 2-(- 1) \cdot 0,(- 1) \cdot 3- 1 \cdot 2, 1 \cdot 0- 2 \cdot 3)=(4,- 5,- 6)$$

$|a|= \sqrt{1+4+1}= \sqrt{6} \approx 2.449$；$\cos \theta= \dfrac{1}{\sqrt{6} \cdot \sqrt{13}} \approx 0.1132$。
校验：$(a \times b) \cdot a= 4- 10+6= 0$ 且 $(a \times b) \cdot b= 12+0- 12= 0$ ✓（垂直于两者）。
:::

### 8.2 平面、直线与位置关系

| 对象 | 方程 | 关键量 |
| --- | --- | --- |
| 平面点法式 | $A(x- x_{0})+B(y- y_{0})+C(z- z_{0})=0$ | 法向量 `n=(A,B,C)` |
| 平面一般式 | `Ax+By+Cz+D=0` | `D=0` 过原点；缺某变量 ⇒ 平行于对应轴 |
| 直线对称式 | $\dfrac{x- x_{0}}{m}=\dfrac{y- y_{0}}{n}=\dfrac{z- z_{0}}{p}$ | 方向向量 `s=(m,n,p)` |
| 直线参数式 | $x=x_{0}+mt, y=y_{0}+nt, z=z_{0}+pt$ | 代入平面求交点最方便 |
| 直线一般式 | 两平面交线 | $s= n_{1} \times n_{2}$（别把法向量当方向向量） |

**距离与夹角**：
- 点 $P_{0}$ 到平面：$d=|Ax_{0}+By_{0}+Cz_{0}+D| \sqrt{A^{2}+B^{2}+C^{2}}$；
- 两平面夹角：$\cos\theta=\dfrac{|n_1\cdot n_2|}{|n_1||n_2|}$（取锐角）；
- 线面夹角：$\sin\theta=\dfrac{|s\cdot n|}{|s||n|}$；两直线夹角用 $s_{1} \cdot s_{2}$；
- 异面直线距离：$d=|[s_{1} s_{2} P_{1}P_{2}]||s_{1} \times s_{2}|$。

::: tip 工作例题 · 点到平面距离
平面 $2x- y+ 2z- 3= 0$，法向量 $n=(2,- 1,2)$，`|n|=3`。
点 `(0,0,0)`：$d=|- 3| 3= 1$。
（注意：点 `(1,1,1)` 满足 $2- 1+2- 3=0$，恰在平面上，距离为 0 —— 出题时容易误选此类点作例题。）
:::

**平面束**：过两平面交线的一切平面（除第二个平面本身）可写成 $(A_{1}x+B_{1}y+C_{1}z+D_{1})+\lambda(A_{2}x+B_{2}y+C_{2}z+D_{2})=0$，求「过已知直线且满足某条件」的平面时最省力。

### 8.3 曲面与空间曲线

![二次曲面标准方程、旋转曲面与截痕法](/math/math-surface.svg)

| 曲面 | 标准方程（`a,b,c>0`） | 截痕特征 |
| --- | --- | --- |
| 椭球面 | $\dfrac{x^{2}}{a^{2}}+\dfrac{y^{2}}{b^{2}}+\dfrac{z^{2}}{c^{2}}=1$ | 各方向截痕为椭圆 |
| 单叶双曲面 | $\dfrac{x^{2}}{a^{2}}+\dfrac{y^{2}}{b^{2}}- \dfrac{z^{2}}{c^{2}}=1$ | 水平截椭圆，含直线 |
| 双叶双曲面 | $\dfrac{x^{2}}{a^{2}}- \dfrac{y^{2}}{b^{2}}- \dfrac{z^{2}}{c^{2}}=1$ | 沿 x 轴分两叶 |
| 椭圆锥面 | $\dfrac{x^{2}}{a^{2}}+\dfrac{y^{2}}{b^{2}}- \dfrac{z^{2}}{c^{2}}=0$ | 过原点的直线族 |
| 椭圆抛物面 | $z= \dfrac{x^{2}}{a^{2}}+\dfrac{y^{2}}{b^{2}}$ | 水平截椭圆 |
| 双曲抛物面（马鞍面） | $z= \dfrac{x^{2}}{a^{2}}- \dfrac{y^{2}}{b^{2}}$ | 水平截双曲线 |
| 柱面 | 方程缺一个变量（如 $x^{2}+y^{2}=R^{2}$） | 母线平行缺失变量的轴 |
| 球面 | $(x- x_{0})^{2}+(y- y_{0})^{2}+(z- z_{0})^{2}=R^{2}$ | — |

**旋转曲面**：`yOz` 面上 `f(y,z)=0` 绕 `z` 轴旋转 ⇒ 把 `y` 换成 $\pm\sqrt{x^{2}+y^{2}}$；绕 `y` 轴则把 `z` 换成 $\pm\sqrt{x^{2}+z^{2}}$。
**截痕法**：用 `z=k`、`x=k`、`y=k` 的平面去截，看截痕类型随 `k` 的变化，拼出整体形状。
**空间曲线**：一般式 = 两曲面 `F=0, G=0` 交线；参数式 `x=x(t), y=y(t), z=z(t)`（如圆柱螺线 $x=a \cos t, y=a \sin t, z=bt$）；在 `xOy` 面的投影由「消去 z 得 `H(x,y)=0`，再与 `z=0` 联立」得到。

::: danger 易错 · 空间解析几何
- $a \times b$ 反交换、$a \cdot b$ 交换；混合积是行列式，对换两列变号。
- 直线一般式中方向向量是两法向量的**叉积**；求线面夹角用 `sin`（不是 `cos`）。
- 曲面方程「缺变量」才是柱面；只含 $x^{2}+y^{2}$ 形式且含 $z^{2}$ 的是旋转曲面，别混。
:::

---

## 第 9 章 多元函数微分学及其应用（★★★）

### 9.1 二重极限、偏导数与全微分

![偏导数、全微分、链式法则、方向导数与梯度](/math/math-multivariable.svg)

| 概念 | 定义 / 判据 |
| --- | --- |
| 二重极限 | $\forall \epsilon>0 \exists \delta>0, 0<\sqrt{(x- x_{0})^{2}+(y- y_{0})^{2}}<\delta \Rightarrow\vert f- A\vert <\epsilon$；要求**沿任意路径**趋于同一值 |
| 累次极限 | `lim_x lim_y f` 与 `lim_y lim_x f`；二者存在且不等 ⇒ 二重极限不存在（反之不成立） |
| 偏导数 | $f_{x}(x_{0},y_{0})=\lim \dfrac{f(x_{0}+h,y_{0})- f(x_{0},y_{0})}{h}$（固定其余变量） |
| 全微分 | $\Delta z= A\Delta x+B\Delta y+o(\rho)$，$\rho=\sqrt{\Delta x^{2}+\Delta y^{2}}$ ⇒ $dz=f_{x}dx+f_{y}dy$ |

**关系图（二元，与一元差别很大）**：

$$
\begin{gathered}
\text{偏导数连续} \; \Rightarrow \; \text{可微} \; \Rightarrow \; \text{连续} \; \Rightarrow \; \text{二重极限存在} \\
\text{⇓ } \\
\text{偏导数存在（且各方向导数存在）} \\
\text{反例：偏导数存在但「不连续」「不可微」都成立} \; -- \; \text{与一元「可导} \; \Rightarrow \; \text{连续」截然不同}
\end{gathered}
$$

::: danger 易错 · 多元微分
- 判定二重极限**不存在**：沿 $y=kx$ 得依赖 $k$ 的值，或沿 $y=x$ 与 $y=x^{2}$ 得不同值，即可判否。但沿有限条路径都相同**不能**判存在。
- 偏导数存在 ⇏  连续、⇏  可微；可微才保证「沿任意方向的方向导数都存在且等于 $\nabla f \cdot e$」。
- 二阶混合偏导 $f_{xy}= f_{gammax}$ 需要**连续**条件（克莱罗 / 施瓦茨定理），否则可能不等。
:::

### 9.2 复合、隐函数与几何应用

**链式法则**（先画变量关系图，"一分多合"）：
`z=f(u,v)`, `u=u(x,y)`, `v=v(x,y)` ⇒ $\dfrac{\partial z}{\partial x}= f_{u}u_{x}+f_{v}v_{x}$，$\dfrac{\partial z}{\partial y}$ 同理。
**一阶全微分形式不变性**：无论 `u,v` 是自变量还是中间变量，$dz= f_{u}du+f_{vdv}$ 形式不变（求全微分与验算都靠它）。

**隐函数求导**：`F(x,y,z)=0` ⇒ $\dfrac{\partial z}{\partial x}=- \dfrac{F_{x}}{F_{z}}$、$\dfrac{\partial z}{\partial y}=- \dfrac{F_{y}}{F_{z}}$（$F_{z}=0$）；方程组 `F=G=0` 用雅可比行列式 $J= \dfrac{\partial(F,G)}{\partial}(u,v)= 0$，解线性方程组求各偏导。

**几何应用**：
- 曲面 `F(x,y,z)=0` 在点 $P_{0}$ 的法向量 $\nabla F(P_{0})$，切平面 $F_{x}(x- x_{0})+F_{y}(y- y_{0})+F_{z}(z- z_{0})=0$，法线 $\dfrac{x- x_{0}}{F_{x}}= \dfrac{y- y_{0}}{F_{y}}= \dfrac{z- z_{0}}{F_{z}}$；
- 空间曲线 `r(t)=(x(t),y(t),z(t))` 的切向量 $r'(t_{0})$，切线 $\dfrac{x-x_{0}}{x'}=\dfrac{y-y_{0}}{y'}=\dfrac{z-z_{0}}{z'}$，法平面 $x'(x- x_{0})+y'(y- y_{0})+z'(z- z_{0})=0$。

### 9.3 方向导数、梯度与极值

**方向导数**（`f` 可微时）：$\dfrac{\partial f}{\partial l}= f_{x}\cos \alpha+f_{y}\cos \beta+f_{z} \cos \gamma= \nabla f \cdot e_{l}$。
**梯度** $\nabla f=(f_{x},f_{y},f_{z})$：指向函数增长最快方向，$| \nabla f|$ 是最大方向导数；负梯度是下降最快方向（梯度下降算法的数学来源）；梯度与等值面正交。

::: tip 工作例题 · 方向导数
$f=x^{2}y+\sin(xy)$ ⇒ $f_{x}=2xy+y \cos(xy)$，$f_{y}=x^{2}+x \cos(xy)$。
在 `(0,1)`：$\nabla f=(1, 0)$。沿 $e=\left(\dfrac{1}{\sqrt{2}}, \dfrac{1}{\sqrt{2}}\right)$ 的方向导数 $= 1 \cdot\left(\dfrac{1}{\sqrt{2}}\right)+0= \dfrac{1}{\sqrt{2}} \approx 0.7071$；
最大方向导数 $=| \nabla f|=1$（沿 x 轴正向），最小 $=- 1$（沿 x 轴负向）。
:::

![无条件极值、条件极值与拉格朗日乘数法](/math/math-extremum.svg)

| 判别 | 结论 |
| --- | --- |
| 无条件极值必要条件 | $f_{x}=f_{y}=0$（驻点）或偏导不存在点 |
| 记 $A=f_{xx}, B=f_{xy}, C=f_{yy}$，$\Delta=AC- B^{2}$ | $\Delta>0$ 且 `A<0` 极大；$\Delta>0$ 且 `A>0` 极小；$\Delta<0$ 鞍点；$\Delta=0$ 失效 |
| 海森矩阵 | 正定 ⇒ 极小、负定 ⇒ 极大、不定 ⇒ 鞍点 |
| 条件极值 | $L=f+\lambda \phi$（多约束 $L=f+\sum \lambda_{i}\phi_{i}$），解 $\nabla L=0$；几何含义 $\nabla f ∥ \nabla \phi$ |

::: tip 工作例题 · 两组极值
$$
\begin{gathered}
(1) f=x^{2}+y^{2} \; \text{在} \; \text{(0,0)} \; \text{：} \; A=C=2, B=0 \Rightarrow \Delta=4>0 \; \text{且} \; A>0 \Rightarrow \; \text{极小值} \; \text{0} \\
\text{f=xy} \; \text{在} \; \text{(0,0)} \; \text{：} \; A=C=0, B=1 \Rightarrow \Delta=- 1<0 \Rightarrow \; \text{鞍点（不是极值点）} \\
\text{(2)} \; \text{条件极值：} \; \min x^{2}+y^{2} s.t. x+y=1 \\
L=x^{2}+y^{2}- \lambda(x+y- 1) \; \text{，} \; \frac{\partial L}{\partial x}=2x- \lambda=0, \frac{\partial L}{\partial y}=2y- \lambda=0 \Rightarrow x=y \\
\text{代入约束} \; \Rightarrow x=y=\frac{1}{2} \Rightarrow f_{\min}= \frac{1}{4}+\frac{1}{4}= \frac{1}{2} \\
(3) f=xy s.t. x^{2}+y^{2}=1 \Rightarrow \; \text{极大} \; \text{1/2} \; \text{（} \; x=y=±\frac{1}{\sqrt{2}} \; \text{）、极小} \; - \frac{1}{2}
\end{gathered}
$$
:::

**闭区域最值流程**：① 内部驻点值；② 边界上的最值（代入边界化一元，或对边界再用拉格朗日）；③ 比较全部候选。依据是有界闭区域上连续函数必有最值（Weierstrass 定理）。

::: danger 易错 · 极值
- 驻点不一定是极值点（鞍点）；极值点也可能偏导不存在（如 $z=\sqrt{x^{2}+y^{2}}$ 在原点取极小）。
- $\Delta=0$ 时二阶判别失效，须回到定义或看更高阶（如 $z=x^{4}+y^{4}$ 与 $z=x^{4}- y^{4}$）。
- 拉格朗日乘数法给出的是**候选点**，$\lambda$ 本身不是所求；含不等式约束时需另查边界与 KKT 条件。
:::

**补充 · 二元泰勒与最小二乘**：二元泰勒 $f(x_{0}+h,y_{0}+k)= f+(h \partial_{x}+k \partial_{y})f+ \dfrac{1}{2}(h \partial_{x}+k \partial_{y})^{2}f+ \cdots$，是极值充分条件的证明基础；教材「最小二乘法」一节即令残差平方和对参数偏导为零，本质是本章的无条件极值。

### 9.4 多元微分「四个概念」的反例库

| 命题 | 真伪 | 反例 / 理由 |
| --- | --- | --- |
| 偏导存在 ⇒ 连续 | 假 | $f=\dfrac{xy}{x^{2}+y^{2}}$（(0,0) 补 0）：偏导存在但不连续 |
| 连续 ⇒ 偏导存在 | 假 | `f=|x|+|y|` |
| 各方向方向导数存在 ⇒ 可微 | 假 | 方向导数只沿直线，可微要求全增量线性逼近 |
| 偏导连续 ⇒ 可微 | 真 | 充分条件（教材标准定理） |
| 可微 ⇒ 偏导连续 | 假 | 见第 2 章 $x^{2} \sin\left(\dfrac{1}{x}\right)$ 的一元类比，二元可构造类似例子 |
| 混合偏导恒相等 | 假 | 需连续条件；经典反例 $f=\dfrac{xy(x^{2}- y^{2})}{x^{2}+y^{2}}$ 在原点 $f_{xy}=f_{gammax}$ |

---

## 第 10 章 重积分（★★★）

### 10.1 二重积分

![二重/三重积分、换序与极柱球坐标](/math/math-multiple-integral.svg)

$\iint _{D} f(x,y)d\sigma= \lim \sum f(\xi_{i},\eta_{i})\Delta \sigma_{i}$；几何上是曲顶柱体的**代数体积**（$f \ge 0$ 时为正）。

| 区域型 | 化为累次积分 |
| --- | --- |
| X 型 $a \le x \le b, \phi_{1}(x) \le y \le \phi_{2}(x)$ | $\int_{a}^{b} dx \int_{\phi_{1}}^{\phi_{2}} f(x,y)dy$ |
| Y 型 $c \le y \le d, \psi_{1}(y) \le x \le \psi_{2}(y)$ | $\int_{c}^d dy \int_{\psi_{1}}^{\psi_{2}} f(x,y)dx$ |
| 极坐标 $x=r \cos \theta, y=r \sin \theta$ | $\iint  f(r \cos \theta, r \sin \theta) \cdot r dr d\theta$（**别漏雅可比 r**） |

**交换积分次序三步**：① 由原上下限写出区域不等式并画图；② 换一个视角重写不等式；③ 若区域非简单型则**分块**。

::: tip 工作例题 · 换序与极坐标
$$
\begin{gathered}
(1) \int_{0}^{1}dx \int_{x}^{1} f(x,y)dy= \int_{0}^{1}dy \int_{0}^{y} f(x,y)dx \\
\text{（区域为} \; 0 \le x \le y \le 1 \; \text{的三角形，换序后先} \; \text{x} \; \text{后} \; \text{y} \; \text{）} \\
(2) \iint _{x^{2}+y^{2} \le a^{2}} e^{-(x^{2}+y^{2})}dxdy= \int_{0}^{2\pi}d\theta \int_{0}^{a} e^{- r^{2}} r dr \\
= 2\pi \cdot[- \frac{1}{2} e^{- r^{2}}]_{0}^{a}= \pi(1- e^{- a^{2}}) \; \text{；} \; a=1 \Rightarrow \pi(1- e^{-1}) \approx 1.9859 \\
\text{(3)} \; \text{教材经典：} \; \iint _{D} e^{- y^{2}}dxdy \; \text{（} \; \text{D} \; \text{由} \; \text{y=x, y=1, x=0} \; \text{围成）} \\
\text{先对} \; \text{y} \; \text{积分不可行（} \; e^{- y^{2}} \; \text{无初等原函数），必须换序先对} \; \text{x} \; \text{：} \\
\int_{0}^{1}dy \int_{0}^{y} e^{- y^{2}}dx= \int_{0}^{1} y e^{- y^{2}}dy= \frac{1}{2}(1- e^{-1}) \\
\text{(4)} \; \text{可分离：} \; \iint _{[a,b] \times[c,d]} g(x)h(y)dxdy=\left( \int_{a}^{b} g dx\right)\left( \int_{c}^d h dy\right) \\
\Rightarrow \iint _{[0,1]^{2}}(x+y)dxdy= \frac{1}{2}+ \frac{1}{2}= 1
\end{gathered}
$$
:::

**对称性**（先于计算使用）：若 $D$ 关于 $y$ 轴对称且 $f$ 对 $x$ 为奇 ⇒ 积分为 0、为偶 ⇒ 两倍；若 D 关于 $y=x$ 对称，则 $\iint _{D} f(x,y)d\sigma= \iint _{D} f(y,x)d\sigma$（轮换对称性，可把 $\iint  \dfrac{f(x)}{f(x)+f(y)}$ 化为面积的一半）。

### 10.2 三重积分

| 坐标 | 变换 | 体积元 | 适用区域 |
| --- | --- | --- | --- |
| 直角 | — | `dx dy dz` | 一般；投影法（先 z）/ 截面法（先 xy） |
| 柱 | $x=r \cos \theta, y=r \sin \theta, z=z$ | $r dr d\theta dz$ | 旋转体、含 $x^{2}+y^{2}$ |
| 球 | $x=\rho \sin \phi \cos \theta, y=\rho \sin \phi \sin \theta, z=\rho \cos \phi$ | $\rho^{2} \sin \phi d\rho d\phi d\theta$ | 球体、锥体、含 $x^{2}+y^{2}+z^{2}$ |
| 一般换元 | `x=x(u,v,w)` 等 | `|J| du dv dw` | $J= \dfrac{\partial(x,y,z)}{\partial}(u,v,w)$ |

**φ 是与 z 轴正向的夹角**（$0 \le \phi \le \pi$），$\theta \in[0,2\pi]$；常见错误是把 $\sin \phi$ 写成 $\cos \phi$、或把 $\phi$ 当成与 `xOy` 面的夹角。

::: tip 工作例题 · 三重积分
$$
\begin{gathered}
(1) \iiint _{x^{2}+y^{2}+z^{2} \le R^{2}} 1 dV= \frac{4\pi R^{3}}{3} \; \text{（} \; R=1 \Rightarrow \frac{4\pi}{3} \approx 4.18879 \; \text{）} \\
\text{(2) 上半球} \; \iiint_{\Omega} z\,dV \; (\Omega: x^{2}+y^{2}+z^{2}\le 1,\, z\ge 0) \\
= \int_{0}^{2\pi}d\theta \int_{0}^{\frac{\pi}{2}}\sin \phi \cos \phi d\phi \int_{0}^{1} \rho^{3} d\rho \\
= 2\pi \cdot\left(\frac{1}{2}\right) \cdot\left(\frac{1}{4}\right)= \frac{\pi}{4} \approx 0.785398 \\
(3) \iiint _\Omega(x^{2}+y^{2}) dV \; \text{（} \; \Omega \; \text{为圆柱} \; x^{2}+y^{2} \le 1, 0 \le z \le 1 \; \text{），柱坐标：} \\
\int_{0}^{2\pi}d\theta \int_{0}^{1} r^{3} dr \int_{0}^{1} dz= 2\pi \cdot \frac{1}{4}= \frac{\pi}{2}
\end{gathered}
$$
:::

**应用**：曲面面积 $A= \iint _{D_{xy}} \sqrt{1+z_{x}^{2}+z_{y}^{2}} dxdy$（`z=z(x,y)`）；平面薄片质量 $M=\iint \rho d\sigma$、质心 $\bar{x}=\iint x\rho \dfrac{d\sigma}{M}$、转动惯量 $I_{z}=\iint (x^{2}+y^{2})\rho d\sigma$；万有引力按分量积分。

::: danger 易错 · 重积分
- 换序/换元后**上下限与雅可比必须同步改**；极坐标漏 `r`、球坐标漏 $\rho^{2}\sin \phi$ 最常见。
- 二重积分中值定理 $\iint _{D} f d\sigma= f(\xi,\eta) \cdot Area(D)$ 要求 `f` 连续、`D` 闭连通。
- 被积函数含绝对值或分段时，必须按符号/分界把区域切开再积分。
:::

### 10.3 重积分换序的通用算法

① 从累次积分上下限写出不等式组；② 在 `xOy` 平面画出区域边界曲线并求交点；③ 用「穿线法」：对固定的 y 从左边界穿到右边界，读出 `x` 的上下限；④ 若穿线过程中边界函数发生变化（区域不是 Y 简单型），**按变化点分块**；⑤ 写出新的累次积分并检查端点。
**对称性优先级**：奇偶性 → 轮换对称 → 区域可加性 → 换元（极/柱/球）→ 直接积分。先化简再动笔是节省时间的关键。

---

## 第 11 章 曲线积分、曲面积分与场论（★★★）

### 11.1 两类线积分与两类面积分

![两类线面积分、格林/高斯/斯托克斯公式与散度旋度](/math/math-field.svg)

| 类型 | 记号 | 与方向 | 计算要点 |
| --- | --- | --- | --- |
| 第一类（对弧长） | $\int_{L} f(x,y,z)ds$ | 无关 | 参数化后代 $ds=\sqrt{\dot{x}^{2}+\dot{y}^{2}+\dot{z}^{2}}dt$；下限须小于上限 |
| 第二类（对坐标） | $\int_{L} Pdx+Qdy+Rdz$ | **有关**（反向变号） | 代入参数方程，起终点决定上下限（可上大下小） |
| 第一类面积分 | $\iint _{\Sigma} f dS$ | 无关（无方向） | 投影 + $dS= \sqrt{1+z_{x}^{2}+z_{y}^{2}}dxdy$ |
| 第二类面积分 | $\iint _{\Sigma} P dydz+Q dzdx+R dxdy$ | **与侧有关** | 投影到相应坐标面并按侧定正负；或合一投影法 |

**两类之间的联系**：$\int Pdx+Qdy= \int(P \cos \alpha+Q \cos \beta)ds$；$\iint P dydz+Q dzdx+R dxdy= \iint (P \cos \alpha+Q \cos \beta+R \cos \gamma)dS$，其中 $(\cos \alpha, \cos \beta, \cos \gamma)$ 是切向/法向的方向余弦。

### 11.2 三大公式

| 公式 | 表达式 | 条件 |
| --- | --- | --- |
| **格林** | $\oint _{L} Pdx+Qdy= \iint _{D}\left( \dfrac{\partial Q}{\partial x}- \dfrac{\partial P}{\partial y}\right)dxdy$ | `L` 为正向（逆时针）分段光滑闭曲线，`P,Q` 在 `D` 上有一阶连续偏导 |
| **高斯** | $\oiint _{\Sigma} P dydz+Q dzdx+R dxdy= \iiint _\Omega\left( \dfrac{\partial P}{\partial x}+ \dfrac{\partial Q}{\partial y}+ \dfrac{\partial R}{\partial z}\right)dV$ | $\sum$ 取**外侧**闭曲面 |
| **斯托克斯** | $\oint _\Gamma Pdx+Qdy+Rdz= \iint _{\Sigma}(rot A) \cdot n dS$ | $\Gamma$ 与 $\sum$ 的侧符合右手规则 |

**统一视角**：三者都是「**边界上的积分 = 内部某种导数的积分**」，即广义斯托克斯定理 $\int_{\partial M} \omega= \int_{M} d\omega$；牛顿–莱布尼茨是它在区间 `[a,b]` 上的 1 维特例。

**路径无关与全微分求积**（单连通域内等价）：
$\dfrac{\partial P}{\partial y}= \dfrac{\partial Q}{\partial x}$ ⇔ $\oint _{L} Pdx+Qdy= 0$（任意闭路）⇔ 积分与路径无关 ⇔ `Pdx+Qdy` 是某 `u(x,y)` 的全微分，且 $u(x,y)= \int_{(x_{0},y_{0})}^{(x,y)} Pdx+Qdy$（沿折线计算）。

**散度与旋度**：$div A= \dfrac{\partial P}{\partial x}+ \dfrac{\partial Q}{\partial y}+ \dfrac{\partial R}{\partial z}$（标量，通量源强度）；$rot A= \nabla \times A$（向量，环流强度）；$\nabla\left(\dfrac{1}{r}\right)$、$\nabla \cdot\left(\dfrac{r}{r^{3}}\right)$ 等恒等式在场论中常用。

::: tip 工作例题 · 三大公式
$$
\begin{gathered}
\text{(1)} \; \text{格林求面积：取} \; P=- \frac{y}{2}, Q=\frac{x}{2} \Rightarrow \oint_{L}\dfrac{x\,dy-y\,dx}{2}= Area(D) \\
\Rightarrow \; \text{单位圆上} \; \oint  x dy- y dx= 2\pi \approx 6.28319 \\
\text{(2)} \; \text{奇点陷阱：} \; \oint_{L}\dfrac{x\,dy-y\,dx}{x^{2}+y^{2}} = 2\pi \\
\text{此处} \; \text{P,Q} \; \text{在原点无定义，不能直接套格林（会错得} \; \text{0} \; \text{）；} \\
\text{须挖去以原点为心的小圆} \; \epsilon \; \text{，在环形域用格林（旋度为} \; \text{0} \; \text{）} \; \Rightarrow \; \text{等于小圆上的积分} \; 2\pi \\
\text{(3)} \; \text{高斯：} \; \oiint _{S} x dydz+y dzdx+z dxdy= \iiint _\Omega 3 dV= 3V \\
\text{单位球} \; V=\frac{4\pi}{3} \Rightarrow 4\pi \approx 12.56637 \\
\text{(4) div(x,y,z)=3} \; \text{；} \; rot(- y,x,0)=(0,0,2) \; \text{；} \; \nabla(x^{2}+y^{2}+z^{2})=(2x,2y,2z)
\end{gathered}
$$
:::

::: danger 易错 · 三大公式
- 非闭曲线要**补线**成闭、非闭曲面要**补面**成闭，补上的部分最后要减掉。
- 区域含奇点（分母为零、偏导不连续）必须**挖洞**，否则格林/高斯结论错误。
- 方向：格林逆时针为正、高斯外侧为正、斯托克斯与法向满足右手规则；取反则整体变号。
- 第一类积分与方向无关且可用对称性；第二类积分与方向/侧有关，先定向再计算。
:::

**补充 · 场论术语**：通量 $\Phi=\iint _{\Sigma} A \cdot n dS$（高斯：通量 = 散度的体积分）；环流量 $\Gamma=\oint _\Gamma A \cdot dl$（斯托克斯：环流量 = 旋度通量）；$div A \equiv 0$ 称无源场（沿任意闭曲面的通量为零），$rot A \equiv 0$ 且在单连通域内称无旋场/保守场（存在势函数）。梯度场必无旋，无旋场在单连通域内必为梯度场。

### 11.3 三大公式的统一形式与场论恒等式

广义斯托克斯定理 $\int_{\partial M} \omega= \int_{M} d\omega$ 在外微分语言下统一：
- `n=1`：牛顿–莱布尼茨（$\int_{[a,b]} dF= F(b)- F(a)$）；
- `n=2`：格林公式（平面区域边界是曲线）；
- `n=3`：高斯（体边界是闭曲面）、斯托克斯（曲面边界是闭曲线）——取决于取 2-形式还是 1-形式。

**常用场论恒等式**：

<div class="kb-tile-2col">

<div class="kb-tile-item">

$\nabla \times( \nabla f)=0$（梯度场无旋）

</div>

<div class="kb-tile-item">

$\nabla \cdot( \nabla \times A)=0$（旋度场无源）

</div>

<div class="kb-tile-item">

$\nabla \cdot(f A)= \nabla f \cdot A+f \nabla \cdot A$

</div>

<div class="kb-tile-item">

$\nabla^{2}f= \nabla \cdot( \nabla f)$（拉普拉斯算子）

</div>

</div>

这些是电磁学、流体力学方程的语言基础。

---

## 第 12 章 无穷级数（★★★）

### 12.1 常数项级数

![判敛决策树、幂级数与傅里叶级数](/math/math-series.svg)

$\sum u_{n}$ 收敛 ⇔ 部分和序列 $S_{n}= \sum_{k=1}^{n} u_{k}$ 收敛。**必要条件**：$\lim u_{n}= 0$（不满足立即发散；满足未必收敛，如调和级数）。

| 类型 | 审敛法 | 判据 |
| --- | --- | --- |
| 正项 | 比较 / 极限比较 | 与 $\sum\dfrac{1}{n^{p}}$（`p>1` 收敛）、几何级数 $\sum q^{n}$（`|q|<1` 收敛）比 |
| 正项 | 比值（达朗贝尔） | $\rho=\lim \dfrac{u_{n+1}}{u_{n}}$：$\rho<1$ 收敛、$\rho>1$ 发散、`=1` 失效 |
| 正项 | 根值（柯西） | $\rho=\lim_{n\to\infty}\sqrt[n]{u_{n}}$，同上 |
| 正项 | 积分判别 | $u_{n}=f(n)$，`f` 正递减 ⇒ $\sum u_{n}$ 与 $\int_{1}^\infty f(x)dx$ 同敛散 |
| 交错 | 莱布尼茨 | $u_{n}$ 单调递减且趋于 0 ⇒ 收敛，余项 $\vert r_{n}\vert  \le u_{n+1}$ |
| 一般 | 绝对收敛 | $\sum\vert u_{n}\vert $ 收敛 ⇒ $\sum u_{n}$ 收敛；反之称条件收敛 |

**收敛级数的性质**：可逐项加减、乘常数、任意加括号；**绝对收敛可任意重排且和不变**，条件收敛重排可改变和甚至发散（黎曼重排定理）。

::: tip 工作例题 · 五个经典级数
$$
\begin{gathered}
\text{(1)} \; \text{几何级数} \; \sum_{n=0}^\infty q^{n}= \frac{1}{1- q} \; \text{（} \; \text{|q|<1} \; \text{）；} \; |q| \ge 1 \; \text{发散} \\
\text{(2) p} \; \text{级数} \; \sum\frac{1}{n^{p}} \; \text{：} \; \text{p>1} \; \text{收敛、} \; p \le 1 \; \text{发散；} \; \sum\frac{1}{n} \; \text{发散（调和级数）} \\
\text{(3)} \; \text{裂项} \; \sum_{n=1}^\infty \frac{1}{n(n+1)}= \sum\left(\frac{1}{n}- \frac{1}{n+1}\right)= 1 \\
\text{(4)} \; \text{交错调和} \; \sum\frac{(-1)^{n+1}}{n}= \ln 2 \approx 0.693147 \; \text{（条件收敛）} \\
(5) \sum\frac{(-1)^{n+1}}{n^{2}}= \frac{\pi^{2}}{12} \approx 0.822467 \; \text{（绝对收敛）}
\end{gathered}
$$
:::

### 12.2 幂级数与函数展开

$\sum a_{n}(x- x_{0})^{n}$ 的**收敛半径** $R= \lim|\dfrac{a_{n}}{a_{n+1}}|$ 或 $R=\dfrac{1}{\limsup_{n\to\infty}\sqrt[n]{|a_{n}|}}$；收敛区间 $(x_{0}- R, x_{0}+R)$，**端点必须单独判断**才得收敛域。

| 性质 | 内容 |
| --- | --- |
| 阿贝尔定理 | 在收敛区间内闭一致收敛；和函数在收敛区间内连续 |
| 逐项运算 | 可逐项求导、逐项积分，**收敛半径不变**（端点收敛性可能改变） |
| 和函数求法 | 逐项求导/积分化为几何级数求和，再积分/求导还原；注意 `S(0)` 定常数 |

::: tip 工作例题 · 和函数
$$
\begin{gathered}
\sum_{n=0}^\infty x^{n}= \frac{1}{1- x},|x|<1 \\
\text{逐项求导：} \; \sum_{n=1}^\infty n x^{n- 1}= \frac{1}{(1- x)^{2}} \\
\text{两边乘} \; \text{x} \; \text{：} \; \sum_{n=1}^\infty n x^{n}= \frac{x}{(1- x)^{2}} \\
\text{验算} \; x=\frac{1}{2} \; \text{：右侧} \; = \frac{0.5}{0.25}= 2 \; \text{；前} \; \text{50} \; \text{项部分和} \; \text{= 2.0000 }\checkmark \\
\sum_{n=1}^\infty \frac{x^{n}}{n}=- \ln(1- x),- 1 \le x<1 \\
\text{（由} \; \int_{0}^{x}\frac{1}{1-t}\,dt \; \text{逐项积分得到；端点} \; x=- 1 \; \text{收敛、} \; \text{x=1} \; \text{发散）}
\end{gathered}
$$
:::

**五个麦克劳林展开**（见第 1.3 节表），收敛域分别为：

<div class="kb-tile-2col">

<div class="kb-tile-item">

$e^{x}$、$\sin x$、$\cos x$ 为 $(- \infty,+ \infty)$

</div>

<div class="kb-tile-item">

$\ln(1+x)$ 为 $(-1,1]$

</div>

<div class="kb-tile-item">

$(1+x)^\alpha$ 依赖 $\alpha$，一般 $(- 1,1)$

</div>

</div>

**补充 · 一致收敛**：函数项级数 $\sum u_{n}(x)$ 的一致收敛性（魏尔斯特拉斯 M 判别法：$|u_{n}(x)| \le M_{n}$ 且 $\sum M_{n}$ 收敛）保证和函数连续、可逐项积分与逐项求导（还需导函数一致收敛）。这解释「为何幂级数能在收敛区间内任意逐项运算」，教材把它列为选学但逻辑上不可缺。

### 12.3 傅里叶级数

周期为 $2\pi$ 的函数：

$$\frac{f(x) \sim a_{0}}{2}+ \sum_{n=1}^\infty(a_{n} \cos nx+ b_{n} \sin nx)$$

$a_{n}=\left(\dfrac{1}{\pi}\right) \int_{- \pi}^{\pi} f(x)\cos nx dx$，$b_{n}=\left(\dfrac{1}{\pi}\right) \int_{- \pi}^{\pi} f(x)\sin nx dx$。

**狄利克雷收敛定理**（教材核心）：若 `f` 在一个周期上连续或只有有限个第一类间断点，且只有有限个极值点，则级数收敛，且
- 在连续点收敛于 `f(x)`；
- 在间断点收敛于 $\dfrac{f(x^{-})+f(x^{+})}{2}$；
- 在端点 $±\pi$ 收敛于 $\dfrac{f(- \pi^{+})+f(\pi^{-})}{2}$。

| 情形 | 展开形式 |
| --- | --- |
| `f` 奇（$- \pi,\pi$） | 正弦级数，只含 $b_{n}$（$f(x)=x \Rightarrow x= 2\sum(- 1)^{n+1} \sin \dfrac{nx}{n}$） |
| `f` 偶（$- \pi,\pi$） | 余弦级数，只含 $a_{n}$（$f(x)=\vert x\vert  \Rightarrow\vert x\vert = \dfrac{\pi}{2}-\left(\dfrac{4}{\pi}\right)\sum \dfrac{\cos(2k- 1)x}{(2k- 1)^{2}}$） |
| $[0,\pi]$ 上给定 | 作奇延拓得正弦级数、偶延拓得余弦级数 |
| 周期 `2l` | 把 `nx` 换成 $\dfrac{n\pi x}{l}$，系数中 $\dfrac{1}{\pi}$ 换 `1/l` |

::: tip 工作例题 · 用傅里叶级数求数项级数的和
$$
\begin{gathered}
x= 2\sum_{n=1}^\infty \frac{(- 1)^{n+1} \sin(nx)}{n}, x \in(- \pi,\pi) \\
\text{取} \; x=\frac{\pi}{2} \; \text{：} \; \frac{\pi}{2}= 2\left(1- \frac{1}{3}+ \frac{1}{5}- \frac{1}{7}+ \cdots\right) \\
\Rightarrow 1- \frac{1}{3}+ \frac{1}{5}- \cdots= \frac{\pi}{4} \approx 0.785398 \; \text{（莱布尼茨级数）} \\
|x|= \frac{\pi}{2}-\left(\frac{4}{\pi}\right)\sum_{k=1}^\infty \frac{\cos((2k- 1)x)}{(2k- 1)^{2}}, x \in[- \pi,\pi] \\
\text{取} \; \text{x=0} \; \text{：} \; 0= \frac{\pi}{2}- \frac{\left(\frac{4}{\pi}\right)\sum 1}{(2k- 1)^{2}} \Rightarrow \sum\frac{1}{(2k-1)^{2}}=\frac{\pi^{2}}{8}
\end{gathered}
$$
:::

::: danger 易错 · 级数
- $\lim u_{n}= 0$ 只是**必要**条件；调和级数是最经典反例。
- 比值/根值法 $\rho=1$ 时**失效**，必须换比较、积分或拉比/高斯判别法（如 $\sum\dfrac{1}{n}$、$\sum\dfrac{1}{n^{2}}$ 都是 $\rho=1$ 但敛散不同）。
- 交错级数用莱布尼茨判收敛，但**绝对收敛性要另判** $\sum|u_{n}|$；「收敛」与「绝对收敛」不可混。
- 逐项求导/积分后收敛半径不变，但**端点**可能从收敛变发散（如 $\sum\dfrac{x^{n}}{n}$ 与 $\sum x^{n-1}$），必须重新检验。
- 傅里叶级数在间断点收敛到左右极限的平均值，**不是** `f(x)`；端点同理。
:::

### 12.4 级数判敛法的强弱排序

$$
\begin{gathered}
\text{必要条件（通项} \; \to 0 \; \text{）} \; \to \; \text{正项：比较} \; \text{/} \; \text{极限比较（最基础）} \\
\to \; \text{比值} \; \text{/} \; \text{根值（对阶乘、指数型最有效；} \; \rho=1 \; \text{失效）} \\
\to \; \text{积分判别、拉比判别、高斯判别（对} \; \rho=1 \; \text{的临界情形）} \\
\text{交错：莱布尼茨（收敛）} \; \to \; \text{再看} \; \sum|u_{n}| \; \text{（绝对} \; \text{or} \; \text{条件）}
\end{gathered}
$$
**根值强于比值**：由 $\lim \dfrac{u_{n+1}}{u_{n}}= \rho \Rightarrow \lim_{n\to\infty}\sqrt[n]{u_{n}}= \rho$，反之不然；故含 `n` 次幂的项优先用根值。
**阿贝尔 / 狄利克雷判别法**：处理 $\sum a_{n}b_{n}$ 型，若 $\sum a_{n}$ 部分和有界且 $b_{n}$ 单调趋于 0 ⇒ 收敛（狄利克雷）；这解释了交错级数判别的一般原理。

::: tip 补充 · 积分判别的两个经典临界例
$\sum \dfrac{1}{n \ln n}$ 与 $\sum \dfrac{1}{n(\ln n)^{2}}$ 都是比值/根值 $\rho=1$ 失效、比较判别也难处理的临界级数，用积分判别（换元 $u=\ln x$）：
$\int_{2}^\infty \dfrac{dx}{x \ln x}=[\ln \ln x]_{2}^\infty= \infty$ ⇒ **发散**；
$\int_{2}^\infty \dfrac{dx}{x(\ln x)^{2}}=[- \dfrac{1}{\ln} x]_{2}^\infty= \dfrac{1}{\ln} 2$ ⇒ **收敛**。
记忆规律：分母每多套一层「收敛得更快」的因子（`ln n` → $(\ln n)^{2}$），敛散性就可能翻转——这是判断题最爱考的边界情形。
:::

### 12.5 傅里叶级数与幂级数的对照

| 维度 | 幂级数 | 傅里叶级数 |
| --- | --- | --- |
| 基函数 | $1, x, x^{2}, \cdots$（幂函数） | `1, cos nx, sin nx`（三角函数，正交系） |
| 系数来源 | 泰勒系数 $\dfrac{f^{(n)}(0)}{n}!$（局部信息） | 积分 $a_{n}, b_{n}$（**整体**信息，用正交性） |
| 收敛要求 | 函数解析 + 余项→0 | 狄利克雷条件（分段光滑，允许间断） |
| 适用范围 | 只能展开光滑解析函数 | 可展开有跳跃间断的周期函数 |
| 端点 | 收敛域端点单独判 | 间断点收敛到左右极限平均 |

**帕塞瓦尔等式**：$\left(\dfrac{1}{\pi}\right) \int_{- \pi}^{\pi} f^{2} dx= \dfrac{a_{0}^{2}}{2}+ \sum(a_{n}^{2}+b_{n}^{2})$，是「能量守恒」在频域的表述，也是求 $\sum\dfrac{1}{n^{4}}=\dfrac{\pi^{4}}{90}$ 一类级数和的工具。

### 12.6 高数与后续课程的接口

| 高数工具 | 后续课程如何使用 |
| --- | --- |
| 偏导数、梯度、拉格朗日乘数 | 机器学习梯度下降与带约束优化、微观经济学效用最大化与成本最小化 |
| 重积分、多重求和 | 概率论联合密度、边缘分布、期望；计量中的多重积分 |
| 级数与泰勒展开 | 数值分析误差估计、概率母函数、计量中非线性模型的线性化 |
| 常微分方程 | 宏观经济增长模型、物理/电路建模、动力系统 |
| 三大公式 / 场论 | 电磁学麦克斯韦方程、流体力学守恒律 |
| 傅里叶级数 | 信号处理 FFT、时间序列的谱分析、偏微分方程分离变量 |

::: danger 易错 · 跨课程迁移
- 经济学中的「边际」就是导数，但要注意**自变量是离散还是连续**、是否允许取微分；
- 机器学习里的「梯度」是多元函数的 $\nabla f$，但损失函数的可微性（ReLU、hinge）并非处处成立，需要次梯度；
- 概率密度积分要求 $\int f= 1$，这与「反常积分收敛」是同一套判敛工具。
:::

---

## 典型计算题逐步演算（可照抄的解题格式）

> 每道题按「识别类型 → 选方法 → 逐步演算 → 验算」四步展开，代码块内是考场可直接复用的书写格式。

### 演 1 · 极限（七类未定式）· 第 1 章

$$
\begin{gathered}
(1) \lim_{x \to 0}\frac{\sin(3x)}{5x} \\
\text{重要极限} \; \sin \frac{u}{u} \to 1 \; \text{：} \; = \lim \frac{\left(\frac{3}{5}\right) \cdot \sin(3x)}{3x}= \frac{3}{5}= 0.6 \\
(2) \lim_{x \to 0}\frac{e^{x}- 1- x}{x^{2}} \; \text{（} \; \text{0/0} \; \text{）} \\
\text{泰勒：} \; e^{x}= 1+ x+ \frac{x^{2}}{2}+ o(x^{2}) \Rightarrow \; \text{分子} \; = \frac{x^{2}}{2}+ o(x^{2}) \Rightarrow \; \text{极限} \; = \frac{1}{2} \\
(3) \lim_{x \to 0}\frac{\tan x- \sin x}{x^{3}} \; \text{（} \; \text{0/0} \; \text{，加减型不可用等价无穷小直接替换）} \\
\text{泰勒：} \; \tan x= x+ \frac{x^{3}}{3}+ o(x^{3}) \; \text{，} \; \sin x= x- \frac{x^{3}}{6}+ o(x^{3}) \\
\text{差} \; = \frac{x^{3}}{2} \Rightarrow \; \text{极限} \; = \frac{1}{2} \; \text{（数值验证} \; x=1e- 4 \; \text{得} \; \text{0.50000000} \; \text{）} \\
(4) \lim_{n \to \infty}\left(1+ \frac{2}{n}\right)^{n} \; \text{（} \; 1^\infty \; \text{）} \\
\text{取对数：} \; n \ln\left(1+\frac{2}{n}\right) \sim n \cdot\left(\frac{2}{n}\right)= 2 \Rightarrow \; \text{极限} \; = e^{2} \approx 7.389056 \\
(5) \lim_{x \to \infty}\frac{x+ \sin x}{x} \\
= 1+ \sin \frac{x}{x} \to 1 \; \text{；洛必达会得} \; 1+\cos x \; \text{（极限不存在）} \; \Rightarrow \; \text{此处洛必达失效}
\end{gathered}
$$

### 演 2 · 导数（分段点与隐函数）· 第 2 章

$$
\begin{gathered}
(1) f(x)=x^{2} \sin\left(\frac{1}{x}\right)(x=0), f(0)=0 \; \text{，求} \; \text{f′(0)} \\
\text{定义：} \; f'(0)=\lim_{x \to 0}\frac{x^{2} \sin\left(\frac{1}{x}\right)- 0}{x}= \lim x \sin\left(\frac{1}{x}\right)= 0 \; \text{（有界} \; \times \; \text{无穷小）} \\
\text{但} \; x=0 \; \text{时} \; f'(x)=2x \sin\left(\frac{1}{x}\right)- \cos\left(\frac{1}{x}\right) \; \text{，} \; x \to 0 \; \text{无极限} \; \Rightarrow f' \; \text{在} \; \text{0} \; \text{不连续} \\
(2) x^{2}+ y^{2}= 1 \; \text{求} \; \text{dy/dx} \; \text{与} \; \frac{d^{2}y}{dx^{2}} \\
\text{隐函数：} \; 2x+ 2y y'= 0 \Rightarrow y'=- \frac{x}{y} \\
\text{再求导：} \; y''=- \frac{y- x y'}{y^{2}}=- \frac{y+ \frac{x^{2}}{y}}{y^{2}}=- \frac{x^{2}+y^{2}}{y^{3}}=- \frac{1}{y^{3}} \\
(3) y= x^{x} \Rightarrow \ln y= x \ln x \Rightarrow y'= y(\ln x+ 1)= x^{x}(\ln x+ 1)
\end{gathered}
$$

### 演 3 · 中值定理与极值 · 第 3 章

$$
\begin{gathered}
\text{题：证明} \; f(x)=x^{3}- 3x \; \text{在} \; \text{[0,1]} \; \text{上满足拉格朗日定理，并求} \; \xi \; \text{。} \\
\text{(1)} \; \text{验证：多项式在} \; \text{[0,1]} \; \text{连续、} \; \text{(0,1)} \; \text{可导} \; \checkmark \\
(2) f(1)=- 2, f(0)=0 \Rightarrow \frac{f(1)- f(0)}{1- 0}=- 2 \\
(3) f'(x)=3x^{2}- 3=- 2 \Rightarrow 3x^{2}=1 \Rightarrow x=\frac{1}{\sqrt{3}} \in(0,1) \checkmark \Rightarrow \xi=\frac{1}{\sqrt{3}} \\
\text{题：求} \; f(x)=x^{3}- 3x^{2}+1 \; \text{的单调区间、极值与拐点。} \\
(1) f'=3x^{2}- 6x=3x(x- 2) \; \text{，驻点} \; \text{x=0,2} \\
\text{(2)} \; \text{区间：} \; (- \infty,0) f'>0 \; \text{增；} \; \text{(0,2) f′<0} \; \text{减；} \; (2,+ \infty) f'>0 \; \text{增} \\
\text{(3)} \; \text{极大} \; \text{f(0)=1} \; \text{，极小} \; f(2)=8- 12+1=- 3 \\
(4) f''=6x- 6=0 \Rightarrow x=1 \; \text{；两侧} \; \text{f''} \; \text{变号} \; \Rightarrow \; \text{拐点} \; (1, 1- 3+1)=(1,- 1)
\end{gathered}
$$

### 演 4 · 不定积分（分部与换元）· 第 4 章

$$
\begin{gathered}
(1) \int x e^{x} dx \; \text{：} \; u=x \Rightarrow \int x e^{x}dx= x e^{x}- \int e^{x}dx=(x- 1)e^{x}+ C \\
\text{验算：} \; [(x- 1)e^{x}]'= e^{x}+(x- 1)e^{x}= x e^{x} \checkmark \\
(2) \int \ln x dx= x \ln x- \int x \cdot\left(\frac{1}{x}\right)dx= x \ln x- x+ C \\
(3) \int \frac{dx}{x^{2}+4}=\left(\frac{1}{2}\right)\arctan\left(\frac{x}{2}\right)+ C \\
(4) \int \sqrt{1- x^{2}} dx \; \text{：令} \; x=\sin t \Rightarrow \int \cos^{2}t dt= \frac{t}{2}+ \frac{\sin 2t}{4}+ C \\
\text{回代：} \; = \frac{1}{2} \arcsin x+ \frac{1}{2} x\sqrt{1- x^{2}}+ C
\end{gathered}
$$

### 演 5 · 定积分与反常积分 · 第 5 章

$$
\begin{gathered}
(1)\; \int_{0}^{\frac{\pi}{2}}\sin^{2}x\,dx=\int_{0}^{\frac{\pi}{2}}\dfrac{1-\cos 2x}{2}\,dx \\
=[\frac{x}{2}- \frac{\sin 2x}{4}]_{0}^{\frac{\pi}{2}}= \frac{\pi}{4} \approx 0.785398 \\
(2) \int_{0}^{1} x e^{x} dx=[(x- 1)e^{x}]_{0}^{1}= 0-(- 1)= 1 \\
(3) \int_{0}^\pi x \sin x dx \; \text{：区间再现} \; \Rightarrow I=\left(\frac{\pi}{2}\right) \int_{0}^\pi \sin x dx=\left(\frac{\pi}{2}\right) \cdot 2= \pi \\
\text{(4)} \; \text{判敛：} \; \int_{1}^\infty \frac{dx}{x^{p}} \; \text{收敛} \; \Leftrightarrow p>1 \; \text{；} \; \int_{0}^{1}\dfrac{dx}{x^{p}} \; \text{收敛} \; \Leftrightarrow p<1 \\
(5) \int_{0}^\infty e^{- x^{2}}dx= \frac{\sqrt{\pi}}{2} \; \text{：设} \; \text{I} \; \text{，} \; I^{2}= \int \int e^{-(x^{2}+y^{2})}dxdy \; \text{（第一象限）} \\
= \int_{0}^{\frac{\pi}{2}}d\theta \int_{0}^\infty e^{- r^{2}}r dr=\left(\frac{\pi}{2}\right) \cdot\left(\frac{1}{2}\right)= \frac{\pi}{4} \Rightarrow I=\frac{\sqrt{\pi}}{2}
\end{gathered}
$$

### 演 6 · 定积分应用（微元法）· 第 6 章

$$
\begin{gathered}
\text{题：} \; y=x^{2}(0 \le x \le 1) \; \text{绕} \; \text{x} \; \text{轴旋转体体积与旋转曲面面积。} \\
\text{(1)} \; \text{体积微元} \; dV= \pi y^{2} dx= \pi x^{4} dx \Rightarrow V= \pi \int_{0}^{1}x^{4}dx= \frac{\pi}{5} \approx 0.628319 \\
\text{(2)} \; \text{曲面面积} \; S= 2\pi \int_{0}^{1} y\sqrt{1+y'^{2}}dx= 2\pi \int_{0}^{1} x^{2}\sqrt{1+4x^{2}}dx \\
\text{(3)} \; \text{题：} \; y=\sin x(0 \le x \le \pi) \; \text{与} \; \text{x} \; \text{轴面积} \; A= \int_{0}^\pi \sin x dx=[- \cos x]_{0}^\pi= 2 \\
\text{(4)} \; \text{题：星形线} \; x=a \cos^{3}t, y=a \sin^{3}t \; \text{全长} \\
ds= \sqrt{\dot{x}^{2}+\dot{y}^{2}}dt= 3a|\sin t \cos t|dt \\
\text{第一象限} \; \int_{0}^{\frac{\pi}{2}}3a \sin t \cos t dt= \frac{3a}{2} \Rightarrow \; \text{全长} \; 4 \times\left(\frac{3a}{2}\right)=6a
\end{gathered}
$$

### 演 7 · 微分方程 · 第 7 章

$$
\begin{gathered}
(1) y'+2y=e^{x} \Rightarrow(e^{2x}y)'=e^{3x} \Rightarrow e^{2x}y= \frac{1}{3} e^{3x}+C \Rightarrow y= \frac{1}{3} e^{x}+Ce^{- 2x} \\
(2) y''- 3y'+2y=0 \Rightarrow r^{2}- 3r+2=0 \Rightarrow r=1,2 \Rightarrow y=C_{1}e^{x}+C_{2}e^{2x} \\
(3) y''+4y=\sin x \; \text{：齐次解} \; C_{1}\cos 2x+C_{2}\sin 2x \; \text{；设} \; y*=A \sin x \\
\Rightarrow- A+4A=1 \Rightarrow A=\frac{1}{3} \Rightarrow y=C_{1}\cos 2x+C_{2}\sin 2x+\left(\frac{1}{3}\right)\sin x \\
\text{(4)} \; \text{共振情形} \; y''+4y=\sin 2x \; \text{须设} \; \text{y*=x(A cos2x+B sin2x)} \; \text{（不可漏} \; \text{x} \; \text{）} \\
\text{(5)} \; \text{欧拉方程} \; x^{2}y''+xy'- y=0 \; \text{：设} \; y=x^{k} \Rightarrow k(k- 1)+k- 1=k^{2}- 1=0 \Rightarrow k=±1 \\
\Rightarrow y=C_{1}x+\frac{C_{2}}{x}
\end{gathered}
$$

### 演 8 · 空间解析几何 · 第 8 章

```text
① a=(1,2,−1), b=(3,0,2)：a·b=1；a×b=(4,−5,−6)；|a|=√6
② 求过 P(1,2,3) 且法向量 n=(2,−1,1) 的平面：
   2(x−1)−(y−2)+(z−3)=0 ⇒ 2x−y+z−3=0
③ 点 (0,0,0) 到平面 2x−y+2z−3=0 的距离：|−3|/√(4+1+4)=3/3=1
④ 直线 L: (x−1)/2 = (y+1)/(−1) = z/3，方向 s=(2,−1,3)，过点 (1,−1,0)
   与平面 x+y+z=1 的夹角：sinθ=|s·n|/(|s||n|)
   = |2−1+3|/(√14·√3)=4/√42 ⇒ θ=arcsin(4/√42)
```

### 演 9 · 多元微分与极值 · 第 9 章

$$
\begin{gathered}
(1) f=x^{2}y+\sin(xy) \; \text{：} \; f_{x}=2xy+y \cos(xy) \; \text{，} \; f_{y}=x^{2}+x \cos(xy) \\
\text{在} \; \text{(0,1)} \; \text{：} \; \nabla f=(1,0) \; \text{；沿} \; e=\left(\frac{1}{\sqrt{2}},\frac{1}{\sqrt{2}}\right) \; \text{的方向导数} \; = \frac{1}{\sqrt{2}} \approx 0.707107 \\
\text{(2)} \; \text{曲面} \; z=x^{2}+y^{2} \; \text{在} \; \text{(1,1,2)} \; \text{：令} \; F=x^{2}+y^{2}- z \; \text{，} \; \nabla F=(2x,2y,- 1)=(2,2,- 1) \\
\text{切平面} \; 2(x- 1)+2(y- 1)-(z- 2)=0 \Rightarrow 2x+2y- z- 2=0 \\
\text{(3)} \; \text{无条件极值} \; f=x^{2}+y^{2} \; \text{：} \; A=C=2,B=0 \Rightarrow \Delta=4>0 \; \text{且} \; A>0 \Rightarrow(0,0) \; \text{极小} \; \text{0} \\
\text{f=xy} \; \text{：} \; \Delta=- 1<0 \Rightarrow(0,0) \; \text{是鞍点} \\
\text{(4)} \; \text{条件极值} \; \min x^{2}+y^{2} s.t. x+y=1 \; \text{：} \\
L=x^{2}+y^{2}- \lambda(x+y- 1) \; \text{，} \; 2x=\lambda, 2y=\lambda \Rightarrow x=y=\frac{1}{2} \Rightarrow f_{\min}=\frac{1}{2}
\end{gathered}
$$

### 演 10 · 重积分 · 第 10 章

$$
\begin{gathered}
\text{(1)} \; \text{换序：} \; \int_{0}^{1}dx \int_{x}^{1} f dy \; \text{（区域} \; 0 \le x \le y \le 1 \; \text{）} \; \Rightarrow \int_{0}^{1}dy \int_{0}^{y} f dx \\
(2) \iint _{D} e^{- y^{2}}dxdy \; \text{，} \; D: 0 \le x \le y \le 1 \\
= \int_{0}^{1}dy \int_{0}^{y} e^{- y^{2}}dx= \int_{0}^{1} y e^{- y^{2}}dy= \frac{1}{2}(1- e^{-1}) \approx 0.31606 \\
(3) \iint _{x^{2}+y^{2} \le a^{2}} e^{-(x^{2}+y^{2})}dxdy= 2\pi \int_{0}^{a} r e^{- r^{2}}dr= \pi(1- e^{- a^{2}}) \\
a=1 \Rightarrow \approx 1.985865 \\
\text{(4)} \; \iiint_{\text{上半球}} z\,dV=\int_{0}^{2\pi}\!d\theta\int_{0}^{\pi/2}\!\sin\phi\cos\phi\,d\phi\int_{0}^{1}\!\rho^{3}d\rho \\
= 2\pi \cdot\left(\frac{1}{2}\right) \cdot\left(\frac{1}{4}\right)= \frac{\pi}{4} \approx 0.785398 \\
\text{(5) 单位球} \; \iiint_{\Omega} 1\,dV=\dfrac{4\pi}{3}\approx 4.188790
\end{gathered}
$$

### 演 11 · 曲线曲面积分与三大公式 · 第 11 章

$$
\begin{gathered}
\text{(1)} \; \text{单位圆} \; \text{L} \; \text{（逆时针）：} \; \oint _{L} x dy- y dx \\
\text{参数} \; x=\cos t, y=\sin t \Rightarrow x dy- y dx= \cos^{2}t dt+ \sin^{2}t dt= dt \\
\Rightarrow \; \text{积分} \; = \int_{0}^{2\pi}dt= 2\pi \; \text{（} \; = 2 \cdot Area \; \text{，格林公式验证：} \; \iint _{D} 2 dxdy= 2\pi \; \text{）} \\
\text{(2)} \; \text{奇点陷阱：} \; \oint_{L}\dfrac{x\,dy-y\,dx}{x^{2}+y^{2}} \\
\frac{\partial Q}{\partial x}- \frac{\partial P}{\partial y}= 0 \; \text{但原点为奇点} \; \Rightarrow \; \text{不能直接得} \; \text{0} \\
\text{挖去半径} \; \epsilon \; \text{小圆后由格林} \; \Rightarrow \; \text{等于小圆积分} \; = 2\pi \\
\text{(3)} \; \text{高斯：} \; \oiint _{S} x dydz+y dzdx+z dxdy= \iiint _\Omega 3 dV \; \text{，单位球} \; \Rightarrow 3 \cdot\left(\frac{4\pi}{3}\right)=4\pi \\
\text{(4) div(x,y,z)=3} \; \text{；} \; rot(- y,x,0)=(0,0,2) \\
\text{(5)} \; \text{判路径无关：} \; P=2xy, Q=x^{2} \Rightarrow \frac{\partial P}{\partial y}=2x= \frac{\partial Q}{\partial x} \Rightarrow \; \text{与路径无关} \\
\text{原函数} \; u= \int Pdx= x^{2}y+\phi(y) \; \text{，由} \; u_{y}=x^{2}+\phi '=Q \Rightarrow \phi '=0 \Rightarrow u=x^{2}y+C
\end{gathered}
$$

### 演 12 · 级数 · 第 12 章

$$
\begin{gathered}
\text{(1)} \; \text{判敛} \; \sum \frac{n}{2^{n}} \; \text{：比值} \; \rho=\lim \frac{\frac{n+1}{2^{n+1}}}{\frac{n}{2^{n}}}= \frac{1}{2}< 1 \Rightarrow \; \text{收敛} \\
\text{(2)} \; \text{判敛} \; \sum \frac{1}{n^{2}} \; \text{：} \; p=2>1 \Rightarrow \; \text{收敛；} \; \sum\frac{1}{n} \; \text{：} \; p=1 \Rightarrow \; \text{发散} \\
\text{(3)} \; \text{收敛半径} \; \sum \frac{x^{n}}{n} \; \text{：} \; R=\lim|\frac{a_{n}}{a_{n+1}}|= \lim \frac{n+1}{n}= 1 \\
\text{端点} \; x=1 \Rightarrow \sum\frac{1}{n} \; \text{发散；} \; x=- 1 \Rightarrow \sum\frac{(-1)^{n}}{n} \; \text{收敛} \; \Rightarrow \; \text{收敛域} \; \text{[−1,1)} \\
\text{(4)} \; \text{和函数} \; \sum_{n=1}^\infty n x^{n} \; \text{：由} \; \sum x^{n}=\frac{1}{1- x} \; \text{逐项求导乘} \; \text{x} \\
\Rightarrow \frac{x}{(1- x)^{2}} \; \text{（} \; \text{|x|<1} \; \text{）；验算} \; x=\frac{1}{2} \Rightarrow 2 \\
(5) \sum\frac{1}{n(n+1)}= \sum\left(\frac{1}{n}- \frac{1}{n+1}\right)= 1- \lim \frac{1}{N+1}= 1 \\
(6) \sum\frac{(-1)^{n+1}}{n}= \ln 2 \; \text{（条件收敛）；} \; \sum\frac{(-1)^{n+1}}{n^{2}}= \frac{\pi^{2}}{12} \; \text{（绝对收敛）}
\end{gathered}
$$

---

## 图形读图专题：18 张图怎么画、怎么读

| 图 | 必画元素 | 读图要点（最常被问的一句） |
| --- | --- | --- |
| `math-overview` | 12 章分四段与主线条 | 一元微分 → 一元积分 → 方程与空间 → 多元 → 级数，顺序不可颠倒 |
| `math-function` | 五类基本初等函数与四性质 | 反函数存在要求一一对应；奇偶性先看定义域 |
| `math-limit` | ε–δ 邻域、两个重要极限曲线 | 定义是「去心」邻域；$f(x_{0})$ 与极限无关 |
| `math-taylor` | 两种余项、五个展开 | 佩亚诺用于局部求极限，拉格朗日用于整体误差估计 |
| `math-derivative` | 割线趋切线、Δy 与 dy | 可导 ⇔ 可微 ⇒ 连续，反向不成立 |
| `math-mvt` | 弦与平行切线、罗尔水平切线 | 拉格朗日 = 弦斜率等于某点切线斜率 |
| `math-application` | f′/f″ 符号表、三类渐近线 | 拐点要写坐标；水平/斜渐近线分 ±∞ 求 |
| `math-integral` | 三类积分法流程 | 分部取 u 按「反对幂指三」；第二换元须回代 |
| `math-definite` | 黎曼和矩形、曲边梯形 | 微积分基本定理把「和的极限」化为「原函数增量」 |
| `math-app-integration` | 微元条带、旋转体 | 微元可加是前提；面积要加绝对值 |
| `math-ode` | 分类决策树 | 先判阶数与线性，再判齐次/可分离；共振要乘 $x^{k}$ |
| `math-vector` | 三种积、平面法向量、直线方向 | 直线一般式的方向是两法向量的叉积 |
| `math-surface` | 二次曲面截痕 | 缺变量是柱面；负号个数决定单/双叶 |
| `math-multivariable` | 关系链、梯度与等值线 | 偏导存在 ⇏  连续、⇏  可微（与一元不同） |
| `math-extremum` | $\Delta=AC- B^{2}$ 判别、约束曲线 | 梯度与约束梯度平行即拉格朗日条件 |
| `math-multiple-integral` | X/Y 型区域、极/球坐标 | 换序三步；球坐标 $dV=\rho^{2}\sin \phi d\rho d\phi d\theta$ |
| `math-field` | 闭曲线/闭曲面与定向 | 三大公式 = 边界积分 = 内部导数积分；奇点必须挖洞 |
| `math-series` | 判敛决策树 | 先看通项是否趋于 0，再按正项/交错选判别法 |

::: tip 手绘 Check（考场上 3 分钟画一张合格图）
① 标坐标轴名称与原点；② 曲线标函数式或字母；③ 关键点（交点、驻点、分界点）标坐标或虚线投影；④ 面积题打阴影并写出积分式；⑤ 方向题（闭曲线、曲面侧）画箭头；⑥ 分段函数用实线/空心点区分是否取到。缺任一项都可能被扣分。
:::

---

## 各章高频题型与解题套路

> 按 12 章列出「见到题目 → 识别类型 → 标准动作」，是考前快速检索用的操作手册。

### 第 1 章 · 函数极限连续

| 题型 | 标准动作 |
| --- | --- |
| 求 $\dfrac{0}{0}$ 极限 | 先试等价无穷小（仅乘除）→ 加减结构或主阶抵消直接上泰勒 → 最后才洛必达 |
| 求 $1^\infty$ 极限 | 凑 $(1+\alpha)^{\dfrac{1}{\alpha}}$ 或取对数；速算 $e^{\lim g(f- 1)}$ |
| 递推数列极限 | 证有界（归纳）+ 证单调（作差/作商）⇒ 设极限 A 解 `A=f(A)`，注意验证 A 的合理性 |
| n 项和极限 | 夹逼准则（放缩）或定积分定义 $\lim\left(\dfrac{1}{n}\right)\sum f\left(\dfrac{k}{n}\right)= \int_{0}^{1}f dx$ |
| 无穷小阶的比较 | 求 $\lim \dfrac{\alpha}{\beta}$：为 0 则 α 高阶、∞ 则低阶、常数 c≠0 则同阶、1 则等价 |
| 间断点分类 | 找所有可疑点（分母为 0、分段点、无定义点）→ 逐点算左右极限 → 归类 |
| 含参数的分段函数 | 由连续/可导条件列方程（连续：左右极限 = 函数值；可导：左右导数相等）求参数 |
| 证明方程有根 | 构造 $F(x)=f(x)- x$ 或原函数，用零点定理；唯一性再用单调性 |

### 第 2 章 · 导数与微分

| 题型 | 标准动作 |
| --- | --- |
| 用定义求导 | 写差商 → 代入 → 化简（有理化、等价无穷小）→ 取极限；分段点必用定义 |
| 复合/隐函数/参数求导 | 画变量关系图；隐函数两边对 x 求导把 y 视为 x 的函数；参数方程二阶导先对 t |
| 幂指函数 $u(x)^{v(x)}$ | 取对数或化为 $e^{v \ln u}$ |
| 高阶导数 / 求 $f^{(n)}(0)$ | 莱布尼茨公式、已知展开式系数、或递推 |
| 导数几何应用 | 切线 $y- f(x_{0})=f'(x_{0})(x- x_{0})$，法线斜率 $- \dfrac{1}{f}'$；注意 $f'=0$ 时法线竖直 |
| 含绝对值的可导性 | $g(x)\vert x- a\vert $ 在 $a$ 可导 $\Leftrightarrow g(a)=0$ |

### 第 3 章 · 中值定理与导数应用

| 题型 | 标准动作 |
| --- | --- |
| 证 $\exists \xi : F'(\xi)=0$ | 构造 F → 验证罗尔三条件 → 结论（写清 ξ 在开区间） |
| 证含两个中值 $\xi,\eta$ | 分别对两个函数用拉格朗日，或对同一函数在不同区间用中值定理 |
| 证不等式 | ① 移项构造 `F(x)` 证 `F′>0` 且 $F(a) \ge 0$；② 拉格朗日中值定理放缩；③ 泰勒展开 + 余项符号；④ 凹凸性（琴生不等式） |
| 讨论方程根的个数 | 求单调区间与极值 → 结合端点符号与零点定理分区间计数 |
| 求渐近线 | 无定义点查铅直；$± \infty$ 分别求水平；若无水平再求斜 |
| 最值应用题 | 设变量 → 建立目标函数 → 求导找唯一驻点 → 说明实际最值存在即得结论 |

### 第 4 章 · 不定积分

| 题型 | 标准动作 |
| --- | --- |
| 有理函数积分 | 多项式除法 → 分母因式分解 → 待定系数拆部分分式 → 逐项积分 |
| 三角有理式 | 先看能否用倍角/降幂/凑微分；否则万能代换 |
| 分部积分循环型 | 两次分部后出现原积分 ⇒ 移项解方程，`+C` 最后补 |
| 含 `|x|` / 分段被积函数 | 分段积分，再由原函数连续性统一各段常数 |
| 抽象函数积分 | 用凑微分与分部把 $\int f'(x)g(x)dx$ 转化为已知条件 |

### 第 5 章 · 定积分与反常积分

| 题型 | 标准动作 |
| --- | --- |
| 定积分计算 | 先查奇偶/周期/区间再现化简 → 再换元或分部 → 换元时**同步改上下限** |
| 变限函数极限 | 洛必达 + 变限求导通式；含参数先换元 |
| 积分等式证明 | 换元 $t=a+b- x$、分部、或构造辅助函数用罗尔 |
| 积分不等式 | 保号性、比较性、估值定理、柯西–施瓦茨 $\left(\int fg\right)^2 \le \int f^2 \int g^2$ |
| 反常积分计算与判敛 | 分段取极限；判敛用 p 判别 / 极限比较；瑕点在内部必须拆 |
| 定积分定义求极限 | 凑成 $\lim\left(\dfrac{1}{n}\right)\sum f\left(\dfrac{k}{n}\right)$ 识别为 $\int_{0}^{1} f(x)dx$ |

### 第 6 章 · 定积分应用

| 题型 | 标准动作 |
| --- | --- |
| 面积 | 画图求交点 → 判断上下曲线 → 分段加绝对值 → 积分；极坐标用 $\dfrac{1}{2} \int r^{2}d\theta$ |
| 旋转体体积 | 绕 x 用圆盘 $\pi \int f^{2}dx$；绕 y 用柱壳 $2\pi \int x f dx$ 或反函数圆盘 |
| 弧长 | 三种形式按已知选（直角 / 参数 / 极坐标） |
| 物理应用 | 建坐标系 → 写微元（注意深度、力臂）→ 定限 → 积分 |

### 第 7 章 · 常微分方程

| 题型 | 标准动作 |
| --- | --- |
| 一阶方程 | 按可分离 → 齐次 → 线性 → 伯努利 → 全微分的顺序判别；齐次常需先作平移 `x=X+h, y=Y+k` |
| 可降阶 | 判断缺 y 还是缺 x，选择令 $p=y'$ 后把 $y''$ 写成 $p'$ 或 $p\dfrac{dp}{dy}$ |
| 二阶常系数 | 特征方程 → 齐次通解 → 按右端形式设特解（共振乘 $x^{k}$） |
| 由解反求方程 | 由解的结构反推特征根，或用 `y″+py′+qy=0` 待定 p,q |
| 变限积分方程 | 两边求导化为 ODE，并从**原方程**提取初始条件 |
| 应用题 | 由变化率/几何条件列方程（如「切线斜率」「冷却速率」），再定初值 |

### 第 8 章 · 空间解析几何

| 题型 | 标准动作 |
| --- | --- |
| 求平面方程 | 找一点 + 法向量（叉积或已知垂直条件）；平面束处理「过交线」 |
| 求直线方程 | 找一点 + 方向向量（叉积/平行/两点差）；一般式要化为对称式 |
| 距离与夹角 | 直接用公式，注意线面夹角用 `sin` |
| 投影 | 消去对应变量得投影柱面，再与坐标面方程联立 |
| 旋转曲面 | 按绕哪个轴替换对应变量，注意 $\pm\sqrt{\cdot}$ 与定义域 |

### 第 9 章 · 多元微分

| 题型 | 标准动作 |
| --- | --- |
| 判二重极限不存在 | 沿 `y=kx`（得依赖 k 的值）或沿 $y=x$ 与 $y=x^{2}$ 得不同值 |
| 求偏导 / 全微分 | 固定其余变量；抽象复合函数先画变量图再写链式 |
| 判可微性 | 偏导连续 ⇒ 可微（最常用）；否则回定义算 $\dfrac{\lim[\Delta z- f_{x}\Delta x- f_{y}\Delta y]}{\rho}$ |
| 方向导数 / 梯度 | 可微时用 $\nabla f \cdot e_{l}$；单位化方向向量别忘 |
| 切平面 / 法线 | $\nabla F$ 作法向量；参数曲线用 `r′(t)` |
| 极值 / 最值 | 驻点 → $\Delta=AC- B^{2}$ 判别 → 闭区域再查边界；条件极值用拉格朗日 |
| 抽象函数方程 | 由给定的全微分或偏导关系，用变量代换化为 PDE 再积分 |

### 第 10 章 · 重积分

| 题型 | 标准动作 |
| --- | --- |
| 化累次积分 / 换序 | 写不等式 → 画图 → 穿线法重写 → 非简单型分块 |
| 极坐标 | 区域含圆、被积含 $x^{2}+y^{2}$ ⇒ 换极坐标，写清 $\theta$ 与 `r` 范围 |
| 三重积分 | 含 $x^{2}+y^{2}$ 用柱；含 $x^{2}+y^{2}+z^{2}$ 用球；先一后二 / 先二后一按截面选 |
| 对称性 | 奇偶性 → 轮换对称 → 区域可加，先化简 |
| 含绝对值 / max,min | 按分界线把区域切开分别积分 |
| 曲面面积 / 质心 | 用 $\sqrt{1+z_{x}^{2}+z_{y}^{2}}$ 与 $\iint x\rho \dfrac{d\sigma}{M}$ 等公式 |

### 第 11 章 · 线面积分与场论

| 题型 | 标准动作 |
| --- | --- |
| 第一类线积分 | 参数化 + `ds`；利用对称性；上下限小到大 |
| 第二类线积分 | 参数化直接代入（最稳）或格林（闭曲线）/ 补线 / 判路径无关 |
| 路径无关求积分 | 验证 $P_{y}=Q_{x}$ → 选折线路径求原函数 `u` → `u(终点)−u(起点)` |
| 第二类面积分 | 合一投影法或逐面投影；先定侧 |
| 高斯 / 斯托克斯 | 检查闭性与连续性；有奇点挖洞；非闭补面后减去 |
| 散度 / 旋度 / 通量 | 直接按定义求偏导，注意 $\nabla \cdot( \nabla \times A)=0$ 可秒判 |

### 第 12 章 · 无穷级数

| 题型 | 标准动作 |
| --- | --- |
| 判正项级数敛散 | 等价无穷小找主阶 → 与 $\dfrac{1}{n^{p}}$ 极限比较；阶乘/指数用比值；`n` 次幂用根值 |
| 判交错 / 一般项 | 莱布尼茨判收敛；再判 $\sum\vert u_{n}\vert $ 得绝对或条件收敛 |
| 求收敛半径 / 域 | 比值或根值求 R，$x=x_{0}±R$ 两端点单独判 |
| 求和函数 | 逐项求导/积分化为几何级数 → 求和 → 逆运算还原 → 定常数 → 讨论端点 |
| 展开为幂级数 | 用五个基本展开 + 四则/复合/逐项积分；记住收敛域可能缩小 |
| 傅里叶展开 | 先判奇偶 → 算 $a_{n},b_{n}$（用正交性）→ 写级数 → 用狄利克雷说明收敛值 |
| 求数项级数和 | 构造幂级数取特定 x；或由傅里叶级数在特殊点代入 |

---

## 重要公式推导补遗

> 教材多以「给出公式」为主，这里补上几个最常被追问「为什么」的推导要点。

### 推 1 · 华里士公式的递推

设 $I_{n}= \int_{0}^{\dfrac{\pi}{2}} \sin^{n}x dx$。分部取 $u=\sin^{n- 1}x, dv=\sin x dx$：

$$I_{n}=[- \sin^{n- 1}x \cos x]_{0}^{\frac{\pi}{2}}+(n- 1) \int_{0}^{\frac{\pi}{2}} \sin^{n- 2}x \cos^{2}x dx$$

$$=(n- 1) \int \sin^{n- 2}x(1- \sin^{2}x)dx=(n- 1)(I_{n-2}- I_{n})$$

⇒ $n I_{n}=(n- 1)I_{n-2}$ ⇒ $I_{n}= \dfrac{n- 1}{n} \cdot I_{n-2}$。
由 $I_{0}=\dfrac{\pi}{2}$、$I_{1}=1$ 递推得偶/奇两套结果；令 `n=2` 得 $I_{2}= \dfrac{1}{2}\cdot\dfrac{\pi}{2}= \dfrac{\pi}{4}$ ✓。

### 推 2 · 泊松积分与 $\Gamma\left(\dfrac{1}{2}\right)$

由综 3：$I^2=\iint_{\text{第一象限}} e^{-(x^2+y^2)}dxdy=\dfrac{\pi}{2}\int_0^{\infty}e^{-r^2}2r\cdot\dfrac{1}{2}dr=\dfrac{\pi}{4}$ ⇒ $I=\dfrac{\sqrt{\pi}}{2}$。
换元 $t=x^{2}$：$\Gamma\left(\dfrac{1}{2}\right)= \int_{0}^\infty t^{- \dfrac{1}{2}}e^{- t}dt= 2 \int_{0}^\infty e^{- x^{2}}dx= \sqrt{\pi}$；
由 $\Gamma(s+1)=s\Gamma(s)$ 得 $\Gamma(n+1)=n!$、$\Gamma\left(\dfrac{3}{2}\right)=\dfrac{\sqrt{\pi}}{2}$，故 Γ 是阶乘的连续延拓。

### 推 3 · 牛顿–莱布尼茨 ⇒ 格林 ⇒ 高斯（同一思想）

$$
\begin{gathered}
\text{一维：} \; \int_{a}^{b} F'(x)dx= F(b)- F(a) \; \text{（区间内部导数的积分} \; \text{=} \; \text{边界上的值）} \\
\text{二维：} \; \iint _{D}(Q_{x}- P_{y})dxdy= \oint _{\partial D} Pdx+Qdy \; \text{（内部旋度} \; \text{=} \; \text{边界环流）} \\
\text{三维：} \; \iiint _\Omega div A dV= \oiint _{\partial \Omega} A \cdot n dS \; \text{（内部散度} \; \text{=} \; \text{边界通量）} \\
\text{三者都是「把内部相邻微元的贡献相互抵消，只剩边界」：} \\
\text{分割区域后，相邻小区域的公共边界上方向相反、积分抵消。}
\end{gathered}
$$
**推论**：取 $P=- \dfrac{y}{2}, Q=\dfrac{x}{2}$ ⇒ $Q_{x}- P_{y}=1$ ⇒ $Area(D)= \dfrac{1}{2} \oint (x dy- y dx)$（格林求面积公式）。

### 推 4 · 一阶线性方程的积分因子

$y'+P(x)y=Q(x)$。设存在 $\mu(x)$ 使 $(\mu y)'=\mu Q$，展开 $\mu y'+\mu 'y=\mu Q$ 对比得 $\mu '=\mu P$ ⇒ $\mu=e^{\int P dx}$。
于是 $(\mu y)'=\mu Q \Rightarrow \mu y= \int \mu Q dx+ C$，即通解公式。这套「乘积分因子」也是综 2 中辅助函数构造的来源。

### 推 5 · 幂级数求和函数的通法

$$
\begin{gathered}
\text{求} \; S(x)=\sum_{n=1}^\infty n x^{n} \; \text{：} \\
\frac{S(x)}{x}= \sum n x^{n- 1}=\left(\sum x^{n}\right)'=[\frac{1}{1- x}- 1]'= \frac{1}{(1- x)^{2}} \\
\Rightarrow S(x)= \frac{x}{(1- x)^{2}} \; \text{，} \; \text{|x|<1} \\
\text{求} \; S(x)=\sum \frac{x^{n}}{n} \; \text{：} \\
S'(x)=\sum x^{n- 1}=\frac{1}{1- x} \Rightarrow S(x)=- \ln(1- x)+C \; \text{；由} \; S(0)=0 \Rightarrow C=0
\end{gathered}
$$
关键：**逐项求导把系数 `n` 消掉、逐项积分把分母 `n` 补上**，最后务必用 `S(0)` 定常数并单独检验端点。

### 推 6 · 傅里叶系数公式来自正交性

三角函数系 `{1, cos nx, sin nx}` 在 $[- \pi,\pi]$ 上正交：
$\int_{- \pi}^{\pi} \cos mx \cos nx dx= \pi \delta_{mn}$（$m,n \ge 1$），$\int \sin mx \sin nx dx= \pi \delta_{mn}$，$\int \sin mx \cos nx dx= 0$，$\int_{- \pi}^{\pi}1 dx= 2\pi$。
两边同乘 `cos nx` 并在 $[- \pi,\pi]$ 上逐项积分，除第 n 项外全为 0 ⇒ $a_{n}=\left(\dfrac{1}{\pi}\right) \int f \cos nx dx$；常数为 $\dfrac{a_{0}}{2}$ 正是为统一系数形式。

### 推 7 · 二元极值充分条件来自泰勒

在驻点 $(x_{0},y_{0})$ 处 $f_{x}=f_{y}=0$，二阶泰勒：
$\Delta f \approx \dfrac{1}{2}(A h^{2}+ 2B hk+ C k^{2})$，这是关于 `(h,k)` 的二次型。
其正定 ⇔ `A>0` 且 $AC- B^{2}>0$ ⇒ $\Delta f>0$ 恒成立 ⇒ 极小；负定 ⇔ `A<0` 且 $\Delta>0$ ⇒ 极大；$\Delta<0$ 时二次型不定 ⇒ 沿不同方向符号相反 ⇒ 鞍点。$\Delta=0$ 时二次项不足以判定，需更高阶。

### 推 8 · 欧拉公式 $e^{ix}= \cos x+ i \sin x$

把 $e^z= \sum \dfrac{z^{n}}{n}!$ 中令 `z=ix`，按偶次/奇次分组：

$$e^{ix}=[1- \frac{x^{2}}{2}!+ \frac{x^{4}}{4}!- \cdots]+ i[x- \frac{x^{3}}{3}!+ \frac{x^{5}}{5}!- \cdots]= \cos x+ i \sin x$$

取 $x=\pi$ 得 $e^{i\pi}+1=0$；由此复数可写 $z=re^{i\theta}$，是常系数方程复根解 $e^{\alpha x}(C_{1}\cos \beta x+C_{2}\sin \beta x)$ 的来源。

---

## 综合例题精讲（跨章）

### 综 1 · 极限 → 导数 → 泰勒（第 1–3 章）

题：设 $f(x)$ 在 $x=0$ 二阶可导，$\lim_{x \to 0}[\dfrac{f(x)}{x}+ \sin \dfrac{x}{x^{2}}]= 1$，求 $f(0)$、$f'(0)$，并讨论 $f''(0)$ 能否确定。

$$
\begin{gathered}
\text{(1)} \; \text{通分：} \; \lim \frac{x f(x)+ \sin x}{x^{2}}= 1 \; \text{（有限）} \; \Rightarrow \; \text{分子必须为} \; O(x^{2}) \\
\text{(2)} \; \text{若} \; f(0)=0 \; \text{，则} \; \text{x f(x) ~ f(0)x} \; \text{而} \; \sin x \sim x \Rightarrow \; \text{分子} \; \text{~ (f(0)+1)x} \\
\text{要使其为} \; O(x^{2}) \; \text{必须} \; f(0)=- 1 \\
\text{(3)} \; \text{泰勒：} \; f(x)=- 1+ f'(0)x+ \frac{1}{2} f''(0)x^{2}+ o(x^{2}) \; \text{，} \; \sin x= x- \frac{x^{3}}{6}+ o(x^{3}) \\
\text{分子} \; = x[- 1+ f'(0)x+ \frac{1}{2} f''(0)x^{2}+ o(x^{2})]+ x- \frac{x^{3}}{6}+ o(x^{3}) \\
= f'(0)x^{2}+[ \frac{1}{2} f''(0)- \frac{1}{6}]x^{3}+ o(x^{3}) \\
\text{(4)} \; \text{分子} \; x^{2}= f'(0)+[ \frac{1}{2} f''(0)- \frac{1}{6}]x+ o(x) \to f'(0)= 1 \\
x^{3} \; \text{项除以} \; x^{2} \; \text{后随} \; x \to 0 \; \text{消失，对极限无约束} \; \Rightarrow f''(0) \; \text{不能由该条件确定} \\
\text{结论：} \; f(0)=- 1 \; \text{，} \; \text{f′(0)=1} \; \text{，} \; \text{f''(0)} \; \text{任意（如} \; f=- 1+x \; \text{与} \; f=- 1+x+x^{2} \; \text{都满足条件）}
\end{gathered}
$$
**方法要点**：分式极限存在且分母为 $x^{m}$ ⇒ 分子低于 $x^{m}$ 阶的系数必须全为 0，$x^{m}$ 阶系数等于极限值；**高于** $x^{m}$ 阶的系数不受该极限约束。本题只「探到」二阶系数 $f'(0)$，探不到 $f''(0)$——判断条件究竟能确定几阶信息，是这类题的真正考点。

### 综 2 · 积分上限函数与微分方程（第 2、5、7 章）

题：设 `f(x)` 连续且 $f(x)= e^{x}+ \int_{0}^{x}(x- t)f(t)dt$，求 `f(x)`。

$$
\begin{gathered}
\text{(1)} \; \text{拆开：} \; f(x)= e^{x}+ x \int_{0}^{x} f(t)dt- \int_{0}^{x} t f(t)dt \\
\text{(2)} \; \text{求导：} \; f'(x)= e^{x}+ \int_{0}^{x} f(t)dt+ x f(x)- x f(x)= e^{x}+ \int_{0}^{x} f(t)dt \\
\text{(3)} \; \text{再求导：} \; f''(x)= e^{x}+ f(x) \Rightarrow f''- f= e^{x} \\
\text{(4)} \; \text{特征方程} \; r^{2}- 1=0 \Rightarrow \; \text{齐次解} \; C_{1}e^{x}+C_{2}e^{- x} \\
\lambda=1 \; \text{是单特征根} \; \Rightarrow \; \text{设特解} \; y*=A x e^{x} \; \text{，代入方程} \; y*''- y*= e^{x} \; \text{计算：} \\
y*'=A(1+x)e^{x}, y*''=A(2+x)e^{x} \Rightarrow y*''- y*= 2A e^{x}= e^{x} \Rightarrow A=\frac{1}{2} \\
(5) f(x)= C_{1}e^{x}+ C_{2}e^{- x}+ \frac{1}{2} x e^{x} \\
\text{(6)} \; \text{由原式} \; f(0)=e^{0}=1 \; \text{；由} \; (2) f'(0)=e^{0}+0=1 \\
f(0)=C_{1}+C_{2}=1 \; \text{；} \; f'=C_{1}e^{x}- C_{2}e^{- x}+ \frac{1}{2}(1+x)e^{x} \Rightarrow f'(0)=C_{1}- C_{2}+ \frac{1}{2}=1 \\
\Rightarrow C_{1}=\frac{3}{4}, C_{2}=\frac{1}{4} \\
\text{结论：} \; f(x)= \frac{3}{4} e^{x}+ \frac{1}{4} e^{- x}+ \frac{1}{2} x e^{x}
\end{gathered}
$$
**方法要点**：变限积分方程 → 求导化为微分方程 → 从原方程提取初始条件（这一步最易漏）。

### 综 3 · 二重积分 → 反常积分（第 5、10 章）

题：用二重积分计算泊松积分 $I= \int_{0}^\infty e^{- x^{2}}dx$。

$$
\begin{gathered}
\text{(1)} \; I^{2}=\left(\int_{0}^{\infty}e^{-x^{2}}dx\right)\left(\int_{0}^{\infty}e^{-y^{2}}dy\right)=\iint_{\text{第一象限}}e^{-(x^{2}+y^{2})}\,dxdy \\
\text{(2)} \; \text{化极坐标：} \; x=r \cos \theta, y=r \sin \theta, dxdy= r dr d\theta \; \text{，} \; \theta \text{∈[0,}\pi \text{/2], r∈[0,∞)} \\
(3) I^{2}= \int_{0}^{\frac{\pi}{2}}d\theta \int_{0}^\infty e^{- r^{2}} r dr=\left(\frac{\pi}{2}\right) \cdot[- \frac{1}{2} e^{- r^{2}}]_{0}^\infty=\left(\frac{\pi}{2}\right)\left(\frac{1}{2}\right)= \frac{\pi}{4} \\
(4) I= \frac{\sqrt{\pi}}{2} \approx 0.886227 \; \text{（取正根）}
\end{gathered}
$$
**推广**：$\int_{- \infty}^\infty e^{- x^{2}}dx= \sqrt{\pi}$（高斯积分，概率论正态分布归一化常数的来源）；$\Gamma\left(\dfrac{1}{2}\right)=\sqrt{\pi}$ 由此得。

### 综 4 · 曲线积分 → 级数（第 11、12 章）

题：由 $x=2\sum\dfrac{(-1)^{n+1}\sin(nx)}{n}$（$x \in(- \pi, \pi)$）导出 $\sum\dfrac{1}{(2k-1)^{2}}=\dfrac{\pi^{2}}{8}$，并说明为何取 $x=\dfrac{\pi}{2}$ 得 $\dfrac{\pi}{4}$。

$$
\begin{gathered}
\text{(1)} \; \text{傅里叶级数逐项积分（在收敛区间内合法）：} \\
\int_{0}^{x} t dt= \frac{2\sum(- 1)^{n+1}}{n} \int_{0}^{x} \sin nt dt \\
\frac{x^{2}}{2}= \frac{2\sum(- 1)^{n+1}(1- \cos nx)}{n^{2}} \\
\text{(2)} \; \text{取} \; x=\pi \; \text{：} \; \frac{\pi^{2}}{2}= 2\sum\frac{(-1)^{n+1}\left(1-(-1)^{n}\right)}{n^{2}}= 4\sum_{k \ge 1}\frac{1}{(2k- 1)^{2}} \\
\Rightarrow \sum_{k \ge 1}\frac{1}{(2k- 1)^{2}}= \frac{\pi^{2}}{8} \checkmark \\
\text{(3)} \; \text{原展开式取} \; x=\frac{\pi}{2} \; \text{：} \; \frac{\pi}{2}= 2\left(1- \frac{1}{3}+ \frac{1}{5}- \cdots\right) \Rightarrow \; \text{交错奇倒数和} \; = \frac{\pi}{4} \\
\text{(4)} \; \text{帕塞瓦尔：由} \; \text{|x|} \; \text{的余弦级数也可得} \; \sum\frac{1}{n^{2}}= \frac{\pi^{2}}{6}
\end{gathered}
$$
**方法要点**：傅里叶级数既能「求和函数」也能「求数项和」；逐项积分后收敛性变好（系数多除一个 n）。

### 综 5 · 多元极值 ↔  条件极值 ↔  经济学（第 3、9 章）

题：在 $x^{2}+y^{2}+z^{2}=1$ 下求 `f=xyz` 的最大值，并说明与微观经济学条件极值的关系。

$$
\begin{gathered}
(1) L= xyz+ \lambda(x^{2}+y^{2}+z^{2}- 1) \\
(2) \frac{\partial L}{\partial x}= yz+2\lambda x= 0 \; \text{；同理} \; xz+2\lambda y=0 \; \text{、} \; xy+2\lambda z=0 \\
\text{(3)} \; \text{若} \; xyz=0 \; \text{，三式乘} \; \text{x,y,z} \; \text{后相等} \; \Rightarrow 2\lambda x^{2}=2\lambda y^{2}=2\lambda z^{2} \Rightarrow x^{2}=y^{2}=z^{2}=\frac{1}{3} \\
(4) f_{\max}=\left(\frac{1}{\sqrt{3}}\right)^{3}= \frac{1}{3\sqrt{3}} \approx 0.19245 \; \text{（取全正或两负一正）} \\
\text{(5)} \; \text{若} \; \text{xyz=0} \; \text{则} \; \text{f=0} \; \text{，非最大} \\
\text{(6)} \; \text{经济学对应：效用} \; \text{U(X,Y)} \; \text{在预算约束} \; \text{PxX+PyY=I} \; \text{下最大化，} \\
\text{拉格朗日条件即} \; MRS= \frac{Px}{Py} \; \text{；} \; \lambda \; \text{的边际解释为「收入的边际效用」}
\end{gathered}
$$
**方法要点**：条件极值求出的只是候选点，还要比较边界/退化情形（本题 `xyz=0`）。

### 综 6 · 三大公式的选择（第 10、11 章）

题：计算 $\oiint _{\Sigma} x^{3} dydz+ y^{3} dzdx+ z^{3} dxdy$，$\sum$ 为球面 $x^{2}+y^{2}+z^{2}=R^{2}$ 外侧。

$$
\begin{gathered}
\text{(1)} \; \text{高斯公式：} \; div A= 3x^{2}+3y^{2}+3z^{2}= 3r^{2} \\
\text{(2)} \; \text{原式} \; = \iiint _\Omega 3(x^{2}+y^{2}+z^{2})dV \; \text{，用球坐标：} \\
= 3 \int_{0}^{2\pi}d\theta \int_{0}^\pi \sin \phi d\phi \int_{0}^R \rho^{2} \cdot \rho^{2} d\rho \\
= 3 \cdot 2\pi \cdot 2 \cdot \frac{R^{5}}{5}= \frac{12\pi R^{5}}{5} \\
\text{(3)} \; \text{校验} \; \text{R=1} \; \text{、取} \; \text{A=(x,y,z)} \; \text{时原式} \; = 3V= 4\pi \; \text{（与前面例题一致）} \; \checkmark
\end{gathered}
$$
**选择规则**：闭曲面且偏导连续 ⇒ 高斯；闭曲线平面 ⇒ 格林；空间闭曲线 ⇒ 斯托克斯；非闭 ⇒ 先补面/补线；有奇点 ⇒ 挖洞。

### 综 7 · 幂级数解微分方程（第 7、12 章）

题：用幂级数求 `y′=y, y(0)=1` 的解。

$$
\begin{gathered}
\text{(1)} \; \text{设} \; y= \sum_{n=0}^\infty a_{n} x^{n} \Rightarrow y'= \sum_{n=1}^\infty n a_{n} x^{n- 1} \\
\text{(2)} \; \text{代入：} \; \sum_{n=1}^\infty n a_{n} x^{n- 1}= \sum_{n=0}^\infty a_{n} x^{n} \\
\text{比较} \; x^{k} \; \text{系数：} \; (k+1)a_{k+1}= a_{k} \Rightarrow a_{k+1}= \frac{a_{k}}{k+1} \\
\text{(3)} \; \text{由} \; a_{0}= y(0)=1 \Rightarrow a_{n}= \frac{1}{n}! \\
(4) y= \sum \frac{x^{n}}{n}!= e^{x} \; \text{，收敛半径} \; R= \infty \; \text{（比值} \; |\frac{a_{n}}{a_{n+1}}|= n+1 \to \infty \; \text{）}
\end{gathered}
$$
**意义**：把微分方程化为系数的递推关系；教材第十二章「微分方程的幂级数解法」即此，也是非初等函数（贝塞尔、勒让德）的定义方式。

### 综 8 · 答题模板：证明题四步法

面对「证明存在 ξ 使……」的中值定理证明题：
① **改写**：把待证式整理成 $F'(\xi)=0$ 或 $F'(\xi)=k$，明确中值定理类型；
② **构造函数**：反推 $F$（含积分因子 $e^{g(x)}$、或 $f(x)- kx$、或两端点差的形式）；
③ **验证条件**：写出 `F` 在闭区间连续、开区间可导、端点值相等（罗尔）或直接引用拉格朗日/柯西；
④ **得出结论**：注明 $\xi \in(a,b)$ 且属于**开区间**，并检查是否要用到零点定理/介值定理先定位中间点。
凡含 $f''$、$f'''$ 的题目，考虑「对 $f'$ 用中值定理」或「两次罗尔」；含积分的题目考虑积分中值定理或变限函数。

---

## 易混概念对照

| # | 概念 A | 概念 B | 关键区别 |
| --- | --- | --- | --- |
| 1 | 函数相同 | 表达式相同 | 需定义域与对应规则都相同；`x` 与 $\dfrac{x^{2}}{x}$ 定义域不同 |
| 2 | 极限存在 | 函数在该点有定义 | 极限是「去心」邻域行为，与该点函数值无关 |
| 3 | 无穷小 | 很小的数 | 无穷小是以 0 为极限的**变量**；0 是唯一为常数的无穷小 |
| 4 | 等价无穷小替换 | 泰勒展开 | 前者只能用于乘除因子；后者可处理加减与主阶抵消 |
| 5 | 连续 | 可导 | 可导必连续；连续未必可导（`|x|`） |
| 6 | 可导 | 可微 | 一元等价；多元可微强于偏导存在 |
| 7 | 驻点 | 极值点 | 驻点是 $f'=0$；极值点也可在不可导点，驻点也可能是鞍点 |
| 8 | 极值 | 最值 | 局部 vs 全局；闭区间最值还要比较端点 |
| 9 | 拐点 | 驻点 | 拐点是 $f''$ 变号的曲线上的点（写坐标）；驻点是 $f'=0$ 的 $x$ 值 |
| 10 | 凹凸（凹/凸） | 函数凸性（优化） | 国内高数「凹=∪」与凸优化「凸=∪」命名易混，看定义 $f''$ 符号 |
| 11 | 水平渐近线 | 斜渐近线 | 同一方向二者至多各一条；$x \to+ \infty$ 与 $- \infty$ 分开求 |
| 12 | 罗尔 | 拉格朗日 | 罗尔要求 $f(a)=f(b)$；拉格朗日是其旋转不变推广 |
| 13 | 柯西中值定理 | 洛必达 | 前者是定理，后者是其推论（且洛必达有条件限制） |
| 14 | 佩亚诺余项 | 拉格朗日余项 | 局部 $o( \cdot)$ vs 整体含 $\xi$；分别用于求极限与误差估计 |
| 15 | 原函数 | 定积分 | 前者是函数族（`+C`），后者是一个数 |
| 16 | 第一换元 | 第二换元 | 凑微分（不换变量）vs 令 $x=\psi(t)$（要回代） |
| 17 | 分部积分 `u` 选取 | 换元顺序 | 「反对幂指三」取 u；换元看复合结构 |
| 18 | 积分上限函数 | 变限积分 | 前者 $\int_{a}^{x}$，后者上下限都变；求导通式不同 |
| 19 | 无穷区间反常积分 | 瑕积分 | $\int_{1}^\infty x^{- p}$ 收敛 p>1；$\int_{0}^{1} x^{- p}$ 收敛 p<1（方向相反） |
| 20 | 绝对收敛（积分） | 条件收敛 | $\int\vert f\vert $ 收敛 ⇒ $\int f$ 收敛；反之不然 |
| 21 | 微元 `dU` | 增量 $\Delta U$ | 要求 $\Delta U- dU=o(dx)$，即「以直代曲」的误差为高阶 |
| 22 | 弧长公式 | 旋转曲面面积 | $\int \sqrt{1+y'^{2}}dx$ vs $2\pi \int y\sqrt{1+y'^{2}}dx$ |
| 23 | 齐次方程（一阶） | 齐次线性方程 | $y'=\phi\left(\dfrac{y}{x}\right)$ vs `y′+P(x)y=0`；同名不同义 |
| 24 | 线性方程齐次解 | 非齐次特解 | 通解 = 齐次通解 + 一个特解；特解不含任意常数 |
| 25 | 特征根重数 k | 待定系数 $x^{k}$ | λ 是特征方程的 k 重根 ⇒ 特解乘 $x^{k}$（共振） |
| 26 | 欧拉方程 | 欧拉公式 | $x^{2}y''+pxy'+qy=f$ vs $e^{ix}=\cos x+i \sin x$ |
| 27 | 数量积 | 向量积 | 标量 vs 向量；交换 vs 反交换 |
| 28 | 混合积 | 行列式 | 混合积是三向量构成的三阶行列式；共面 ⇔ 为 0 |
| 29 | 平面法向量 | 直线方向向量 | 直线一般式方向 = 两平面法向量叉积 |
| 30 | 柱面 | 旋转曲面 | 方程缺一个变量 vs 由母线绕轴旋转生成 |
| 31 | 二重极限 | 累次极限 | 二重极限沿任意路径；累次极限是先后两次一元极限 |
| 32 | 偏导数存在 | 可微 | 多元中偏导存在 ⇏  连续、⇏  可微；偏导连续 ⇒ 可微 |
| 33 | 方向导数 | 梯度 | 方向导数是标量（沿某方向变化率）；梯度是向量（最大增长方向） |
| 34 | 全微分形式不变性 | 链式法则 | 前者说 $dz=f_{u}du+f_{vdv}$ 形式不变，后者给出偏导的具体组合 |
| 35 | 无条件极值 $\Delta=AC- B^{2}$ | 条件极值拉格朗日 | 前者判驻点性质，后者处理带约束；λ 不是所求 |
| 36 | X 型 / Y 型区域 | 换序 | 前者是先 y 后 x / 先 x 后 y；换序要重画区域、必要时分块 |
| 37 | 极坐标 $r dr d\theta$ | 球坐标 $\rho^{2}\sin \phi$ | 二维雅可比 vs 三维雅可比；φ 是与 z 轴夹角 |
| 38 | 第一类线积分 | 第二类线积分 | 对弧长（与方向无关）vs 对坐标（反向变号） |
| 39 | 第一类面积分 | 第二类面积分 | 对面积（无侧向）vs 对坐标（与侧有关） |
| 40 | 格林 | 高斯 | 平面闭曲线→二重积分 vs 空间闭曲面→三重积分 |
| 41 | 斯托克斯 | 高斯 | 曲面边界曲线 vs 体积边界曲面；分别对应旋度与散度 |
| 42 | 散度 | 旋度 | 标量（通量源）vs 向量（环流强度）；$\nabla \cdot( \nabla \times A)=0$ |
| 43 | 路径无关 | 全微分求积 | 单连通域内二者等价；判据 $\dfrac{\partial P}{\partial y}= \dfrac{\partial Q}{\partial x}$ |
| 44 | 级数收敛 | 通项趋于 0 | 后者是必要条件非充分（调和级数） |
| 45 | 绝对收敛 | 条件收敛 | 前者可任意重排且和不变；后者重排可改变和 |
| 46 | 比值判别 | 根值判别 | 根值更强；$\rho=1$ 二者都失效 |
| 47 | 收敛半径 | 收敛域 | 半径给出开区间，端点须单独判定才得收敛域 |
| 48 | 泰勒级数 | 傅里叶级数 | 局部导数信息 / 解析要求 vs 整体积分信息 / 允许间断 |
| 49 | 一致收敛 | 逐点收敛 | 一致收敛才保证和函数连续、可逐项积分与求导 |
| 50 | 狄利克雷收敛定理 | 莱布尼茨判别法 | 前者判傅里叶级数收敛值，后者判交错级数收敛 |

---

## 记号与术语速查

| 记号 | 读法 | 含义 |
| --- | --- | --- |
| $\forall, \exists, \Rightarrow, \Leftrightarrow$ | 任意 / 存在 / 推出 / 等价 | 逻辑量词，ε–δ 定义的基础 |
| $\epsilon, \delta, N, M$ | 艾普西龙 / 德尔塔 | 极限定义中的任意小量与相应阈值 |
| $o( \cdot), O( \cdot), \sim$ | 高阶无穷小 / 同阶 / 等价 | $\alpha=o(\beta)$ 表示 $\lim \dfrac{\alpha}{\beta}= 0$ |
| `lim, sup, inf` | 极限 / 上确界 / 下确界 | 数列也常用上下极限 `limsup/liminf` |
| $f', f'', f^{(n)}$ | 一阶 / 二阶 / n 阶导数 | 偏导用 $f_{x}, f_{xy}$ |
| $dy, \Delta y, dx$ | 微分 / 增量 / 自变量微分 | $\Delta y= dy+ o(\Delta x)$ |
| $\int, \iint , \iiint , \oint , \oiint $ | 不定/定积分 / 二重 / 三重 / 闭曲线 / 闭曲面 | `∮` 强调路径闭合 |
| $\int_{a}^{x}, \int_{\alpha(x)}^{\beta(x)}$ | 积分上限函数 / 变限积分 | 求导用莱布尼茨通式 |
| $\sum, \Pi$ | 求和 / 求积 | $S_{n}$ 为部分和 |
| $\nabla, \nabla \cdot, \nabla \times, \nabla^{2}$ | 梯度 / 散度 / 旋度 / 拉普拉斯算子 | Nabla 算子 |
| $\partial, \dfrac{\partial(F,G)}{\partial}(u,v)$ | 偏导 / 雅可比行列式 | 隐函数方程组与重积分换元 |
| $\rho, \phi, \theta, r$ | 球径 / 天顶角 / 方位角 / 极径 | 球坐标 $\phi$ 是与 z 轴夹角 |
| $\vert a\vert , a \cdot b, a \times b,[a b c]$ | 模 / 数量积 / 向量积 / 混合积 | 三种积结果类型不同 |
| $\Delta=AC- B^{2}$ | 判别式 | 二元极值判别；`H` 为海森矩阵 |
| $\kappa, \rho=\dfrac{1}{\kappa}$ | 曲率 / 曲率半径 | 注意 ρ 与球坐标 ρ 同名不同义 |
| `R` | 收敛半径 | 收敛域需另判端点 |
| $a_{n}, b_{n}$ | 傅里叶系数 | 由三角函数系正交性得到 |

| 中文术语 | 英文 / 常见别名 |
| --- | --- |
| 夹逼准则 | Squeeze theorem / 迫敛性 / 两边夹 |
| 单调有界准则 | Monotone convergence theorem |
| 柯西中值定理 | Cauchy's mean value theorem |
| 洛必达法则 | L'Hôpital's rule |
| 泰勒公式（佩亚诺 / 拉格朗日余项） | Taylor's formula (Peano / Lagrange remainder) |
| 麦克劳林展开 | Maclaurin series |
| 牛顿–莱布尼茨公式 | Fundamental theorem of calculus（微积分基本定理） |
| 分部积分 | Integration by parts |
| 区间再现 / King 公式 | King property |
| 华里士公式 | Wallis formula / 点火公式 |
| 反常积分 | Improper integral；无界函数情形称瑕积分 |
| 微元法 | Element method / 元素法 |
| 伯努利方程 | Bernoulli equation |
| 特征方程 | Characteristic equation |
| 朗斯基行列式 | Wronskian |
| 欧拉方程（ODE） | $Cauchy- Euler$ |
| 混合积 | Scalar triple product |
| 克莱罗定理 | Clairaut's theorem / 混合偏导相等 |
| 拉格朗日乘数法 | Lagrange multiplier method |
| 海森矩阵 | Hessian matrix |
| 雅可比行列式 | Jacobian determinant |
| 格林 / 高斯 / 斯托克斯公式 | Green's / Gauss's (divergence) / Stokes' theorem |
| 散度 / 旋度 / 梯度 | Divergence / Curl / Gradient |
| 路径无关 | Path independence；对应保守场 conservative field |
| 莱布尼茨判别法 | Leibniz test（交错级数） |
| 阿贝尔定理 / 狄利克雷收敛定理 | Abel's theorem / Dirichlet conditions |
| 帕塞瓦尔等式 | Parseval's identity |
| 魏尔斯特拉斯 M 判别法 | Weierstrass M-test |
| 刘维尔定理 | Liouville's theorem（初等原函数不存在性） |

---

## 附录 A 公式与结论速查

### A.1 极限与连续（第 1 章）

| 项目 | 公式 |
| --- | --- |
| 两个重要极限 | $\lim_{x \to 0} \dfrac{\sin x}{x}= 1$；$\lim_{x \to \infty}\left(1+\dfrac{1}{x}\right)^{x}= e$ |
| $1^\infty$ 速算 | $\lim f^g= e^{\lim g(f- 1)}$（$f \to 1, g \to \infty$） |
| 等价无穷小 | $\sin x \sim \tan x \sim \arcsin x \sim \ln(1+x) \sim e^{x}- 1 \sim x$；$1-\cos x \sim \dfrac{x^{2}}{2}$；$(1+x)^\alpha- 1 \sim \alpha x$；$x-\sin x \sim \dfrac{x^{3}}{6}$ |
| 五个麦克劳林 | $e^{x}=\sum\dfrac{x^{n}}{n!}$；$\sin x=\sum\dfrac{(-1)^{n}x^{2n+1}}{(2n+1)!}$；$\cos x=\sum\dfrac{(-1)^{n}x^{2n}}{(2n)!}$；$\ln(1+x)=\sum\dfrac{(-1)^{n-1}x^{n}}{n}$；$(1+x)^\alpha=1+\alpha x+\dfrac{\alpha(\alpha- 1)x^{2}}{2}+ \cdots$ |
| 泰勒余项 | 佩亚诺 $o((x- x_{0})^{n})$；拉格朗日 $\dfrac{f^{(n+1)}(\xi)(x- x_{0})^{n+1}}{n+1}!$ |
| 间断点 | 第一类（可去/跳跃，左右极限存在）；第二类（无穷/振荡） |
| 闭区间连续四性质 | 有界、最值、介值、零点定理 |

### A.2 导数与微分（第 2 章）

| 项目 | 公式 |
| --- | --- |
| 定义 | $f'(x_{0})=\lim \dfrac{f(x_{0}+\Delta x)- f(x_{0})}{\Delta x}$；$dy=f'(x)dx$ |
| 四则 | $(uv)'=u'v+uv'$；$\left(\dfrac{u}{v}\right)'=\dfrac{u'v- uv'}{v^{2}}$ |
| 链式 / 反函数 | $\dfrac{dy}{dx}=f'(u)g'(x)$；$\dfrac{dx}{dy}=\dfrac{1}{y'}$ |
| 隐函数 / 参数 | $\dfrac{dy}{dx}=- \dfrac{F_{x}}{F_{y}}$；$\dfrac{dy}{dx}=\dfrac{\dot{y}}{\dot{x}}$，$\dfrac{d^{2}y}{dx^{2}}=\dfrac{\dfrac{d}{dt\left(\dfrac{dy}{dx}\right)}}{\dot{x}}$ |
| 对数求导 | $y=x^{x} \Rightarrow y'=x^{x}(\ln x+1)$ |
| 莱布尼茨 | $(uv)^{(n)}=\sum C(n,k)u^{(k)}v^{(n-k)}$ |
| 常用 n 阶 | $(\sin x)^{(n)}=\sin\left(x+\dfrac{n\pi}{2}\right)$；$\left(\dfrac{1}{x+a}\right)^{(n)}=\dfrac{(-1)^{n}\,n!}{(x+a)^{n+1}}$ |

### A.3 中值定理与导数应用（第 3 章）

| 项目 | 公式 |
| --- | --- |
| 罗尔 / 拉格朗日 / 柯西 | $f'(\xi)=0$；$f(b)- f(a)=f'(\xi)(b- a)$；$\dfrac{f(b)- f(a)}{g(b)- g(a)}=\dfrac{f'(\xi)}{g'(\xi)}$ |
| 洛必达 | $\lim \dfrac{f}{g}=\lim \dfrac{f'}{g'}$（须验证四前提） |
| 单调 / 凹凸 | $f'>0$ 增；$f''>0$ 凹（∪） |
| 极值充分 | $f'(x_{0})=0, f''(x_{0})<0$ 极大、`>0` 极小 |
| 渐近线 | 水平 `y=A`；铅直 $x=x_{0}$；斜 $a=\lim \dfrac{f}{x}, b=\lim(f- ax)$ |
| 曲率 | $\kappa=\dfrac{\vert y''\vert}{(1+y'^{2})^{\dfrac{3}{2}}}$，$\rho=\dfrac{1}{\kappa}$ |

### A.4 积分（第 4–6 章）

| 项目 | 公式 |
| --- | --- |
| 基本 | $\int x^{a}\,dx=\dfrac{x^{a+1}}{a+1}+C\ (a\ne -1)$；$\int\dfrac{dx}{x}=\ln\lvert x\rvert+C$；$\dfrac{\int dx}{a^{2}+x^{2}}=\left(\dfrac{1}{a}\right)\arctan\left(\dfrac{x}{a}\right)+C$ |
| 三类方法 | 第一换元 $\int f(\phi)\phi 'dx= \int f(u)du$；第二换元 $x=\psi(t)$；分部 $\int u dv=uv- \int v du$ |
| 微积分基本定理 | $\Phi(x)= \int_{a}^{x}f(t)dt \Rightarrow \Phi '=f$；$\int_{a}^{b}f dx=F(b)- F(a)$ |
| 变限求导 | $\dfrac{d}{dx} \int_{\alpha(x)}^{\beta(x)}f= f(\beta)\beta '- f(\alpha)\alpha '$ |
| 区间再现 | $\int_{a}^{b}f(x)dx= \int_{a}^{b}f(a+b- x)dx$；$\int_{0}^\pi x f(\sin x)dx=\left(\dfrac{\pi}{2}\right) \int_{0}^\pi f(\sin x)dx$ |
| 华里士 | $I_{n}= \int_{0}^{\dfrac{\pi}{2}}\sin^{n}x dx$，$I_{n}=\dfrac{n-1}{n}\,I_{n-2}$；偶 $\dfrac{(n-1)!!}{n!!}\cdot\dfrac{\pi}{2}$，奇 $\dfrac{(n-1)!!}{n!!}$ |
| 反常积分 | $\int_{1}^\infty x^{- p}$ 收敛 ⇔ `p>1`；$\int_{0}^{1}x^{- p}$ 收敛 ⇔ `p<1`；$\int_{0}^\infty e^{- x^{2}}dx=\dfrac{\sqrt{\pi}}{2}$ |
| 微元法应用 | 面积 $\int\vert f- g\vert dx$；极坐标 $\dfrac{1}{2} \int r^{2}d\theta$；体积 $\pi \int f^{2}dx$（绕 x）、$2\pi \int x f dx$（绕 y）；弧长 $\int \sqrt{1+y'^{2}}dx$；功 $\int F dx$ |

### A.5 微分方程（第 7 章）

| 类型 | 通解 / 解法 |
| --- | --- |
| 可分离 | $\dfrac{\int dy}{g(y)}= \int f(x)dx+C$ |
| 一阶线性 | $y=e^{- \int P}[ \int Q e^{\int P}dx+C]$ |
| 伯努利 | $z=y^{1- n}$ 化线性 |
| 二阶常系数齐次 | $r^{2}+pr+q=0$：不等实根 $C_{1}e^{r_{1}x}+C_{2}e^{r_{2}x}$；重根 $(C_{1}+C_{2}x)e^{rx}$；复根 $e^{\alpha x}(C_{1}\cos \beta x+C_{2}\sin \beta x)$ |
| 非齐次特解 | $y*=x^{k}e^{\lambda x}Q_{m}(x)$（`k` = λ 的特征根重数） |
| 欧拉方程 | $x=e^{t}$ 或设 $y=x^{k}$ |

### A.6 空间解析几何（第 8 章）

| 项目 | 公式 |
| --- | --- |
| 三种积 | $a\cdot b=a_{x}b_{x}+a_{y}b_{y}+a_{z}b_{z}$；$a \times b$ 为叉积分量；$[a b c]=(a \times b) \cdot c$ |
| 平面 | `Ax+By+Cz+D=0`，`n=(A,B,C)`；点面距 $d=\vert Ax_{0}+By_{0}+Cz_{0}+D\vert  \sqrt{A^{2}+B^{2}+C^{2}}$ |
| 直线 | $\dfrac{x- x_{0}}{m}=\dfrac{y- y_{0}}{n}=\dfrac{z- z_{0}}{p}$，`s=(m,n,p)`；一般式 $s=n_{1} \times n_{2}$ |
| 夹角 | 面面 $\cos\theta=\dfrac{|n_1\cdot n_2|}{|n_1||n_2|}$；线面 $\sin\theta=\dfrac{|s\cdot n|}{|s||n|}$ |
| 异面直线距离 | $d=\vert [s_{1} s_{2} P_{1}P_{2}]\vert \vert s_{1} \times s_{2}\vert $ |
| 旋转曲面 | 绕 z 轴：$f(y,z)=0 \Rightarrow f\left(\pm\sqrt{x^{2}+y^{2}}, z\right)=0$ |

### A.7 多元微分（第 9 章）

| 项目 | 公式 |
| --- | --- |
| 全微分 | $dz=f_{x}dx+f_{y}dy$；可微要求 $\Delta z- dz=o(\rho)$ |
| 链式 | $z=f(u,v), u=u(x,y), v=v(x,y) \Rightarrow z_{x}=f_{u}u_{x}+f_{v}v_{x}$ |
| 隐函数 | $z_{x}=- \dfrac{F_{x}}{F_{z}}$；方程组用雅可比 $J=0$ |
| 方向导数 / 梯度 | $\dfrac{\partial f}{\partial l}= \nabla f \cdot e_{l}$（可微时）；$\nabla f=(f_{x},f_{y},f_{z})$；最大值 $\vert  \nabla f\vert $ |
| 切平面 / 法线 | $F_{x}(x- x_{0})+F_{y}(y- y_{0})+F_{z}(z- z_{0})=0$；法线方向 $\nabla F$ |
| 极值判别 | $A=f_{xx},B=f_{xy},C=f_{yy},\Delta=AC- B^{2}$；$\Delta>0$ 且 `A<0` 极大、`A>0` 极小；$\Delta<0$ 鞍点 |
| 条件极值 | $L=f+\sum \lambda_{i}\phi_{i}$，解 $\nabla L=0$ |

### A.8 重积分与线面积分（第 10–11 章）

| 项目 | 公式 |
| --- | --- |
| 二重积分 | X 型 $\int_{a}^{b}dx \int_{\phi_{1}}^{\phi_{2}}f dy$；极坐标 $\iint f(r \cos \theta,r \sin \theta) r dr d\theta$ |
| 三重积分 | 柱 $dV=r dr d\theta dz$；球 $dV=\rho^{2}\sin \phi d\rho d\phi d\theta$；一般 `dV=|J|du dv dw` |
| 曲面面积 | $A=\iint \sqrt{1+z_{x}^{2}+z_{y}^{2}}dxdy$ |
| 两类线积分 | $\int_{L} f ds$；$\int_{L} Pdx+Qdy= \int(P \cos \alpha+Q \cos \beta)ds$ |
| 两类面积分 | $\iint _{\Sigma} f dS$；$\iint _{\Sigma} P dydz+Q dzdx+R dxdy=\iint (P \cos \alpha+Q \cos \beta+R \cos \gamma)dS$ |
| 格林 | $\oint _{L} Pdx+Qdy=\iint _{D}(Q_{x}- P_{y})dxdy$ |
| 高斯 | $\oiint _{\Sigma} P dydz+Q dzdx+R dxdy=\iiint _\Omega(P_{x}+Q_{y}+R_{z})dV$ |
| 斯托克斯 | $\oint _\Gamma A \cdot dl=\iint _{\Sigma}(rot A) \cdot n dS$ |
| 散度 / 旋度 | $div A=P_{x}+Q_{y}+R_{z}$；$rot A= \nabla \times A$；$\nabla \times( \nabla f)=0$、$\nabla \cdot( \nabla \times A)=0$ |
| 路径无关 | 单连通域内 $P_{y}=Q_{x}$ ⇔ 闭路积分为 0 ⇔ 存在原函数 `u` |

### A.9 无穷级数（第 12 章）

| 项目 | 公式 |
| --- | --- |
| 必要条件 | $\sum u_{n}$ 收敛 ⇒ $\lim u_{n}=0$ |
| 基准级数 | $\sum q^{n}$ 收敛 ⇔ `|q|<1`；$\sum\dfrac{1}{n^{p}}$ 收敛 ⇔ `p>1`；$\sum\dfrac{1}{n(n+1)}=1$ |
| 比值 / 根值 | $\rho=\lim \dfrac{u_{n+1}}{u_{n}}$ 或 $\lim_{n\to\infty}\sqrt[n]{u_{n}}$；$\rho<1$ 收敛、`>1` 发散、`=1` 失效 |
| 交错 | 莱布尼茨：$u_{n}↓0$ ⇒ 收敛，$\vert r_{n}\vert  \le u_{n+1}$ |
| 幂级数 | $R=\lim\vert \dfrac{a_{n}}{a_{n+1}}\vert $；逐项求导/积分 R 不变 |
| 常用和函数 | $\sum x^{n}=\dfrac{1}{1- x}$；$\sum n x^{n}=\dfrac{x}{(1- x)^{2}}$；$\sum\dfrac{x^{n}}{n}=- \ln(1- x)$；$\sum\dfrac{(-1)^{n+1}}{n}=\ln 2$ |
| 傅里叶系数 | $a_{n}=\left(\dfrac{1}{\pi}\right) \int_{- \pi}^{\pi}f \cos nx dx$，$b_{n}=\left(\dfrac{1}{\pi}\right) \int_{- \pi}^{\pi}f \sin nx dx$ |
| 狄利克雷 | 间断点收敛于 $\dfrac{f(x^{-})+f(x^{+})}{2}$ |
| 帕塞瓦尔 | $\left(\dfrac{1}{\pi}\right) \int_{- \pi}^{\pi}f^{2}dx= \dfrac{a_{0}^{2}}{2}+\sum(a_{n}^{2}+b_{n}^{2})$ |

### A.10 一页纸解题索引

| 见到 | 立即想到 |
| --- | --- |
| $\dfrac{0}{0}$ 且加减结构 | **泰勒展开**（不是等价无穷小替换），展开到主阶不抵消 |
| $1^\infty$ / $0^{0}$ / $\infty^{0}$ | 取对数，$e^{\lim g \ln f}$ 或 $1^\infty$ 速算 |
| 递推数列极限 | 单调有界准则：先证有界、再证单调、最后解 `A=f(A)` |
| 分段点求导 / 连续性 | **用定义**算左右导数/极限，不代入公式 |
| 证明含 $f'(\xi)$ | 构造辅助函数 + 罗尔；含比值 ⇒ 柯西 |
| 积分含根式 | 三角代换或整体代换；含 $x^{2}+a^{2}$ 想到 arctan |
| 对称区间积分 | 先查奇偶性；三角积分用区间再现 / 华里士 |
| 变限积分求导 | 通式；含参数先换元提出 |
| 反常积分判敛 | 先定类型（无穷区间 / 瑕点），再选 `p` 判别；瑕点在内部要拆 |
| 一阶微分方程 | 先判类型，线性用积分因子；除以 `g(y)` 记得补常数解 |
| 二阶常系数非齐次 | 特征根 → 齐次解 → 按共振重数设 $x^{k}$ 特解 |
| 空间直线一般式 | $s=n_{1} \times n_{2}$；线面夹角用 `sin` |
| 多元「是否可微」 | 先查偏导连续（充分）；不满足则用定义 $\Delta z- dz=o(\rho)$ |
| 条件极值 | 拉格朗日 $L=f+\lambda \phi$，求出候选点后比较 |
| 二重积分算不动 | 换序 / 换极坐标；$e^{- y^{2}}$ 型必须换序 |
| 三重积分 | 含 $x^{2}+y^{2}$ 用柱坐标，含 $x^{2}+y^{2}+z^{2}$ 用球坐标 |
| 闭曲面积分 | 高斯（外侧）；有奇点先挖洞 |
| 闭曲线积分 | 平面用格林、空间用斯托克斯；非闭先补线 |
| 判级数敛散 | 先看通项 → 正项选比较/比值/根值 → 交错用莱布尼茨 → 再判绝对收敛 |
| 求和函数 | 逐项求导或积分化为几何级数，再还原并定常数 |
| 求数项级数和 | 构造幂级数或傅里叶级数，取合适的 `x` 代入 |

---

## 附录 B 易错点速查

1. 函数相同要求定义域与对应规则都相同，仅表达式化简相同不够（`x` 与 $\dfrac{x^{2}}{x}$）。
2. 奇偶性判定的第一步是检查定义域是否关于原点对称。
3. $\sqrt{x^{2}}=|x|$，`arcsin(sin x)` 只在主值区间等于 `x`。
4. 极限定义是「去心」邻域，$f(x_{0})$ 无定义或不等于极限都不影响极限存在。
5. $\lim f= A> 0 \Rightarrow$ 附近 `f>0`；但 `f>0` 只能推出 $\lim f \ge 0$（严格不等号会丢失）。
6. 极限四则运算要求各极限存在且分母极限非零；$\infty- \infty$、$0 \cdot_{\infty}$ 不能拆。
7. 无穷小是**变量**不是「很小的数」；0 是唯一为常数的无穷小。
8. 等价无穷小只能在**乘除因子**中替换；加减项替换前须确认主阶不抵消。
9. $\tan x- \sin \dfrac{x \sim x^{3}}{2}$，不是 `0`；$x-\sin x \sim \dfrac{x^{3}}{6}$。
10. 洛必达只适用于 $\dfrac{0}{0}$、$\dfrac{\infty}{\infty}$，且 $\lim\dfrac{f'}{g'}$ 必须存在；$\dfrac{x+\sin x}{x}$ 是失效反例。
11. $1^\infty$ 未定式须取对数或用 $e^{\lim g(f- 1)}$，不能把底数与指数分别取极限。
12. 佩亚诺余项用于局部求极限，拉格朗日余项用于整体误差估计，二者不可混用。
13. 有任意阶导数 ≠ 泰勒级数收敛到原函数（$e^{- \dfrac{1}{x^{2}}}$ 是反例）。
14. 可去间断与跳跃间断同属第一类；无穷与振荡属第二类。
15. 介值定理与零点定理要求**闭区间上连续**，开区间结论可能失效。
16. 可导 ⇒ 连续、连续 ⇒ 极限存在；反向均不成立（`|x|` 是最简反例）。
17. 一元「可导 ⇔ 可微」，多元「可微 ⇒ 偏导存在」且反之不成立。
18. 导函数可以不连续，但由达布定理导函数没有第一类间断点。
19. 分段点求导必须用定义算左右导数，不能直接代两侧导函数。
20. 参数方程二阶导数要「先对 t 求导再除以 ẋ」，不是 `ÿ/ẍ`。
21. $\int\dfrac{dx}{x}=\ln\lvert x\rvert+C$，绝对值不可省；不定积分不要漏 `+C`。
22. 罗尔定理三条件（闭连续、开可导、端点值相等）缺一不可（`|x|` 在 $[- 1,1]$）。
23. 拉格朗日中值定理的 $\xi$ 属于**开区间** `(a,b)`。
24. 柯西中值定理是洛必达的证明基础，不要把二者当成同一件事。
25. $f'(x_{0})=0$ 只是极值的必要条件（可导时），驻点可能是鞍点。
26. 极值是局部概念、最值是全局概念；闭区间最值必须比较端点。
27. 拐点是曲线上的**点**（写坐标），$f''=0$ 既非充分也非必要。
28. 水平/斜渐近线在 $x \to+ \infty$ 与 $x \to- \infty$ 要分别求，结果可不同。
29. 同一方向水平与斜渐近线至多各一条；有水平线时不必再求斜线。
30. 第一换元不换变量、第二换元必须**回代**；三角代换别把 `t` 留在答案里。
31. 分部积分取 `u` 按「反、对、幂、指、三」；循环型需两次分部后解方程。
32. $e^{- x^{2}}$、`sin x/x`、$\dfrac{1}{\ln} x$ 没有初等原函数，不要硬凑。
33. 有第一类间断点的函数没有原函数，但可能有定积分（可积 ≠ 有原函数）。
34. 积分上限函数 $\Phi$ 在 `f` 可积时连续，仅在 `f` 连续时可导。
35. 变限求导通式中下限项要带负号并乘 $\alpha '(x)$。
36. 被积函数含积分上限变量 `x` 时，须先换元把 `x` 提到积分号外。
37. 对称区间上奇函数积分为 0、偶函数为两倍——前提是区间关于原点对称。
38. $\int_{0}^{\dfrac{\pi}{2}}\sin^{2}x dx= \dfrac{\pi}{4}$，不是 $\dfrac{\pi}{2}$；华里士公式奇偶情形系数不同。
39. $\int_{1}^\infty x^{- p}dx$ 收敛 `p>1`，$\int_{0}^{1}x^{- p}dx$ 收敛 `p<1`，方向相反最易记反。
40. 瑕点在积分区间**内部**必须拆成两段，一段发散即整体发散。
41. 反常积分不能用「柯西主值」冒充收敛。
42. 面积公式要加绝对值（或先求交点分段），否则上下曲线交叉会抵消。
43. 弧长是 $\int \sqrt{1+y'^{2}}dx$，不是 $\int(1+y')dx$。
44. 绕 y 轴的柱壳法与圆盘法积分变量不同，上下限不可混用。
45. 微元法要求 $\Delta U- dU=o(dx)$，即「以直代曲」的误差是高阶无穷小。
46. 「齐次方程 $y'=\phi\left(\dfrac{y}{x}\right)$」与「线性齐次方程 `Q=0`」同名不同义。
47. 可分离变量时除以 `g(y)` 会丢失 `g(y)=0` 的常数解。
48. 一阶线性通解中积分因子是 $e^{\int P dx}$，符号写反会导致全题错误。
49. 特征根为重根时齐次解必须多乘 `x`；复根时别漏 $e^{\alpha x}$。
50. 待定系数法的 $x^{k}$ 因子：$\lambda$ 是特征根的重数即 `k`，漏乘是最高频失分点。
51. 非齐次通解 = 齐次通解 + 一个特解；特解中不含任意常数。
52. 欧拉方程令 $x=e^{t}$；`x<0` 时用 $|x|=e^{t}$，别忽略定义域。
53. 初值问题要把全部常数用初始条件定出，常数个数等于方程阶数。
54. $a \times b$ 反交换、$a \cdot b$ 交换；混合积是对换行列式变号。
55. 直线一般式的方向向量是两平面法向量的**叉积**，不是其中之一。
56. 线面夹角用 $\sin\theta=\dfrac{|s\cdot n|}{|s||n|}$，面面夹角用 `cos`。
57. 点到平面距离公式分母是法向量的模 $\sqrt{A^{2}+B^{2}+C^{2}}$，不要漏根号。
58. 曲面方程缺一个变量才是柱面；含 $x^{2}+y^{2}$ 且含 $z^{2}$ 的一般不是柱面。
59. 旋转曲面代换规则：绕 z 轴把 `y` 换成 $\pm\sqrt{x^{2}+y^{2}}$，别换错变量。
60. 二次曲面单叶/双叶由负号个数与右端符号共同决定。
61. 二重极限要求沿**任意路径**相同；有限条路径相同不能判存在。
62. 累次极限存在且不等 ⇒ 二重极限不存在；逆命题不成立。
63. 多元偏导数存在 ⇏  连续、⇏  可微；**偏导连续 ⇒ 可微**才是充分条件。
64. 方向导数定义式不要求可微；只有可微时才能用 $\nabla f \cdot e_{l}$。
65. 梯度方向是增长最快方向，$- \nabla f$ 是下降最快方向。
66. 二阶混合偏导相等需要**连续**条件（克莱罗定理），不保证时可能不等。
67. 隐函数求导要求 $F_{z}=0$；方程组情形要求雅可比行列式 $J=0$。
68. 曲面法向量是 $\nabla F$；切平面公式里的系数取**该点处**的偏导值。
69. $\Delta=AC- B^{2}>0$ 时还要看 `A` 的符号；$\Delta<0$ 是鞍点；$\Delta=0$ 判别失效。
70. 极值点也可能偏导不存在（如 $z=\sqrt{x^{2}+y^{2}}$ 在原点）。
71. 拉格朗日乘数 $\lambda$ 不是所求；求出的是候选点，还要比较或结合实际判断。
72. 闭区域最值必须同时检查内部驻点与**整个边界**。
73. 二重积分换序后若区域不是 X/Y 简单型，必须分块。
74. 极坐标面积元是 $r dr d\theta$，漏 `r` 是最高频错误。
75. 球坐标体积元 $\rho^{2}\sin \phi d\rho d\phi d\theta$，$\phi$ 是与 z 轴正向夹角（0 到 π）。
76. 三重积分「先二后一」与「先一后二」的截面/投影选择要看区域形状。
77. $\iint _{D} e^{- y^{2}}dxdy$ 型积分必须换序（先对 x），否则原函数非初等。
78. 第一类线积分与方向无关（上下限须小到大）；第二类与方向有关（反向变号）。
79. 第一类面积分无侧向；第二类面积分必须先定侧再投影。
80. 格林公式要求闭曲线**正向**（逆时针）且区域内偏导连续。
81. 高斯公式要求闭曲面取**外侧**；取内侧整体变号。
82. 区域内有奇点必须挖洞，$\dfrac{x dy- y dx}{x^{2}+y^{2}}$ 是经典反例（结果 2π 不是 0）。
83. 非闭曲线/曲面用公式前要补线/补面，并减去补上部分的贡献。
84. 路径无关四等价只在**单连通域**内成立，含洞区域须另外检验。
85. `div A=0` 称无源场、`rot A=0` 称无旋场；$\nabla \cdot( \nabla \times A)=0$、$\nabla \times( \nabla f)=0$。
86. 级数收敛的必要条件是通项趋于 0；调和级数说明它不充分。
87. `p` 级数 `p>1` 收敛、几何级数 `|q|<1` 收敛，是两个最常用比较基准。
88. 比值/根值法 $\rho=1$ 时失效（$\sum\dfrac{1}{n}$ 与 $\sum\dfrac{1}{n^{2}}$ 都是 $\rho=1$）。
89. 根值判别强于比值判别；阶乘型用比值、`n` 次幂型用根值。
90. 交错级数莱布尼茨判收敛，但**绝对收敛性要另判**。
91. 绝对收敛可任意重排；条件收敛重排可改变和（黎曼定理）。
92. 幂级数收敛半径给出开区间，**端点必须单独判断**才得收敛域。
93. 逐项求导/积分后半径不变，但端点敛散可能改变。
94. 求和函数时别忘了由 `S(0)` 或极限确定积分常数。
95. 傅里叶级数在间断点收敛到左右极限的**平均值**，不是 `f(x)`。
96. 奇函数展开为正弦级数、偶函数为余弦级数；$[0,\pi]$ 上需先作奇/偶延拓。
97. 周期 `2l` 时把 `nx` 换成 $\dfrac{n\pi x}{l}$，系数中 $\dfrac{1}{\pi}$ 换成 `1/l`。
98. 一致收敛才保证和函数连续、可逐项积分与求导；逐点收敛不保证。
99. 所有计算题都应做一次交叉验算：积分结果求导、微分方程解代入原方程、级数和代入特值。
100. 中值定理证明题的 $\xi$ 必须落在**开区间**；用零点定理时先验证端点异号。
101. 遇到「不存在 / 不成立」类命题，先想反例库（`|x|`、$x^{2} \sin\left(\dfrac{1}{x}\right)$、$\sin\left(\dfrac{1}{x}\right)$、调和级数、鞍点）。
102. 单位与量纲要一致：物理应用题的面积、体积、功、压力不能混用变量。
103. 分段函数、含绝对值函数、含参数函数，一律先分情况讨论再计算。
104. 任何「等价」「充分必要」的表述都要检查逆命题；教材中大量定理只是充分条件。

---

::: tip 复习路线建议
**第一轮**：按 12 章正文过一遍，把每个 `danger` 与附录 B 对应条目对照；自己动手重画 18 张图（尤其黎曼和、中值定理几何、二重积分区域换序、球坐标、三大公式定向、判敛决策树）。
**第二轮**：只做「典型计算题逐步演算」12 题、各章末的证明链/反例库/判敛工具箱等进阶小节、8 个公式推导补遗、8 道跨章综合例题与 50 组易混概念对照，检验是否真正区分了概念；配合「各章高频题型清单」练「识别类型」的速度，重点复盘所有数值例题的手算过程与验算。
**第三轮**：用题库按章抽题，限时完成计算题；证明题严格套用「综 8 四步法」。
**考场检查清单**：① 定理条件写了吗（连续/可导/单连通/闭区间/正向）；② 常数 `C`、`+C`、`|x|`、`r`、$\rho^{2}\sin \phi$ 漏了吗；③ 分段与绝对值是否分情况；④ 结果是否做了求导/代入验算；⑤ 题目问的是「点」还是「值」、是「收敛」还是「绝对收敛」。
:::

