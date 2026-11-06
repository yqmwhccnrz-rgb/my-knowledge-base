---
summary: "14 章 MATLAB 笔记：从矩阵与运算、程序流程控制、绘图，到数据分析、数值积分、方程求解与符号计算，再到句柄图形、GUI、Simulink 与接口；涵盖隐式扩展、string、预分配等实战要点。"
---

# Matlab 笔记

::: info 笔记概要
- **所属课程**：MATLAB 程序设计与应用
- **核心内容**：以矩阵为基本数据对象，掌握数据运算、矩阵处理、M 文件与流程控制、绘图、数据分析与多项式、数值微分积分、方程求解、符号计算，并了解句柄图形、GUI、Simulink 与外部接口
- **学习建议**：每个函数都要亲手敲一遍并观察 `size` / `class` / 输出；**点运算（`.*` `./` `.^`）与矩阵运算（`*` `/` `^`）的区别**是全书第一重点，务必分清；统计函数默认「按列」，可用 `dim=2` 改按行
- **关键词**：矩阵、点运算、冒号表达式、M 文件、函数文件、plot、polyfit、integral、ode45、syms、句柄
:::


## 全书目录

| 章节 | 主要内容 |
| --- | --- |
| 第 1 章 | MATLAB 概貌与主要功能、操作界面、搜索路径、命令行基本操作、帮助系统 |
| 第 2 章 | 数值数据类型、矩阵表示、冒号表达式、元素引用、变量与预定义变量、内部函数、算术/关系/逻辑运算、字符串、结构与单元数据 |
| 第 3 章 | 特殊矩阵、矩阵变换、矩阵求值、特征值与特征向量、稀疏矩阵 |
| 第 4 章 | M 文件、顺序/选择/循环结构、函数文件、参数可调性、全局与局部变量、特殊形式函数、程序调试与优化 |
| 第 5 章 | 二维曲线、其他二维图形、三维图形、隐函数绘图、图形修饰、图像处理与动画 |
| 第 6 章 | 数据统计分析、多项式计算、数据插值、曲线拟合 |
| 第 7 章 | 数值微分、数值积分、离散傅里叶变换 |
| 第 8 章 | 线性方程组求解、非线性方程求解、最优化问题、常微分方程初值问题 |
| 第 9 章 | 符号对象、符号微积分、级数、方程符号求解 |
| 第 10 章 | 图形对象与句柄、图形窗口与坐标轴、低层绘图、光照与材质 |
| 第 11 章 | 对话框设计、菜单设计、可视化 GUI 设计 |
| 第 12 章 | Simulink 基础、仿真模型建立、仿真分析、子系统封装、S 函数 |
| 第 13 章 | 与 Office 混合使用、数据接口（文件 / MAT）、与其他语言接口（MEX / 引擎） |
| 第 14 章 | 综合应用：电路、控制系统、分形曲线、最优化、工程结构 |
| 附录 A | 全书易错点速查 |
| 附录 B | 常用函数速查表 |
| 附录 C | 原书 17 个上机实验索引 |

---

## 第1章 MATLAB 系统环境

### 1.1 MATLAB 概貌

MATLAB 是 **MATrix LABoratory（矩阵实验室）** 的缩写，20 世纪 70 年代后期由美国新墨西哥大学 **Cleve Moler** 教授为方便学生调用 LINPACK / EISPACK 而编写，早期用 FORTRAN 实现。1984 年 **MathWorks** 公司成立并推出 MATLAB 1.0（DOS 版），核心改用 C 语言编写。1992 年的 4.0 版具有划时代意义，随后加入符号计算工具包与 Simulink。


MATLAB 起源于矩阵运算，现已把**数值计算、符号计算、图形处理、系统仿真、程序流程控制**集成在统一环境中，并提供面向特定领域的工具箱（Toolbox）。

### 1.2 主要功能

| 功能 | 说明 |
| --- | --- |
| 数值计算 | 以矩阵为基本数据对象，提供国际公认的可靠算法与高度优化的函数库，是 MATLAB 的立身之本 |
| 符号计算 | 可求解析解；原书时代借助 MuPAD 引擎(详见附录 B.1) |
| 绘图 | 分**高层绘图**（`plot` 等，给参数即出图）与**低层绘图**（直接操作图形对象句柄，更灵活）两个层次 |
| 程序设计语言 | 具备流程控制、函数调用、数据结构、输入输出、面向对象等特征，是解释性语言 |
| 工具箱扩展 | 分**功能性工具箱**（扩充符号计算、仿真、文字处理等）与**学科性工具箱**（Control System、Signal Processing、Optimization、Statistics 等） |



### 1.3 操作界面与搜索路径

R2012b 之后的主窗口主要由以下部分组成：

| 窗口 | 作用 |
| --- | --- |
| 命令行窗口 (Command Window) | 输入命令并立即执行，`>>` 为提示符 |
| 工作区 (Workspace) | 显示当前所有变量的名称、大小、类型、字节数 |
| 当前文件夹 (Current Folder) | 显示当前目录下的文件，相当于工作目录 |
| 命令历史记录 (Command History) | 记录曾执行过的命令，可双击重跑 |
| 图形窗口 / 编辑器 | 绘图输出与 M 文件编辑 |

**搜索路径**是 MATLAB 查找文件的目录集合。当输入一个名字（如 `foo`）时，MATLAB 按以下顺序查找：

1. 是否为工作区中的变量
2. 是否为当前目录下的文件
3. 是否为搜索路径中的文件（内置函数优先级最高）

::: danger 易错点
若你的 M 文件不在当前目录、也不在搜索路径中，运行会报「未定义函数或变量」。用 `addpath('D:\mycode')` 临时加入，或 `pathtool` 图形化设置；`which foo -all` 可以查看 MATLAB 最终会调用哪个同名文件——**同名遮蔽**是常见 bug 来源。
:::

### 1.4 命令行基本操作

```matlab
>> 3 + 4
ans =
     7

>> x = 1:5          % 末尾不加分号 → 显示结果
x =
     1     2     3     4     5

>> y = x.^2;        % 加分号 → 只执行、不显示
>> who              % 列出变量名
>> whos             % 列出变量名 + 大小 + 字节数 + 类型
>> clear x          % 删除变量 x
>> clc              % 清屏（不删变量）
>> close all        % 关闭所有图形窗口
>> format long      % 改变输出显示精度（不改变内部存储精度）
```

常用 `format`：`short`（默认，4 位小数）、`long`（15 位）、`short e` / `long e`（科学记数）、`rat`（有理数近似）、`hex`（十六进制机器表示）、`compact` / `loose`（空行疏密）。`format` 单独使用恢复默认。



### 1.5 帮助系统

```matlab
help plot          % 显示函数帮助文本（M 文件开头的连续注释）
doc plot           % 打开完整文档（含示例）
lookfor fourier    % 在所有函数第一行注释中搜索关键词
which plot -all    % 定位函数文件位置
demo               % 演示
```

::: tip 提示
`help` 显示的是**函数文件开头连续的 `%` 注释行**，所以自己写函数时写好这段注释，`help 你的函数` 就能用（详见 4.3.1）。
:::

---

## 第2章 MATLAB 数据及其运算

### 2.1 数值数据类型

MATLAB 的数值数据分**整型、浮点型、复数型**，默认所有数值都是 **double（双精度，8 字节）**。

| 类别 | 类型 | 说明 |
| --- | --- | --- |
| 整型 | `int8` / `uint8`、`int16` / `uint16`、`int32` / `uint32`、`int64` / `uint64` | 带符号 / 无符号，数字表示位数 |
| 浮点 | `single`（4 字节）、`double`（8 字节，默认） | `single` 约 7 位有效数字，`double` 约 16 位 |
| 复数 | `double` / `single` 的复数形式 | 实部虚部均为浮点，`i` 或 `j` 为虚数单位 |
| 逻辑 | `logical` | 关系/逻辑运算结果，`true` / `false` |
| 字符 | `char`（单引号）、`string`（双引号） | 见 2.6 |

```matlab
>> x = int8(129)      % 超出 int8 范围(-128~127) → 饱和到 127
x =
  127
>> y = int16(129)     % 范围内 → 129
>> class(9)           % 查看类型
ans =
    'double'
>> z = complex(2, 3)  % 构造复数 2+3i
>> real(z), imag(z), abs(z), conj(z)
```


::: danger 易错点 · `i` 和 `j` 是预定义变量
`i` / `j` 默认是虚数单位，但**可以被重新赋值覆盖**。一旦用 `for i=1:n` 之后又要写复数，`7+5*i` 就不再是复数了。推荐两种做法：
1. 复数常量写成 `7+5i`（`i` 紧贴数字，是字面量，不受变量影响）；
2. 更稳妥地写 `7+5*1i` —— **`1i` / `1j` 永不被覆盖**，是工程代码的首选。
:::

### 2.2 矩阵的表示

矩阵是 MATLAB **最基本的数据对象**，大部分运算都在矩阵意义下执行。无需声明维数与类型，系统自动配置。

#### 2.2.1 建立矩阵

```matlab
A = [1,2,3; 4,5,6; 7,8,9]      % 同一行用逗号/空格分隔，不同行用分号
B = [2+3i, 5; 3-5j, 6j]        % 复数矩阵
C = [A, B; B, A]                % 用小矩阵拼接成大矩阵（要求维度相容）
R = [1,2,3; 4,5,6]; I = [6,7,8; 9,10,11];
Z = R + 1i*I                    % 实部矩阵 + 虚部矩阵构成复数矩阵
```


#### 2.2.2 冒号表达式与 linspace

```matlab
e1:e2:e3        % 初值:步长:终值，生成行向量
0:1:5           % → [0 1 2 3 4 5]
0:5             % 省略步长 → 步长 1，等价于 0:1:5
1:-2:10         % 步长为负而初值<终值 → 空矩阵 []
linspace(a,b,n) % a 到 b 之间等分 n 个点（含端点），n 省略时为 100
linspace(0,pi,6)% → [0 0.6283 1.2566 1.8850 2.5133 3.1416]
logspace(a,b,n) % 10^a 到 10^b 之间 n 个对数等分点
```

`linspace(a,b,n)` 等价于 `a:(b-a)/(n-1):b`。


#### 2.2.3 矩阵元素的引用

**下标（Subscript）方式**：`A(3,2)` 表示第 3 行第 2 列，下标必须是正整数。

```matlab
A = [1,2,3; 4,5,6];
A(3,2) = 200        % 下标越界 → 自动扩展矩阵，未赋值的新位置补 0
```

**序号（Index / 线性索引）方式**：MATLAB **按列存储**元素，序号即内存中的排列顺序。

```matlab
>> A = [1,2,3; 4,5,6];
>> A(3)             % 第 3 号元素是 2（即 A(1,2)）
ans =
     2
```

对 m×n 矩阵，`A(i,j)` 的序号为 `(j-1)*m + i`。转换函数：

```matlab
D = sub2ind(size(A), I, J)    % 下标 → 序号
[I, J] = ind2sub([3,3], [1,3,5])   % 序号 → 下标
```

::: danger 易错点 · 按列优先，不是按行
`A = [1 2 3; 4 5 6]` 的线性索引顺序是 **1 → 4 → 2 → 5 → 3 → 6**，不是 1 2 3 4 5 6。用 `reshape`、`A(:)`、`find` 时务必记住这一点。
:::

**用冒号取子矩阵**：

| 写法 | 含义 |
| --- | --- |
| `A(i,j)` | 第 i 行第 j 列元素 |
| `A(i,:)` | 第 i 行全部元素 |
| `A(:,j)` | 第 j 列全部元素 |
| `A(i:i+m, k:k+m)` | 指定行列范围构成的子矩阵 |
| `A(end,:)` | 最后一行（`end` 表示该维最后一个下标） |
| `A([1,4], 3:end)` | 第 1、4 行与第 3 列到最后一列的交叉 |
| `A(:, [2,4]) = []` | 删除第 2、4 列（赋空矩阵即删除） |
| `A(:)` | 按列拉直成一个列向量 |

```matlab
x = 23:12:98;              % 举例：12 个元素的行向量
y = reshape(x, 3, 4)       % 按列重新排成 3×4
z = reshape(y, 2, 6)       % 再排成 2×6（元素总数必须不变）
```


矩阵大小相关函数：`size(A)` 返回 `[行数, 列数]`、`length(A)` 返回**最长维长度**、`ndims(A)` 返回维数、`numel(A)` 返回元素总数、`isempty(A)` 判空。

::: danger 易错点 · length 对矩阵
`length(A)` 返回 `max(size(A))`，对 3×5 矩阵返回 5，对 5×3 矩阵也返回 5——**它不是元素个数**。要元素总数用 `numel(A)`，要行数用 `size(A,1)`。
:::

### 2.3 变量及其操作

#### 2.3.1 变量名与赋值

变量名**以字母开头**，后接字母、数字或下划线，最多 63 个字符，**区分大小写**。

```matlab
myexamp12        % 合法
12myexamp        % 非法：数字开头
_myexamp12       % 非法：下划线开头
```


赋值语句两种格式：

```matlab
变量 = 表达式      % 结果赋给该变量
表达式             % 结果赋给预定义变量 ans
```

末尾加分号 `;` 则只执行不显示。**大矩阵一律加分号**，否则刷屏且极慢。

#### 2.3.2 预定义变量

| 变量 | 含义 | 变量 | 含义 |
| --- | --- | --- | --- |
| `ans` | 最近一次无赋值运算的结果 | `pi` | 圆周率 π |
| `i` / `j` | 虚数单位 | `eps` | 浮点相对精度（约 2.22e-16） |
| `inf` / `Inf` | 无穷大（如 `1/0`） | `NaN` / `nan` | 非数（如 `0/0`、`inf/inf`） |
| `realmax` | 最大正实数 | `realmin` | 最小正实数 |
| `nargin` | 函数调用时输入实参个数 | `nargout` | 调用时输出实参个数 |

::: danger 易错点 · 不要给预定义变量赋值
给 `pi`、`i`、`eps` 赋值会覆盖其含义，产生极隐蔽的错误。若确实写过 `i = 3`，用 `clear i` 恢复。
:::

#### 2.3.3 变量管理

```matlab
who                 % 只列变量名
whos                % 变量名 + 大小 + 字节 + 类型
clear               % 清除全部工作区变量
clear a b           % 只清除 a、b
save mydata a x     % 把 a、x 存入 mydata.mat
save mydata -append % 追加变量到已有 MAT 文件
load mydata         % 载入 mydata.mat 中的变量
```


### 2.4 常用内部函数

内部函数（系统函数/库函数）的**自变量规定为矩阵**，运算法则是**逐元素作用**，结果与自变量同型。

```matlab
A = [4,2; 3,6];
B = sqrt(A)         % → [2.0000 1.4142; 1.7321 2.4495]
```

| 类别 | 函数 |
| --- | --- |
| 三角（弧度） | `sin` `cos` `tan` `asin` `acos` `atan` |
| 三角（角度） | `sind` `cosd` `tand` `asind` `acosd` `atand`（函数名后加 `d`） |
| 双曲 / 反双曲 | `sinh` `cosh` `tanh` / `asinh` `acosh` `atanh` |
| 指数对数 | `exp` `log`（自然对数）`log10` `log2` `sqrt` `pow2` |
| 取整 | `fix`（向 0）`floor`（向下）`ceil`（向上）`round`（四舍五入） |
| 余数 | `rem`（求余）`mod`（求模） |
| 其他 | `abs`（绝对值/复模/ASCII）`sign` `gcd` `lcm` `factorial` `isprime` `primes` `perms` `randperm` |

```matlab
>> abs(-4), abs(3+4i), abs('a')      % → 4, 5, 97
>> fix(2.45), floor(2.45), ceil(2.45), round(2.45)   % → 2 2 3 2
>> fix(-2.65), floor(-2.65), ceil(-2.65), round(-2.65) % → -2 -3 -2 -3
```

::: danger 易错点 · `rem` 与 `mod` 对负数不同
`rem(a,b) = a - b.*fix(a./b)`，商向 **0** 取整，结果符号随 **a**；
`mod(a,b) = a - b.*floor(a./b)`，商向 **负无穷** 取整，结果符号随 **b**。

```matlab
>> rem(-7,4), mod(-7,4)     % → -3, 1
>> rem(7,-4), mod(7,-4)     % →  3, -1
```
a、b 同号时两者相等；异号时 `mod(a,b) = rem(a,b) + b`。另外 `rem(a,0)=NaN`，`mod(a,0)=a`。
:::

#### 2.4.2 矩阵超越函数

函数名在普通函数后加 `m`，**输入必须是方阵**，是矩阵意义（而非逐元素）的运算：

```matlab
sqrtm(A)         % 矩阵平方根 B，满足 B*B = A
logm(A)          % 矩阵自然对数
expm(A)          % 矩阵指数 e^A（与 logm 互逆）
funm(A, @fun)    % 一般矩阵函数，@fun 可取 @exp @log @sin @cos @sinh @cosh
```

::: danger 易错点 · `sqrt(A)` 与 `sqrtm(A)` 完全不同
`sqrt(A)` 是对**每个元素**开方；`sqrtm(A)` 求的是满足 `B*B = A` 的**矩阵** B。同理 `exp(A)` 逐元素求指数，`expm(A)` 才是矩阵指数。含负特征值的矩阵 `sqrtm` 会得到复矩阵；像 `[0 1; 0 0]` 这样的矩阵**不存在平方根**。
:::

### 2.5 MATLAB 运算

#### 2.5.1 算术运算

基本算术运算符：`+` `-` `*` `/`（右除）`\`（左除）`^`（乘方），**都是在矩阵意义下进行**（标量只是特例）。

```matlab
A + B             % 同型矩阵对应元素相加（或标量加每个元素）
A * B             % 矩阵乘：A 的列数必须等于 B 的行数
A \ B             % 左除：等价于 inv(A)*B，即解 A*X = B
B / A             % 右除：等价于 B*inv(A)，即解 X*A = B
A ^ 2             % 方阵乘方，等价于 A*A
```

::: danger 易错点 · 左除与右除不相等
对矩阵一般 `A\B ≠ B/A`（前者解 `A*X=B`，后者解 `X*A=B`）；含标量时两者结果才相同（如 `3/4 == 4\3 == 0.75`）。维数不相容时 `A*B` 会报「内部矩阵维度必须一致」。
:::


**点运算**（.`*` `./` `.\` `.^`）：两矩阵**对应元素**之间运算，要求同型。

```matlab
A = [1,2,3; 4,5,6; 7,8,9];
B = [-1,0,1; 1,-1,0; 0,1,1];
C = A .* B         % 对应元素相乘
A ./ B             % A 元素除以 B 对应元素；B .\ A 与之等价
A .^ 2             % 各元素各自平方
2 .^ [1 2 3]       % 底为标量
x = 0.1:0.3:1;
y = sin(x) .* cos(x);      % 必须点乘！写成 * 会报维度错误
```

::: danger 易错点 · 全书第一大坑
`*` `^` `/` 是**矩阵运算**，`.*` `.^` `./` 是**逐元素运算**。凡是「对一组 x 逐个求 y」的场景（绘图、统计、向量化），几乎都要用点运算。原书例 2-1 的 `sin(x).*cos(x)` 就是这个道理。
:::


#### 2.5.2 关系运算

6 种关系运算符：`<` `<=` `>` `>=` `==` `~=`（**注意不是 `!=`**），对应函数 `lt` `le` `gt` `ge` `eq` `ne`。

- 两个标量比较 → 结果为 `1`（真）或 `0`（假）
- 两个同型矩阵 → 逐元素比较，返回同型 0/1 矩阵
- 标量与矩阵 → 标量与每个元素比较，返回同型 0/1 矩阵

```matlab
A = fix((90-10+1)*rand(5) + 10);    % [10,90] 区间随机整数 5 阶方阵
P = rem(A,3) == 0;                  % 判断哪些元素能被 3 整除
k = find(A > 4);                    % 找出大于 4 的元素序号（线性索引）
A(k)                                % 用序号取出这些元素
```

常用关系/判定函数：`all`（全非零）、`any`（存在非零）、`find`（非零元素位置）、`exist`（变量/文件是否存在）、`isempty`、`isinf`、`isnan`、`isfinite`、`isinteger`、`isnumeric`、`isreal`、`isfloat`。



#### 2.5.3 逻辑运算

3 个运算符 `&`（与）`|`（或）`~`（非），4 个函数 `and` `or` `not` `xor`。**非零为真（1），零为假（0）**。

```matlab
A = [4,65,-54,0,6]; B = [0,5,3,2,-6];
A & B                  % → [0 1 1 0 1]
xor(A>10, B<10)
```


**优先级**：算术 > 关系 > 逻辑。`~` 是单目运算符，优先级较高。

### 2.6 字符串

#### 2.6.1 字符串的表示

```matlab
xm = 'Central South University'     % 单引号括起的字符序列（char 数组）
xm = 'I''m a teacher.'              % 串内单引号要写两遍
A = 'ABCDEF'; A(1:3)                % → 'ABC'（当作行向量引用）
ch = ['abcdef'; '123456'];          % 字符串矩阵，各行字符数必须相等
ch(2,3)                             % → '3'
```


#### 2.6.2 字符串操作

```matlab
ch = 'ABc123d4e56Fg9';
subch = ch(1:5)                     % 取子串 → 'ABc12'
revch = ch(end:-1:1)                % 倒排
k = find(ch>='a' & ch<='z');        % 找小写字母位置
ch(k) = ch(k) - ('a'-'A');         % 小写转大写（ASCII 运算）
length(k)                           % 统计个数

abs('MATLAB')                       % → [77 65 84 76 65 66]（ASCII 码）
char([77 65 84 76 65 66])          % 反转为字符串
char(abs('MATLAB')+32)              % → 'matlab'
num2str(3.14), str2num('3.14'), str2double('3.14'), int2str(3)
['Room temperature is ', num2str(21.1111), ' degrees C.']
strcat('ss','ff','DD','1234')
eval('[t, sin(t), cos(t)]')         % 把字符串当命令执行
```




#### 2.6.3 结构数据与单元数据

```matlab
% 结构数据 struct：用「字段」组织不同类型的数据
student.name = 'Tom';
student.score = [88, 92, 79];
student(2).name = 'Ann';
student(2).score = [95, 87, 90];

% 单元数据 cell：每个单元可存任意类型、任意大小
C = {1, 'hello', [1 2; 3 4]};
C{1}            % 取单元「内容」→ 1
C(1)            % 取单元「本身」→ 1×1 cell
```

::: danger 易错点 · `{}` 与 `()` 的区别
对 cell 数组，`C(k)` 返回的是 **cell**（一个包装），`C{k}` 返回的才是**里面的数据**。对 struct，`S.field` 返回字段内容；字段名不确定时用 `S.(name)` 动态访问。
:::


---

## 第3章 MATLAB 矩阵处理

### 3.1 特殊矩阵

#### 3.1.1 通用特殊矩阵

| 函数 | 作用 |
| --- | --- |
| `zeros(m,n)` | 全零矩阵；`zeros(size(A))` 生成与 A 同型 |
| `ones(m,n)` | 全 1 矩阵 |
| `eye(m,n)` | 单位矩阵（主对角线为 1） |
| `rand(m,n)` | (0,1) 区间**均匀分布**随机矩阵 |
| `randn(m,n)` | 均值 0、方差 1 的**标准正态分布**随机矩阵 |
| `randi([a,b],m,n)` | [a,b] 区间随机整数矩阵 |
| `randperm(n)` | 1~n 的随机排列 |

```matlab
x = 20 + (50-20)*rand(5);       % [20,50] 均匀分布 5 阶随机矩阵
y = 0.6 + sqrt(0.1)*randn(5);   % 均值 0.6、方差 0.1 的正态随机矩阵
```

一般化公式：`x ~ U(0,1)` → `y = a + (b-a)*x` 得到 `U(a,b)`；`x ~ N(0,1)` → `y = mu + sigma*x` 得到 `N(mu, sigma^2)`（**注意第二个参数是标准差 sigma，不是方差**，方差是 `sigma^2`）。


#### 3.1.2 专门学科特殊矩阵

| 函数 | 生成 |
| --- | --- |
| `magic(n)` | n 阶魔方矩阵，每行/列/两对角线和相等，为 `n(n^2+1)/2` |
| `vander(V)` | 以向量 V 为基础向量的范德蒙矩阵（最后一列全 1） |
| `hilb(n)` / `invhilb(n)` | n 阶希尔伯特矩阵及其精确逆矩阵 |
| `toeplitz(x,y)` / `toeplitz(x)` | 托普利兹矩阵（对称版） |
| `compan(p)` | 多项式 p 的伴随矩阵 |
| `pascal(n)` | 帕斯卡矩阵 |
| `hadamard(n)` | 哈达玛矩阵 |

```matlab
>> magic(3)
ans =
     8     1     6
     3     5     7
     4     9     2

>> M = 100 + magic(5);   % 每行/列/对角线和 = 65 + 5*100 = 565
>> vander(1:5)
>> format rat; H = hilb(4); I = invhilb(4); format
>> toeplitz(1:6)
```

::: danger 易错点 · 希尔伯特矩阵高度病态
`hilb(n)` 元素 `h(i,j) = 1/(i+j-1)`，是典型的**病态矩阵**：n 稍大时条件数极大，`inv(hilb(n))` 的数值结果很不可靠。原书给 `invhilb(n)` 正是因为它返回**精确的有理数逆**，可直接用来对比展示浮点误差。测试线性方程组算法常用它做「压力测试」。
:::

### 3.2 矩阵变换

#### 3.2.1 对角阵与三角阵

```matlab
diag(A)          % 提取主对角线元素 → 列向量
diag(A,k)        % 提取第 k 条对角线（k>0 主对角线上方，k<0 下方）
diag(V)          % 由向量 V 构造对角阵
diag(V,k)        % 把 V 放在第 k 条对角线上
triu(A)  / triu(A,k)   % 上三角（第 k 条对角线及以上保留）
tril(A)  / tril(A,k)   % 下三角
```

::: danger 易错点 · `diag(diag(A))` 与 `diag(A)`
`diag(A)`（A 为矩阵）**提取**对角线得到向量；`diag(v)`（v 为向量）**构造**对角阵。想「只保留 A 的对角线、其余置零」要写 `diag(diag(A))` 两次。原书习题也考了这个。
:::

#### 3.2.2 转置与旋转

```matlab
A.'       % 普通转置（不取共轭）
A'        % 共轭转置：实数时等价于 A.'，复数时虚部取反
rot90(A,k)% 逆时针旋转 90°×k（k=1 可省略，可为负表示顺时针）
fliplr(A) % 左右翻转
flipud(A) % 上下翻转
```

::: danger 易错点 · 复数矩阵 `'` 与 `.'`
对含复数的矩阵，`A'` 是**共轭转置**（Hermitian），`A.'` 才是纯转置。做线性代数题时用 `A'`；只想交换行列、不改变元素时用 `A.'`。这是 MATLAB 与数学书写习惯最容易混淆的一处。
:::

#### 3.2.3 矩阵求逆与伪逆

```matlab
inv(A)     % 方阵的逆（A 必须非奇异）
pinv(A)    % 伪逆（Moore-Penrose），对奇异/非方阵也适用，基于 SVD
```


### 3.3 矩阵求值

| 函数 | 含义 |
| --- | --- |
| `det(A)` | 方阵行列式 |
| `rank(A)` | 矩阵的秩 |
| `trace(A)` | 矩阵的迹（主对角线元素之和） |
| `norm(V)` / `norm(V,1)` / `norm(V,inf)` | 向量 2 范数 / 1 范数 / 无穷范数 |
| `norm(A)` / `norm(A,1)` / `norm(A,inf)` / `norm(A,'fro')` | 矩阵 2 范数（最大奇异值）/ 列和范数 / 行和范数 / Frobenius 范数 |
| `cond(A)` / `cond(A,1)` / `cond(A,inf)` | 条件数（衡量病态程度） |
| `rcond(A)` | 条件数倒数估计，接近 0 表示接近奇异 |

```matlab
A = [1,2,3; 4,5,6; 7,8,0];
det(A), rank(A), trace(A), norm(A), cond(A)
```

::: danger 易错点 · 条件数不是行列式
判断方程组是否「难算」看 **`cond(A)`**（越大越病态，1e16 量级基本不可用），**不是** `det(A)`。行列式很小不代表病态（缩放矩阵即可让 det 任意小而条件数不变）。另外 `det(A)≈0` 作为奇异判据也不可靠，应用 `rank(A)` 或 `rcond(A)`。
:::

### 3.4 矩阵的特征值与特征向量

```matlab
E = eig(A)              % 只返回全部特征值（列向量）
[V, D] = eig(A)         % V 的列是特征向量，D 是对角阵，满足 A*V = V*D
eigs(A, k)              % 求大型稀疏矩阵的前 k 个特征值
```


### 3.5 稀疏矩阵

大型矩阵若绝大多数元素为 0，用**完全存储**会浪费大量内存和计算。MATLAB 提供**稀疏存储方式**：只保存非零元素的值与位置。

```matlab
S = sparse(A)                    % 全矩阵 → 稀疏存储
A = full(S)                      % 稀疏 → 全矩阵
sparse(m,n)                      % m×n 全零稀疏矩阵
sparse(u,v,s)                    % 由等长向量构造：非零元 s(k) 位于 (u(k),v(k))
speye(m,n)                       % 稀疏单位矩阵
spdiags(B,d,m,n)                 % 带状（对角）稀疏矩阵
nnz(S)                           % 非零元素个数
spy(S)                           % 可视化非零元分布
```

```matlab
A = sparse([1,2,5,7], [1,3,2,3], [1,1,2,4]);
S = speye(3,5);
[B,d] = spdiags(A);              % 提取非零对角线
```

::: danger 易错点 · 不要先建全矩阵再 sparse
原书也提醒：真正需要稀疏矩阵时，应该**直接用 `sparse(u,v,s)` / `spdiags` / `speye` 构造**，而不是先 `zeros(10000)` 再转——后者在转换前就已耗尽内存。另外稀疏矩阵**可以参与大多数矩阵运算**，但与全矩阵混合后结果可能变回全矩阵，注意 `nnz` 与内存。
:::

---

## 第4章 MATLAB 程序流程控制

### 4.1 M 文件

M 文件是以 `.m` 为扩展名的文本文件，用 `edit 文件名` 新建或打开。分两类：

| 类型 | 特点 |
| --- | --- |
| **脚本文件 (Script)** | 无输入输出参数；直接键入文件名运行；变量**留在基本工作区**；共享调用者的工作区 |
| **函数文件 (Function)** | 以 `function` 行开头；有输入输出参数；必须以调用方式运行；内部变量是**局部变量**，执行完不保留 |

```matlab
% 脚本 exch.m —— 交换 a、b
clear;
a = 1:10;
b = [11,12,13,14; 15,16,17,18];
c = a; a = b; b = c;
a, b
% 命令行输入 exch 即执行，a/b/c 仍留在工作区
```

```matlab
% 函数 fexch.m
function [a,b] = fexch(a,b)
c = a; a = b; b = c;
end
% 命令行：[x,y] = fexch(x,y)。函数内的 a/b/c 不进入工作区
```



### 4.2 程序控制结构

三种基本结构：**顺序、选择、循环**。

#### 4.2.1 顺序结构

```matlab
a = input('请输入 a = ');        % 从键盘输入（可输入表达式）
b = input('请输入姓名：','s');   % 's' 表示按字符串读入
disp(a)                          % 显示变量值（不显示变量名）
fprintf('a = %.4f\n', a);        % 格式化输出
pause                            % 暂停，按任意键继续
pause(2)                         % 暂停 2 秒
```


#### 4.2.2 选择结构

**if 语句**（单分支 / 双分支 / 多分支）：

```matlab
if 条件
    语句组
end

if 条件
    语句组1
else
    语句组2
end

if 条件1
    语句组1
elseif 条件2
    语句组2
elseif 条件m
    语句组m
else
    语句组n
end
```

```matlab
% 例：判断字符类型
c = input('请输入一个字符：','s');
if c >= 'A' && c <= 'Z'
    disp('大写字母');
elseif c >= 'a' && c <= 'z'
    disp('小写字母');
elseif c >= '0' && c <= '9'
    disp('数字');
else
    disp('其他字符');
end
```

::: danger 易错点 · elseif 连写、条件必须标量可判
`elseif` 是**一个词**（不是 `else if`，后者会多出一个 `end`）。`if` 条件若为数组，MATLAB 要求**所有元素都为真**才成立（等价于 `all(条件(:))`），所以 `if A > 0` 对矩阵往往不是你想要的；用 `any(A(:)>0)` / `all(A(:)>0)` 明确意图。
:::

**switch 语句**：

```matlab
switch 表达式        % 应为标量或字符串
    case 结果表1
        语句组1
    case {结果表2}    % 多个结果用大括号（cell）括起来
        语句组2
    otherwise
        语句组n
end
```

```matlab
% 例：按价格区间给折扣，switch 表达式用 fix(price/100)
switch fix(price/100)
    case {0,1}
        rate = 0;
    case {2,3,4}
        rate = 0.03;
    case num2cell(5:9)
        rate = 0.05;
    case num2cell(10:24)
        rate = 0.08;
    otherwise
        rate = 0.10;
end
```

::: danger 易错点 · switch 只执行一个分支
与 C 语言不同，MATLAB 的 `switch` **不会「贯穿」**（不需要也不支持 `break`）；匹配到第一个 `case` 执行完就直接跳出。多个候选值要用 `{...}` cell 数组或 `num2cell(...)` 表达。
:::

**try 语句**（异常处理）：

```matlab
try
    语句组1            % 尝试执行
catch ME
    语句组2            % 出错后执行，ME 是 MException 对象
end
```


#### 4.2.3 循环结构

**for 语句**：循环次数事先确定时用。

```matlab
for 循环变量 = 表达式1:表达式2:表达式3
    循环体
end

for k = [1,3,2,5]      % 也可以直接遍历一个行向量的每个元素
    disp(k)
end
```

执行要点（原书总结得很到位）：
1. 冒号表达式的三个值**只在循环开始时计算一次**，循环体内改它们不影响循环次数。
2. 循环体内修改循环变量，下一轮开始时会被**重新赋为向量下一个元素**，改动不累积。
3. 退出循环后，循环变量等于向量的**最后一个元素值**。
4. 向量为空时循环体**一次也不执行**（如 `1:-2:10`）。
5. 循环变量还可以是**列向量**：`for v = A` 时每次取 A 的**一列**。

```matlab
% 例：求 [100,200] 之间第一个能被 21 整除的整数
for n = 100:200
    if rem(n,21) ~= 0
        continue        % 跳过本轮剩余语句，进入下一轮
    end
    n
    break               % 跳出整个循环
end
```


**while 语句**：循环次数不确定时用。

```matlab
while 条件
    循环体
end
```

```matlab
% 例：输入若干数，输入 0 结束，求和与平均
sum = 0; n = 0;
x = input('Enter a number (end in 0): ');
while x ~= 0
    sum = sum + x;
    n = n + 1;
    x = input('Enter a number (end in 0): ');
end
if n > 0
    sum, mean = sum/n
end
```

**break / continue / 循环嵌套**：`break` 终止循环，`continue` 跳过本轮剩余语句。嵌套循环中 `break` **只跳出它所在的最内层循环**。

```matlab
% 例：求 [1,500] 内全部完数（一个数等于其真因子之和）
for m = 1:500
    s = 0;
    for k = 1:m/2
        if rem(m,k) == 0
            s = s + k;
        end
    end
    if m == s
        disp(m)        % → 6, 28, 496
    end
end
```



### 4.3 函数文件

#### 4.3.1 基本结构

```matlab
function 输出形参表 = 函数名(输入形参表)
% 第一行注释：大写函数名 + 功能简述（供 lookfor / help 搜索）
% 后续连续注释：参数含义、调用格式（构成完整帮助文本）
%
% （空一行后的注释：作者、日期、版本等档案信息）
函数体语句
end
```

```matlab
function [s,p] = fcircle(r)
%FCIRCLE 计算半径为 r 的圆的面积和周长
%   r 圆半径；s 圆面积；p 圆周长
%   调用格式：[s,p] = fcircle(r)
s = pi*r*r;
p = 2*pi*r;
end
```

要点：
- 多个输出形参用方括号：`[s,p]`；多个输入用逗号分隔。
- **函数文件名一般与函数名一致**。不一致时 MATLAB 以**文件名为准**调用（忽略内部函数名），强烈建议统一。
- 紧随 `function` 行的**连续 `%` 注释**构成 `help 函数名` 的输出；`lookfor 关键词` 只搜第一行。
- `return` 可提前结束函数，通常省略（执行完自动返回）。
- `end` 作为函数结尾在现代 MATLAB 中可选；但**含子函数/嵌套函数时必须写 `end`**。

#### 4.3.2 函数调用与递归

```matlab
[输出实参表] = 函数名(输入实参表)
```

实参的**顺序、个数**要与形参一致。函数可以调用自身（递归）：

```matlab
function f = factor(n)
if n <= 1
    f = 1;
else
    f = factor(n-1)*n;    % 递归调用
end
end
```


#### 4.3.3 函数参数的可调性

`nargin` / `nargout` 记录调用时实参个数，据此让一个函数完成多种功能：

```matlab
function fout = charray(a,b,c)
if nargin == 1
    fout = a;
elseif nargin == 2
    fout = a + b;
elseif nargin == 3
    fout = (a*b*c)/2;
end
end
```


#### 4.3.4 全局变量与局部变量

函数内的变量默认是**局部变量**，与基本工作区及其他函数相互隔离。要共享需 `global`：

```matlab
function f = wadd(x,y)
global ALPHA BETA
f = ALPHA*x + BETA*y;
end
```
调用前也要在命令行声明：`global ALPHA BETA; ALPHA=1; BETA=2; wadd(1,2)` → 5。


### 4.4 特殊形式的函数

| 形式 | 说明 |
| --- | --- |
| **主函数 / 子函数** | 一个函数文件中第一个函数是主函数，外部只能调主函数；其余为子函数，仅本文件内可见 |
| **匿名函数** | `f = @(x) ...`，见 4.3.2 |
| **嵌套函数** | 定义在另一个函数体内，可访问外层函数的变量（需配 `end`） |
| **内联函数 `inline`** | 原书介绍过，现已废弃(见附录 B.1) |


### 4.5 程序调试与优化

**调试**：
- 在编辑器左侧行号处点设**断点**，用 `F5` 运行、`F10` 单步、`F11` 步入、`Shift+F11` 步出。
- 命令行也可用 `dbstop in 文件名 at 行号`、`dbstep`、`dbcont`、`dbquit`、`dbclear all`。
- `keyboard` 可在指定位置暂停进入调试态。
- 现代 MATLAB 编辑器会实时给出**代码分析器（Code Analyzer）**的橙色提示，很多错误不必运行就能发现。

**性能分析**：

```matlab
tic;  ...代码...;  toc       % 简单计时
profile on;  myfun();  profile viewer   % 逐函数耗时剖析
```



---

## 第5章 MATLAB 绘图

MATLAB 绘图分两个层次：**高层绘图函数**（`plot` 等，给参数即出图，最常用）与**低层绘图操作**（直接操作图形对象句柄，第 10 章）。高层函数本质上由低层函数搭建而成。

### 5.1 二维图形

#### 5.1.1 plot 基本用法

```matlab
plot(x, y)              % x、y 为等长向量，绘制线性坐标曲线
plot(y)                 % 只有 y 时，横坐标默认 1:length(y)
plot(x, y, 'r--o')      % 线型/颜色/标记一次指定
plot(x1,y1,s1, x2,y2,s2, ...)   % 一张图叠加多条曲线
plot(x, Y)              % Y 为矩阵时，按列画多条曲线，横坐标共用 x
plot(Y)                 % 按列绘制，横坐标为行号
```

```matlab
% 例 5-1：0≤x≤2π 绘制 y = 2e^(-0.5x) sin(2πx)
x = 0:pi/100:2*pi;
y = 2*exp(-0.5*x) .* sin(2*pi*x);
plot(x,y)

% 例 5-2：参数方程 x = t*cos(3t), y = t*sin(2t)
t = -pi:pi/100:pi;
x = t.*cos(3*t);
y = t.*sin(2*t);
plot(x,y)
```

::: danger 易错点 · 绘图必须点运算
`y = 2*exp(-0.5*x).*sin(2*pi*x)`：`2` 是标量可用 `*`，但 `exp(...)` 与 `sin(...)` 都是**向量**，中间必须 `.*`。写成 `*` 会报「内部矩阵维度必须一致」。这是第 2 章点运算坑在绘图里的直接体现。
:::

**线型、颜色、标记**（可组合成字符串，如 `'r--o'`）：

| 类别 | 可选项 |
| --- | --- |
| 颜色 | `b` 蓝 `g` 绿 `r` 红 `c` 青 `m` 品红 `y` 黄 `k` 黑 `w` 白 |
| 线型 | `-` 实线 `--` 虚线 `:` 点线 `-.` 点划线 |
| 标记 | `.` 点 `o` 圈 `x` 叉 `+` 加号 `*` 星 `s` 方 `d` 菱 `^` `v` `<` `>` 三角 `p` 五角 `h` 六角 |

```matlab
% 更推荐用「属性名-值对」，可读性更好
plot(x, y, 'Color', [0.2 0.4 0.8], 'LineWidth', 2, 'LineStyle', '--');
```



#### 5.1.2 图形辅助操作

```matlab
title('正弦曲线')                 % 标题（支持 LaTeX/TeX 解释器）
xlabel('x'), ylabel('y')         % 轴标签
legend('sin','cos')              % 图例（按绘制顺序对应）
grid on / grid minor             % 网格线
hold on / hold off               % 保持当前图形，允许叠加绘制
axis([xmin xmax ymin ymax])      % 设定坐标范围
axis equal                       % 两轴等比例（画圆必用）
axis tight / axis off / axis square
text(x, y, '标注')               % 在指定位置加文字
gtext('标注')                    % 用鼠标点选位置加文字
subplot(m, n, p)                 % 把窗口分成 m×n 个子图，激活第 p 个
figure / clf / close all         % 新建图形窗口 / 清空 / 关闭全部
```

```matlab
x = linspace(0, 2*pi, 200);
subplot(2,1,1); plot(x, sin(x)); title('sin'); grid on
subplot(2,1,2); plot(x, cos(x)); title('cos'); grid on
```

::: danger 易错点 · 三个经典绘图坑
1. 画叠加曲线前忘写 `hold on` → 后一条覆盖前一条。
2. 用 `plot` 画圆/椭圆后没写 `axis equal` → 看起来是椭圆（窗口拉伸）。
3. `subplot` 的 p 是**按行从左到右编号**：`subplot(2,3,4)` 是第二行第一个。
:::


### 5.2 其他形式二维图形

| 函数 | 图形 |
| --- | --- |
| `bar(x,y)` / `barh` | 条形图 / 水平条形图 |
| `histogram(x)` / `histogram(x,nbins)` | 直方图(见附录 B.1) |
| `pie(x)` / `pie3` | 饼图 |
| `stairs(x,y)` | 阶梯图 |
| `stem(x,y)` | 火柴杆（离散序列）图 |
| `semilogx` / `semilogy` / `loglog` | 单轴 / 双轴对数坐标 |
| `polarplot(theta,rho)` | 极坐标图 |
| `area` / `fill` / `errorbar` / `scatter` / `quiver` | 面积图 / 填充 / 误差棒 / 散点 / 向量场 |

```matlab
theta = 0:0.01:2*pi;
rho = sin(2*theta).*cos(2*theta);
polarplot(theta, rho)
```



### 5.3 三维图形

#### 5.3.1 三维曲线

```matlab
plot3(x, y, z)
t = 0:pi/50:10*pi;
plot3(sin(t), cos(t), t); grid on; xlabel('x'); ylabel('y'); zlabel('z')
```

#### 5.3.2 三维曲面

```matlab
[X, Y] = meshgrid(x, y);      % 由两个向量生成网格坐标矩阵（关键！）
Z = f(X, Y);                  % 对每个网格点求函数值（必须用点运算）
mesh(X, Y, Z)                 % 网格曲面（线框）
surf(X, Y, Z)                 % 着色曲面
surfc / surfl                 % 带等高线 / 带光照
contour(X, Y, Z) / contour3  % 等高线
meshc / meshz                 % 带等高线 / 带帘幕
```

```matlab
[X,Y] = meshgrid(-2:0.1:2);
Z = X.*exp(-X.^2 - Y.^2);    % 必须用 .* 和 .^
surf(X,Y,Z); shading interp; colorbar
```

::: danger 易错点 · 忘记 meshgrid 与点运算
`surf` 要求 X、Y、Z 是**同型矩阵**。先用 `meshgrid` 把向量扩展成网格矩阵，再用 `.*` `.^` 逐元素算 Z。写成 `X*exp(...)` 或 `X^2` 会报维度错误。
:::

```matlab
[X,Y,Z] = sphere(50);         % 单位球面网格
surf(X,Y,Z); axis equal
[X,Y,Z] = cylinder(r, n);     % 柱面
[X,Y,Z] = peaks(50);          % 经典测试曲面
```

#### 5.3.3 其他三维图形

`bar3` / `pie3` / `stem3` / `fill3` / `scatter3` / `ribbon` / `contour3` / `slice`（体切片）/ `isosurface`。

### 5.4 隐函数绘图

```matlab
fimplicit(@(x,y) x.^2 + y.^2 - 1)                 % 二维隐函数
fimplicit3(@(x,y,z) x.^2 + y.^2 + z.^2 - 1)      % 三维隐曲面
```


### 5.5 图形修饰处理

```matlab
view(az, el)        % 设置视点：方位角 az、仰角 el（默认 az=-37.5, el=30）
view(2) / view(3)   % 俯视 / 默认三维
rotate3d on         % 允许鼠标拖动旋转
colormap(jet)       % 色图：jet / parula(默认) / hsv / hot / cool / gray / bone
colorbar            % 显示色标
shading flat / faceted / interp   % 曲面着色方式
caxis([cmin cmax])  % 色标范围（新版用 clim）
light('Position',[1 0 1]); lighting gouraud; material shiny
axis([xmin xmax ymin ymax zmin zmax]); axis vis3d
```



### 5.6 图像处理与动画

```matlab
A = imread('photo.jpg');     % 读入图像（返回 uint8 三维数组：高×宽×通道）
imshow(A); imwrite(B,'out.png');
image(A); axis image off      % 低层显示
```

```matlab
% 动画：逐帧抓取后播放
for k = 1:50
    plot(x, sin(x + k/10)); axis([0 2*pi -1 1]); drawnow
    F(k) = getframe;         % 抓取当前帧
end
movie(F, 2, 30)              % 播放 2 遍，每秒 30 帧
```


### 5.7 交互式绘图工具

「绘图」选项卡可选变量后直接点图形类型出图；绘图工具（Plot Tools）可交互式改属性。生成的代码可用「生成代码」按钮导出，是学习属性设置的好办法。


---

## 第6章 数据分析与多项式计算

### 6.1 数据统计分析

::: danger 最重要的规则 · 默认按列
MATLAB 的统计函数默认对矩阵的**每一列**分别计算（`dim=1`），返回一个行向量；要对**每一行**计算，须显式给 `dim=2`。这与 numpy 的 `axis` 习惯不同，是最容易出错的地方。
:::

```matlab
A = [1 2 3; 4 5 6];
max(A)          % → [4 5 6]（各列最大值）
max(A,[],2)     % → [3; 6]（各行最大值）
mean(A)         % → [2.5 3.5 4.5]
mean(A,2)       % → [2; 5]
```

#### 6.1.1 最大值和最小值

```matlab
max(A)               % 各列最大值
[Y,U] = max(A)       % Y 为最大值，U 为对应位置（行号）
max(A,[],dim)        % 指定维
max(A,B)             % 两同型矩阵逐元素取较大者
max(A,[],'all')      % 全矩阵最大值
min(A)               % 同理
```

#### 6.1.2 求和与求积 / 平均值与中值

```matlab
sum(A) / sum(A,2)    % 按列 / 按行求和
prod(A)              % 各列元素连乘
mean(A)              % 算术平均
median(A)            % 中位数
mode(A)              % 众数
```

#### 6.1.3 累加和与累乘积

```matlab
cumsum(A)            % 各列累加（第 k 行为前 k 行之和）
cumprod(A)           % 各列累乘
cumsum(A,2)          % 按行累加
```

#### 6.1.4 标准差与相关系数

```matlab
std(A)               % 各列标准差，默认 flag=0（除以 n-1，样本标准差）
std(A,1)             % flag=1（除以 n，总体标准差）
std(A,flag,dim)      % 完整格式
var(A)               % 方差（同样有 flag/dim）
cov(A)               % 协方差矩阵
corrcoef(A)          % 相关系数矩阵
```

::: danger 易错点 · std 的 flag
`std(x)` 默认按 **n-1** 归一化（无偏样本标准差），`std(x,1)` 才按 **n**。如果你和 pandas/numpy 的结果对不上，多半是这个默认值的差异（numpy 的 `np.std` 默认 ddof=0）。含 `NaN` 时结果也是 `NaN`，用 `std(A,'omitnan')`。
:::

#### 6.1.5 排序

```matlab
sort(A)                  % 各列升序
sort(A,'descend')        % 降序
sort(A,dim,mode)         % dim=1 按列，dim=2 按行
[Y,I] = sort(A)          % I 记录排序后元素在原矩阵中的位置（行号）
sortrows(A, col)         % 按指定列对「行」整体排序（表格数据常用）
```


### 6.2 多项式计算

MATLAB 用**降幂排列的系数行向量**表示多项式：`p = [a_n ... a_1 a_0]` 表示 `a_n x^n + ... + a_1 x + a_0`。

::: danger 易错点 · 缺项要补 0
`x^3 + 2x - 5` 要写成 `[1 0 2 -5]`，**缺的 x² 项必须写 0**。少了这一位，整个多项式次数就变了。
:::

#### 6.2.1 四则运算

```matlab
conv(p1, p2)         % 多项式乘法（系数卷积）
[q, r] = deconv(p1, p2)  % 多项式除法：p1 = conv(p2,q) + r
```

#### 6.2.2 导函数

```matlab
polyder(p)           % 多项式 p 的导数系数
polyder(p1,p2)       % 乘积 p1*p2 的导数
[num, den] = polyder(p1,p2)  % 商 p1/p2 的导数（返回分子/分母）
```

#### 6.2.3 求值

```matlab
polyval(p, x)        % 逐元素求值：把 x 的每个元素代入多项式
polyvalm(p, A)       % 矩阵多项式：p(2) 项用 A*A（矩阵乘），常数项用 eye
```

::: danger 易错点 · polyval 与 polyvalm 本质不同
对 p = x²+2x+1 与方阵 A：
- `polyval(p,A)` = `A.^2 + 2*A + 1`（**逐元素**平方）；
- `polyvalm(p,A)` = `A*A + 2*A + I`（**矩阵**乘、常数项为**单位阵**）。

原书例 6-11 专门对比了二者。求「矩阵多项式」必须用 `polyvalm`。
:::

#### 6.2.4 求根

```matlab
roots(p)             % 求多项式全部根（内部构造伴随矩阵求特征值）
poly(r)              % 由根反求多项式系数（首项系数为 1）
```

### 6.3 数据插值

```matlab
Y1 = interp1(X, Y, X1, method)     % 一维插值
Z1 = interp2(X, Y, Z, X1, Y1, method)  % 二维插值
V1 = interpn(...)                  % N 维插值
```

| `method` | 说明 |
| --- | --- |
| `'nearest'` | 最近点，最快，不连续 |
| `'linear'` | 线性（**默认**） |
| `'spline'` | 三次样条，光滑但可能过冲 |
| `'pchip'` | 保形三次 Hermite，单调性保持好，不易过冲 |
| `'cubic'` | 与 `'pchip'` 等价（一维） |

也可用专用函数：`spline(X,Y,X1)` 等价于 `interp1(...,'spline')`，`pchip(X,Y,X1)` 同理。

```matlab
x = 0:0.2:2;  y = sin(x);
xi = 0:0.02:2;
yi = interp1(x, y, xi, 'spline');
plot(x,y,'o', xi,yi,'-')
```

::: danger 易错点 · 别外插、X 要单调
`interp1` 默认对超出 `[min(X),max(X)]` 的查询点返回 `NaN`（可给 `'extrap'` 显式外插，但**外插结果不可靠**）。另外 X 必须**严格单调且无重复**，否则报错。二维插值要求 X、Y 构成规则网格（散点用 `scatteredInterpolant`）。
:::

### 6.4 曲线拟合

插值是「曲线必须过所有数据点」，拟合是「找一条最贴近整体趋势的曲线」，用**最小二乘法**。

```matlab
p = polyfit(x, y, n)      % 用 n 次多项式最小二乘拟合
y1 = polyval(p, x1)       % 用拟合出的系数在新点上求值
```

```matlab
x = 0:0.1:1;
y = [-0.447 1.978 3.28 6.16 7.08 7.34 7.66 9.56 9.48 9.30 11.2];
p = polyfit(x, y, 2);        % 二次拟合
plot(x, y, 'o', x, polyval(p,x), '-'); legend('数据','拟合')
```

::: danger 易错点 · 阶数不是越高越好
n 太大会**过拟合**（曲线完美穿过噪声点，但泛化极差），且高次多项式数值不稳定。一般先看散点图选 2~3 次，必要时用 `polyfit` 的带中心化三输出形式：
```matlab
[p, S, mu] = polyfit(x, y, n);   % mu 为 [mean(x), std(x)]
y1 = polyval(p, x1, S, mu);      % 求值也要传 S、mu
```
`x` 数值跨度大时这个形式能显著改善条件数。
:::


---

## 第7章 数值微分与积分

### 7.1 数值微分

#### 7.1.1 差分与差商

```matlab
diff(X)              % 相邻元素之差（一阶差分），结果比 X 少 1 个元素
diff(X, n)           % n 阶差分
diff(A, n, dim)      % 矩阵按指定维差分
```

近似导数：`f'(x) ≈ (f(x+h) - f(x))/h`（向前差商），更精确可用**中心差商** `(f(x+h)-f(x-h))/(2h)`。

#### 7.1.2 数值微分实现

```matlab
x = 0:0.01:pi;
y = sin(x);
dy = diff(y) ./ diff(x);        % 长度比 x 少 1
plot(x(1:end-1), dy)

% 或者直接给出函数，用中心差商
h = 1e-5;
f = @(x) sin(x);
df = (f(1+h) - f(1-h)) / (2*h);
```


::: danger 易错点 · h 不是越小越精确
h 太小会因浮点相减而**灾难性抵消**，误差反而变大。双精度下 `h ≈ 1e-5 ~ 1e-6`（约 `eps^(1/3)` 量级）较稳妥；需要高精度时用**符号微分**（第 9 章 `diff(syms)`）或复步导数。
:::

### 7.2 数值积分

#### 7.2.1 基本原理

数值积分用**求积公式**近似：把区间分成若干小段，用梯形 / 辛普森等公式累加。MATLAB 提供的函数分两类：
- 给定**被积函数句柄** → 自适应积分（`integral` 等）；
- 给定**离散数据点** → `trapz`。

#### 7.2.2 定积分实现


::: danger 易错点 · integral 要求向量化
`integral` 会**一次传入一个向量** x 来批量求值，所以被积函数里必须写 `x.^2`、`.*`、`./`。写 `x^2` 会报「矩阵维度必须一致」。若函数确实只能接受标量，加 `'ArrayValued', true`（但会慢很多）。
:::

**离散数据积分**：

```matlab
x = 0:0.1:pi;  y = sin(x);
I = trapz(x, y)          % 梯形法，≈ 1.9998
```

#### 7.2.3 多重积分

```matlab
% 例：∫∫ (x+y) dx dy
I = integral2(@(x,y) x+y, 0,1, 0,1)
% 注意：内层积分限可以是函数句柄（变限积分）
I = integral2(@(x,y) x.*y, 0,1, 0, @(x) x)   % y 上限 = x
```

### 7.3 离散傅里叶变换 (DFT)

```matlab
Y = fft(X)           % 一维快速傅里叶变换
X = ifft(Y)          % 逆变换
fft2 / ifft2         % 二维（图像频域）
fftshift(Y)          % 把零频移到频谱中心（画图必备）
```

```matlab
Fs = 1000;  t = 0:1/Fs:1-1/Fs;
x = sin(2*pi*50*t) + 0.5*sin(2*pi*120*t);
Y = fft(x);
P2 = abs(Y/length(x));
P1 = P2(1:floor(length(x)/2)+1);
f = Fs*(0:floor(length(x)/2))/length(x);
plot(f, P1); xlabel('f (Hz)'); ylabel('|P1|')   % 在 50、120 Hz 处出现峰
```

::: danger 易错点 · fft 的三个坑
1. 结果是**双边谱**且未按频率排序，`fftshift` 才把 0 频放中间。
2. 幅度要除以 `N = length(x)`；单边谱只取前 `N/2+1` 点，除直流与 Nyquist 点外幅度要 ×2。
3. `fft` 假设信号**周期延拓**，非整周期截断会**频谱泄漏**，需加窗（`hann`、`hamming`）。
:::

---

## 第8章 MATLAB 方程数值求解

### 8.1 线性方程组求解

对 `A*X = b`：

#### 8.1.1 直接解法

```matlab
x = A\b               % 首选：反斜杠，内部按 A 的结构自动选算法
```


```matlab
[L,U] = lu(A);        % LU 分解（A = L*U，带置换时 [L,U,P] = lu(A)）
R = chol(A);          % Cholesky 分解（A = R'*R，要求对称正定）
[Q,R] = qr(A);        % QR 分解
```

```matlab
A = [1,2,3; 4,5,6; 7,8,0];  b = [1;2;3];
x = A\b;
% 验证残差
norm(A*x - b)
```

#### 8.1.2 迭代解法

大型稀疏方程组常用迭代法（Jacobi、Gauss-Seidel、SOR、共轭梯度）。MATLAB 提供 `pcg`（预条件共轭梯度）、`gmres`、`bicg` 等：

```matlab
x = pcg(A, b, 1e-8, 1000);
```


#### 8.1.3 求通解

```matlab
null(A)          % 齐次方程组 A*x=0 的基础解系（正交规范基）
null(A,'r')      % 有理形式
rref([A b])       % 增广矩阵的行最简形，用于人工分析秩与自由变量
```

### 8.2 非线性方程数值求解

```matlab
% 单变量：fzero 需要「变号区间」或初值
f = @(x) x.^3 - 2*x - 5;
x = fzero(f, 2)               % 从 x=2 附近搜索
x = fzero(f, [1 3])          % 给变号区间更稳妥：f(1)<0, f(3)>0

% 方程组：fsolve（需 Optimization Toolbox）
F = @(x) [x(1)^2 + x(2)^2 - 1;
          x(1) - x(2)];
x = fsolve(F, [0.5; 0.5]);

% 多项式方程
r = roots([1 0 -2 -5]);
```

::: danger 易错点 · fzero 只找一个根
`fzero` 只返回**一个**根，且区间法要求两端函数值**异号**（否则报错）。多根问题要先画图（`fplot`）定位各根区间再逐段求。多项式求全部根用 `roots`。
:::

### 8.3 最优化问题求解

```matlab
% 无约束、单变量、有界区间
[x, fval] = fminbnd(@(x) (x-3).^2, 0, 5)

% 无约束、多变量（单纯形法，无需梯度）
[x, fval] = fminsearch(@(x) (x(1)-1)^2 + (x(2)-2)^2, [0;0])

% 无约束、多变量（梯度法，需 Optimization Toolbox）
[x, fval] = fminunc(@(x) x(1)^2 + x(2)^2, [1;1])

% 线性规划：min f'*x  s.t. A*x<=b, Aeq*x=beq, lb<=x<=ub
[x, fval] = linprog(f, A, b, Aeq, beq, lb, ub)
```

```matlab
options = optimset('Display','iter','TolX',1e-8);   % 原书写法
[x,fval] = fminbnd(f,0,5,options);
```


::: danger 易错点 · 局部最优
`fminsearch` / `fminunc` 找到的是**局部极小值**，结果依赖初值 `x0`。多峰函数要多试几个初值，或用 `ga` / `particleswarm` / `MultiStart` 做全局搜索。
:::

### 8.4 常微分方程初值问题

原书 8.4 介绍了龙格—库塔法原理并手工实现。实际使用直接调用 ODE 套件：

```matlab
% y' = f(t,y), y(t0)=y0
[t, y] = ode45(@(t,y) -2*y + sin(t), [0 10], 1);
plot(t, y)
```

| 求解器 | 适用 | 说明 |
| --- | --- | --- |
| `ode45` | **非刚性，首选** | 四/五阶 Runge-Kutta-Fehlberg，中等精度 |
| `ode23` | 非刚性，低精度/有奇点 | 二/三阶 RK，步长更粗 |
| `ode113` | 非刚性，高精度 | 变阶 Adams-Bashforth-Moulton |
| `ode15s` | **刚性** | 变阶 BDF，刚性问题必用 |
| `ode23s` / `ode23t` / `ode23tb` | 刚性，低精度 | 不同隐式格式 |

```matlab
% 二阶方程 y'' + y = 0 化为一阶方程组，令 z = [y; y']
f = @(t,z) [z(2); -z(1)];
[t, z] = ode45(f, [0 2*pi], [1; 0]);
plot(t, z(:,1))      % → cos(t)
```

::: danger 易错点 · 刚性方程用错求解器
若 `ode45` 跑得极慢或步长小到几乎不动，多半是**刚性问题**（系统中存在量级悬殊的时间尺度），换 `ode15s` 通常立竿见影。另外 ODE 函数签名必须是 `(t,y)` **两个参数**，即使不显含 t 也要写。
:::


---

## 第9章 MATLAB 符号计算

数值计算给近似解，**符号计算给解析解**（精确表达式）。功能由 **Symbolic Math Toolbox** 提供。


### 9.1 符号计算基础

#### 9.1.1 建立符号对象

```matlab
syms x y              % 一次性声明多个符号变量（推荐）
x = sym('x');         % 等价写法
a = sym(1/3);         % 精确有理数 1/3（不是 0.3333）
S = sym('a*x^2 + b*x + c');
```

::: danger 易错点 · sym(1/3) 与 sym('1/3')
`sym(1/3)` 先把 1/3 算成 double（0.3333…）再转符号，会得到近似有理数；要精确值应写 `sym('1/3')` 或 `sym(1)/3`。同理 `sym(pi)` 与 `sym('pi')` 不同。
:::

```matlab
syms x real           % 声明为实数（可让 simplify 得到更简结果）
syms n positive integer
assumptions(x)        % 查看假设
assume(x, 'positive')
```

#### 9.1.2 基本符号运算

```matlab
syms x
f = x^2 + 2*x + 1;
simplify(f)           % 化简
expand((x+1)^3)       % 展开
factor(x^2 - 1)       % 因式分解 → (x-1)*(x+1)
collect(f, x)         % 按 x 合并同类项
numden(f)             % 提取分子分母
subs(f, x, 2)         % 代入 x=2 → 9
vpa(pi, 50)           % 变精度：π 的 50 位有效数字
double(sym(sqrt(2)))  % 转成双精度数值
pretty(f)             % 类数学排版显示
```

::: danger 易错点 · 符号与数值混用
`syms x; y = x/3` 得到精确符号 1/3*x；若写 `y = x*0.3333` 就引入浮点近似。符号推导中尽量用整数、有理数、`sym('pi')`，避免任何 double 常量。
:::

#### 9.1.3 符号运算中变量的确定

未指定自变量时，MATLAB 按 `symvar` 的规则选取：优先 `x`，然后按字母**离 x 最近**的顺序（如 `y`、`z`、`w`…）。显式指定更稳妥：

```matlab
symvar(f)             % 列出表达式中所有符号变量（替代已移除的 findsym）
diff(f, x)            % 明确对 x 求导
```

#### 9.1.4 符号矩阵运算

```matlab
A = sym([1 2; 3 4]);
inv(A), det(A), rank(A), eig(A), A^2, A.'
```

符号矩阵的运算规则与数值矩阵一致，但结果是精确表达式。

### 9.2 符号微积分

```matlab
syms x a
limit(sin(x)/x, x, 0)            % → 1
limit((1+1/n)^n, n, inf)         % → exp(1)
diff(sin(x^2), x)                % → 2*x*cos(x^2)
diff(f, x, 2)                    % 二阶导
int(x^2, x)                      % 不定积分 → x^3/3（不带常数 C）
int(exp(-x^2), x, 0, inf)        % 定积分 → sqrt(pi)/2
int(int(x*y, y, 0, 1), x, 0, 1) % 重积分
```

::: danger 易错点 · 不定积分没有积分常数
`int(f,x)` 返回**一个**原函数，**不写 +C**，需要时自行加上。另外很多初等函数的原函数不存在初等闭式（如 `exp(-x^2)` 的不定积分），MATLAB 会返回 `erf` 等特殊函数或原样返回，这不是错误。
:::

### 9.3 级数

```matlab
syms n x
symsum(1/n^2, n, 1, inf)         % → pi^2/6
symsum(x^n, n, 0, inf)           % → 1/(1-x)（收敛域内）
taylor(exp(x), x, 0, 'Order', 6) % 在 x=0 处展开到 5 阶
taylor(sin(x), x, 'ExpansionPoint', pi/2, 'Order', 5)
```


### 9.4 方程符号求解

```matlab
syms x y
solve(x^2 - 3*x + 2 == 0, x)     % → 1, 2
[x, y] = solve(x + y == 3, x - y == 1, x, y)

syms y(x)
dsolve(diff(y,x) == y, y(0) == 1)  % → exp(x)
```



---

## 第10章 MATLAB 图形对象句柄（低层绘图）

高层绘图（`plot`）之所以简单，是因为它替你创建了一整套**图形对象**并设置好属性。低层绘图就是直接拿到这些对象的**句柄（handle）**去读写属性，控制力更强。

### 10.1 图形对象及其句柄

MATLAB 的图形对象构成一棵**层次树**：

```
Root（根，屏幕）
 └─ Figure（图形窗口）
     └─ Axes（坐标轴）
         ├─ Line（曲线）
         ├─ Surface（曲面）
         ├─ Text（文本）
         ├─ Patch（块）
         └─ Light（光源）
```

每个对象都有唯一句柄，以及一组「属性名—属性值」。

```matlab
h = figure;                 % 新建窗口，返回句柄
h = plot(x, y);             % 返回曲线对象句柄（现代 MATLAB 直接返回对象）
gcf                         % getCurrentFigure：当前图形窗口句柄
gca                         % getCurrentAxes：当前坐标轴句柄
gco                         % getCurrentObject：最近被选中的对象句柄
findobj(gca, 'Type', 'line')% 按属性查找对象
```


### 10.2 图形窗口与坐标轴

```matlab
figure('Name','我的图', 'Color','w', 'Position',[100 100 800 600])
set(gcf, 'Name', '标题')
axes('Position',[0.1 0.1 0.8 0.8])
set(gca, 'XLim',[0 10], 'FontSize',12, 'XGrid','on')
```

常用 Figure 属性：`Name`、`Color`、`Position`、`Visible`、`NumberTitle`、`MenuBar`、`ToolBar`。
常用 Axes 属性：`XLim`/`YLim`/`ZLim`、`XLabel`/`YLabel`/`Title`、`XScale`（`'linear'`/`'log'`）、`FontSize`、`FontName`、`Box`、`GridLineStyle`、`View`、`CameraPosition`。


### 10.3 低层绘图操作

```matlab
% 曲线对象
h = line('XData', x, 'YData', y, 'Color','r', 'LineWidth',2);

% 曲面对象
hs = surface('XData',X, 'YData',Y, 'ZData',Z, 'FaceColor','interp');

% 文本对象
ht = text(0.5, 0.5, '标注', 'FontSize', 14, 'Color','b');

% 块对象（多边形填充）
hp = patch('XData',[0 1 1 0], 'YData',[0 0 1 1], 'FaceColor','g');

% 其他核心对象：rectangle、image、light、uicontrol、uimenu、hgtransform
delete(h)                  % 删除对象
```

### 10.4 光照和材质处理

```matlab
surf(X,Y,Z); shading interp
light('Position',[1 0 1], 'Style','infinite');
lighting gouraud           % 或 flat / phong
material shiny             % 或 dull / metal / [ka kd ks]
camlight headlight
```

::: tip 提示
低层绘图的实际价值在于**精细控制**：多条曲线分别设属性、动态调整视角、做交互式图形、批量改字体。日常出图仍以高层函数为主，需要微调时用 `gca`/句柄补几行即可。
:::

---

## 第11章 MATLAB 图形用户界面设计

原书介绍两条路线：**用 `uicontrol` / `uimenu` 以代码方式搭界面**，以及用 **GUIDE** 可视化设计。

### 11.1 对话框设计（控件）

```matlab
h = uicontrol('Style','pushbutton', 'String','确定', ...
              'Position',[20 20 80 30], 'Callback',@myCallback);

function myCallback(src, event)
    disp('按钮被点击');
end
```

常用控件 `Style`：`pushbutton`（按钮）、`togglebutton`、`radiobutton`、`checkbox`、`edit`（编辑框）、`text`（静态文本）、`slider`、`listbox`、`popupmenu`、`frame`、`axes`。

常用属性：`String`（显示文字）、`Value`（当前值）、`Position`（[左 下 宽 高]）、`Callback`（回调函数句柄）、`Enable`、`Visible`、`Tag`、`UserData`。

::: danger 易错点 · Callback 的签名
回调函数至少接收 `(src, event)` 两个参数（`src` 是触发控件句柄，`event` 是事件数据）。用匿名函数捕获额外数据：`'Callback', @(src,event) myfun(src, data)`。另外回调里改界面要注意**句柄有效性**与 `drawnow`。
:::

### 11.2 菜单设计

```matlab
f = figure;
m = uimenu(f, 'Text','文件');          % 新版属性 Text（旧版 Label）
uimenu(m, 'Text','打开', 'Callback',@openfile);
cm = uicontextmenu;                     % 快捷（右键）菜单
```


### 11.3 可视化 GUI 设计



---

## 第12章 MATLAB Simulink 系统仿真

Simulink 是 MATLAB 下的**动态系统建模与仿真**集成环境，用**框图（模块 + 连线）**描述系统，无需手写微分方程求解代码。


### 12.1 仿真初步

基本流程：**新建模型 → 从库中拖入模块 → 连线 → 设置模块参数与仿真参数 → 运行 → 观察结果（Scope / To Workspace）**。

典型入门模型：`Sine Wave` → `Gain` → `Integrator` → `Scope`，或用 `Transfer Fcn` 描述传递函数。

### 12.2 建立仿真模型

| 类别 | 常用模块 |
| --- | --- |
| 输入源 Sources | `Constant`、`Sine Wave`、`Step`、`Ramp`、`Clock`、`From Workspace` |
| 连续 Continuous | `Integrator`、`Derivative`、`Transfer Fcn`、`State-Space` |
| 数学 Math | `Gain`、`Sum`、`Product`、`Math Function` |
| 输出 Sinks | `Scope`、`To Workspace`、`Display`、`To File` |
| 离散 / 逻辑 | `Unit Delay`、`Discrete Transfer Fcn`、`Switch`、`Relational Operator` |

模块操作：选中、复制、删除、旋转（`Ctrl+R`）、连线（拖动端口）、设置参数（双击）、加标注。

```matlab
add_block('simulink/Sources/Sine Wave','mymodel/Sin')
set_param('mymodel/Gain','Gain','2')
add_line('mymodel','Sin/1','Gain/1')
```

### 12.3 仿真参数与结果分析

```matlab
set_param('mymodel','StopTime','10','Solver','ode45')
simOut = sim('mymodel');
tout = simOut.tout;  yout = simOut.yout;
plot(tout, yout)
```

关键参数：`StartTime` / `StopTime`、求解器（`ode45` 变步长 / `ode15s` 刚性 / `FixedStepDiscrete`）、`MaxStep`、相对与绝对容差。

::: danger 易错点 · 代数环与刚性
模型里若出现**无延迟的反馈环**（代数环），Simulink 会报警告甚至无法求解，需在环中插入 `Unit Delay` 或 `Memory` 模块。含快慢悬殊时间尺度的模型要换 `ode15s` 等刚性求解器。
:::

### 12.4 子系统及其封装

- **子系统 (Subsystem)**：把一组模块框起来，简化顶层图（`Ctrl+G` 创建）。
- **条件执行子系统**：`Enabled Subsystem`、`Triggered Subsystem`、`Function-Call Subsystem`。
- **封装 (Mask)**：给子系统自定义参数对话框、图标与说明，让子系统像内置模块一样使用。

### 12.5 S 函数

S 函数（System Function）用 MATLAB / C / C++ 编写自定义模块，按 `初始化 → 计算导数 → 更新状态 → 计算输出 → 结束` 的**仿真阶段回调**组织。


---

## 第13章 MATLAB 外部程序接口技术

### 13.1 与 Office 混合使用

原书讲 **MATLAB Notebook**（在 Word 里调用 MATLAB）与 **Excel Link**（在 Excel 里调用 MATLAB）。


### 13.2 数据接口

#### 13.2.1 文件操作

```matlab
fid = fopen('data.txt', 'r');       % 'r'读 'w'写 'a'追加
A = fscanf(fid, '%f', [3 inf]);
fprintf(fid, '%8.4f\n', x);
fclose(fid);

[fid, msg] = fopen('data.txt','r');
if fid < 0, error('打开失败: %s', msg); end
```

低级函数：`fread` / `fwrite`（二进制）、`fgetl` / `fgets`（按行）、`feof`、`frewind`、`fseek`、`ftell`。


#### 13.2.2 MAT 文件

```matlab
save('data.mat', 'A', 'B')        % 保存指定变量
S = load('data.mat');             % 载入为结构体（S.A、S.B），更安全
whos('-file','data.mat')          % 不载入也能查看内容
```


### 13.3 与其他语言接口

| 方式 | 说明 |
| --- | --- |
| **MEX 文件** | 用 C/C++/Fortran 写计算密集函数，编译成可被 MATLAB 直接调用的二进制模块（`mex myfun.c`） |
| **MATLAB 引擎** | 在 C/C++/Java/Python 程序里启动 MATLAB、执行命令、交换数据 |
| **MATLAB Coder** | 把 MATLAB 代码生成独立 C/C++ 代码 |
| **MATLAB Compiler** | 打包成独立应用或库 |


### 13.4 关于「17 个实验」

原书实验篇按章节配套 17 个上机实验（见附录 C），从「系统环境与运算基础」到「综合实验」。这类实验的目的都是**把命令行示例亲手敲一遍并观察输出**，建议配合本笔记每章末尾的代码段做。

---

## 第14章 MATLAB 的综合应用

本章是全书知识的综合演练，展示把「数学模型 → MATLAB 实现 → 可视化」串起来的完整思路。

### 14.1 电路分析

**调谐振荡电路**：先由基尔霍夫定律列出微分方程/状态方程，再用 `ode45` 求数值解，或建立传递函数用 `tf` / `step` / `bode`（Control System Toolbox）分析频响。

```matlab
sys = tf([1], [L*C, R*C, 1]);     % 二阶 RLC 传递函数
step(sys);  bode(sys);
```

### 14.2 控制系统分析

**线性反馈控制系统**：用 `tf`、`ss`、`feedback`、`step`、`rlocus`、`margin` 等分析稳定性与动态性能；也可在 Simulink 里搭闭环框图仿真。

### 14.3 分形曲线的绘制

**科赫 (Koch) 曲线**：把线段三等分，中间一段替换成等边三角形的两条边，对每条新线段**递归重复**。

实现要点（对应第 4 章的递归 / 循环 + 第 5 章的 plot）：
```matlab
function koch(p1, p2, n)
    if n == 0
        plot([p1(1) p2(1)], [p1(2) p2(2)]); hold on
    else
        d = (p2 - p1)/3;
        a = p1 + d;
        b = p1 + 2*d;
        % 中点向外旋转 60° 得到顶点
        R = [cos(pi/3) -sin(pi/3); sin(pi/3) cos(pi/3)];
        c = a + R*d;
        koch(p1, a, n-1); koch(a, c, n-1);
        koch(c, b, n-1);  koch(b, p2, n-1);
    end
    axis equal; axis off
end
```

::: danger 易错点 · 递归要有终止条件
递归函数**必须有 `n == 0` 之类的基线分支**，否则无限递归直到栈溢出。科赫曲线层数 n=5 时线段数是 4⁵=1024，n 再大绘制会明显变慢。
:::

### 14.4 最优化问题求解

**证券投资组合**（在给定收益下最小化风险，即均值—方差模型）与**生产决策问题**（线性规划），分别用 `fmincon` / `quadprog` 与 `linprog` 求解。核心是先把实际问题**翻译成标准形式**（目标函数、不等式/等式约束、变量上下界），再选对应求解器。

### 14.5 工程结构分析

**静不定问题**与**直梁自由振动频率**：本质是大型线性方程组 `K*u = F` 与广义特征值问题 `K*phi = lambda*M*phi`，用第 3、8 章的矩阵运算、`eig`、稀疏矩阵（`sparse`）求解。

::: tip 提示
第 14 章的价值不在具体公式，而在**建模套路**：先把物理问题写成矩阵/方程，再调用第 2-9 章的工具求解，最后用第 5 章绘图呈现。学完前面各章，本章的例子应能读懂思路。
:::

---

## 附录 A 全书易错点速查

| # | 易错点 | 正确做法 |
| --- | --- | --- |
| 1 | `*` 与 `.*` 混用 | 逐元素运算一律加点；向量化函数内部也要 `.*` `.^` `./` |
| 2 | 统计函数默认按列 | 按行要加 `dim=2`：`mean(A,2)`、`max(A,[],2)` |
| 3 | 线性索引按列优先 | `A(3)` 是第 1 列第 3 行；`reshape` 也按列 |
| 4 | `length(A)` 是最大维长度 | 元素总数用 `numel(A)`，行数用 `size(A,1)` |
| 5 | `i`/`j` 被覆盖 | 复数写 `1i`、`7+5i`，别拿 i 当循环变量 |
| 6 | `A'` 与 `A.'` | 复数矩阵 `A'` 是共轭转置，纯转置用 `A.'` |
| 7 | 用 `inv(A)*b` 解方程组 | 一律用 `x = A\b` |
| 8 | `polyval` / `polyvalm` 混淆 | 矩阵多项式用 `polyvalm`（常数项是单位阵） |
| 9 | 多项式缺项忘补 0 | `x³+2x-5` → `[1 0 2 -5]` |
| 10 | 浮点数用 `==` 比较 | 用容差 `abs(a-b) < 1e-12`；`isnan` 判 NaN |
| 11 | `if` 条件用数组 | 明确写 `all(...)` / `any(...)` |
| 12 | `elseif` 写成 `else if` | `elseif` 是一个词，不多加 `end` |
| 13 | `switch` 想「贯穿」 | MATLAB 只执行第一个匹配分支，用 `{...}` 并列多值 |
| 14 | 循环里扩展数组 | 先 `zeros` 预分配，或向量化 |
| 15 | 遮蔽内置函数名 | 别用 `sum`/`mean`/`i`/`pi` 作变量名 |
| 16 | `integral` / `fplot` 里没向量化 | 函数句柄内必须 `x.^2`、`.*` |
| 17 | `strcmp(s1,s2,n)` | 正确是 `strncmp(s1,s2,n)` |
| 18 | 符号计算里混入 double | 用 `sym('1/3')`、`syms`，别写 `0.3333` |
| 19 | `solve` 写 `=` 而非 `==` | 符号等式必须用 `==` |
| 20 | `quad`/`ezplot`/`hist`/`xlsread`/`GUIDE` | 见附录 B 的替换表 |

---

## 附录 B 常用函数速查表

### B.1 原书过时函数 → 现代替代

| 已废弃/不推荐 | 现代替代 | 出现章节 |
| --- | --- | --- |
| `quad` / `quadl` / `dblquad` / `triplequad` | `integral` / `integral2` / `integral3` | 7.2 |
| `ezplot` / `ezplot3` | `fplot` / `fimplicit` / `fplot3` | 5.1、5.4 |
| `ezmesh` / `ezsurf` / `ezcontour` / `ezpolar` | `fmesh` / `fsurf` / `fcontour` / `polarplot` | 5.3、5.4 |
| `hist` / `histc` | `histogram` / `histcounts` | 5.2 |
| `polar` | `polarplot` | 5.2 |
| `inline` | 匿名函数 `@(x) ...` | 4.4 |
| `setstr` | `char` | 2.6 |
| `findstr` | `strfind`（注意参数顺序） | 2.6 |
| `strcmp(s1,s2,n)`（笔误） | `strncmp(s1,s2,n)` | 2.6 |
| `findsym` | `symvar` | 9.1 |
| `lasterr` | `MException` / `ME.message` | 4.2 |
| `xlsread` / `xlswrite` | `readtable` / `writetable` / `readmatrix` | 13 |
| `optimset` | `optimoptions` | 8.3 |
| `bsxfun`（不再必需） | 隐式扩展（R2016b 起） | 2.5 |
| `GUIDE` / `guide` | `appdesigner` + `uifigure` | 11 |
| MATLAB Notebook / Excel Link | Live Script / `readtable` 系列 | 13 |
| `uimenu(...,'Label',...)` | `uimenu(...,'Text',...)` | 11 |
| `taylor(f,n,a)` 位置参数 | `taylor(f,x,'ExpansionPoint',a,'Order',n)` | 9.3 |
| `solve('字符串')` | `syms` + `==` + 显式变量 | 9.4 |
| `eval` / 动态变量名 | 函数句柄、动态字段名、`cell`/`struct` | 2.6、4.1 |

### B.2 高频函数按用途速查

| 用途 | 函数 |
| --- | --- |
| 建矩阵 | `zeros` `ones` `eye` `rand` `randn` `randi` `randperm` `linspace` `logspace` `meshgrid` |
| 特殊矩阵 | `magic` `vander` `hilb` `invhilb` `toeplitz` `compan` `pascal` |
| 矩阵信息 | `size` `length` `ndims` `numel` `isempty` `class` `whos` |
| 矩阵变换 | `diag` `triu` `tril` `rot90` `fliplr` `flipud` `reshape` `A'` `A.'` |
| 矩阵求值 | `det` `rank` `trace` `norm` `cond` `rcond` `inv` `pinv` `eig` `svd` |
| 索引转换 | `sub2ind` `ind2sub` `find` `end` `A(:)` |
| 稀疏矩阵 | `sparse` `full` `speye` `spdiags` `nnz` `spy` |
| 数学函数 | `sin`/`sind` `exp` `log` `sqrt` `abs` `sign` `fix` `floor` `ceil` `round` `rem` `mod` `gcd` `lcm` |
| 矩阵函数 | `sqrtm` `logm` `expm` `funm` |
| 统计 | `max` `min` `sum` `prod` `mean` `median` `std` `var` `cov` `corrcoef` `cumsum` `cumprod` `sort` `sortrows` |
| 多项式 | `conv` `deconv` `polyder` `polyval` `polyvalm` `roots` `poly` `polyfit` |
| 插值拟合 | `interp1` `interp2` `interpn` `spline` `pchip` `polyfit` |
| 微积分 | `diff` `gradient` `trapz` `integral` `integral2` `integral3` `quadgk` `fft` `ifft` `fftshift` |
| 方程求解 | `A\b` `lu` `chol` `qr` `null` `rref` `fzero` `fsolve` `roots` `pcg` `gmres` |
| 优化 | `fminbnd` `fminsearch` `fminunc` `fmincon` `linprog` `quadprog` `ga` |
| ODE | `ode45` `ode23` `ode113` `ode15s` `odeset` |
| 符号 | `syms` `sym` `symvar` `simplify` `expand` `factor` `collect` `subs` `vpa` `limit` `diff` `int` `taylor` `symsum` `solve` `dsolve` `matlabFunction` |
| 绘图 | `plot` `fplot` `fimplicit` `plot3` `surf` `mesh` `contour` `subplot` `tiledlayout` `hold` `grid` `axis` `legend` `title` `xlabel` `ylabel` `view` `colormap` `colorbar` |
| 字符串/数据 | `num2str` `str2double` `sprintf` `fprintf` `strcmp` `strncmp` `strfind` `readtable` `writetable` `readmatrix` `load` `save` |
| 程序结构 | `if`/`elseif`/`else`/`end` `switch`/`case`/`otherwise` `try`/`catch` `for`/`while` `break` `continue` `function` `nargin` `nargout` `varargin` |

---

## 附录 C 原书 17 个上机实验索引

| 实验 | 主题 | 对应章节 |
| --- | --- | --- |
| 实验 1 | MATLAB 系统环境与运算基础 | 第 1、2 章 |
| 实验 2 | MATLAB 矩阵处理 | 第 3 章 |
| 实验 3 | 顺序结构程序设计 | 第 4 章 |
| 实验 4 | 选择结构程序设计 | 第 4 章 |
| 实验 5 | 循环结构程序设计 | 第 4 章 |
| 实验 6 | 函数文件 | 第 4 章 |
| 实验 7 | 绘图操作 | 第 5 章 |
| 实验 8 | 数据分析与多项式计算 | 第 6 章 |
| 实验 9 | 数值微分与积分 | 第 7 章 |
| 实验 10 | 方程数值求解 | 第 8 章 |
| 实验 11 | 符号计算对象与符号微积分 | 第 9 章 |
| 实验 12 | 级数与方程符号求解 | 第 9 章 |
| 实验 13 | 低层绘图操作 | 第 10 章 |
| 实验 14 | 对话框与菜单设计 | 第 11 章 |
| 实验 15 | Simulink 的应用 | 第 12 章 |
| 实验 16 | 外部程序接口 | 第 13 章 |
| 实验 17 | 综合实验 | 第 14 章 |

::: tip 学习建议
实验 1~6 是**打地基**（矩阵、索引、流程控制、函数文件），务必逐题手敲；实验 7~12 是**工具运用**（绘图、统计、积分、求解、符号），重点体会「向量化 + 函数句柄」；实验 13~17 属于**拓展了解**，按兴趣选做即可。每个实验都建议配合本笔记对应章节的代码示例对照阅读。
:::




