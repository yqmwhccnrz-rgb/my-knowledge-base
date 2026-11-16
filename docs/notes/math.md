---
summary: "高等数学 全面详解笔记，将上下册内容按知识逻辑综合为 12 章（不分册）：函数极限与连续、导数与微分、微分中值定理与导数应用、不定积分、定积分与反常积分、定积分的应用、常微分方程、向量代数与空间解析几何、多元函数微分学及其应用、重积分、曲线积分与曲面积分及场论、无穷级数。覆盖 ε-δ 定义与两个重要极限、等价无穷小与泰勒公式、中值定理与洛必达、三类积分法与微积分基本定理、微元法、一阶/二阶常系数微分方程、三种向量积与平面直线、偏导数全微分方向导数梯度与拉格朗日乘数、二重三重积分与换序及极柱球坐标、两类线面积分与格林/高斯/斯托克斯公式、常数项级数审敛与幂级数傅里叶级数。含 18 张自绘图、12 道逐步演算代码块、11 组深挖专题、8 个公式推导补遗、8 道跨章综合例题、12 章高频题型清单、50 组易混概念对照、48 条补充与修正汇总、记号与中英术语速查、附录 A 十组公式速查与一页纸解题索引、附录 B 104 条易错点。"
---

# 高等数学笔记

::: info 笔记概要
- **所属课程**：高等数学（理工科 / 经管类等专业公共基础课）。
- **编写说明**：本笔记把两份教材的内容**综合成一条知识链，不分上下册**——先学一元函数微积分（第 1–6 章），再学微分方程（第 7 章），然后引入空间与多元（第 8–11 章），最后以无穷级数收束（第 12 章）。
- **核心内容**：全书只有两条主线。① **极限**：导数是差商的极限、定积分是黎曼和的极限、重积分与线面积分是微元法的极限、级数是部分和的极限；② **互逆与推广**：<img class="fml" src="/formulas/76afd560e2feaf.png" alt="\int_{a}^{b} f dx= F(b)- F(a)" width="177" height="34"> 是牛顿–莱布尼茨公式，格林、高斯、斯托克斯都是它在高维的推广（统一于广义斯托克斯定理）。抓住这两条，12 章就是一个整体。
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
| 函数 | <img class="fml" src="/formulas/dd73bd413e672f.png" alt="y= f(x), x \in D" width="130" height="33"> | **两要素**：定义域 D 与对应规则 f；二者完全相同才是同一函数 |
| 有界 | <img class="fml" src="/formulas/196fae216974ce.png" alt="\exists M&gt; 0,\vert f(x)\vert  \le M" width="165" height="33"> | 有界性依赖于所给区间（如 `1/x` 在 (0,1) 无界、在 [1,2] 有界） |
| 单调 | <img class="fml" src="/formulas/5a095360d9b1aa.png" alt="x_{1}&lt; x_{2} \Rightarrow f(x_{1}) \le f(x_{2})" width="201" height="33"> | 严格单调是反函数存在的充分条件 |
| 奇偶 | <img class="fml" src="/formulas/39c436730e21c3.png" alt="f(- x)=- f(x)" width="128" height="33"> / <img class="fml" src="/formulas/4be86fc42ce2d6.png" alt="f(- x)= f(x)" width="114" height="33"> | 前提：定义域关于原点对称；奇函数若在 0 有定义则 `f(0)=0` |
| 周期 | `f(x+T) = f(x)` | `sin x, cos x` 周期 <img class="fml" src="/formulas/e5d3bd790b4d66.png" alt="2\pi" width="27" height="33">；`tan x` 周期 <img class="fml" src="/formulas/0e03884f457656.png" alt="\pi" width="18" height="34">；常数函数无最小正周期 |
| 反函数 | 一一对应才有反函数 | <img class="fml" src="/formulas/b58202100fde32.png" alt="\frac{dy}{dx}= \frac{1}{\frac{dx}{dy}}" width="67" height="40">；原函数与反函数图像关于 `y=x` 对称 |
| 复合函数 | <img class="fml" src="/formulas/e224b276317ca6.png" alt="f \circ g" width="44" height="33"> 要求 `R_g ⊆ D_f` | 分层拆解是链式求导的前提 |
| 初等函数 | 基本初等函数经有限次四则与复合、且能写成一个式子 | 在定义区间内连续；分段函数一般**不是**初等函数 |

::: danger 易错 · 函数
- 判定奇偶性**第一步**是检查定义域是否关于原点对称，否则直接判「非奇非偶」。
- <img class="fml" src="/formulas/7c103e1a2aef46.png" alt="\arcsin(\sin x)= x" width="136" height="33">（仅在 <img class="fml" src="/formulas/3446f4690811d5.png" alt="[- \frac{\pi}{2}, \frac{\pi}{2}]" width="62" height="33"> 成立）；<img class="fml" src="/formulas/6081008adda09c.png" alt="\sqrt{x^{2}}=|x|" width="83" height="33">，不是 `x`；<img class="fml" src="/formulas/6a781ddbe44c81.png" alt="\ln(e^{x})=x" width="86" height="33"> 但 <img class="fml" src="/formulas/768dd1a8ca5dc0.png" alt="e^{\ln x}=x" width="71" height="33"> 需 `x>0`。
- 符号函数 `sgn x`、取整函数 `[x]`、狄利克雷函数、积分上限函数 <img class="fml" src="/formulas/93788ed39ba315.png" alt="\Phi(x)= \int_{a}^{x} f(t)dt" width="137" height="33"> 都不是初等函数，但常考。
:::

### 1.2 极限的定义与性质

![极限定义、等价无穷小与两个重要极限](/math/math-limit.svg)

**ε–δ 定义**：<img class="fml" src="/formulas/2f7837bcaba951.png" alt="\lim_{x \to x_{0}} f(x)= A \Leftrightarrow \forall \epsilon&gt;0, \exists \delta&gt;0, 0&lt;|x- x_{0}|&lt;\delta \Rightarrow|f(x)- A|&lt;\epsilon" width="548" height="33">。
数列版：<img class="fml" src="/formulas/8f47e8fff74d09.png" alt="\lim a_{n}= A \Leftrightarrow \forall \epsilon&gt;0, \exists N, n&gt;N \Rightarrow|a_{n}- A|&lt;\epsilon" width="382" height="33">。
注意定义中 <img class="fml" src="/formulas/26727d6a3b0fb5.png" alt="x= x_{0}" width="58" height="33">（去心），故 <img class="fml" src="/formulas/a3b963bcc12b7a.png" alt="f(x_{0})" width="49" height="33"> 可以无定义、也可以不等于 A —— 这正是可去间断点的来源。

| 性质 | 内容 |
| --- | --- |
| 唯一性 | 极限若存在必唯一 |
| 局部有界 / 保号 | <img class="fml" src="/formulas/ad22a293df21a9.png" alt="\lim f= A&gt; 0 \Rightarrow" width="138" height="33"> 去心邻域内 `f > 0`；反之由 <img class="fml" src="/formulas/b0ac9a74dc6ec1.png" alt="f \ge 0" width="51" height="33"> 只能得 <img class="fml" src="/formulas/889ab1e663f375.png" alt="A \ge 0" width="53" height="33"> |
| 四则运算 | 各极限存在且分母极限非零时才可拆分；<img class="fml" src="/formulas/2d92d9933e8950.png" alt="\infty- \infty" width="64" height="33">、<img class="fml" src="/formulas/b6c5dce3826285.png" alt="0 \cdot_{\infty}" width="35" height="33"> 不能直接拆 |
| 左右极限 | <img class="fml" src="/formulas/9d0af07c339712.png" alt="\lim_{x \to x_{0}} f= A \Leftrightarrow f(x_{0}^{-})= f(x_{0}^{+})= A" width="295" height="33"> |
| 夹逼准则 | <img class="fml" src="/formulas/4d1a53d264b831.png" alt="g \le f \le h" width="85" height="33"> 且 <img class="fml" src="/formulas/0e8ba1756e1c93.png" alt="\lim g= \lim h= A \Rightarrow \lim f= A" width="246" height="33"> |
| 单调有界准则 | 单调有界数列必有极限（用于递推数列 <img class="fml" src="/formulas/9c1573b10e5fe9.png" alt="a_{n+1}= f(a_{n})" width="107" height="33">） |
| 两个重要极限 | <img class="fml" src="/formulas/b298fc2aae7f3a.png" alt="\lim_{x \to 0} \dfrac{\sin x}{x}= 1" width="133" height="44">；<img class="fml" src="/formulas/aa153fcd2785f7.png" alt="\lim_{x \to \infty}\left(1+\frac{1}{x}\right)^{x}= e" width="166" height="33">、<img class="fml" src="/formulas/0a268d0247feea.png" alt="\lim_{x \to 0}(1+x)^{\frac{1}{x}}= e" width="156" height="33"> |

::: tip 补充 · 海涅定理（归结原则）
<img class="fml" src="/formulas/47a6f3875babca.png" alt="\lim_{x \to x_{0}} f(x)= A" width="140" height="33"> ⇔ 对任意满足 <img class="fml" src="/formulas/db0e863e9b79dc.png" alt="x_{n} \to x_{0}" width="71" height="33">（<img class="fml" src="/formulas/21e0e1524ca741.png" alt="x_{n}=x_{0}" width="67" height="33">）的数列都有 <img class="fml" src="/formulas/0c2e0bee2db3f8.png" alt="f(x_{n}) \to A" width="91" height="33">。它把**函数极限化为数列极限**，两大用途：① 证明极限不存在——找两个收敛到同一点的数列使 <img class="fml" src="/formulas/a9b4736b037eae.png" alt="f(x_{n})" width="50" height="33"> 极限不同（如 <img class="fml" src="/formulas/9df073beca920d.png" alt="f=\sin\left(\frac{1}{x}\right)" width="94" height="33"> 在 0 处取 <img class="fml" src="/formulas/54eb8f618c2985.png" alt="x_{n}=\frac{1}{2n\pi}" width="75" height="33"> 与 <img class="fml" src="/formulas/afd26818d59b55.png" alt="x_{n}=\frac{1}{2n\pi+\frac{\pi}{2}}" width="95" height="37">）；② 把数列极限转为函数极限来算（先求 <img class="fml" src="/formulas/b10c6870796c52.png" alt="\lim_{x \to \infty}f(x)" width="102" height="33"> 得 <img class="fml" src="/formulas/b3406d14ed7c04.png" alt="\lim a_{n}" width="52" height="33">，反之不行）。
:::

::: tip 工作例题 · 七类未定式的处理
- `0/0`：<img class="fml" src="/formulas/23e388b2a6df2e.png" alt="\lim_{x \to 0} \dfrac{\sin 3x}{5x}= \dfrac{3}{5}" width="146" height="44">（重要极限），<img class="fml" src="/formulas/d8f00c44425a54.png" alt="\lim_{x \to 0}\frac{e^{x}- 1- x}{x^{2}}= \frac{1}{2}" width="145" height="33">（泰勒或洛必达）。
- <img class="fml" src="/formulas/638c8be7aac7e4.png" alt="1^\infty" width="29" height="33">：先取对数或用速算 <img class="fml" src="/formulas/fba9944268486d.png" alt="\lim f^g= e^{\lim g(f- 1)}" width="145" height="33">；<img class="fml" src="/formulas/e60e75df37fa9a.png" alt="\lim_{n \to \infty}\left(1+\frac{2}{n}\right)^{n}= e^{2} \approx 7.3891" width="247" height="33">（数值验证：n=10000 时 7.3876）。
- <img class="fml" src="/formulas/2d92d9933e8950.png" alt="\infty- \infty" width="64" height="33">：<img class="fml" src="/formulas/42d7a7c0db68f0.png" alt="\tan x- \sin x" width="103" height="33"> 型不能逐项替换，<img class="fml" src="/formulas/b0e9b2bca1732e.png" alt="\lim_{x \to 0}\frac{\tan x- \sin x}{x^{3}}= \frac{1}{2}" width="162" height="33">（数值验证 0.500000）。
- <img class="fml" src="/formulas/b6c5dce3826285.png" alt="0 \cdot_{\infty}" width="35" height="33"> 化为 `0/0`；<img class="fml" src="/formulas/0aa24a18a957f4.png" alt="0^{0}" width="23" height="33">、<img class="fml" src="/formulas/96377a713e77fc.png" alt="\infty^{0}" width="32" height="33"> 取对数；<img class="fml" src="/formulas/5486ef8db66980.png" alt="\frac{\infty}{\infty}" width="24" height="33"> 用洛必达或提最高阶。
:::

**常用等价无穷小**（<img class="fml" src="/formulas/2f8c5e9d8b93a9.png" alt="x \to 0" width="54" height="33">，**只能在乘除因子中替换**）：
<img class="fml" src="/formulas/d63e28f19c686f.png" alt="\sin x \sim \tan x \sim \arcsin x \sim \arctan x \sim \ln(1+x) \sim e^{x}- 1 \sim x" width="473" height="33">；
<img class="fml" src="/formulas/d50c3c1a66502e.png" alt="1-\cos x \sim \frac{x^{2}}{2}" width="115" height="33">；<img class="fml" src="/formulas/772dbfa6d21bae.png" alt="(1+x)^\alpha- 1 \sim \alpha x" width="147" height="33">；<img class="fml" src="/formulas/a32bff933e21f1.png" alt="x-\sin x \sim \frac{x^{3}}{6}" width="115" height="33">；<img class="fml" src="/formulas/68a92b1eed6396.png" alt="\tan x- x \sim \frac{x^{3}}{3}" width="119" height="33">；<img class="fml" src="/formulas/e4351fb37e2866.png" alt="x-\ln(1+x) \sim \frac{x^{2}}{2}" width="149" height="33">。

::: danger 易错 · 等价无穷小
「加减项中替换」是最高频错误：<img class="fml" src="/formulas/42d7a7c0db68f0.png" alt="\tan x- \sin x" width="103" height="33"> 若用 `sin x ~ x`、`tan x ~ x` 相减得 0，主阶被抵消，正确答案需展开到三阶（<img class="fml" src="/formulas/b3fbc32b296424.png" alt="\frac{x^{3}}{2}" width="24" height="33">）。判定准则：替换后若结果的主阶未被抵消即可用，否则必须上泰勒。
:::

### 1.3 泰勒公式

![泰勒公式余项、五个麦克劳林展开与求极限](/math/math-taylor.svg)

<img class="fml" src="/formulas/23ae8871480b8f.png" alt="f(x)= \sum_{k=0}\frac{^{n} f^{(k)}(x_{0})(x- x_{0})^{k}}{k}!+ R_{n}(x)" width="282" height="36">：
- **佩亚诺余项** <img class="fml" src="/formulas/6997469d82781b.png" alt="R_{n}= o((x- x_{0})^{n})" width="147" height="33">：局部性质，用于求极限与判极值，只需 `n` 阶可导。
- **拉格朗日余项** <img class="fml" src="/formulas/753a17a9e5aaf0.png" alt="R_{n}= \frac{f^{(n+1)}(\xi)(x- x_{0})^{n+1}}{n+1}!" width="166" height="37">：整体性质，用于误差估计与不等式证明，需 `n+1` 阶可导。

| 函数 | 麦克劳林展开（<img class="fml" src="/formulas/2f8c5e9d8b93a9.png" alt="x \to 0" width="54" height="33">） |
| --- | --- |
| <img class="fml" src="/formulas/23413ccd73e8be.png" alt="e^{x}" width="24" height="33"> | <img class="fml" src="/formulas/367aca3e2ab03c.png" alt="1+ x+ \frac{x^{2}}{2}!+ \cdots+ \frac{x^{n}}{n}!+ o(x^{n})" width="241" height="33"> |
| `sin x` | <img class="fml" src="/formulas/9c24f54da6dc87.png" alt="x- \frac{x^{3}}{3}!+ \frac{x^{5}}{5}!- \cdots" width="147" height="33"> |
| `cos x` | <img class="fml" src="/formulas/f6c1070026c69c.png" alt="1- \frac{x^{2}}{2}!+ \frac{x^{4}}{4}!- \cdots" width="146" height="33"> |
| `ln(1+x)` | <img class="fml" src="/formulas/8a2ca88f25274c.png" alt="x- \frac{x^{2}}{2}+ \frac{x^{3}}{3}- \cdots+ \frac{(- 1)^{n-1}x^{n}}{n}" width="220" height="35"> |
| <img class="fml" src="/formulas/76c1f942f49b3f.png" alt="(1+x)^\alpha" width="71" height="33"> | <img class="fml" src="/formulas/d41f30e1f4aa56.png" alt="1+ \alpha x+ \frac{\alpha(\alpha- 1)x^{2}}{2}!+ \cdots" width="187" height="35"> |
| `arctan x` | <img class="fml" src="/formulas/c04382091553e3.png" alt="x- \frac{x^{3}}{3}+ \frac{x^{5}}{5}- \cdots" width="138" height="33"> |

::: tip 工作例题 · 展开到几阶
分母是 <img class="fml" src="/formulas/025821bec71ad8.png" alt="x^{m}" width="29" height="33">，就把分子展开到「首个非零项恰为 <img class="fml" src="/formulas/025821bec71ad8.png" alt="x^{m}" width="29" height="33">」：
- <img class="fml" src="/formulas/e285899d238426.png" alt="\frac{e^{x}- 1- x}{x^{2}}" width="56" height="33">：<img class="fml" src="/formulas/a00c7acd60c58d.png" alt="e^{x}= 1+x+\frac{x^{2}}{2}+o(x^{2})" width="188" height="33"> ⇒ 分子 <img class="fml" src="/formulas/803c5a8137c6d0.png" alt="= \frac{x^{2}}{2}+ o(x^{2})" width="104" height="33"> ⇒ 极限 `1/2`。
- <img class="fml" src="/formulas/15da1c14df6984.png" alt="\frac{\tan x- \sin x}{x^{3}}" width="74" height="33">：<img class="fml" src="/formulas/e6f635a175b994.png" alt="\tan x= x+ \frac{x^{3}}{3}" width="118" height="34">，<img class="fml" src="/formulas/cc9eeb4e841df0.png" alt="\sin x= x- \frac{x^{3}}{6}" width="115" height="34"> ⇒ 差 <img class="fml" src="/formulas/d10ef306018868.png" alt="= \frac{x^{3}}{2}" width="42" height="34"> ⇒ 极限 `1/2`。
由展开式还可直接读出 <img class="fml" src="/formulas/51b8b90046cfdf.png" alt="f^{(n)}(0)= n! \cdot a_{n}" width="129" height="34">；判极值时看「首个非零偶数阶导数」。
:::

**补充 · 严格性说明**：`f` 有任意阶导数并不保证其泰勒级数收敛到 `f`（经典反例 <img class="fml" src="/formulas/ac7ed7dae34446.png" alt="f(x)=e^{- \frac{1}{x^{2}}}" width="100" height="35">（x≠0）、`f(0)=0`，在 0 处各阶导数全为 0）。收敛到原函数需拉格朗日余项趋于 0，即函数**解析**。教材多只给展开式，此处补足条件。

### 1.4 连续与间断点

| 类型 | 判据 | 例子 |
| --- | --- | --- |
| 第一类·可去 | 左右极限存在且相等，但 <img class="fml" src="/formulas/cbc84953828858.png" alt="= f(x_{0})" width="67" height="34"> 或无定义 | `sin x / x` 在 0 |
| 第一类·跳跃 | 左右极限存在但不等 | `sgn x` 在 0 |
| 第二类·无穷 | 至少一侧极限为 ∞ | `1/x` 在 0 |
| 第二类·振荡 | 极限不存在且不趋于 ∞ | <img class="fml" src="/formulas/443259d666f1a6.png" alt="\sin\left(\frac{1}{x}\right)" width="60" height="34"> 在 0 |

**闭区间上连续函数的四性质**：有界性、最值定理、介值定理、零点定理（<img class="fml" src="/formulas/1a46f9c817fd5a.png" alt="f(a)f(b)&lt;0 \Rightarrow \exists \xi, f(\xi)=0" width="226" height="34">）。这四条是第 3 章大量证明题的依据。

::: danger 易错 · 连续
- `f` 在 <img class="fml" src="/formulas/745a16e24c23d6.png" alt="x_{0}" width="25" height="34"> 连续要求「极限存在 + 有定义 + 极限等于函数值」三条同时成立。
- 介值定理要求**闭区间上连续**；开区间或不连续时结论可能失效。
- 连续不一定可导（`|x|` 在 0）；可导必连续；导函数可以不连续（但导函数无第一类间断点，即达布定理）。
:::

### 1.5 极限严格化的三个层次

| 层次 | 内容 | 作用 |
| --- | --- | --- |
| 直观 | 「无限逼近」 | 建立直觉，但无法证明 |
| ε–δ / ε–N | 把「任意接近」量化为 <img class="fml" src="/formulas/46f26d50db5335.png" alt="\forall \epsilon \exists \delta" width="42" height="34"> | 证明极限存在、唯一性、保号性 |
| 拓扑 | 邻域、聚点、完备性、柯西列 | 实数完备性等价于「单调有界必收敛」「柯西列必收敛」 |

**七种等价刻画**：<img class="fml" src="/formulas/f4c848a53f63e7.png" alt="\lim a_{n}=A" width="90" height="34"> ⇔ 任意子列收敛到 A（若有子列不收敛或收敛到别的值，则原数列不收敛）。判定发散常用「找两个子列极限不同」，如 <img class="fml" src="/formulas/7747e0417042c8.png" alt="(- 1)^{n}" width="52" height="34">。
**Stolz 定理**（考研常用）：<img class="fml" src="/formulas/048e288d9b08b5.png" alt="b_{n}" width="23" height="34"> 严格递增趋于 ∞ 时，<img class="fml" src="/formulas/060970cffcf861.png" alt="\lim \frac{a_{n}}{b_{n}}= \lim \frac{a_{n+1}- a_{n}}{b_{n+1}- b_{n}}" width="155" height="36">（离散版洛必达），用于 <img class="fml" src="/formulas/a6167751e5d4f2.png" alt="\lim \frac{1+\frac{1}{2}+ \cdots+\frac{1}{n}}{\ln} n= 1" width="151" height="36"> 一类题。

---

## 第 2 章 导数与微分（★★★）

### 2.1 导数的定义与几何意义

![导数定义、几何意义与可导连续关系](/math/math-derivative.svg)

<img class="fml" src="/formulas/18eba40b0ef52a.png" alt="f&#x27;(x_{0})= \lim_{\Delta x \to 0}\frac{f(x_{0}+\Delta x)- f(x_{0})}{\Delta x}" width="243" height="34">，几何上是切线斜率 <img class="fml" src="/formulas/34f4d2e4a3a7f4.png" alt="\tan \alpha" width="47" height="34">，物理上是瞬时速度。
**微分** `dy = f′(x)dx`，且 <img class="fml" src="/formulas/19d0f06d5e9e87.png" alt="\Delta y= dy+ o(\Delta x)" width="143" height="34"> ——「以直代曲」是微元法的理论基础。

| 关系（一元） | 结论 |
| --- | --- |
| 可导 ⇔ 可微 | 等价（多元不再等价） |
| 可导 ⇒ 连续 ⇒ 极限存在 | 反向均不成立：`|x|` 在 0 连续不可导 |
| 可导 ⇔ 左导数 = 右导数（有限） | 分段点必须用定义算 |
| `f′` 未必连续 | 但由达布定理，`f′` 无跳跃间断 |

### 2.2 求导法则与特殊函数

| 类型 | 公式 |
| --- | --- |
| 四则 | `(uv)′ = u′v + uv′`；<img class="fml" src="/formulas/7db0dac25d811f.png" alt="\left(\frac{u}{v}\right)&#x27;= \frac{u&#x27;v- uv&#x27;}{v^{2}}" width="111" height="34"> |
| 复合（链式） | <img class="fml" src="/formulas/27fac4a205a861.png" alt="y=f(u), u=g(x) \Rightarrow y&#x27;= f&#x27;(u)g&#x27;(x)" width="292" height="34">，多层复合逐层相乘 |
| 反函数 | <img class="fml" src="/formulas/522f94382c41b7.png" alt="\frac{dx}{dy}= \frac{1}{y}&#x27;" width="64" height="36">；<img class="fml" src="/formulas/97ead55ade9f1b.png" alt="\frac{d^{2}x}{dy^{2}}=- y&#x27;&#x27;(y&#x27;)^{3}" width="120" height="36"> |
| 隐函数 | <img class="fml" src="/formulas/f04bdb6af0dbf9.png" alt="F(x,y)=0 \Rightarrow \frac{dy}{dx}=- \frac{F_{x}}{F_{y}}" width="197" height="37">（<img class="fml" src="/formulas/e51b50c7fbf36a.png" alt="F_{y}=0" width="58" height="34">） |
| 参数方程 | <img class="fml" src="/formulas/2ffbc0ff5111cd.png" alt="\frac{dy}{dx}= \frac{\dot{y}}{\dot{x}}" width="61" height="34">；<img class="fml" src="/formulas/963bc8ccccd71f.png" alt="\frac{d^{2}y}{dx^{2}}= \frac{\frac{d}{dt\left(\frac{\dot{y}}{\dot{x}}\right)}}{\dot{x}}= \frac{\dot{x}\ddot{y}- \ddot{y}\ddot{x}}{\dot{x}^{3}}" width="159" height="48">（先对 t 求导再除 ẋ） |
| 对数求导 | <img class="fml" src="/formulas/bc375f2212094b.png" alt="y=x^{x} \Rightarrow \ln y= x \ln x \Rightarrow y&#x27;= x^{x}(\ln x+ 1)" width="335" height="34"> |
| 高阶·莱布尼茨 | <img class="fml" src="/formulas/73ab689f70b17b.png" alt="(uv)^{(n)}= \sum_{k} C(n,k) u^{(k)} v^{(n-k)}" width="240" height="34"> |
| 常用 n 阶 | <img class="fml" src="/formulas/0df498b5ce870f.png" alt="(\sin x)^{(n)}= \sin\left(x+\frac{n\pi}{2}\right)" width="190" height="34">；<img class="fml" src="/formulas/938db9f18e1a2d.png" alt="\left(\dfrac{1}{x+a}\right)^{(n)}=\dfrac{(-1)^{n}\,n!}{(x+a)^{n+1}}" width="204" height="56"> |

::: tip 工作例题 · 分段点与含绝对值因子
<img class="fml" src="/formulas/9cd1bdf42017c3.png" alt="f(x)= x^{2} \sin\left(\frac{1}{x}\right)" width="138" height="34">（x≠0）、`f(0)=0`：在 0 处 <img class="fml" src="/formulas/13162cc1b222ce.png" alt="f&#x27;(0)= \lim x \sin\left(\frac{1}{x}\right)= 0" width="195" height="34">（可导），但 <img class="fml" src="/formulas/6221cb006cdb6f.png" alt="f&#x27;(x)=2x \sin\left(\frac{1}{x}\right)- \cos\left(\frac{1}{x}\right)" width="221" height="34"> 在 0 处极限不存在 ⇒ **导函数不连续**。这是「可导但导函数不连续」的标准反例。
经典结论：<img class="fml" src="/formulas/c9987369952dbe.png" alt="g(x)|x- a|" width="91" height="34"> 在 `a` 处可导 ⇔ `g(a)=0`（此时导数为 0）。
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
| 费马引理 | `f` 在 <img class="fml" src="/formulas/745a16e24c23d6.png" alt="x_{0}" width="25" height="34"> 可导且取极值 | <img class="fml" src="/formulas/50a0a7c4e6ade6.png" alt="f&#x27;(x_{0})=0" width="86" height="34"> |
| 罗尔 | `[a,b]` 连续、`(a,b)` 可导、`f(a)=f(b)` | <img class="fml" src="/formulas/142ddcf2f765d8.png" alt="\exists \xi \in(a,b)" width="87" height="34">, <img class="fml" src="/formulas/5f4cd0741f20c3.png" alt="f&#x27;(\xi)=0" width="77" height="34"> |
| 拉格朗日 | `[a,b]` 连续、`(a,b)` 可导 | <img class="fml" src="/formulas/11784e0ef7bd88.png" alt="f(b)- f(a)= f&#x27;(\xi)(b- a)" width="209" height="34"> |
| 柯西 | `f,g` 满足上述条件且 <img class="fml" src="/formulas/5e61604c0433e7.png" alt="g&#x27;=0" width="53" height="34"> | <img class="fml" src="/formulas/b546d340c5acc9.png" alt="\frac{f(b)- f(a)}{g(b)- g(a)}= f&#x27;\frac{\xi}{g}&#x27;(\xi)" width="144" height="37"> |
| 泰勒 | `n+1` 阶可导 | 带拉格朗日余项的 `n` 阶展开（`n=0` 退化为拉格朗日） |

**逻辑链**：罗尔（特殊）→ 拉格朗日（罗尔 + 辅助函数）→ 柯西（参数形式）→ 泰勒（高阶），而**柯西是洛必达法则的证明基础**。

::: tip 工作例题 · 辅助函数构造三步
证 <img class="fml" src="/formulas/31dbc4a6c1a12d.png" alt="\exists \xi : f&#x27;(\xi)+ f(\xi)g&#x27;(\xi)= 0" width="202" height="34">：
① 把待证式看成某函数 `F` 的导数等于 0；② 乘积分因子 `e^{g(x)}` 得 `F(x)=e^{g(x)}f(x)`；③ 对 `F` 用罗尔定理。
常见模板：证 <img class="fml" src="/formulas/0e0dbf6cb69376.png" alt="f&#x27;(\xi)=k" width="78" height="34"> ⇒ <img class="fml" src="/formulas/9d01d96a08aad0.png" alt="F=f- kx" width="97" height="34">；证 <img class="fml" src="/formulas/6331fb43a3ac8b.png" alt="f&#x27;\frac{\xi}{g}&#x27;(\xi)=k" width="94" height="36"> ⇒ 柯西；含 `f″` ⇒ 两次罗尔或对 `f′` 用拉格朗日；含积分 ⇒ 积分中值定理。
:::

**洛必达法则的四个前提**（常被忽略）：① 属 `0/0` 或 <img class="fml" src="/formulas/5486ef8db66980.png" alt="\frac{\infty}{\infty}" width="24" height="33">；② 去心邻域内 `f′、g′` 存在且 <img class="fml" src="/formulas/5e61604c0433e7.png" alt="g&#x27;=0" width="53" height="34">；③ `lim f′/g′` 存在或为 ∞；④ 若 `lim f′/g′` 振荡不存在则**法则失效**，须改用定义或泰勒。
反例：<img class="fml" src="/formulas/eb0ac0abbe2958.png" alt="\lim_{x \to \infty}\frac{x+\sin x}{x}= 1" width="146" height="33">，但 <img class="fml" src="/formulas/bc39eceb5a8e28.png" alt="f&#x27;/g&#x27;= 1+\cos x" width="135" height="33"> 极限不存在，洛必达给不出结论。

### 3.2 单调性、凹凸性、极值与渐近线

![单调凹凸拐点、三类渐近线与作图流程](/math/math-application.svg)

| 判据 | 结论 |
| --- | --- |
| `f′>0` / `f′<0` | 单调递增 / 递减 |
| `f″>0` / `f″<0` | 图形凹（∪，下凸）/ 凸（∩，上凸） |
| `f″` 变号且曲线连续 | 该点为**拐点**（须写成坐标 <img class="fml" src="/formulas/62169bee60e8c9.png" alt="(x_{0}, f(x_{0}))" width="88" height="34">） |
| <img class="fml" src="/formulas/50a0a7c4e6ade6.png" alt="f&#x27;(x_{0})=0" width="86" height="34"> 且 `f′` 变号 | 极值（一阶充分必要判别） |
| <img class="fml" src="/formulas/b46c94de817f5c.png" alt="f&#x27;(x_{0})=0, f&#x27;&#x27;(x_{0})&lt;0" width="176" height="34"> / `>0` | 极大 / 极小；`f″=0` 时失效，须回到定义或更高阶 |

**三类渐近线**：
- 水平 `y = A`，若 <img class="fml" src="/formulas/e96e9d09e102e4.png" alt="\lim_{x \to ± \infty} f(x)= A" width="150" height="34">；
- 铅直 <img class="fml" src="/formulas/26727d6a3b0fb5.png" alt="x= x_{0}" width="58" height="33">，若 <img class="fml" src="/formulas/abc93766cc56ef.png" alt="\lim_{x \to x_{0}} f(x)= \infty" width="144" height="34">（在无定义点、分段点找）；
- 斜 `y = ax+b`，<img class="fml" src="/formulas/a53ee23e792b13.png" alt="a= \lim \frac{f(x)}{x}" width="96" height="34">，<img class="fml" src="/formulas/fd5083fb1408d4.png" alt="b= \lim[f(x)- ax]" width="150" height="34">（只需在水平不存在时求），且 <img class="fml" src="/formulas/bded77789221e0.png" alt="x \to+ \infty" width="77" height="34"> 与 <img class="fml" src="/formulas/6aa1d0a3ab58c5.png" alt="x \to- \infty" width="76" height="34"> 要分别计算。

**曲率** <img class="fml" src="/formulas/45b75032cc6c0f.png" alt="\kappa=\dfrac{|y&#x27;&#x27;|}{(1+y&#x27;^{2})^{\frac{3}{2}}}" width="119" height="53">，曲率半径 <img class="fml" src="/formulas/77e79fd61c9bae.png" alt="\rho= \frac{1}{\kappa}" width="51" height="34">（直线 <img class="fml" src="/formulas/1d4101825a6d4b.png" alt="\kappa=0" width="50" height="34">）。

::: danger 易错 · 导数应用
- 极值是**局部**概念、最值是**全局**概念；闭区间最值必须比较「驻点 + 不可导点 + 端点」。
- <img class="fml" src="/formulas/0f7c7e3c14142d.png" alt="f&#x27;&#x27;(x_{0})=0" width="90" height="34"> 既非拐点的充分条件也非必要条件：<img class="fml" src="/formulas/a3d6f22f6a1009.png" alt="f=x^{4}" width="59" height="34"> 在 0 有 `f″=0` 但不是拐点；<img class="fml" src="/formulas/2177cce4db540f.png" alt="f=x^{\frac{1}{3}}" width="61" height="34"> 在 0 是拐点但二阶导不存在。
- 拐点是曲线上的**点**（要写坐标），极值点是 **x 值**；两者概念维度不同。
- 同一方向水平与斜渐近线至多各一条；若 `a` 不存在（且非 ∞）则无斜渐近线。
:::

**函数作图七步**：定义域与对称性 → 求 `f′, f″` 及其全部零点/不存在点 → 列表分段 → 判单调与极值 → 判凹凸与拐点 → 求渐近线 → 描特殊点连线。列表法（`+ / 0 / − / 不存在`）是最不易失分的格式。

::: tip 补充 · 由单调性得到的常用不等式
构造函数 + 单调性是证明不等式的标准武器，几条「母不等式」值得记住（都可由 `F(x)` 求导证出）：
- <img class="fml" src="/formulas/6a242f0494c880.png" alt="e^{x} \ge 1+x" width="88" height="34">（等号仅 `x=0`）；
- <img class="fml" src="/formulas/446b06b5eec9c1.png" alt="\frac{x}{1+x} \le \ln(1+x) \le x" width="162" height="34">（<img class="fml" src="/formulas/6b65112c6d9f3a.png" alt="x&gt;- 1" width="64" height="34">）；
- `sin x < x < tan x`（<img class="fml" src="/formulas/36af224d250b46.png" alt="0&lt;x&lt;\frac{\pi}{2}" width="85" height="34">）；
- <img class="fml" src="/formulas/0f7872d34bfb2a.png" alt="1- \frac{x^{2}}{2} \le \cos x" width="116" height="34">。
琴生不等式（凸函数 <img class="fml" src="/formulas/d14d7739c08d85.png" alt="f\left(\sum \lambda_{i}x_{i}\right) \le \sum \lambda_{i}f(x_{i})" width="188" height="34">）则是凹凸性的直接推论，处理「和式/均值型」不等式时优先想到。
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
**条件不可省的反例**：`f(x)=|x|` 在 <img class="fml" src="/formulas/b768c3141a0411.png" alt="[- 1,1]" width="56" height="34"> 满足连续且 <img class="fml" src="/formulas/bb9ad34a89e07c.png" alt="f(- 1)=f(1)" width="111" height="33">，但 0 处不可导 ⇒ 不存在 <img class="fml" src="/formulas/5f4cd0741f20c3.png" alt="f&#x27;(\xi)=0" width="77" height="34"> 的点，可见「可导」条件不可去。

---

## 第 4 章 不定积分（★★★）

### 4.1 原函数与基本公式

![三种主要积分法与三类常见可积函数](/math/math-integral.svg)

<img class="fml" src="/formulas/c97d93c121f22b.png" alt="\int f(x)dx= F(x)+ C \Leftrightarrow F&#x27;(x)=f(x)" width="303" height="33">。**连续函数必有原函数**（积分上限函数就是一个）；但有第一类间断点的函数没有原函数（导函数无第一类间断点——达布定理）。

| 基本积分 | 结果 |
| --- | --- |
| <img class="fml" src="/formulas/331fcbe1b00eb4.png" alt="\int x^a dx" width="59" height="33"> | `x^{a+1}/(a+1)+C` (<img class="fml" src="/formulas/72a5eb276907af.png" alt="a=- 1" width="63" height="33">)；<img class="fml" src="/formulas/72a5eb276907af.png" alt="a=- 1" width="63" height="33"> 时 `ln|x|+C` |
| <img class="fml" src="/formulas/c1411c1ff5737f.png" alt="\int e^{x}dx" width="58" height="33">, <img class="fml" src="/formulas/cfba23d0d1d7c1.png" alt="\int a^{x}dx" width="59" height="33"> | <img class="fml" src="/formulas/63165c200f65bc.png" alt="e^{x}+C" width="59" height="33">, <img class="fml" src="/formulas/fadf91efe7db81.png" alt="\frac{a^{x}}{\ln} a+C" width="69" height="33"> |
| <img class="fml" src="/formulas/12424f4a3f3143.png" alt="\int \sin x dx" width="77" height="33">, <img class="fml" src="/formulas/cfe8b3d440a593.png" alt="\int \cos x dx" width="78" height="33"> | <img class="fml" src="/formulas/72df3703bddfe3.png" alt="- \cos x+C" width="97" height="33">, `sin x+C` |
| <img class="fml" src="/formulas/5ccbf3d9ae8429.png" alt="\frac{\int dx}{1+x^{2}}" width="40" height="36">, <img class="fml" src="/formulas/f08b3cf3a78fff.png" alt="\frac{\int dx}{\sqrt{1- x^{2}}}" width="50" height="38"> | `arctan x+C`, `arcsin x+C` |
| <img class="fml" src="/formulas/8c664179fb328f.png" alt="\int \sec x dx" width="77" height="33"> | `ln|sec x + tan x|+C` |
| <img class="fml" src="/formulas/d713ee57fd411c.png" alt="\frac{\int dx}{a^{2}+x^{2}}" width="46" height="36">, <img class="fml" src="/formulas/d8b24eaf047c5e.png" alt="\frac{\int dx}{\sqrt{a^{2}- x^{2}}}" width="56" height="38"> | <img class="fml" src="/formulas/cc291e059c0933.png" alt="\left(\frac{1}{a}\right)\arctan\left(\frac{x}{a}\right)+C" width="153" height="33">, `arcsin(x/a)+C` |
| <img class="fml" src="/formulas/b910ee17d04d59.png" alt="\int f&#x27;\frac{x}{f(x)dx}" width="79" height="36"> | `ln|f(x)|+C`（最高频凑微分） |

### 4.2 三种主要积分法

**第一换元（凑微分）**：<img class="fml" src="/formulas/805c7167beda8e.png" alt="\int f(\phi(x))\phi &#x27;(x)dx= \int f(u)du" width="233" height="33">，关键是把被积式拆成「函数 × 其导数」。
**第二换元（变量代换）**：令 <img class="fml" src="/formulas/8bbc1d63addef1.png" alt="x=\psi(t)" width="74" height="33"> 单调可导，<img class="fml" src="/formulas/7c9c055a52ba78.png" alt="\int f(x)dx= \int f(\psi(t))\psi &#x27;(t)dt" width="224" height="33">，最后必须**回代**。

| 根式 | 代换 | 恒等式 |
| --- | --- | --- |
| <img class="fml" src="/formulas/30f5b92e5664ca.png" alt="\sqrt{a^{2}- x^{2}}" width="78" height="33"> | <img class="fml" src="/formulas/587a92645101a3.png" alt="x= a \sin t" width="85" height="33"> | <img class="fml" src="/formulas/d8f647f4be7060.png" alt="a^{2}- x^{2}= a^{2}\cos^{2}t" width="146" height="33"> |
| <img class="fml" src="/formulas/8d3759baccf8b3.png" alt="\sqrt{a^{2}+x^{2}}" width="78" height="33"> | <img class="fml" src="/formulas/74a7c59992f064.png" alt="x= a \tan t" width="89" height="33"> | <img class="fml" src="/formulas/2150bc78f0a3da.png" alt="a^{2}+x^{2}= a^{2}\sec^{2}t" width="145" height="33"> |
| <img class="fml" src="/formulas/5510cadec10e35.png" alt="\sqrt{x^{2}- a^{2}}" width="78" height="33"> | <img class="fml" src="/formulas/0813af33b412dc.png" alt="x= a \sec t" width="85" height="33"> | <img class="fml" src="/formulas/fc557bc61ef2b7.png" alt="x^{2}- a^{2}= a^{2}\tan^{2}t" width="149" height="33"> |

**分部积分** <img class="fml" src="/formulas/5086f5226bf923.png" alt="\int u dv= uv- \int v du" width="159" height="33">，取 `u` 的优先级口诀「**反、对、幂、指、三**」（反三角 → 对数 → 幂 → 指数 → 三角），把容易求导的放在 `u`。
循环型（如 <img class="fml" src="/formulas/ab187bb48d6f98.png" alt="\int e^{x}\cos x dx" width="98" height="33">）需两次分部后解方程；递推型（如 <img class="fml" src="/formulas/48f5b0c31ade0a.png" alt="I_{n}= \int \sec^{n}x dx" width="126" height="33">）建立递推公式。

### 4.3 三类常见可积函数

| 类型 | 方法 |
| --- | --- |
| 有理函数 `P(x)/Q(x)` | 先化为真分式（多项式除法）→ 分母因式分解 → 部分分式（含重根、二次不可约）→ 逐项积分 |
| 三角有理式 `R(sin x, cos x)` | 万能代换 <img class="fml" src="/formulas/5b7ca1919cb3dd.png" alt="t=\tan\left(\frac{x}{2}\right)" width="94" height="33">：<img class="fml" src="/formulas/77ae8a494cdc13.png" alt="\sin x= \frac{2t}{1+t^{2}}" width="96" height="34">，<img class="fml" src="/formulas/1c52fca747ecbd.png" alt="\cos x= \frac{1- t^{2}}{1+t^{2}}" width="98" height="35">，<img class="fml" src="/formulas/77587b6e546446.png" alt="dx= \frac{2dt}{1+t^{2}}" width="80" height="34">；有更简对称式时优先用 |
| 简单无理函数 | 根式整体代换：<img class="fml" src="/formulas/1696a10405f9a5.png" alt="\int R\left(x,^{n}\sqrt{ax+b}\right)dx" width="168" height="33"> 令 <img class="fml" src="/formulas/39d0d39d3fccf0.png" alt="t=^{n}\sqrt{ax+b}" width="110" height="33">；倒代换 <img class="fml" src="/formulas/0290977fa2741c.png" alt="x=\frac{1}{t}" width="52" height="33"> 处理高次分母 |

::: danger 易错 · 不定积分
- **不要漏 `+C`**；分段积分时各段常数须由连续性统一（否则原函数不连续）。
- 三角代换回代时用辅助直角三角形，别把 `t` 直接留在答案里。
- <img class="fml" src="/formulas/7ff9b056d9bdd3.png" alt="e^{- x^{2}}" width="38" height="34">、`sin x / x`、<img class="fml" src="/formulas/424fbb4096c004.png" alt="\frac{1}{\ln} x" width="32" height="34">、<img class="fml" src="/formulas/e8fe847cfdf305.png" alt="\sqrt{1+k^{2}\sin^{2}x}" width="118" height="35"> 等**原函数不是初等函数**（刘维尔定理），不要硬算；它们靠级数、变限积分或数值方法处理（见第 5、12 章）。
- <img class="fml" src="/formulas/983d6b4fed6520.png" alt="\int\dfrac{dx}{x}=\ln\lvert x\rvert+C" width="140" height="46">，绝对值不能省。
:::

::: tip 工作例题 · 三个分部积分


<p class="fml-block"><img class="fml" src="/formulas/e92765145da2f4.png" alt="\begin{gathered}
(1) \int x e^{x} dx \; \text{：取} \; u=x, dv=e^{x}dx \Rightarrow x e^{x}- \int e^{x}dx=(x- 1)e^{x}+ C \\
\text{验算：} \; [(x- 1)e^{x}]&#x27;= e^{x}+(x- 1)e^{x}= x e^{x} \checkmark \\
(2) \int \ln x dx= x \ln x- \int x \cdot\left(\frac{1}{x}\right)dx= x \ln x- x+ C \\
(3) \int x \cos x dx= x \sin x- \int \sin x dx= x \sin x+ \cos x+ C
\end{gathered}" width="540" height="169"></p>


**验算习惯**：对结果求导，看是否回到被积函数（比重新积分快得多）。
:::

### 4.4 积分技巧体系：何时用哪个

| 被积特征 | 首选方法 |
| --- | --- |
| 复合函数 × 内层导数 | 第一换元（凑微分） |
| 含 <img class="fml" src="/formulas/d932747e87193b.png" alt="\sqrt{a^{2}±x^{2}}" width="77" height="34">、<img class="fml" src="/formulas/5510cadec10e35.png" alt="\sqrt{x^{2}- a^{2}}" width="78" height="33"> | 三角代换 |
| 两个不同类函数相乘（幂×指/三/对/反三角） | 分部积分，按「反对幂指三」取 u |
| 有理分式 | 部分分式分解 |
| 三角函数有理式 | 万能代换（有对称性时优先用倍角/降幂） |
| 对称区间 | 先查奇偶性；三角积分可用区间再现 |
| <img class="fml" src="/formulas/41b9b187dd1450.png" alt="\int_{0}^{\frac{\pi}{2}} \sin^{n}x dx" width="96" height="34"> | 华里士公式 |
| 变限积分求导 | 通式 + 先换元把参数提出 |

**不可积但要会处理的函数**：<img class="fml" src="/formulas/8d29e0fa827dfb.png" alt="\int e^{- x^{2}}dx" width="73" height="34"> 用级数展开或误差函数 `erf(x)`；<img class="fml" src="/formulas/8c77cadac03764.png" alt="\int_{0}^{+\infty}\frac{\sin x}{x}\,dx=\frac{\pi}{2}" width="132" height="34">（狄利克雷积分，用含参积分或拉普拉斯变换）；<img class="fml" src="/formulas/c0b395b3b713e1.png" alt="\int_{0}^{\frac{\pi}{2}} \ln \sin x dx=-\left(\frac{\pi}{2}\right)\ln 2" width="203" height="34">（用区间再现与倍角）。

---

## 第 5 章 定积分与反常积分（★★★）

### 5.1 定义、性质与微积分基本定理

![黎曼和、微积分基本定理与简化技巧](/math/math-definite.svg)

<img class="fml" src="/formulas/89774ffe03beac.png" alt="\int_{a}^{b} f(x)dx= \lim_{\lambda \to 0} \sum f(\xi_{i})\Delta x_{i}" width="251" height="34">（<img class="fml" src="/formulas/838c5c79a9c2aa.png" alt="\lambda=\max \Delta x_{i}" width="108" height="34">）。几何上是曲边梯形的**代数面积**（x 轴下方为负）。
**可积的充分条件**：连续、或单调、或只有有限个第一类间断点；**可积的必要条件**：有界。

| 定理 | 内容 |
| --- | --- |
| 积分中值定理 | `f` 连续 ⇒ <img class="fml" src="/formulas/e7f56e7f04a72d.png" alt="\int_{a}^{b} f dx= f(\xi)(b- a)" width="168" height="34"> |
| 积分上限函数 | <img class="fml" src="/formulas/93788ed39ba315.png" alt="\Phi(x)= \int_{a}^{x} f(t)dt" width="137" height="33">；`f` 连续 ⇒ <img class="fml" src="/formulas/6fb9b4fb2a22c2.png" alt="\Phi &#x27;(x)=f(x)" width="106" height="33">；`f` 可积 ⇒ <img class="fml" src="/formulas/911ac546a85224.png" alt="\Phi" width="20" height="33"> 连续（未必可导） |
| 变限求导通式 | <img class="fml" src="/formulas/0308a6599230c5.png" alt="\frac{d}{dx} \int_{\alpha(x)}^{\beta(x)} f(t)dt= f(\beta)\beta &#x27;- f(\alpha)\alpha &#x27;" width="264" height="38"> |
| **牛顿–莱布尼茨** | <img class="fml" src="/formulas/76afd560e2feaf.png" alt="\int_{a}^{b} f dx= F(b)- F(a)" width="177" height="34">，把求和极限化为原函数增量 |
| 含参变量 | 被积函数含 `x` 时须先换元把 `x` 提到积分号外，再求导 |

::: tip 补充 · 用定积分定义求 n 项和极限
形如 <img class="fml" src="/formulas/759f38ef2857f3.png" alt="\lim_{n \to \infty}\frac{1}{n}\sum_{k=1}^{n} f\left(\frac{k}{n}\right)" width="170" height="33"> 的极限，正是取 <img class="fml" src="/formulas/431f29fd30f2f5.png" alt="x_{k}=\frac{k}{n}" width="61" height="33">、<img class="fml" src="/formulas/146927f03dfd0f.png" alt="\Delta x=\frac{1}{n}" width="67" height="33">、<img class="fml" src="/formulas/e7b646639b0718.png" alt="\xi_{i}=x_{i}" width="60" height="33"> 的黎曼和，故等于 <img class="fml" src="/formulas/7add9cc48cd398.png" alt="\int_{0}^{1} f(x)dx" width="83" height="33">。
例：



<p class="fml-block"><img class="fml" src="/formulas/8431ab71630652.png" alt="\lim\left(\frac{1}{n}\right)\left(\sqrt{1+\frac{1}{n}}+\sqrt{1+\frac{2}{n}}+ \cdots+\sqrt{1+\frac{n}{n}}\right)= \int_{0}^{1}\sqrt{1+x}dx=\left[ \frac{2}{3}(1+x)^{\frac{3}{2}}\right]_{0}^{1}= \frac{2}{3}\left(2\sqrt{2}- 1\right) \approx 1.2189" width="789" height="45"></p>


若和式不是标准 <img class="fml" src="/formulas/5fcdcafca72166.png" alt="\left(\frac{1}{n}\right)\sum f\left(\frac{k}{n}\right)" width="102" height="33"> 形状，先提出 `1/n` 凑形；凑不出的用夹逼放缩。
:::

### 5.2 计算简化四技巧

::: tip 工作例题 · 五个必记积分


<p class="fml-block"><img class="fml" src="/formulas/55ffa201304161.png" alt="\begin{gathered}
(1) \int_{0}^{\frac{\pi}{2}} \sin^{2}x dx= \int_{0}^{\frac{\pi}{2}} \cos^{2}x dx= \frac{\pi}{4} \approx 0.785398 \\
\text{（用} \; \cos 2x= 1- 2\sin^{2}x \; \text{，或华里士公式} \; I_{2}=\left(\frac{1}{2}\right) \cdot\left(\frac{\pi}{2}\right) \; \text{）} \\
(2) \int_{0}^{1} x e^{x} dx=[(x- 1)e^{x}]_{0}^{1}= 0-(- 1)= 1 \\
(3) \int_{0}\frac{^{1} dx}{1+x^{2}}= \arctan x|_{0}^{1}= \frac{\pi}{4} \\
(4) \int_{0}^\pi x \sin x dx=[- x \cos x+ \sin x]_{0}^\pi= \pi \\
(5) \int_{0}^\infty e^{- x^{2}} dx= \frac{\sqrt{\pi}}{2} \approx 0.886227 \; \text{（泊松积分，用二重积分极坐标证明）}
\end{gathered}" width="571" height="294"></p>


:::

| 技巧 | 公式 / 说明 |
| --- | --- |
| 奇偶性 | 对称区间：`f` 奇 ⇒ 积分为 0；`f` 偶 ⇒ <img class="fml" src="/formulas/5251304f1fac49.png" alt="2 \int_{0}^{a} f dx" width="72" height="33"> |
| 周期性 | <img class="fml" src="/formulas/ff023f03acbfea.png" alt="\int_{a}^{a+T} f dx= \int_{0}^{T} f dx" width="157" height="34">；<img class="fml" src="/formulas/2a412be5c4bd3e.png" alt="\int_{0}^{nT} f dx= n \int_{0}^{T} f dx" width="162" height="34"> |
| 区间再现（King） | <img class="fml" src="/formulas/96886db7fac80f.png" alt="\int_{a}^{b} f(x)dx= \int_{a}^{b} f(a+b- x)dx" width="242" height="34">；用于 <img class="fml" src="/formulas/0fe9f9d707cb3e.png" alt="\int_{0}^{\frac{\pi}{2}} f(\sin x, \cos x)dx" width="157" height="34"> 与 <img class="fml" src="/formulas/f961e93c8b9013.png" alt="\int_{0}^\pi x f(\sin x)dx=\left(\frac{\pi}{2}\right) \int_{0}^\pi f(\sin x)dx" width="277" height="33"> |
| 华里士公式 | <img class="fml" src="/formulas/46697ae8328a07.png" alt="I_{n}= \int_{0}^{\frac{\pi}{2}}\sin^{n}x dx= \int_{0}^{\frac{\pi}{2}}\cos^{n}x dx" width="250" height="34">；`n` 偶 ⇒ <img class="fml" src="/formulas/b6b8e75e7369d2.png" alt="\dfrac{(n-1)!!}{n!!}\cdot\dfrac{\pi}{2}" width="104" height="46">；`n` 奇 ⇒ <img class="fml" src="/formulas/2bf227fd3d3ba8.png" alt="\dfrac{(n-1)!!}{n!!}" width="76" height="46">；<img class="fml" src="/formulas/860b1485de9ede.png" alt="I_{n}= \frac{n- 1}{n} \cdot I_{n-2}" width="120" height="33"> |

### 5.3 反常积分（广义积分）

| 类型 | 定义 | 收敛判据 |
| --- | --- | --- |
| 无穷区间 | <img class="fml" src="/formulas/9ce5afbbc387eb.png" alt="\int_{a}^\infty f dx= \lim_{b \to \infty} \int_{a}^{b} f dx" width="199" height="33"> | <img class="fml" src="/formulas/e8bc279d880767.png" alt="\int_{1}^\infty \frac{dx}{x^{p}}" width="53" height="33"> 收敛 ⇔ `p > 1` |
| 无界函数（瑕积分） | 瑕点在端点/内部，须分段取极限 | <img class="fml" src="/formulas/ff03fc549d6c15.png" alt="\int_{0}^{1}\dfrac{dx}{x^{p}}" width="52" height="45"> 收敛 ⇔ `p < 1` |

::: danger 易错 · 反常积分
- 两个 `p` 的收敛方向**相反**（无穷区间 `p>1`、瑕积分 `p<1`），是最高频记忆错误。
- 瑕点在区间**内部**时必须拆成两段分别判敛，只要有一段发散即整体发散；不能用「主值」冒充收敛。
- 比较判别法要求非负；一般函数用**绝对收敛**判据（<img class="fml" src="/formulas/eea7d01c26077b.png" alt="\int|f|" width="42" height="33"> 收敛 ⇒ <img class="fml" src="/formulas/7cfeb56e9a7689.png" alt="\int f" width="33" height="33"> 收敛）。
- 计算反常积分仍可用牛顿–莱布尼茨，但要在无穷/瑕点处取极限，不能把 ∞ 直接代入。
:::

**Γ 函数**（补充）：<img class="fml" src="/formulas/197299876cd4f3.png" alt="\Gamma(s)= \int_{0}^\infty x^{s- 1}e^{- x}dx(s&gt;0)" width="226" height="33">，满足 <img class="fml" src="/formulas/bd5571871303c9.png" alt="\Gamma(s+1)=s\Gamma(s)" width="136" height="33">、<img class="fml" src="/formulas/09e41af8bcc674.png" alt="\Gamma(n+1)=n!" width="113" height="33">、<img class="fml" src="/formulas/849e4f3575b7ba.png" alt="\Gamma\left(\frac{1}{2}\right)=\sqrt{\pi}" width="98" height="33">。它是阶乘的连续延拓，也是 <img class="fml" src="/formulas/f783b473aa8131.png" alt="\int_{0}^\infty e^{- x^{2}}dx= \frac{\sqrt{\pi}}{2}" width="132" height="34"> 的推导工具。

### 5.4 反常积分判敛的完整工具箱

| 判别法 | 陈述 |
| --- | --- |
| 比较判别 | <img class="fml" src="/formulas/5a3aa8bf141d04.png" alt="0 \le f \le g" width="84" height="33">，<img class="fml" src="/formulas/1b8a6fc827cb52.png" alt="\int g" width="31" height="33"> 收敛 ⇒ <img class="fml" src="/formulas/7cfeb56e9a7689.png" alt="\int f" width="33" height="33"> 收敛；<img class="fml" src="/formulas/7cfeb56e9a7689.png" alt="\int f" width="33" height="33"> 发散 ⇒ <img class="fml" src="/formulas/1b8a6fc827cb52.png" alt="\int g" width="31" height="33"> 发散 |
| 极限比较 | <img class="fml" src="/formulas/29e614e6dc2406.png" alt="\lim \frac{f}{g}= c \in(0, \infty)" width="148" height="35"> ⇒ 同敛散；`c=0` 且 <img class="fml" src="/formulas/1b8a6fc827cb52.png" alt="\int g" width="31" height="33"> 收敛 ⇒ <img class="fml" src="/formulas/7cfeb56e9a7689.png" alt="\int f" width="33" height="33"> 收敛；<img class="fml" src="/formulas/1464adebb259f9.png" alt="c= \infty" width="56" height="33"> 且 <img class="fml" src="/formulas/1b8a6fc827cb52.png" alt="\int g" width="31" height="33"> 发散 ⇒ <img class="fml" src="/formulas/7cfeb56e9a7689.png" alt="\int f" width="33" height="33"> 发散 |
| 柯西判别（p 判别） | <img class="fml" src="/formulas/e1ff93ba7a2532.png" alt="\int_{1}^\infty f(x)dx" width="90" height="33">：若 <img class="fml" src="/formulas/ffc34b92efd0fd.png" alt="\lim x^{p} f(x)= c" width="118" height="33"> 且 `p>1` ⇒ 收敛；<img class="fml" src="/formulas/8b6a17f0158de2.png" alt="p \le 1" width="48" height="33"> 且 `c>0` ⇒ 发散。瑕积分换用 <img class="fml" src="/formulas/ba9fe7adec0195.png" alt="\lim(x- a)^{p} f(x)" width="129" height="33">，`p<1` 收敛 |
| 绝对/条件收敛 | <img class="fml" src="/formulas/2e15010cd6335c.png" alt="\int\vert f\vert" width="43" height="33"> 收敛 ⇒ <img class="fml" src="/formulas/7cfeb56e9a7689.png" alt="\int f" width="33" height="33"> 收敛；反之称条件收敛（如 <img class="fml" src="/formulas/e450052d554a7c.png" alt="\int_{1}^\infty \sin \frac{x}{x dx}" width="85" height="33">） |
| Γ / B 函数 | <img class="fml" src="/formulas/62d06b102693f1.png" alt="\Gamma(s)" width="41" height="33">、<img class="fml" src="/formulas/267fa062d9184e.png" alt="B(p,q)=\frac{\Gamma(p)\Gamma(q)}{\Gamma}(p+q)" width="189" height="33">，把许多反常积分化为特殊函数值 |

---

## 第 6 章 定积分的应用（★★）

### 6.1 微元法（元素法）

![微元法、几何与物理应用公式表](/math/math-app-integration.svg)

在 `[x, x+dx]` 上把所求量 `U` 的局部增量写成 `dU = f(x)dx`，要求 <img class="fml" src="/formulas/b07bfbebe62034.png" alt="\Delta U- dU= o(dx)" width="147" height="33">，则 <img class="fml" src="/formulas/87bfa6a8480833.png" alt="U= \int_{a}^{b} f(x)dx" width="121" height="34">。核心思想是「以直代曲、以匀代变」，且微元必须**可加**。
标准流程：**选积分变量 → 写出微元 → 由区域定上下限 → 积分**。

| 几何量 | 直角坐标 | 极坐标 / 参数式 |
| --- | --- | --- |
| 平面面积 | <img class="fml" src="/formulas/8275eaf530bc27.png" alt="A= \int_{a}^{b}\vert f- g\vert dx" width="136" height="34"> | <img class="fml" src="/formulas/c67b599d3887db.png" alt="A= \frac{1}{2} \int_{a}ᵝ r^{2}(\theta)d\theta" width="138" height="34"> |
| 旋转体体积（绕 x） | <img class="fml" src="/formulas/dfaa7dc4966ab5.png" alt="V=\pi \int_{a}^{b} f^{2}(x)dx" width="141" height="34"> | 绕 y 轴柱壳 <img class="fml" src="/formulas/bd7aabed9bf710.png" alt="V=2\pi \int_{a}^{b} x f(x)dx" width="154" height="34"> |
| 已知截面 | <img class="fml" src="/formulas/8eb1019c334363.png" alt="V= \int_{a}^{b} A(x)dx" width="123" height="34"> | — |
| 弧长 | <img class="fml" src="/formulas/9241c3a28d0013.png" alt="s= \int_{a}^{b}\sqrt{1+y&#x27;^{2}}dx" width="149" height="34"> | <img class="fml" src="/formulas/b0e0660000cee8.png" alt="s= \int \sqrt{\dot{x}^{2}+\dot{y}^{2}}dt" width="143" height="33">；<img class="fml" src="/formulas/a458739e56ef60.png" alt="s= \int \sqrt{r^{2}+r&#x27;^{2}}d\theta" width="144" height="33"> |
| 旋转曲面面积 | <img class="fml" src="/formulas/f634f9fbf669c0.png" alt="S=2\pi \int_{a}^{b} f(x)\sqrt{1+y&#x27;^{2}}dx" width="209" height="34"> | — |

**物理应用**：变力做功 <img class="fml" src="/formulas/702bb158f9de8d.png" alt="W= \int F(x)dx" width="123" height="33">；液体侧压力 <img class="fml" src="/formulas/fbde031b8d1f6b.png" alt="P= \int \rho g h(x)w(x)dx" width="169" height="33">；质心 <img class="fml" src="/formulas/9543cbae464701.png" alt="\bar{x}= \frac{\int x dm}{\int dm}" width="81" height="39">；函数平均值 <img class="fml" src="/formulas/f479f25549b4dd.png" alt="\bar{f}=\left(\frac{1}{b- a}\right) \int_{a}^{b} f dx" width="138" height="35">；均方根 <img class="fml" src="/formulas/9638aa046895fc.png" alt="\sqrt{\left(\frac{1}{b- a}\right) \int f^{2}dx}" width="122" height="42">（交流电有效值）。

::: tip 工作例题 · 三道几何题（已核算）


<p class="fml-block"><img class="fml" src="/formulas/45c88da74aa4dc.png" alt="\begin{gathered}
(1) y=x^{2}(0 \le x \le 1) \; \text{绕} \; \text{x} \; \text{轴：} \; V= \pi \int_{0}^{1}(x^{2})^{2}dx= \pi \int_{0}^{1}x^{4}dx= \frac{\pi}{5} \approx 0.628319 \\
(2) y=\sin x(0 \le x \le \pi) \; \text{与} \; \text{x} \; \text{轴围成面积：} \; A= \int_{0}^\pi \sin x dx=[- \cos x]_{0}^\pi= 2 \\
\text{(3)} \; \text{星形线} \; x=a \cos^{3}t, y=a \sin^{3}t \; \text{全长} \; \text{= 6a} \; \text{（} \; \text{a=1} \; \text{时为} \; \text{6} \; \text{）；} \\
\text{第一象限弧长} \; = \int_{0}^{\frac{\pi}{2}}3a \sin t \cos t dt= \frac{3a}{2} \; \text{，乘} \; \text{4} \; \text{得} \; \text{6a} \\
\text{(4)} \; \text{抛物线} \; y=x^{2} \; \text{在} \; \text{[0,1]} \; \text{的弧长} \; = \frac{1}{2}[\sqrt{5}+ \frac{1}{2} \ln\left(2+\sqrt{5}\right)]
\end{gathered}" width="620" height="219"></p>


:::

::: danger 易错 · 微元法
- 面积必须加绝对值（或先求交点分段），否则上下曲线交叉时正负抵消。
- 绕 y 轴旋转可用柱壳法或圆盘法，两者积分变量不同，别混用上下限。
- 弧长公式中 <img class="fml" src="/formulas/b4b12c171310b9.png" alt="\sqrt{1+y&#x27;^{2}}" width="76" height="34"> 不能写成 `1+y′`；物理量的单位与坐标系要一致。
:::

---

## 第 7 章 常微分方程（★★★）

### 7.1 一阶方程的分类解法

![微分方程分类决策树与标准解法](/math/math-ode.svg)

| 类型 | 标准形式 | 解法 |
| --- | --- | --- |
| 可分离变量 | `y′=f(x)g(y)` | <img class="fml" src="/formulas/e2c472576096e1.png" alt="\frac{\int dy}{g(y)}= \int f(x)dx+ C" width="164" height="38"> |
| 齐次方程 | <img class="fml" src="/formulas/02db8c6f27ed0e.png" alt="y&#x27;=\phi\left(\frac{y}{x}\right)" width="85" height="34"> | 令 <img class="fml" src="/formulas/d34cf334a0d083.png" alt="u=\frac{y}{x} \Rightarrow y&#x27;=u+xu&#x27;" width="174" height="34">，化为可分离 |
| 一阶线性 | `y′+P(x)y=Q(x)` | 积分因子 <img class="fml" src="/formulas/f3b8af3e3d17dc.png" alt="e^{\int P dx}" width="50" height="34">；<img class="fml" src="/formulas/f6e15a23018a77.png" alt="y= e^{- \int P}[ \int Q e^{\int P}dx+ C]" width="207" height="34"> |
| 伯努利 | <img class="fml" src="/formulas/dbf2cd346b8af3.png" alt="y&#x27;+Py=Qy^{n}(n=0,1)" width="195" height="34"> | 令 <img class="fml" src="/formulas/dbe67da308230c.png" alt="z=y^{1- n}" width="74" height="34"> 化为线性 |
| 全微分方程 | `M dx+N dy=0` 且 <img class="fml" src="/formulas/5f10128ee5ccf3.png" alt="\frac{\partial M}{\partial y}= \frac{\partial N}{\partial x}" width="79" height="36"> | 求原函数 `u(x,y)=C`（偏积分法 / 曲线积分） |
| 可降阶 | `y″=f(x)` / `f(x,y′)` / `f(y,y′)` | 积两次 / 令 `p=y′` / 令 `p=y′`, <img class="fml" src="/formulas/e1d0b9a7af27eb.png" alt="y&#x27;&#x27;=\frac{p dp}{dy}" width="71" height="36"> |

::: tip 工作例题 · 一阶线性
<img class="fml" src="/formulas/84680f728d0fb2.png" alt="y&#x27;+2y=e^{x}" width="101" height="34">：积分因子 `e^{2x}`，两边乘后 `(e^{2x}y)′=e^{3x}`，
⇒ `e^{2x}y = ⅓e^{3x}+C` ⇒ <img class="fml" src="/formulas/7c81414d3c95d0.png" alt="y= \frac{1}{3} e^{x}+ Ce^{- 2x}" width="135" height="34">。
验算：<img class="fml" src="/formulas/6dcbce7fa6c794.png" alt="y&#x27;+2y= \frac{1}{3} e^{x}- 2Ce^{- 2x}+ \frac{2}{3} e^{x}+ 2Ce^{- 2x}= e^{x}" width="355" height="34"> ✓
:::

### 7.2 高阶线性方程与常系数

**解的结构**：`n` 阶线性方程通解含 `n` 个独立任意常数；齐次解的线性组合仍是齐次解；**非齐次通解 = 齐次通解 + 一个特解**；两非齐次解之差是齐次解。

**二阶常系数齐次** `y″+py′+qy=0`，特征方程 <img class="fml" src="/formulas/843f276d8a3fa9.png" alt="r^{2}+pr+q=0" width="125" height="34">：

| 特征根 | 通解 |
| --- | --- |
| 两不等实根 <img class="fml" src="/formulas/feb63e9166e3d9.png" alt="r_{1}=r_{2}" width="61" height="34"> | <img class="fml" src="/formulas/b1b57e2a570dad.png" alt="C_{1}e^{r_{1}x}+C_{2}e^{r_{2}x}" width="124" height="34"> |
| 二重根 `r` | <img class="fml" src="/formulas/b0ed4ffb52ffad.png" alt="(C_{1}+C_{2}x)e^{rx}" width="115" height="34"> |
| 共轭复根 <img class="fml" src="/formulas/bf70465e226a13.png" alt="\alpha ±i\beta" width="57" height="34"> | <img class="fml" src="/formulas/d16810d5eeb1f3.png" alt="e^{\alpha x}(C_{1}\cos \beta x+C_{2}\sin \beta x)" width="208" height="34"> |

**非齐次特解（待定系数法）**：
- <img class="fml" src="/formulas/577c4d43c0b3ff.png" alt="f(x)=e^{\lambda x}P_{m}(x)" width="136" height="34"> ⇒ 设 <img class="fml" src="/formulas/9d42725d8af7c6.png" alt="y*=x^{k} e^{\lambda x}Q_{m}(x)" width="141" height="34">，`k` 是 <img class="fml" src="/formulas/da7676c04d86b3.png" alt="\lambda" width="18" height="34"> 作为特征根的重数（0/1/2）；
- <img class="fml" src="/formulas/11a35131ab2773.png" alt="f(x)=e^{\alpha x}[A \cos \beta x+B \sin \beta x]" width="249" height="34"> ⇒ 设 <img class="fml" src="/formulas/508da639f1b8d8.png" alt="y*=x^{k} e^{\alpha x}[C \cos \beta x+D \sin \beta x]" width="253" height="34">，`k` 由 <img class="fml" src="/formulas/98f88a40fc98c1.png" alt="\alpha+i\beta" width="58" height="34"> 是否为特征根决定。

::: tip 工作例题 · 三组方程


<p class="fml-block"><img class="fml" src="/formulas/06d5fd65394afa.png" alt="\begin{gathered}
(1) y&#x27;&#x27;- 3y&#x27;+2y=0 \Rightarrow r^{2}- 3r+2=0 \Rightarrow r=1,2 \Rightarrow y=C_{1}e^{x}+C_{2}e^{2x} \\
(2) y&#x27;&#x27;+4y=0 \Rightarrow r=±2i \Rightarrow y=C_{1}\cos 2x+C_{2}\sin 2x \\
(3) y&#x27;&#x27;+4y=\sin x \; \text{：设} \; y*=A \sin x \Rightarrow- A \sin x+4A \sin x= 3A \sin x= \sin x \\
\Rightarrow A=\frac{1}{3} \Rightarrow y*=\left(\frac{1}{3}\right)\sin x \; \text{，通解} \; y=C_{1}\cos 2x+C_{2}\sin 2x+\left(\frac{1}{3}\right)\sin x \\
\text{(4)} \; \text{若右端改为} \; \sin 2x \; \text{，则与齐次解共振，须设} \; \text{y*=x(A cos2x+B sin2x)}
\end{gathered}" width="603" height="159"></p>


:::

**欧拉方程** <img class="fml" src="/formulas/177a805aeb5387.png" alt="x^{2}y&#x27;&#x27;+pxy&#x27;+qy=f(x)" width="195" height="34">：令 <img class="fml" src="/formulas/54b3654cc929b5.png" alt="x=e^{t}" width="55" height="34">（即 <img class="fml" src="/formulas/4ce5a13c86d815.png" alt="t=\ln x" width="65" height="34">）化为常系数；齐次情形也可直接设 <img class="fml" src="/formulas/c18de30dbca090.png" alt="y=x^{k}" width="58" height="34"> 解指标方程。

::: danger 易错 · 微分方程
- 「齐次」一词有两义：<img class="fml" src="/formulas/02db8c6f27ed0e.png" alt="y&#x27;=\phi\left(\frac{y}{x}\right)" width="85" height="34"> 的齐次方程 ≠ 线性方程的齐次（`Q=0`），看上下文。
- 待定系数法漏乘 <img class="fml" src="/formulas/e2a88b944111e4.png" alt="x^{k}" width="25" height="34"> 是最高频失分点：只要 <img class="fml" src="/formulas/da7676c04d86b3.png" alt="\lambda" width="18" height="34"> 是特征根就必须乘。
- 可分离变量时除以 `g(y)` 会丢失 `g(y)=0` 对应的常数解，需单独补回。
- 初值问题要把常数用初始条件定出；通解中的常数个数必须等于方程阶数。
:::

### 7.3 线性微分方程解的结构

<img class="fml" src="/formulas/5256794c5b00c2.png" alt="L[y]=y^{(n)}+a_{1}(x)y^{(n-1)}+ \cdots+a_{n}(x)y" width="312" height="34"> 是**线性算子**，故：
- 齐次解集是 n 维线性空间（基 = 基本解组，朗斯基行列式 <img class="fml" src="/formulas/bd8684d15d193b.png" alt="W=0" width="59" height="34"> 判别线性无关）；
- 非齐次通解 = 齐次通解 + 任一特解；
- 叠加原理：<img class="fml" src="/formulas/e73c2717a51554.png" alt="L[y]=f_{1}+f_{2}" width="116" height="34"> 的解 = 对应两解之和。

**常数变易法**：已知齐次基本解 <img class="fml" src="/formulas/6ad0409e7de87e.png" alt="y_{1},y_{2}" width="46" height="34">，设特解 <img class="fml" src="/formulas/cda08a72adc0d9.png" alt="y*=C_{1}(x)y_{1}+C_{2}(x)y_{2}" width="191" height="34">，解方程组 <img class="fml" src="/formulas/fd788b27e38dfa.png" alt="C_{1}&#x27;y_{1}+C_{2}&#x27;y_{2}=0" width="133" height="34">、<img class="fml" src="/formulas/b6bfd2f74eff8f.png" alt="C_{1}&#x27;y_{1}&#x27;+C_{2}&#x27;y_{2}&#x27;=f" width="135" height="34">，可处理一般（非常系数）二阶方程 —— 这是待定系数法失效时的通用手段。
**幂级数解法**（选学内容）：在常点附近设 <img class="fml" src="/formulas/bd1fd3bd3338e4.png" alt="y=\sum a_{n}x^{n}" width="99" height="34"> 代入方程递推系数，是勒让德、贝塞尔方程的标准解法；欧拉公式 <img class="fml" src="/formulas/679d009ab744b6.png" alt="e^{ix}=\cos x+i \sin x" width="154" height="34"> 也由幂级数得到。

---

## 第 8 章 向量代数与空间解析几何（★★★）

### 8.1 三种向量积

![三种积、平面与直线方程](/math/math-vector.svg)

| 运算 | 定义 | 性质与用途 |
| --- | --- | --- |
| 数量积 | `a·b = |a||b|cosθ = axbx+aᵧbᵧ+a_zb_z` | 结果是**标量**；夹角 `cosθ=a·b/(|a||b|)`；投影 <img class="fml" src="/formulas/4195f87b4baf11.png" alt="Prj_{b} a= a \cdot b\vert b\vert" width="124" height="34">；垂直 ⇔ <img class="fml" src="/formulas/6bfdd027c7681c.png" alt="a \cdot b=0" width="70" height="34"> |
| 向量积 | <img class="fml" src="/formulas/9e2c479dd0a7a8.png" alt="a\times b=(a_{y}b_{z}-a_{z}b_{y},\;a_{z}b_{x}-a_{x}b_{z},\;a_{x}b_{y}-a_{y}b_{x})" width="368" height="34"> | 结果是**向量**，<img class="fml" src="/formulas/88142e0055bb98.png" alt="\bot a" width="31" height="34"> 且 <img class="fml" src="/formulas/3189d3d0283c49.png" alt="\bot b" width="28" height="34">（右手系）；<img class="fml" src="/formulas/6c6bed8c5e3a97.png" alt="\vert a \times b\vert" width="56" height="34"> = 平行四边形面积；平行 ⇔ <img class="fml" src="/formulas/80e6a16fd41791.png" alt="a \times b=0" width="79" height="34">；**反交换** <img class="fml" src="/formulas/113fa597673d23.png" alt="a \times b=- b \times a" width="122" height="34"> |
| 混合积 | <img class="fml" src="/formulas/027de2732595ef.png" alt="[a b c]=(a \times b) \cdot c" width="139" height="34">（三阶行列式） | 绝对值 = 平行六面体体积；三向量共面 ⇔ 混合积 = 0；轮换不变、对换变号 |
| 方向余弦 | <img class="fml" src="/formulas/c76afc30b63e6b.png" alt="\cos \alpha=a_{x}\vert a\vert" width="106" height="34"> 等 | <img class="fml" src="/formulas/30d95bc3a1b75a.png" alt="\cos^{2}\alpha+\cos^{2}\beta+\cos^{2}\gamma=1" width="219" height="34"> |

::: tip 工作例题 · 三种积手算
<img class="fml" src="/formulas/3c43b6df15d939.png" alt="a=(1,2,- 1)" width="110" height="34">，`b=(3,0,2)`：



<p class="fml-block"><img class="fml" src="/formulas/66564ad3ae4556.png" alt="a \cdot b= 3+ 0- 2= 1" width="164" height="34"></p>





<p class="fml-block"><img class="fml" src="/formulas/c4f3846c4802a3.png" alt="a \times b=(2 \cdot 2-(- 1) \cdot 0,(- 1) \cdot 3- 1 \cdot 2, 1 \cdot 0- 2 \cdot 3)=(4,- 5,- 6)" width="513" height="34"></p>



<img class="fml" src="/formulas/2d0e92d22a9ce3.png" alt="|a|= \sqrt{1+4+1}= \sqrt{6} \approx 2.449" width="247" height="34">；<img class="fml" src="/formulas/57c0148980d73f.png" alt="\cos \theta= \frac{1}{\sqrt{6} \cdot \sqrt{13}} \approx 0.1132" width="187" height="37">。
校验：<img class="fml" src="/formulas/e7852e850b2cf3.png" alt="(a \times b) \cdot a= 4- 10+6= 0" width="218" height="34"> 且 <img class="fml" src="/formulas/8af7249c32a9fe.png" alt="(a \times b) \cdot b= 12+0- 12= 0" width="226" height="34"> ✓（垂直于两者）。
:::

### 8.2 平面、直线与位置关系

| 对象 | 方程 | 关键量 |
| --- | --- | --- |
| 平面点法式 | <img class="fml" src="/formulas/8cd41611c0856a.png" alt="A(x- x_{0})+B(y- y_{0})+C(z- z_{0})=0" width="309" height="34"> | 法向量 `n=(A,B,C)` |
| 平面一般式 | `Ax+By+Cz+D=0` | `D=0` 过原点；缺某变量 ⇒ 平行于对应轴 |
| 直线对称式 | <img class="fml" src="/formulas/4b90d815404f57.png" alt="\frac{x- x_{0}}{m}=\frac{y- y_{0}}{n}=\frac{z- z_{0}}{p}" width="152" height="36"> | 方向向量 `s=(m,n,p)` |
| 直线参数式 | <img class="fml" src="/formulas/6ad1b1a0155789.png" alt="x=x_{0}+mt, y=y_{0}+nt, z=z_{0}+pt" width="292" height="34"> | 代入平面求交点最方便 |
| 直线一般式 | 两平面交线 | <img class="fml" src="/formulas/a54ae56d67dde6.png" alt="s= n_{1} \times n_{2}" width="97" height="34">（别把法向量当方向向量） |

**距离与夹角**：
- 点 <img class="fml" src="/formulas/054fef859b1d8a.png" alt="P_{0}" width="25" height="34"> 到平面：<img class="fml" src="/formulas/76026e77289271.png" alt="d=|Ax_{0}+By_{0}+Cz_{0}+D| \sqrt{A^{2}+B^{2}+C^{2}}" width="343" height="34">；
- 两平面夹角：`cosθ = |n1·n2|/(|n1||n2|)`（取锐角）；
- 线面夹角：`sinθ = |s·n|/(|s||n|)`；两直线夹角用 <img class="fml" src="/formulas/cb981afa47b57f.png" alt="s_{1} \cdot s_{2}" width="51" height="34">；
- 异面直线距离：<img class="fml" src="/formulas/aaa9a921536c36.png" alt="d=|[s_{1} s_{2} P_{1}P_{2}]||s_{1} \times s_{2}|" width="191" height="34">。

::: tip 工作例题 · 点到平面距离
平面 <img class="fml" src="/formulas/37a9cf9db45e1d.png" alt="2x- y+ 2z- 3= 0" width="161" height="34">，法向量 <img class="fml" src="/formulas/213ca7a70b75da.png" alt="n=(2,- 1,2)" width="112" height="34">，`|n|=3`。
点 `(0,0,0)`：<img class="fml" src="/formulas/bfde7b4ec4c2f3.png" alt="d=|- 3| 3= 1" width="122" height="34">。
（注意：点 `(1,1,1)` 满足 <img class="fml" src="/formulas/f57c01e58c5359.png" alt="2- 1+2- 3=0" width="141" height="34">，恰在平面上，距离为 0 —— 出题时容易误选此类点作例题。）
:::

**平面束**：过两平面交线的一切平面（除第二个平面本身）可写成 <img class="fml" src="/formulas/0d22847ebd77c1.png" alt="(A_{1}x+B_{1}y+C_{1}z+D_{1})+\lambda(A_{2}x+B_{2}y+C_{2}z+D_{2})=0" width="454" height="34">，求「过已知直线且满足某条件」的平面时最省力。

### 8.3 曲面与空间曲线

![二次曲面标准方程、旋转曲面与截痕法](/math/math-surface.svg)

| 曲面 | 标准方程（`a,b,c>0`） | 截痕特征 |
| --- | --- | --- |
| 椭球面 | <img class="fml" src="/formulas/69e03e575c19e8.png" alt="\frac{x^{2}}{a^{2}}+\frac{y^{2}}{b^{2}}+\frac{z^{2}}{c^{2}}=1" width="132" height="35"> | 各方向截痕为椭圆 |
| 单叶双曲面 | <img class="fml" src="/formulas/c09a97636169ed.png" alt="\frac{x^{2}}{a^{2}}+\frac{y^{2}}{b^{2}}- \frac{z^{2}}{c^{2}}=1" width="133" height="35"> | 水平截椭圆，含直线 |
| 双叶双曲面 | <img class="fml" src="/formulas/f7aeb10a0dee95.png" alt="\frac{x^{2}}{a^{2}}- \frac{y^{2}}{b^{2}}- \frac{z^{2}}{c^{2}}=1" width="132" height="35"> | 沿 x 轴分两叶 |
| 椭圆锥面 | <img class="fml" src="/formulas/a9ca0946879eaa.png" alt="\frac{x^{2}}{a^{2}}+\frac{y^{2}}{b^{2}}- \frac{z^{2}}{c^{2}}=0" width="132" height="35"> | 过原点的直线族 |
| 椭圆抛物面 | <img class="fml" src="/formulas/bfa20a079901df.png" alt="z= \frac{x^{2}}{a^{2}}+\frac{y^{2}}{b^{2}}" width="95" height="35"> | 水平截椭圆 |
| 双曲抛物面（马鞍面） | <img class="fml" src="/formulas/711f2294ec6b64.png" alt="z= \frac{x^{2}}{a^{2}}- \frac{y^{2}}{b^{2}}" width="95" height="35"> | 水平截双曲线 |
| 柱面 | 方程缺一个变量（如 <img class="fml" src="/formulas/0805a78f4651fd.png" alt="x^{2}+y^{2}=R^{2}" width="107" height="34">） | 母线平行缺失变量的轴 |
| 球面 | <img class="fml" src="/formulas/1707d9bdbcb214.png" alt="(x- x_{0})^{2}+(y- y_{0})^{2}+(z- z_{0})^{2}=R^{2}" width="301" height="34"> | — |

**旋转曲面**：`yOz` 面上 `f(y,z)=0` 绕 `z` 轴旋转 ⇒ 把 `y` 换成 <img class="fml" src="/formulas/0985f0252ca14b.png" alt="\pm\sqrt{x^{2}+y^{2}}" width="94" height="34">；绕 `y` 轴则把 `z` 换成 <img class="fml" src="/formulas/d9567f6d8758ba.png" alt="\pm\sqrt{x^{2}+z^{2}}" width="92" height="34">。
**截痕法**：用 `z=k`、`x=k`、`y=k` 的平面去截，看截痕类型随 `k` 的变化，拼出整体形状。
**空间曲线**：一般式 = 两曲面 `F=0, G=0` 交线；参数式 `x=x(t), y=y(t), z=z(t)`（如圆柱螺线 <img class="fml" src="/formulas/17384ac376e171.png" alt="x=a \cos t, y=a \sin t, z=bt" width="226" height="34">）；在 `xOy` 面的投影由「消去 z 得 `H(x,y)=0`，再与 `z=0` 联立」得到。

::: danger 易错 · 空间解析几何
- <img class="fml" src="/formulas/b6270200a68017.png" alt="a \times b" width="46" height="34"> 反交换、<img class="fml" src="/formulas/c6cd36ad6e62c2.png" alt="a \cdot b" width="37" height="34"> 交换；混合积是行列式，对换两列变号。
- 直线一般式中方向向量是两法向量的**叉积**；求线面夹角用 `sin`（不是 `cos`）。
- 曲面方程「缺变量」才是柱面；只含 <img class="fml" src="/formulas/f0c0ee88f1c9cc.png" alt="x^{2}+y^{2}" width="63" height="34"> 形式且含 <img class="fml" src="/formulas/7033d70b38ae64.png" alt="z^{2}" width="23" height="34"> 的是旋转曲面，别混。
:::

---

## 第 9 章 多元函数微分学及其应用（★★★）

### 9.1 二重极限、偏导数与全微分

![偏导数、全微分、链式法则、方向导数与梯度](/math/math-multivariable.svg)

| 概念 | 定义 / 判据 |
| --- | --- |
| 二重极限 | <img class="fml" src="/formulas/0ebe3d6afb4151.png" alt="\forall \epsilon&gt;0 \exists \delta&gt;0, 0&lt;\sqrt{(x- x_{0})^{2}+(y- y_{0})^{2}}&lt;\delta \Rightarrow\vert f- A\vert &lt;\epsilon" width="474" height="34">；要求**沿任意路径**趋于同一值 |
| 累次极限 | `lim_x lim_y f` 与 `lim_y lim_x f`；二者存在且不等 ⇒ 二重极限不存在（反之不成立） |
| 偏导数 | <img class="fml" src="/formulas/56a8557b99e61f.png" alt="f_{x}(x_{0},y_{0})=\lim \frac{f(x_{0}+h,y_{0})- f(x_{0},y_{0})}{h}" width="251" height="34">（固定其余变量） |
| 全微分 | <img class="fml" src="/formulas/4d20cd8f98ec09.png" alt="\Delta z= A\Delta x+B\Delta y+o(\rho)" width="207" height="34">，<img class="fml" src="/formulas/9f0a9b51ab6f1e.png" alt="\rho=\sqrt{\Delta x^{2}+\Delta y^{2}}" width="143" height="34"> ⇒ <img class="fml" src="/formulas/51ad508a06f4b1.png" alt="dz=f_{x}dx+f_{y}dy" width="143" height="34"> |

**关系图（二元，与一元差别很大）**：



<p class="fml-block"><img class="fml" src="/formulas/c0b61ce22ba130.png" alt="\begin{gathered}
\text{偏导数连续} \; \Rightarrow \; \text{可微} \; \Rightarrow \; \text{连续} \; \Rightarrow \; \text{二重极限存在} \\
\text{⇓ } \\
\text{偏导数存在（且各方向导数存在）} \\
\text{反例：偏导数存在但「不连续」「不可微」都成立} \; -- \; \text{与一元「可导} \; \Rightarrow \; \text{连续」截然不同}
\end{gathered}" width="706" height="111"></p>



::: danger 易错 · 多元微分
- 判定二重极限**不存在**：沿 `y=kx` 得依赖 `k` 的值，或沿 `y=x` 与 <img class="fml" src="/formulas/6dd98f6cdd0fea.png" alt="y=x^{2}" width="57" height="34"> 得不同值，即可判否。但沿有限条路径都相同**不能**判存在。
- 偏导数存在 ⇏  连续、⇏  可微；可微才保证「沿任意方向的方向导数都存在且等于 <img class="fml" src="/formulas/8de007a3857e13.png" alt="\nabla f \cdot e" width="54" height="34">」。
- 二阶混合偏导 <img class="fml" src="/formulas/5aba32fe24e23d.png" alt="f_{xy}= f_{gammax}" width="113" height="34"> 需要**连续**条件（克莱罗 / 施瓦茨定理），否则可能不等。
:::

### 9.2 复合、隐函数与几何应用

**链式法则**（先画变量关系图，"一分多合"）：
`z=f(u,v)`, `u=u(x,y)`, `v=v(x,y)` ⇒ <img class="fml" src="/formulas/51006933e5d859.png" alt="\frac{\partial z}{\partial x}= f_{u}u_{x}+f_{v}v_{x}" width="139" height="34">，<img class="fml" src="/formulas/dd416436a8cdd1.png" alt="\frac{\partial z}{\partial y}" width="25" height="36"> 同理。
**一阶全微分形式不变性**：无论 `u,v` 是自变量还是中间变量，<img class="fml" src="/formulas/e0de10c0f96d34.png" alt="dz= f_{u}du+f_{vdv}" width="136" height="34"> 形式不变（求全微分与验算都靠它）。

**隐函数求导**：`F(x,y,z)=0` ⇒ <img class="fml" src="/formulas/23a50b4a28592a.png" alt="\frac{\partial z}{\partial x}=- \frac{F_{x}}{F_{z}}" width="82" height="35">、<img class="fml" src="/formulas/92e0904e64e7c1.png" alt="\frac{\partial z}{\partial y}=- \frac{F_{y}}{F_{z}}" width="81" height="36">（<img class="fml" src="/formulas/05226f1e6b0d7e.png" alt="F_{z}=0" width="58" height="34">）；方程组 `F=G=0` 用雅可比行列式 <img class="fml" src="/formulas/3f081fe180dac9.png" alt="J= \frac{\partial(F,G)}{\partial}(u,v)= 0" width="160" height="34">，解线性方程组求各偏导。

**几何应用**：
- 曲面 `F(x,y,z)=0` 在点 <img class="fml" src="/formulas/054fef859b1d8a.png" alt="P_{0}" width="25" height="34"> 的法向量 <img class="fml" src="/formulas/0f6c7845fc6f89.png" alt="\nabla F(P_{0})" width="69" height="34">，切平面 <img class="fml" src="/formulas/18e8e692475702.png" alt="F_{x}(x- x_{0})+F_{y}(y- y_{0})+F_{z}(z- z_{0})=0" width="325" height="34">，法线 <img class="fml" src="/formulas/7688d407d352d7.png" alt="\frac{x- x_{0}}{F_{x}}= \frac{y- y_{0}}{F_{y}}= \frac{z- z_{0}}{F_{z}}" width="152" height="37">；
- 空间曲线 `r(t)=(x(t),y(t),z(t))` 的切向量 <img class="fml" src="/formulas/f22e90d866e531.png" alt="r&#x27;(t_{0})" width="47" height="34">，切线 <img class="fml" src="/formulas/c5dc715e91a954.png" alt="\frac{x-x_{0}}{x&#x27;}=\frac{y-y_{0}}{y&#x27;}=\frac{z-z_{0}}{z&#x27;}" width="152" height="36">，法平面 <img class="fml" src="/formulas/d5ac87f5892a71.png" alt="x&#x27;(x- x_{0})+y&#x27;(y- y_{0})+z&#x27;(z- z_{0})=0" width="309" height="34">。

### 9.3 方向导数、梯度与极值

**方向导数**（`f` 可微时）：<img class="fml" src="/formulas/a5c6d5d27489a9.png" alt="\frac{\partial f}{\partial l}= f_{x}\cos \alpha+f_{y}\cos \beta+f_{z} \cos \gamma= \nabla f \cdot e_{l}" width="341" height="34">。
**梯度** <img class="fml" src="/formulas/8e7258f56c4ba7.png" alt="\nabla f=(f_{x},f_{y},f_{z})" width="135" height="34">：指向函数增长最快方向，<img class="fml" src="/formulas/25a66f672692ad.png" alt="| \nabla f|" width="42" height="34"> 是最大方向导数；负梯度是下降最快方向（梯度下降算法的数学来源）；梯度与等值面正交。

::: tip 工作例题 · 方向导数
<img class="fml" src="/formulas/e243f8e99e868c.png" alt="f=x^{2}y+\sin(xy)" width="146" height="34"> ⇒ <img class="fml" src="/formulas/75dc4840ff0705.png" alt="f_{x}=2xy+y \cos(xy)" width="167" height="34">，<img class="fml" src="/formulas/4bbb0ed0fcd3ab.png" alt="f_{y}=x^{2}+x \cos(xy)" width="157" height="34">。
在 `(0,1)`：<img class="fml" src="/formulas/731642bcb24707.png" alt="\nabla f=(1, 0)" width="96" height="34">。沿 <img class="fml" src="/formulas/feafffba8e88da.png" alt="e=\left(\frac{1}{\sqrt{2}}, \frac{1}{\sqrt{2}}\right)" width="110" height="41"> 的方向导数 <img class="fml" src="/formulas/5613449a75ab7e.png" alt="= 1 \cdot\left(\frac{1}{\sqrt{2}}\right)+0= \frac{1}{\sqrt{2}} \approx 0.7071" width="239" height="41">；
最大方向导数 <img class="fml" src="/formulas/9d9101dc7b0356.png" alt="=| \nabla f|=1" width="94" height="34">（沿 x 轴正向），最小 <img class="fml" src="/formulas/83231f1c3b0900.png" alt="=- 1" width="49" height="34">（沿 x 轴负向）。
:::

![无条件极值、条件极值与拉格朗日乘数法](/math/math-extremum.svg)

| 判别 | 结论 |
| --- | --- |
| 无条件极值必要条件 | <img class="fml" src="/formulas/86a2c326067ebd.png" alt="f_{x}=f_{y}=0" width="96" height="34">（驻点）或偏导不存在点 |
| 记 <img class="fml" src="/formulas/e22cfa09277ca8.png" alt="A=f_{xx}, B=f_{xy}, C=f_{yy}" width="206" height="34">，<img class="fml" src="/formulas/d08e23b37ab082.png" alt="\Delta=AC- B^{2}" width="116" height="34"> | <img class="fml" src="/formulas/a1224bf4e91754.png" alt="\Delta&gt;0" width="55" height="34"> 且 `A<0` 极大；<img class="fml" src="/formulas/a1224bf4e91754.png" alt="\Delta&gt;0" width="55" height="34"> 且 `A>0` 极小；<img class="fml" src="/formulas/b2e13ad93929c7.png" alt="\Delta&lt;0" width="54" height="34"> 鞍点；<img class="fml" src="/formulas/4a17320a23ee6e.png" alt="\Delta=0" width="55" height="34"> 失效 |
| 海森矩阵 | 正定 ⇒ 极小、负定 ⇒ 极大、不定 ⇒ 鞍点 |
| 条件极值 | <img class="fml" src="/formulas/46e5136118ab18.png" alt="L=f+\lambda \phi" width="96" height="34">（多约束 <img class="fml" src="/formulas/1b88f2432ba638.png" alt="L=f+\sum \lambda_{i}\phi_{i}" width="129" height="34">），解 <img class="fml" src="/formulas/13073bb17f8bc4.png" alt="\nabla L=0" width="67" height="34">；几何含义 <img class="fml" src="/formulas/7386f88f6845e7.png" alt="\nabla f ∥ \nabla \phi" width="67" height="34"> |

::: tip 工作例题 · 两组极值


<p class="fml-block"><img class="fml" src="/formulas/f708a832581780.png" alt="\begin{gathered}
(1) f=x^{2}+y^{2} \; \text{在} \; \text{(0,0)} \; \text{：} \; A=C=2, B=0 \Rightarrow \Delta=4&gt;0 \; \text{且} \; A&gt;0 \Rightarrow \; \text{极小值} \; \text{0} \\
\text{f=xy} \; \text{在} \; \text{(0,0)} \; \text{：} \; A=C=0, B=1 \Rightarrow \Delta=- 1&lt;0 \Rightarrow \; \text{鞍点（不是极值点）} \\
\text{(2)} \; \text{条件极值：} \; \min x^{2}+y^{2} s.t. x+y=1 \\
L=x^{2}+y^{2}- \lambda(x+y- 1) \; \text{，} \; \frac{\partial L}{\partial x}=2x- \lambda=0, \frac{\partial L}{\partial y}=2y- \lambda=0 \Rightarrow x=y \\
\text{代入约束} \; \Rightarrow x=y=\frac{1}{2} \Rightarrow f_{\min}= \frac{1}{4}+\frac{1}{4}= \frac{1}{2} \\
(3) f=xy s.t. x^{2}+y^{2}=1 \Rightarrow \; \text{极大} \; \text{1/2} \; \text{（} \; x=y=±\frac{1}{\sqrt{2}} \; \text{）、极小} \; - \frac{1}{2}
\end{gathered}" width="633" height="217"></p>


:::

**闭区域最值流程**：① 内部驻点值；② 边界上的最值（代入边界化一元，或对边界再用拉格朗日）；③ 比较全部候选。依据是有界闭区域上连续函数必有最值（Weierstrass 定理）。

::: danger 易错 · 极值
- 驻点不一定是极值点（鞍点）；极值点也可能偏导不存在（如 <img class="fml" src="/formulas/2fddbc961196ee.png" alt="z=\sqrt{x^{2}+y^{2}}" width="114" height="34"> 在原点取极小）。
- <img class="fml" src="/formulas/4a17320a23ee6e.png" alt="\Delta=0" width="55" height="34"> 时二阶判别失效，须回到定义或看更高阶（如 <img class="fml" src="/formulas/2ac95a9016f122.png" alt="z=x^{4}+y^{4}" width="95" height="34"> 与 <img class="fml" src="/formulas/723d4c3043cb3e.png" alt="z=x^{4}- y^{4}" width="96" height="34">）。
- 拉格朗日乘数法给出的是**候选点**，<img class="fml" src="/formulas/da7676c04d86b3.png" alt="\lambda" width="18" height="34"> 本身不是所求；含不等式约束时需另查边界与 KKT 条件。
:::

**补充 · 二元泰勒与最小二乘**：二元泰勒 <img class="fml" src="/formulas/64110f5a91c301.png" alt="f(x_{0}+h,y_{0}+k)= f+(h \partial_{x}+k \partial_{y})f+ \frac{1}{2}(h \partial_{x}+k \partial_{y})^{2}f+ \cdots" width="477" height="34">，是极值充分条件的证明基础；教材「最小二乘法」一节即令残差平方和对参数偏导为零，本质是本章的无条件极值。

### 9.4 多元微分「四个概念」的反例库

| 命题 | 真伪 | 反例 / 理由 |
| --- | --- | --- |
| 偏导存在 ⇒ 连续 | 假 | <img class="fml" src="/formulas/5e7d8659ac0aa3.png" alt="f=\frac{xy}{x^{2}+y^{2}}" width="80" height="36">（(0,0) 补 0）：偏导存在但不连续 |
| 连续 ⇒ 偏导存在 | 假 | `f=|x|+|y|` |
| 各方向方向导数存在 ⇒ 可微 | 假 | 方向导数只沿直线，可微要求全增量线性逼近 |
| 偏导连续 ⇒ 可微 | 真 | 充分条件（教材标准定理） |
| 可微 ⇒ 偏导连续 | 假 | 见第 2 章 <img class="fml" src="/formulas/18c64475e69804.png" alt="x^{2} \sin\left(\frac{1}{x}\right)" width="80" height="34"> 的一元类比，二元可构造类似例子 |
| 混合偏导恒相等 | 假 | 需连续条件；经典反例 <img class="fml" src="/formulas/c8ddb0af4cabe6.png" alt="f=\frac{xy(x^{2}- y^{2})}{x^{2}+y^{2}}" width="103" height="38"> 在原点 <img class="fml" src="/formulas/b22a1a78f48cb4.png" alt="f_{xy}=f_{gammax}" width="113" height="34"> |

---

## 第 10 章 重积分（★★★）

### 10.1 二重积分

![二重/三重积分、换序与极柱球坐标](/math/math-multiple-integral.svg)

<img class="fml" src="/formulas/b586a44ee8ec86.png" alt="\iint _{D} f(x,y)d\sigma= \lim \sum f(\xi_{i},\eta_{i})\Delta \sigma_{i}" width="271" height="34">；几何上是曲顶柱体的**代数体积**（<img class="fml" src="/formulas/b0ac9a74dc6ec1.png" alt="f \ge 0" width="51" height="33"> 时为正）。

| 区域型 | 化为累次积分 |
| --- | --- |
| X 型 <img class="fml" src="/formulas/f289460da060b1.png" alt="a \le x \le b, \phi_{1}(x) \le y \le \phi_{2}(x)" width="231" height="34"> | <img class="fml" src="/formulas/fab052a8fae1c2.png" alt="\int_{a}^{b} dx \int_{\phi_{1}}^{\phi_{2}} f(x,y)dy" width="150" height="37"> |
| Y 型 <img class="fml" src="/formulas/cb3f688e06b8ed.png" alt="c \le y \le d, \psi_{1}(y) \le x \le \psi_{2}(y)" width="231" height="34"> | <img class="fml" src="/formulas/615882b79e2e5e.png" alt="\int_{c}^d dy \int_{\psi_{1}}^{\psi_{2}} f(x,y)dx" width="152" height="37"> |
| 极坐标 <img class="fml" src="/formulas/e81eb8e7fc349d.png" alt="x=r \cos \theta, y=r \sin \theta" width="174" height="34"> | <img class="fml" src="/formulas/e91c3eff04e41f.png" alt="\iint  f(r \cos \theta, r \sin \theta) \cdot r dr d\theta" width="211" height="34">（**别漏雅可比 r**） |

**交换积分次序三步**：① 由原上下限写出区域不等式并画图；② 换一个视角重写不等式；③ 若区域非简单型则**分块**。

::: tip 工作例题 · 换序与极坐标


<p class="fml-block"><img class="fml" src="/formulas/701c01620158df.png" alt="\begin{gathered}
(1) \int_{0}^{1}dx \int_{x}^{1} f(x,y)dy= \int_{0}^{1}dy \int_{0}^{y} f(x,y)dx \\
\text{（区域为} \; 0 \le x \le y \le 1 \; \text{的三角形，换序后先} \; \text{x} \; \text{后} \; \text{y} \; \text{）} \\
(2) \iint _{x^{2}+y^{2} \le a^{2}} e^{-(x^{2}+y^{2})}dxdy= \int_{0}^{2\pi}d\theta \int_{0}^{a} e^{- r^{2}} r dr \\
= 2\pi \cdot[- \frac{1}{2} e^{- r^{2}}]_{0}^{a}= \pi(1- e^{- a^{2}}) \; \text{；} \; a=1 \Rightarrow \pi(1- e^{-1}) \approx 1.9859 \\
\text{(3)} \; \text{教材经典：} \; \iint _{D} e^{- y^{2}}dxdy \; \text{（} \; \text{D} \; \text{由} \; \text{y=x, y=1, x=0} \; \text{围成）} \\
\text{先对} \; \text{y} \; \text{积分不可行（} \; e^{- y^{2}} \; \text{无初等原函数），必须换序先对} \; \text{x} \; \text{：} \\
\int_{0}^{1}dy \int_{0}^{y} e^{- y^{2}}dx= \int_{0}^{1} y e^{- y^{2}}dy= \frac{1}{2}(1- e^{-1}) \\
\text{(4)} \; \text{可分离：} \; \iint _{[a,b] \times[c,d]} g(x)h(y)dxdy=\left( \int_{a}^{b} g dx\right)\left( \int_{c}^d h dy\right) \\
\Rightarrow \iint _{[0,1]^{2}}(x+y)dxdy= \frac{1}{2}+ \frac{1}{2}= 1
\end{gathered}" width="495" height="406"></p>


:::

**对称性**（先于计算使用）：若 D 关于 y 轴对称且 `f` 对 x 为奇 ⇒ 积分为 0、为偶 ⇒ 两倍；若 D 关于 `y=x` 对称，则 <img class="fml" src="/formulas/fc5ea59c550417.png" alt="\iint _{D} f(x,y)d\sigma= \iint _{D} f(y,x)d\sigma" width="233" height="34">（轮换对称性，可把 <img class="fml" src="/formulas/defa3eb09439fc.png" alt="\iint  \frac{f(x)}{f(x)+f(y)}" width="91" height="36"> 化为面积的一半）。

### 10.2 三重积分

| 坐标 | 变换 | 体积元 | 适用区域 |
| --- | --- | --- | --- |
| 直角 | — | `dx dy dz` | 一般；投影法（先 z）/ 截面法（先 xy） |
| 柱 | <img class="fml" src="/formulas/2706e8c4ddc06c.png" alt="x=r \cos \theta, y=r \sin \theta, z=z" width="224" height="34"> | <img class="fml" src="/formulas/eb214a3acc5ede.png" alt="r dr d\theta dz" width="70" height="34"> | 旋转体、含 <img class="fml" src="/formulas/f0c0ee88f1c9cc.png" alt="x^{2}+y^{2}" width="63" height="34"> |
| 球 | <img class="fml" src="/formulas/2aa174a4daf257.png" alt="x=\rho \sin \phi \cos \theta, y=\rho \sin \phi \sin \theta, z=\rho \cos \phi" width="344" height="34"> | <img class="fml" src="/formulas/9f66e07d00e430.png" alt="\rho^{2} \sin \phi d\rho d\phi d\theta" width="118" height="34"> | 球体、锥体、含 <img class="fml" src="/formulas/4f872fcad6f607.png" alt="x^{2}+y^{2}+z^{2}" width="101" height="34"> |
| 一般换元 | `x=x(u,v,w)` 等 | `|J| du dv dw` | <img class="fml" src="/formulas/11597c7fe7f5b0.png" alt="J= \frac{\partial(x,y,z)}{\partial}(u,v,w)" width="153" height="34"> |

**φ 是与 z 轴正向的夹角**（<img class="fml" src="/formulas/3e3dd5e550cf5e.png" alt="0 \le \phi \le \pi" width="85" height="34">），<img class="fml" src="/formulas/34b3646cac66b5.png" alt="\theta \in[0,2\pi]" width="84" height="34">；常见错误是把 <img class="fml" src="/formulas/55fda307ec0e36.png" alt="\sin \phi" width="43" height="34"> 写成 <img class="fml" src="/formulas/022e5db5cfb7d3.png" alt="\cos \phi" width="44" height="34">、或把 <img class="fml" src="/formulas/e93c93e662956e.png" alt="\phi" width="18" height="34"> 当成与 `xOy` 面的夹角。

::: tip 工作例题 · 三重积分


<p class="fml-block"><img class="fml" src="/formulas/60459058627495.png" alt="\begin{gathered}
(1) \iiint _{x^{2}+y^{2}+z^{2} \le R^{2}} 1 dV= \frac{4\pi R^{3}}{3} \; \text{（} \; R=1 \Rightarrow \frac{4\pi}{3} \approx 4.18879 \; \text{）} \\
\text{(2) 上半球} \; \iiint_{\Omega} z\,dV \; (\Omega: x^{2}+y^{2}+z^{2}\le 1,\, z\ge 0) \\
= \int_{0}^{2\pi}d\theta \int_{0}^{\frac{\pi}{2}}\sin \phi \cos \phi d\phi \int_{0}^{1} \rho^{3} d\rho \\
= 2\pi \cdot\left(\frac{1}{2}\right) \cdot\left(\frac{1}{4}\right)= \frac{\pi}{4} \approx 0.785398 \\
(3) \iiint _\Omega(x^{2}+y^{2}) dV \; \text{（} \; \Omega \; \text{为圆柱} \; x^{2}+y^{2} \le 1, 0 \le z \le 1 \; \text{），柱坐标：} \\
\int_{0}^{2\pi}d\theta \int_{0}^{1} r^{3} dr \int_{0}^{1} dz= 2\pi \cdot \frac{1}{4}= \frac{\pi}{2}
\end{gathered}" width="542" height="293"></p>


:::

**应用**：曲面面积 <img class="fml" src="/formulas/2a34b400ce1ec0.png" alt="A= \iint _{D_{xy}} \sqrt{1+z_{x}^{2}+z_{y}^{2}} dxdy" width="225" height="42">（`z=z(x,y)`）；平面薄片质量 <img class="fml" src="/formulas/ad2d676d05d8ec.png" alt="M=\iint \rho d\sigma" width="100" height="34">、质心 <img class="fml" src="/formulas/175534b74d9c85.png" alt="\bar{x}=\iint x\rho \frac{d\sigma}{M}" width="100" height="34">、转动惯量 <img class="fml" src="/formulas/3d54817c400e2e.png" alt="I_{z}=\iint (x^{2}+y^{2})\rho d\sigma" width="163" height="34">；万有引力按分量积分。

::: danger 易错 · 重积分
- 换序/换元后**上下限与雅可比必须同步改**；极坐标漏 `r`、球坐标漏 <img class="fml" src="/formulas/c3e877466aa74e.png" alt="\rho^{2}\sin \phi" width="62" height="34"> 最常见。
- 二重积分中值定理 <img class="fml" src="/formulas/6a596e92561838.png" alt="\iint _{D} f d\sigma= f(\xi,\eta) \cdot Area(D)" width="223" height="34"> 要求 `f` 连续、`D` 闭连通。
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
| 第一类（对弧长） | <img class="fml" src="/formulas/4d8b2a74549af7.png" alt="\int_{L} f(x,y,z)ds" width="115" height="34"> | 无关 | 参数化后代 <img class="fml" src="/formulas/eeb175abde1fe3.png" alt="ds=\sqrt{\dot{x}^{2}+\dot{y}^{2}+\dot{z}^{2}}dt" width="175" height="34">；下限须小于上限 |
| 第二类（对坐标） | <img class="fml" src="/formulas/b2cb4a39222a60.png" alt="\int_{L} Pdx+Qdy+Rdz" width="170" height="34"> | **有关**（反向变号） | 代入参数方程，起终点决定上下限（可上大下小） |
| 第一类面积分 | <img class="fml" src="/formulas/8bdc92fcb173f1.png" alt="\iint _{\Sigma} f dS" width="67" height="34"> | 无关（无方向） | 投影 + <img class="fml" src="/formulas/cbeb5bedab682f.png" alt="dS= \sqrt{1+z_{x}^{2}+z_{y}^{2}}dxdy" width="193" height="42"> |
| 第二类面积分 | <img class="fml" src="/formulas/0e15069601daa9.png" alt="\iint _{\Sigma} P dydz+Q dzdx+R dxdy" width="233" height="34"> | **与侧有关** | 投影到相应坐标面并按侧定正负；或合一投影法 |

**两类之间的联系**：<img class="fml" src="/formulas/6be6b8dfa4ac06.png" alt="\int Pdx+Qdy= \int(P \cos \alpha+Q \cos \beta)ds" width="309" height="34">；<img class="fml" src="/formulas/c3eacc8a013429.png" alt="\iint P dydz+Q dzdx+R dxdy= \iint (P \cos \alpha+Q \cos \beta+R \cos \gamma)dS" width="511" height="34">，其中 <img class="fml" src="/formulas/511a02a26e2201.png" alt="(\cos \alpha, \cos \beta, \cos \gamma)" width="150" height="34"> 是切向/法向的方向余弦。

### 11.2 三大公式

| 公式 | 表达式 | 条件 |
| --- | --- | --- |
| **格林** | <img class="fml" src="/formulas/c5884e71a0e764.png" alt="\oint _{L} Pdx+Qdy= \iint _{D}\left( \frac{\partial Q}{\partial x}- \frac{\partial P}{\partial y}\right)dxdy" width="296" height="41"> | `L` 为正向（逆时针）分段光滑闭曲线，`P,Q` 在 `D` 上有一阶连续偏导 |
| **高斯** | <img class="fml" src="/formulas/250750a7da3a2b.png" alt="\oiint _{\Sigma} P dydz+Q dzdx+R dxdy= \iiint _\Omega\left( \frac{\partial P}{\partial x}+ \frac{\partial Q}{\partial y}+ \frac{\partial R}{\partial z}\right)dV" width="446" height="41"> | <img class="fml" src="/formulas/e44ebcebe1d93c.png" alt="\sum" width="26" height="34"> 取**外侧**闭曲面 |
| **斯托克斯** | <img class="fml" src="/formulas/49f0cf7af3f1a3.png" alt="\oint _\Gamma Pdx+Qdy+Rdz= \iint _{\Sigma}(rot A) \cdot n dS" width="313" height="34"> | <img class="fml" src="/formulas/8f84e38c1baea5.png" alt="\Gamma" width="18" height="34"> 与 <img class="fml" src="/formulas/e44ebcebe1d93c.png" alt="\sum" width="26" height="34"> 的侧符合右手规则 |

**统一视角**：三者都是「**边界上的积分 = 内部某种导数的积分**」，即广义斯托克斯定理 <img class="fml" src="/formulas/520279308c2be5.png" alt="\int_{\partial M} \omega= \int_{M} d\omega" width="122" height="34">；牛顿–莱布尼茨是它在区间 `[a,b]` 上的 1 维特例。

**路径无关与全微分求积**（单连通域内等价）：
<img class="fml" src="/formulas/e42d7c24b4a713.png" alt="\frac{\partial P}{\partial y}= \frac{\partial Q}{\partial x}" width="74" height="36"> ⇔ <img class="fml" src="/formulas/4ebc5882e39834.png" alt="\oint _{L} Pdx+Qdy= 0" width="149" height="34">（任意闭路）⇔ 积分与路径无关 ⇔ `Pdx+Qdy` 是某 `u(x,y)` 的全微分，且 <img class="fml" src="/formulas/31b3b7f43215eb.png" alt="u(x,y)= \int_{(x_{0},y_{0})}^{(x,y)} Pdx+Qdy" width="220" height="38">（沿折线计算）。

**散度与旋度**：<img class="fml" src="/formulas/c0b8fa473dae3e.png" alt="div A= \frac{\partial P}{\partial x}+ \frac{\partial Q}{\partial y}+ \frac{\partial R}{\partial z}" width="176" height="36">（标量，通量源强度）；<img class="fml" src="/formulas/c8c172bfeacdc3.png" alt="rot A= \nabla \times A" width="118" height="34">（向量，环流强度）；<img class="fml" src="/formulas/ae59eb3d69b940.png" alt="\nabla\left(\frac{1}{r}\right)" width="52" height="34">、<img class="fml" src="/formulas/f444c4732a816c.png" alt="\nabla \cdot\left(\frac{r}{r^{3}}\right)" width="67" height="34"> 等恒等式在场论中常用。

::: tip 工作例题 · 三大公式


<p class="fml-block"><img class="fml" src="/formulas/2f7fcce76f23a2.png" alt="\begin{gathered}
\text{(1)} \; \text{格林求面积：取} \; P=- \frac{y}{2}, Q=\frac{x}{2} \Rightarrow \oint_{L}\dfrac{x\,dy-y\,dx}{2}= Area(D) \\
\Rightarrow \; \text{单位圆上} \; \oint  x dy- y dx= 2\pi \approx 6.28319 \\
\text{(2)} \; \text{奇点陷阱：} \; \oint_{L}\dfrac{x\,dy-y\,dx}{x^{2}+y^{2}} = 2\pi \\
\text{此处} \; \text{P,Q} \; \text{在原点无定义，不能直接套格林（会错得} \; \text{0} \; \text{）；} \\
\text{须挖去以原点为心的小圆} \; \epsilon \; \text{，在环形域用格林（旋度为} \; \text{0} \; \text{）} \; \Rightarrow \; \text{等于小圆上的积分} \; 2\pi \\
\text{(3)} \; \text{高斯：} \; \oiint _{S} x dydz+y dzdx+z dxdy= \iiint _\Omega 3 dV= 3V \\
\text{单位球} \; V=\frac{4\pi}{3} \Rightarrow 4\pi \approx 12.56637 \\
\text{(4) div(x,y,z)=3} \; \text{；} \; rot(- y,x,0)=(0,0,2) \; \text{；} \; \nabla(x^{2}+y^{2}+z^{2})=(2x,2y,2z)
\end{gathered}" width="676" height="308"></p>


:::

::: danger 易错 · 三大公式
- 非闭曲线要**补线**成闭、非闭曲面要**补面**成闭，补上的部分最后要减掉。
- 区域含奇点（分母为零、偏导不连续）必须**挖洞**，否则格林/高斯结论错误。
- 方向：格林逆时针为正、高斯外侧为正、斯托克斯与法向满足右手规则；取反则整体变号。
- 第一类积分与方向无关且可用对称性；第二类积分与方向/侧有关，先定向再计算。
:::

**补充 · 场论术语**：通量 <img class="fml" src="/formulas/8de0a4be0ef010.png" alt="\Phi=\iint _{\Sigma} A \cdot n dS" width="130" height="34">（高斯：通量 = 散度的体积分）；环流量 <img class="fml" src="/formulas/11e78c1bd5356b.png" alt="\Gamma=\oint _\Gamma A \cdot dl" width="103" height="34">（斯托克斯：环流量 = 旋度通量）；<img class="fml" src="/formulas/bebd4840817904.png" alt="div A \equiv 0" width="78" height="34"> 称无源场（沿任意闭曲面的通量为零），<img class="fml" src="/formulas/be7237e6c0f727.png" alt="rot A \equiv 0" width="77" height="34"> 且在单连通域内称无旋场/保守场（存在势函数）。梯度场必无旋，无旋场在单连通域内必为梯度场。

### 11.3 三大公式的统一形式与场论恒等式

广义斯托克斯定理 <img class="fml" src="/formulas/520279308c2be5.png" alt="\int_{\partial M} \omega= \int_{M} d\omega" width="122" height="34"> 在外微分语言下统一：
- `n=1`：牛顿–莱布尼茨（<img class="fml" src="/formulas/a08cfb321e5219.png" alt="\int_{[a,b]} dF= F(b)- F(a)" width="183" height="36">）；
- `n=2`：格林公式（平面区域边界是曲线）；
- `n=3`：高斯（体边界是闭曲面）、斯托克斯（曲面边界是闭曲线）——取决于取 2-形式还是 1-形式。

**常用场论恒等式**：<img class="fml" src="/formulas/a190fe1d7958ab.png" alt="\nabla \times( \nabla f)=0" width="116" height="34">（梯度场无旋）；<img class="fml" src="/formulas/3460fa1fcb5db2.png" alt="\nabla \cdot( \nabla \times A)=0" width="131" height="34">（旋度场无源）；<img class="fml" src="/formulas/9d97a63c612871.png" alt="\nabla \cdot(f A)= \nabla f \cdot A+f \nabla \cdot A" width="222" height="34">；<img class="fml" src="/formulas/88719f385125a9.png" alt="\nabla^{2}f= \nabla \cdot( \nabla f)" width="131" height="34">（拉普拉斯算子）。这些是电磁学、流体力学方程的语言基础。

---

## 第 12 章 无穷级数（★★★）

### 12.1 常数项级数

![判敛决策树、幂级数与傅里叶级数](/math/math-series.svg)

<img class="fml" src="/formulas/f146c73d423019.png" alt="\sum u_{n}" width="47" height="34"> 收敛 ⇔ 部分和序列 <img class="fml" src="/formulas/e8d0197997fcc7.png" alt="S_{n}= \sum_{k=1}^{n} u_{k}" width="114" height="34"> 收敛。**必要条件**：<img class="fml" src="/formulas/67113015399642.png" alt="\lim u_{n}= 0" width="86" height="34">（不满足立即发散；满足未必收敛，如调和级数）。

| 类型 | 审敛法 | 判据 |
| --- | --- | --- |
| 正项 | 比较 / 极限比较 | 与 <img class="fml" src="/formulas/619d063f40addd.png" alt="\sum\frac{1}{n^{p}}" width="46" height="34">（`p>1` 收敛）、几何级数 <img class="fml" src="/formulas/9c1504b6aa06f9.png" alt="\sum q^{n}" width="46" height="34">（`|q|<1` 收敛）比 |
| 正项 | 比值（达朗贝尔） | <img class="fml" src="/formulas/3510355471c888.png" alt="\rho=\lim \frac{u_{n+1}}{u_{n}}" width="97" height="35">：<img class="fml" src="/formulas/c66c05cf32fc3f.png" alt="\rho&lt;1" width="49" height="34"> 收敛、<img class="fml" src="/formulas/d12b13f3b62ee3.png" alt="\rho&gt;1" width="49" height="34"> 发散、`=1` 失效 |
| 正项 | 根值（柯西） | <img class="fml" src="/formulas/1927bb92b4771c.png" alt="\rho=\lim_{n\to\infty}\sqrt[n]{u_{n}}" width="135" height="34">，同上 |
| 正项 | 积分判别 | <img class="fml" src="/formulas/bed3fbf92e4703.png" alt="u_{n}=f(n)" width="85" height="34">，`f` 正递减 ⇒ <img class="fml" src="/formulas/f146c73d423019.png" alt="\sum u_{n}" width="47" height="34"> 与 <img class="fml" src="/formulas/e1ff93ba7a2532.png" alt="\int_{1}^\infty f(x)dx" width="90" height="33"> 同敛散 |
| 交错 | 莱布尼茨 | <img class="fml" src="/formulas/0599e563734b20.png" alt="u_{n}" width="25" height="34"> 单调递减且趋于 0 ⇒ 收敛，余项 <img class="fml" src="/formulas/a1f6a72e650c0d.png" alt="\vert r_{n}\vert  \le u_{n+1}" width="92" height="34"> |
| 一般 | 绝对收敛 | <img class="fml" src="/formulas/70aa7e08807578.png" alt="\sum\vert u_{n}\vert" width="57" height="34"> 收敛 ⇒ <img class="fml" src="/formulas/f146c73d423019.png" alt="\sum u_{n}" width="47" height="34"> 收敛；反之称条件收敛 |

**收敛级数的性质**：可逐项加减、乘常数、任意加括号；**绝对收敛可任意重排且和不变**，条件收敛重排可改变和甚至发散（黎曼重排定理）。

::: tip 工作例题 · 五个经典级数


<p class="fml-block"><img class="fml" src="/formulas/69ff47cd457511.png" alt="\begin{gathered}
\text{(1)} \; \text{几何级数} \; \sum_{n=0}^\infty q^{n}= \frac{1}{1- q} \; \text{（} \; \text{|q|&lt;1} \; \text{）；} \; |q| \ge 1 \; \text{发散} \\
\text{(2) p} \; \text{级数} \; \sum\frac{1}{n^{p}} \; \text{：} \; \text{p&gt;1} \; \text{收敛、} \; p \le 1 \; \text{发散；} \; \sum\frac{1}{n} \; \text{发散（调和级数）} \\
\text{(3)} \; \text{裂项} \; \sum_{n=1}^\infty \frac{1}{n(n+1)}= \sum\left(\frac{1}{n}- \frac{1}{n+1}\right)= 1 \\
\text{(4)} \; \text{交错调和} \; \sum\frac{(-1)^{n+1}}{n}= \ln 2 \approx 0.693147 \; \text{（条件收敛）} \\
(5) \sum\frac{(-1)^{n+1}}{n^{2}}= \frac{\pi^{2}}{12} \approx 0.822467 \; \text{（绝对收敛）}
\end{gathered}" width="568" height="248"></p>


:::

### 12.2 幂级数与函数展开

<img class="fml" src="/formulas/6d98934117308e.png" alt="\sum a_{n}(x- x_{0})^{n}" width="118" height="34"> 的**收敛半径** <img class="fml" src="/formulas/4bc23f1fc06cd1.png" alt="R= \lim|\frac{a_{n}}{a_{n+1}}|" width="111" height="36"> 或 <img class="fml" src="/formulas/ae68bd88240c88.png" alt="R=\frac{1}{\limsup_{n\to\infty}\sqrt[n]{|a_{n}|}}" width="150" height="42">；收敛区间 <img class="fml" src="/formulas/401e95ac16da28.png" alt="(x_{0}- R, x_{0}+R)" width="135" height="34">，**端点必须单独判断**才得收敛域。

| 性质 | 内容 |
| --- | --- |
| 阿贝尔定理 | 在收敛区间内闭一致收敛；和函数在收敛区间内连续 |
| 逐项运算 | 可逐项求导、逐项积分，**收敛半径不变**（端点收敛性可能改变） |
| 和函数求法 | 逐项求导/积分化为几何级数求和，再积分/求导还原；注意 `S(0)` 定常数 |

::: tip 工作例题 · 和函数


<p class="fml-block"><img class="fml" src="/formulas/80cd2a31b3fb6a.png" alt="\begin{gathered}
\sum_{n=0}^\infty x^{n}= \frac{1}{1- x},|x|&lt;1 \\
\text{逐项求导：} \; \sum_{n=1}^\infty n x^{n- 1}= \frac{1}{(1- x)^{2}} \\
\text{两边乘} \; \text{x} \; \text{：} \; \sum_{n=1}^\infty n x^{n}= \frac{x}{(1- x)^{2}} \\
\text{验算} \; x=\frac{1}{2} \; \text{：右侧} \; = \frac{0.5}{0.25}= 2 \; \text{；前} \; \text{50} \; \text{项部分和} \; \text{= 2.0000 }\checkmark \\
\sum_{n=1}^\infty \frac{x^{n}}{n}=- \ln(1- x),- 1 \le x&lt;1 \\
\text{（由} \; \int_{0}\frac{^{x} 1}{(1- t)dt} \; \text{逐项积分得到；端点} \; x=- 1 \; \text{收敛、} \; \text{x=1} \; \text{发散）}
\end{gathered}" width="524" height="321"></p>


:::

**五个麦克劳林展开**（见第 1.3 节表），收敛域分别为：
<img class="fml" src="/formulas/23413ccd73e8be.png" alt="e^{x}" width="24" height="33">、`sin x`、`cos x` 为 <img class="fml" src="/formulas/0a088aa2567698.png" alt="(- \infty,+ \infty)" width="92" height="34">；`ln(1+x)` 为 `(−1,1]`；<img class="fml" src="/formulas/76c1f942f49b3f.png" alt="(1+x)^\alpha" width="71" height="33"> 依赖 α，一般 <img class="fml" src="/formulas/144fa95193174c.png" alt="(- 1,1)" width="61" height="34">。

**补充 · 一致收敛**：函数项级数 <img class="fml" src="/formulas/eec92032697c05.png" alt="\sum u_{n}(x)" width="71" height="34"> 的一致收敛性（魏尔斯特拉斯 M 判别法：<img class="fml" src="/formulas/6e8bd63eec5eff.png" alt="|u_{n}(x)| \le M_{n}" width="109" height="34"> 且 <img class="fml" src="/formulas/a81e36f9ba95d0.png" alt="\sum M_{n}" width="55" height="34"> 收敛）保证和函数连续、可逐项积分与逐项求导（还需导函数一致收敛）。这解释「为何幂级数能在收敛区间内任意逐项运算」，教材把它列为选学但逻辑上不可缺。

### 12.3 傅里叶级数

周期为 <img class="fml" src="/formulas/e5d3bd790b4d66.png" alt="2\pi" width="27" height="33"> 的函数：



<p class="fml-block"><img class="fml" src="/formulas/cb6349577d2653.png" alt="\frac{f(x) \sim a_{0}}{2}+ \sum_{n=1}^\infty(a_{n} \cos nx+ b_{n} \sin nx)" width="291" height="34"></p>



<img class="fml" src="/formulas/6e6f60f0fa0783.png" alt="a_{n}=\left(\frac{1}{\pi}\right) \int_{- \pi}^{\pi} f(x)\cos nx dx" width="215" height="35">，<img class="fml" src="/formulas/4614d3cdbfb7a8.png" alt="b_{n}=\left(\frac{1}{\pi}\right) \int_{- \pi}^{\pi} f(x)\sin nx dx" width="211" height="35">。

**狄利克雷收敛定理**（教材核心）：若 `f` 在一个周期上连续或只有有限个第一类间断点，且只有有限个极值点，则级数收敛，且
- 在连续点收敛于 `f(x)`；
- 在间断点收敛于 <img class="fml" src="/formulas/d83368e72257fe.png" alt="\frac{f(x^{-})+f(x^{+})}{2}" width="85" height="35">；
- 在端点 <img class="fml" src="/formulas/a91d92d87ea0ab.png" alt="±\pi" width="32" height="34"> 收敛于 <img class="fml" src="/formulas/dbfd99c7f2440b.png" alt="\frac{f(- \pi^{+})+f(\pi^{-})}{2}" width="96" height="35">。

| 情形 | 展开形式 |
| --- | --- |
| `f` 奇（<img class="fml" src="/formulas/1f0bae7bef1700.png" alt="- \pi,\pi" width="50" height="34">） | 正弦级数，只含 <img class="fml" src="/formulas/048e288d9b08b5.png" alt="b_{n}" width="23" height="34">（<img class="fml" src="/formulas/8423b80ff569de.png" alt="f(x)=x \Rightarrow x= 2\sum(- 1)^{n+1} \sin \frac{nx}{n}" width="276" height="34">） |
| `f` 偶（<img class="fml" src="/formulas/1f0bae7bef1700.png" alt="- \pi,\pi" width="50" height="34">） | 余弦级数，只含 <img class="fml" src="/formulas/1c6cb586f29f57.png" alt="a_{n}" width="25" height="34">（<img class="fml" src="/formulas/eacf55bbbeb44b.png" alt="f(x)=\vert x\vert  \Rightarrow\vert x\vert = \frac{\pi}{2}-\left(\frac{4}{\pi}\right)\sum \frac{\cos(2k- 1)x}{(2k- 1)^{2}}" width="311" height="36">） |
| <img class="fml" src="/formulas/cc7cdbf17cc3cb.png" alt="[0,\pi]" width="45" height="34"> 上给定 | 作奇延拓得正弦级数、偶延拓得余弦级数 |
| 周期 `2l` | 把 `nx` 换成 <img class="fml" src="/formulas/118b4c4a326057.png" alt="\frac{n\pi x}{l}" width="34" height="34">，系数中 <img class="fml" src="/formulas/68babd24e5e7f4.png" alt="\frac{1}{\pi}" width="18" height="34"> 换 `1/l` |

::: tip 工作例题 · 用傅里叶级数求数项级数的和


<p class="fml-block"><img class="fml" src="/formulas/5503fd3138580f.png" alt="\begin{gathered}
x= 2\sum_{n=1}^\infty \frac{(- 1)^{n+1} \sin(nx)}{n}, x \in(- \pi,\pi) \\
\text{取} \; x=\frac{\pi}{2} \; \text{：} \; \frac{\pi}{2}= 2\left(1- \frac{1}{3}+ \frac{1}{5}- \frac{1}{7}+ \cdots\right) \\
\Rightarrow 1- \frac{1}{3}+ \frac{1}{5}- \cdots= \frac{\pi}{4} \approx 0.785398 \; \text{（莱布尼茨级数）} \\
|x|= \frac{\pi}{2}-\left(\frac{4}{\pi}\right)\sum_{k=1}^\infty \frac{\cos((2k- 1)x)}{(2k- 1)^{2}}, x \in[- \pi,\pi] \\
\text{取} \; \text{x=0} \; \text{：} \; 0= \frac{\pi}{2}- \frac{\left(\frac{4}{\pi}\right)\sum 1}{(2k- 1)^{2}} \Rightarrow \sum\frac{1}{(2k-1)^{2}}=\frac{\pi^{2}}{8}
\end{gathered}" width="430" height="259"></p>


:::

::: danger 易错 · 级数
- <img class="fml" src="/formulas/67113015399642.png" alt="\lim u_{n}= 0" width="86" height="34"> 只是**必要**条件；调和级数是最经典反例。
- 比值/根值法 <img class="fml" src="/formulas/71f55b31ab0f91.png" alt="\rho=1" width="49" height="34"> 时**失效**，必须换比较、积分或拉比/高斯判别法（如 <img class="fml" src="/formulas/3b869ac1188e0e.png" alt="\sum\frac{1}{n}" width="40" height="34">、<img class="fml" src="/formulas/fee8346edec651.png" alt="\sum\frac{1}{n^{2}}" width="46" height="34"> 都是 <img class="fml" src="/formulas/71f55b31ab0f91.png" alt="\rho=1" width="49" height="34"> 但敛散不同）。
- 交错级数用莱布尼茨判收敛，但**绝对收敛性要另判** <img class="fml" src="/formulas/d0460b51c5e149.png" alt="\sum|u_{n}|" width="58" height="34">；「收敛」与「绝对收敛」不可混。
- 逐项求导/积分后收敛半径不变，但**端点**可能从收敛变发散（如 <img class="fml" src="/formulas/86dde35d3b56ab.png" alt="\sum\frac{x^{n}}{n}" width="46" height="34"> 与 <img class="fml" src="/formulas/9e3e3b310fdebe.png" alt="\sum x^{n-1}" width="64" height="34">），必须重新检验。
- 傅里叶级数在间断点收敛到左右极限的平均值，**不是** `f(x)`；端点同理。
:::

### 12.4 级数判敛法的强弱排序



<p class="fml-block"><img class="fml" src="/formulas/cea0d9e4f62514.png" alt="\begin{gathered}
\text{必要条件（通项} \; \to 0 \; \text{）} \; \to \; \text{正项：比较} \; \text{/} \; \text{极限比较（最基础）} \\
\to \; \text{比值} \; \text{/} \; \text{根值（对阶乘、指数型最有效；} \; \rho=1 \; \text{失效）} \\
\to \; \text{积分判别、拉比判别、高斯判别（对} \; \rho=1 \; \text{的临界情形）} \\
\text{交错：莱布尼茨（收敛）} \; \to \; \text{再看} \; \sum|u_{n}| \; \text{（绝对} \; \text{or} \; \text{条件）}
\end{gathered}" width="503" height="118"></p>


**根值强于比值**：由 <img class="fml" src="/formulas/e7d369a76f902a.png" alt="\lim \frac{u_{n+1}}{u_{n}}= \rho \Rightarrow \lim_{n\to\infty}\sqrt[n]{u_{n}}= \rho" width="252" height="35">，反之不然；故含 `n` 次幂的项优先用根值。
**阿贝尔 / 狄利克雷判别法**：处理 <img class="fml" src="/formulas/64cb2953ee6d67.png" alt="\sum a_{n}b_{n}" width="63" height="34"> 型，若 <img class="fml" src="/formulas/57b737405be82c.png" alt="\sum a_{n}" width="46" height="34"> 部分和有界且 <img class="fml" src="/formulas/048e288d9b08b5.png" alt="b_{n}" width="23" height="34"> 单调趋于 0 ⇒ 收敛（狄利克雷）；这解释了交错级数判别的一般原理。

::: tip 补充 · 积分判别的两个经典临界例
<img class="fml" src="/formulas/b36c338dafd5ba.png" alt="\sum \frac{1}{n \ln n}" width="64" height="34"> 与 <img class="fml" src="/formulas/18baab17fe911e.png" alt="\sum \frac{1}{n(\ln n)^{2}}" width="76" height="36"> 都是比值/根值 <img class="fml" src="/formulas/71f55b31ab0f91.png" alt="\rho=1" width="49" height="34"> 失效、比较判别也难处理的临界级数，用积分判别（换元 <img class="fml" src="/formulas/48560f363607ec.png" alt="u=\ln x" width="69" height="34">）：
<img class="fml" src="/formulas/54ad9b53e544d1.png" alt="\int_{2}^\infty \frac{dx}{x \ln x}=[\ln \ln x]_{2}^\infty= \infty" width="204" height="34"> ⇒ **发散**；
<img class="fml" src="/formulas/69216b18208b86.png" alt="\int_{2}^\infty \frac{dx}{x(\ln x)^{2}}=[- \frac{1}{\ln} x]_{2}^\infty= \frac{1}{\ln} 2" width="215" height="36"> ⇒ **收敛**。
记忆规律：分母每多套一层「收敛得更快」的因子（`ln n` → <img class="fml" src="/formulas/19781ec1d94cfc.png" alt="(\ln n)^{2}" width="56" height="34">），敛散性就可能翻转——这是判断题最爱考的边界情形。
:::

### 12.5 傅里叶级数与幂级数的对照

| 维度 | 幂级数 | 傅里叶级数 |
| --- | --- | --- |
| 基函数 | <img class="fml" src="/formulas/f1c63ffabd4d3a.png" alt="1, x, x^{2}, \cdots" width="89" height="34">（幂函数） | `1, cos nx, sin nx`（三角函数，正交系） |
| 系数来源 | 泰勒系数 <img class="fml" src="/formulas/16fe2576bc5aa9.png" alt="\frac{f^{(n)}(0)}{n}!" width="53" height="37">（局部信息） | 积分 <img class="fml" src="/formulas/7e5696aec2d508.png" alt="a_{n}, b_{n}" width="48" height="34">（**整体**信息，用正交性） |
| 收敛要求 | 函数解析 + 余项→0 | 狄利克雷条件（分段光滑，允许间断） |
| 适用范围 | 只能展开光滑解析函数 | 可展开有跳跃间断的周期函数 |
| 端点 | 收敛域端点单独判 | 间断点收敛到左右极限平均 |

**帕塞瓦尔等式**：<img class="fml" src="/formulas/c9055c11832039.png" alt="\left(\frac{1}{\pi}\right) \int_{- \pi}^{\pi} f^{2} dx= \frac{a_{0}^{2}}{2}+ \sum(a_{n}^{2}+b_{n}^{2})" width="256" height="36">，是「能量守恒」在频域的表述，也是求 <img class="fml" src="/formulas/b8e1e8668fede9.png" alt="\sum\frac{1}{n^{4}}=\frac{\pi^{4}}{90}" width="87" height="34"> 一类级数和的工具。

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
- 机器学习里的「梯度」是多元函数的 <img class="fml" src="/formulas/642a8e1c877b45.png" alt="\nabla f" width="32" height="34">，但损失函数的可微性（ReLU、hinge）并非处处成立，需要次梯度；
- 概率密度积分要求 <img class="fml" src="/formulas/02e84cbf7b7908.png" alt="\int f= 1" width="66" height="34">，这与「反常积分收敛」是同一套判敛工具。
:::

---

## 典型计算题逐步演算（可照抄的解题格式）

> 每道题按「识别类型 → 选方法 → 逐步演算 → 验算」四步展开，代码块内是考场可直接复用的书写格式。

### 演 1 · 极限（七类未定式）· 第 1 章



<p class="fml-block"><img class="fml" src="/formulas/328a1eb1c95875.png" alt="\begin{gathered}
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
\end{gathered}" width="609" height="486"></p>



### 演 2 · 导数（分段点与隐函数）· 第 2 章



<p class="fml-block"><img class="fml" src="/formulas/4325d58ca6f2c9.png" alt="\begin{gathered}
(1) f(x)=x^{2} \sin\left(\frac{1}{x}\right)(x=0), f(0)=0 \; \text{，求} \; \text{f′(0)} \\
\text{定义：} \; f&#x27;(0)=\lim_{x \to 0}\frac{x^{2} \sin\left(\frac{1}{x}\right)- 0}{x}= \lim x \sin\left(\frac{1}{x}\right)= 0 \; \text{（有界} \; \times \; \text{无穷小）} \\
\text{但} \; x=0 \; \text{时} \; f&#x27;(x)=2x \sin\left(\frac{1}{x}\right)- \cos\left(\frac{1}{x}\right) \; \text{，} \; x \to 0 \; \text{无极限} \; \Rightarrow f&#x27; \; \text{在} \; \text{0} \; \text{不连续} \\
(2) x^{2}+ y^{2}= 1 \; \text{求} \; \text{dy/dx} \; \text{与} \; \frac{d^{2}y}{dx^{2}} \\
\text{隐函数：} \; 2x+ 2y y&#x27;= 0 \Rightarrow y&#x27;=- \frac{x}{y} \\
\text{再求导：} \; y&#x27;&#x27;=- \frac{y- x y&#x27;}{y^{2}}=- \frac{y+ \frac{x^{2}}{y}}{y^{2}}=- \frac{x^{2}+y^{2}}{y^{3}}=- \frac{1}{y^{3}} \\
(3) y= x^{x} \Rightarrow \ln y= x \ln x \Rightarrow y&#x27;= y(\ln x+ 1)= x^{x}(\ln x+ 1)
\end{gathered}" width="619" height="318"></p>



### 演 3 · 中值定理与极值 · 第 3 章



<p class="fml-block"><img class="fml" src="/formulas/439b38c50d974e.png" alt="\begin{gathered}
\text{题：证明} \; f(x)=x^{3}- 3x \; \text{在} \; \text{[0,1]} \; \text{上满足拉格朗日定理，并求} \; \xi \; \text{。} \\
\text{(1)} \; \text{验证：多项式在} \; \text{[0,1]} \; \text{连续、} \; \text{(0,1)} \; \text{可导} \; \checkmark \\
(2) f(1)=- 2, f(0)=0 \Rightarrow \frac{f(1)- f(0)}{1- 0}=- 2 \\
(3) f&#x27;(x)=3x^{2}- 3=- 2 \Rightarrow 3x^{2}=1 \Rightarrow x=\frac{1}{\sqrt{3}} \in(0,1) \checkmark \Rightarrow \xi=\frac{1}{\sqrt{3}} \\
\text{题：求} \; f(x)=x^{3}- 3x^{2}+1 \; \text{的单调区间、极值与拐点。} \\
(1) f&#x27;=3x^{2}- 6x=3x(x- 2) \; \text{，驻点} \; \text{x=0,2} \\
\text{(2)} \; \text{区间：} \; (- \infty,0) f&#x27;&gt;0 \; \text{增；} \; \text{(0,2) f′&lt;0} \; \text{减；} \; (2,+ \infty) f&#x27;&gt;0 \; \text{增} \\
\text{(3)} \; \text{极大} \; \text{f(0)=1} \; \text{，极小} \; f(2)=8- 12+1=- 3 \\
(4) f&#x27;&#x27;=6x- 6=0 \Rightarrow x=1 \; \text{；两侧} \; \text{f&#x27;&#x27;} \; \text{变号} \; \Rightarrow \; \text{拐点} \; (1, 1- 3+1)=(1,- 1)
\end{gathered}" width="601" height="282"></p>



### 演 4 · 不定积分（分部与换元）· 第 4 章



<p class="fml-block"><img class="fml" src="/formulas/cfd602c8e35d1c.png" alt="\begin{gathered}
(1) \int x e^{x} dx \; \text{：} \; u=x \Rightarrow \int x e^{x}dx= x e^{x}- \int e^{x}dx=(x- 1)e^{x}+ C \\
\text{验算：} \; [(x- 1)e^{x}]&#x27;= e^{x}+(x- 1)e^{x}= x e^{x} \checkmark \\
(2) \int \ln x dx= x \ln x- \int x \cdot\left(\frac{1}{x}\right)dx= x \ln x- x+ C \\
(3) \int \frac{dx}{x^{2}+4}=\left(\frac{1}{2}\right)\arctan\left(\frac{x}{2}\right)+ C \\
(4) \int \sqrt{1- x^{2}} dx \; \text{：令} \; x=\sin t \Rightarrow \int \cos^{2}t dt= \frac{t}{2}+ \frac{\sin 2t}{4}+ C \\
\text{回代：} \; = \frac{1}{2} \arcsin x+ \frac{1}{2} x\sqrt{1- x^{2}}+ C
\end{gathered}" width="526" height="258"></p>



### 演 5 · 定积分与反常积分 · 第 5 章



<p class="fml-block"><img class="fml" src="/formulas/af9786571a3947.png" alt="\begin{gathered}
(1)\; \int_{0}^{\frac{\pi}{2}}\sin^{2}x\,dx=\int_{0}^{\frac{\pi}{2}}\dfrac{1-\cos 2x}{2}\,dx \\
=[\frac{x}{2}- \frac{\sin 2x}{4}]_{0}^{\frac{\pi}{2}}= \frac{\pi}{4} \approx 0.785398 \\
(2) \int_{0}^{1} x e^{x} dx=[(x- 1)e^{x}]_{0}^{1}= 0-(- 1)= 1 \\
(3) \int_{0}^\pi x \sin x dx \; \text{：区间再现} \; \Rightarrow I=\left(\frac{\pi}{2}\right) \int_{0}^\pi \sin x dx=\left(\frac{\pi}{2}\right) \cdot 2= \pi \\
\text{(4)} \; \text{判敛：} \; \int_{1}^\infty \frac{dx}{x^{p}} \; \text{收敛} \; \Leftrightarrow p&gt;1 \; \text{；} \; \int_{0}^{1}\dfrac{dx}{x^{p}} \; \text{收敛} \; \Leftrightarrow p&lt;1 \\
(5) \int_{0}^\infty e^{- x^{2}}dx= \frac{\sqrt{\pi}}{2} \; \text{：设} \; \text{I} \; \text{，} \; I^{2}= \int \int e^{-(x^{2}+y^{2})}dxdy \; \text{（第一象限）} \\
= \int_{0}^{\frac{\pi}{2}}d\theta \int_{0}^\infty e^{- r^{2}}r dr=\left(\frac{\pi}{2}\right) \cdot\left(\frac{1}{2}\right)= \frac{\pi}{4} \Rightarrow I=\frac{\sqrt{\pi}}{2}
\end{gathered}" width="535" height="339"></p>



### 演 6 · 定积分应用（微元法）· 第 6 章



<p class="fml-block"><img class="fml" src="/formulas/17d8e9a4c69dd1.png" alt="\begin{gathered}
\text{题：} \; y=x^{2}(0 \le x \le 1) \; \text{绕} \; \text{x} \; \text{轴旋转体体积与旋转曲面面积。} \\
\text{(1)} \; \text{体积微元} \; dV= \pi y^{2} dx= \pi x^{4} dx \Rightarrow V= \pi \int_{0}^{1}x^{4}dx= \frac{\pi}{5} \approx 0.628319 \\
\text{(2)} \; \text{曲面面积} \; S= 2\pi \int_{0}^{1} y\sqrt{1+y&#x27;^{2}}dx= 2\pi \int_{0}^{1} x^{2}\sqrt{1+4x^{2}}dx \\
\text{(3)} \; \text{题：} \; y=\sin x(0 \le x \le \pi) \; \text{与} \; \text{x} \; \text{轴面积} \; A= \int_{0}^\pi \sin x dx=[- \cos x]_{0}^\pi= 2 \\
\text{(4)} \; \text{题：星形线} \; x=a \cos^{3}t, y=a \sin^{3}t \; \text{全长} \\
ds= \sqrt{\dot{x}^{2}+\dot{y}^{2}}dt= 3a|\sin t \cos t|dt \\
\text{第一象限} \; \int_{0}^{\frac{\pi}{2}}3a \sin t \cos t dt= \frac{3a}{2} \Rightarrow \; \text{全长} \; 4 \times\left(\frac{3a}{2}\right)=6a
\end{gathered}" width="586" height="285"></p>



### 演 7 · 微分方程 · 第 7 章



<p class="fml-block"><img class="fml" src="/formulas/4654e5524ff41b.png" alt="\begin{gathered}
(1) y&#x27;+2y=e^{x} \Rightarrow(e^{2x}y)&#x27;=e^{3x} \Rightarrow e^{2x}y= \frac{1}{3} e^{3x}+C \Rightarrow y= \frac{1}{3} e^{x}+Ce^{- 2x} \\
(2) y&#x27;&#x27;- 3y&#x27;+2y=0 \Rightarrow r^{2}- 3r+2=0 \Rightarrow r=1,2 \Rightarrow y=C_{1}e^{x}+C_{2}e^{2x} \\
(3) y&#x27;&#x27;+4y=\sin x \; \text{：齐次解} \; C_{1}\cos 2x+C_{2}\sin 2x \; \text{；设} \; y*=A \sin x \\
\Rightarrow- A+4A=1 \Rightarrow A=\frac{1}{3} \Rightarrow y=C_{1}\cos 2x+C_{2}\sin 2x+\left(\frac{1}{3}\right)\sin x \\
\text{(4)} \; \text{共振情形} \; y&#x27;&#x27;+4y=\sin 2x \; \text{须设} \; \text{y*=x(A cos2x+B sin2x)} \; \text{（不可漏} \; \text{x} \; \text{）} \\
\text{(5)} \; \text{欧拉方程} \; x^{2}y&#x27;&#x27;+xy&#x27;- y=0 \; \text{：设} \; y=x^{k} \Rightarrow k(k- 1)+k- 1=k^{2}- 1=0 \Rightarrow k=±1 \\
\Rightarrow y=C_{1}x+\frac{C_{2}}{x}
\end{gathered}" width="695" height="244"></p>



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



<p class="fml-block"><img class="fml" src="/formulas/63e3b28fb7d4a1.png" alt="\begin{gathered}
(1) f=x^{2}y+\sin(xy) \; \text{：} \; f_{x}=2xy+y \cos(xy) \; \text{，} \; f_{y}=x^{2}+x \cos(xy) \\
\text{在} \; \text{(0,1)} \; \text{：} \; \nabla f=(1,0) \; \text{；沿} \; e=\left(\frac{1}{\sqrt{2}},\frac{1}{\sqrt{2}}\right) \; \text{的方向导数} \; = \frac{1}{\sqrt{2}} \approx 0.707107 \\
\text{(2)} \; \text{曲面} \; z=x^{2}+y^{2} \; \text{在} \; \text{(1,1,2)} \; \text{：令} \; F=x^{2}+y^{2}- z \; \text{，} \; \nabla F=(2x,2y,- 1)=(2,2,- 1) \\
\text{切平面} \; 2(x- 1)+2(y- 1)-(z- 2)=0 \Rightarrow 2x+2y- z- 2=0 \\
\text{(3)} \; \text{无条件极值} \; f=x^{2}+y^{2} \; \text{：} \; A=C=2,B=0 \Rightarrow \Delta=4&gt;0 \; \text{且} \; A&gt;0 \Rightarrow(0,0) \; \text{极小} \; \text{0} \\
\text{f=xy} \; \text{：} \; \Delta=- 1&lt;0 \Rightarrow(0,0) \; \text{是鞍点} \\
\text{(4)} \; \text{条件极值} \; \min x^{2}+y^{2} s.t. x+y=1 \; \text{：} \\
L=x^{2}+y^{2}- \lambda(x+y- 1) \; \text{，} \; 2x=\lambda, 2y=\lambda \Rightarrow x=y=\frac{1}{2} \Rightarrow f_{\min}=\frac{1}{2}
\end{gathered}" width="690" height="255"></p>



### 演 10 · 重积分 · 第 10 章



<p class="fml-block"><img class="fml" src="/formulas/818993b8683a3f.png" alt="\begin{gathered}
\text{(1)} \; \text{换序：} \; \int_{0}^{1}dx \int_{x}^{1} f dy \; \text{（区域} \; 0 \le x \le y \le 1 \; \text{）} \; \Rightarrow \int_{0}^{1}dy \int_{0}^{y} f dx \\
(2) \iint _{D} e^{- y^{2}}dxdy \; \text{，} \; D: 0 \le x \le y \le 1 \\
= \int_{0}^{1}dy \int_{0}^{y} e^{- y^{2}}dx= \int_{0}^{1} y e^{- y^{2}}dy= \frac{1}{2}(1- e^{-1}) \approx 0.31606 \\
(3) \iint _{x^{2}+y^{2} \le a^{2}} e^{-(x^{2}+y^{2})}dxdy= 2\pi \int_{0}^{a} r e^{- r^{2}}dr= \pi(1- e^{- a^{2}}) \\
a=1 \Rightarrow \approx 1.985865 \\
\text{(4)} \; \iiint_{\text{上半球}} z\,dV=\int_{0}^{2\pi}\!d\theta\int_{0}^{\pi/2}\!\sin\phi\cos\phi\,d\phi\int_{0}^{1}\!\rho^{3}d\rho \\
= 2\pi \cdot\left(\frac{1}{2}\right) \cdot\left(\frac{1}{4}\right)= \frac{\pi}{4} \approx 0.785398 \\
\text{(5) 单位球} \; \iiint_{\Omega} 1\,dV=\dfrac{4\pi}{3}\approx 4.188790
\end{gathered}" width="539" height="369"></p>



### 演 11 · 曲线曲面积分与三大公式 · 第 11 章



<p class="fml-block"><img class="fml" src="/formulas/d935901f2a2b61.png" alt="\begin{gathered}
\text{(1)} \; \text{单位圆} \; \text{L} \; \text{（逆时针）：} \; \oint _{L} x dy- y dx \\
\text{参数} \; x=\cos t, y=\sin t \Rightarrow x dy- y dx= \cos^{2}t dt+ \sin^{2}t dt= dt \\
\Rightarrow \; \text{积分} \; = \int_{0}^{2\pi}dt= 2\pi \; \text{（} \; = 2 \cdot Area \; \text{，格林公式验证：} \; \iint _{D} 2 dxdy= 2\pi \; \text{）} \\
\text{(2)} \; \text{奇点陷阱：} \; \oint_{L}\dfrac{x\,dy-y\,dx}{x^{2}+y^{2}} \\
\frac{\partial Q}{\partial x}- \frac{\partial P}{\partial y}= 0 \; \text{但原点为奇点} \; \Rightarrow \; \text{不能直接得} \; \text{0} \\
\text{挖去半径} \; \epsilon \; \text{小圆后由格林} \; \Rightarrow \; \text{等于小圆积分} \; = 2\pi \\
\text{(3)} \; \text{高斯：} \; \oiint _{S} x dydz+y dzdx+z dxdy= \iiint _\Omega 3 dV \; \text{，单位球} \; \Rightarrow 3 \cdot\left(\frac{4\pi}{3}\right)=4\pi \\
\text{(4) div(x,y,z)=3} \; \text{；} \; rot(- y,x,0)=(0,0,2) \\
\text{(5)} \; \text{判路径无关：} \; P=2xy, Q=x^{2} \Rightarrow \frac{\partial P}{\partial y}=2x= \frac{\partial Q}{\partial x} \Rightarrow \; \text{与路径无关} \\
\text{原函数} \; u= \int Pdx= x^{2}y+\phi(y) \; \text{，由} \; u_{y}=x^{2}+\phi &#x27;=Q \Rightarrow \phi &#x27;=0 \Rightarrow u=x^{2}y+C
\end{gathered}" width="638" height="409"></p>



### 演 12 · 级数 · 第 12 章



<p class="fml-block"><img class="fml" src="/formulas/40408bf9d7cb55.png" alt="\begin{gathered}
\text{(1)} \; \text{判敛} \; \sum \frac{n}{2^{n}} \; \text{：比值} \; \rho=\lim \frac{\frac{n+1}{2^{n+1}}}{\frac{n}{2^{n}}}= \frac{1}{2}&lt; 1 \Rightarrow \; \text{收敛} \\
\text{(2)} \; \text{判敛} \; \sum \frac{1}{n^{2}} \; \text{：} \; p=2&gt;1 \Rightarrow \; \text{收敛；} \; \sum\frac{1}{n} \; \text{：} \; p=1 \Rightarrow \; \text{发散} \\
\text{(3)} \; \text{收敛半径} \; \sum \frac{x^{n}}{n} \; \text{：} \; R=\lim|\frac{a_{n}}{a_{n+1}}|= \lim \frac{n+1}{n}= 1 \\
\text{端点} \; x=1 \Rightarrow \sum\frac{1}{n} \; \text{发散；} \; x=- 1 \Rightarrow \sum\frac{(-1)^{n}}{n} \; \text{收敛} \; \Rightarrow \; \text{收敛域} \; \text{[−1,1)} \\
\text{(4)} \; \text{和函数} \; \sum_{n=1}^\infty n x^{n} \; \text{：由} \; \sum x^{n}=\frac{1}{1- x} \; \text{逐项求导乘} \; \text{x} \\
\Rightarrow \frac{x}{(1- x)^{2}} \; \text{（} \; \text{|x|&lt;1} \; \text{）；验算} \; x=\frac{1}{2} \Rightarrow 2 \\
(5) \sum\frac{1}{n(n+1)}= \sum\left(\frac{1}{n}- \frac{1}{n+1}\right)= 1- \lim \frac{1}{N+1}= 1 \\
(6) \sum\frac{(-1)^{n+1}}{n}= \ln 2 \; \text{（条件收敛）；} \; \sum\frac{(-1)^{n+1}}{n^{2}}= \frac{\pi^{2}}{12} \; \text{（绝对收敛）}
\end{gathered}" width="573" height="381"></p>



---

## 图形读图专题：18 张图怎么画、怎么读

| 图 | 必画元素 | 读图要点（最常被问的一句） |
| --- | --- | --- |
| `math-overview` | 12 章分四段与主线条 | 一元微分 → 一元积分 → 方程与空间 → 多元 → 级数，顺序不可颠倒 |
| `math-function` | 五类基本初等函数与四性质 | 反函数存在要求一一对应；奇偶性先看定义域 |
| `math-limit` | ε–δ 邻域、两个重要极限曲线 | 定义是「去心」邻域；<img class="fml" src="/formulas/a3b963bcc12b7a.png" alt="f(x_{0})" width="49" height="33"> 与极限无关 |
| `math-taylor` | 两种余项、五个展开 | 佩亚诺用于局部求极限，拉格朗日用于整体误差估计 |
| `math-derivative` | 割线趋切线、Δy 与 dy | 可导 ⇔ 可微 ⇒ 连续，反向不成立 |
| `math-mvt` | 弦与平行切线、罗尔水平切线 | 拉格朗日 = 弦斜率等于某点切线斜率 |
| `math-application` | f′/f″ 符号表、三类渐近线 | 拐点要写坐标；水平/斜渐近线分 ±∞ 求 |
| `math-integral` | 三类积分法流程 | 分部取 u 按「反对幂指三」；第二换元须回代 |
| `math-definite` | 黎曼和矩形、曲边梯形 | 微积分基本定理把「和的极限」化为「原函数增量」 |
| `math-app-integration` | 微元条带、旋转体 | 微元可加是前提；面积要加绝对值 |
| `math-ode` | 分类决策树 | 先判阶数与线性，再判齐次/可分离；共振要乘 <img class="fml" src="/formulas/e2a88b944111e4.png" alt="x^{k}" width="25" height="34"> |
| `math-vector` | 三种积、平面法向量、直线方向 | 直线一般式的方向是两法向量的叉积 |
| `math-surface` | 二次曲面截痕 | 缺变量是柱面；负号个数决定单/双叶 |
| `math-multivariable` | 关系链、梯度与等值线 | 偏导存在 ⇏  连续、⇏  可微（与一元不同） |
| `math-extremum` | <img class="fml" src="/formulas/d08e23b37ab082.png" alt="\Delta=AC- B^{2}" width="116" height="34"> 判别、约束曲线 | 梯度与约束梯度平行即拉格朗日条件 |
| `math-multiple-integral` | X/Y 型区域、极/球坐标 | 换序三步；球坐标 <img class="fml" src="/formulas/b525ea956cedcb.png" alt="dV=\rho^{2}\sin \phi d\rho d\phi d\theta" width="166" height="33"> |
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
| 求 `0/0` 极限 | 先试等价无穷小（仅乘除）→ 加减结构或主阶抵消直接上泰勒 → 最后才洛必达 |
| 求 <img class="fml" src="/formulas/638c8be7aac7e4.png" alt="1^\infty" width="29" height="33"> 极限 | 凑 <img class="fml" src="/formulas/98ffe8a35ff1f7.png" alt="(1+\alpha)^{\frac{1}{\alpha}}" width="74" height="33"> 或取对数；速算 <img class="fml" src="/formulas/5c9a207a42a8a6.png" alt="e^{\lim g(f- 1)}" width="76" height="33"> |
| 递推数列极限 | 证有界（归纳）+ 证单调（作差/作商）⇒ 设极限 A 解 `A=f(A)`，注意验证 A 的合理性 |
| n 项和极限 | 夹逼准则（放缩）或定积分定义 <img class="fml" src="/formulas/f7785bfcdd61af.png" alt="\lim\left(\frac{1}{n}\right)\sum f\left(\frac{k}{n}\right)= \int_{0}^{1}f dx" width="205" height="33"> |
| 无穷小阶的比较 | 求 <img class="fml" src="/formulas/a484aa0088528a.png" alt="\lim \frac{\alpha}{\beta}" width="47" height="35">：为 0 则 α 高阶、∞ 则低阶、常数 c≠0 则同阶、1 则等价 |
| 间断点分类 | 找所有可疑点（分母为 0、分段点、无定义点）→ 逐点算左右极限 → 归类 |
| 含参数的分段函数 | 由连续/可导条件列方程（连续：左右极限 = 函数值；可导：左右导数相等）求参数 |
| 证明方程有根 | 构造 <img class="fml" src="/formulas/ef741e674e8ecd.png" alt="F(x)=f(x)- x" width="135" height="33"> 或原函数，用零点定理；唯一性再用单调性 |

### 第 2 章 · 导数与微分

| 题型 | 标准动作 |
| --- | --- |
| 用定义求导 | 写差商 → 代入 → 化简（有理化、等价无穷小）→ 取极限；分段点必用定义 |
| 复合/隐函数/参数求导 | 画变量关系图；隐函数两边对 x 求导把 y 视为 x 的函数；参数方程二阶导先对 t |
| 幂指函数 `u(x)^{v(x)}` | 取对数或化为 <img class="fml" src="/formulas/252902701378a4.png" alt="e^{v \ln u}" width="45" height="33"> |
| 高阶导数 / 求 <img class="fml" src="/formulas/f2143aeac17a31.png" alt="f^{(n)}(0)" width="59" height="33"> | 莱布尼茨公式、已知展开式系数、或递推 |
| 导数几何应用 | 切线 <img class="fml" src="/formulas/3ef17518a56647.png" alt="y- f(x_{0})=f&#x27;(x_{0})(x- x_{0})" width="213" height="33">，法线斜率 <img class="fml" src="/formulas/57e552298b61c0.png" alt="- \frac{1}{f}&#x27;" width="37" height="35">；注意 `f′=0` 时法线竖直 |
| 含绝对值的可导性 | <img class="fml" src="/formulas/41e45a4dee07b5.png" alt="g(x)\vert x- a\vert" width="92" height="33"> 在 a 可导 ⇔ `g(a)=0` |

### 第 3 章 · 中值定理与导数应用

| 题型 | 标准动作 |
| --- | --- |
| 证 <img class="fml" src="/formulas/d12d51c08ab887.png" alt="\exists \xi : F&#x27;(\xi)=0" width="114" height="33"> | 构造 F → 验证罗尔三条件 → 结论（写清 ξ 在开区间） |
| 证含两个中值 <img class="fml" src="/formulas/0f3970aedb9d86.png" alt="\xi,\eta" width="33" height="33"> | 分别对两个函数用拉格朗日，或对同一函数在不同区间用中值定理 |
| 证不等式 | ① 移项构造 `F(x)` 证 `F′>0` 且 <img class="fml" src="/formulas/ab02464aff55a9.png" alt="F(a) \ge 0" width="77" height="33">；② 拉格朗日中值定理放缩；③ 泰勒展开 + 余项符号；④ 凹凸性（琴生不等式） |
| 讨论方程根的个数 | 求单调区间与极值 → 结合端点符号与零点定理分区间计数 |
| 求渐近线 | 无定义点查铅直；<img class="fml" src="/formulas/4d63245854c00c.png" alt="± \infty" width="39" height="33"> 分别求水平；若无水平再求斜 |
| 最值应用题 | 设变量 → 建立目标函数 → 求导找唯一驻点 → 说明实际最值存在即得结论 |

### 第 4 章 · 不定积分

| 题型 | 标准动作 |
| --- | --- |
| 有理函数积分 | 多项式除法 → 分母因式分解 → 待定系数拆部分分式 → 逐项积分 |
| 三角有理式 | 先看能否用倍角/降幂/凑微分；否则万能代换 |
| 分部积分循环型 | 两次分部后出现原积分 ⇒ 移项解方程，`+C` 最后补 |
| 含 `|x|` / 分段被积函数 | 分段积分，再由原函数连续性统一各段常数 |
| 抽象函数积分 | 用凑微分与分部把 <img class="fml" src="/formulas/8b5e698f72398d.png" alt="\int f&#x27;(x)g(x)dx" width="114" height="33"> 转化为已知条件 |

### 第 5 章 · 定积分与反常积分

| 题型 | 标准动作 |
| --- | --- |
| 定积分计算 | 先查奇偶/周期/区间再现化简 → 再换元或分部 → 换元时**同步改上下限** |
| 变限函数极限 | 洛必达 + 变限求导通式；含参数先换元 |
| 积分等式证明 | 换元 <img class="fml" src="/formulas/647ea9770f5252.png" alt="t=a+b- x" width="108" height="33">、分部、或构造辅助函数用罗尔 |
| 积分不等式 | 保号性、比较性、估值定理、柯西–施瓦茨 `（∫fg)² ≤ ∫f²∫g²` |
| 反常积分计算与判敛 | 分段取极限；判敛用 p 判别 / 极限比较；瑕点在内部必须拆 |
| 定积分定义求极限 | 凑成 <img class="fml" src="/formulas/5a70eae1bef921.png" alt="\lim\left(\frac{1}{n}\right)\sum f\left(\frac{k}{n}\right)" width="129" height="33"> 识别为 <img class="fml" src="/formulas/7add9cc48cd398.png" alt="\int_{0}^{1} f(x)dx" width="83" height="33"> |

### 第 6 章 · 定积分应用

| 题型 | 标准动作 |
| --- | --- |
| 面积 | 画图求交点 → 判断上下曲线 → 分段加绝对值 → 积分；极坐标用 <img class="fml" src="/formulas/cf2fafc2af52e8.png" alt="\frac{1}{2} \int r^{2}d\theta" width="70" height="33"> |
| 旋转体体积 | 绕 x 用圆盘 <img class="fml" src="/formulas/ac609748bd74fa.png" alt="\pi \int f^{2}dx" width="73" height="33">；绕 y 用柱壳 <img class="fml" src="/formulas/77424cb695f2c1.png" alt="2\pi \int x f dx" width="85" height="33"> 或反函数圆盘 |
| 弧长 | 三种形式按已知选（直角 / 参数 / 极坐标） |
| 物理应用 | 建坐标系 → 写微元（注意深度、力臂）→ 定限 → 积分 |

### 第 7 章 · 常微分方程

| 题型 | 标准动作 |
| --- | --- |
| 一阶方程 | 按可分离 → 齐次 → 线性 → 伯努利 → 全微分的顺序判别；齐次常需先作平移 `x=X+h, y=Y+k` |
| 可降阶 | 判断缺 y 还是缺 x，选择令 `p=y′` 后把 `y″` 写成 `p′` 或 `p dp/dy` |
| 二阶常系数 | 特征方程 → 齐次通解 → 按右端形式设特解（共振乘 <img class="fml" src="/formulas/e2a88b944111e4.png" alt="x^{k}" width="25" height="34">） |
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
| 旋转曲面 | 按绕哪个轴替换对应变量，注意 <img class="fml" src="/formulas/1b471406943707.png" alt="\pm\sqrt{\cdot}" width="40" height="33"> 与定义域 |

### 第 9 章 · 多元微分

| 题型 | 标准动作 |
| --- | --- |
| 判二重极限不存在 | 沿 `y=kx`（得依赖 k 的值）或沿 `y=x` 与 <img class="fml" src="/formulas/6dd98f6cdd0fea.png" alt="y=x^{2}" width="57" height="34"> 得不同值 |
| 求偏导 / 全微分 | 固定其余变量；抽象复合函数先画变量图再写链式 |
| 判可微性 | 偏导连续 ⇒ 可微（最常用）；否则回定义算 <img class="fml" src="/formulas/4559c9789bec19.png" alt="\frac{\lim[\Delta z- f_{x}\Delta x- f_{y}\Delta y]}{\rho}" width="131" height="36"> |
| 方向导数 / 梯度 | 可微时用 <img class="fml" src="/formulas/1e49b7daf574c6.png" alt="\nabla f \cdot e_{l}" width="58" height="33">；单位化方向向量别忘 |
| 切平面 / 法线 | <img class="fml" src="/formulas/5b95371d9ff9cf.png" alt="\nabla F" width="36" height="33"> 作法向量；参数曲线用 `r′(t)` |
| 极值 / 最值 | 驻点 → <img class="fml" src="/formulas/d08e23b37ab082.png" alt="\Delta=AC- B^{2}" width="116" height="34"> 判别 → 闭区域再查边界；条件极值用拉格朗日 |
| 抽象函数方程 | 由给定的全微分或偏导关系，用变量代换化为 PDE 再积分 |

### 第 10 章 · 重积分

| 题型 | 标准动作 |
| --- | --- |
| 化累次积分 / 换序 | 写不等式 → 画图 → 穿线法重写 → 非简单型分块 |
| 极坐标 | 区域含圆、被积含 <img class="fml" src="/formulas/f0c0ee88f1c9cc.png" alt="x^{2}+y^{2}" width="63" height="34"> ⇒ 换极坐标，写清 <img class="fml" src="/formulas/2d3198fcda5e70.png" alt="\theta" width="16" height="33"> 与 `r` 范围 |
| 三重积分 | 含 <img class="fml" src="/formulas/f0c0ee88f1c9cc.png" alt="x^{2}+y^{2}" width="63" height="34"> 用柱；含 <img class="fml" src="/formulas/4f872fcad6f607.png" alt="x^{2}+y^{2}+z^{2}" width="101" height="34"> 用球；先一后二 / 先二后一按截面选 |
| 对称性 | 奇偶性 → 轮换对称 → 区域可加，先化简 |
| 含绝对值 / max,min | 按分界线把区域切开分别积分 |
| 曲面面积 / 质心 | 用 <img class="fml" src="/formulas/2c98ae0374b3a5.png" alt="\sqrt{1+z_{x}^{2}+z_{y}^{2}}" width="110" height="42"> 与 <img class="fml" src="/formulas/e7da11ba1e562b.png" alt="\iint x\rho \frac{d\sigma}{M}" width="66" height="33"> 等公式 |

### 第 11 章 · 线面积分与场论

| 题型 | 标准动作 |
| --- | --- |
| 第一类线积分 | 参数化 + `ds`；利用对称性；上下限小到大 |
| 第二类线积分 | 参数化直接代入（最稳）或格林（闭曲线）/ 补线 / 判路径无关 |
| 路径无关求积分 | 验证 <img class="fml" src="/formulas/e451b6f83f5234.png" alt="P_{y}=Q_{x}" width="72" height="33"> → 选折线路径求原函数 `u` → `u(终点)−u(起点)` |
| 第二类面积分 | 合一投影法或逐面投影；先定侧 |
| 高斯 / 斯托克斯 | 检查闭性与连续性；有奇点挖洞；非闭补面后减去 |
| 散度 / 旋度 / 通量 | 直接按定义求偏导，注意 <img class="fml" src="/formulas/3460fa1fcb5db2.png" alt="\nabla \cdot( \nabla \times A)=0" width="131" height="34"> 可秒判 |

### 第 12 章 · 无穷级数

| 题型 | 标准动作 |
| --- | --- |
| 判正项级数敛散 | 等价无穷小找主阶 → 与 <img class="fml" src="/formulas/5450590036d399.png" alt="\frac{1}{n^{p}}" width="24" height="33"> 极限比较；阶乘/指数用比值；`n` 次幂用根值 |
| 判交错 / 一般项 | 莱布尼茨判收敛；再判 <img class="fml" src="/formulas/70aa7e08807578.png" alt="\sum\vert u_{n}\vert" width="57" height="34"> 得绝对或条件收敛 |
| 求收敛半径 / 域 | 比值或根值求 R，<img class="fml" src="/formulas/02678f3ec2c152.png" alt="x=x_{0}±R" width="94" height="33"> 两端点单独判 |
| 求和函数 | 逐项求导/积分化为几何级数 → 求和 → 逆运算还原 → 定常数 → 讨论端点 |
| 展开为幂级数 | 用五个基本展开 + 四则/复合/逐项积分；记住收敛域可能缩小 |
| 傅里叶展开 | 先判奇偶 → 算 <img class="fml" src="/formulas/7f373bf33be627.png" alt="a_{n},b_{n}" width="48" height="33">（用正交性）→ 写级数 → 用狄利克雷说明收敛值 |
| 求数项级数和 | 构造幂级数取特定 x；或由傅里叶级数在特殊点代入 |

---

## 重要公式推导补遗

> 教材多以「给出公式」为主，这里补上几个最常被追问「为什么」的推导要点。

### 推 1 · 华里士公式的递推

设 <img class="fml" src="/formulas/3b0055be546aa5.png" alt="I_{n}= \int_{0}^{\frac{\pi}{2}} \sin^{n}x dx" width="135" height="35">。分部取 <img class="fml" src="/formulas/e566072f922a47.png" alt="u=\sin^{n- 1}x, dv=\sin x dx" width="205" height="34">：



<p class="fml-block"><img class="fml" src="/formulas/786a54d5d19629.png" alt="I_{n}=[- \sin^{n- 1}x \cos x]_{0}^{\frac{\pi}{2}}+(n- 1) \int_{0}^{\frac{\pi}{2}} \sin^{n- 2}x \cos^{2}x dx" width="416" height="35"></p>





<p class="fml-block"><img class="fml" src="/formulas/4292039c51265a.png" alt="=(n- 1) \int \sin^{n- 2}x(1- \sin^{2}x)dx=(n- 1)(I_{n-2}- I_{n})" width="428" height="34"></p>



⇒ <img class="fml" src="/formulas/3ffa4f03f1e932.png" alt="n I_{n}=(n- 1)I_{n-2}" width="146" height="34"> ⇒ <img class="fml" src="/formulas/860b1485de9ede.png" alt="I_{n}= \frac{n- 1}{n} \cdot I_{n-2}" width="120" height="33">。
由 <img class="fml" src="/formulas/c8a139b7910c8c.png" alt="I_{0}=\frac{\pi}{2}" width="57" height="34">、<img class="fml" src="/formulas/d78f91dea32fcf.png" alt="I_{1}=1" width="55" height="34"> 递推得偶/奇两套结果；令 `n=2` 得 <img class="fml" src="/formulas/ada8c16c9f2001.png" alt="I_{2}= \dfrac{1}{2}\cdot\dfrac{\pi}{2}= \dfrac{\pi}{4}" width="125" height="44"> ✓。

### 推 2 · 泊松积分与 <img class="fml" src="/formulas/12459dbb9aef8b.png" alt="\Gamma\left(\frac{1}{2}\right)" width="48" height="34">

由综 3：`I² = ∬_{第一象限}e^{−(x²+y²)}dxdy = (π/2)∫0^∞ e^{−r²}2r·(1/2)dr … = π/4` ⇒ <img class="fml" src="/formulas/586e7e7ca126a5.png" alt="I=\frac{\sqrt{\pi}}{2}" width="63" height="34">。
换元 <img class="fml" src="/formulas/a4c202ac1ebd57.png" alt="t=x^{2}" width="54" height="34">：<img class="fml" src="/formulas/eaf105199d21f3.png" alt="\Gamma\left(\frac{1}{2}\right)= \int_{0}^\infty t^{- \frac{1}{2}}e^{- t}dt= 2 \int_{0}^\infty e^{- x^{2}}dx= \sqrt{\pi}" width="330" height="34">；
由 <img class="fml" src="/formulas/bd5571871303c9.png" alt="\Gamma(s+1)=s\Gamma(s)" width="136" height="33"> 得 <img class="fml" src="/formulas/09e41af8bcc674.png" alt="\Gamma(n+1)=n!" width="113" height="33">、<img class="fml" src="/formulas/439788c5dbf078.png" alt="\Gamma\left(\frac{3}{2}\right)=\frac{\sqrt{\pi}}{2}" width="94" height="34">，故 Γ 是阶乘的连续延拓。

### 推 3 · 牛顿–莱布尼茨 ⇒ 格林 ⇒ 高斯（同一思想）



<p class="fml-block"><img class="fml" src="/formulas/21d5568b9f1264.png" alt="\begin{gathered}
\text{一维：} \; \int_{a}^{b} F&#x27;(x)dx= F(b)- F(a) \; \text{（区间内部导数的积分} \; \text{=} \; \text{边界上的值）} \\
\text{二维：} \; \iint _{D}(Q_{x}- P_{y})dxdy= \oint _{\partial D} Pdx+Qdy \; \text{（内部旋度} \; \text{=} \; \text{边界环流）} \\
\text{三维：} \; \iiint _\Omega div A dV= \oiint _{\partial \Omega} A \cdot n dS \; \text{（内部散度} \; \text{=} \; \text{边界通量）} \\
\text{三者都是「把内部相邻微元的贡献相互抵消，只剩边界」：} \\
\text{分割区域后，相邻小区域的公共边界上方向相反、积分抵消。}
\end{gathered}" width="590" height="199"></p>


**推论**：取 <img class="fml" src="/formulas/f9739829b502ca.png" alt="P=- \frac{y}{2}, Q=\frac{x}{2}" width="127" height="34"> ⇒ <img class="fml" src="/formulas/122964a274950c.png" alt="Q_{x}- P_{y}=1" width="103" height="34"> ⇒ <img class="fml" src="/formulas/1c775c30d89bd6.png" alt="Area(D)= \frac{1}{2} \oint (x dy- y dx)" width="218" height="34">（格林求面积公式）。

### 推 4 · 一阶线性方程的积分因子

`y′+P(x)y=Q(x)`。设存在 <img class="fml" src="/formulas/d6bb2161f3bc97.png" alt="\mu(x)" width="42" height="34"> 使 <img class="fml" src="/formulas/edca8fd53496f5.png" alt="(\mu y)&#x27;=\mu Q" width="94" height="34">，展开 <img class="fml" src="/formulas/da3a7faa4ed8f0.png" alt="\mu y&#x27;+\mu &#x27;y=\mu Q" width="127" height="34"> 对比得 <img class="fml" src="/formulas/0ab3a864e86628.png" alt="\mu &#x27;=\mu P" width="70" height="34"> ⇒ <img class="fml" src="/formulas/6acf93530327be.png" alt="\mu=e^{\int P dx}" width="85" height="34">。
于是 <img class="fml" src="/formulas/f37dcde43661c9.png" alt="(\mu y)&#x27;=\mu Q \Rightarrow \mu y= \int \mu Q dx+ C" width="261" height="34">，即通解公式。这套「乘积分因子」也是综 2 中辅助函数构造的来源。

### 推 5 · 幂级数求和函数的通法



<p class="fml-block"><img class="fml" src="/formulas/95941bcca04901.png" alt="\begin{gathered}
\text{求} \; S(x)=\sum_{n=1}^\infty n x^{n} \; \text{：} \\
\frac{S(x)}{x}= \sum n x^{n- 1}=\left(\sum x^{n}\right)&#x27;=[\frac{1}{1- x}- 1]&#x27;= \frac{1}{(1- x)^{2}} \\
\Rightarrow S(x)= \frac{x}{(1- x)^{2}} \; \text{，} \; \text{|x|&lt;1} \\
\text{求} \; S(x)=\sum \frac{x^{n}}{n} \; \text{：} \\
S&#x27;(x)=\sum x^{n- 1}=\frac{1}{1- x} \Rightarrow S(x)=- \ln(1- x)+C \; \text{；由} \; S(0)=0 \Rightarrow C=0
\end{gathered}" width="601" height="235"></p>


关键：**逐项求导把系数 `n` 消掉、逐项积分把分母 `n` 补上**，最后务必用 `S(0)` 定常数并单独检验端点。

### 推 6 · 傅里叶系数公式来自正交性

三角函数系 `{1, cos nx, sin nx}` 在 <img class="fml" src="/formulas/97882832f26aa1.png" alt="[- \pi,\pi]" width="60" height="33"> 上正交：
<img class="fml" src="/formulas/12d88fa1c43aa0.png" alt="\int_{- \pi}^{\pi} \cos mx \cos nx dx= \pi \delta_{mn}" width="222" height="34">（<img class="fml" src="/formulas/eee35d3647a508.png" alt="m,n \ge 1" width="74" height="33">），<img class="fml" src="/formulas/c9b011da44748f.png" alt="\int \sin mx \sin nx dx= \pi \delta_{mn}" width="203" height="33">，<img class="fml" src="/formulas/6efb926aae2e84.png" alt="\int \sin mx \cos nx dx= 0" width="175" height="33">，<img class="fml" src="/formulas/da23696656020d.png" alt="\int_{- \pi}^{\pi}1 dx= 2\pi" width="108" height="34">。
两边同乘 `cos nx` 并在 <img class="fml" src="/formulas/97882832f26aa1.png" alt="[- \pi,\pi]" width="60" height="33"> 上逐项积分，除第 n 项外全为 0 ⇒ <img class="fml" src="/formulas/346d87f65961c0.png" alt="a_{n}=\left(\frac{1}{\pi}\right) \int f \cos nx dx" width="176" height="33">；常数为 <img class="fml" src="/formulas/53104a17664564.png" alt="\frac{a_{0}}{2}" width="23" height="33"> 正是为统一系数形式。

### 推 7 · 二元极值充分条件来自泰勒

在驻点 <img class="fml" src="/formulas/0e129aa0a68218.png" alt="(x_{0},y_{0})" width="62" height="33"> 处 <img class="fml" src="/formulas/86a2c326067ebd.png" alt="f_{x}=f_{y}=0" width="96" height="34">，二阶泰勒：
<img class="fml" src="/formulas/3f2512b33e00e6.png" alt="\Delta f \approx \frac{1}{2}(A h^{2}+ 2B hk+ C k^{2})" width="230" height="33">，这是关于 `(h,k)` 的二次型。
其正定 ⇔ `A>0` 且 <img class="fml" src="/formulas/58f9d18330a371.png" alt="AC- B^{2}&gt;0" width="110" height="33"> ⇒ <img class="fml" src="/formulas/7de46673679d1f.png" alt="\Delta f&gt;0" width="66" height="33"> 恒成立 ⇒ 极小；负定 ⇔ `A<0` 且 <img class="fml" src="/formulas/a1224bf4e91754.png" alt="\Delta&gt;0" width="55" height="34"> ⇒ 极大；<img class="fml" src="/formulas/b2e13ad93929c7.png" alt="\Delta&lt;0" width="54" height="34"> 时二次型不定 ⇒ 沿不同方向符号相反 ⇒ 鞍点。<img class="fml" src="/formulas/4a17320a23ee6e.png" alt="\Delta=0" width="55" height="34"> 时二次项不足以判定，需更高阶。

### 推 8 · 欧拉公式 <img class="fml" src="/formulas/221877010a76c7.png" alt="e^{ix}= \cos x+ i \sin x" width="154" height="33">

把 <img class="fml" src="/formulas/a25755dfedb8cc.png" alt="e^z= \sum \frac{z^{n}}{n}!" width="90" height="33"> 中令 `z=ix`，按偶次/奇次分组：



<p class="fml-block"><img class="fml" src="/formulas/8054631c2dc584.png" alt="e^{ix}=[1- \frac{x^{2}}{2}!+ \frac{x^{4}}{4}!- \cdots]+ i[x- \frac{x^{3}}{3}!+ \frac{x^{5}}{5}!- \cdots]= \cos x+ i \sin x" width="511" height="34"></p>



取 <img class="fml" src="/formulas/f3bf5c66cf4d56.png" alt="x=\pi" width="52" height="33"> 得 <img class="fml" src="/formulas/f6f7c3ed5ed15e.png" alt="e^{i\pi}+1=0" width="92" height="33">；由此复数可写 <img class="fml" src="/formulas/a52222004b78b0.png" alt="z=re^{i\theta}" width="68" height="33">，是常系数方程复根解 <img class="fml" src="/formulas/d16810d5eeb1f3.png" alt="e^{\alpha x}(C_{1}\cos \beta x+C_{2}\sin \beta x)" width="208" height="34"> 的来源。

---

## 综合例题精讲（跨章）

### 综 1 · 极限 → 导数 → 泰勒（第 1–3 章）

题：设 `f(x)` 在 `x=0` 二阶可导，<img class="fml" src="/formulas/4cb519d318a516.png" alt="\lim_{x \to 0}[\frac{f(x)}{x}+ \sin \frac{x}{x^{2}}]= 1" width="193" height="33">，求 `f(0)`、`f′(0)`，并讨论 `f″(0)` 能否确定。



<p class="fml-block"><img class="fml" src="/formulas/f404080f43a13c.png" alt="\begin{gathered}
\text{(1)} \; \text{通分：} \; \lim \frac{x f(x)+ \sin x}{x^{2}}= 1 \; \text{（有限）} \; \Rightarrow \; \text{分子必须为} \; O(x^{2}) \\
\text{(2)} \; \text{若} \; f(0)=0 \; \text{，则} \; \text{x f(x) ~ f(0)x} \; \text{而} \; \sin x \sim x \Rightarrow \; \text{分子} \; \text{~ (f(0)+1)x} \\
\text{要使其为} \; O(x^{2}) \; \text{必须} \; f(0)=- 1 \\
\text{(3)} \; \text{泰勒：} \; f(x)=- 1+ f&#x27;(0)x+ \frac{1}{2} f&#x27;&#x27;(0)x^{2}+ o(x^{2}) \; \text{，} \; \sin x= x- \frac{x^{3}}{6}+ o(x^{3}) \\
\text{分子} \; = x[- 1+ f&#x27;(0)x+ \frac{1}{2} f&#x27;&#x27;(0)x^{2}+ o(x^{2})]+ x- \frac{x^{3}}{6}+ o(x^{3}) \\
= f&#x27;(0)x^{2}+[ \frac{1}{2} f&#x27;&#x27;(0)- \frac{1}{6}]x^{3}+ o(x^{3}) \\
\text{(4)} \; \text{分子} \; x^{2}= f&#x27;(0)+[ \frac{1}{2} f&#x27;&#x27;(0)- \frac{1}{6}]x+ o(x) \to f&#x27;(0)= 1 \\
x^{3} \; \text{项除以} \; x^{2} \; \text{后随} \; x \to 0 \; \text{消失，对极限无约束} \; \Rightarrow f&#x27;&#x27;(0) \; \text{不能由该条件确定} \\
\text{结论：} \; f(0)=- 1 \; \text{，} \; \text{f′(0)=1} \; \text{，} \; \text{f&#x27;&#x27;(0)} \; \text{任意（如} \; f=- 1+x \; \text{与} \; f=- 1+x+x^{2} \; \text{都满足条件）}
\end{gathered}" width="734" height="326"></p>


**方法要点**：分式极限存在且分母为 <img class="fml" src="/formulas/025821bec71ad8.png" alt="x^{m}" width="29" height="33"> ⇒ 分子低于 <img class="fml" src="/formulas/025821bec71ad8.png" alt="x^{m}" width="29" height="33"> 阶的系数必须全为 0，<img class="fml" src="/formulas/025821bec71ad8.png" alt="x^{m}" width="29" height="33"> 阶系数等于极限值；**高于** <img class="fml" src="/formulas/025821bec71ad8.png" alt="x^{m}" width="29" height="33"> 阶的系数不受该极限约束。本题只「探到」二阶系数 `f′(0)`，探不到 `f″(0)`——判断条件究竟能确定几阶信息，是这类题的真正考点。

### 综 2 · 积分上限函数与微分方程（第 2、5、7 章）

题：设 `f(x)` 连续且 <img class="fml" src="/formulas/115587072090a6.png" alt="f(x)= e^{x}+ \int_{0}^{x}(x- t)f(t)dt" width="222" height="34">，求 `f(x)`。



<p class="fml-block"><img class="fml" src="/formulas/dba60ef416ac44.png" alt="\begin{gathered}
\text{(1)} \; \text{拆开：} \; f(x)= e^{x}+ x \int_{0}^{x} f(t)dt- \int_{0}^{x} t f(t)dt \\
\text{(2)} \; \text{求导：} \; f&#x27;(x)= e^{x}+ \int_{0}^{x} f(t)dt+ x f(x)- x f(x)= e^{x}+ \int_{0}^{x} f(t)dt \\
\text{(3)} \; \text{再求导：} \; f&#x27;&#x27;(x)= e^{x}+ f(x) \Rightarrow f&#x27;&#x27;- f= e^{x} \\
\text{(4)} \; \text{特征方程} \; r^{2}- 1=0 \Rightarrow \; \text{齐次解} \; C_{1}e^{x}+C_{2}e^{- x} \\
\lambda=1 \; \text{是单特征根} \; \Rightarrow \; \text{设特解} \; y*=A x e^{x} \; \text{，代入方程} \; y*&#x27;&#x27;- y*= e^{x} \; \text{计算：} \\
y*&#x27;=A(1+x)e^{x}, y*&#x27;&#x27;=A(2+x)e^{x} \Rightarrow y*&#x27;&#x27;- y*= 2A e^{x}= e^{x} \Rightarrow A=\frac{1}{2} \\
(5) f(x)= C_{1}e^{x}+ C_{2}e^{- x}+ \frac{1}{2} x e^{x} \\
\text{(6)} \; \text{由原式} \; f(0)=e^{0}=1 \; \text{；由} \; (2) f&#x27;(0)=e^{0}+0=1 \\
f(0)=C_{1}+C_{2}=1 \; \text{；} \; f&#x27;=C_{1}e^{x}- C_{2}e^{- x}+ \frac{1}{2}(1+x)e^{x} \Rightarrow f&#x27;(0)=C_{1}- C_{2}+ \frac{1}{2}=1 \\
\Rightarrow C_{1}=\frac{3}{4}, C_{2}=\frac{1}{4} \\
\text{结论：} \; f(x)= \frac{3}{4} e^{x}+ \frac{1}{4} e^{- x}+ \frac{1}{2} x e^{x}
\end{gathered}" width="653" height="410"></p>


**方法要点**：变限积分方程 → 求导化为微分方程 → 从原方程提取初始条件（这一步最易漏）。

### 综 3 · 二重积分 → 反常积分（第 5、10 章）

题：用二重积分计算泊松积分 <img class="fml" src="/formulas/288581f261d46a.png" alt="I= \int_{0}^\infty e^{- x^{2}}dx" width="119" height="34">。



<p class="fml-block"><img class="fml" src="/formulas/ed266e08d885da.png" alt="\begin{gathered}
\text{(1)} \; I^{2}=\left(\int_{0}^{\infty}e^{-x^{2}}dx\right)\left(\int_{0}^{\infty}e^{-y^{2}}dy\right)=\iint_{\text{第一象限}}e^{-(x^{2}+y^{2})}\,dxdy \\
\text{(2)} \; \text{化极坐标：} \; x=r \cos \theta, y=r \sin \theta, dxdy= r dr d\theta \; \text{，} \; \theta \text{∈[0,}\pi \text{/2], r∈[0,∞)} \\
(3) I^{2}= \int_{0}^{\frac{\pi}{2}}d\theta \int_{0}^\infty e^{- r^{2}} r dr=\left(\frac{\pi}{2}\right) \cdot[- \frac{1}{2} e^{- r^{2}}]_{0}^\infty=\left(\frac{\pi}{2}\right)\left(\frac{1}{2}\right)= \frac{\pi}{4} \\
(4) I= \frac{\sqrt{\pi}}{2} \approx 0.886227 \; \text{（取正根）}
\end{gathered}" width="583" height="172"></p>


**推广**：<img class="fml" src="/formulas/d342d59f64a0ff.png" alt="\int_{- \infty}^\infty e^{- x^{2}}dx= \sqrt{\pi}" width="142" height="35">（高斯积分，概率论正态分布归一化常数的来源）；<img class="fml" src="/formulas/849e4f3575b7ba.png" alt="\Gamma\left(\frac{1}{2}\right)=\sqrt{\pi}" width="98" height="33"> 由此得。

### 综 4 · 曲线积分 → 级数（第 11、12 章）

题：由 <img class="fml" src="/formulas/24e3ed629bd783.png" alt="x=2\sum\frac{(-1)^{n+1}\sin(nx)}{n}" width="164" height="36">（<img class="fml" src="/formulas/3bfdd9e869c7b0.png" alt="x \in(- \pi, \pi)" width="97" height="34">）导出 <img class="fml" src="/formulas/489d28fdc85a34.png" alt="\sum\frac{1}{(2k-1)^{2}}=\frac{\pi^{2}}{8}" width="118" height="36">，并说明为何取 <img class="fml" src="/formulas/962fc579a57209.png" alt="x=\frac{\pi}{2}" width="53" height="34"> 得 <img class="fml" src="/formulas/00b546d8c5e2c6.png" alt="\frac{\pi}{4}" width="19" height="33">。



<p class="fml-block"><img class="fml" src="/formulas/ee3352162ef3dc.png" alt="\begin{gathered}
\text{(1)} \; \text{傅里叶级数逐项积分（在收敛区间内合法）：} \\
\int_{0}^{x} t dt= \frac{2\sum(- 1)^{n+1}}{n} \int_{0}^{x} \sin nt dt \\
\frac{x^{2}}{2}= \frac{2\sum(- 1)^{n+1}(1- \cos nx)}{n^{2}} \\
\text{(2)} \; \text{取} \; x=\pi \; \text{：} \; \frac{\pi^{2}}{2}= 2\sum\frac{(-1)^{n+1}\left(1-(-1)^{n}\right)}{n^{2}}= 4\sum_{k \ge 1}\frac{1}{(2k- 1)^{2}} \\
\Rightarrow \sum_{k \ge 1}\frac{1}{(2k- 1)^{2}}= \frac{\pi^{2}}{8} \checkmark \\
\text{(3)} \; \text{原展开式取} \; x=\frac{\pi}{2} \; \text{：} \; \frac{\pi}{2}= 2\left(1- \frac{1}{3}+ \frac{1}{5}- \cdots\right) \Rightarrow \; \text{交错奇倒数和} \; = \frac{\pi}{4} \\
\text{(4)} \; \text{帕塞瓦尔：由} \; \text{|x|} \; \text{的余弦级数也可得} \; \sum\frac{1}{n^{2}}= \frac{\pi^{2}}{6}
\end{gathered}" width="591" height="329"></p>


**方法要点**：傅里叶级数既能「求和函数」也能「求数项和」；逐项积分后收敛性变好（系数多除一个 n）。

### 综 5 · 多元极值 ↔  条件极值 ↔  经济学（第 3、9 章）

题：在 <img class="fml" src="/formulas/022b0a63a48333.png" alt="x^{2}+y^{2}+z^{2}=1" width="134" height="34"> 下求 `f=xyz` 的最大值，并说明与微观经济学条件极值的关系。



<p class="fml-block"><img class="fml" src="/formulas/82dd7ecad7a23d.png" alt="\begin{gathered}
(1) L= xyz+ \lambda(x^{2}+y^{2}+z^{2}- 1) \\
(2) \frac{\partial L}{\partial x}= yz+2\lambda x= 0 \; \text{；同理} \; xz+2\lambda y=0 \; \text{、} \; xy+2\lambda z=0 \\
\text{(3)} \; \text{若} \; xyz=0 \; \text{，三式乘} \; \text{x,y,z} \; \text{后相等} \; \Rightarrow 2\lambda x^{2}=2\lambda y^{2}=2\lambda z^{2} \Rightarrow x^{2}=y^{2}=z^{2}=\frac{1}{3} \\
(4) f_{\max}=\left(\frac{1}{\sqrt{3}}\right)^{3}= \frac{1}{3\sqrt{3}} \approx 0.19245 \; \text{（取全正或两负一正）} \\
\text{(5)} \; \text{若} \; \text{xyz=0} \; \text{则} \; \text{f=0} \; \text{，非最大} \\
\text{(6)} \; \text{经济学对应：效用} \; \text{U(X,Y)} \; \text{在预算约束} \; \text{PxX+PyY=I} \; \text{下最大化，} \\
\text{拉格朗日条件即} \; MRS= \frac{Px}{Py} \; \text{；} \; \lambda \; \text{的边际解释为「收入的边际效用」}
\end{gathered}" width="646" height="265"></p>


**方法要点**：条件极值求出的只是候选点，还要比较边界/退化情形（本题 `xyz=0`）。

### 综 6 · 三大公式的选择（第 10、11 章）

题：计算 <img class="fml" src="/formulas/2ace5e6f3a0cdd.png" alt="\oiint _{\Sigma} x^{3} dydz+ y^{3} dzdx+ z^{3} dxdy" width="242" height="34">，<img class="fml" src="/formulas/e44ebcebe1d93c.png" alt="\sum" width="26" height="34"> 为球面 <img class="fml" src="/formulas/db65cef09de13d.png" alt="x^{2}+y^{2}+z^{2}=R^{2}" width="145" height="34"> 外侧。



<p class="fml-block"><img class="fml" src="/formulas/82819d9e99163a.png" alt="\begin{gathered}
\text{(1)} \; \text{高斯公式：} \; div A= 3x^{2}+3y^{2}+3z^{2}= 3r^{2} \\
\text{(2)} \; \text{原式} \; = \iiint _\Omega 3(x^{2}+y^{2}+z^{2})dV \; \text{，用球坐标：} \\
= 3 \int_{0}^{2\pi}d\theta \int_{0}^\pi \sin \phi d\phi \int_{0}^R \rho^{2} \cdot \rho^{2} d\rho \\
= 3 \cdot 2\pi \cdot 2 \cdot \frac{R^{5}}{5}= \frac{12\pi R^{5}}{5} \\
\text{(3)} \; \text{校验} \; \text{R=1} \; \text{、取} \; \text{A=(x,y,z)} \; \text{时原式} \; = 3V= 4\pi \; \text{（与前面例题一致）} \; \checkmark
\end{gathered}" width="574" height="198"></p>


**选择规则**：闭曲面且偏导连续 ⇒ 高斯；闭曲线平面 ⇒ 格林；空间闭曲线 ⇒ 斯托克斯；非闭 ⇒ 先补面/补线；有奇点 ⇒ 挖洞。

### 综 7 · 幂级数解微分方程（第 7、12 章）

题：用幂级数求 `y′=y, y(0)=1` 的解。



<p class="fml-block"><img class="fml" src="/formulas/921a9a43f0c55c.png" alt="\begin{gathered}
\text{(1)} \; \text{设} \; y= \sum_{n=0}^\infty a_{n} x^{n} \Rightarrow y&#x27;= \sum_{n=1}^\infty n a_{n} x^{n- 1} \\
\text{(2)} \; \text{代入：} \; \sum_{n=1}^\infty n a_{n} x^{n- 1}= \sum_{n=0}^\infty a_{n} x^{n} \\
\text{比较} \; x^{k} \; \text{系数：} \; (k+1)a_{k+1}= a_{k} \Rightarrow a_{k+1}= \frac{a_{k}}{k+1} \\
\text{(3)} \; \text{由} \; a_{0}= y(0)=1 \Rightarrow a_{n}= \frac{1}{n}! \\
(4) y= \sum \frac{x^{n}}{n}!= e^{x} \; \text{，收敛半径} \; R= \infty \; \text{（比值} \; |\frac{a_{n}}{a_{n+1}}|= n+1 \to \infty \; \text{）}
\end{gathered}" width="559" height="243"></p>


**意义**：把微分方程化为系数的递推关系；教材第十二章「微分方程的幂级数解法」即此，也是非初等函数（贝塞尔、勒让德）的定义方式。

### 综 8 · 答题模板：证明题四步法

面对「证明存在 ξ 使……」的中值定理证明题：
① **改写**：把待证式整理成 <img class="fml" src="/formulas/135bf43bf939de.png" alt="F&#x27;(\xi)=0" width="81" height="33"> 或 <img class="fml" src="/formulas/baaa3c35f0338f.png" alt="F&#x27;(\xi)=k" width="81" height="33">，明确中值定理类型；
② **构造函数**：反推 `F`（含积分因子 `e^{g(x)}`、或 <img class="fml" src="/formulas/fe01f67b61b489.png" alt="f(x)- kx" width="84" height="33">、或两端点差的形式）；
③ **验证条件**：写出 `F` 在闭区间连续、开区间可导、端点值相等（罗尔）或直接引用拉格朗日/柯西；
④ **得出结论**：注明 <img class="fml" src="/formulas/74c286feecc02e.png" alt="\xi \in(a,b)" width="76" height="33"> 且属于**开区间**，并检查是否要用到零点定理/介值定理先定位中间点。
凡含 `f″`、`f‴` 的题目，考虑「对 `f′` 用中值定理」或「两次罗尔」；含积分的题目考虑积分中值定理或变限函数。

---

## 易混概念对照

| # | 概念 A | 概念 B | 关键区别 |
| --- | --- | --- | --- |
| 1 | 函数相同 | 表达式相同 | 需定义域与对应规则都相同；`x` 与 <img class="fml" src="/formulas/67767bc057e81f.png" alt="\frac{x^{2}}{x}" width="24" height="33"> 定义域不同 |
| 2 | 极限存在 | 函数在该点有定义 | 极限是「去心」邻域行为，与该点函数值无关 |
| 3 | 无穷小 | 很小的数 | 无穷小是以 0 为极限的**变量**；0 是唯一为常数的无穷小 |
| 4 | 等价无穷小替换 | 泰勒展开 | 前者只能用于乘除因子；后者可处理加减与主阶抵消 |
| 5 | 连续 | 可导 | 可导必连续；连续未必可导（`|x|`） |
| 6 | 可导 | 可微 | 一元等价；多元可微强于偏导存在 |
| 7 | 驻点 | 极值点 | 驻点是 `f′=0`；极值点也可在不可导点，驻点也可能是鞍点 |
| 8 | 极值 | 最值 | 局部 vs 全局；闭区间最值还要比较端点 |
| 9 | 拐点 | 驻点 | 拐点是 `f″` 变号的曲线上的点（写坐标）；驻点是 `f′=0` 的 x 值 |
| 10 | 凹凸（凹/凸） | 函数凸性（优化） | 国内高数「凹=∪」与凸优化「凸=∪」命名易混，看定义 `f″` 符号 |
| 11 | 水平渐近线 | 斜渐近线 | 同一方向二者至多各一条；<img class="fml" src="/formulas/bded77789221e0.png" alt="x \to+ \infty" width="77" height="34"> 与 <img class="fml" src="/formulas/d65c3ba60d6455.png" alt="- \infty" width="39" height="33"> 分开求 |
| 12 | 罗尔 | 拉格朗日 | 罗尔要求 `f(a)=f(b)`；拉格朗日是其旋转不变推广 |
| 13 | 柯西中值定理 | 洛必达 | 前者是定理，后者是其推论（且洛必达有条件限制） |
| 14 | 佩亚诺余项 | 拉格朗日余项 | 局部 <img class="fml" src="/formulas/d684972d5c66b5.png" alt="o( \cdot)" width="34" height="33"> vs 整体含 <img class="fml" src="/formulas/4a819ecce90cdc.png" alt="\xi" width="16" height="33">；分别用于求极限与误差估计 |
| 15 | 原函数 | 定积分 | 前者是函数族（`+C`），后者是一个数 |
| 16 | 第一换元 | 第二换元 | 凑微分（不换变量）vs 令 <img class="fml" src="/formulas/8bbc1d63addef1.png" alt="x=\psi(t)" width="74" height="33">（要回代） |
| 17 | 分部积分 `u` 选取 | 换元顺序 | 「反对幂指三」取 u；换元看复合结构 |
| 18 | 积分上限函数 | 变限积分 | 前者 <img class="fml" src="/formulas/dc7efb8ea57a84.png" alt="\int_{a}^{x}" width="27" height="33">，后者上下限都变；求导通式不同 |
| 19 | 无穷区间反常积分 | 瑕积分 | <img class="fml" src="/formulas/50198a4f4d5d5d.png" alt="\int_{1}^\infty x^{- p}" width="62" height="33"> 收敛 p>1；<img class="fml" src="/formulas/27f2c2f87a8385.png" alt="\int_{0}^{1} x^{- p}" width="56" height="33"> 收敛 p<1（方向相反） |
| 20 | 绝对收敛（积分） | 条件收敛 | <img class="fml" src="/formulas/2e15010cd6335c.png" alt="\int\vert f\vert" width="43" height="33"> 收敛 ⇒ <img class="fml" src="/formulas/7cfeb56e9a7689.png" alt="\int f" width="33" height="33"> 收敛；反之不然 |
| 21 | 微元 `dU` | 增量 <img class="fml" src="/formulas/4b984252dd3408.png" alt="\Delta U" width="36" height="33"> | 要求 <img class="fml" src="/formulas/80bf32123b5cea.png" alt="\Delta U- dU=o(dx)" width="147" height="33">，即「以直代曲」的误差为高阶 |
| 22 | 弧长公式 | 旋转曲面面积 | <img class="fml" src="/formulas/5601640719f134.png" alt="\int \sqrt{1+y&#x27;^{2}}dx" width="110" height="33"> vs <img class="fml" src="/formulas/1301aab843c551.png" alt="2\pi \int y\sqrt{1+y&#x27;^{2}}dx" width="142" height="33"> |
| 23 | 齐次方程（一阶） | 齐次线性方程 | <img class="fml" src="/formulas/02db8c6f27ed0e.png" alt="y&#x27;=\phi\left(\frac{y}{x}\right)" width="85" height="34"> vs `y′+P(x)y=0`；同名不同义 |
| 24 | 线性方程齐次解 | 非齐次特解 | 通解 = 齐次通解 + 一个特解；特解不含任意常数 |
| 25 | 特征根重数 k | 待定系数 <img class="fml" src="/formulas/e2a88b944111e4.png" alt="x^{k}" width="25" height="34"> | λ 是特征方程的 k 重根 ⇒ 特解乘 <img class="fml" src="/formulas/e2a88b944111e4.png" alt="x^{k}" width="25" height="34">（共振） |
| 26 | 欧拉方程 | 欧拉公式 | <img class="fml" src="/formulas/2e5cbe7bb0504f.png" alt="x^{2}y&#x27;&#x27;+pxy&#x27;+qy=f" width="171" height="33"> vs <img class="fml" src="/formulas/679d009ab744b6.png" alt="e^{ix}=\cos x+i \sin x" width="154" height="34"> |
| 27 | 数量积 | 向量积 | 标量 vs 向量；交换 vs 反交换 |
| 28 | 混合积 | 行列式 | 混合积是三向量构成的三阶行列式；共面 ⇔ 为 0 |
| 29 | 平面法向量 | 直线方向向量 | 直线一般式方向 = 两平面法向量叉积 |
| 30 | 柱面 | 旋转曲面 | 方程缺一个变量 vs 由母线绕轴旋转生成 |
| 31 | 二重极限 | 累次极限 | 二重极限沿任意路径；累次极限是先后两次一元极限 |
| 32 | 偏导数存在 | 可微 | 多元中偏导存在 ⇏  连续、⇏  可微；偏导连续 ⇒ 可微 |
| 33 | 方向导数 | 梯度 | 方向导数是标量（沿某方向变化率）；梯度是向量（最大增长方向） |
| 34 | 全微分形式不变性 | 链式法则 | 前者说 <img class="fml" src="/formulas/194c4217ed717b.png" alt="dz=f_{u}du+f_{vdv}" width="136" height="33"> 形式不变，后者给出偏导的具体组合 |
| 35 | 无条件极值 <img class="fml" src="/formulas/d08e23b37ab082.png" alt="\Delta=AC- B^{2}" width="116" height="34"> | 条件极值拉格朗日 | 前者判驻点性质，后者处理带约束；λ 不是所求 |
| 36 | X 型 / Y 型区域 | 换序 | 前者是先 y 后 x / 先 x 后 y；换序要重画区域、必要时分块 |
| 37 | 极坐标 <img class="fml" src="/formulas/99198cf114b02e.png" alt="r dr d\theta" width="52" height="33"> | 球坐标 <img class="fml" src="/formulas/c3e877466aa74e.png" alt="\rho^{2}\sin \phi" width="62" height="34"> | 二维雅可比 vs 三维雅可比；φ 是与 z 轴夹角 |
| 38 | 第一类线积分 | 第二类线积分 | 对弧长（与方向无关）vs 对坐标（反向变号） |
| 39 | 第一类面积分 | 第二类面积分 | 对面积（无侧向）vs 对坐标（与侧有关） |
| 40 | 格林 | 高斯 | 平面闭曲线→二重积分 vs 空间闭曲面→三重积分 |
| 41 | 斯托克斯 | 高斯 | 曲面边界曲线 vs 体积边界曲面；分别对应旋度与散度 |
| 42 | 散度 | 旋度 | 标量（通量源）vs 向量（环流强度）；<img class="fml" src="/formulas/3460fa1fcb5db2.png" alt="\nabla \cdot( \nabla \times A)=0" width="131" height="34"> |
| 43 | 路径无关 | 全微分求积 | 单连通域内二者等价；判据 <img class="fml" src="/formulas/e42d7c24b4a713.png" alt="\frac{\partial P}{\partial y}= \frac{\partial Q}{\partial x}" width="74" height="36"> |
| 44 | 级数收敛 | 通项趋于 0 | 后者是必要条件非充分（调和级数） |
| 45 | 绝对收敛 | 条件收敛 | 前者可任意重排且和不变；后者重排可改变和 |
| 46 | 比值判别 | 根值判别 | 根值更强；<img class="fml" src="/formulas/71f55b31ab0f91.png" alt="\rho=1" width="49" height="34"> 二者都失效 |
| 47 | 收敛半径 | 收敛域 | 半径给出开区间，端点须单独判定才得收敛域 |
| 48 | 泰勒级数 | 傅里叶级数 | 局部导数信息 / 解析要求 vs 整体积分信息 / 允许间断 |
| 49 | 一致收敛 | 逐点收敛 | 一致收敛才保证和函数连续、可逐项积分与求导 |
| 50 | 狄利克雷收敛定理 | 莱布尼茨判别法 | 前者判傅里叶级数收敛值，后者判交错级数收敛 |

---

## 记号与术语速查

| 记号 | 读法 | 含义 |
| --- | --- | --- |
| <img class="fml" src="/formulas/cd08001f69456c.png" alt="\forall, \exists, \Rightarrow, \Leftrightarrow" width="90" height="33"> | 任意 / 存在 / 推出 / 等价 | 逻辑量词，ε–δ 定义的基础 |
| <img class="fml" src="/formulas/ab66c0596529bd.png" alt="\epsilon, \delta, N, M" width="83" height="33"> | 艾普西龙 / 德尔塔 | 极限定义中的任意小量与相应阈值 |
| <img class="fml" src="/formulas/d931c7a6486640.png" alt="o( \cdot), O( \cdot), \sim" width="99" height="33"> | 高阶无穷小 / 同阶 / 等价 | <img class="fml" src="/formulas/8f699d293649d4.png" alt="\alpha=o(\beta)" width="76" height="33"> 表示 <img class="fml" src="/formulas/22acf405be7bc1.png" alt="\lim \frac{\alpha}{\beta}= 0" width="80" height="35"> |
| `lim, sup, inf` | 极限 / 上确界 / 下确界 | 数列也常用上下极限 `limsup/liminf` |
| <img class="fml" src="/formulas/f3acc01c84ccec.png" alt="f&#x27;, f&#x27;&#x27;, f^{(n)}" width="85" height="33"> | 一阶 / 二阶 / n 阶导数 | 偏导用 <img class="fml" src="/formulas/16968b5cc7fbf4.png" alt="f_{x}, f_{xy}" width="55" height="33"> |
| <img class="fml" src="/formulas/a0538b9ab5f14d.png" alt="dy, \Delta y, dx" width="85" height="33"> | 微分 / 增量 / 自变量微分 | <img class="fml" src="/formulas/19d0f06d5e9e87.png" alt="\Delta y= dy+ o(\Delta x)" width="143" height="34"> |
| <img class="fml" src="/formulas/036f9076ca04b9.png" alt="\int, \iint , \iiint , \oint , \oiint" width="123" height="33"> | 不定/定积分 / 二重 / 三重 / 闭曲线 / 闭曲面 | `∮` 强调路径闭合 |
| <img class="fml" src="/formulas/c4cb8a1eb385a7.png" alt="\int_{a}^{x}, \int_{\alpha(x)}^{\beta(x)}" width="72" height="38"> | 积分上限函数 / 变限积分 | 求导用莱布尼茨通式 |
| <img class="fml" src="/formulas/3521054cfbadea.png" alt="\sum, \Pi" width="48" height="33"> | 求和 / 求积 | <img class="fml" src="/formulas/7349f1463fc090.png" alt="S_{n}" width="26" height="33"> 为部分和 |
| <img class="fml" src="/formulas/1757175cecadd8.png" alt="\nabla, \nabla \cdot, \nabla \times, \nabla^{2}" width="116" height="33"> | 梯度 / 散度 / 旋度 / 拉普拉斯算子 | Nabla 算子 |
| <img class="fml" src="/formulas/1afe1b9c68bd6a.png" alt="\partial, \frac{\partial(F,G)}{\partial}(u,v)" width="111" height="33"> | 偏导 / 雅可比行列式 | 隐函数方程组与重积分换元 |
| <img class="fml" src="/formulas/80d4e8c87ff042.png" alt="\rho, \phi, \theta, r" width="68" height="33"> | 球径 / 天顶角 / 方位角 / 极径 | 球坐标 <img class="fml" src="/formulas/e93c93e662956e.png" alt="\phi" width="18" height="34"> 是与 z 轴夹角 |
| <img class="fml" src="/formulas/90b7ed8dacc112.png" alt="\vert a\vert , a \cdot b, a \times b,[a b c]" width="153" height="33"> | 模 / 数量积 / 向量积 / 混合积 | 三种积结果类型不同 |
| <img class="fml" src="/formulas/d08e23b37ab082.png" alt="\Delta=AC- B^{2}" width="116" height="34"> | 判别式 | 二元极值判别；`H` 为海森矩阵 |
| <img class="fml" src="/formulas/379a0fdb92b50c.png" alt="\kappa, \rho=\frac{1}{\kappa}" width="70" height="33"> | 曲率 / 曲率半径 | 注意 ρ 与球坐标 ρ 同名不同义 |
| `R` | 收敛半径 | 收敛域需另判端点 |
| <img class="fml" src="/formulas/7e5696aec2d508.png" alt="a_{n}, b_{n}" width="48" height="34"> | 傅里叶系数 | 由三角函数系正交性得到 |

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
| 欧拉方程（ODE） | <img class="fml" src="/formulas/458ca1de941ea6.png" alt="Cauchy- Euler" width="137" height="33"> |
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
| 两个重要极限 | <img class="fml" src="/formulas/b298fc2aae7f3a.png" alt="\lim_{x \to 0} \dfrac{\sin x}{x}= 1" width="133" height="44">；<img class="fml" src="/formulas/aa153fcd2785f7.png" alt="\lim_{x \to \infty}\left(1+\frac{1}{x}\right)^{x}= e" width="166" height="33"> |
| <img class="fml" src="/formulas/638c8be7aac7e4.png" alt="1^\infty" width="29" height="33"> 速算 | <img class="fml" src="/formulas/fba9944268486d.png" alt="\lim f^g= e^{\lim g(f- 1)}" width="145" height="33">（<img class="fml" src="/formulas/13443ba212a097.png" alt="f \to 1, g \to \infty" width="116" height="33">） |
| 等价无穷小 | <img class="fml" src="/formulas/344ed45de374fc.png" alt="\sin x \sim \tan x \sim \arcsin x \sim \ln(1+x) \sim e^{x}- 1 \sim x" width="386" height="34">；<img class="fml" src="/formulas/d50c3c1a66502e.png" alt="1-\cos x \sim \frac{x^{2}}{2}" width="115" height="33">；<img class="fml" src="/formulas/772dbfa6d21bae.png" alt="(1+x)^\alpha- 1 \sim \alpha x" width="147" height="33">；<img class="fml" src="/formulas/a32bff933e21f1.png" alt="x-\sin x \sim \frac{x^{3}}{6}" width="115" height="33"> |
| 五个麦克劳林 | <img class="fml" src="/formulas/40931e03270efe.png" alt="e^{x}=\sum\frac{x^{n}}{n!}" width="87" height="34">；<img class="fml" src="/formulas/cc981edcc23f87.png" alt="\sin x=\sum\frac{(-1)^{n}x^{2n+1}}{(2n+1)!}" width="153" height="38">；<img class="fml" src="/formulas/5e24e03b8ca63a.png" alt="\cos x=\sum\frac{(-1)^{n}x^{2n}}{(2n)!}" width="144" height="38">；<img class="fml" src="/formulas/d95b3af4a0704d.png" alt="\ln(1+x)=\sum\frac{(-1)^{n-1}x^{n}}{n}" width="183" height="36">；<img class="fml" src="/formulas/2b1f7aadb59a38.png" alt="(1+x)^\alpha=1+\alpha x+\frac{\alpha(\alpha- 1)x^{2}}{2}+ \cdots" width="271" height="36"> |
| 泰勒余项 | 佩亚诺 <img class="fml" src="/formulas/9fd1de0541847c.png" alt="o((x- x_{0})^{n})" width="101" height="34">；拉格朗日 <img class="fml" src="/formulas/7fd406ee04b439.png" alt="\frac{f^{(n+1)}(\xi)(x- x_{0})^{n+1}}{n+1}!" width="121" height="37"> |
| 间断点 | 第一类（可去/跳跃，左右极限存在）；第二类（无穷/振荡） |
| 闭区间连续四性质 | 有界、最值、介值、零点定理 |

### A.2 导数与微分（第 2 章）

| 项目 | 公式 |
| --- | --- |
| 定义 | <img class="fml" src="/formulas/de3953bdf1f7e8.png" alt="f&#x27;(x_{0})=\lim \frac{f(x_{0}+\Delta x)- f(x_{0})}{\Delta x}" width="205" height="34">；`dy=f′(x)dx` |
| 四则 | `(uv)′=u′v+uv′`；<img class="fml" src="/formulas/3955fbd1ba4008.png" alt="\left(\frac{u}{v}\right)&#x27;=\frac{u&#x27;v- uv&#x27;}{v^{2}}" width="111" height="34"> |
| 链式 / 反函数 | <img class="fml" src="/formulas/432647bacff8e9.png" alt="\frac{dy}{dx}=f&#x27;(u)g&#x27;(x)" width="126" height="34">；<img class="fml" src="/formulas/d4a29afc9d98aa.png" alt="\dfrac{dx}{dy}=\dfrac{1}{y&#x27;}" width="72" height="48"> |
| 隐函数 / 参数 | <img class="fml" src="/formulas/5b356ff855960d.png" alt="\frac{dy}{dx}=- \frac{F_{x}}{F_{y}}" width="81" height="37">；<img class="fml" src="/formulas/6423431152458f.png" alt="\frac{dy}{dx}=\frac{\dot{y}}{\dot{x}}" width="61" height="34">，<img class="fml" src="/formulas/b05525fc180749.png" alt="\frac{d^{2}y}{dx^{2}}=\frac{\frac{d}{dt\left(\frac{dy}{dx}\right)}}{\dot{x}}" width="98" height="48"> |
| 对数求导 | <img class="fml" src="/formulas/016a0d786ae64d.png" alt="y=x^{x} \Rightarrow y&#x27;=x^{x}(\ln x+1)" width="215" height="34"> |
| 莱布尼茨 | <img class="fml" src="/formulas/db2512e2655eb3.png" alt="(uv)^{(n)}=\sum C(n,k)u^{(k)}v^{(n-k)}" width="232" height="34"> |
| 常用 n 阶 | <img class="fml" src="/formulas/fe49ed7e31e5de.png" alt="(\sin x)^{(n)}=\sin\left(x+\frac{n\pi}{2}\right)" width="191" height="34">；<img class="fml" src="/formulas/938db9f18e1a2d.png" alt="\left(\dfrac{1}{x+a}\right)^{(n)}=\dfrac{(-1)^{n}\,n!}{(x+a)^{n+1}}" width="204" height="56"> |

### A.3 中值定理与导数应用（第 3 章）

| 项目 | 公式 |
| --- | --- |
| 罗尔 / 拉格朗日 / 柯西 | <img class="fml" src="/formulas/5f4cd0741f20c3.png" alt="f&#x27;(\xi)=0" width="77" height="34">；<img class="fml" src="/formulas/83cd72e4d4dc2a.png" alt="f(b)- f(a)=f&#x27;(\xi)(b- a)" width="209" height="34">；<img class="fml" src="/formulas/e2f1c2ed724c3b.png" alt="\dfrac{f(b)- f(a)}{g(b)- g(a)}=\dfrac{f&#x27;(\xi)}{g&#x27;(\xi)}" width="164" height="50"> |
| 洛必达 | <img class="fml" src="/formulas/7341116d15fe27.png" alt="\lim \dfrac{f}{g}=\lim \dfrac{f&#x27;}{g&#x27;}" width="120" height="49">（须验证四前提） |
| 单调 / 凹凸 | `f′>0` 增；`f″>0` 凹（∪） |
| 极值充分 | <img class="fml" src="/formulas/b46c94de817f5c.png" alt="f&#x27;(x_{0})=0, f&#x27;&#x27;(x_{0})&lt;0" width="176" height="34"> 极大、`>0` 极小 |
| 渐近线 | 水平 `y=A`；铅直 <img class="fml" src="/formulas/8843865fe019e6.png" alt="x=x_{0}" width="58" height="34">；斜 <img class="fml" src="/formulas/4225394c250389.png" alt="a=\lim \frac{f}{x}, b=\lim(f- ax)" width="210" height="34"> |
| 曲率 | <img class="fml" src="/formulas/e5e29f440e596e.png" alt="\kappa=\dfrac{\vert y&#x27;&#x27;\vert}{(1+y&#x27;^{2})^{\frac{3}{2}}}" width="119" height="53">，<img class="fml" src="/formulas/ad0ac5ca8188b0.png" alt="\rho=\frac{1}{\kappa}" width="51" height="34"> |

### A.4 积分（第 4–6 章）

| 项目 | 公式 |
| --- | --- |
| 基本 | <img class="fml" src="/formulas/973db64307ff20.png" alt="\int x^{a}\,dx=\dfrac{x^{a+1}}{a+1}+C\ (a\ne -1)" width="240" height="48">；<img class="fml" src="/formulas/983d6b4fed6520.png" alt="\int\dfrac{dx}{x}=\ln\lvert x\rvert+C" width="140" height="46">；<img class="fml" src="/formulas/f20d5ff7533ab5.png" alt="\frac{\int dx}{a^{2}+x^{2}}=\left(\frac{1}{a}\right)\arctan\left(\frac{x}{a}\right)+C" width="215" height="35"> |
| 三类方法 | 第一换元 <img class="fml" src="/formulas/0922aa9def3137.png" alt="\int f(\phi)\phi &#x27;dx= \int f(u)du" width="185" height="34">；第二换元 <img class="fml" src="/formulas/8bbc1d63addef1.png" alt="x=\psi(t)" width="74" height="33">；分部 <img class="fml" src="/formulas/d92337e8f51e94.png" alt="\int u dv=uv- \int v du" width="160" height="34"> |
| 微积分基本定理 | <img class="fml" src="/formulas/e3e1cc20fa1579.png" alt="\Phi(x)= \int_{a}^{x}f(t)dt \Rightarrow \Phi &#x27;=f" width="216" height="34">；<img class="fml" src="/formulas/873998c398eaca.png" alt="\int_{a}^{b}f dx=F(b)- F(a)" width="177" height="35"> |
| 变限求导 | <img class="fml" src="/formulas/84c85427133d87.png" alt="\frac{d}{dx} \int_{\alpha(x)}^{\beta(x)}f= f(\beta)\beta &#x27;- f(\alpha)\alpha &#x27;" width="228" height="38"> |
| 区间再现 | <img class="fml" src="/formulas/a0a511dff3719f.png" alt="\int_{a}^{b}f(x)dx= \int_{a}^{b}f(a+b- x)dx" width="242" height="35">；<img class="fml" src="/formulas/f961e93c8b9013.png" alt="\int_{0}^\pi x f(\sin x)dx=\left(\frac{\pi}{2}\right) \int_{0}^\pi f(\sin x)dx" width="277" height="33"> |
| 华里士 | <img class="fml" src="/formulas/de7bc3f77add90.png" alt="I_{n}= \int_{0}^{\frac{\pi}{2}}\sin^{n}x dx" width="135" height="34">，<img class="fml" src="/formulas/68b43b5cf16c33.png" alt="I_{n}=\dfrac{n-1}{n}\,I_{n-2}" width="127" height="44">；偶 <img class="fml" src="/formulas/b6b8e75e7369d2.png" alt="\dfrac{(n-1)!!}{n!!}\cdot\dfrac{\pi}{2}" width="104" height="46">，奇 <img class="fml" src="/formulas/2bf227fd3d3ba8.png" alt="\dfrac{(n-1)!!}{n!!}" width="76" height="46"> |
| 反常积分 | <img class="fml" src="/formulas/50198a4f4d5d5d.png" alt="\int_{1}^\infty x^{- p}" width="62" height="33"> 收敛 ⇔ `p>1`；<img class="fml" src="/formulas/9b4264dd0440fb.png" alt="\int_{0}^{1}x^{- p}" width="56" height="34"> 收敛 ⇔ `p<1`；<img class="fml" src="/formulas/66e13a03582f70.png" alt="\int_{0}^\infty e^{- x^{2}}dx=\frac{\sqrt{\pi}}{2}" width="133" height="34"> |
| 微元法应用 | 面积 <img class="fml" src="/formulas/76033451cb66ca.png" alt="\int\vert f- g\vert dx" width="93" height="34">；极坐标 <img class="fml" src="/formulas/cf2fafc2af52e8.png" alt="\frac{1}{2} \int r^{2}d\theta" width="70" height="33">；体积 <img class="fml" src="/formulas/ac609748bd74fa.png" alt="\pi \int f^{2}dx" width="73" height="33">（绕 x）、<img class="fml" src="/formulas/77424cb695f2c1.png" alt="2\pi \int x f dx" width="85" height="33">（绕 y）；弧长 <img class="fml" src="/formulas/5601640719f134.png" alt="\int \sqrt{1+y&#x27;^{2}}dx" width="110" height="33">；功 <img class="fml" src="/formulas/1e89d96afa16d3.png" alt="\int F dx" width="55" height="34"> |

### A.5 微分方程（第 7 章）

| 类型 | 通解 / 解法 |
| --- | --- |
| 可分离 | <img class="fml" src="/formulas/a9b11d49f1ddad.png" alt="\frac{\int dy}{g(y)}= \int f(x)dx+C" width="164" height="37"> |
| 一阶线性 | <img class="fml" src="/formulas/73f3568c0d3794.png" alt="y=e^{- \int P}[ \int Q e^{\int P}dx+C]" width="206" height="34"> |
| 伯努利 | <img class="fml" src="/formulas/dbe67da308230c.png" alt="z=y^{1- n}" width="74" height="34"> 化线性 |
| 二阶常系数齐次 | <img class="fml" src="/formulas/843f276d8a3fa9.png" alt="r^{2}+pr+q=0" width="125" height="34">：不等实根 <img class="fml" src="/formulas/b1b57e2a570dad.png" alt="C_{1}e^{r_{1}x}+C_{2}e^{r_{2}x}" width="124" height="34">；重根 <img class="fml" src="/formulas/b0ed4ffb52ffad.png" alt="(C_{1}+C_{2}x)e^{rx}" width="115" height="34">；复根 <img class="fml" src="/formulas/d16810d5eeb1f3.png" alt="e^{\alpha x}(C_{1}\cos \beta x+C_{2}\sin \beta x)" width="208" height="34"> |
| 非齐次特解 | <img class="fml" src="/formulas/89df9223a16fd9.png" alt="y*=x^{k}e^{\lambda x}Q_{m}(x)" width="141" height="34">（`k` = λ 的特征根重数） |
| 欧拉方程 | <img class="fml" src="/formulas/54b3654cc929b5.png" alt="x=e^{t}" width="55" height="34"> 或设 <img class="fml" src="/formulas/c18de30dbca090.png" alt="y=x^{k}" width="58" height="34"> |

### A.6 空间解析几何（第 8 章）

| 项目 | 公式 |
| --- | --- |
| 三种积 | <img class="fml" src="/formulas/8a393b0d1808bf.png" alt="a\cdot b=a_{x}b_{x}+a_{y}b_{y}+a_{z}b_{z}" width="201" height="34">；<img class="fml" src="/formulas/b6270200a68017.png" alt="a \times b" width="46" height="34"> 为叉积分量；<img class="fml" src="/formulas/027de2732595ef.png" alt="[a b c]=(a \times b) \cdot c" width="139" height="34"> |
| 平面 | `Ax+By+Cz+D=0`，`n=(A,B,C)`；点面距 <img class="fml" src="/formulas/0cdaeffc29c03a.png" alt="d=\vert Ax_{0}+By_{0}+Cz_{0}+D\vert  \sqrt{A^{2}+B^{2}+C^{2}}" width="343" height="34"> |
| 直线 | <img class="fml" src="/formulas/4b90d815404f57.png" alt="\frac{x- x_{0}}{m}=\frac{y- y_{0}}{n}=\frac{z- z_{0}}{p}" width="152" height="36">，`s=(m,n,p)`；一般式 <img class="fml" src="/formulas/4c7879042b44db.png" alt="s=n_{1} \times n_{2}" width="97" height="34"> |
| 夹角 | 面面 `cosθ=|n1·n2|/(|n1||n2|)`；线面 `sinθ=|s·n|/(|s||n|)` |
| 异面直线距离 | <img class="fml" src="/formulas/d6189b6eaae687.png" alt="d=\vert [s_{1} s_{2} P_{1}P_{2}]\vert \vert s_{1} \times s_{2}\vert" width="191" height="34"> |
| 旋转曲面 | 绕 z 轴：<img class="fml" src="/formulas/627e57eeb28360.png" alt="f(y,z)=0 \Rightarrow f\left(\pm\sqrt{x^{2}+y^{2}}, z\right)=0" width="290" height="41"> |

### A.7 多元微分（第 9 章）

| 项目 | 公式 |
| --- | --- |
| 全微分 | <img class="fml" src="/formulas/51ad508a06f4b1.png" alt="dz=f_{x}dx+f_{y}dy" width="143" height="34">；可微要求 <img class="fml" src="/formulas/1052bc0ecb0699.png" alt="\Delta z- dz=o(\rho)" width="127" height="34"> |
| 链式 | <img class="fml" src="/formulas/496ae579401866.png" alt="z=f(u,v), u=u(x,y), v=v(x,y) \Rightarrow z_{x}=f_{u}u_{x}+f_{v}v_{x}" width="434" height="34"> |
| 隐函数 | <img class="fml" src="/formulas/96d584b3ea7ed8.png" alt="z_{x}=- \frac{F_{x}}{F_{z}}" width="79" height="35">；方程组用雅可比 <img class="fml" src="/formulas/344bc2cec6effa.png" alt="J=0" width="51" height="34"> |
| 方向导数 / 梯度 | <img class="fml" src="/formulas/2ef1923825bd10.png" alt="\frac{\partial f}{\partial l}= \nabla f \cdot e_{l}" width="102" height="34">（可微时）；<img class="fml" src="/formulas/8e7258f56c4ba7.png" alt="\nabla f=(f_{x},f_{y},f_{z})" width="135" height="34">；最大值 <img class="fml" src="/formulas/e33e4e9404c833.png" alt="\vert  \nabla f\vert" width="42" height="34"> |
| 切平面 / 法线 | <img class="fml" src="/formulas/18e8e692475702.png" alt="F_{x}(x- x_{0})+F_{y}(y- y_{0})+F_{z}(z- z_{0})=0" width="325" height="34">；法线方向 <img class="fml" src="/formulas/5b95371d9ff9cf.png" alt="\nabla F" width="36" height="33"> |
| 极值判别 | <img class="fml" src="/formulas/2396890f68d556.png" alt="A=f_{xx},B=f_{xy},C=f_{yy},\Delta=AC- B^{2}" width="324" height="34">；<img class="fml" src="/formulas/a1224bf4e91754.png" alt="\Delta&gt;0" width="55" height="34"> 且 `A<0` 极大、`A>0` 极小；<img class="fml" src="/formulas/b2e13ad93929c7.png" alt="\Delta&lt;0" width="54" height="34"> 鞍点 |
| 条件极值 | <img class="fml" src="/formulas/1b88f2432ba638.png" alt="L=f+\sum \lambda_{i}\phi_{i}" width="129" height="34">，解 <img class="fml" src="/formulas/13073bb17f8bc4.png" alt="\nabla L=0" width="67" height="34"> |

### A.8 重积分与线面积分（第 10–11 章）

| 项目 | 公式 |
| --- | --- |
| 二重积分 | X 型 <img class="fml" src="/formulas/01a640b2102bc9.png" alt="\int_{a}^{b}dx \int_{\phi_{1}}^{\phi_{2}}f dy" width="108" height="36">；极坐标 <img class="fml" src="/formulas/4dd81fc9b764d3.png" alt="\iint f(r \cos \theta,r \sin \theta) r dr d\theta" width="198" height="34"> |
| 三重积分 | 柱 <img class="fml" src="/formulas/9eb20b7e8b181e.png" alt="dV=r dr d\theta dz" width="117" height="34">；球 <img class="fml" src="/formulas/b525ea956cedcb.png" alt="dV=\rho^{2}\sin \phi d\rho d\phi d\theta" width="166" height="33">；一般 `dV=|J|du dv dw` |
| 曲面面积 | <img class="fml" src="/formulas/a3d45ef9660ab2.png" alt="A=\iint \sqrt{1+z_{x}^{2}+z_{y}^{2}}dxdy" width="207" height="42"> |
| 两类线积分 | <img class="fml" src="/formulas/1601f28d8c515c.png" alt="\int_{L} f ds" width="56" height="34">；<img class="fml" src="/formulas/3b83de5a578621.png" alt="\int_{L} Pdx+Qdy= \int(P \cos \alpha+Q \cos \beta)ds" width="315" height="34"> |
| 两类面积分 | <img class="fml" src="/formulas/8bdc92fcb173f1.png" alt="\iint _{\Sigma} f dS" width="67" height="34">；<img class="fml" src="/formulas/4336f6759d646a.png" alt="\iint _{\Sigma} P dydz+Q dzdx+R dxdy=\iint (P \cos \alpha+Q \cos \beta+R \cos \gamma)dS" width="518" height="34"> |
| 格林 | <img class="fml" src="/formulas/4c2bd5e9f6c996.png" alt="\oint _{L} Pdx+Qdy=\iint _{D}(Q_{x}- P_{y})dxdy" width="281" height="34"> |
| 高斯 | <img class="fml" src="/formulas/416db676667b04.png" alt="\oiint _{\Sigma} P dydz+Q dzdx+R dxdy=\iiint _\Omega(P_{x}+Q_{y}+R_{z})dV" width="430" height="34"> |
| 斯托克斯 | <img class="fml" src="/formulas/4a10ab0ba32122.png" alt="\oint _\Gamma A \cdot dl=\iint _{\Sigma}(rot A) \cdot n dS" width="213" height="34"> |
| 散度 / 旋度 | <img class="fml" src="/formulas/3d75162d7128f0.png" alt="div A=P_{x}+Q_{y}+R_{z}" width="174" height="34">；<img class="fml" src="/formulas/c8c172bfeacdc3.png" alt="rot A= \nabla \times A" width="118" height="34">；<img class="fml" src="/formulas/a190fe1d7958ab.png" alt="\nabla \times( \nabla f)=0" width="116" height="34">、<img class="fml" src="/formulas/3460fa1fcb5db2.png" alt="\nabla \cdot( \nabla \times A)=0" width="131" height="34"> |
| 路径无关 | 单连通域内 <img class="fml" src="/formulas/e451b6f83f5234.png" alt="P_{y}=Q_{x}" width="72" height="33"> ⇔ 闭路积分为 0 ⇔ 存在原函数 `u` |

### A.9 无穷级数（第 12 章）

| 项目 | 公式 |
| --- | --- |
| 必要条件 | <img class="fml" src="/formulas/f146c73d423019.png" alt="\sum u_{n}" width="47" height="34"> 收敛 ⇒ <img class="fml" src="/formulas/94a3c7476d4121.png" alt="\lim u_{n}=0" width="86" height="34"> |
| 基准级数 | <img class="fml" src="/formulas/9c1504b6aa06f9.png" alt="\sum q^{n}" width="46" height="34"> 收敛 ⇔ `|q|<1`；<img class="fml" src="/formulas/619d063f40addd.png" alt="\sum\frac{1}{n^{p}}" width="46" height="34"> 收敛 ⇔ `p>1`；<img class="fml" src="/formulas/1940dc88466fc9.png" alt="\sum\frac{1}{n(n+1)}=1" width="107" height="37"> |
| 比值 / 根值 | <img class="fml" src="/formulas/3510355471c888.png" alt="\rho=\lim \frac{u_{n+1}}{u_{n}}" width="97" height="35"> 或 <img class="fml" src="/formulas/0fe8f52adc9602.png" alt="\lim_{n\to\infty}\sqrt[n]{u_{n}}" width="102" height="34">；<img class="fml" src="/formulas/c66c05cf32fc3f.png" alt="\rho&lt;1" width="49" height="34"> 收敛、`>1` 发散、`=1` 失效 |
| 交错 | 莱布尼茨：<img class="fml" src="/formulas/2d58f9a3aa00af.png" alt="u_{n}↓0" width="53" height="34"> ⇒ 收敛，<img class="fml" src="/formulas/a1f6a72e650c0d.png" alt="\vert r_{n}\vert  \le u_{n+1}" width="92" height="34"> |
| 幂级数 | <img class="fml" src="/formulas/bd543fb093839f.png" alt="R=\lim\vert \frac{a_{n}}{a_{n+1}}\vert" width="111" height="36">；逐项求导/积分 R 不变 |
| 常用和函数 | <img class="fml" src="/formulas/add890e01e800e.png" alt="\sum x^{n}=\frac{1}{1- x}" width="98" height="34">；<img class="fml" src="/formulas/d468dd1daab909.png" alt="\sum n x^{n}=\frac{x}{(1- x)^{2}}" width="125" height="36">；<img class="fml" src="/formulas/6bcedc659ffee6.png" alt="\sum\frac{x^{n}}{n}=- \ln(1- x)" width="156" height="33">；<img class="fml" src="/formulas/e2050f5f9867f2.png" alt="\sum\frac{(-1)^{n+1}}{n}=\ln 2" width="127" height="35"> |
| 傅里叶系数 | <img class="fml" src="/formulas/5fc2f363d6d3b6.png" alt="a_{n}=\left(\frac{1}{\pi}\right) \int_{- \pi}^{\pi}f \cos nx dx" width="190" height="34">，<img class="fml" src="/formulas/25aa48714427ac.png" alt="b_{n}=\left(\frac{1}{\pi}\right) \int_{- \pi}^{\pi}f \sin nx dx" width="186" height="34"> |
| 狄利克雷 | 间断点收敛于 <img class="fml" src="/formulas/d83368e72257fe.png" alt="\frac{f(x^{-})+f(x^{+})}{2}" width="85" height="35"> |
| 帕塞瓦尔 | <img class="fml" src="/formulas/959a740f68b0f0.png" alt="\left(\frac{1}{\pi}\right) \int_{- \pi}^{\pi}f^{2}dx= \frac{a_{0}^{2}}{2}+\sum(a_{n}^{2}+b_{n}^{2})" width="255" height="36"> |

### A.10 一页纸解题索引

| 见到 | 立即想到 |
| --- | --- |
| `0/0` 且加减结构 | **泰勒展开**（不是等价无穷小替换），展开到主阶不抵消 |
| <img class="fml" src="/formulas/638c8be7aac7e4.png" alt="1^\infty" width="29" height="33"> / <img class="fml" src="/formulas/0aa24a18a957f4.png" alt="0^{0}" width="23" height="33"> / <img class="fml" src="/formulas/96377a713e77fc.png" alt="\infty^{0}" width="32" height="33"> | 取对数，<img class="fml" src="/formulas/b45769cf11de47.png" alt="e^{\lim g \ln f}" width="65" height="33"> 或 <img class="fml" src="/formulas/638c8be7aac7e4.png" alt="1^\infty" width="29" height="33"> 速算 |
| 递推数列极限 | 单调有界准则：先证有界、再证单调、最后解 `A=f(A)` |
| 分段点求导 / 连续性 | **用定义**算左右导数/极限，不代入公式 |
| 证明含 <img class="fml" src="/formulas/01a64f0906e047.png" alt="f&#x27;(\xi)" width="45" height="33"> | 构造辅助函数 + 罗尔；含比值 ⇒ 柯西 |
| 积分含根式 | 三角代换或整体代换；含 <img class="fml" src="/formulas/2eccecbce44f26.png" alt="x^{2}+a^{2}" width="62" height="33"> 想到 arctan |
| 对称区间积分 | 先查奇偶性；三角积分用区间再现 / 华里士 |
| 变限积分求导 | 通式；含参数先换元提出 |
| 反常积分判敛 | 先定类型（无穷区间 / 瑕点），再选 `p` 判别；瑕点在内部要拆 |
| 一阶微分方程 | 先判类型，线性用积分因子；除以 `g(y)` 记得补常数解 |
| 二阶常系数非齐次 | 特征根 → 齐次解 → 按共振重数设 <img class="fml" src="/formulas/e2a88b944111e4.png" alt="x^{k}" width="25" height="34"> 特解 |
| 空间直线一般式 | <img class="fml" src="/formulas/4c7879042b44db.png" alt="s=n_{1} \times n_{2}" width="97" height="34">；线面夹角用 `sin` |
| 多元「是否可微」 | 先查偏导连续（充分）；不满足则用定义 <img class="fml" src="/formulas/1052bc0ecb0699.png" alt="\Delta z- dz=o(\rho)" width="127" height="34"> |
| 条件极值 | 拉格朗日 <img class="fml" src="/formulas/46e5136118ab18.png" alt="L=f+\lambda \phi" width="96" height="34">，求出候选点后比较 |
| 二重积分算不动 | 换序 / 换极坐标；<img class="fml" src="/formulas/26b5cab20fb0b7.png" alt="e^{- y^{2}}" width="38" height="33"> 型必须换序 |
| 三重积分 | 含 <img class="fml" src="/formulas/f0c0ee88f1c9cc.png" alt="x^{2}+y^{2}" width="63" height="34"> 用柱坐标，含 <img class="fml" src="/formulas/4f872fcad6f607.png" alt="x^{2}+y^{2}+z^{2}" width="101" height="34"> 用球坐标 |
| 闭曲面积分 | 高斯（外侧）；有奇点先挖洞 |
| 闭曲线积分 | 平面用格林、空间用斯托克斯；非闭先补线 |
| 判级数敛散 | 先看通项 → 正项选比较/比值/根值 → 交错用莱布尼茨 → 再判绝对收敛 |
| 求和函数 | 逐项求导或积分化为几何级数，再还原并定常数 |
| 求数项级数和 | 构造幂级数或傅里叶级数，取合适的 `x` 代入 |

---

## 附录 B 易错点速查

1. 函数相同要求定义域与对应规则都相同，仅表达式化简相同不够（`x` 与 <img class="fml" src="/formulas/67767bc057e81f.png" alt="\frac{x^{2}}{x}" width="24" height="33">）。
2. 奇偶性判定的第一步是检查定义域是否关于原点对称。
3. <img class="fml" src="/formulas/6081008adda09c.png" alt="\sqrt{x^{2}}=|x|" width="83" height="33">，`arcsin(sin x)` 只在主值区间等于 `x`。
4. 极限定义是「去心」邻域，<img class="fml" src="/formulas/a3b963bcc12b7a.png" alt="f(x_{0})" width="49" height="33"> 无定义或不等于极限都不影响极限存在。
5. <img class="fml" src="/formulas/ad22a293df21a9.png" alt="\lim f= A&gt; 0 \Rightarrow" width="138" height="33"> 附近 `f>0`；但 `f>0` 只能推出 <img class="fml" src="/formulas/dcf3b07c0913dc.png" alt="\lim f \ge 0" width="78" height="34">（严格不等号会丢失）。
6. 极限四则运算要求各极限存在且分母极限非零；<img class="fml" src="/formulas/2d92d9933e8950.png" alt="\infty- \infty" width="64" height="33">、<img class="fml" src="/formulas/b6c5dce3826285.png" alt="0 \cdot_{\infty}" width="35" height="33"> 不能拆。
7. 无穷小是**变量**不是「很小的数」；0 是唯一为常数的无穷小。
8. 等价无穷小只能在**乘除因子**中替换；加减项替换前须确认主阶不抵消。
9. <img class="fml" src="/formulas/eb7ce2be406249.png" alt="\tan x- \sin \frac{x \sim x^{3}}{2}" width="126" height="34">，不是 `0`；<img class="fml" src="/formulas/a32bff933e21f1.png" alt="x-\sin x \sim \frac{x^{3}}{6}" width="115" height="33">。
10. 洛必达只适用于 `0/0`、<img class="fml" src="/formulas/5486ef8db66980.png" alt="\frac{\infty}{\infty}" width="24" height="33">，且 `lim f′/g′` 必须存在；`(x+sin x)/x` 是失效反例。
11. <img class="fml" src="/formulas/638c8be7aac7e4.png" alt="1^\infty" width="29" height="33"> 未定式须取对数或用 <img class="fml" src="/formulas/5c9a207a42a8a6.png" alt="e^{\lim g(f- 1)}" width="76" height="33">，不能把底数与指数分别取极限。
12. 佩亚诺余项用于局部求极限，拉格朗日余项用于整体误差估计，二者不可混用。
13. 有任意阶导数 ≠ 泰勒级数收敛到原函数（<img class="fml" src="/formulas/571c6f16def8ca.png" alt="e^{- \frac{1}{x^{2}}}" width="41" height="34"> 是反例）。
14. 可去间断与跳跃间断同属第一类；无穷与振荡属第二类。
15. 介值定理与零点定理要求**闭区间上连续**，开区间结论可能失效。
16. 可导 ⇒ 连续、连续 ⇒ 极限存在；反向均不成立（`|x|` 是最简反例）。
17. 一元「可导 ⇔ 可微」，多元「可微 ⇒ 偏导存在」且反之不成立。
18. 导函数可以不连续，但由达布定理导函数没有第一类间断点。
19. 分段点求导必须用定义算左右导数，不能直接代两侧导函数。
20. 参数方程二阶导数要「先对 t 求导再除以 ẋ」，不是 `ÿ/ẍ`。
21. <img class="fml" src="/formulas/983d6b4fed6520.png" alt="\int\dfrac{dx}{x}=\ln\lvert x\rvert+C" width="140" height="46">，绝对值不可省；不定积分不要漏 `+C`。
22. 罗尔定理三条件（闭连续、开可导、端点值相等）缺一不可（`|x|` 在 <img class="fml" src="/formulas/b768c3141a0411.png" alt="[- 1,1]" width="56" height="34">）。
23. 拉格朗日中值定理的 <img class="fml" src="/formulas/4a819ecce90cdc.png" alt="\xi" width="16" height="33"> 属于**开区间** `(a,b)`。
24. 柯西中值定理是洛必达的证明基础，不要把二者当成同一件事。
25. <img class="fml" src="/formulas/50a0a7c4e6ade6.png" alt="f&#x27;(x_{0})=0" width="86" height="34"> 只是极值的必要条件（可导时），驻点可能是鞍点。
26. 极值是局部概念、最值是全局概念；闭区间最值必须比较端点。
27. 拐点是曲线上的**点**（写坐标），`f″=0` 既非充分也非必要。
28. 水平/斜渐近线在 <img class="fml" src="/formulas/bded77789221e0.png" alt="x \to+ \infty" width="77" height="34"> 与 <img class="fml" src="/formulas/6aa1d0a3ab58c5.png" alt="x \to- \infty" width="76" height="34"> 要分别求，结果可不同。
29. 同一方向水平与斜渐近线至多各一条；有水平线时不必再求斜线。
30. 第一换元不换变量、第二换元必须**回代**；三角代换别把 `t` 留在答案里。
31. 分部积分取 `u` 按「反、对、幂、指、三」；循环型需两次分部后解方程。
32. <img class="fml" src="/formulas/7ff9b056d9bdd3.png" alt="e^{- x^{2}}" width="38" height="34">、`sin x/x`、<img class="fml" src="/formulas/424fbb4096c004.png" alt="\frac{1}{\ln} x" width="32" height="34"> 没有初等原函数，不要硬凑。
33. 有第一类间断点的函数没有原函数，但可能有定积分（可积 ≠ 有原函数）。
34. 积分上限函数 <img class="fml" src="/formulas/911ac546a85224.png" alt="\Phi" width="20" height="33"> 在 `f` 可积时连续，仅在 `f` 连续时可导。
35. 变限求导通式中下限项要带负号并乘 <img class="fml" src="/formulas/11baca015d82cf.png" alt="\alpha &#x27;(x)" width="47" height="34">。
36. 被积函数含积分上限变量 `x` 时，须先换元把 `x` 提到积分号外。
37. 对称区间上奇函数积分为 0、偶函数为两倍——前提是区间关于原点对称。
38. <img class="fml" src="/formulas/46484ca91bb163.png" alt="\int_{0}^{\frac{\pi}{2}}\sin^{2}x dx= \frac{\pi}{4}" width="129" height="34">，不是 <img class="fml" src="/formulas/f28e3637dd110b.png" alt="\frac{\pi}{2}" width="18" height="34">；华里士公式奇偶情形系数不同。
39. <img class="fml" src="/formulas/f70a70c45174b9.png" alt="\int_{1}^\infty x^{- p}dx" width="82" height="34"> 收敛 `p>1`，<img class="fml" src="/formulas/d7a9062b56b31b.png" alt="\int_{0}^{1}x^{- p}dx" width="76" height="34"> 收敛 `p<1`，方向相反最易记反。
40. 瑕点在积分区间**内部**必须拆成两段，一段发散即整体发散。
41. 反常积分不能用「柯西主值」冒充收敛。
42. 面积公式要加绝对值（或先求交点分段），否则上下曲线交叉会抵消。
43. 弧长是 <img class="fml" src="/formulas/5601640719f134.png" alt="\int \sqrt{1+y&#x27;^{2}}dx" width="110" height="33">，不是 <img class="fml" src="/formulas/e51f12f20cd485.png" alt="\int(1+y&#x27;)dx" width="97" height="34">。
44. 绕 y 轴的柱壳法与圆盘法积分变量不同，上下限不可混用。
45. 微元法要求 <img class="fml" src="/formulas/80bf32123b5cea.png" alt="\Delta U- dU=o(dx)" width="147" height="33">，即「以直代曲」的误差是高阶无穷小。
46. 「齐次方程 <img class="fml" src="/formulas/02db8c6f27ed0e.png" alt="y&#x27;=\phi\left(\frac{y}{x}\right)" width="85" height="34">」与「线性齐次方程 `Q=0`」同名不同义。
47. 可分离变量时除以 `g(y)` 会丢失 `g(y)=0` 的常数解。
48. 一阶线性通解中积分因子是 <img class="fml" src="/formulas/f3b8af3e3d17dc.png" alt="e^{\int P dx}" width="50" height="34">，符号写反会导致全题错误。
49. 特征根为重根时齐次解必须多乘 `x`；复根时别漏 <img class="fml" src="/formulas/c44b463475ec45.png" alt="e^{\alpha x}" width="31" height="34">。
50. 待定系数法的 <img class="fml" src="/formulas/e2a88b944111e4.png" alt="x^{k}" width="25" height="34"> 因子：<img class="fml" src="/formulas/da7676c04d86b3.png" alt="\lambda" width="18" height="34"> 是特征根的重数即 `k`，漏乘是最高频失分点。
51. 非齐次通解 = 齐次通解 + 一个特解；特解中不含任意常数。
52. 欧拉方程令 <img class="fml" src="/formulas/54b3654cc929b5.png" alt="x=e^{t}" width="55" height="34">；`x<0` 时用 <img class="fml" src="/formulas/b3c1cbea5751a5.png" alt="|x|=e^{t}" width="65" height="34">，别忽略定义域。
53. 初值问题要把全部常数用初始条件定出，常数个数等于方程阶数。
54. <img class="fml" src="/formulas/b6270200a68017.png" alt="a \times b" width="46" height="34"> 反交换、<img class="fml" src="/formulas/c6cd36ad6e62c2.png" alt="a \cdot b" width="37" height="34"> 交换；混合积是对换行列式变号。
55. 直线一般式的方向向量是两平面法向量的**叉积**，不是其中之一。
56. 线面夹角用 `sinθ=|s·n|/(|s||n|)`，面面夹角用 `cos`。
57. 点到平面距离公式分母是法向量的模 <img class="fml" src="/formulas/42a4454d617aff.png" alt="\sqrt{A^{2}+B^{2}+C^{2}}" width="129" height="34">，不要漏根号。
58. 曲面方程缺一个变量才是柱面；含 <img class="fml" src="/formulas/f0c0ee88f1c9cc.png" alt="x^{2}+y^{2}" width="63" height="34"> 且含 <img class="fml" src="/formulas/7033d70b38ae64.png" alt="z^{2}" width="23" height="34"> 的一般不是柱面。
59. 旋转曲面代换规则：绕 z 轴把 `y` 换成 <img class="fml" src="/formulas/0985f0252ca14b.png" alt="\pm\sqrt{x^{2}+y^{2}}" width="94" height="34">，别换错变量。
60. 二次曲面单叶/双叶由负号个数与右端符号共同决定。
61. 二重极限要求沿**任意路径**相同；有限条路径相同不能判存在。
62. 累次极限存在且不等 ⇒ 二重极限不存在；逆命题不成立。
63. 多元偏导数存在 ⇏  连续、⇏  可微；**偏导连续 ⇒ 可微**才是充分条件。
64. 方向导数定义式不要求可微；只有可微时才能用 <img class="fml" src="/formulas/1e49b7daf574c6.png" alt="\nabla f \cdot e_{l}" width="58" height="33">。
65. 梯度方向是增长最快方向，<img class="fml" src="/formulas/08db18faad599e.png" alt="- \nabla f" width="46" height="34"> 是下降最快方向。
66. 二阶混合偏导相等需要**连续**条件（克莱罗定理），不保证时可能不等。
67. 隐函数求导要求 <img class="fml" src="/formulas/05226f1e6b0d7e.png" alt="F_{z}=0" width="58" height="34">；方程组情形要求雅可比行列式 <img class="fml" src="/formulas/344bc2cec6effa.png" alt="J=0" width="51" height="34">。
68. 曲面法向量是 <img class="fml" src="/formulas/5b95371d9ff9cf.png" alt="\nabla F" width="36" height="33">；切平面公式里的系数取**该点处**的偏导值。
69. <img class="fml" src="/formulas/206398a2f375e1.png" alt="\Delta=AC- B^{2}&gt;0" width="149" height="34"> 时还要看 `A` 的符号；<img class="fml" src="/formulas/b2e13ad93929c7.png" alt="\Delta&lt;0" width="54" height="34"> 是鞍点；<img class="fml" src="/formulas/4a17320a23ee6e.png" alt="\Delta=0" width="55" height="34"> 判别失效。
70. 极值点也可能偏导不存在（如 <img class="fml" src="/formulas/2fddbc961196ee.png" alt="z=\sqrt{x^{2}+y^{2}}" width="114" height="34"> 在原点）。
71. 拉格朗日乘数 <img class="fml" src="/formulas/da7676c04d86b3.png" alt="\lambda" width="18" height="34"> 不是所求；求出的是候选点，还要比较或结合实际判断。
72. 闭区域最值必须同时检查内部驻点与**整个边界**。
73. 二重积分换序后若区域不是 X/Y 简单型，必须分块。
74. 极坐标面积元是 <img class="fml" src="/formulas/99198cf114b02e.png" alt="r dr d\theta" width="52" height="33">，漏 `r` 是最高频错误。
75. 球坐标体积元 <img class="fml" src="/formulas/759b4d979a79c9.png" alt="\rho^{2}\sin \phi d\rho d\phi d\theta" width="119" height="34">，<img class="fml" src="/formulas/e93c93e662956e.png" alt="\phi" width="18" height="34"> 是与 z 轴正向夹角（0 到 π）。
76. 三重积分「先二后一」与「先一后二」的截面/投影选择要看区域形状。
77. <img class="fml" src="/formulas/6015df7111c366.png" alt="\iint _{D} e^{- y^{2}}dxdy" width="105" height="34"> 型积分必须换序（先对 x），否则原函数非初等。
78. 第一类线积分与方向无关（上下限须小到大）；第二类与方向有关（反向变号）。
79. 第一类面积分无侧向；第二类面积分必须先定侧再投影。
80. 格林公式要求闭曲线**正向**（逆时针）且区域内偏导连续。
81. 高斯公式要求闭曲面取**外侧**；取内侧整体变号。
82. 区域内有奇点必须挖洞，<img class="fml" src="/formulas/27e44a67db6049.png" alt="\frac{x dy- y dx}{x^{2}+y^{2}}" width="61" height="36"> 是经典反例（结果 2π 不是 0）。
83. 非闭曲线/曲面用公式前要补线/补面，并减去补上部分的贡献。
84. 路径无关四等价只在**单连通域**内成立，含洞区域须另外检验。
85. `div A=0` 称无源场、`rot A=0` 称无旋场；<img class="fml" src="/formulas/3460fa1fcb5db2.png" alt="\nabla \cdot( \nabla \times A)=0" width="131" height="34">、<img class="fml" src="/formulas/a190fe1d7958ab.png" alt="\nabla \times( \nabla f)=0" width="116" height="34">。
86. 级数收敛的必要条件是通项趋于 0；调和级数说明它不充分。
87. `p` 级数 `p>1` 收敛、几何级数 `|q|<1` 收敛，是两个最常用比较基准。
88. 比值/根值法 <img class="fml" src="/formulas/71f55b31ab0f91.png" alt="\rho=1" width="49" height="34"> 时失效（<img class="fml" src="/formulas/3b869ac1188e0e.png" alt="\sum\frac{1}{n}" width="40" height="34"> 与 <img class="fml" src="/formulas/fee8346edec651.png" alt="\sum\frac{1}{n^{2}}" width="46" height="34"> 都是 <img class="fml" src="/formulas/71f55b31ab0f91.png" alt="\rho=1" width="49" height="34">）。
89. 根值判别强于比值判别；阶乘型用比值、`n` 次幂型用根值。
90. 交错级数莱布尼茨判收敛，但**绝对收敛性要另判**。
91. 绝对收敛可任意重排；条件收敛重排可改变和（黎曼定理）。
92. 幂级数收敛半径给出开区间，**端点必须单独判断**才得收敛域。
93. 逐项求导/积分后半径不变，但端点敛散可能改变。
94. 求和函数时别忘了由 `S(0)` 或极限确定积分常数。
95. 傅里叶级数在间断点收敛到左右极限的**平均值**，不是 `f(x)`。
96. 奇函数展开为正弦级数、偶函数为余弦级数；<img class="fml" src="/formulas/cc7cdbf17cc3cb.png" alt="[0,\pi]" width="45" height="34"> 上需先作奇/偶延拓。
97. 周期 `2l` 时把 `nx` 换成 <img class="fml" src="/formulas/118b4c4a326057.png" alt="\frac{n\pi x}{l}" width="34" height="34">，系数中 <img class="fml" src="/formulas/68babd24e5e7f4.png" alt="\frac{1}{\pi}" width="18" height="34"> 换成 `1/l`。
98. 一致收敛才保证和函数连续、可逐项积分与求导；逐点收敛不保证。
99. 所有计算题都应做一次交叉验算：积分结果求导、微分方程解代入原方程、级数和代入特值。
100. 中值定理证明题的 <img class="fml" src="/formulas/4a819ecce90cdc.png" alt="\xi" width="16" height="33"> 必须落在**开区间**；用零点定理时先验证端点异号。
101. 遇到「不存在 / 不成立」类命题，先想反例库（`|x|`、<img class="fml" src="/formulas/18c64475e69804.png" alt="x^{2} \sin\left(\frac{1}{x}\right)" width="80" height="34">、<img class="fml" src="/formulas/443259d666f1a6.png" alt="\sin\left(\frac{1}{x}\right)" width="60" height="34">、调和级数、鞍点）。
102. 单位与量纲要一致：物理应用题的面积、体积、功、压力不能混用变量。
103. 分段函数、含绝对值函数、含参数函数，一律先分情况讨论再计算。
104. 任何「等价」「充分必要」的表述都要检查逆命题；教材中大量定理只是充分条件。

---

::: tip 复习路线建议
**第一轮**：按 12 章正文过一遍，把每个 `danger` 与附录 B 对应条目对照；自己动手重画 18 张图（尤其黎曼和、中值定理几何、二重积分区域换序、球坐标、三大公式定向、判敛决策树）。
**第二轮**：只做「典型计算题逐步演算」12 题、各章末的证明链/反例库/判敛工具箱等进阶小节、8 个公式推导补遗、8 道跨章综合例题与 50 组易混概念对照，检验是否真正区分了概念；配合「各章高频题型清单」练「识别类型」的速度，重点复盘所有数值例题的手算过程与验算。
**第三轮**：用题库按章抽题，限时完成计算题；证明题严格套用「综 8 四步法」。
**考场检查清单**：① 定理条件写了吗（连续/可导/单连通/闭区间/正向）；② 常数 `C`、`+C`、`|x|`、`r`、<img class="fml" src="/formulas/c3e877466aa74e.png" alt="\rho^{2}\sin \phi" width="62" height="34"> 漏了吗；③ 分段与绝对值是否分情况；④ 结果是否做了求导/代入验算；⑤ 题目问的是「点」还是「值」、是「收敛」还是「绝对收敛」。
:::

