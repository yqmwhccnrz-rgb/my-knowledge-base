---
summary: "计算机组成与系统结构 全面详解笔记，共 9 章：计算机系统概述与性能评价、数据的机器级表示、运算方法与运算部件、存储器分层体系结构、指令系统、中央处理器、指令流水线、系统总线、输入/输出系统。覆盖补码与 IEEE 754、ALU 与浮点运算、Cache 映射与虚存地址变换、指令格式与寻址、单周期/多周期数据通路、流水线冒险与加速比、总线带宽、中断与 DMA。含 12 张自绘图、大量工作例题（数值演算）、对比表、公式速查与易错点，并对教材中偏旧的实例与现代实现作了补充修正。"
---

# 计算机组成与系统结构笔记

::: info 笔记概要
- **所属课程**：计算机组成原理 / 计算机系统结构（计算机类、软件工程等专业核心基础课）。
- **核心内容**：以「**指令集体系结构 ISA** 是软硬件交界面」为主线，向下深入数据的机器级表示、运算部件、存储器层次、CPU 数据通路与流水线、总线与 I/O；向上理解程序如何被编译、链接、装入并执行。重点抓三条线：① **数据怎么表示与运算**（补码、IEEE 754、定点/浮点运算）；② **指令怎么执行**（指令格式、寻址、数据通路、控制器、流水线）；③ **系统怎么提速**（局部性、Cache、虚存、并行与 I/O 方式），并用 CPI、AMAT、加速比等公式量化。
- **学习建议**：本书计算题比重大，务必能独立完成进制与补码转换、浮点编码与加减、Cache 地址划分与命中时间、页表/TLB 地址变换、扩展操作码、流水线时空图与加速比、总线带宽、磁盘存取时间等演算；每个公式都要能代入数值。
:::

## 全书目录

| 章 | 主题 | 核心考点 | 重要度 |
| --- | --- | --- | --- |
| 1 | 计算机系统概述 | 冯·诺依曼结构、层次化结构、ISA、性能评价（CPI/MIPS/Amdahl/SPEC） | ★★★ |
| 2 | 数据的机器级表示 | 数制、原/反/补/移码、IEEE 754、BCD/字符、大小端、校验码 | ★★★ |
| 3 | 运算方法与运算部件 | 补码加减与溢出、乘法（Booth）、除法、浮点五步运算、ALU | ★★★ |
| 4 | 存储器分层体系结构 | SRAM/DRAM、主存扩展、**Cache 映射与性能**、虚拟存储器与 TLB | ★★★ |
| 5 | 指令系统 | 指令格式、扩展操作码、寻址方式、CISC/RISC、过程调用 | ★★★ |
| 6 | 中央处理器 | 数据通路、单周期/多周期设计、硬连线与微程序控制器、异常中断 | ★★★ |
| 7 | 指令流水线 | 时空图、吞吐率/加速比/效率、三种冒险、多发射与超标量 | ★★★ |
| 8 | 系统总线 | 总线组成、事务与裁决、定时方式、**总线带宽**、总线标准 | ★★ |
| 9 | 输入/输出系统 | I/O 接口与端口编址、磁盘与 RAID、程序查询/中断/DMA/通道 | ★★ |
| 综 | 综合例题精讲 | 跨章节计算题完整演算（考前自检） | 复习用 |
| 附 A / B | 速查 | 公式结论速查表、易错点清单 | 复习用 |

---

## 第 1 章 计算机系统概述

### 1.1 计算机的功能与特性（★）

计算机是一种能**自动、高速、按程序**处理数字化信息的电子设备。其基本功能是**数据加工、数据存储、数据传送、控制**；区别于计算器的关键在于**存储程序（stored program）**：指令与数据以同等地位存放在存储器中，CPU 按地址取出指令、译码、执行，由程序计数器 PC 自动指向下一条指令。

### 1.2 计算机发展历程（★）

| 代 | 时期 | 逻辑元件 | 典型特征 |
| --- | --- | --- | --- |
| 第一代 | 1946 起 | 电子管 | ENIAC、IAS；机器语言/汇编，体积大、功耗高 |
| 第二代 | 1950s 末 | 晶体管 | 出现高级语言、批处理与多道程序 |
| 第三代 | 1960s 中 | 中小规模集成电路 | **IBM System/360 首次提出"体系结构"概念**，系列机兼容 |
| 第四代 | 1970s 起 | 大规模/超大规模集成电路 | 微处理器、个人计算机、并行与多核 |

- **摩尔定律**：芯片上晶体管数约每 18~24 个月翻一番（经验规律，非物理定律）；近十余年因功耗墙、内存墙与制程成本而明显放缓，性能提升转向**多核、异构加速器、专用领域架构 DSA 与先进封装**。
- 教材中的 Intel CPU 芯片性能比较表（<img class="fml" src="/formulas/3f977f21c1025b.png" alt="4004 \to 8080 \to \cdots \to Pentium 4" width="263" height="34">）体现的正是集成度、主频、线宽、数据/地址总线宽度的演进。

### 1.3 计算机系统的组成（★★★）

![冯·诺依曼结构与计算机系统层次](/coa/coa-vonneumann.svg)

- **硬件五大部件**：运算器、控制器、存储器、输入设备、输出设备。
  - **运算器 ALU**：算术/逻辑运算，含通用寄存器组与状态标志（N/Z/C/V）。
  - **控制器 CU**：PC、IR、指令译码器、时序与控制信号发生器，是"指挥中心"。
  - **存储器**：按地址访问的一维线性空间，指令与数据不加区分（靠执行阶段解释）。
  - CPU = 运算器 + 控制器（+ 现代的多级 Cache、MMU、流水线部件）。
- **软件**：系统软件（操作系统、编译/汇编程序、驱动程序、数据库管理系统）与应用软件。
- 三条信息流：**数据流**（在运算器、存储器、I/O 之间）、**控制流**（控制器发出）、**地址流**（指定访存位置）。

::: danger 易错 · 冯·诺依曼结构
- "存储程序"指**指令和数据都放在同一存储器、用同一套地址访问**，不是"程序存在硬盘里"。
- 现代计算机以**存储器/互连为中心**，而非以运算器为中心；指令与数据 Cache 分离只是实现层面的优化，ISA 层仍是统一地址空间。
- **ISA（指令集体系结构）** 是软硬件交界面：它规定数据类型与格式、指令格式、寻址方式、可访问寄存器、存储空间与编址、中断结构、I/O 编址方式、工作状态与存储保护；**微体系结构（流水线级数、Cache 大小、乱序与否）不属于 ISA**，同一 ISA 可有完全不同的实现。
:::

### 1.4 计算机系统的层次化结构（★★★）

自顶向下：最终用户 → 应用程序 → 高级语言（编译）→ 汇编语言（汇编）→ 操作系统/系统程序员 → **ISA 机器语言层** → 微体系结构（数据通路/控制器）→ 数字逻辑电路 → 器件物理。

- 上层是下层的**抽象**，下层是上层的**实现**；每一层都向上一层提供"服务"并隐藏细节。
- **程序开发与执行过程**：编辑源程序 → 编译成汇编 → 汇编成可重定位目标模块 → 链接（符号解析 + 重定位）生成可执行文件 → 装入主存（可能涉及动态链接与地址重定位）→ OS 创建进程、分配地址空间 → CPU 取指执行。
- 从"程序员视角理解硬件、从硬件视角理解程序"是本教材反复强调的思路：例如**局部性**影响程序性能，**对齐**影响访存次数，**过程调用约定**决定栈帧与寄存器使用。

### 1.5 计算机系统性能评价（★★★）

#### 1.5.1 基本指标与公式

| 指标 | 定义 / 公式 |
| --- | --- |
| 时钟周期 T | 主频 f 的倒数，<img class="fml" src="/formulas/7f8312a93b9d86.png" alt="T= \frac{1}{f}" width="55" height="36"> |
| **CPI** | 每条指令平均所需时钟周期数；加权平均 `CPI = Σ(指令 i 的 CPI × 该类指令占比)` |
| **CPU 时间** | `CPU 时间 = 指令数 IC × CPI × T = IC × CPI / f` |
| **MIPS** | 每秒百万条指令，<img class="fml" src="/formulas/1c84265ae5a6a1.png" alt="MIPS= \frac{f}{CPI \times 10^{6}}" width="143" height="35"> |
| MFLOPS | 每秒百万次浮点运算 |
| 吞吐率 / 响应时间 | 单位时间完成的任务数 / 单个任务从提交到完成的时间 |

**性能三要素**：指令数 IC（编译器与 ISA）、CPI（微体系结构）、时钟周期 T（工艺与流水线深度）。三者相互制约——提高主频可能增大 CPI，减少指令数可能增大 CPI。

::: tip 工作示例 · CPU 时间（教材习题风格）
某机器主频 `4 GHz`，程序 P 的指令数 <img class="fml" src="/formulas/bbeec630a6aff7.png" alt="8 \times 10^{9}" width="63" height="34"> 条，平均 `CPI = 1.25`：


<p class="fml-block"><img class="fml" src="/formulas/2584de61ba851d.png" alt="\begin{gathered}
\text{CPU} \; \text{时间} \; = IC \times \frac{CPI}{f}= 8 \times 10^{9} \times \frac{1.25}{4 \times 10^{9}}= \frac{10 \times 10^{9}}{4 \times 10^{9}}= 2.5 s \\
\text{若把主频提到} \; \text{5 GHz} \; \text{而} \; \text{CPI} \; \text{不变} \; \to \; \text{时间} \; \text{= 2.0 s} \; \text{（提速} \; \text{1.25} \; \text{倍）} \\
\text{若改用优化编译使指令数降为} \; 7 \times 10^{9} \; \text{但} \; \text{CPI} \; \text{升到} \; 1.5 \to \; \text{时间} \; = \frac{10.5 \times 10^{9}}{4 \times 10^{9}}= 2.625 s \; \text{（反而变慢）}
\end{gathered}" width="792" height="123"></p>


结论：不能只看主频或单一指标，必须综合 <img class="fml" src="/formulas/7a478c5594d2e1.png" alt="IC \times \frac{CPI}{f}" width="83" height="36">。
:::

::: tip 工作示例 · 加权 CPI 与两台机器比较
程序在某机器上 50% ALU 指令（CPI=1）、20% Load（CPI=5）、20% Store（CPI=5）、10% 分支（CPI=3）：


<p class="fml-block"><img class="fml" src="/formulas/72e03b8e5f4b0a.png" alt="CPI= 0.5 \times 1+ 0.2 \times 5+ 0.2 \times 5+ 0.1 \times 3= 0.5+ 1+ 1+ 0.3= 2.8" width="547" height="34"></p>


又设 M1 主频 1 GHz、CPI=4；M2 主频 1.2 GHz、CPI=2，同一程序指令数相同：


<p class="fml-block"><img class="fml" src="/formulas/615613b5af624d.png" alt="\text{M1} \; \text{时间} \; = \frac{IC \times 4}{1 \times 10^{9}}= 4IC ns M2 \; \text{时间} \; = \frac{IC \times 2}{1.2 \times 10^{9}} \approx 1.67IC ns \to M2 \; \text{约快} \; \text{2.4} \; \text{倍}" width="605" height="35"></p>


:::

#### 1.5.2 Amdahl 定律与加速比



<p class="fml-block"><img class="fml" src="/formulas/a26e01a8fc3e9b.png" alt="\text{系统加速比} \; S= \frac{T_{\text{旧}}}{T_{\text{新}}} = \frac{1}{(1- F)+ \dfrac{F}{S_{\text{局部}}}}" width="275" height="62"></p>


其中 `F` 是被改进部分在**原总时间**中所占比例，`S_局部` 是该部分自身的加速倍数。

::: tip 工作示例 · Amdahl 定律
某程序中浮点运算占执行时间的 `40%`，若把浮点部件加速 `10` 倍：


<p class="fml-block"><img class="fml" src="/formulas/f8006d44b1df53.png" alt="S= \frac{1}{(1- 0.4)+ \frac{0.4}{10}}= \frac{1}{0.6+ 0.04}= \frac{1}{0.64} \approx 1.5625" width="314" height="39"></p>


即使把浮点部件加速到无穷大（<img class="fml" src="/formulas/93c6d8d20a540a.png" alt="\frac{0.4}{\infty} \to 0" width="64" height="34">），整体加速比上限也只有 <img class="fml" src="/formulas/e4299408e76d2b.png" alt="\frac{1}{0.6} \approx 1.67" width="83" height="34">。**结论：优化必须针对占比最大的部分**；"只优化一小块代码"收益有限。

对比 **Gustafson 定律**：若问题规模随处理器数增大（保持并行时间不变），可扩展加速比 <img class="fml" src="/formulas/4863d152338471.png" alt="S= p- \alpha(p- 1)" width="138" height="34">，其中 α 为串行占比；它说明扩大问题规模时并行仍有价值。
:::

#### 1.5.3 基准程序与 MIPS 陷阱

- **基准程序（benchmark）**：用一组有代表性的真实程序评测性能，最著名的是 **SPEC**（`SPECint` 整数、`SPECfp` 浮点，后扩展为 SPEC CPU2006/2017 等），用几何平均汇总相对参考机的比值。
- **MIPS 不可靠**：MIPS 只反映 `f/CPI`，**不含指令数**。不同 ISA 完成同一任务所需指令数差别巨大；同一程序优化后可能指令数减少而 CPI 上升，MIPS 下降但总时间反而缩短。教材专门以例子说明「从 MIPS 数看，优化后速度反而变慢」。

::: tip 工作示例 · MIPS 陷阱
机器 A：主频 `100 MHz`、CPI=2 → <img class="fml" src="/formulas/5ff3edf760d86a.png" alt="MIPS_{A}= \frac{100}{2}= 50" width="160" height="34">；机器 B：主频 `200 MHz`、CPI=5 → <img class="fml" src="/formulas/25a82b17e16f5a.png" alt="MIPS_{B}= \frac{200}{5}= 40" width="159" height="34">。
若同一任务在 B 上编译出的指令数只有 A 的一半：


<p class="fml-block"><img class="fml" src="/formulas/782176af42359c.png" alt="\begin{gathered}
\text{A} \; \text{时间} \; = \frac{IC \times 2}{100MHz}= \frac{2IC}{1e8} B \; \text{时间} \; = \frac{0.5IC \times 5}{200MHz}= \frac{1.25IC}{1e8} \\
\text{B 更快，但} \; MIPS_{B}(40) \; \text{小于} \; MIPS_{A}(50) \; \text{——说明 MIPS 不能跨 ISA、跨编译器比较性能}
\end{gathered}" width="715" height="71"></p>


:::

### 1.6 概念辨析与现代视角

#### 1.6.1 几组高频易混概念

| 对比 | 关键区别 |
| --- | --- |
| **计算机组成 vs 体系结构** | 组成（organization）是实现 ISA 的硬件部件与互连（数据通路、Cache、流水线）；体系结构（architecture）是程序员可见的属性（指令、寄存器、寻址、存储模型） |
| **兼容性与系列机** | 同一 ISA 的不同实现可运行同一软件（向后兼容）；系列机靠"相同体系结构 + 不同组成"覆盖不同价位 |
| **固件 / 微程序** | 微程序把控制信号以微指令形式存于控制存储器，介于硬件与软件之间；现代高性能 CPU 多用硬连线 + 译码为微操作（μop） |
| **吞吐量 vs 响应时间** | 批处理/服务器关注吞吐率，交互式关注响应时间；两者优化手段可能冲突 |
| **字长 / 地址位数 / 数据总线宽度** | 三者不必相等：字长是运算/寄存器宽度，地址位数决定寻址空间，总线宽度决定一次传送位数 |

#### 1.6.2 现代视角补充（教材以单核、MIPS/IA-32、Pentium 4 为主）

- **并行层级**：指令级并行（流水线、多发射、乱序、SIMD 向量指令 AVX/SVE）→ 线程级并行（多核/超线程）→ 数据级并行（GPU、TPU/NPU）→ 请求级并行（多机集群）。
- **功耗墙与"暗硅"**：主频在 2005 年后基本停滞，性能提升靠多核、专用加速器与异构计算；**Dennard 缩放失效**使功耗密度成为首要约束。
- **Roofline 模型**：性能上限由「峰值算力」与「内存带宽 × 运算强度」共同决定，用于判断程序是计算受限还是访存受限。
- **评测陷阱**：应报告完整软硬件环境、编译器选项与数据集，避免只挑有利于自己的指标；SPEC 用几何平均而非算术平均，防止大数值程序主导结果。

::: danger 易错 · 性能评价
- 「主频越高机器越快」错误：还需看 CPI 与指令数；不同 ISA 之间尤其不能比主频/MIPS。
- Amdahl 定律里的 `F` 是**原执行时间占比**，不是代码行数占比。
- `CPU 时间 = IC × CPI / f` 中的 CPI 必须是**该程序**的加权平均 CPI，不能拿理论理想值 1 直接代入。
- 提升某一部件速度带来的整体收益恒小于 <img class="fml" src="/formulas/17a8a6e59957d1.png" alt="\frac{1}{1- F}" width="37" height="35">；"局部加速无穷大 → 整体无穷快"是错的。
:::

---

## 第 2 章 数据的机器级表示

### 2.1 进位计数制与转换（★★）

- 常用进制：二进制 B / 八进制 O / 十进制 D / 十六进制 H；`R` 进制按权展开 <img class="fml" src="/formulas/8fa8f1d2f53a56.png" alt="\sum d_{i} \times R^{i}" width="84" height="34">。
- **二 ↔  十六**：每 4 位二进制对应 1 位十六进制（因此十六进制是二进制的紧凑写法）；二 ↔  八 每 3 位一组。
- **十 → 二**：整数部分"除 2 取余，逆序排列"，小数部分"乘 2 取整，顺序排列"（小数可能无限循环，故 0.1 无法用有限二进制精确表示）。

::: tip 工作示例 · 进制转换
`0x3A5F` → <img class="fml" src="/formulas/d8e33478e51d0c.png" alt="0011 1010 0101 1111_{2}" width="157" height="34"> → 十进制 <img class="fml" src="/formulas/e4e40046620823.png" alt="3 \times 4096+ 10 \times 256+ 5 \times 16+ 15= 14943" width="340" height="34">。
十进制 `0.625` → 二进制 `0.101`（<img class="fml" src="/formulas/a97dbef9fac3f2.png" alt="0.625 \times 2=1.25" width="134" height="34"> 取 1；<img class="fml" src="/formulas/9570256005e5f1.png" alt="0.25 \times 2=0.5" width="116" height="34"> 取 0；<img class="fml" src="/formulas/18cab45309d232.png" alt="0.5 \times 2=1.0" width="107" height="34"> 取 1）。
:::

### 2.2 定点数与浮点数（★★）

| 表示 | 小数点位置 | 特点 |
| --- | --- | --- |
| **定点数** | 固定（纯整数 / 纯小数） | 硬件简单，但表示范围与精度不可兼得 |
| **浮点数** | 随阶码浮动 <img class="fml" src="/formulas/174f8a70db69ed.png" alt="N= M \times R^E" width="113" height="34"> | 范围大，精度由尾数位决定；运算需对阶/规格化 |

### 2.3 整数的机器级表示（★★★）

![数据的机器级表示与 IEEE 754](/coa/coa-datarep.svg)

- **无符号整数**：全部位表示数值，n 位范围 <img class="fml" src="/formulas/ff76362d98a33a.png" alt="0 \sim 2^{n}- 1" width="88" height="34">。
- **带符号整数的四种编码**（以 n=8、真值 −5 为例）：

| 编码 | +5 | −5 | 规则 |
| --- | --- | --- | --- |
| 原码 | `0000 0101` | `1000 0101` | 最高位为符号位，其余为绝对值 |
| 反码 | `0000 0101` | `1111 1010` | 负数：原码符号位不变、数值位取反 |
| **补码** | `0000 0101` | `1111 1011` | 负数：反码 + 1；或"从右向左第一个 1 之后取反" |
| 移码 | `1000 0101` | `0111 1011` | 补码符号位取反；`[X]移 = 2^(n−1) + X`，便于比较大小 |

- **n 位补码范围** <img class="fml" src="/formulas/98baf1211e5807.png" alt="- 2^{n- 1} \sim 2^{n- 1}- 1" width="142" height="34">（8 位为 <img class="fml" src="/formulas/1295480bb76d11.png" alt="- 128" width="47" height="34">）；**0 的表示唯一**；<img class="fml" src="/formulas/e44aaeff3d7cff.png" alt="- 2^{n- 1}" width="54" height="34"> 的补码是 <img class="fml" src="/formulas/5e77dcbfce9ad9.png" alt="1000 \cdots 0" width="79" height="34">（原码无法表示）。
- **补码的意义**：`[X+Y]补 = [X]补 + [Y]补`、`[X−Y]补 = [X]补 + [−Y]补`，符号位参与运算、进位丢弃，硬件只需加法器。
- **符号扩展**：正数补 0、负数补 1（保持值不变）；**零扩展**用于无符号数。
- **C 语言整数**：`char/short/int/long` 有符号与 `unsigned` 版本；**有符号与无符号混合运算时，有符号数被隐式转换为无符号**，是经典 bug 来源（如 <img class="fml" src="/formulas/ecf99a7da9e194.png" alt="- 1&lt; 1U" width="77" height="34"> 为假）；溢出对无符号数是模 <img class="fml" src="/formulas/1475105e7f5cff.png" alt="2^{n}" width="24" height="34"> 回绕，对有符号数在 C 标准中是**未定义行为**。

::: tip 工作示例 · 补码换算
求 <img class="fml" src="/formulas/86ce001b29de44.png" alt="- 100" width="48" height="34"> 的 8 位补码：`+100 = 0110 0100` → 取反 `1001 1011` → 加 1 = `1001 1100`（`0x9C`）。
已知 8 位补码 `0x9C`：最高位为 1 是负数 → 取反加 1 得 `0110 0100 = 100` → 真值 <img class="fml" src="/formulas/86ce001b29de44.png" alt="- 100" width="48" height="34">。
:::

### 2.4 实数的表示与 IEEE 754（★★★）

- **一般浮点格式**：<img class="fml" src="/formulas/2ac6422345e156.png" alt="N=(- 1)^S \times M \times R^E" width="180" height="34">；阶码 E 常用**移码**（便于比较大小），尾数 M 常用**原码/补码小数**，基数 R 隐含为 2。
- **规格化**：调整阶码使尾数最高数值位为有效位（二进制即 `1.xxxx`），以最大化有效精度。规格化后 IEEE 754 可**隐藏最高位 1**，尾数字段只存小数部分。
- **IEEE 754 单精度（32 bit）**：`S(1) | E(8, bias=127) | M(23)`；真值 <img class="fml" src="/formulas/90bc4e9b45b0eb.png" alt="=(- 1)^S \times(1.M) \times 2^{E- 127}" width="211" height="34">；**双精度（64 bit）** `S(1) | E(11, bias=1023) | M(52)`。

| E 与 M 取值 | 表示 |
| --- | --- |
| `E = 0, M = 0` | ±0（由符号位决定） |
| <img class="fml" src="/formulas/87b93be965ca91.png" alt="E= 0, M= 0" width="114" height="34"> | **非规格化数** <img class="fml" src="/formulas/0931fdad1e46a7.png" alt="0.M \times 2^{- 126}" width="100" height="34">，用于表示接近 0 的极小值、实现渐进下溢 |
| <img class="fml" src="/formulas/834764c3ab0a26.png" alt="1 \le E \le 254" width="105" height="34"> | 规格化数 <img class="fml" src="/formulas/0aa7d2db2169e4.png" alt="1.M \times 2^{E- 127}" width="110" height="34"> |
| `E = 255, M = 0` | ±∞ |
| <img class="fml" src="/formulas/d26986c14e17cf.png" alt="E= 255, M= 0" width="131" height="34"> | **NaN**（非数，如 0/0、√−1） |

::: tip 工作示例 · 十进制转 IEEE 754 单精度
把 <img class="fml" src="/formulas/c4131fe8281abb.png" alt="- 12.75" width="62" height="34"> 编码为 32 位浮点：
```text
① 转二进制：$12.75=1100.11_{2}=1.10011_{2}\times 2^{3}$
② 符号 S = 1（负数）
③ 阶码 E = 3 + 127 = 130 = 1000 00102
④ 尾数 M = 去掉隐藏位后的 10011，右补 0 到 23 位 = 1001 1000 0000 0000 0000 000
⑤ 拼接：1 | 10000010 | 10011000000000000000000
        = 1100 0001 0100 1100 0000 0000 0000 0000 = 0xC14C0000
```
反向：`0x41200000` → `S=0, E=130→指数3, M=010…0 → 1.012 × 2³ = 1.25×8 = 10.0`。
:::

::: danger 易错 · 浮点数
- **浮点运算不满足结合律**：`(a+b)+c` 与 `a+(b+c)` 可能不同，因为对阶右移会丢失低位。
- 单精度约 7 位十进制有效数字、双精度约 16 位；<img class="fml" src="/formulas/95b6341cd570ff.png" alt="0.1+ 0.2= 0.3" width="121" height="34">（二进制无限循环），金融计算用 `BigDecimal`/十进制浮点。
- 阶码上溢 → ∞、下溢 → 0 或非规格化数；非规格化数的隐藏位是 **0** 而不是 1。
- IEEE 754 默认舍入为"就近偶数（round to nearest, ties to even）"，不是简单的四舍五入。
:::

### 2.5 十进制数与非数值数据（★★）

- **十进制数表示**：① 用 ASCII 字符逐个表示（便于显示，不便运算）；② **BCD 码**（8421 码，4 bit 表示 1 位十进制数，<img class="fml" src="/formulas/c73b7d7239a905.png" alt="12 \to 0001 0010" width="124" height="34">），分压缩（1 B 存 2 位）与非压缩（1 B 存 1 位）。BCD 加法结果大于 9 时需**加 6 修正**。
- **逻辑值**：用一位或一字节表示真/假（C 语言中 0 为假、非 0 为真）。
- **西文字符**：ASCII 7 bit（128 个字符），扩展用 1 字节；控制字符（如 LF=0x0A）不显示。
- **汉字**：输入码 → 机内码（GB2312/GBK 双字节、Unicode 码点）→ 字形码（点阵/矢量）；UTF-8 是变长 1~4 字节编码，兼容 ASCII。

### 2.6 数据宽度、存储与校验（★★★）

- **单位**：位 bit、字节 B（`1 B = 8 bit`）、字 word（字长由 CPU 决定）；<img class="fml" src="/formulas/18124d5629929d.png" alt="1 KB= 2^{10} B" width="107" height="34">，注意与网络速率单位 <img class="fml" src="/formulas/6e8780167050dc.png" alt="\frac{1 kbit}{s}= \frac{10^{3} bit}{s}" width="99" height="34"> 的区别。
- **字节序**：**大端**（高位字节在低地址，网络字节序、部分 RISC）与**小端**（低位字节在低地址，x86、多数 ARM）。多字节对象跨平台传输必须转换；位域、结构体打包也受字节序影响。
- **对齐**：数据地址是其长度的整数倍时一次访存即可取到；未对齐可能触发多次访存甚至（在某些架构上）异常。结构体成员顺序会影响 `sizeof`。
- **数据校验码**：

| 校验码 | 原理 | 能力 |
| --- | --- | --- |
| 奇偶校验 | 使 1 的个数为奇/偶 | 只能检**奇数位**错，无纠错能力 |
| **海明码** | 多重奇偶校验，校验位放在 <img class="fml" src="/formulas/c72dae4f8013bf.png" alt="2^{i}" width="21" height="34"> 位置 | 可**纠 1 位错 / 检 2 位错**（SEC-DED 加总校验位） |
| CRC | 模 2 除法生成冗余码 | 检多位突发错，用于磁盘、网络 |

::: tip 工作示例 · 海明码校验位数
数据 `n = 8` 位，需校验位 k 满足 <img class="fml" src="/formulas/f10fa185bf9c8b.png" alt="2^{k} \ge n+ k+ 1" width="121" height="34">：


<p class="fml-block"><img class="fml" src="/formulas/3892b223e5740d.png" alt="k=3: 8 \ge 8+3+1=12 \times k=4: 16 \ge 8+4+1=13 \checkmark \to \; \text{需} \; \text{4} \; \text{位校验位，总} \; \text{12} \; \text{位}" width="679" height="33"></p>


校验位放在第 `1, 2, 4, 8` 位；接收端由各校验组重算得到"指错字"，其值就是出错位的位置（全 0 表示无错）。主存常用 **ECC（SEC-DED）** 内存，能纠 1 位、检 2 位错。
:::

### 2.7 编码细节与现代浮点格式

#### 2.7.1 补码、移码与 C 语言陷阱



<p class="fml-block"><img class="fml" src="/formulas/1113d554f87ba3.png" alt="\begin{gathered}
\text{[X]} \; \text{补} \; \text{+ [Y]} \; \text{补} \; \text{= [X+Y]} \; \text{补} \; \text{（模} \; 2^{n} \; \text{）} \\
[- Y] \; \text{补} \; \text{= [Y]} \; \text{补} \; \text{连同符号位按位取反、末位加} \; \text{1} \\
\text{移码：同一真值的移码与补码只差符号位；移码全} \; \text{0} \; \text{对应最小真值，便于浮点阶码比较}
\end{gathered}" width="686" height="84"></p>



| 陷阱 | 说明 |
| --- | --- |
| 有符号溢出 | C 中未定义行为；硬件用 <img class="fml" src="/formulas/ca2a02ca719c74.png" alt="C_{n} ⊕ C_{n- 1}" width="87" height="33"> 或双符号位检测 |
| 有符号/无符号混合 | 有符号被隐式转为无符号，<img class="fml" src="/formulas/ecf99a7da9e194.png" alt="- 1&lt; 1U" width="77" height="34"> 结果为假 |
| 移位 | 算术右移补符号位、逻辑右移补 0；左移丢高位，右移丢低位 |
| 类型转换 | 短→长要符号扩展（有符号）或零扩展（无符号）；长→短直接截断 |

#### 2.7.2 IEEE 754 的边界与新型浮点格式

- **表示范围**（单精度）：规格化最小正数 <img class="fml" src="/formulas/84fe44f244dd3f.png" alt="\approx 1.18 \times 10^{-38}" width="121" height="33">（<img class="fml" src="/formulas/68c321bea8e3b8.png" alt="2^{-126}" width="45" height="33">），最大 <img class="fml" src="/formulas/5e35ba5e680dbb.png" alt="\approx 3.40 \times 10^{38}" width="110" height="33">；非规格化最小正数 <img class="fml" src="/formulas/08dc49cfe6ccb9.png" alt="\approx 1.4 \times 10^{-45}" width="112" height="33">（<img class="fml" src="/formulas/709d4fc6e6b298.png" alt="2^{-149}" width="45" height="33">）。
- **相对误差**：单精度机器精度 <img class="fml" src="/formulas/8ac8c790a8b4b0.png" alt="\epsilon= 2^{-23} \approx 1.19 \times 10^{-7}" width="182" height="33">，双精度 <img class="fml" src="/formulas/319765ae05b788.png" alt="2^{-52} \approx 2.22 \times 10^{-16}" width="158" height="33">。
- **现代补充**（教材只讲单/双精度）：**半精度 FP16**（E5/M10，深度学习推理）、**bfloat16**（E8/M7，保留与 FP32 相同的指数范围，训练常用）、**FP8**、NVIDIA **TF32**、**融合乘加 FMA**（一次舍入，精度更高）；IEEE 754-2008 还定义了十进制浮点与多精度格式。
- **NaN 传播**：`NaN != NaN` 恒为真；比较运算遇到 NaN 需特殊处理。

::: danger 易错 · 数据表示
- 原码/反码的 ±0 有两种表示（`0000 0000` 与 `1000 0000` / `1111 1111`），补码与移码 0 唯一。
- 8 位补码 `1000 0000` 是 <img class="fml" src="/formulas/1295480bb76d11.png" alt="- 128" width="47" height="34">，**没有对应的 8 位原码/反码**；对它取反加 1 仍是它自己。
- 移码用于阶码时偏置值单精度是 **127**（不是 128），双精度 **1023**；`E` 字段存的是 `真指数 + bias`。
- 海明码的条件是 <img class="fml" src="/formulas/f10fa185bf9c8b.png" alt="2^{k} \ge n+ k+ 1" width="121" height="34">（n 为数据位、k 为校验位），不要写成 <img class="fml" src="/formulas/0fcbe5d667c872.png" alt="2^{k} \ge n+ k" width="90" height="33">。
:::

---

## 第 3 章 运算方法与运算部件

### 3.1 运算器与算术逻辑单元（★★★）

![加法器、ALU 与补码加减运算](/coa/coa-alu.svg)

- **一位全加器**：`S = A ⊕ B ⊕ C_in`，<img class="fml" src="/formulas/7035397a08e6db.png" alt="C_{out}= A \cdot B+(A⊕B) \cdot C_{in}" width="226" height="33">；记 <img class="fml" src="/formulas/fab2acfed683d3.png" alt="G= A \cdot B" width="86" height="33">（进位生成）、`P = A⊕B`（进位传递），则 <img class="fml" src="/formulas/91778c39bb3043.png" alt="C_{out}= G+ P \cdot C_{in}" width="150" height="33">。
- **n 位加法器**：行波进位（RCA）逐级等待，时延 ∝ n；**先行进位（CLA）**把各级进位展开为 G/P 的与或式并行产生，时延 <img class="fml" src="/formulas/f2f182680b4944.png" alt="\propto \log n" width="63" height="33">，代价是门数增加；成组先行进位折中。
- **ALU**：在加法器基础上加入与/或/非/异或、移位、比较等功能，由操作选择线决定执行哪种运算，并输出 **N（负）/Z（零）/C（进位）/V（溢出）** 标志位供条件分支使用。
- **移位器**：逻辑左/右移（补 0）、算术右移（补符号位）、循环移位；桶形移位器可在一个周期内移任意位。

### 3.2 定点数加减运算（★★★）



<p class="fml-block"><img class="fml" src="/formulas/925b9b1138a7e9.png" alt="\begin{gathered}
\text{[X + Y]} \; \text{补} \; \text{= [X]} \; \text{补} \; \text{+ [Y]} \; \text{补} \; \text{（模} \; 2^{n} \; \text{，符号位参与运算，最高进位丢弃）} \\
[X- Y] \; \text{补} \; \text{= [X]} \; \text{补} \; +[- Y] \; \text{补} \; \text{（} \; [- Y] \; \text{补} \; \text{= [Y]} \; \text{补} \; \text{连同符号位按位取反、末位加} \; \text{1} \; \text{）}
\end{gathered}" width="681" height="57"></p>



**溢出判断**（三种等价方法）：

| 方法 | 判据 |
| --- | --- |
| 单符号位进位 | <img class="fml" src="/formulas/2fb7151bbf8933.png" alt="OV= C_{n} ⊕ C_{n- 1}" width="139" height="33">，其中 C_n 是符号位产生的进位、<img class="fml" src="/formulas/8fa17f4decfcf4.png" alt="C_{n- 1}" width="44" height="33"> 是最高数值位向符号位的进位 |
| **双符号位（变形补码）** | `00`/`11` 正常；`01` 正溢出（结果应为正却为负）；`10` 负溢出 |
| 操作数/结果符号 | 同号相加才可能溢出；若结果符号与两操作数不同则溢出 |

::: tip 工作示例 · 8 位补码加减与溢出


<p class="fml-block"><img class="fml" src="/formulas/70442cffdf69cc.png" alt="\begin{gathered}
(1) 9- 5 \; \text{：} \; \text{0000 1001 + 1111 1011(−5} \; \text{的补码} \; \text{) = 1 0000 0100 →} \; \text{丢弃进位} \; \text{= 0000 0100 = +4 }\checkmark \\
\text{(2) 120 + 10} \; \text{：} \; 0111 1000+ 0000 1010= 1000 0010=- 126 \; \text{（数学结果} \; \text{+130 &gt; +127} \; \text{）} \\
C_{n}= 0 \; \text{（符号位未产生进位）、} \; C_{n- 1}= 1 \to OV= 1 \; \text{，正溢出} \; \checkmark \\
(3)- 120- 20 \; \text{：} \; 1000 1000+ 1110 1100= 1 0111 0100 \to 0111 0100=+116 \; \text{（应为} \; - 140 \; \text{）} \\
\text{双符号位将出现} \; 10 \to \; \text{负溢出}
\end{gathered}" width="746" height="137"></p>


:::

::: danger 易错 · 补码运算
- 溢出只可能发生在**同号相加**或**异号相减**；异号相加永远不会溢出。
- 无符号数的"溢出"判据是最高位**有进位**（`C_n = 1`），与有符号数的 <img class="fml" src="/formulas/ca2a02ca719c74.png" alt="C_{n} ⊕ C_{n- 1}" width="87" height="33"> 不是一回事。
- `[−Y]补` 的求法是**连同符号位一起取反再加 1**，不能只取反数值位；对 <img class="fml" src="/formulas/e44aaeff3d7cff.png" alt="- 2^{n- 1}" width="54" height="34"> 求补仍是它自己（溢出）。
:::

### 3.3 定点数乘法运算（★★★）

| 方法 | 思路 | 特点 |
| --- | --- | --- |
| **原码一位乘法** | 符号位单独异或，数值部分用"加法 + 右移"迭代 n 次，乘数最低位决定加 0 还是加被乘数 | 直观，需 n 次加法与 n 次右移 |
| **补码一位乘法（Booth）** | 乘数末位补一个 0，按相邻两位 `y_i y_(i+1)` 判断：`00/11` 只右移；`01` 加 `[X]补`；`10` 减 `[X]补`；最后一步不右移 | 直接对补码运算、对连续 1 有压缩效果，适合有符号数 |
| 快速乘法器 | 阵列乘法器（并行产生所有部分积）、Wallace 树压缩、Booth 编码 + 进位保留加法器 | 面积大但一周期或数周期出结果 |

::: tip 工作示例 · 原码一位乘法
`X = 0.1101`（13/16），`Y = 0.1011`（11/16），求 <img class="fml" src="/formulas/62cede35f6f3f8.png" alt="X \times Y" width="60" height="34">（符号均为 0）。取双符号位部分积 P 初值 `00.0000`：


<p class="fml-block"><img class="fml" src="/formulas/20a4a564a5e5f8.png" alt="\begin{gathered}
\text{y3(} \; \text{最低位} \; \text{)=1 → P += 00.1101 = 00.1101 →} \; \text{右移} \; \text{1} \; \text{位} \; \text{= 00.0110 1} \\
y_{2}=1 \to P+= 00.1101= 01.0011 1 \to \; \text{右移} \; \text{1} \; \text{位} \; \text{= 00.1001 11} \\
y_{1}=0 \to \; \text{不加} \; \to \; \text{右移} \; \text{1} \; \text{位} \; \text{= 00.0100 111} \\
y_{0}=1 \to P+= 00.1101= 01.0001 111 \to \; \text{右移} \; \text{1} \; \text{位} \; \text{= 00.1000 1111} \\
\text{数值结果} \; = 0.1000 1111_{2}= \frac{143}{256} \; \text{；符号} \; \text{= 0 ⊕ 0 = 0} \\
\text{验证：} \; \frac{13}{16} \times \frac{11}{16}= \frac{143}{256} \checkmark
\end{gathered}" width="536" height="193"></p>


:::

::: tip 工作示例 · Booth 规则速记
设乘数低位补 <img class="fml" src="/formulas/13cb99c57a9fd4.png" alt="y_{- 1}= 0" width="65" height="34">，逐位比较 <img class="fml" src="/formulas/5228b14fe54943.png" alt="(y_{i}, y_{i- 1})" width="73" height="34">：


<p class="fml-block"><img class="fml" src="/formulas/092960951aa640.png" alt="\begin{gathered}
\text{00、11} \to \; \text{部分积不变，仅算术右移} \; \text{1} \; \text{位} \\
01 \to \; \text{部分积} \; \text{+ [X]} \; \text{补，再右移} \\
10 \to \; \text{部分积} \; +[- X] \; \text{补，再右移}
\end{gathered}" width="326" height="84"></p>


最后一步只运算不右移；n 位乘数做 n 次判断、n−1 次移位，结果为 2n 位补码。
:::

### 3.4 定点数除法运算（★★）

| 方法 | 规则 |
| --- | --- |
| **恢复余数法** | 余数先减除数；若余数为负则"加回除数"恢复，并上商 0；为正则上商 1；余数左移继续 |
| **加减交替法（不恢复余数）** | 余数为正：左移后减除数、上商 1；余数为负：左移后**加**除数、上商 0；免去恢复步骤，速度更快 |
| 原码除法 | 符号单独异或，数值用绝对值运算；商 n+1 位，需判"是否溢出"（第一次上商为 1 说明被除数 ≥ 除数，溢出） |
| 阵列除法器 | 用可控加减单元 CAS 阵列并行实现，速度快、硬件多 |

### 3.5 浮点数运算（★★★）

![浮点数加减运算五步流程](/coa/coa-float.svg)

**浮点加减五步**：**① 对阶**（小阶向大阶看齐，尾数右移 <img class="fml" src="/formulas/5f9c1f01cdc53e.png" alt="\Delta E" width="36" height="34"> 位，阶码取大者；右移丢失的低位用 G/R/S 保护位保留）→ **② 尾数加减**（按补码运算）→ **③ 规格化**（左规/右规并同步调整阶码）→ **④ 舍入**（就近偶数/向零/向 ±∞）→ **⑤ 判溢出**（阶码而非尾数溢出，上溢 → ∞、下溢 → 0 或非规格化数）。

**浮点乘除**：阶码相加/相减（并修正 bias）、尾数相乘/相除，之后同样规格化、舍入、判溢出。

::: tip 工作示例 · 需要右规的浮点加法
设 <img class="fml" src="/formulas/7635433ca3470f.png" alt="X= 0.1101 \times 2^{2}" width="134" height="34">（= 3.25）、<img class="fml" src="/formulas/7f234fdf1019ea.png" alt="Y= 0.1011 \times 2^{3}" width="133" height="34">（= 5.5），尾数用 4 位小数：


<p class="fml-block"><img class="fml" src="/formulas/b4a823d3d5f9ae.png" alt="\begin{gathered}
\text{(1)} \; \text{对阶：} \; \Delta E= 3- 2= 1 \; \text{，} \; \text{X} \; \text{尾数右移} \; \text{1} \; \text{位} \; \to 0.01101 \times 2^{3} \; \text{（保留保护位）} \\
\text{(2)} \; \text{尾数相加：} \; \text{0.01101 + 0.10110 = 1.00011} \; \text{（} \; \times 2^{3} \; \text{）} \\
\text{(3)} \; \text{右规：尾数} \; \ge 1 \; \text{，右移} \; \text{1} \; \text{位} \; \to 0.100011 \; \text{，阶码} \; \text{3 + 1 = 4} \\
\text{(4)} \; \text{舍入：本例保留} \; \text{4} \; \text{位小数，} \; \text{0.100011} \; \text{超过中点} \; \text{0.10001} \; \text{，向上舍入得} \; 0.1001 \to 0.1001 \times 2^{4}= 9.0 \\
\text{若保留更多位} \; \to 0.100011 \times 2^{4}= 8.75 \; \text{（与} \; \text{3.25 + 5.5 = 8.75} \; \text{一致，可见舍入误差的来源）} \\
\text{(5)} \; \text{阶码} \; \text{4} \; \text{未溢出。注意：右规只可能右移} \; \text{1} \; \text{位，左规则可能移多位}
\end{gathered}" width="790" height="166"></p>


:::

::: danger 易错 · 浮点运算
- 对阶永远是**小阶向大阶看齐**（尾数右移），不能反过来（左移会丢失高位有效数字）。
- 溢出判断看**阶码**：尾数溢出可通过右规修正，只有阶码超出表示范围才是真溢出。
- 尾数右移会丢失精度，故浮点加法不满足结合律；舍入误差会累积。
:::

### 3.6 运算部件与十进制运算（★★）

- **定点运算部件**：寄存器组 + ALU + 移位器 + 多路选择器 + 状态标志 + 内部总线；**浮点运算部件**另设阶码运算器与尾数运算器（早期用协处理器 8087/80287，现代已集成进 CPU）。
- **十进制数加减（BCD）**：按 4 位一组做二进制加法，若某组结果 `> 9`（或产生向高组的进位）则**对该组加 6（0110）修正**。
  - 例：`25 + 37` → BCD `0010 0101 + 0011 0111 = 0101 1100`，低组 `1100 = 12 > 9` → 加 `0110` 得 `0110 0010` = `62` ✓。
- 现代 CPU 大多不再提供十进制算术指令（了解即可），金融计算改用定点十进制库或十进制浮点（IEEE 754-2008）。

### 3.7 数值演算与硬件实现要点

#### 3.7.1 三组综合演算



<p class="fml-block"><img class="fml" src="/formulas/43f33cd8fe8781.png" alt="\begin{gathered}
\text{(1)} \; \text{已知} \; \text{8} \; \text{位补码} \; \text{0xB6 = 1011 0110} \; \text{：符号为} \; 1 \to \; \text{取反} \; \text{0100 1001} \; \text{，加} \; 1 \to 0100 1010= 74 \to \; \text{真值} \; - 74 \\
\text{(2) 16} \; \text{位补码} \; \text{0xFFB6} \; \text{表示} \; - 74 \; \text{的符号扩展：高位全补} \; \text{1} \; \text{（而非} \; \text{0} \; \text{）} \\
\text{(3)  Booth} \; \text{判断：} \; X=- 3 \; \text{（} \; \text{1101} \; \text{），} \; \text{Y = +5} \; \text{（} \; \text{0101} \; \text{，末尾补} \; 0 \to 0101 0 \; \text{）} \\
\text{从低位：} \; 10 \to \; \text{减} \; \text{[X]} \; \text{补（即} \; \text{+3} \; \text{）；} \; 01 \to \; \text{加} \; \text{[X]} \; \text{补（} \; - 3 \; \text{）} \; \cdots \cdots \; \text{最终积} \; - 15 \; \text{（} \; \text{8} \; \text{位补码} \; \text{1111 0001} \; \text{）}
\end{gathered}" width="854" height="110"></p>



#### 3.7.2 运算部件的时序与面积权衡

| 实现 | 时延 | 面积 / 功耗 | 适用 |
| --- | --- | --- | --- |
| 行波进位加法器 | O(n) | 最省 | 低功耗嵌入式 |
| 先行进位 / 前缀加法器（Kogge-Stone） | O(log n) | 门数与布线多 | 高性能 ALU |
| 迭代乘法（n 次加移） | O(n) 周期 | 复用一个加法器 | 早期 CPU / 低成本核 |
| 阵列 / Wallace 树 + Booth | 1~3 周期 | 面积大 | 现代高性能核 |
| 除法迭代（SRT 等） | 数十周期 | 较小 | 除法频度低，可慢 |

> 现代 CPU 的**融合乘加 FMA**（<img class="fml" src="/formulas/3f2fb0e6c4785e.png" alt="a \times b+c" width="75" height="34"> 一次舍入）既提高性能又提高精度；SIMD 向量单元（SSE/AVX/NEON/SVE）把同一运算并行施加到多个数据通道，是浮点峰值算力（FLOPS）的主要来源。

::: danger 易错 · 运算方法
- 补码加减的进位要**丢弃**，但溢出判断要看 <img class="fml" src="/formulas/ca2a02ca719c74.png" alt="C_{n} ⊕ C_{n- 1}" width="87" height="33">，两者不矛盾。
- Booth 乘法最后一步**不移位**；n 位乘数得到 2n 位积。
- 加减交替除法中余数为负时下一步是**加**除数；恢复余数法则要先"加回"再左移。
- 浮点对阶只看阶差，尾数右移位数 <img class="fml" src="/formulas/2b13d1b70e8dfe.png" alt="=|E_{X}- E_{Y}|" width="107" height="34">；右移后阶码统一为较大的那个。
:::

---

## 第 4 章 存储器分层体系结构

### 4.1 存储器概述与性能指标（★★）

| 分类维度 | 类别 |
| --- | --- |
| 存储介质 | 半导体（SRAM/DRAM/Flash）、磁表面（磁盘/磁带）、光（光盘） |
| 存取方式 | **随机存取 RAM**（访问时间与地址无关）、顺序存取（磁带）、直接存取（磁盘）、相联存取（TLB/Cache 按内容查找） |
| 可改写性 | 读写存储器 / 只读存储器 ROM（PROM/EPROM/EEPROM/Flash） |
| 信息易失性 | **易失**（SRAM/DRAM 断电丢失）／**非易失**（ROM/Flash/磁盘） |
| 所在位置 | 寄存器、Cache、主存、辅存（外存） |

**三个主要性能指标**：**容量**（字数 × 字长）、**速度**（存取时间 / 存取周期 / 带宽）、**价格**（每位成本）。三者互相矛盾：容量越大、速度越快，单位成本越高——这正是引入**层次结构**的根本原因。

![存储器分层体系结构与平均访问时间](/coa/coa-hierarchy.svg)

### 4.2 半导体存储器（★★★）

| 类型 | 存储原理 | 特点 | 用途 |
| --- | --- | --- | --- |
| **SRAM** | 6 晶体管双稳态触发器 | 快、不需刷新、集成度低、功耗与成本高 | Cache、寄存器堆 |
| **DRAM** | 单管 + 电容，靠电荷表示 | 慢于 SRAM、集成度高、需**定期刷新**、行列地址复用 | 主存 |
| ROM / Flash | 熔丝 / 浮栅晶体管 | 非易失；Flash 按块擦除、写入前需先擦 | BIOS、SSD、U 盘 |

- **DRAM 刷新**：电容电荷会泄漏，一般要求在 `2 ms`（或 `64 ms`，视器件）内把所有行刷新一遍。刷新按**行**进行（一行一次读操作即完成整行再生），方式有**集中刷新**（停止读写、有"死区"）、**分散刷新**（每存取周期后插入刷新，无死区但周期加倍）、**异步刷新**（按行数把刷新分散到整个刷新间隔，折中方案）。
- **地址复用**：DRAM 用同一组引脚分两次送行地址（RAS）与列地址（CAS），减少引脚数；现代 SDRAM/DDR 用多 Bank 并行与突发传送提高带宽。
- **主存与 CPU 连接**：地址线 → 译码/片选，数据线双向，控制线（读/写/片选/就绪）；扩展方式见下。

::: tip 工作示例 · 存储器芯片扩展（必考）
用 `1K × 4 位` 的 SRAM 芯片构成 `4K × 8 位` 主存：


<p class="fml-block"><img class="fml" src="/formulas/dc25957420e835.png" alt="\begin{gathered}
\text{字扩展：} \; \frac{4K}{1K}= 4 \; \text{组；位扩展：} \; \frac{8}{4}= 2 \; \text{片} \; \text{/} \; \text{组} \; \to \; \text{共} \; 4 \times 2= 8 \; \text{片} \\
\text{总地址线} \; = \log_{2}(4K)= 12 \; \text{根：低} \; \text{10} \; \text{位接所有芯片的片内地址端，} \\
\text{高} \; \text{2} \; \text{位经} \; \text{2-4} \; \text{译码器产生} \; \text{4} \; \text{个片选信号；每组} \; \text{2} \; \text{片分别接数据总线高} \; \text{4} \; \text{位} \; \text{/} \; \text{低} \; \text{4} \; \text{位}
\end{gathered}" width="653" height="99"></p>


一般公式：所需片数 = `(目标容量 / 芯片容量) × (目标字长 / 芯片字长)`。
:::

::: tip 工作示例 · DRAM 刷新安排
设 DRAM 内部 `128 行`、要求 `2 ms` 内全部刷新一遍，存取周期 <img class="fml" src="/formulas/c21b6dbc9e9ada.png" alt="0.5 \mu s" width="49" height="33">：


<p class="fml-block"><img class="fml" src="/formulas/a4eac07f04f04a.png" alt="\begin{gathered}
\text{异步刷新：每隔} \; \frac{2 ms}{128}= 15.625 \mu s \; \text{刷新一行（每次占用} \; \text{1} \; \text{个存取周期）} \\
\text{集中刷新：} \; \text{2 ms} \; \text{末尾连续用} \; 128 \times 0.5 \mu s= 64 \mu s \; \text{刷新} \; \to \; \text{这段时间} \; \text{CPU} \; \text{不能访存（死区）} \\
\text{分散刷新：每个存取周期都附带一次刷新，存取周期变为} \; 1 \mu s \; \text{，无死区但整体变慢}
\end{gathered}" width="728" height="99"></p>


:::

### 4.3 存储层次与程序访问局部性（★★★）

- **时间局部性**：刚被访问的信息很可能再次被访问（循环体、循环变量、反复调用的函数）。
- **空间局部性**：与刚访问过的信息相邻的信息很可能被访问（顺序执行的指令、数组连续元素、结构体字段）。
- 层次结构的组织：上层保存下层中**当前最活跃的一小部分副本**；命中则在快层直接取，缺失则从下层调入一个**块**（block/line）而非单个字。
- 目标：整体访问速度接近最快层、容量与每位成本接近最慢层。

**平均访问时间**：`AMAT = 命中时间 + 缺失率 × 缺失代价`；多级 Cache 时逐级嵌套累加。

### 4.4 高速缓冲存储器 Cache（★★★）

![Cache 地址映射、替换算法与写策略](/coa/coa-cache.svg)

#### 4.4.1 基本工作原理

CPU 给出主存地址 → 由地址中的 index 定位 Cache 行/组 → 比较 Tag 并检查有效位 → **命中**则取块内偏移对应的数据；**缺失**则从主存调入整个主存块（可能替换旧行），CPU 等待或继续执行（乱序核）。

**三种映射方式**：

| 映射 | 规则 | 地址划分 | 优缺点 |
| --- | --- | --- | --- |
| **直接映射** | 主存块号 mod 行数 → 唯一行 | `Tag | 行号 | 块内地址` | 硬件最简、查找最快；**冲突缺失多** |
| **全相联** | 任意块可放任意行 | `Tag | 块内地址` | 冲突最少、利用率高；需并行比较全部 Tag，成本高 |
| **组相联** | 块号 mod 组数 → 固定组，组内任意行 | `Tag | 组号 | 块内地址` | 折中；n 路组相联即每组 n 行，最常用 |

通用关系：`Tag 位数 = 主存地址位数 − 组（行）索引位数 − 块内偏移位数`；`Cache 数据容量 = 行数 × 块大小`。

::: tip 工作示例 · 教材风格：64 KB Cache、块 128 B、直接映射、32 位主存地址


<p class="fml-block"><img class="fml" src="/formulas/916409d8536d9a.png" alt="\begin{gathered}
\text{块内偏移} \; = \log_{2}128= 7 bit \\
\text{行数} \; = \frac{64 KB}{128 B}= 512= 2^{9} \to \; \text{行号} \; \text{index = 9 bit} \\
Tag= 32- 9- 7= 16 bit \\
\text{每行另有} \; \text{1} \; \text{位有效位（写回法还要} \; \text{1} \; \text{位脏位）} \\
\text{附加硬件（仅标记阵列）} \; = 512 \times(16+ 1) bit= 8704 bit= 1088 B \\
\text{若改为} \; \text{4} \; \text{路组相联：组数} \; = \frac{512}{4}= 128 \to \; \text{组号} \; \text{7 bit} \; \text{，} \; Tag= 32- 7- 7= 18 bit
\end{gathered}" width="648" height="193"></p>


:::

::: tip 工作示例 · 命中判断
访问地址 `0x1234 5678`（32 位），上例直接映射：
```text
块内偏移 = 低 7 位；行号 = 接下来的 9 位；Tag = 高 16 位
取出该行的 Tag 与有效位比较：有效位=1 且 Tag 相同 → 命中，按块内偏移取数
否则缺失，从主存调入该地址所在的整块（128 B）到该行
```
:::

#### 4.4.2 替换算法、写策略与一致性

| 项 | 选项 | 说明 |
| --- | --- | --- |
| 替换算法 | **LRU**（最近最少用，命中率好）、FIFO（简单、可能有 Belady 异常）、LFU、Random | 直接映射无需替换算法（位置唯一直接覆盖） |
| 写命中 | **写直达 Write-through**：同时写 Cache 与主存；**写回 Write-back**：只写 Cache 并置脏位，替换时才写回 | 写回速度快，但主存与 Cache 会暂时不一致 |
| 写缺失 | **写分配**（先调入块再写）／**非写分配**（直接写主存） | 通常写回配写分配、写直达配非写分配 |
| 一致性 | 多核 **MESI / MOESI** 协议（Modified / Exclusive / Shared / Invalid） | DMA 与 I/O 也需考虑 Cache 一致性；伪共享会显著降低性能 |

::: danger 易错 · Cache
- Cache 与主存之间以**块**为单位传送，不是按字节；块大小增大可利用空间局部性，但也会增大缺失代价与冲突。
- Cache 的**容量指数据阵列**，不含 Tag、有效位、脏位等附加硬件；题目问"Cache 总容量"时要看清是否包含标记。
- 三种缺失（3C 模型）：** compulsory 冷启动缺失**（首次访问）、**capacity 容量缺失**（块被挤出）、**conflict 冲突缺失**（映射竞争）。
- 提高相联度可减少冲突缺失，但会增加命中时间与硬件复杂度，并非"路数越多越好"。
:::

#### 4.4.3 Cache 性能评估（★★★）



<p class="fml-block"><img class="fml" src="/formulas/ea91864ea01bdd.png" alt="\begin{gathered}
\text{AMAT =} \; \text{命中时间} \; \text{+} \; \text{缺失率} \; \times \; \text{缺失代价} \\
\text{CPU} \; \text{时间} \; \text{= (CPU} \; \text{执行时钟数} \; \text{+} \; \text{访存停顿时钟数} \; \text{) ×} \; \text{时钟周期} \\
\text{访存停顿} \; \text{=} \; \text{指令数} \; \times \; \text{指令缺失率} \; \times \; \text{缺失代价} \; \text{+} \; \text{指令数} \; \times \; \text{访存指令占比} \; \times \; \text{数据缺失率} \; \times \; \text{缺失代价}
\end{gathered}" width="820" height="84"></p>



::: tip 工作示例 · AMAT 与 CPI 综合（必考）
设理想 `CPI = 2`，指令 Cache 缺失率 `2%`，数据 Cache 缺失率 `5%`，访存指令占全部指令 `30%`，缺失代价均为 `100` 个时钟周期：


<p class="fml-block"><img class="fml" src="/formulas/a92da78369ae19.png" alt="\begin{gathered}
\text{每条指令的指令缺失停顿} \; = 2\% \times 100= 2 \; \text{周期} \\
\text{每条指令的数据缺失停顿} \; = 30\% \times 5\% \times 100= 1.5 \; \text{周期} \\
\text{实际} \; \text{CPI = 2 + 2 + 1.5 = 5.5} \; \text{（性能约为理想情况的} \; \frac{2}{5.5} \approx 36\% \; \text{）} \\
\text{若把缺失代价降到} \; 50 \to \; \text{实际} \; \text{CPI = 2 + 1 + 0.75 = 3.75}
\end{gathered}" width="528" height="125"></p>


另：L1 命中 `1 ns`、L1 缺失率 `5%`、L2 命中 `10 ns`、L2 缺失率 `20%`、主存 `100 ns`：


<p class="fml-block"><img class="fml" src="/formulas/bbdde9b1bf8ff6.png" alt="AMAT= 1+ 0.05 \times(10+ 0.20 \times 100)= 1+ 0.05 \times 30= 2.5 ns" width="500" height="33"></p>


:::

### 4.5 虚拟存储器（★★★）

![虚拟存储器地址变换、页表与 TLB](/coa/coa-vm.svg)

- **动机**：主存容量不足、多进程需要隔离与保护、程序员希望使用连续且大于物理内存的**虚拟地址空间**。
- **三种管理方式**：

| 方式 | 划分单位 | 特点 |
| --- | --- | --- |
| **页式** | 固定大小页（如 4 KB） | 无外部碎片、地址变换简单（页表）；存在内部碎片；最主流 |
| 段式 | 按逻辑段（代码/数据/栈） | 便于共享与保护、符合程序语义；有外部碎片 |
| 段页式 | 段内再分页 | 兼顾两者，地址变换最复杂 |

- **地址变换**：`VA = VPN | 页内偏移` → 查页表（或先查 TLB）得到 `PFN` → `PA = PFN | 页内偏移`；**页内偏移在变换前后不变**。
- **页表项 PTE**：PFN、有效位（是否在内存）、脏位、访问/引用位、权限位（读/写/执行、用户/内核）、缓存与写策略控制位。
- **TLB（快表）**：用相联存储器缓存近期 <img class="fml" src="/formulas/8ea49202bca1ff.png" alt="VPN \to PFN" width="124" height="33"> 映射，命中可省去一次或多次页表访存；未命中要遍历页表（page table walk），并把结果装入 TLB。
- **缺页处理**：PTE 有效位为 0 → 触发**缺页异常** → OS 选一页换出（脏页需写回磁盘）→ 从外存调入目标页 → 更新 PTE 与 TLB → **重新执行**刚才那条指令。
- **存储保护**：每进程独立页表（独立虚拟空间）+ PTE 权限位 + 用户/内核态 + 越界检查，防止进程互访或用户程序访问内核。

::: tip 页面置换算法（缺页时选哪一页换出）
- **OPT（最佳）**：淘汰将来最久不用的页，无法实现，仅作理论下界；
- **FIFO**：淘汰最早调入的页，实现最简单，但可能出现 **Belady 异常**（分配页框更多反而缺页更多）；
- **LRU（最近最久未用）**：淘汰最久未被访问的页，靠引用位/时间戳近似实现，性能接近 OPT，是主流选择；
- **Clock（NRU）**：把页组织成循环队列，用访问位扫描淘汰，硬件开销小，实际 OS 多用其改进版（双指针、考虑脏位）。
缺页率 p 与分配给进程的**驻留集**大小强相关；p 过高引发 **抖动（thrashing）**<img class="fml" src="/formulas/1f1cb40865e9d4.png" alt="-- CPU" width="84" height="33"> 大部分时间花在换页上。
:::

::: tip 工作示例 · 页表容量与地址变换
`32 位`虚拟地址、页大小 `4 KB`、物理内存 `256 MB`、PTE `4 B`：


<p class="fml-block"><img class="fml" src="/formulas/e7fb3fa6836ec5.png" alt="\begin{gathered}
\text{页内偏移} \; = \log_{2}4096= 12 bit \; \text{；} \; VPN= 32- 12= 20 bit \; \text{；} \; PFN= 28- 12= 16 bit \\
\text{单级页表} \; = 2^{20} \; \text{项} \; \times 4 B= 4 MB \; \text{（每个进程都要一份，太浪费）} \\
\text{两级页表：} \; \text{VA =} \; \text{页目录号} \; \text{(10) |} \; \text{页表号} \; \text{(10) | offset(12)} \; \text{，只为用到的二级页表分配内存} \\
VA= 0x12345678 \to VPN= 0x12345 \; \text{，} \; \text{offset = 0x678} \; \text{；若} \; PFN= 0xABCD \to PA= 0xABCD678
\end{gathered}" width="818" height="111"></p>


:::

::: tip 工作示例 · 有效访问时间（含缺页）
设页表访存 `100 ns`、TLB 命中 `10 ns`（命中率 98%）、缺页率 `p = 0.001`、缺页处理 `10 ms`：


<p class="fml-block"><img class="fml" src="/formulas/eb048b27457493.png" alt="\begin{gathered}
\text{无缺页时的平均访存} \; \approx 0.98 \times 10+ 0.02 \times(10+ 100)= 9.8+ 2.2= 12 ns \\
\text{计入缺页：} \; EAT \approx(1- p) \times 12 ns+ p \times 10 ms \approx 10 \mu s \; \text{（主要由缺页项主导）}
\end{gathered}" width="616" height="57"></p>


结论：缺页率必须极低，否则磁盘访问会吞掉所有 CPU 性能——这靠程序局部性、合理的页面置换（LRU/Clock）与足够的驻留集保证。
:::

::: danger 易错 · 虚存 vs Cache
| | Cache | 虚拟存储器 |
| --- | --- | --- |
| 目的 | 弥合 **CPU 与主存**的速度差 | 弥合**主存容量**不足、提供保护与隔离 |
| 实现 | 全硬件 | 硬件（MMU/TLB）+ 操作系统（页表、缺页处理） |
| 块大小 | 几十~几百字节（行） | 固定页（通常 4 KB，可大页 2 MB/1 GB） |
| 缺失代价 | 几十~数百周期 | 磁盘 I/O，百万级周期 |
| 地址 | 主存物理地址 → Cache | 虚拟地址 → 物理地址 |
两者**可以同时缺失**：先 TLB/页表得到物理地址，再查 Cache；顺序不能颠倒。
:::

### 4.6 多级 Cache、一致性与现代存储

#### 4.6.1 多级 Cache 与包含性

- 现代 CPU 通常有 **L1（指令/数据分离，32~64 KB）→ L2（每核私有，256 KB~2 MB）→ L3（多核共享，数 MB~数十 MB）**；私有/共享、包含（inclusive）/非包含（non-inclusive）/独占（exclusive）策略影响一致性与容量利用。
- **伪共享（false sharing）**：两个核频繁写同一 Cache 行中的不同变量，导致该行在核间反复失效；用**按 Cache 行大小对齐/填充**可解决。
- **Cache 一致性协议**：MESI/MOESI/MESIF，通过侦听（snooping）或目录（directory）维护多核间同一物理地址副本的一致；这直接影响多线程程序性能。

#### 4.6.2 现代存储技术补充（教材以 SDRAM/DDR、机械盘为主）

| 主题 | 补充 |
| --- | --- |
| 主存 | DDR4 → **DDR5**（更高频率、双通道子通道、片上 ECC）、**HBM**（堆叠 + 宽接口，用于 GPU/AI 加速器）、LPDDR（移动低功耗） |
| 非易失 | **3D NAND**、NVMe SSD（PCIe + 多队列）、**持久内存 NVM / CXL.mem** 模糊主存与外存边界；QLC/PLC 提高密度但降低耐久 |
| 可靠性 | ECC SEC-DED、**Chipkill**、内存镜像、RowHammer 与 TRR 防护；磁盘/SSD 用 RAID 与纠删码 |
| 页表 | x86-64 常用 4~5 级页表、**大页 2 MB/1 GB** 降低 TLB 压力、**ASID/PCID** 避免上下文切换时全刷 TLB、页表遍历缓存 |
| 安全 | 页表隔离（KPTI）、地址空间布局随机化 ASLR、推测执行侧信道（Meltdown/Spectre）与缓存计时攻击 |

::: tip 工作示例 · 多级 Cache 综合
理想 CPI = 1.5，L1 命中时间 1 周期、L1 缺失率 8%，L2 命中时间 10 周期、L2 缺失率（相对 L1 缺失）25%，主存缺失代价 120 周期，访存指令占 35%：


<p class="fml-block"><img class="fml" src="/formulas/459aa566938bcd.png" alt="\begin{gathered}
\text{L1} \; \text{缺失代价} \; = 10+ 0.25 \times 120= 40 \; \text{周期} \\
\text{每条指令的平均访存停顿（按一次取指} \; \text{+} \; \text{部分数据访问估算）} \\
\approx 1 \times 0.08 \times 40+ 0.35 \times 0.08 \times 40= 3.2+ 1.12= 4.32 \; \text{周期} \\
\text{实际} \; CPI \approx 1.5+ 4.32= 5.82 \to \; \text{存储层次是性能瓶颈，优化数据布局} \; \text{/} \; \text{局部性收益最大}
\end{gathered}" width="702" height="111"></p>


:::

::: danger 易错 · 存储层次
- `AMAT = 命中时间 + 缺失率 × 缺失代价`，**命中时间始终要算**，不能只算缺失部分。
- 多级 Cache 的"缺失率"要分清是**局部缺失率**（相对上一级的访问）还是**全局缺失率**（相对全部访存），代入公式时不能混。
- 虚拟地址到物理地址的变换由 **MMU** 完成；TLB 是页表的 Cache，不是主存的 Cache。
- 页内偏移位数 = `log2(页大小)`，与物理内存大小无关；PFN 位数由**物理地址位数**决定。
:::

---

## 第 5 章 指令系统

### 5.1 指令格式设计（★★★）

![指令格式、扩展操作码与寻址方式](/coa/coa-instruction.svg)

**指令 = 操作码 OP + 地址码 A**。OP 指明操作类型（并隐含寻址方式），地址码给出操作数地址、结果地址或下条指令地址。

#### 5.1.1 地址码个数

| 格式 | 语义 | 特点 |
| --- | --- | --- |
| 四地址 | <img class="fml" src="/formulas/8fb664ffdd6ca2.png" alt="A1 OP A2 \to A3" width="130" height="34">，下条指令 `A4` | 指令长、访存多，已淘汰 |
| 三地址 | <img class="fml" src="/formulas/8fb664ffdd6ca2.png" alt="A1 OP A2 \to A3" width="130" height="34">，下条由 PC 隐含 | 指令长，但程序短；RISC 常用（寄存器型） |
| 二地址 | <img class="fml" src="/formulas/cbc93241cd5f22.png" alt="A1 OP A2 \to A1" width="130" height="34"> | 破坏一个操作数，最普遍（x86） |
| 一地址 | <img class="fml" src="/formulas/e10ced2c676186.png" alt="ACC OP A1 \to ACC" width="168" height="34"> | 隐含累加器，指令短但程序长 |
| 零地址 | 操作数隐含在**堆栈栈顶** | 适合表达式求值（逆波兰式），无需地址字段 |

**格式设计原则**：① 指令长度尽量短且与机器字长/存储边界匹配；② 有足够的操作种类与寻址能力；③ 字段规整便于硬件快速译码（RISC 采用**定长**指令，CISC 多为**变长**）；④ 保留扩展空间与兼容。

#### 5.1.2 扩展操作码（高频计算题）

**思想**：地址码字段多的指令（如三地址）用**短操作码**，地址码少的指令用**长操作码**；用若干"扩展标志"编码串接，从而在固定字长内获得更多指令条数。原则：**使用频度高的指令分配短操作码**（类似 Huffman 编码思想）。

::: tip 工作示例 · 扩展操作码经典演算
指令字长 `16 位`、每个地址码 `4 位`。若三地址指令 `15` 条、二地址 `15` 条、一地址 `15` 条，零地址最多多少条？
```text
① 三地址格式：OP(4) | A1(4) | A2(4) | A3(4)。OP 共 16 种，用 15 种（0000~1110），
   留下 1111 作为「扩展标志」，表示该指令格式不是三地址
② 二地址：1111 | OP'(4) | A1(4) | A2(4)。OP' 用 15 种，留 1111 1111
③ 一地址：1111 1111 | OP''(4) | A1(4)。OP'' 用 15 种，留 1111 1111 1111
④ 零地址：1111 1111 1111 | OP'''(4) → 2⁴ = 16 条
```
若一地址只用 14 条，则多留一个扩展前缀，零地址可增至 <img class="fml" src="/formulas/476a78f404e638.png" alt="2 \times 16= 32" width="97" height="34"> 条 —— 每少用一条短格式指令，可多换得 `2^剩余地址码位数` 条长格式指令。
:::

### 5.2 寻址方式（★★★）

**有效地址 EA** 是操作数在存储器/寄存器中的实际位置；**寻址方式**决定如何由指令中的形式地址 A 得到 EA。

| 寻址方式 | EA / 操作数 | 特点与用途 |
| --- | --- | --- |
| **立即** | 操作数 = A | 最快，不访存；常数、小整数 |
| **直接** | `EA = A` | 简单，寻址范围受地址码位数限制 |
| **间接** | `EA = (A)` | 需多次访存；扩大寻址范围、支持指针/间接跳转 |
| **寄存器直接** | `EA = R` | 不访存、最快；RISC 的主要方式 |
| **寄存器间接** | `EA = (R)` | 一次访存；指针、数组基址 |
| **变址** | `EA = A + (IX)` | IX 由用户/编译器改，**适合数组遍历**（A 为数组首址） |
| **基址** | `EA = A + (BR)` | BR 由 OS 设定，**适合程序重定位 / 多道程序** |
| **相对** | `EA = (PC) + 位移` | 位置无关代码；分支与跳转指令 |
| **堆栈** | 由 SP 隐含 | 零地址指令、过程调用与表达式求值 |
| 复合 | 基址+变址+位移、比例变址 | x86 支持"基址 + 变址×比例 + 位移"，便于多维数组 |

::: tip 工作示例 · EA 演算


<p class="fml-block"><img class="fml" src="/formulas/f4f53ddaeb8bfb.png" alt="\begin{gathered}
\text{(1)} \; \text{相对转移：当前指令地址} \; \text{0x1000} \; \text{、指令长} \; \text{4 B} \; \text{、位移量} \; - 3 \; \text{（以「字」为单位，字长} \; \text{4 B} \; \text{）} \\
\text{取指后} \; PC= 0x1004 \to EA= 0x1004+(- 3 \times 4)= 0x0FF8 \\
\text{(2)} \; \text{变址寻址：数组首址} \; \text{A = 0x2000} \; \text{、元素} \; \text{4 B} \; \text{、变址寄存器} \; \text{IX = 4} \\
EA= 0x2000+ 4 \times 4= 0x2010 \; \text{（第} \; \text{4} \; \text{个元素，从} \; \text{0} \; \text{开始计）} \\
\text{(3)} \; \text{基址寻址：} \; \text{BR = 0x3000} \; \text{（} \; \text{OS} \; \text{分配的段基址）、指令中} \; A= 0x0500 \to EA= 0x3500
\end{gathered}" width="765" height="138"></p>


:::

::: danger 易错 · 指令格式与寻址
- **变址与基址的区别**不在计算公式（都是加法），而在**谁修改寄存器**：变址寄存器由程序指令修改（面向数组元素），基址寄存器由操作系统设定（面向重定位）。
- 相对寻址的基准是**取指后的 PC 值**（已指向下一条指令），不是当前指令地址。
- 指令字长、机器字长、存储字长三者概念不同：指令字长是单条指令的位数，可定长也可变长。
:::

### 5.3 指令类型与操作码编码（★★）

| 类别 | 典型指令 |
| --- | --- |
| 数据传送 | MOV / LOAD / STORE / PUSH / POP / 交换 |
| 算术逻辑 | ADD/SUB/MUL/DIV、AND/OR/XOR/NOT、比较 CMP |
| 移位 | 逻辑/算术/循环/带进位循环移位 |
| 控制转移 | 无条件跳转 JMP、条件分支 BEQ/BNE、调用 CALL、返回 RET、陷阱 |
| 串/向量 | 串传送与比较、SIMD 向量运算 |
| 系统 / I/O | 特权指令、中断返回、IN/OUT（或统一用内存映射 I/O） |

**操作码编码**：定长编码（译码快但浪费编码空间）、**扩展操作码**（变长，提高编码密度）、Huffman 编码（按频度变长，译码复杂）。设计 ISA 时需在**代码密度、译码速度、可扩展性、兼容性**之间权衡。

### 5.4 CISC 与 RISC（★★★）

| 维度 | CISC（x86、VAX） | RISC（MIPS、ARM、RISC-V） |
| --- | --- | --- |
| 指令数量/长度 | 多、变长 | 少、定长（常 4 B） |
| 寻址方式 | 丰富，多数指令可直接访存 | 少，**仅 Load/Store 访存** |
| 寄存器 | 较少 | 较多通用寄存器 |
| 控制器 | 多为微程序（现代 x86 混合） | 硬连线为主 |
| 流水线 | 难（步骤差异大） | 易（步骤规整） |
| CPI | 常 > 1 | 理想 1（多发射可 < 1） |
| 代码密度 | 高（程序指令数少） | 较低 |
| 代表 | x86 / x86-64 | MIPS、ARM、RISC-V、SPARC |

> 现代界限已模糊：**x86 内部把 CISC 指令译码为类 RISC 的 μop 再乱序执行**；RISC 处理器也加入复杂指令与向量扩展。真正的分水岭是 **Load/Store 架构 + 定长指令 + 寄存器数量**。

**MIPS 三种指令格式**（教材以 MIPS 为 CPU 设计蓝本）：

| 类型 | 字段（32 位） | 用途 |
| --- | --- | --- |
| **R 型** | `op(6) rs(5) rt(5) rd(5) shamt(5) funct(6)` | 寄存器-寄存器运算，如 `add $t0,$t1,$t2` | 
| **I 型** | `op(6) rs(5) rt(5) immediate(16)` | 立即数、Load/Store、条件分支 |
| **J 型** | `op(6) target(26)` | 无条件跳转 |

MIPS 有 32 个 32 位通用寄存器：`$zero`(恒 0)、`$at`、`$v0~$v1`(返回值)、`$a0~$a3`(参数)、`$t0~$t9`(临时)、`$s0~$s7`(保存)、`$gp/$sp/$fp/$ra`。**教材还指出 MIPS 没有寄存器传送指令**，用伪指令 `move` 由汇编器翻译成 `add $dst, $src, $zero`。

### 5.5 过程调用与栈帧（★★）

```text
调用序列：① 参数放到约定寄存器/压栈 → ② CALL：把返回地址写入 $ra 并跳转
被调用者：③ 调整 $sp 建栈帧，保存 $s 类寄存器与 $fp → ④ 执行函数体
         ⑤ 返回值放 $v0 \to  ⑥ 恢复寄存器与 $sp → ⑦ RET 跳回 $ra
```
- **调用约定（ABI）**规定：哪些寄存器由调用者保存（caller-saved，如 `$t` 类）、哪些由被调用者保存（callee-saved，如 `$s` 类）、参数与返回值放在哪里、栈如何对齐。
- 递归、嵌套调用靠**栈**实现；每次调用形成一个栈帧（返回地址、旧 `$fp`、局部变量、保存的寄存器）。
- 叶子函数可不建完整栈帧（编译器优化）；`$fp` 便于调试回溯与动态栈分配。

### 5.6 现代 ISA 一览

#### 5.6.1 主流指令集对比（RISC-V / ARM / x86-64）

| 主题 | 补充 |
| --- | --- |
| **RISC-V** | 开源、模块化扩展（I/M/A/F/D/C 等，如 RV32IMAFDC）、定长 32 位指令 + 压缩指令 C 扩展、无延迟槽、特权架构规范；已成为教学与产业热点 |
| **ARM / AArch64** | Load/Store、条件执行（AArch32）、大寄存器堆；移动与服务器广泛；SVE 可伸缩向量 |
| **x86-64** | 变长 1~15 B、64 位寄存器与地址、REX/VEX/EVEX 前缀、AVX2/AVX-512 向量扩展；向后兼容 32 位 |
| **SIMD / 向量** | 一条指令处理多个数据通道（SSE/AVX/NEON/SVE/RVV），是 FLOPS 与多媒体性能主要来源 |
| **特权与虚拟化** | 用户/内核态、系统调用指令、VT-x/AMD-V 与扩展页表 EPT/NPT、可信执行环境 TEE |
| **指令安全** | 推测执行带来的 Meltdown/Spectre 侧信道，说明"ISA 语义正确"不等于"微架构实现安全" |

#### 5.6.2 工作示例 · 指令数与 CPI 的权衡



<p class="fml-block"><img class="fml" src="/formulas/76a5ed57f348dc.png" alt="\begin{gathered}
\text{编译器生成序列} \; \text{S1} \; \text{：} \; \text{100} \; \text{条指令，} \; \text{CPI = 1.0} \; \text{；序列} \; \text{S2} \; \text{：} \; \text{70} \; \text{条指令，} \; \text{CPI = 1.5} \\
\text{同一主频下：} \; \text{S1} \; \text{时间} \; = 100 \times 1.0= 100 \; \text{周期；} \; \text{S2} \; \text{时间} \; = 70 \times 1.5= 105 \; \text{周期} \; \to S1 \; \text{更快}
\end{gathered}" width="729" height="57"></p>


说明：减少指令数（IC）未必更快，若因此增大了 CPI（如更多复杂指令、更多 Cache 缺失），总时间可能反而变长 —— 与第 1 章 <img class="fml" src="/formulas/7a478c5594d2e1.png" alt="IC \times \frac{CPI}{f}" width="83" height="36"> 的结论一致。

::: danger 易错 · 指令系统
- **ISA 是软硬件界面**：寄存器个数、指令格式、寻址方式属于 ISA；Cache 大小、流水线级数、是否乱序属于**组成/微体系结构**。
- RISC 的"指令条数少"指**指令种类少**，不是程序里指令数量少；同等程序 RISC 的 IC 通常比 CISC 多。
- 扩展操作码中，"每少用一条短格式指令"换得的是 `2^(该格式剩余地址码位数)` 条更长格式的指令编码，不是 1 条。
- `move`/`li` 等常是**伪指令**（由汇编器展开），并非 CPU 真正支持的机器指令。
:::

---

## 第 6 章 中央处理器

### 6.1 CPU 的功能与基本组成（★★★）

![CPU 数据通路与控制器](/coa/coa-datapath.svg)

**CPU 四大功能**：**指令控制**（按程序顺序取指、控制指令流向）、**操作控制**（产生每条指令所需的微命令序列）、**时间控制**（各操作按严格时序）、**数据加工**（算术逻辑运算），现代还包括**中断/异常处理**与**存储管理（MMU）**。

| 组成 | 关键部件 |
| --- | --- |
| 运算部件 | ALU、移位器、乘除法器、通用寄存器堆、状态标志寄存器 |
| 控制部件 | **PC**、**IR**、指令译码器、时序发生器、控制信号形成电路（硬连线或微程序） |
| 寄存器 | 用户可见（通用寄存器、PC、PSW/标志）与用户不可见（MAR、MDR、IR、流水线寄存器、暂存器） |
| 内部互连 | 单总线 / 双总线 / 三总线结构，或专用数据通路（多路选择器 + 独立连线） |

### 6.2 指令执行过程与数据通路（★★★）

一条指令的典型执行周期：
```text
① 取指 IF：PC → MAR → 主存/指令 Cache；读出指令 → MDR → IR；PC ← PC + 4
② 译码 ID：解析 OP 与寻址方式；读寄存器堆（rs/rt），立即数符号扩展
③ 执行 EX：ALU 做运算 / 计算有效地址 / 比较分支条件；更新标志位
④ 访存 MEM：Load/Store 读写数据存储器；其余指令跳过
⑤ 写回 WB：把 ALU 结果或读出的数据写回目的寄存器
⑥ 中断周期：在一条指令结束后检查中断请求，若有则转入中断响应
```

**指令周期、机器周期与节拍**：指令周期 = 取出并执行一条指令的全部时间，由若干**机器周期（CPU 周期）**组成（如取指、间址、执行、中断周期），每个机器周期又包含若干**节拍（时钟周期）**，一个节拍完成一个最基本的微操作。可屏蔽中断（INTR）在指令周期末尾查询，而 DMA 请求以总线周期为粒度响应。

数据通路的两种基本结构：
- **单总线结构**：所有寄存器共用一条内部总线，同一时刻只能传送一个数据，需大量暂存器与节拍，控制简单但慢。
- **专用通路 / 多总线结构**：用多路选择器为 ALU 各输入单独配通路，可并行读写多个寄存器（寄存器堆需双读端口 + 单写端口），是单周期与流水线 CPU 的基础。

### 6.3 单周期处理器设计（★★★）

**思想**：一条指令在**一个时钟周期**内走完全部数据通路；`CPI = 1`，但时钟周期必须按**最慢指令**（通常是 `lw`：取指 + 译码 + ALU 算地址 + 访存 + 写回）确定。

#### 6.3.1 主要控制信号

| 信号 | 作用 |
| --- | --- |
| `RegDst` | 写回目的寄存器选 `rt`（I 型）还是 `rd`（R 型） |
| `ALUSrc` | ALU 第二操作数来自寄存器堆还是符号扩展后的立即数 |
| `ALUOp / ALUControl` | 决定 ALU 执行加、减、与、或、比较等具体操作 |
| `MemRead / MemWrite` | 数据存储器读/写使能 |
| `MemtoReg` | 写回数据来自 ALU 结果还是数据存储器 |
| `RegWrite` | 寄存器堆写使能 |
| `Branch / PCSrc` | `Branch 且 Zero=1` 时 `PC ← 分支目标`，否则 <img class="fml" src="/formulas/0815156e0ea2c2.png" alt="PC \leftarrow PC+4" width="121" height="34"> |
| `Jump` | J 型跳转的目标地址拼接 |

控制器本质是**组合逻辑**：输入 `op`（+ `funct`），输出上述控制信号；因此单周期 CPU 不需要状态机（无"当前处于第几拍"的概念）。

::: tip 工作示例 · 时钟周期由最慢指令决定
设各部件延迟：PC 读出 `2 ns`、指令存储器 `8 ns`、译码与控制 `3 ns`、寄存器堆读 `5 ns`、ALU `8 ns`、数据存储器 `10 ns`、寄存器堆写 `5 ns`：


<p class="fml-block"><img class="fml" src="/formulas/9e09cefe3bd102.png" alt="\begin{gathered}
\text{lw} \; \text{路径} \; = 2+ 8+ 3+ 5+ 8+ 10+ 5= 41 ns \to \; \text{时钟周期至少} \; \text{41 ns} \; \text{（主频} \; \le \; \text{约} \; \text{24 MHz} \; \text{）} \\
\text{R} \; \text{型} \; add= 2+ 8+ 3+ 5+ 8+ 5= 31 ns \to \; \text{但仍需等满} \; \text{41 ns} \; \text{，浪费} \; \text{10 ns} \\
beq \approx 2+ 8+ 3+ 5+ 8= 26 ns \to \; \text{浪费更多}
\end{gathered}" width="739" height="84"></p>


结论：单周期设计硬件简单、CPI=1，但**所有指令都被最慢者拖慢**；这正是引入多周期与流水线的动机。
:::

::: danger 易错 · 单周期
- 单周期 CPU 必须**分离的指令存储器与数据存储器**（或双端口），否则 IF 与 MEM 在同一周期内争用同一部件，产生结构冒险。
- `CPI = 1` 不等于"性能最好"：主频被最慢指令拉低，总时间仍是 <img class="fml" src="/formulas/5fb4e134a97457.png" alt="IC \times 1 \times T" width="96" height="34">。
- 控制信号是**纯组合逻辑**由 OP 译码得到；没有状态寄存器、没有微指令序列。
:::

### 6.4 多周期处理器设计（★★★）

**思想**：把一条指令拆成若干**时钟周期（节拍）**，每拍完成一个子操作，**部件分时复用**（同一 ALU 既算地址又做运算，指令与数据可共用同一存储器）。

| 阶段 | 典型 R 型 | 典型 `lw` | 典型 `beq` |
| --- | --- | --- | --- |
| 取指 | IF | IF | IF |
| 译码/读寄存器 | ID | ID | ID |
| 执行 | EX（ALU 运算） | EX（算有效地址） | EX（比较并算目标） |
| 访存 | — | MEM | — |
| 写回 | WB | WB | — |
| CPI | 4 | 5 | 3 |

- 需要**流水线之外的时序状态机**（有限状态机 FSM）：当前状态 + 指令 OP 决定下一状态与微命令；因此需要**指令寄存器 IR、MDR、A/B/ALUOut 等暂存寄存器**保存跨拍数据。
- **优点**：时钟周期由**最慢的单个阶段**决定（远短于单周期），CPI 虽 >1 但总体更快；同一部件可复用、硬件更省。
- **信号竞争**（教材 *6.3.1）：同一周期内若读写同一寄存器/存储器，需靠**时钟边沿分离**（前半拍写、后半拍读）或设置独立读写端口，避免竞争。
- **CPI 不再统一**：不同指令的周期数不同，程序 CPI 需按指令混合比例加权。

### 6.5 硬连线控制器与微程序控制器（★★★）

| 维度 | **硬连线（组合逻辑）控制器** | **微程序控制器** |
| --- | --- | --- |
| 实现 | 由门电路/PLA 直接根据 OP、状态、标志产生控制信号 | 把每条机器指令翻译成一段**微程序**（若干条微指令），存于**控制存储器**（ROM） |
| 速度 | 快（组合逻辑延迟） | 较慢（每条微指令需一次控存读出） |
| 规整性 / 可修改性 | 杂乱、难以修改扩展 | 规整、易修改与扩展指令（改微程序即可） |
| 适用 | RISC、流水线 CPU、追求高性能 | CISC、复杂指令系统 |
| 核心部件 | 状态机 + 译码矩阵 | **微地址寄存器 μPC / CAR**、微指令寄存器、控存、微地址形成电路 |

**微指令格式**：`控制字段（微命令集合） + 顺序字段（下一条微地址/判别条件）`。编码方式：
- **直接编码（不译法）**：每一位对应一个微命令，最快但微指令字长最长；
- **字段直接编码**：把互斥微命令分组合并编码（每段需留一个"无操作"码），缩短字长；
- **字段间接编码 / 混合编码**：进一步压缩，但需额外译码级。
**微地址形成**：`下地址字段` 显式给出、或由 `OP` 经映射逻辑得到微程序入口、或由状态标志（如 Zero）分支选择。

::: tip 工作示例 · 微程序条数与控存容量
某机器有 `64` 条机器指令，每条平均 `4` 条微指令，微指令字长 `32 bit`：


<p class="fml-block"><img class="fml" src="/formulas/78666062f6772e.png" alt="\begin{gathered}
\text{微指令总数} \; = 64 \times 4= 256 \; \text{条} \; \to \; \text{需} \; \text{8} \; \text{位微地址} \\
\text{控存容量} \; = 256 \times 32 bit= 8192 bit= 1 KB
\end{gathered}" width="393" height="57"></p>


:::

### 6.6 异常与中断处理（★★★）

| 概念 | 说明 |
| --- | --- |
| **异常 Exception** | 由**当前指令**引起、同步发生（除零、溢出、缺页、非法指令、系统调用） |
| **中断 Interrupt** | 由**外部事件**引起、异步发生（定时器、键盘、磁盘完成、网卡收包） |
| 响应时机 | 通常在一条指令执行**结束时**检查；缺页等精确异常需在特定流水级处理 |
| 处理流程 | 保存断点 <img class="fml" src="/formulas/c9566c8cd38541.png" alt="PC \to EPC" width="105" height="34">、记录 Cause、切到内核态、关/屏蔽同级中断、跳到异常向量表入口 → 执行服务程序 → 恢复现场 → 返回 |
| 中断向量 | 每个中断类型对应一个入口地址，放在**中断向量表**中；也可为非向量中断（统一入口再软件判优） |
| 判优与嵌套 | 硬件排队器（菊花链）/ 软件查询；用**中断屏蔽字**动态调整优先级，允许高优先级中断嵌套 |
| 精确异常 | 异常指令之前的指令必须全部完成、之后的指令不得产生副作用；流水线 CPU 靠 ROB / 重排序缓冲保证 |

### 6.7 从 MIPS 单周期到现代乱序核

#### 6.7.1 设计方法演进



<p class="fml-block"><img class="fml" src="/formulas/bb88715bf972ea.png" alt="\begin{gathered}
\text{IAS} \; \text{简单} \; CPU \to \; \text{总线式} \; CPU \to \; \text{单周期} \; CPU \to \; \text{多周期} \; CPU \to \; \text{基本流水线} \; \text{CPU} \\
\to \; \text{动态超标量超流水线} \; \text{CPU} \; \text{（} \; \text{Pentium 4} \; \text{为例）}
\end{gathered}" width="689" height="57"></p>


每前进一步都在解决上一步的瓶颈：单周期被最慢指令拖累 → 多周期复用部件、缩短周期 → 流水线让多条指令重叠 → 多发射/乱序进一步挖掘指令级并行 ILP。

#### 6.7.2 现代微体系结构关键机制

| 机制 | 作用 |
| --- | --- |
| **寄存器重命名** | 消除 WAR/WAW 伪相关，只保留真 RAW 相关 |
| **乱序执行 + 保留站/ROB** | 操作数就绪就发射，按程序顺序**提交**，保证精确异常 |
| **Tomasulo 算法 / 记分板** | 动态调度、CDB 公共数据总线广播结果 |
| **分支预测** | BHT/BTB、两级自适应预测、感知机预测，减少控制冒险惩罚 |
| **推测执行** | 在预测路径上提前执行；预测失败则冲刷并回滚（也是 Meltdown/Spectre 的根源） |
| **多核与同时多线程 SMT** | 一个物理核上共享执行资源、呈现多个逻辑处理器 |

::: tip 工作示例 · 多周期 CPI
某程序指令混合：`40%` ALU（4 周期）、`25%` lw（5 周期）、`15%` sw（4 周期）、`20%` beq（3 周期）：


<p class="fml-block"><img class="fml" src="/formulas/4b3d8dc78c7029.png" alt="\begin{gathered}
\text{平均} \; CPI= 0.40 \times 4+ 0.25 \times 5+ 0.15 \times 4+ 0.20 \times 3= 1.6+ 1.25+ 0.6+ 0.6= 4.05 \\
\text{若时钟周期从单周期的} \; \text{41 ns} \; \text{降到} \; \text{12 ns} \; \text{：} \\
\text{单周期} \; \text{时间} \; = IC \times 1 \times 41 \; \text{；多周期} \; \text{时间} \; = IC \times 4.05 \times 12= 48.6 IC \to \; \text{反而略慢} \\
\text{把周期再降到} \; 8 ns \to 32.4 IC \; \text{，才体现出多周期优势}
\end{gathered}" width="669" height="111"></p>


说明：多周期必须让**时钟周期显著缩短**（各阶段延迟尽量均衡）才有收益。
:::

::: danger 易错 · CPU 设计
- 单周期控制器是组合逻辑、无状态；多周期控制器必须有**状态机**与暂存寄存器。
- 微程序控制器"慢"是指控制路径多一次控存访问，但**改变指令系统只需改微程序**，这是 CISC 选择它的原因。
- 异常是同步的、中断是异步的；二者响应入口与保存现场机制相同，但触发源与返回行为可能不同（缺页要**重执行**该指令，外部中断通常执行下一条）。
- `PC+4` 的 "4" 来自按字节编址且指令长 4 B；若按字编址或变长指令则不同。
:::

---

## 第 7 章 指令流水线

### 7.1 流水线的基本原理（★★★）

**思想**：把一条指令的执行分成若干**相互独立、可并行**的阶段，不同指令的不同阶段在同一时刻由不同硬件部件处理（时间并行性）。经典 **MIPS 五级流水线**：`IF 取指 → ID 译码/读寄存器 → EX 执行/算地址 → MEM 访存 → WB 写回`。

关键硬件要求：各级之间加**流水线寄存器（锁存器）**保存中间结果；各阶段尽量**时延均衡**（最慢阶段决定时钟周期）；指令与数据存储器分离（或分离 Cache）以避免结构冲突；寄存器堆需支持"前半拍写、后半拍读"。

![五级指令流水线时空图与加速比](/coa/coa-pipeline.svg)

### 7.2 性能指标（★★★）

设 `k` 个流水段、每段 1 个时钟周期 `t`、共 `n` 条指令（理想无冒险）：



<p class="fml-block"><img class="fml" src="/formulas/ea56942b1085ca.png" alt="\begin{gathered}
\text{非流水时间} \; T_{\text{非}} = n \cdot k \cdot t \\
\text{流水时间} \; T_{\text{流}} =(k+ n- 1) \cdot t \; \text{（首条填满流水线需} \; k \; \text{拍，之后每拍流出} \; 1 \; \text{条）} \\
\text{加速比} \; S= \frac{T_{\text{非}}}{T_{\text{流}}} = \frac{n \cdot k}{k+ n- 1} \xrightarrow{n \to \infty} k \\
\text{吞吐率} \; TP= \frac{n}{(k+n- 1) \cdot t} \; \text{，最大} \; TP_{\max}= \frac{1}{t} \\
\text{效率} \; E= \frac{S}{k}= \frac{n}{k+n- 1} \; \text{（时空图中被占用的面积占比）}
\end{gathered}" width="619" height="190"></p>



::: tip 工作示例 · 理想加速比
`k = 5`、`n = 100` 条指令、每段 `1 ns`：


<p class="fml-block"><img class="fml" src="/formulas/b22a7417cc6467.png" alt="\begin{gathered}
T_{\text{非}} = 100 \times 5 \times 1= 500\,\text{ns} \\
T_{\text{流}} =(5+ 100- 1) \times 1= 104\,\text{ns} \\
S= \frac{500}{104} \approx 4.81 \; \text{（理论上限} \; \text{5} \; \text{，} \; \text{n} \; \text{越大越接近）}
\end{gathered}" width="386" height="97"></p>


若各段时间不等：`IF 2 / ID 1 / EX 2 / MEM 2 / WB 1 ns`，锁存器开销 `0.5 ns`：


<p class="fml-block"><img class="fml" src="/formulas/def042bc8ff7b8.png" alt="\begin{gathered}
\text{时钟周期} \; \text{= max(} \; \text{各段} \; \text{) +} \; \text{锁存} \; \text{= 2 + 0.5 = 2.5 ns} \\
\text{非流水单条} \; = 2+1+2+2+1= 8 ns \to 100 \; \text{条} \; \text{= 800 ns} \\
\text{流水} \; =(5+ 100- 1) \times 2.5= 260 ns \to S \approx 3.08
\end{gathered}" width="458" height="84"></p>


结论：**各段不均衡 + 寄存器开销 + 冒险停顿**使实际加速比明显低于段数 k；单纯增加段数（超流水线）会因锁存开销与冒险惩罚而收益递减。
:::

### 7.3 流水线冒险（★★★）

![流水线冒险与解决方法](/coa/coa-hazard.svg)

| 冒险类型 | 成因 | 典型对策 |
| --- | --- | --- |
| **结构冒险** | 多条指令同时争用同一硬件（如 IF 与 MEM 同用一个存储器） | 分离指令/数据 Cache、增加部件、插入气泡（停顿） |
| **数据冒险** | 后续指令需要前面指令尚未产生/写回的数据 | **转发/旁路（forwarding）**、停顿、编译器调度、Load 延迟槽 |
| **控制冒险** | 分支方向与目标是未知，后续已取指的指令可能作废 | **分支预测**（静态/动态 BHT+BTB）、提前计算分支、延迟槽、失败时冲刷流水线 |

**数据相关的三种类型**：
- **RAW（写后读，真相关）**：`I1: add $t0,...` 后 `I2: sub ...,$t0,...`，I2 必须等 I1 产生结果；顺序与乱序机器都存在。
- **WAR（读后写，反相关）**、**WAW（写后写，输出相关）**：仅在**乱序执行**时才会造成冲突，由**寄存器重命名**消除。

**延迟分支（delayed branch）**：早期 MIPS 等 ISA 在分支指令后设置一个**延迟槽**，无论分支是否成功该槽内指令都会被执行；编译器把一条无关指令（或分支前的有用指令）填入槽中，即可掩盖 1 拍分支惩罚。代价是编程与编译复杂度上升，现代 ISA（RISC-V、AArch64）已放弃延迟槽，改用更深的分支预测。

::: tip 工作示例 · 转发能消除多少停顿
```text
I1: add $t0, $t1, $t2     IF ID EX MEM WB
I2: sub $t3, $t0, $t4        IF ID EX  MEM WB
```
I2 的 EX 需要新 `$t0`，而 I1 的结果在 EX 结束时已算出（写回要等 WB）。
- **不转发**：需等到 I1 的 WB 后，插入 **2 个气泡**；
- **有转发**：把 I1 的 ALU 结果从 EX/MEM 流水线寄存器直接引到 I2 的 ALU 输入 → **0 停顿**；
- **Load-Use 情形**（`lw $t0, 0($t1)` 紧跟使用 `$t0` 的指令）：数据要到 MEM 结束才可用，转发后仍需 **1 个停顿**，编译器可插入无关指令填充该槽。
:::

::: tip 工作示例 · 分支预测对 CPI 的影响
设分支指令占 `20%`、预测准确率 `90%`、预测失败惩罚 `3` 个时钟周期：


<p class="fml-block"><img class="fml" src="/formulas/a814824dea49ce.png" alt="\begin{gathered}
\text{平均控制停顿} \; = 0.20 \times(1- 0.90) \times 3= 0.06 \; \text{周期} \; \text{/} \; \text{指令} \\
\text{若理想} \; \text{CPI = 1} \; \text{且无其它冒险} \; \to \; \text{实际} \; \text{CPI = 1 + 0.06 = 1.06} \\
\text{若准确率降到} \; 70\% \to \; \text{停顿} \; = 0.20 \times 0.30 \times 3= 0.18 \to CPI= 1.18
\end{gathered}" width="541" height="84"></p>


在深流水线（如教材提到的 Pentium 4 达 20+ 级）中失败惩罚可达十几~几十周期，**分支预测准确率的权重极大**。
:::

### 7.4 高级流水线技术（★★）

| 技术 | 原理 | 代价 / 代表 |
| --- | --- | --- |
| **静态多发射（VLIW / EPIC）** | 编译器在一条超长指令字里打包多个可并行操作，硬件按约定同时发射 | 依赖编译器；IA-64 Itanium、DSP |
| **动态多发射（超标量）** | 硬件每周期发射多条指令，配合乱序执行、重命名、ROB | 硬件复杂；现代 x86/ARM 高性能核 |
| **超流水线** | 增加段数 k、每段更短以提高主频 | 冒险惩罚变大；Pentium 4 是极端例子（后回归较短流水线） |
| **超长指令字 + SIMD** | 一条指令内并行处理多个数据 | 向量寄存器、AVX/SVE |
| 向量/张量扩展 | 面向数组与矩阵的数据级并行 | GPU、TPU/NPU |

**IPC 与 CPI**：单发射理想 `CPI = 1`（`IPC = 1`）；n 发射超标量理想 <img class="fml" src="/formulas/343013b1f91504.png" alt="CPI= \frac{1}{n}" width="80" height="33">，实际 CPI 受冒险与访存限制，常为 0.3~1 以上。

### 7.5 流水线设计约束与性能综合

#### 7.5.1 实际 CPI 的构成



<p class="fml-block"><img class="fml" src="/formulas/e5e152df88bb7a.png" alt="\begin{gathered}
\text{实际} \; \text{CPI =} \; \text{理想} \; \text{CPI +} \; \text{结构冒险停顿} \; \text{+} \; \text{数据冒险停顿} \; \text{+} \; \text{控制冒险停顿} \; \text{+} \; \text{存储缺失停顿} \\
\text{CPU} \; \text{时间} \; \text{=} \; \text{指令数} \; \times \; \text{实际} \; CPI \times \; \text{时钟周期}
\end{gathered}" width="697" height="57"></p>



::: tip 工作示例 · 综合 CPI
某 5 级流水线：理想 CPI = 1；`lw` 占 25%，其中 `Load-Use` 冲突占 `lw` 的 40%（每次停顿 1 拍）；分支占 15%，预测失败率 20%（惩罚 3 拍）；指令 Cache 缺失率 2%（缺失代价 20 拍）：


<p class="fml-block"><img class="fml" src="/formulas/42a6f0f9aa1c58.png" alt="\begin{gathered}
\text{Load-Use} \; \text{停顿} \; = 0.25 \times 0.40 \times 1= 0.10 \; \text{周期} \; \text{/} \; \text{指令} \\
\text{分支停顿} \; = 0.15 \times 0.20 \times 3= 0.09 \; \text{周期} \; \text{/} \; \text{指令} \\
\text{取指缺失停顿} \; = 0.02 \times 20= 0.40 \; \text{周期} \; \text{/} \; \text{指令} \\
\text{实际} \; \text{CPI = 1 + 0.10 + 0.09 + 0.40 = 1.59}
\end{gathered}" width="417" height="111"></p>


可见存储缺失往往比冒险更贵，呼应第 4 章的 AMAT 分析。
:::

#### 7.5.2 设计约束清单

- **各段均衡**：最慢段决定时钟周期；切分过细会增加锁存器开销与冒险惩罚。
- **精确异常**：异常指令之前的指令必须完成、之后的不能留下副作用；乱序核靠 ROB 按序提交。
- **寄存器堆端口**：单周期内要支持 WB 写 + ID 读两个源（通常双读一写）。
- **PC 与分支**：分支目标要尽早算出（把比较与地址计算前移到 ID 可减少惩罚）。
- **存储器带宽**：IF 每拍取一条指令，Load/Store 还要访存，需分离 I-Cache/D-Cache 或多端口。
- **功耗与面积**：更深的流水线、更多发射宽度带来更多寄存器与转发网络，收益递减。

::: danger 易错 · 流水线
- 流水线的**加速比上限是段数 k**，且只有指令数 n ≫ k 时才接近；小段程序反而可能因填充/排空而变慢。
- 流水线**不缩短单条指令的执行时间**（反而因锁存器略增），它提高的是**吞吐率**。
- 「转发可以消除所有数据冒险」是错的：Load-Use 仍需 1 拍停顿（或靠调度填充）。
- 增加段数不一定提升性能：冒险惩罚与锁存开销会同步增大，Pentium 4 的高频深流水线就是历史教训。
- 超标量的理想 `CPI = 1/发射宽度 < 1`，但别把它与单发射理想 CPI=1 混淆。
:::

---

## 第 8 章 系统总线

### 8.1 总线的基本概念与分类（★★）

**总线**是多个功能部件之间共享的**公共信息传输通路**，同一时刻只允许一个主设备发送（可多个从设备接收）。采用总线而非专用连线的好处是**减少连线数、便于扩展与标准化**，代价是**共享导致带宽争用**。

| 分类维度 | 类别 |
| --- | --- |
| 位置 | **片内总线**（CPU 内部）、**系统总线**（<img class="fml" src="/formulas/bc6543905abc5f.png" alt="CPU \leftrightarrow" width="72" height="33">主存/I/O）、**I/O 总线 / 外部总线**（设备互连） |
| 传送方式 | 并行总线（多根数据线同时传，短距）、**串行总线**（差分高速点对点，长距，现代主流） |
| 定时 | 同步总线（统一时钟）、异步总线（请求-应答握手） |
| 功能 | 数据总线、地址总线、控制总线 |

### 8.2 系统总线的组成（★★）

| 组 | 方向 | 作用 |
| --- | --- | --- |
| **数据总线** | 双向 | 传送数据/指令/状态；**宽度**决定一次可传送的位数 |
| **地址总线** | 单向（主→从） | 指明主存单元或 I/O 端口；**宽度**决定最大寻址空间 |
| **控制总线** | 混合 | 读/写、时钟、复位、中断请求/响应、**总线请求/授权**、就绪/应答 |

> 注意：地址总线"宽度 = n 位 → 寻址 2ⁿ 个单元"，这里的单元通常是**字节**（按字节编址）；而数据总线宽度决定一次传送的数据量，两者不必相等。

### 8.3 总线设计的五个要素（★★★）

![总线带宽与 I/O 数据传送方式总览](/coa/coa-io.svg)

| 要素 | 要点 |
| --- | --- |
| 信号线类型 | 专用/复用（地址数据复用可减少引脚）、并行/串行 |
| **总线事务类型** | 存储器读/写、I/O 读/写、中断响应、DMA 传送、配置周期；一个事务含**地址期 + 数据期**（可拆分/流水化） |
| **总线带宽** | 单位时间最大数据传输率，见下公式 |
| **总线裁决（仲裁）** | 菊花链（优先级固定、简单）、计数器定时查询（可改优先级）、**独立请求**（最快、线数多）；集中式/分布式 |
| **定时方式** | 同步（统一时钟，快但受最慢设备限制、时钟偏斜限制长度）；异步（握手，适应不同速度设备，开销大）；半同步 |



<p class="fml-block"><img class="fml" src="/formulas/868542493b69fd.png" alt="\text{总线带宽} \; \left(\frac{B}{s}\right)= \; \text{总线宽度} \; \frac{bit}{8} \times \; \text{总线工作频率} \; (Hz) \times \; \text{每周期传送次数}" width="570" height="33"></p>



::: tip 工作示例 · 总线带宽
同步总线宽 `64 bit`、频率 `100 MHz`、每周期传 1 次：


<p class="fml-block"><img class="fml" src="/formulas/d682469aa9f7cd.png" alt="\begin{gathered}
\text{带宽} \; = \frac{64}{8} \times 100 \times 10^{6}= 8 \times \frac{10^{8} B}{s}= \frac{800 MB}{s} \\
\text{若采用} \; \text{DDR} \; \text{（上升} \; \text{/} \; \text{下降沿各传一次）} \; \to \; \text{每周期} \; \text{2} \; \text{次} \; \to \frac{1.6 GB}{s} \\
\text{若改为} \; \text{32 bit} \; \text{、} \; \text{200 MHz} \; \text{、每周期} \; \text{2} \; \text{次} \; \to 4 \times 2 \times 200 \times 10^{6}= \frac{1.6 GB}{s} \; \text{（同等带宽的不同组合）}
\end{gathered}" width="767" height="131"></p>


一次总线事务若要传 `128 B` 数据，64 bit 总线需 <img class="fml" src="/formulas/126173a8059b17.png" alt="\frac{128}{8}= 16" width="72" height="34"> 个数据周期；若每个事务还有 1 个地址周期，则**有效带宽** = `128 B / (17 周期 × 10 ns) ≈ 753 MB/s`，低于理论峰值。
:::

### 8.4 总线接口单元与总线标准（★★）

- **总线接口单元（BIU）**：负责地址/数据缓冲与驱动、时序配合、协议转换、错误检测、中断与 DMA 请求；设备通过接口挂到总线上，CPU 只需与接口交互。
- **总线标准演进**（教材以 ISA/EISA/PCI 为主）：

| 标准 | 特点 | 现状 |
| --- | --- | --- |
| ISA / EISA | 早期 PC 并行总线，8/16/32 位 | 已淘汰 |
| PCI / PCI-X | 同步并行、即插即用、支持总线主设备 | 被 PCIe 取代 |
| **PCIe** | **串行差分、点对点、多 lane（x1/x4/x8/x16）、交换式拓扑、包交换、向后兼容软件模型** | 现代 PC/服务器主流，代际带宽近似翻倍（<img class="fml" src="/formulas/a546886704d177.png" alt="Gen3 \approx \frac{\frac{985 MB}{s}}{lane}" width="112" height="36">，Gen4/5/6 依次翻倍） |
| USB | 通用串行、热插拔、树形拓扑、主机轮询 | 外设主流；USB4 融合 Thunderbolt，走 PCIe/DisplayPort 隧道，速率达 40~80 Gbps |
| **AMBA / AXI / AHB** | 片上系统 SoC 内部互连 | 手机/嵌入式芯片内部 |
| CXL / NVLink / Infinity Fabric | 面向 <img class="fml" src="/formulas/bc6543905abc5f.png" alt="CPU \leftrightarrow" width="72" height="33">加速器/内存池的高速缓存一致互连 | AI/HPC 与异构计算 |

::: tip 补充 · 现代互连（教材未涉及）
- **从并行总线到串行点对点**：并行总线在高频下受时钟偏斜与串扰限制，PCIe 用高速串行 + 多 lane + 交换芯片获得更高带宽与更强扩展性。
- **片上网络 NoC**：多核/众核芯片内部用分组交换的二维网格取代共享总线，解决可扩展性瓶颈。
- **CXL** 在 PCIe 物理层之上提供缓存一致性与内存池化，是"内存墙"与异构内存的重要方向。
:::

### 8.5 带宽、裁决与事务综合例题

::: tip 工作示例 · 多主设备争用
设总线上有 CPU 与一个 DMA 控制器，总线周期 `20 ns`，一次 DMA 传送 `1 KB`（每次占 4 B 数据 + 1 周期地址开销）：


<p class="fml-block"><img class="fml" src="/formulas/81c6320e73ea49.png" alt="\begin{gathered}
\text{数据周期数} \; = \frac{1024}{4}= 256 \; \text{；总占用} \; \approx 256 \times 2= 512 \; \text{周期（若每次都含地址期）} \\
\text{占用时间} \; \approx 512 \times 20 ns= 10.24 \mu s \; \text{；期间} \; \text{CPU} \; \text{若需访存，只能靠周期挪用} \; \text{/} \; \text{等待}
\end{gathered}" width="652" height="71"></p>


可见 DMA 虽减少 CPU 干预，但仍与 CPU **争用总线与主存带宽**；这是"周期窃取"名称的由来。
:::

::: danger 易错 · 总线
- 总线带宽公式中的"宽度"是**数据线位数**；地址线宽度决定的是寻址空间，不能代入带宽公式。
- 总线复用地址/数据线可减少引脚，但同一周期无法同时送地址和数据，**会降低有效带宽**。
- 同步总线适合速度相近、距离短的设备；异步总线靠握手适应速度差异，但与 CPU 时钟无关。
- 独立请求仲裁最快但控制线数最多；菊花链最省线但优先级固定、对故障敏感（链路上一环故障会影响后面设备）。
:::

---

## 第 9 章 输入/输出系统

### 9.1 I/O 系统概述与外设（★）

**I/O 系统** = I/O 设备 + I/O 接口（控制器）+ I/O 软件（驱动、中断服务、OS 的 I/O 子系统）+ 互连总线。基本功能：**把外设的低速、多样、机电信号转换成 CPU 可读写的数据，并屏蔽设备差异**。

| 设备类别 | 例子 | 特点 |
| --- | --- | --- |
| 人机交互 | 键盘、鼠标、扫描仪、显示器、打印机 | 低速、字符型、多用中断 |
| 存储型 | 磁盘、SSD、光盘、磁带 | 高速、成块传送、多用 DMA |
| 通信型 | 网卡、Modem | 速率差异大、协议复杂 |
| 传感/控制 | ADC/DAC、工业现场设备 | 实时性要求高 |

**显示器（CRT/LCD 光栅扫描）**：图像按**像素点阵**组织，像素值存于**显存（帧缓冲）**，由显示控制器周期性读取并经 DAC 输出；关键参数有**分辨率**（如 <img class="fml" src="/formulas/b57f08267762da.png" alt="1920 \times 1080" width="100" height="34">）、**灰度/色深**（每像素位数）、**刷新率**（如 60 Hz）。显存容量 = 分辨率 × 每像素字节数（<img class="fml" src="/formulas/0e137064529b82.png" alt="1920 \times 1080 \times 3 B \approx 6.2 MB" width="226" height="34">）；刷新率越高闪烁越少，但占用显存带宽越多。打印机按成像方式分击打式（针式）与非击打式（激光、喷墨），DPI 表示打印分辨率。

### 9.2 外部存储设备（★★）

#### 9.2.1 磁盘存储器

- 结构：盘片 → 磁道（同心圆）→ **扇区**（传统 512 B，现代 4 KB）→ 柱面（各盘面同一半径的磁道集合）；寻址用 `柱面号 | 盘面号（磁头）| 扇区号`。
- **存取时间 = 寻道时间 + 旋转延迟 + 传输时间 + 控制器开销**。

::: tip 工作示例 · 磁盘平均存取时间
磁盘 `7200 rpm`、平均寻道 `8 ms`、持续传输率 `100 MB/s`、读一个 `4 KB` 块：


<p class="fml-block"><img class="fml" src="/formulas/dd30d34f13cfaf.png" alt="\begin{gathered}
\text{平均旋转延迟} \; = \frac{\frac{60 s}{7200}}{2}= 4.167 ms \; \text{（平均转半圈）} \\
\text{传输时间} \; = \frac{4096 B}{\frac{100 \times 10^{6} B}{s}} \approx 0.041 ms \\
\text{总存取时间} \; \approx 8+ 4.167+ 0.041+ \; \text{控制器开销} \; \approx 12.2 ms
\end{gathered}" width="459" height="127"></p>


对比主存约 `50~100 ns`、SSD 约 <img class="fml" src="/formulas/505cef3f58d833.png" alt="50 \sim 100 \mu s" width="95" height="34"> —— 机械盘的**毫秒级**延迟主要来自机械运动，因此 OS 要做电梯调度、预读与页缓存来减少寻道次数。
:::

#### 9.2.2 RAID（廉价磁盘冗余阵列）

教材对其有较完整介绍，核心是**把多个独立磁盘组织成阵列以提高容量、性能与可靠性**（条带化 striping + 冗余）。

| 级别 | 冗余方式 | 最少盘数 | 特点 |
| --- | --- | --- | --- |
| RAID 0 | 无冗余，纯条带 | 2 | 容量/性能最优，**任一盘坏即全毁** |
| RAID 1 | 镜像 | 2 | 读快、写需双份，容量利用率 50% |
| RAID 2 | 海明码多校验盘 | 3+ | 理论意义大，实际少用 |
| RAID 3 | 位级条带 + 专用校验盘 | 3+ | 校验盘易成写瓶颈 |
| RAID 4 | 块级条带 + 专用校验盘 | 3+ | 同上 |
| **RAID 5** | 块级条带 + **校验分布**在各盘 | 3 | 兼顾容量/性能/容错，允许坏 1 盘 |
| **RAID 6** | 双重校验（P+Q） | 4 | 允许同时坏 2 盘 |
| RAID 10 | 先镜像再条带（1+0） | 4 | 高性能高可靠，容量利用率 50% |

> 现代补充：RAID 由硬件控制器或 Linux mdadm/ZFS 实现；**SSD 阵列需考虑写放大与 TRIM**；大规模分布式存储多用**纠删码（erasure coding）**而非多副本，以更低冗余开销获得同等可靠性。

#### 9.2.3 SSD 与新型存储

- **SSD/NVMe**：基于 NAND Flash，无机械部件、随机访问快；但**写入前必须先擦除块**（擦写次数有限），靠 FTL（闪存转换层）、磨损均衡、垃圾回收与预留空间维持性能与寿命；接口从 SATA/AHCI 演进到 **NVMe over PCIe**（多队列、低延迟）。
- 教材重点讲磁表面存储与硬盘，现代应补充 **3D NAND（TLC/QLC）**、**持久内存**、以及"存储级内存"对存储层次的冲击。

### 9.3 I/O 接口（★★★）

**功能**：① 地址译码/设备选择；② 数据缓冲与电平/格式转换；③ 传送命令与状态（忙、就绪、错误）；④ 中断/DMA 请求；⑤ 定时与协议控制；⑥ 错误检测。

**通用结构**：数据缓冲寄存器、状态寄存器、控制寄存器、地址译码逻辑、中断/DMA 控制逻辑、与总线及外设两侧的接口电路。

**I/O 端口编址方式**：

| 方式 | 说明 | 优缺点 |
| --- | --- | --- |
| **统一编址（存储器映射 I/O，MMIO）** | 把端口当作主存地址空间的一部分，用普通访存指令读写 | 指令丰富、无需专用 I/O 指令；**占用主存地址空间**、地址译码需区分 |
| **独立编址（I/O 映射）** | 单独的 I/O 地址空间，用专用 `IN/OUT` 指令 | 不占主存空间、译码简单；指令少、需额外控制线（x86 采用） |

### 9.4 I/O 数据传送控制方式（★★★）

| 方式 | CPU 参与度 | 数据通路 | 适用 |
| --- | --- | --- | --- |
| **程序直接控制（轮询）** | 全程循环读状态，CPU 被占死 | 外设 <img class="fml" src="/formulas/4401ce3296861e.png" alt="\leftrightarrow" width="24" height="34"> 寄存器 ↔  主存 | 极简单设备，教学示例 |
| **程序中断方式** | 数据就绪时才响应，其余时间可并行执行 | 仍经 CPU 中转到主存 | 键盘、鼠标等低速字符设备 |
| **DMA 方式** | 只在**传送前配置**与**传送后收尾**参与 | 外设 <img class="fml" src="/formulas/4401ce3296861e.png" alt="\leftrightarrow" width="24" height="34"> 控制器 ↔  **主存**（不经 CPU） | 磁盘、网卡等高速成批传送 |
| **通道 / I/O 处理器** | CPU 只启动通道程序，通道统一管理多设备 | 通道执行专用 I/O 程序 | 大型机，高吞吐环境 |

::: tip 工作示例 · 中断方式 vs DMA 的 CPU 开销
某设备以 `100 KB/s` 输入，每次中断传送 `1 B`、中断服务开销 <img class="fml" src="/formulas/8d94b0d20055ba.png" alt="10 \mu s" width="44" height="34">：


<p class="fml-block"><img class="fml" src="/formulas/e7a6e1dc12754a.png" alt="\begin{gathered}
\text{中断频率} \; = 100 \times 10^{3} \; \text{次} \; s \to CPU \; \text{开销} \; = 100 \times 10^{3} \times 10 \mu s= \frac{1 s}{s} \to CPU \; \text{完全被占满！} \\
\text{改用} \; \text{DMA} \; \text{：每} \; \text{ C235 } \; \text{块中断一次} \; \to \; \text{中断次数} \; \text{= 100} \; \text{次} \; s \to \; \text{开销仅} \; \text{1 ms/s} \; \text{（} \; \text{0.1\%} \; \text{）}
\end{gathered}" width="2811" height="34"></p>


这正是高速设备必须用 DMA、且还可在设备侧加缓冲的原因；现代网卡更进一步用**中断合并**与轮询（NAPI/io_uring）减少中断风暴。
:::

### 9.5 中断处理的完整过程（★★★）



<p class="fml-block"><img class="fml" src="/formulas/8027fb471896bd.png" alt="\begin{gathered}
\text{(1)} \; \text{中断请求：设备置请求触发器} \; \to(2) \; \text{中断判优：硬件排队器} \; \text{/} \; \text{软件查询选出最高优先级} \\
\text{(3)} \; \text{中断响应：} \; \text{CPU} \; \text{在指令周期末检测，满足「开中断} \; \text{+} \; \text{未被屏蔽} \; \text{+} \; \text{优先级更高」时响应} \\
\text{(4)} \; \text{保护断点与现场：} \; \text{PC/PSW} \; \text{压栈（或写入} \; \text{EPC} \; \text{），保存通用寄存器} \\
\text{(5)} \; \text{取中断向量：由中断类型号查向量表} \; \to \; \text{装入服务程序入口} \\
\text{(6)} \; \text{执行中断服务程序（可嵌套：用屏蔽字允许更高优先级打断）} \\
\text{(7)} \; \text{恢复现场} \; \to \; \text{开中断} \; \to \; \text{中断返回（} \; \text{RETI} \; \text{）}
\end{gathered}" width="721" height="164"></p>


- **向量中断 vs 非向量中断**：前者由硬件直接给出入口，响应快；后者统一入口后由软件查询中断源。
- **中断屏蔽字**：每个中断源对应一个屏蔽码，可动态改变实际处理优先级（注意"响应优先级"由硬件排队器固定，"处理优先级"可由屏蔽字调整）。

### 9.6 DMA 方式（★★★）



<p class="fml-block"><img class="fml" src="/formulas/5d0b70d77cfcd5.png" alt="\begin{gathered}
\text{(1)} \; \text{预处理：} \; \text{CPU} \; \text{向} \; \text{DMA} \; \text{控制器写入「主存起始地址、传送字数} \; \text{/} \; \text{计数、传送方向、设备地址」并启动设备} \\
\text{(2)} \; \text{数据传送：} \; \text{DMAC} \; \text{向总线控制器发总线请求} \; \to \; \text{获授权后接管总线，} \\
\text{在设备与主存之间直接传送一个字} \; \text{/} \; \text{块，每传一个字自动改地址、减计数} \\
\text{(3)} \; \text{后处理：计数归零} \; \to DMAC \; \text{发中断通知} \; CPU \to CPU \; \text{校验数据、释放缓冲、关闭设备}
\end{gathered}" width="869" height="111"></p>


**CPU 与 DMAC 分时使用主存的三种方式**：停止 CPU 访存（成组传送，CPU 暂停）、**周期挪用/周期窃取**（DMA 挪用空闲总线周期，最常用）、交替分时（按固定时隙划分，无需申请）。

::: tip 工作示例 · DMA 传送时间
DMA 传 `1 MB`、总线带宽 `100 MB/s`、预处理 `100` 周期、后处理中断 `200` 周期，CPU 主频 `1 GHz`：


<p class="fml-block"><img class="fml" src="/formulas/793ebad86c86c8.png" alt="\begin{gathered}
\text{数据传送} \; = \frac{\frac{1 MB}{100 MB}}{s}= 10 ms \\
\text{CPU} \; \text{开销} \; = \frac{100+ 200}{1 GHz}= 0.3 \mu s \\
\text{CPU} \; \text{占用率} \; \approx \frac{0.3 \mu s}{10 ms} \approx 0.003\% \; \text{（几乎可忽略，但总线} \; \text{/} \; \text{主存带宽被占用} \; \text{10 ms} \; \text{）}
\end{gathered}" width="657" height="132"></p>


:::

::: danger 易错 · I/O 与中断
- 中断方式虽然让 CPU 不必轮询，但**每个字节/字仍要经 CPU 中转**；DMA 才是"数据不经过 CPU"。
- DMA 的预处理与后处理由 **CPU** 完成，传送阶段由 **DMAC** 接管总线；DMAC 是总线主设备。
- 响应优先级（硬件裁决）与处理优先级（屏蔽字）是两个概念，别混。
- 中断返回后：外部中断通常执行**下一条**指令，而**缺页异常**要重新执行刚才那条指令。
- 统一编址下用 `MOV` 类访存指令访问端口；独立编址下必须用专用 `IN/OUT` 指令。
:::

### 9.7 现代 I/O 技术演进

| 传统机制 | 现代演进 |
| --- | --- |
| 程序查询 / 中断 / DMA / 通道 | **MSI-X 消息中断**、中断合并、多队列网卡 RSS、`io_uring` 异步 I/O、DPDK 用户态轮询 |
| 并行/串行传输、I/O 接口举例 | **NVMe 多队列**、SR-IOV 设备直通、**RDMA**（绕过 CPU 与内核直接内存访问）、CXL.io |
| 机械磁盘 + RAID | SSD / NVMe / 纠删码 / 分布式存储 / ZFS；磁盘调度在 SSD 上意义下降 |
| 中断向量表 | APIC / GIC、中断亲和性与负载均衡、中断线程化 |

::: tip 工作示例 · 综合：一条 Load 指令的"旅行"
```text
编译：a[i] → lw $t0, offset($s1)
执行：PC → I-Cache(IF) → 译码读寄存器(ID) → ALU 算有效地址(EX)
地址变换：MMU 查 TLB → 命中得物理页号 → 合成物理地址
访存：查 L1 D-Cache → 命中则取数；缺失则查 L2/L3 → 再缺失则访问主存（可能触发缺页）
写回：数据 → WB 写回 $t0 → 更新 PC
若中途缺页：OS 从磁盘调页（毫秒级），重新执行该 lw
```
这条链路把第 2~9 章的知识点串在一起，也是理解"为什么局部性、Cache、TLB、流水线都重要"的最佳框架。
:::

---

## 综合例题精讲（跨章节）

> 以下题目把多章知识点串在一起，均给出完整演算过程，适合考前自检。

### 综合题 1 · 性能评价三步

**题目**：程序 P 在机器 M（主频 `2 GHz`）上执行需 `10 s`，共执行 <img class="fml" src="/formulas/6827f5b6f4931a.png" alt="2 \times 10^{10}" width="69" height="33"> 条指令。编译器优化后指令数降为 <img class="fml" src="/formulas/df50a9eebbc2f9.png" alt="1.6 \times 10^{10}" width="83" height="33">，但 CPI 由 `1.0` 升为 `1.2`。① 求优化前后 CPI 与主频验证；② 判断优化是否划算；③ 若其中某模块原占总时间 `30%`、被加速 5 倍，求整体加速比。



<p class="fml-block"><img class="fml" src="/formulas/2801b94fe231dd.png" alt="\begin{gathered}
\text{(1)} \; \text{优化前：} \; \text{CPU} \; \text{时间} \; = IC \times \frac{CPI}{f} \to 2 \times 10^{10} \times \frac{1.0}{2 \times 10^{9}}= 10 s \checkmark \; \text{（与题给一致）} \\
\text{(2)} \; \text{优化后：时间} \; = 1.6 \times 10^{10} \times \frac{1.2}{2 \times 10^{9}}= 9.6 s \to \; \text{缩短} \; \text{0.4 s} \; \text{（提速约} \; \text{1.04} \; \text{倍），划算} \\
\text{MIPS} \; \text{前} \; = \frac{f}{CPI \times 10^{6}}= 2000 \; \text{；} \; \text{MIPS} \; \text{后} \; \approx 1667 \to MIPS \; \text{下降但时间更短，再次说明} \; \text{MIPS} \; \text{不可靠} \\
\text{(3) Amdahl} \; \text{：} \; S= \frac{1}{(1- 0.3)+ \frac{0.3}{5}}= \frac{1}{0.7+0.06} \approx 1.316 \\
\text{上限} \; = \frac{1}{0.7} \approx 1.43 \; \text{（即使该模块无限快也无法超过）}
\end{gathered}" width="821" height="225"></p>



### 综合题 2 · 数据表示双向转换

**题目**：① 求 <img class="fml" src="/formulas/bd8d1c44d60f28.png" alt="- 37" width="39" height="33"> 的 8 位原/反/补/移码；② 把 <img class="fml" src="/formulas/e01ce4565883d0.png" alt="- 37.25" width="61" height="33"> 编码为 IEEE 754 单精度并写成十六进制；③ 数据 16 位要配几位海明校验位。



<p class="fml-block"><img class="fml" src="/formulas/cdd9e995ad7873.png" alt="\begin{gathered}
(1)+37= 0010 0101 \to \; \text{原码} \; \text{1010 0101} \; \text{；反码} \; \text{1101 1010} \; \text{；补码} \; \text{1101 1011 (0xDB)} \\
\text{移码} \; \text{=} \; \text{补码符号位取反} \; \text{= 0101 1011 (0x5B)} \\
(2) 37.25= 100101.01_{2}= 1.0010101_{2} \times 2^{5} \\
\text{S=1} \; \text{；} \; E= 5+ 127= 132= 1000 0100_{2} \; \text{；} \; \text{M = 0010101} \; \text{后补} \; \text{0} \; \text{到} \; \text{23} \; \text{位} \\
\text{拼接：} \; \text{1 | 10000100 | 00101010000000000000000} \\
\text{= 1100 0010 0001 0101 0000 0000 0000 0000 = 0xC2150000} \\
(3) 2^{k} \ge 16+ k+ 1 \; \text{：} \; k=4 \to 16&lt; 21 \times \; \text{；} \; k=5 \to 32 \ge 22 \checkmark \to \; \text{需} \; \text{5} \; \text{位校验位，总} \; \text{21} \; \text{位}
\end{gathered}" width="725" height="193"></p>



### 综合题 3 · 运算与溢出

**题目**：8 位补码下计算 `100 + 40` 与 <img class="fml" src="/formulas/edb6c5f295c23f.png" alt="- 100- 40" width="87" height="33">，判断是否溢出并写出结果；再用 Booth 规则说明 <img class="fml" src="/formulas/1ef8a6ddfd2f79.png" alt="X=- 3, Y=+5" width="138" height="33"> 的乘积符号与数值。



<p class="fml-block"><img class="fml" src="/formulas/f90b1665abf88e.png" alt="\begin{gathered}
\text{100 = 0110 0100} \; \text{，} \; 40= 0010 1000 \to \; \text{和} \; = 1000 1100=- 116 \; \text{（应为} \; \text{+140} \; \text{）} \\
C_{n}= 0 \; \text{（符号位无进位）、} \; C_{n- 1}= 1 \to OV=1 \; \text{，正溢出，结果无效} \\
- 100= 1001 1100 \; \text{，} \; - 40= 1101 1000 \to \; \text{和} \; = 1 0111 0100 \to 0111 0100=+116 \; \text{（应为} \; - 140 \; \text{）} \\
C_{n}= 1 \; \text{、} \; C_{n- 1}= 0 \to OV=1 \; \text{，负溢出} \\
\text{Booth} \; \text{：} \; X=- 3 \; \text{（} \; \text{4} \; \text{位补码} \; \text{1101} \; \text{），} \; \text{Y=+5} \; \text{（} \; \text{0101} \; \text{，末位补} \; 0 \to 01010 \; \text{）} \\
\text{相邻位从低到高：} \; 10 \to \; \text{减} \; \text{[X]} \; \text{补；} \; 01 \to \; \text{加} \; \text{[X]} \; \text{补；} \; 10 \to \; \text{减} \; \text{[X]} \; \text{补；} \; 01 \to \; \text{加} \; \text{[X]} \; \text{补；最后不移位} \\
\text{符号} \; \text{=} \; \text{负} \; \text{⊕} \; \text{正} \; \text{=} \; \text{负；数值} \; 3 \times 5= 15 \to \; \text{积} \; =- 15 \; \text{（} \; \text{8} \; \text{位补码} \; \text{1111 0001} \; \text{）}
\end{gathered}" width="807" height="190"></p>



### 综合题 4 · 存储系统联合计算

**题目**：主存按字节编址、32 位地址；用 `1M×8 位` 芯片构成 `4M×32 位` 主存；Cache 容量 `64 KB`、块 `128 B`、**4 路组相联**；L1 命中 `1 ns`、缺失率 `5%`、L2 命中 `10 ns`、L2 局部缺失率 `20%`、主存 `100 ns`。求：① 芯片数与地址分配；② Cache 组数、Tag 位数；③ AMAT；④ 若理想 CPI=2、缺失代价折算 100 周期、访存指令占 30%，估算实际 CPI。



<p class="fml-block"><img class="fml" src="/formulas/b675b594d6d6c8.png" alt="\begin{gathered}
\text{(1)} \; \text{片数} \; =\left(\frac{4M}{1M}\right) \times\left(\frac{32}{8}\right)= 4 \times 4= 16 \; \text{片；地址} \; \text{22} \; \text{位，低} \; \text{20} \; \text{位片内寻址，高} \; \text{2} \; \text{位片选} \\
\text{(2)} \; \text{块内偏移} \; = \log_{2}128= 7 bit \; \text{；行数} \; = \frac{64 KB}{128 B}= 512 \; \text{；} \; \text{4} \; \text{路} \; \to \; \text{组数} \; = \frac{512}{4}= 128 \to \; \text{组号} \; \text{7 bit} \\
Tag= 32- 7- 7= 18 bit \; \text{（另需有效位、脏位）} \\
\text{(3) L1} \; \text{缺失代价} \; = 10+ 0.20 \times 100= 30 ns \to AMAT= 1+ 0.05 \times 30= 2.5 ns \\
\text{(4)} \; \text{取指缺失停顿} \; = 1 \times 0.05 \times 100= 5 \; \text{；数据缺失停顿} \; = 0.30 \times 0.05 \times 100= 1.5 \\
\text{实际} \; CPI \approx 2+ 5+ 1.5= 8.5 \to \; \text{存储子系统是主要瓶颈}
\end{gathered}" width="790" height="201"></p>



### 综合题 5 · 指令、寻址与单周期 CPU

**题目**：指令字长 16 位、地址码 4 位、扩展操作码；三地址 12 条、二地址 12 条、一地址 12 条，求零地址最多几条。另：PC=`0x0800`（指令长 4 B）、相对转移位移 <img class="fml" src="/formulas/ecab82b4705540.png" alt="- 5" width="30" height="34">（按字计），求目标地址；最后给出单周期 CPU 的时钟周期估算。



<p class="fml-block"><img class="fml" src="/formulas/8ac2db3e6b0bf4.png" alt="\begin{gathered}
\text{(1)} \; \text{按「剩余扩展槽} \; \times 16 \; \text{」逐层递推：} \\
\text{三地址层：} \; \text{16} \; \text{个} \; \text{OP} \; \text{编码，用} \; \text{12} \; \text{条} \; \to \; \text{剩} \; \text{4} \; \text{个扩展槽} \\
\text{二地址层：} \; 4 \times 16= 64 \; \text{个可用编码，用} \; \text{12} \; \text{条} \; \to \; \text{剩} \; 64- 12= 52 \; \text{个扩展槽} \\
\text{一地址层：} \; 52 \times 16= 832 \; \text{个可用编码，用} \; \text{12} \; \text{条} \; \to \; \text{剩} \; 832- 12= 820 \; \text{个扩展槽} \\
\text{零地址层：} \; 820 \times 16= 13120 \; \text{条（最多）} \\
\text{对照} \; \text{5.1.2} \; \text{的经典题} \; \text{15/15/15} \; \text{：剩} \; 1 \to 16- 15=1 \to 16- 15=1 \to 1 \times 16= 16 \; \text{条} \; \checkmark \\
\text{(2)} \; \text{取指后} \; \text{PC = 0x0800 + 4 = 0x0804} \; \text{；目标} \; = 0x0804+(- 5 \times 4)= 0x0804- 0x14= 0x07F0 \\
\text{(3)} \; \text{单周期时钟周期} \; \text{=} \; \text{最慢指令（} \; \text{lw} \; \text{）路径上所有部件延迟之和；} \\
\text{若} \; \text{PC 2 + IM 8 +} \; \text{译码} \; \text{3 + RF} \; \text{读} \; \text{5 + ALU 8 + DM 10 + RF} \; \text{写} \; 5= 41 ns \to \; \text{主频上限约} \; \text{24 MHz}
\end{gathered}" width="766" height="245"></p>



### 综合题 6 · 流水线、总线与 I/O 综合

**题目**：5 级流水线执行 `200` 条指令，每段 `2 ns`、锁存器开销 `0.5 ns`；分支占 `20%`、预测失败率 `10%`、惩罚 `3` 拍；另有 64 bit / 100 MHz 总线以 DMA 方式传 `2 MB`（每周期 1 次）。求：① 时钟周期与理想流水时间；② 含分支停顿的实际 CPI 与总时间；③ 总线带宽与 DMA 传送时间。



<p class="fml-block"><img class="fml" src="/formulas/95533ccc389d01.png" alt="\begin{gathered}
\text{(1)} \; \text{时钟周期} \; \text{= 2 + 0.5 = 2.5 ns} \\
\text{理想} \; T_{\text{流}} =(5+ 200- 1) \times 2.5= 204 \times 2.5= 510\,\text{ns} \\
\text{非流水} \; T= 200 \times 5 \times 2= 2000 ns \to \; \text{理想加速比} \; \approx 3.92 \\
\text{(2)} \; \text{分支停顿} \; = 0.20 \times 0.10 \times 3= 0.06 \; \text{周期} \; \text{/} \; \text{指令} \; \to \; \text{实际} \; \text{CPI = 1 + 0.06 = 1.06} \\
\text{总时间} \; \approx 200 \times 1.06 \times 2.5= 530 ns \; \text{（比理想多} \; \text{20 ns} \; \text{）} \\
\text{(3)} \; \text{带宽} \; = \frac{64}{8} \times 100 \times 10^{6}= \frac{800 MB}{s} \\
\text{DMA} \; \text{传送} \; 2 MB \to \frac{2}{800 s}= 2.5 ms \; \text{；} \; \text{CPU} \; \text{只在配置与结束中断时介入}
\end{gathered}" width="651" height="220"></p>



::: tip 解题模板
遇到计算题先圈出**已知量的单位**（bit / B / 周期 / ns / MHz），再选公式。**凡是"率"都要看清是局部还是全局**；凡涉及地址都要先画出「Tag | 索引 | 偏移」或「VPN | 偏移」的位划分；凡涉及时间都要明确是"单条指令"还是"整段程序"。最后用数量级常识校验结果（磁盘毫秒、主存纳秒、CPU 亚纳秒）。
:::

## 附录 A 公式与结论速查

| 主题 | 公式 / 结论 |
| --- | --- |
| CPU 时间 | `T = IC × CPI × 时钟周期 = IC × CPI / f` |
| 加权 CPI | `Σ(各类指令 CPI × 该类占比)` |
| MIPS / MFLOPS | <img class="fml" src="/formulas/1c84265ae5a6a1.png" alt="MIPS= \frac{f}{CPI \times 10^{6}}" width="143" height="35">；MFLOPS 为每秒百万次浮点运算 |
| **Amdahl 定律** | `S = 1 / [(1−F) + F/S_局部]`；上限 <img class="fml" src="/formulas/17a8a6e59957d1.png" alt="\frac{1}{1- F}" width="37" height="35"> |
| Gustafson | <img class="fml" src="/formulas/4863d152338471.png" alt="S= p- \alpha(p- 1)" width="138" height="34">（问题规模随并行度增大） |
| 补码范围 | <img class="fml" src="/formulas/98baf1211e5807.png" alt="- 2^{n- 1} \sim 2^{n- 1}- 1" width="142" height="34">；`[−Y]补 = [Y]补 取反加 1` |
| 移码 | `[X]移 = 2^(n−1) + X`；= 补码符号位取反 |
| IEEE 754 单精度 | <img class="fml" src="/formulas/b3565484dadb3a.png" alt="(- 1)^S \times(1.M) \times 2^{E- 127}" width="192" height="34">；S1/E8/M23，双精度 S1/E11/M52、bias 1023 |
| 海明码 | <img class="fml" src="/formulas/f10fa185bf9c8b.png" alt="2^{k} \ge n+ k+ 1" width="121" height="34">；可纠 1 位、加总校验位可检 2 位 |
| 补码溢出 | <img class="fml" src="/formulas/2fb7151bbf8933.png" alt="OV= C_{n} ⊕ C_{n- 1}" width="139" height="33">；双符号位 01 正溢出、10 负溢出 |
| 浮点加减 | 对阶（小阶向大阶）→ 尾数加减 → 规格化 → 舍入 → 判阶码溢出 |
| BCD 修正 | 某 4 位组结果大于 9 或产生进位 → 该组加 6（0110） |
| 芯片扩展 | 片数 = `(目标容量/芯片容量) × (目标字长/芯片字长)` |
| DRAM 刷新 | 异步刷新间隔 = 刷新周期 / 行数 |
| Cache 地址 | `Tag 位数 = 地址位数 − 索引位数 − 块内偏移位数`；容量 = 行数 × 块大小 |
| **AMAT** | `命中时间 + 缺失率 × 缺失代价`；多级时逐级嵌套 |
| 访存停顿 | `IC×指令缺失率×缺失代价 + IC×访存指令占比×数据缺失率×缺失代价` |
| 虚存 | `VPN 位数 = VA 位数 − log2页大小`；页表大小 = `2^VPN × PTE 大小`；`PA = PFN | offset` |
| 扩展操作码 | 少用一条短格式指令可多换得 `2^剩余字段位数` 条长格式指令 |
| 单周期时钟周期 | 由最慢指令（通常 lw）的各部件延迟之和决定 |
| 微程序控存 | 容量 = 微指令条数 × 微指令字长 |
| 流水线 | `T_流 = (k+n−1)t`；<img class="fml" src="/formulas/3fb93f02798ce4.png" alt="S= \frac{nk}{k+n- 1} \to k" width="125" height="35">；<img class="fml" src="/formulas/1c98386e34de92.png" alt="TP= \frac{n}{(k+n- 1)t}" width="116" height="37">；<img class="fml" src="/formulas/4f81664adac53b.png" alt="E= \frac{n}{k+n- 1}" width="90" height="35"> |
| 实际 CPI | `理想 CPI + 结构/数据/控制停顿 + 存储缺失停顿` |
| 总线带宽 | `宽度(bit)/8 × 频率 × 每周期传送次数` |
| 磁盘存取时间 | `寻道 + 旋转延迟 + 传输 + 控制器开销`；平均旋转延迟 = 半圈时间 |
| DMA | CPU 只做预处理与后处理；传送期由 DMAC 接管总线（周期窃取） |

## 附录 B 易错点速查

1. 「存储程序」指指令与数据以同等地位存于同一存储器，不是"程序存在硬盘里"。
2. **ISA 是软硬件交界面**；流水线级数、Cache 大小、乱序与否属于微体系结构，不属于 ISA。
3. 计算机组成 ≠ 计算机系统结构：前者是实现，后者是程序员可见的属性。
4. `CPU 时间 = IC × CPI / f`，主频高不一定快；MIPS 不含指令数，不能跨 ISA 比较。
5. Amdahl 定律中的 `F` 是**原执行时间占比**，不是代码行数占比；整体加速上限 <img class="fml" src="/formulas/17a8a6e59957d1.png" alt="\frac{1}{1- F}" width="37" height="35">。
6. 字长、地址位数、数据总线宽度是三个不同概念，不必相等。
7. 网络速率单位用十进制（<img class="fml" src="/formulas/c500dda905c832.png" alt="k=10^{3}" width="65" height="34">），存储容量用 2 的幂（<img class="fml" src="/formulas/1c06b1599c6678.png" alt="K=2^{10}" width="70" height="34">），别混。
8. 原码/反码的 ±0 有两种表示；补码 0 唯一且能多表示 <img class="fml" src="/formulas/e44aaeff3d7cff.png" alt="- 2^{n- 1}" width="54" height="34">。
9. 8 位补码 `1000 0000` 是 <img class="fml" src="/formulas/1295480bb76d11.png" alt="- 128" width="47" height="34">，没有对应的 8 位原码/反码。
10. 求 `[−Y]补` 要**连同符号位**一起取反再加 1。
11. 符号扩展：正数补 0、负数补 1；零扩展只用于无符号数。
12. IEEE 754 单精度 bias = **127**（不是 128），双精度 1023；隐藏位 1 只在规格化数时存在。
13. 非规格化数（<img class="fml" src="/formulas/d3ba3af0f933b7.png" alt="E=0, M=0" width="114" height="34">）的隐藏位是 0，用于渐进下溢；`E=全1, M=0` 是 ±∞，<img class="fml" src="/formulas/dea4120ae665cc.png" alt="M=0" width="59" height="34"> 是 NaN。
14. 浮点运算**不满足结合律**；对阶永远是小阶向大阶看齐。
15. 浮点溢出判的是**阶码**；尾数溢出可通过右规修正。
16. 大端高位字节在低地址，小端低位字节在低地址；跨平台传输必须统一字节序。
17. 数据对齐影响访存次数与 `sizeof(结构体)`，成员排列顺序会改变结构大小。
18. 海明码条件是 <img class="fml" src="/formulas/24e01f81fa0e7f.png" alt="2^{k} \ge n+k+1" width="120" height="34">；奇偶校验只能检奇数位错。
19. 补码溢出判断用 <img class="fml" src="/formulas/ca2a02ca719c74.png" alt="C_{n} ⊕ C_{n- 1}" width="87" height="33"> 或双符号位；无符号溢出看最高位进位。
20. 同号相加才可能溢出，异号相加永不溢出。
21. Booth 乘法最后一步**不移位**；n 位乘数得到 2n 位积。
22. 加减交替除法中余数为负时下一步是**加除数**；恢复余数法要先加回再左移。
23. 浮点对阶右移会丢精度，需 G/R/S 保护位；舍入默认就近偶数。
24. SRAM 不需刷新、快但贵；DRAM 需按**行**刷新、行列地址复用。
25. DRAM 刷新按行而非按字节；集中刷新有"死区"，异步刷新是折中。
26. 存储器芯片扩展：既要位扩展也要字扩展，片选由高位地址译码产生。
27. Cache 与主存之间按**块**传送；块越大空间局部性越好但缺失代价越高。
28. Cache 容量通常指数据阵列，不含 Tag/有效位/脏位；审题看清"总容量"含义。
29. 直接映射无需替换算法；相联度越高冲突缺失越少，但命中时间与硬件成本上升。
30. 写回法要脏位、写直达常配写缓冲；多核一致性用 MESI/MOESI。
31. `AMAT = 命中时间 + 缺失率 × 缺失代价`，命中时间始终要算。
32. 多级 Cache 要分清**局部缺失率**与**全局缺失率**。
33. 三级缺失：冷启动（compulsory）、容量（capacity）、冲突（conflict）。
34. `TLB` 是页表的 Cache，不是主存的 Cache；地址变换由 MMU 完成。
35. 页内偏移位数只由**页大小**决定；PFN 位数由**物理地址位数**决定。
36. 缺页异常要重新执行原指令；单级页表过大需用多级页表/大页。
37. Cache 解决速度差、虚存解决容量与保护；一次访存可能先后经历 TLB 与 Cache 缺失。
38. ISA 中 RISC 的"指令少"指**种类少**，同等程序的指令条数可能更多。
39. 扩展操作码中短格式指令少用一条，可换得 `2^剩余字段位数` 条长格式指令。
40. 变址与基址的区别在于**谁修改寄存器**（程序 vs OS）；相对寻址基准是取指后的 PC。
41. `move`/`li` 常是汇编器伪指令，不是真正的机器指令。
42. 过程调用约定区分 caller-saved 与 callee-saved 寄存器；递归靠栈帧。
43. 单周期控制器是**组合逻辑**无状态；多周期控制器必须有状态机与暂存寄存器。
44. 单周期 `CPI=1` 但时钟周期由最慢指令决定，性能未必优于多周期。
45. 单周期 CPU 需分离指令/数据存储器，否则 IF 与 MEM 产生结构冒险。
46. 微程序控制器慢但易改指令系统；微指令含控制字段 + 顺序字段。
47. 异常是同步的、中断是异步的；精确异常要求后续指令不留副作用。
48. 流水线**不缩短单条指令执行时间**，提高的是吞吐率；加速比上限为段数 k。
49. 各段不均衡 + 锁存器开销 + 冒险停顿使实际加速比远小于 k。
50. 转发能消除 <img class="fml" src="/formulas/6e7e9965925f20.png" alt="ALU \to ALU" width="114" height="34"> 的 RAW 停顿，但 **Load-Use 仍需 1 拍**。
51. WAR/WAW 是伪相关，只有乱序执行时才需寄存器重命名消除。
52. 分支预测失败的惩罚随流水线深度增大；超标量理想 `CPI = 1/发射宽度`。
53. 总线带宽公式用的是**数据线宽度**，不是地址线宽度；复用地址/数据会降低有效带宽。
54. 同步总线受最慢设备与时钟偏斜限制；异步总线靠握手但开销大。
55. 独立请求仲裁最快但线数最多；菊花链优先级固定且对链路故障敏感。
56. 统一编址（MMIO）用普通访存指令、占主存地址空间；独立编址需专用 `IN/OUT`。
57. 中断方式数据仍经 CPU 中转；**DMA 数据不经 CPU**，但会争用总线/主存带宽。
58. DMA 预处理与后处理由 CPU 完成，传送阶段 DMAC 是总线主设备。
59. 中断响应优先级（硬件排队）与处理优先级（屏蔽字）是两个不同概念。
60. 磁盘平均存取时间 = 寻道 + 平均旋转延迟（半圈）+ 传输 + 控制器开销；随机 I/O 主要受机械延迟限制。
61. RAID 0 无冗余、RAID 1 镜像、RAID 5 分布校验容 1 盘、RAID 6 容 2 盘；RAID 不是备份。
62. SSD 写入前需擦除、有写放大与寿命限制；NVMe 用多队列降低延迟。
63. 现代 x86 把 CISC 指令译码为类 RISC <img class="fml" src="/formulas/5e147d0229697b.png" alt="\mu op" width="36" height="34">；"CISC/RISC 截然对立"已是过时观点。







