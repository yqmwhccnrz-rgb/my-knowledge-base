---
summary: "Java 程序设计 详细笔记，全书 12 章 + 8 个进阶专题，覆盖 Java 平台与开发环境、基本程序结构、对象与类、继承、接口与 lambda、异常与日志、泛型、集合框架、GUI 事件、Swing、并发；并补充 JVM 内存模型与 GC、枚举与注解、java.time、Stream API、NIO.2 文件 I/O、equals/hashCode 契约、Java 8→21 新特性、工程常用工具等进阶知识。含 10 张自绘图（集合框架、异常体系、线程状态、JVM 内存、泛型擦除与 PECS、HashMap 底层、Stream 流水线、I/O 体系、线程池、对象契约）、大量可编译代码示例、工作示例、对比表、公式速查与易错点。"
---

# Java 程序设计笔记

::: info 笔记概要
- **所属课程**：Java 程序设计（计算机类 / 软件工程等专业核心基础课，及软件开发方向通用语言课）。
- **核心内容**：Java 以"一次编写、到处运行"的 JVM 平台 + 庞大类库著称。笔记按"语言基础 → 面向对象（类/继承/接口/泛型）→ 核心类库（集合/异常/IO/并发）→ 图形界面"主线展开，覆盖第 1–12 章；并在文末补充教材相对单薄、但工程必备的进阶主题（JVM 内存与 GC、枚举/注解、java.time、Stream、NIO.2、对象契约）。
- **学习建议**：Java 是"强类型 + 面向对象 + 自动内存管理"的语言，学习要抓住三条线——① 语法（类型/运算符/控制流/字符串）是否熟练；② 面向对象三要素（封装/继承/多态）与接口、泛型如何落地；③ 类库（集合、异常、并发、IO）的 API 与适用场景。本笔记在每个关键知识点都配了可运行的代码示例，并补充了教材未深入但易考易错的点（如自动装箱缓存范围、HashMap 底层、equals/hashCode 契约、PECS 通配符、线程安全集合等）。
- **本版说明**：这是**详细版**——每章在原有精要基础上增设子节，补齐可编译代码、工作示例（含运行结果）、对比表和易错辨析；10 张自绘图均已逐格核对，修正了集合框架体系、异常层次、线程状态转换箭头等图示错误，并新增泛型擦除、HashMap 结构、Stream 流水线、I/O 体系、线程池参数、对象契约等示意图。
:::

## 全书目录

| 章 | 主题 | 核心考点 | 重要度 |
| --- | --- | --- | --- |
| 1 | Java 程序设计概述 | Java 平台特性、白皮书 11 术语、常见误解 | ★ 客观题 |
| 2 | Java 程序设计环境 | JDK 安装、JShell、IDE、jar | ★ |
| 3 | 基本程序设计结构 | 类型/变量/运算符/字符串/数组/控制流 | ★★★ |
| 4 | 对象与类 | 类定义、构造器、static、包、封装、jar | ★★★ |
| 5 | 继承 | 子类/覆盖/多态/Object/包装类/反射 | ★★★ |
| 6 | 接口、lambda 与内部类 | 接口默认方法、函数式接口、lambda、内部类、代理 | ★★★ |
| 7 | 异常、断言、日志 | 异常分类、try-catch-finally、try-with-resources、断言、日志 | ★★★ |
| 8 | 泛型程序设计 | 泛型类/方法、类型擦除、通配符 PECS、局限性 | ★★★ |
| 9 | 集合框架 | List/Set/Queue/Map 实现、迭代器、视图、算法 | ★★★ |
| 10 | 图形用户界面程序设计 | Swing 窗体、2D 图形、事件处理 | ★★ 了解 |
| 11 | Swing 用户界面组件 | 布局、文本/选择组件、菜单、对话框 | ★★ 了解 |
| 12 | 并发 | 线程状态、同步、锁、线程安全集合、线程池、Future | ★★★ |
| 补 1–6 | 进阶与补充 | JVM 内存/GC、枚举/注解、java.time、Stream、NIO.2、equals/hashCode 契约 | ★★★ |
| 补 7–8 | 新特性与工程工具 | Java 8→21 常用新特性、常用类库与构建/测试工具 | ★★ |
| 附 A / B | 速查 | 结论公式速查表、全书易错点清单 | 复习用 |

---

## 第 1 章 Java 程序设计概述

### 1.1 Java 程序设计平台（★）
Java 不只是一种语言，更是一个**平台**：
- **Java 虚拟机（JVM）**：字节码（`.class`）由 JVM 解释/编译执行，实现"一次编写、到处运行（WORA）"。
- **庞大的类库（JDK）**：网络、图形、数据库、并发等开箱即用。
- **自动垃圾回收（GC）**：程序员无需手动释放内存。

::: tip Java 与 C++ 的主要区别
Java 去除了 C++ 中易错、少用的特性：无指针运算、无头文件、无结构/联合、无操作符重载、无虚基类、无多重继承（改用接口）；内存由 GC 自动管理。但保留了 `switch` 等语法。Java 语法可视为"C++ 的一个干净子集 + 面向对象 + 托管运行时"。
:::

### 1.2 白皮书 11 个关键术语（★★）
简单性、面向对象、分布式、健壮性、安全性、体系结构中立、可移植性、解释型、高性能、多线程、动态性。
- **体系结构中立 / 可移植**：字节码与平台无关，数据类型长度固定（`int` 永远 32 位，不随 OS 改变）。
- **多线程**：Java 标准库直接支持（而非依赖 OS 线程 API）。
- **动态性**：运行时可装载类，适合从网络动态加载。

### 1.3 Java 发展简史与常见误解（★）
- Java 1996 年发布，最初由 Sun 公司开发；现由 Oracle 维护。版本节奏：Java 8（LTS，2014）之后改为约每 6 个月一个特性版，LTS 版（8/11/17/21…）才是长期支持版。
- **常见误解纠正**："Java 很慢"——现代 JVM 有 JIT 即时编译与分层编译，性能已接近原生；"Java 只能写 Web"——它覆盖桌面、移动（Android 早期）、大数据、后端、嵌入式等。

### 1.4 JVM / JRE / JDK 三者关系（★★★）

| 概念 | 全称 | 包含什么 | 作用 |
| --- | --- | --- | --- |
| JVM | Java Virtual Machine | 执行引擎、运行时数据区、类加载器 | 把**字节码**翻译成平台机器码并执行，屏蔽 OS/CPU 差异 |
| JRE | Java Runtime Environment | JVM + 核心类库（`java.lang`、`java.util`…） | 只够**运行**已编译的程序 |
| JDK | Java Development Kit | JRE + `javac`、`jar`、`javadoc`、`jshell`、`jstack` 等工具 | 开发、编译、调试、打包 |

包含关系：**JDK ⊃ JRE ⊃ JVM**。JDK 11 起不再单独提供公共 JRE，部署可用 `jlink` 裁剪出最小运行时镜像。

::: danger 易错 · "一次编写，到处运行"的准确含义
跨平台的不是 JVM 本身，而是**字节码**：同一份 `.class` 可以在 Windows / macOS / Linux 各自的 JVM 上运行，但每个平台的 JVM 实现是不同的本地程序。另外 `javac` 编译产物是**字节码而非机器码**，所以 Java 属于"编译 + 解释 + JIT 混合"执行：热点代码会被 JIT 编译成本地机器码缓存复用（Code Cache）。
:::

### 1.5 白皮书 11 个术语逐条速查（★★）

| 术语 | 含义 | 具体体现 |
| --- | --- | --- |
| 简单性 | 去除 C++ 复杂易错特性 | 无指针运算、无头文件、无多重继承、无操作符重载、无手动内存释放 |
| 面向对象 | 以类与接口组织程序 | 除基本类型外一切皆对象；单继承 + 多接口 |
| 分布式 | 网络能力内置于类库 | `java.net`、RMI、HTTP、序列化 |
| 健壮性 | 尽早发现错误、避免崩溃 | 强类型检查、异常机制、GC 消除悬垂指针/内存泄漏的常见来源 |
| 安全性 | 运行时隔离与校验 | 字节码验证器、类加载器命名空间、安全管理器（已淡出）、无指针越界写 |
| 体系结构中立 | 字节码与具体硬件无关 | `.class` 格式统一，`int` 恒 32 位，不随 OS 变化 |
| 可移植性 | 数据类型与 API 有明确规范 | 基本类型长度固定、`String` 统一 UTF-16、标准库行为一致 |
| 解释型 | 字节码由 JVM 解释执行 | 配合 JIT 后性能接近编译型语言 |
| 高性能 | 热点即时编译优化 | 分层编译、内联、逃逸分析、自适应优化 |
| 多线程 | 语言级并发支持 | `Thread`、`synchronized`、`java.util.concurrent`，而非依赖 OS API |
| 动态性 | 运行时装载与链接类 | 反射、动态代理、类加载器、热部署 |

---

## 第 2 章 Java 程序设计环境

### 2.1 JDK 安装与配置（★）
- **JDK（Java Development Kit）** 包含 JRE + 编译器 `javac` + 工具。JRE 仅能运行。
- `JAVA_HOME` 指向 JDK 目录；`PATH` 加入 `%JAVA_HOME%/bin`（Windows）或 `$JAVA_HOME/bin`（macOS/Linux）。
- 验证：`javac -version`、`java -version`。

### 2.2 第一个程序与编译运行（★★）
```java
public class HelloWorld {
    public static void main(String[] args) {
        System.out.println("Hello, Java");
    }
}
```
- `javac HelloWorld.java` → 生成 `HelloWorld.class`（字节码）；`java HelloWorld` → 运行。
- 一个 `.java` 文件中**最多只有一个 public 类**，且文件名须与 public 类名一致；`main` 必须是 `public static void`，参数为 `String[] args`。

### 2.3 JShell（★）
JDK 9+ 提供 `jshell` 交互式 REPL，可逐行执行 Java 表达式，省去写 `main` 与类声明的样板，适合快速验证语法与 API。

### 2.4 集成开发环境与 jar（★★）
- 常用 IDE：IntelliJ IDEA、Eclipse、VS Code（配合插件）。
- **jar**：Java 归档文件（`jar cvf app.jar *.class`），本质是基于 ZIP 的包格式；`MANIFEST.MF` 可指定主类 `Main-Class:`。

### 2.5 从源码到运行的完整链路（★★）

```text
HelloWorld.java
   │  javac（编译：词法/语法分析、类型检查、生成字节码）
   ▼
HelloWorld.class（含常量池、字段表、方法表、属性表；不是机器码）
   │  类加载器 ClassLoader：加载 → 链接(验证 / 准备 / 解析) → 初始化(执行 <clinit>)
   ▼
JVM 运行时数据区（方法区存类元数据、堆存对象、栈存栈帧）
   │  执行引擎：解释器逐条执行 + JIT 把热点方法编译为本地机器码
   ▼
操作系统 / CPU 执行
```

- **双亲委派模型**：自定义加载器 → Application → Platform → Bootstrap，收到加载请求先委托父加载器，父加载不了才自己尝试。作用是**保证 `java.lang.*` 等核心类不被用户同名类冒名替换**。`Class.forName`、`ClassLoader.loadClass` 会触发加载（是否初始化取决于参数）。
- 常用命令：`javac -encoding UTF-8 -d out src/*.java`（编译到 out）、`java -cp out com.example.Main`（按类路径运行）、`javap -c -p Main`（反汇编字节码，理解 `i++`/装箱/桥方法时极有用）、`jar tf app.jar`（列出归档内容）。

### 2.6 常见环境错误对照表（★★）

| 现象 / 报错 | 常见原因 | 处理 |
| --- | --- | --- |
| `错误: 找不到或无法加载主类 X` | `-cp` 没包含 class 输出目录；写了全限定名却没对应目录；类名大小写不符 | 检查 `java -cp out com.example.Main` 的包路径与目录一致 |
| `类 X 是公共的，应在名为 X.java 的文件中声明` | public 类名与文件名不一致 | 改文件名或改类名 |
| `UnsupportedClassVersionError` | 用低版本 JVM 运行高版本 `javac` 编译的 class | 统一 JDK 版本，或用 `javac --release 11` 指定目标版本 |
| `javac 不是内部或外部命令` | `PATH` 未包含 `$JAVA_HOME/bin` | 配置 `JAVA_HOME` 并把 `bin` 加入 `PATH` |
| 中文输出乱码 | 源文件编码与编译时 `-encoding` 不一致，或终端编码不同 | 统一 UTF-8，编译加 `-encoding UTF-8` |

---

## 第 3 章 Java 的基本程序设计结构

### 3.1 注释（★）
三种：`// 单行`、`/* 多行 */`、`/** 文档注释（可由 javadoc 生成 API 文档）*/`。

### 3.2 数据类型（★★★）
Java 是**强类型**语言，8 种基本类型：

| 类别 | 类型 | 位数 / 范围 |
| --- | --- | --- |
| 整型 | `byte` | 8 位，-128 ~ 127 |
| | `short` | 16 位 |
| | `int` | 32 位（最常用） |
| | `long` | 64 位，字面量加 `L`（如 `1L`） |
| 浮点 | `float` | 32 位，字面量加 `F` |
| | `double` | 64 位（默认） |
| 字符 | `char` | 16 位 UTF-16 码元 |
| 布尔 | `boolean` | `true` / `false`（**不是** 0/1，不能与整数互转） |

::: danger 易错 · 类型
- **不能用 `0` 代替 `false`**：`if (x = 0)` 在 C 中合法，在 Java 中编译报错（赋值结果是 int，不能用于布尔上下文）。
- 浮点数有精度误差，**禁止用 `==` 比较两个 double 是否相等**（应用误差范围 `Math.abs(a-b) < 1e-9`）；金额等货币计算用 `BigDecimal`。
- 整数字面量默认 `int`，`10000000000` 超过 int 范围须加 `L`，否则编译期溢出错误。
:::

### 3.3 变量、常量与运算符（★★★）
- 变量须先声明后使用；`final` 修饰常量（惯例全大写 `MAX_SIZE`）。
- 数学函数：`Math.sqrt`、`Math.pow`、`Math.abs`；常量 `Math.PI`、`Math.E`。
- **数值类型转换**：自动提升（小→大），强制转换需 `(type)` 且可能丢失信息。
- **严格浮点**：`strictfp`（了解即可，现代 JVM 已默认严格）。

### 3.4 字符串（★★★）
`String` 是**不可变（immutable）**对象：一旦创建内容不可改，所有"修改"都返回新对象。

```java
String s1 = "abc";
String s2 = "abc";
String s3 = new String("abc");
System.out.println(s1 == s2);      // true  —— 字符串常量池复用
System.out.println(s1 == s3);      // false —— new 强制新建对象
System.out.println(s1.equals(s3)); // true  —— equals 比较内容
```

- **`==` 比较引用地址，`equals` 比较内容**（字符串、包装类、大多数对象都应使用 `equals`）。
- `substring`、`concat`、`replace`、`toUpperCase` 等均返回新 `String`。
- **码点与代码单元**：`String.length()` 返回 UTF-16 代码单元数，含增补字符（emoji）时与"字符数"可能不同；遍历用 `codePoints()` 更稳妥。
- **构建可变字符串用 `StringBuilder`/`StringBuffer`**（后者线程安全），避免循环里反复 `+` 拼接产生大量中间对象。

::: tip 字符串常量池
字面量 `""` 在编译期入池，运行时相同字面量复用同一对象（`s1==s2` 为 true）。`new String("abc")` 一定在堆上新建对象，可用 `s3.intern()` 尝试入池并返回池中引用。
:::

### 3.5 输入与输出（★★）
```java
Scanner in = new Scanner(System.in);
String name = in.nextLine();
int n = in.nextInt();
System.out.printf("%.2f%n", 3.14159);   // 格式化输出
```
- 文件读取：`Scanner in2 = new Scanner(Path.of("a.txt"));` 或 `Files.readAllLines(Path.of("a.txt"))`（详见补 5）。
- `Scanner` 的 `nextInt()` 后紧接 `nextLine()` 会读到残留换行，需先多调用一次 `nextLine()` 消耗掉；`Scanner` 也实现了 `AutoCloseable`，用完应关闭。

### 3.6 控制流程（★★★）
`if / switch / for / while / do-while`，以及 `break / continue`。
- `switch` 支持 `String`、`enum`、整数；Java 12+ 提供 **switch 表达式**（`->` 与 `yield`），避免贯穿（fall-through）错误：
```java
int days = switch (month) {
    case 1,3,5,7,8,10,12 -> 31;
    case 2 -> 28;
    default -> 30;
};
```
- `for each`：`for (String s : list)` 遍历任何实现 `Iterable` 的集合/数组。
- **块作用域**：内层块不能重复声明外层块已有的同名变量（与 C++ 不同）。

### 3.7 大数与数组（★★）
- `BigInteger` / `BigDecimal`：任意精度，加减用 `.add/.multiply` 而非 `+/*`。
- 数组：声明 `int[] a = new int[10];`，长度 `a.length`；`Arrays.toString(a)` 打印；多维数组本质是"数组的数组"。
```java
int[] a = {1, 2, 3};
for (int x : a) System.out.println(x);
```

### 3.8 深挖 · 类型、运算符与字符串（★★★）

#### 3.8.1 基本类型完整速查

| 类型 | 位数 | 默认值 | 包装类 | 字面量写法 | 典型范围 / 说明 |
| --- | --- | --- | --- | --- | --- |
| `byte` | 8 | 0 | `Byte` | `(byte) 127` | −128 ~ 127 |
| `short` | 16 | 0 | `Short` | `(short) 32767` | −32768 ~ 32767 |
| `int` | 32 | 0 | `Integer` | `123`、`0b1010`、`0xFF`、`1_000_000` | ±2³¹ |
| `long` | 64 | 0L | `Long` | `123L` | ±2⁶³ |
| `float` | 32 | 0.0f | `Float` | `3.14F` | 约 6~7 位有效数字 |
| `double` | 64 | 0.0 | `Double` | `3.14`、`1e-3` | 约 15 位有效数字（默认） |
| `char` | 16 | `\u0000` | `Character` | `'A'`、`'\u4e2d'` | UTF-16 码元，可当无符号整数参与运算 |
| `boolean` | — | false | `Boolean` | `true` / `false` | **不能与整数互转** |

> 局部变量**没有默认值**，未初始化就使用会编译报错；只有字段（实例/静态）和数组元素才有上表默认值。JDK 10+ 可用 `var x = 1;` 由编译器推断局部变量类型，但 `var` 不能用于字段、方法参数、返回值，也不能 `var x = null;`。

#### 3.8.2 数值转换与表达式类型提升

**自动提升顺序**：`byte → short → int → long → float → double`（`char` 先转 `int`）。

```java
byte  b = 1;
// b = b + 1;              // 编译错：b+1 结果是 int，不能直接赋回 byte
b += 1;                    // 编译通过：复合赋值自带隐式强制转换
int  i = 'A' + 1;          // 66，char 提升为 int
double d = 1 / 2;          // 0.0  —— 整数除法先算完再转 double（易错！）
double e = 1 / 2.0;        // 0.5
long   big = 1_000_000_000L * 10;   // 10000000000，若漏掉 L 会先 int 溢出
```

::: danger 易错 · 精度与溢出
`long → float`、`int → float` 属于**可能丢失精度**的隐式转换（float 尾数只有 24 位），但编译器不报错；反向一律需要强制转换。`Math.round`、`Math.floor`、`Math.ceil` 的返回类型也要注意（`round(float)` 返回 `int`，`round(double)` 返回 `long`）。
:::

#### 3.8.3 运算符优先级与常见陷阱

| 优先级（高→低，节选） | 运算符 |
| --- | --- |
| 1 | `()` `[]` `.` |
| 2 | `!` `~` `++` `--` `(type)new` |
| 3 | `*` `/` `%` |
| 4 | `+` `-` |
| 5 | `<<` `>>` `>>>` |
| 6 | `<` `>` `<=` `>=` `instanceof` |
| 7 | `==` `!=` |
| 8 | `&` → `^` → `\|`（按位） |
| 9 | `&&` → `\|\|`（逻辑，**短路**） |
| 10 | `? :` |
| 11 | `=` `+=` `-=` …（右结合） |

- `&` / `|` 作用于布尔时**不短路**（两边都求值），`&&` / `||` 短路；`^` 是异或。
- `>>` 算术右移（保留符号位，负数补 1），`>>>` 逻辑右移（补 0）；对 `int` 移位次数实际取 `n & 31`。
- `i++` 与 `++i` 在单独成句时等价，在表达式中前者先取值后自增。

#### 3.8.4 String 常用 API 与拼接真相

| 方法 | 作用 | 备注 |
| --- | --- | --- |
| `length()` / `isEmpty()` | UTF-16 码元数 / 判空 | emoji 等增补字符占 2 个码元 |
| `charAt(i)` / `codePoints()` | 取码元 / 按码点遍历 | 处理 emoji 用 `codePointCount` |
| `substring(a,b)` | 取 `[a,b)` 子串 | 左闭右开 |
| `indexOf` / `contains` / `startsWith` | 查找 | 找不到返回 −1 |
| `equals` / `equalsIgnoreCase` / `compareTo` | 比较 | 千万别用 `==` |
| `trim` / `strip` | 去空白 | `strip` 支持 Unicode 空白（JDK 11+） |
| `split(regex)` / `join` / `replace` | 切分 / 连接 / 替换 | `split` 参数是**正则**，`.` `\|` 要转义 |
| `format` / `formatted` | 格式化 | `String.format("%s-%02d", "a", 7)` |
| `intern()` | 返回常量池中的引用 | 谨慎使用，JDK 7 后池在堆中 |

```java
String s = "Java";
s += "17";               // 编译期常量拼接会折叠；但循环里 += 每轮都新建 StringBuilder
StringBuilder sb = new StringBuilder(32);   // 预估容量，减少扩容
for (int k = 0; k < 100; k++) sb.append(k); // 正确做法
String r = sb.toString();

String x = "ab"; String y = "a" + "b";       // 编译期折叠，x == y 为 true
String z = new String("ab").intern();        // x == z 为 true
```

::: tip 为什么 String 设计成不可变
① 常量池复用节省内存；② 天然线程安全；③ 哈希码可缓存，作为 `HashMap` 键高效可靠；④ 安全性（类名、路径、URL 等参数不会被中途篡改）。代价是频繁修改要换 `StringBuilder`/`StringBuffer`。
:::

#### 3.8.5 格式化输出速查

```java
System.out.printf("%s | %d | %05d | %.2f | %,.2f | %tF %<tT%n",
                  "合计", 42, 42, 3.14159, 1234567.89, java.time.LocalDateTime.now());
// 输出形如：合计 | 42 | 00042 | 3.14 | 1,234,567.89 | 2026-11-13 17:11:05
```

| 占位符 | 含义 | 占位符 | 含义 |
| --- | --- | --- | --- |
| `%d` | 十进制整数 | `%s` | 字符串（调 `toString`） |
| `%f` | 浮点（`%.2f` 保留两位） | `%x` / `%o` | 十六进制 / 八进制 |
| `%n` | 平台换行符 | `%tF` / `%tT` | 日期 `YYYY-MM-DD` / 时间 `HH:mm:ss` |
| `%05d` | 宽度 5、前补 0 | `%,.2f` | 千分位分隔 |

#### 3.8.6 数组与精确计算工作示例

```java
import java.math.BigDecimal;
import java.util.Arrays;

int[] a = {3, 1, 2};
Arrays.sort(a);                              // [1, 2, 3]
System.out.println(Arrays.toString(a));      // [1, 2, 3]
int[] copy = Arrays.copyOf(a, a.length + 1); // 扩容式拷贝，末尾补 0
System.out.println(Arrays.binarySearch(a, 2)); // 1（须先排序）

System.out.println(0.1 + 0.2);              // 0.30000000000000004（二进制浮点误差）
BigDecimal p = new BigDecimal("0.1").add(new BigDecimal("0.2"));
System.out.println(p);                       // 0.3  —— 务必用字符串构造
```

> `BigDecimal` 必须用 `new BigDecimal("0.1")` 或 `BigDecimal.valueOf(0.1)`，写成 `new BigDecimal(0.1)` 会把 double 的误差一起带进来。比较小数值用 `compareTo`（`equals` 还会比较标度：`0.30.equals(0.3)` 为 false）。

---

## 第 4 章 对象与类

### 4.1 面向对象概述（★★）
OOP 三要素：**封装（数据私有 + 访问器/更改器）、继承（复用与扩展）、多态（同一接口不同实现）**。类间关系：依赖（use-a）、聚合（has-a）、继承（is-a）。

### 4.2 类的定义与对象（★★★）
```java
public class Employee {
    private String name;        // 封装：字段私有
    private double salary;
    private final int id;       // final 实例字段，构造后不可变

    public Employee(String name, double salary, int id) {
        this.name = name;       // this 区分形参与字段
        this.salary = salary;
        this.id = id;
    }
    public String getName() { return name; }        // 访问器
    public double getSalary() { return salary; }    // 访问器（第 5 章 Manager 覆盖此方法）
    public void raiseSalary(double pct) {           // 更改器
        salary += salary * pct / 100;
    }
}
```
- **隐式参数 `this` vs 显式参数**：`raiseSalary(double pct)` 中 `pct` 是显式参数，`salary` 属于隐式参数 `this`。
- **封装优点**：内部表示可自由修改而不影响调用方；可加校验。

### 4.3 静态字段、常量与方法（★★★）
- `static` 字段属于**类**而非实例（全类共享一份）；`static final` 定义常量（如 `Math.PI`、`System.out`）。
- `static` 方法（如 `Math.pow`、`main`）无 `this`，只能访问静态成员，常用于工厂方法与工具方法。
- **工厂方法**：`LocalDate.now()`、`LocalDate.of(2026,1,1)` 比构造器更灵活、可返回缓存/子类对象。

### 4.4 对象构造（★★★）
- **重载（overload）**：同名方法参数列表不同（与返回类型无关）。
- 默认构造器：类无显式构造器时编译器提供无参构造；一旦定义任意构造器，默认构造器消失。
- `this(...)` 可在构造器首行调用本类另一构造器，避免重复代码。
- 字段初始化顺序：默认 0/false/null → 显式初始化 → 构造器体。
- **`finalize` 已废弃**：不要依赖它释放资源，用 `try-with-resources` 或显式 `close()`。

### 4.5 包与类路径（★★）
- 包用 `package com.example.util;` 声明，目录结构须匹配；`import` 引入类，`import static` 静态导入。
- 访问级别：`private`（类内）→ 默认（包内）→ `protected`（包内 + 子类）→ `public`（任意）。
- `classpath` 告诉 JVM 去哪找类；现代用 jar + 模块（JPMS，了解即可）。

### 4.6 深挖 · 参数传递与对象引用（★★★）

```java
void change(StringBuilder s) { s.append("!"); }            // 改的是同一个对象 → 生效
void reassign(StringBuilder s) { s = new StringBuilder("new"); } // 只改了副本的指向 → 不生效
void bump(int n) { n++; }                                  // 基本类型副本 → 不生效
```

::: danger 易错 · Java 只有「值传递」
方法参数永远得到**一份副本**：基本类型复制值，引用类型复制「引用（地址）」。因此可以在方法内修改对象**内容**（两个引用指向同一对象），但**不能**让调用方的变量改指向另一个对象。常见考题 `swap(a, b)` 在 Java 里无论怎么写都无法交换两个外部变量。
:::

### 4.7 深挖 · 完整的对象初始化顺序（★★★）

```java
class A {
    static { System.out.print("A静 "); }
    { System.out.print("A实 "); }
    A() { System.out.print("A构 "); }
}
class B extends A {
    static { System.out.print("B静 "); }
    { System.out.print("B实 "); }
    B() { System.out.print("B构 "); }
}
new B();
// 输出：A静 B静 A实 A构 B实 B构
```

顺序固定为：① 父类静态字段/静态块（按源码顺序，类加载时**只一次**）→ ② 子类静态 → ③ 父类实例字段默认值 → ④ 父类显式初始化/实例初始化块 → ⑤ 父类构造器体 → ⑥ 子类实例字段默认值 → ⑦ 子类显式初始化/实例块 → ⑧ 子类构造器体。

> 由此推出一个重要陷阱：**构造器里调用可覆盖方法**会在子类字段尚未初始化时就执行，可能读到 0/null。构造器应只调用 `private`、`final` 或 `static` 方法。

### 4.8 深挖 · 访问修饰符与封装（★★★）

| 修饰符 | 同类 | 同包 | 不同包的子类 | 任意位置 |
| --- | --- | --- | --- | --- |
| `private` | ✔ | ✘ | ✘ | ✘ |
| 默认（包私有） | ✔ | ✔ | ✘ | ✘ |
| `protected` | ✔ | ✔ | ✔（**须通过子类自身引用**） | ✘ |
| `public` | ✔ | ✔ | ✔ | ✔ |

- 封装不只是"字段私有 + getter/setter"：更关键的是**不返回可变内部对象的引用**（防御性拷贝），以及**在构造器和更改器里校验不变量**。
- `final` 修饰类（不可继承，如 `String`）、方法（不可覆盖）、字段（引用不可再指向别处，但对象内容仍可变）。

### 4.9 深挖 · 记录类与不可变对象（Java 16+，★★）

```java
public record Point(int x, int y) {
    public Point {                                   // 紧凑构造器（可对参数做校验）
        if (x < 0 || y < 0) throw new IllegalArgumentException("负坐标");
    }
    public double distance() { return Math.hypot(x, y); }   // 可加自定义方法
}
var p = new Point(1, 2);
System.out.println(p);            // Point[x=1, y=2]（自动 toString）
System.out.println(p.x());        // 1 —— 访问器名就是字段名，没有 getX()
```

`record` 自动生成：私有 final 字段、规范构造器、访问器、`equals`/`hashCode`/`toString`。它是 `final` 的、字段不可变，适合 DTO、坐标、键值对等纯数据载体；需要可变状态或继承时应使用普通类。

---

## 第 5 章 继承

### 5.1 类、超类与子类（★★★）
```java
public class Manager extends Employee {      // is-a 关系（Employee 见 4.2）
    private double bonus;

    public Manager(String name, double salary, int id, double bonus) {
        super(name, salary, id);             // 必须首行调用父类构造器
        this.bonus = bonus;
    }
    public void setBonus(double b) { bonus = b; }

    @Override
    public double getSalary() {              // 覆盖（override）
        return super.getSalary() + bonus;    // super 调用父类被覆盖的方法
    }
}
```
- **覆盖规则**：子类方法签名须与父类一致；修饰符不能更严格（如父类 `public` 子类不能降为 `protected`）；`@Override` 注解让编译器帮你校验是否真在覆盖。
- **多态**：`Employee e = new Manager(); e.getSalary();` 运行时按**实际对象类型**调用 `Manager` 版本（动态绑定）。

::: danger 易错 · 继承与多态
- **静态方法不能被覆盖**，只会被隐藏（调用取决于编译期引用类型）。
- 子类**不能**访问父类的 `private` 成员，应通过 `protected` 或访问器。
- 强制类型转换 `Manager m = (Manager) e;` 前务必用 `instanceof` 判断，否则 `ClassCastException`：
  `if (e instanceof Manager m) { m.setBonus(1000); }`（模式匹配，Java 16+ 可直接绑定变量，作用域内无需再强转）。
- **方法调用解析（动态绑定）**：JVM 从对象实际类开始向上查找最匹配的覆盖方法，这是多态的核心。
:::

### 5.2 Object 类（★★★）
所有类都隐式继承 `java.lang.Object`，关键方法：
- `equals(Object)`：默认比较引用（`==`）；**重写须同时重写 `hashCode`**（详见补充六）。
- `hashCode()`：默认返回对象地址派生值；相等对象必须有相等哈希码。
- `toString()`：默认 `类名@哈希`，建议覆盖为可读信息；`+` 拼接字符串时对象自动调 `toString`。
- `getClass()`：返回运行时 `Class` 对象，用于反射与类型判断（`obj.getClass() == other.getClass()`）。
- `clone()`：默认浅拷贝，需实现 `Cloneable`；更推荐用拷贝构造器。

### 5.3 自动装箱与包装类（★★★）
`int ↔ Integer` 自动转换（autoboxing / unboxing）：
```java
Integer a = 100;        // 自动装箱 Integer.valueOf(100)
int b = a;              // 自动拆箱 a.intValue()
```
::: danger 自动装箱缓存陷阱
`Integer` 对 **-128 ~ 127** 做了缓存：`Integer.valueOf(127) == Integer.valueOf(127)` 为 `true`，但 `Integer.valueOf(128) == Integer.valueOf(128)` 为 `false`（超出缓存，新建对象，`==` 比地址）。**比较值永远用 `equals`**。`Long/Short/Byte` 同样缓存 -128~127，`Character` 缓存 0~127，`Boolean` 缓存 TRUE/FALSE；`Float/Double` 无缓存。
:::

### 5.4 反射（★★，了解）
`Class` 类 + `java.lang.reflect` 可在**运行时**探知类的字段/方法/构造器并调用，是框架（Spring、JUnit）的基石，但会绕过访问控制、带来安全风险，普通业务代码少用。

### 5.5 深挖 · 方法调用解析全过程（★★★）

一次 `obj.method(args)` 其实是**两个阶段**：

1. **编译期（重载解析）**：依据变量的**声明类型**（静态类型）和实参类型，从所有同名重载里选出最匹配的一个，写入字节码的符号引用。
2. **运行期（动态绑定）**：依据对象的**实际类型**（动态类型），从实际类开始向上查找该签名的覆盖版本（`invokevirtual`）。

```java
class Parent { int f = 1; static void s(){ System.out.print("P "); } void m(){ System.out.print("Pm "); } }
class Child extends Parent { int f = 2; static void s(){ System.out.print("C "); } @Override void m(){ System.out.print("Cm "); } }
Parent p = new Child();
System.out.println(p.f);   // 1    —— 字段不参与多态，看引用类型
p.s();                     // P     —— static 方法是「隐藏」，看引用类型
p.m();                     // Cm    —— 实例方法动态绑定，看实际对象类型
```

::: danger 易错 · 多态只属于实例方法
字段、`static` 方法、`private` 方法、`final` 方法、`构造器` 都是**静态绑定**；只有可覆盖的**实例方法**才有动态绑定。另外重载在编译期就定死了，所以 `void f(Object)` 与 `void f(String)` 在 `Object o = "x"; f(o);` 时调用的是 `f(Object)` 版本。
:::

### 5.6 深挖 · 继承的设计原则（★★★）

| 原则 | 含义 | 违反后的典型问题 |
| --- | --- | --- |
| 里氏替换 LSP | 子类对象必须能替换父类出现的一切位置且行为不破坏预期 | 子类覆盖方法时抛新异常、收紧前置条件、改变语义 |
| 组合优于继承 | 优先用「has-a」持有成员，而不是「is-a」继承实现 | 父类后续改动「脆弱基类」问题；子类被迫继承一堆无关方法 |
| 开闭原则 | 对扩展开放、对修改关闭 | 每加一种类型都要改一堆 `if-else` |
| 面向接口编程 | 变量声明用接口/抽象类型 | 与具体实现紧耦合，替换困难 |

```java
abstract class DataParser {
    public final String parse(String src) {      // 模板方法：固定流程 + final 防止被改
        String raw = read(src);                  // 复用父类实现
        return transform(raw);                   // 留给子类的扩展点
    }
    protected abstract String transform(String raw);
    private String read(String s) { return s.trim(); }
}
```

> 判断"该不该继承"：只有当 **is-a 关系成立且确实需要多态**时才用 `extends`；仅仅是想复用几行代码，应该用组合或工具类。

### 5.7 深挖 · 反射工作示例（★★）

```java
Class<?> c1 = String.class;                         // ① 类字面量（最安全，不触发初始化）
Class<?> c2 = "abc".getClass();                      // ② 通过对象
Class<?> c3 = Class.forName("java.lang.String");     // ③ 全限定名（会触发类初始化）
System.out.println(c1.getName());                    // java.lang.String
System.out.println(c1.getSuperclass());             // class java.lang.Object
Method sub = c1.getMethod("substring", int.class);  // 获取 public 方法
Object r = sub.invoke("Hello", 2);                  // "llo"
```

- `getMethod(s)` / `getField(s)` 只取 `public`（含继承来的）；`getDeclaredMethod(s)` / `getDeclaredField(s)` 取本类所有访问级别，操作私有成员需先 `setAccessible(true)`（模块化环境可能抛 `InaccessibleObjectException`）。
- 反射是 Spring 依赖注入、JUnit 发现 `@Test`、Jackson 序列化、动态代理的底层机制；代价是**编译期类型检查失效、性能较低、可能破坏封装**，业务代码应优先用接口与泛型。

---

## 第 6 章 接口、lambda 表达式与内部类

### 6.1 接口（★★★）
接口是**一组公开方法签名**的契约，Java 8 后可有默认/静态/私有方法。
```java
// java.lang.Comparable 的真实定义：只有一个抽象方法，没有默认方法 / 静态方法
public interface Comparable<T> {
    int compareTo(T o);          // 负：this 小；0：相等；正：this 大
}

// 接口里默认 / 静态 / 私有方法的语法（用自定义接口演示，别改 JDK 的类）
interface Greeter {
    void say(String name);                       // 抽象方法（隐式 public abstract）
    default void sayTwice(String n) { say(n); say(n); }   // 默认方法（Java 8+）
    static Greeter of() { return n -> System.out.println(n); } // 静态方法（Java 8+）
    private void log() { System.out.println("called"); }  // 私有方法（Java 9+，仅接口内部复用）
}
```
- 类用 `implements` 实现接口，可实现多个（弥补单继承不足）。
- **接口 vs 抽象类**：接口无状态（不能有实例字段，Java 9+ 允许 `private` 方法但无字段），一个类只能继承一个类但可实现多个接口。
- **默认方法冲突**：类同时继承的多个接口有同名默认方法时，必须在该类中**显式重写**以消除歧义（`接口.super.方法()` 选择其一）。
- **克隆**：`Cloneable` 是"标记接口"（无方法），仅作信号。

### 6.2 lambda 表达式与函数式接口（★★★）
lambda 是"可传递的代码块"，用于简化仅有一个抽象方法的**函数式接口**。
```java
// 注意：List.of(...) 返回的是不可变列表，对它 sort() 会抛 UnsupportedOperationException！
List<String> names = new ArrayList<>(List.of("Bob", "Alice", "Carol"));
names.sort((a, b) -> a.compareTo(b));             // lambda
names.sort(Comparator.comparing(String::length));  // 方法引用：按长度排序
```
- **函数式接口**：只有一个抽象方法的接口（用 `@FunctionalInterface` 标注），如 `Runnable`、`Comparator`、`Predicate<T>`、`Function<T,R>`。
- **变量作用域**：lambda 捕获的局部变量必须是**事实最终（effectively final）**——即初始化后不再被重新赋值。
- 方法引用：`对象::方法`、`类::静态方法`、`类::实例方法`、`类::new`。

::: tip 为什么需要 lambda
在 lambda 之前，传递行为要靠匿名内部类写大量样板。lambda 让"把代码当参数传递"变得简洁，是 Stream API 与并发编程的基础。
:::

### 6.3 内部类（★★）
- **成员内部类**：可访问外部类私有成员（编译器偷偷传入 `Outer.this`）。
- **局部内部类 / 匿名内部类**：定义在方法内或临时使用。
- **静态内部类（`static nested`）**：不持有外部类引用，更轻量。
- **代理（Proxy）**：运行时动态生成实现一组接口的类，AOP、RPC、懒加载等底层机制。

### 6.4 深挖 · 接口 vs 抽象类、默认方法冲突（★★★）

| 维度 | 接口 `interface` | 抽象类 `abstract class` |
| --- | --- | --- |
| 继承数量 | 可实现**多个** | 只能 `extends` **一个** |
| 状态 / 实例字段 | 只能有常量（`public static final` 隐式） | 可有普通字段、可变状态 |
| 构造器 | 没有 | 有 |
| 方法实现 | 抽象 + `default` + `static` + `private`（9+） | 任意访问级别的抽象/具体方法 |
| 访问级别 | 方法默认 `public` | 可 `private` / `protected` / 包私有 |
| 语义 | **能做什么**（能力契约 / 角色） | **是什么**（is-a，共享状态与骨架实现） |

```java
interface A { default String hi() { return "A"; } }
interface B { default String hi() { return "B"; } }
class C implements A, B {
    @Override public String hi() { return A.super.hi() + B.super.hi(); } // 必须显式消歧
}
```

::: danger 易错 · 三条冲突规则
① **类优先**：父类（含 `Object`）的具体方法胜过接口的默认方法；② 两个接口默认方法冲突时，实现类**必须重写**；③ 接口继承链中"子接口版本"胜过"父接口版本"。另外 `Object` 的 `equals/hashCode/toString` 不能由接口默认方法提供（编译报错）。
:::

### 6.5 深挖 · 函数式接口与 lambda 语法（★★★）

| 接口 | 抽象方法 | 用途 | 示例 |
| --- | --- | --- | --- |
| `Runnable` | `void run()` | 无参无返回 | `() -> ...` |
| `Supplier<T>` | `T get()` | 供给 / 懒取值 | `() -> LocalDate.now()` |
| `Consumer<T>` | `void accept(T)` | 消费 | `System.out::println` |
| `Function<T,R>` | `R apply(T)` | 转换 | `String::length` |
| `Predicate<T>` | `boolean test(T)` | 判断 | `s -> s.length() > 3` |
| `BiFunction<T,U,R>` | `R apply(T,U)` | 二元转换 | `(a,b) -> a + b` |
| `Comparator<T>` | `int compare(T,T)` | 比较 | `Comparator.comparing(X::getAge)` |

```java
// lambda 语法：(参数) -> { 语句块 }    单参数可省括号；单表达式可省 {} 与 return
Predicate<String> longWord = s -> s.length() > 3;
Function<String,Integer> len = String::length;         // 方法引用：类::实例方法
Supplier<List<String>> f = ArrayList::new;              // 构造器引用
Comparator<String> cmp = Comparator.comparing(String::length)
                                   .thenComparing(Comparator.naturalOrder());

int base = 10;
// base++;                             // 放开这行会编译错：捕获的变量必须 effectively final
IntUnaryOperator add = x -> x + base;   // OK，base 未被重新赋值
```

::: tip lambda 与匿名内部类的关键区别
① lambda 的 `this` 指向**外围对象**，匿名内部类的 `this` 指向内部类自身；② lambda 编译为 `invokedynamic`（运行期生成），匿名内部类生成独立 `.class`；③ lambda 只能用于**函数式接口**（恰好一个抽象方法，`Object` 的 public 方法与 `default`/`static` 方法不计入）。局部变量捕获要求 effectively final，本质是因为捕获的是**值副本**，避免生命周期不一致导致的数据错乱。
:::

### 6.6 深挖 · 内部类四类型与动态代理（★★）

| 类型 | 定义位置 | 持有外部引用 | 典型用途 |
| --- | --- | --- | --- |
| 成员内部类 | 类体中，非 static | ✔（`Outer.this`） | 与外部实例强绑定，如 `Map.Entry` 实现 |
| 静态嵌套类 | 类体中，`static` | ✘ | 更轻量，如 `Integer` 缓存、`Builder` |
| 局部内部类 | 方法 / 代码块内 | ✔ | 仅方法内使用，可访问 effectively final 局部变量 |
| 匿名内部类 | `new Interface() { /* 实现方法 */ }` | ✔ | 一次性实现；有多个抽象方法时仍需用它 |

```java
// JDK 动态代理：基于接口，是 Spring AOP 的默认实现之一
interface Service { void hello(); }
InvocationHandler h = (proxy, method, args) -> {
    System.out.println("前置日志");      // 增强逻辑
    return null;                        // 真实场景应 method.invoke(target, args)
};
Service s = (Service) Proxy.newProxyInstance(
        Service.class.getClassLoader(), new Class<?>[]{Service.class}, h);
s.hello();                              // 打印：前置日志
```

> JDK 动态代理**只能代理接口**；要代理没有接口的类需 CGLIB/ByteBuddy 之类基于继承的字节码增强（因此 `final` 类无法被代理）。

---

## 第 7 章 异常、断言、日志与调试

### 7.1 异常分类（★★★）
异常层次见下图（`Throwable` 为根）：

![Java 异常体系](/java/java-exceptions.svg)

- **Error**：系统级严重错误（如 `OutOfMemoryError`、`StackOverflowError`），通常无法恢复，**不应捕获**（也不该用 `catch (Throwable)` 把它吞掉）。
- **Exception**：
  - **RuntimeException（未检查）**：代码逻辑错误导致（空指针、越界、类型转换、除零），编译器**不强制**处理，应通过改代码避免。
  - **其他 Exception（已检查/checked）**：如 `IOException`，编译器**强制** `try-catch` 或 `throws` 声明。

### 7.2 捕获与处理（★★★）
```java
// ✘ 常见错例：in 声明在 try 块内，finally 里访问不到；in.close() 还会抛受检异常
// ✔ 正解 1：声明提到 try 外，finally 里再包一层 try-catch
FileInputStream in = null;
try {
    in = new FileInputStream("a.txt");
    // ... 使用 in
} catch (FileNotFoundException e) {        // 子类异常在前
    e.printStackTrace();
} finally {
    if (in != null) {
        try { in.close(); } catch (IOException e) { e.printStackTrace(); }
    }
}

// ✔ 正解 2（推荐）：try-with-resources，资源实现 AutoCloseable，按声明逆序自动关闭
try (InputStream is = new FileInputStream("a.txt");
     BufferedReader br = new BufferedReader(new InputStreamReader(is, StandardCharsets.UTF_8))) {
    System.out.println(br.readLine());
} catch (IOException e) {
    e.printStackTrace();   // close 抛出的异常会作为 suppressed 附加：e.getSuppressed()
}
```
- **捕获顺序**：子类必须写在父类之前。
- **try-with-resources**（推荐）：资源实现 `AutoCloseable`，自动关闭，无需 `finally`：
```java
try (BufferedReader br = Files.newBufferedReader(Path.of("a.txt"))) {
    return br.readLine();
} catch (IOException e) { e.printStackTrace(); }   // 自动关闭后才把异常交给 catch
```
- **异常链**：`throw new RuntimeException("包装", cause);` 用 `getCause()` 追溯根因。

### 7.3 断言与日志（★★）
- `assert cond : "message";` 用于**内部不变量**检查，生产环境默认关闭（`-ea` 开启），不可用于参数校验（用户可关）。
- 日志用 `java.util.logging`（JUL）或 Log4j/SLF4J；比 `System.out.println` 更可控（级别、处理器、格式器、可关闭）。

### 7.4 深挖 · finally、throw/throws 与自定义异常（★★★）

```java
static int demo() {
    try { return 1; }
    finally { /* 不要在这里 return！ */ System.out.println("cleanup"); }
}
```

::: danger 易错 · finally 覆盖返回值
`try { return 1; } finally { return 2; }` 实际返回 **2** —— finally 的 return 会覆盖 try/catch 的返回值，并**吞掉尚未抛出的异常**。同理，finally 里修改在 try 中 return 的**基本类型变量不影响返回值**（返回值已被保存），但若返回的是可变对象引用，修改对象内容会生效。`System.exit()` 或 JVM 崩溃是 finally 不执行的少数例外。
:::

| 对比 | `throw` | `throws` |
| --- | --- | --- |
| 位置 | 方法体内 | 方法声明的签名末尾 |
| 作用 | 抛出一个**异常对象** | 声明本方法**可能抛出**的异常类型，告知调用方 |
| 数量 | 一次一个 | 可逗号分隔多个 |

```java
class ScoreException extends Exception {              // 自定义受检异常
    public ScoreException(String msg) { super(msg); }
}
static void check(int s) throws ScoreException {
    if (s < 0 || s > 100) throw new ScoreException("非法分数: " + s);
}
try { check(120); }
catch (ScoreException e) {
    throw new IllegalArgumentException("参数校验失败", e);  // 异常链：保留根因 cause
}
```

> 覆盖方法时，子类 `throws` 的异常**不能比父类更宽**（不能新增父类未声明的受检异常），但可以抛出更少或更具体的异常，或者不抛。接口同理。

### 7.5 深挖 · 异常与日志最佳实践（★★）

| 日志级别（SLF4J / JUL 对照） | 使用场景 |
| --- | --- |
| `TRACE` / `FINER` | 极细粒度跟踪（循环内部、参数逐条） |
| `DEBUG` / `FINE` | 调试信息，生产默认关闭 |
| `INFO` | 关键业务节点（启动、订单创建） |
| `WARN` | 可恢复的异常、降级、重试 |
| `ERROR` / `SEVERE` | 需要人工介入的失败 |

- 用**参数化日志** `log.info("user={} cost={}ms", name, cost)`，不要字符串拼接（关闭级别时不产生开销）；异常对象作为最后一个参数传入以打印堆栈。
- 不要 `catch (Exception e) {}` 空吞异常；不要在循环中反复抛异常（构造堆栈开销大）；不要用异常做正常流程控制。
- 受检异常 vs 未检查异常的选择：**调用方能合理恢复** → 受检；**编程错误 / 前置条件违反**（参数非法、状态不对）→ 未检查（`IllegalArgumentException`、`IllegalStateException`）。
- 断言 `assert x > 0 : "x must > 0";` 只在 `-ea` 开启时生效，用于**内部不变量自检**；对外参数校验必须用 `if + throw`，否则用户关掉断言就绕过了校验。

---

## 第 8 章 泛型程序设计

### 8.1 为什么用泛型（★★★）
泛型让集合等容器"在编译期保证类型安全、避免强制转换"：
```java
List<String> list = new ArrayList<>();   // <> 菱形推断
list.add("ok");
String s = list.get(0);                  // 无需 (String) 强转
// list.add(123);                        // 编译期直接报错
```

### 8.2 定义泛型类与方法（★★★）
```java
public class Pair<T, U> {
    private final T first;
    private final U second;
    public Pair(T first, U second) { this.first = first; this.second = second; }
    public T getFirst() { return first; }
    public U getSecond() { return second; }

    // 泛型方法：类型参数 <V> 声明在返回类型之前，与类的 T/U 相互独立
    public static <V> List<V> singleton(V v) {
        List<V> one = new ArrayList<>();
        one.add(v);
        return one;
    }
    @Override public String toString() { return "(" + first + ", " + second + ")"; }
}

Pair<String, Integer> p = new Pair<>("age", 18);   // 菱形推断 <>
System.out.println(p);                             // (age, 18)
List<Number> ns = Pair.singleton(Integer.valueOf(1)); // 目标类型推断为 Number
```
- **类型变量限定**：`<T extends Comparable<T>>` 要求 T 实现 Comparable。

### 8.3 类型擦除（★★★）
JVM **没有泛型**——编译后泛型信息被"擦除"：
- `List<String>` 与 `List<Integer>` 运行时都是 `List`；
- 限定类型被替换为第一个 bound（无 bound 则为 `Object`）；
- 必要时编译器自动插入强制转换与**桥方法**以保持多态。

::: danger 泛型局限性（必考易错）
1. **不能用基本类型实例化类型参数**：`List<int>` 非法，须 `List<Integer>`。
2. 运行时类型查询只适用于**原始类型**：`if (a instanceof List)` 可以，`instanceof List<String>` 不行。
3. 不能 `new T()`、不能 `new T[]`（类型擦除后未知）。
4. 静态字段/方法不能使用类的类型变量。
5. 不能抛出或捕获泛型类实例（`catch (T e)` 非法）。
:::

### 8.4 通配符与 PECS（★★★）
- `List<? extends Number>`：**生产者（Producer）**，只能读取（out），不能写入（除 null）——上界通配。
- `List<? super Integer>`：**消费者（Consumer）**，只能写入 Integer 及其子类型（in），读取返回 `Object`——下界通配。
- **PECS 原则**：Producer Extends, Consumer Super。例如 `Collections.copy(dest, src)` 中 `src` 是生产者用 `? extends`，`dest` 是消费者用 `? super`。

![泛型擦除、桥方法与 PECS 通配符](/java/java-generic.svg)

`Collections.copy` 的真实签名正好是 PECS 的教科书范例：

```java
public static <T> void copy(List<? super T> dest, List<? extends T> src)
// dest 只被写入（消费者 → super），src 只被读出（生产者 → extends）
```

### 8.5 深挖 · 擦除与桥方法（★★★）

```java
// 源码
class StringBox implements Comparable<String> {
    @Override public int compareTo(String s) { return 0; }
}
```

擦除后接口方法变成 `compareTo(Object)`，而实现类只有 `compareTo(String)`，签名对不上、多态会断。编译器因此生成一个**桥方法**（`javap -c StringBox` 可见）：

```java
// 编译器自动生成的合成桥方法（示意）
public int compareTo(Object o) { return compareTo((String) o); }  // 转发 + 强制转换
```

::: danger 易错 · 擦除导致的重载冲突
`void f(List<String> a)` 与 `void f(List<Integer> a)` **不能共存**：擦除后两者都是 `f(List)`，签名重复。同理 `class X implements Comparable<X>, Comparable<Y>` 非法（同一接口被参数化两次，擦除后相同）。
:::

### 8.6 深挖 · 泛型局限性完整清单与绕法（★★★）

| 限制 | 根本原因 | 常用绕法 |
| --- | --- | --- |
| `List<int>` 非法 | 擦除后容器要装 `Object` | 用包装类 `List<Integer>`（有装箱开销） |
| `new T()` / `new T[n]` | 运行时不知道 T 是什么 | 传入 `Class<T>` + 反射，或 `Supplier<T>`；数组用 `Array.newInstance(type, n)` |
| `instanceof List<String>` | 运行时泛型信息已消失 | 只判断 `instanceof List`，再逐元素校验类型 |
| 静态字段/方法用类的 `T` | 静态成员属于类，不属于某个参数化实例 | 改成**静态泛型方法**（自己声明 `<T>`） |
| `catch (T e)` / 泛型异常类 | JVM 无法区分擦除后的异常类型 | 用具体异常类型；泛型信息放在异常字段里 |
| 重载参数化类型 | 擦除后签名相同 | 换方法名或换参数个数 |
| `List<String>` 赋给 `List<Object>` | 泛型**不协变** | 用 `List<? extends Object>` 只读视图，或 `Collections.unmodifiableList` |

> 泛型不协变是关键设计：若允许 `List<String>` 当 `List<Object>`，就能往里 `add(new Integer(...))`，类型安全彻底失效。数组却**是协变的**（`String[]` 可赋给 `Object[]`），代价是运行时用 `ArrayStoreException` 兜底——这是数组与泛型最重要的差异之一。

### 8.7 工作示例 · 写一个真正通用的 max（★★★）

```java
public static <T extends Comparable<? super T>> T max(List<? extends T> list) {
    if (list.isEmpty()) throw new IllegalArgumentException("empty list");
    Iterator<? extends T> it = list.iterator();
    T best = it.next();
    while (it.hasNext()) {
        T x = it.next();
        if (x.compareTo(best) > 0) best = x;
    }
    return best;
}
```

签名三处讲究：① `<T extends Comparable<? super T>>` 允许「父类实现了 Comparable」的子类（如某子类继承已实现 `Comparable<父类>` 的基类）；② 参数 `List<? extends T>` 让 `List<Integer>` 也能传给 `T = Number`；③ 用 `Iterator` 而非 `get(i)`，对 `LinkedList` 也是 O(n)。

---

## 第 9 章 集合框架

### 9.1 框架总览（★★★）
集合框架继承层次见下图：

![Java 集合框架](/java/java-collections.svg)

- **Collection**（继承 `Iterable`）三大分支：**List**（有序可重复）、**Set**（无序不重复）、**Queue/Deque**（队列/双端队列）。
- **Map** 是独立的键值对根接口（不继承 Collection）。

### 9.2 各实现对比（★★★）

| 接口 | 实现类 | 底层 | 特点 / 复杂度 |
| --- | --- | --- | --- |
| `List` | `ArrayList` | 动态数组 | 随机访问 O(1)，插入删除尾部 O(1)、中间 O(n) |
| | `LinkedList` | 双向链表 | 头尾插入删除 O(1)，随机访问 O(n) |
| `Set` | `HashSet` | 哈希表 | 增删查 O(1)，无序 |
| | `TreeSet` | 红黑树 | 有序，增删查 O(log n) |
| | `LinkedHashSet` | 哈希 + 链表 | 保持插入顺序 |
| `Queue` | `ArrayDeque` | 循环数组 | 双端队列，优于遗留 `Stack` |
| | `PriorityQueue` | 堆 | 按优先级出队 |
| `Map` | `HashMap` | 哈希表 | 增删查 O(1) |
| | `TreeMap` | 红黑树 | 键有序 |
| | `LinkedHashMap` | 哈希 + 链表 | 保持插入/访问顺序 |
| | `Hashtable` | 哈希表 | 遗留、线程安全、`null` 键非法，不推荐 |

::: info HashMap 底层要点（常考）
- 底层是 `Node<K,V>[]` 数组 + 链表/红黑树。容量始终为 2 的幂。
- 索引：`hash = (h = key.hashCode()) ^ (h >>> 16)` 再 `(n-1) & hash`，高位也参与运算以减少冲突。
- 链表长度 ≥ **8（TREEIFY_THRESHOLD）** 且数组容量 ≥ 64 时转红黑树；≤ 6 退化为链表。
- `key` 须正确重写 `equals`+`hashCode`（见补充六），否则找不到对应桶。
:::

### 9.3 迭代器与视图（★★★）
- `Iterator`：`hasNext()/next()/remove()`；`for-each` 本质用 `Iterator`，**遍历时不能直接用集合 `remove`**，应改用 `iterator.remove()`。
- **视图（Views）**：`keySet()/values()/entrySet()` 是原映射的"视图"，改动视图会反映到原映射。
- 同步视图：`Collections.synchronizedList(...)`（每次访问加锁，效率低）；并发场景用 `java.util.concurrent`（见第 12 章）。
- `Collections` 算法：`sort`（依赖 `Comparable`/`Comparator`）、`shuffle`、`binarySearch`、`max/min`。

### 9.4 实用 API（★★）
- `List.of(a,b,c)`、`Set.of(...)`、`Map.of(k,v,...)`（Java 9+，不可变）；可变用 `new ArrayList<>()`。
- 集合 ↔ 数组：`list.toArray(new String[0])`、`Arrays.asList(arr)`（返回**固定大小**的 List，不能 add/remove）。

![HashMap 底层结构与扩容树化](/java/java-hashmap.svg)

### 9.5 深挖 · HashMap 全流程（★★★）

```java
// 定位桶：先扰动哈希，再按位与取下标（n 为 2 的幂时等价于取模但更快）
static final int hash(Object key) {
    int h;
    return (key == null) ? 0 : (h = key.hashCode()) ^ (h >>> 16);
}
// index = (n - 1) & hash
```

| 环节 | 规则 / 默认值 |
| --- | --- |
| 初始容量 | 16（懒初始化：第一次 put 才真正分配数组） |
| 负载因子 | 0.75；阈值 = 容量 × 负载因子 |
| 扩容 | size > 阈值 → 容量翻倍；JDK 8 用 `(hash & oldCap)` 判断高位，元素要么留原下标要么去 `原下标 + oldCap`，无需重新计算 hash |
| 冲突处理 | 先链表尾插；同桶链表长度 ≥ 8 **且**数组容量 ≥ 64 → 转红黑树；容量不足 64 时优先扩容 |
| 退化 | 树节点数 ≤ 6 → 退回链表 |
| 判同 | 先比 `hash`，再用 `key.equals()`；相同则覆盖 value 并返回旧值 |
| null | 允许 **1 个 null 键**（固定放桶 0）、多个 null 值 |

::: danger 易错 · 键的契约
作为键的类必须**同时正确重写 `equals` 和 `hashCode`**，且参与比较的字段在对象放入 Map 后**不可再修改**，否则 `get` 时会定位到另一个桶 ——「存进去却找不到自己」。`HashMap` 完全非线程安全，并发写用 `ConcurrentHashMap`（JDK 8 起桶级 `synchronized` + CAS，不再使用分段锁）。
:::

### 9.6 深挖 · fail-fast 与视图（★★★）

```java
List<String> l = new ArrayList<>(List.of("a", "b", "c"));
// ✘ for (String s : l) if ("b".equals(s)) l.remove(s);  → ConcurrentModificationException
Iterator<String> it = l.iterator();
while (it.hasNext()) { if ("b".equals(it.next())) it.remove(); }  // ✔ 用迭代器自身的 remove
// 或 Java 8+：l.removeIf(s -> "b".equals(s));
```

- `ArrayList`/`HashMap` 的迭代器是 **fail-fast**：内部记录 `modCount`，遍历中检测到集合被结构性修改就立刻抛 `ConcurrentModificationException`（只是尽力而为的**错误检测**，不是并发保证）。
- `java.util.concurrent` 的集合（如 `ConcurrentHashMap`）迭代器是**弱一致性 / fail-safe**，不抛该异常，但不保证看到所有并发更新。
- `keySet()` / `values()` / `entrySet()` 返回的是**视图**（不是副本）：`map.keySet().remove(k)` 会真的删掉映射；想脱离原集合请用 `new ArrayList<>(...)` 或 `Collections.unmodifiableXxx`。
- `Arrays.asList(arr)` 返回固定大小 List（`set` 可以、`add/remove` 抛 `UnsupportedOperationException`），且改动会反映到原数组；`List.of(...)` 则是**完全不可变**、不允许 `null` 元素。

### 9.7 工作示例 · 词频统计（★★）

```java
String text = "java stream java lambda stream java";
Map<String, Long> freq = Arrays.stream(text.split(" "))
        .collect(Collectors.groupingBy(Function.identity(),
                                       TreeMap::new,      // 指定 Map 实现 → 键有序输出
                                       Collectors.counting()));
System.out.println(freq);   // {java=3, lambda=1, stream=2}

// 等价的经典写法（理解 merge 的用法）
Map<String, Integer> m = new HashMap<>();
for (String w : text.split(" ")) m.merge(w, 1, Integer::sum);
```

### 9.8 集合选型决策表（★★★）

| 需求 | 首选 | 理由 |
| --- | --- | --- |
| 按索引频繁随机访问 | `ArrayList` | 连续数组，`get(i)` 为 O(1)、缓存友好 |
| 频繁在头部/中间增删 | `LinkedList`（或按需换成 `ArrayDeque`） | 已知节点位置时改指针 O(1)；但按索引定位仍 O(n) |
| 去重、不关心顺序 | `HashSet` | 哈希 O(1) |
| 去重且要排序 / 范围查询 | `TreeSet` | 红黑树 O(log n)、有序 |
| 保持插入顺序 | `LinkedHashSet` / `LinkedHashMap` | 双向链表维护顺序，可作 LRU 基础 |
| 键值对高频查找 | `HashMap` | O(1)；千万注意键的不可变性 |
| 键有序 / 需要首尾、区间 | `TreeMap` | `firstKey()`、`headMap()` 等 |
| 队列 / 栈 / 双端 | `ArrayDeque` | 比遗留 `Stack`、`Vector` 更快，且不支持 null |
| 按优先级出队 | `PriorityQueue` | 二叉堆，出队 O(log n) |
| 多线程读写 | `ConcurrentHashMap`、`CopyOnWriteArrayList`、阻塞队列 | 按场景选择，勿用 `Collections.synchronizedXxx` 扛高并发 |
| 对外暴露只读集合 | `List.of` / `Collections.unmodifiableList` | 防止调用方意外修改内部状态 |

---

## 第 10 章 图形用户界面程序设计

### 10.1 Swing 简史与窗体（★）
Java GUI 经历 AWT → Swing（轻量、纯 Java 绘制）→ JavaFX。Swing 组件名多以 `J` 开头（`JFrame`、`JButton`）。
```java
JFrame frame = new JFrame("Demo");
frame.setSize(400, 300);
frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
frame.setVisible(true);     // 最后设为可见
```

### 10.2 绘图与事件（★★）
- 2D 图形：`Graphics2D` 绘制形状、设置 `Color`、`Stroke`。
- **事件处理**采用"委托事件模型"：组件触发事件，注册 `Listener`（`ActionListener` 等）响应：
```java
button.addActionListener(e -> System.out.println("clicked"));
```
- `JPanel` 的 `paintComponent` 方法用于自定义绘制（须调用 `super.paintComponent`）。

### 10.3 深挖 · 委托事件模型与 EDT（★★）

事件处理由三方协作完成：

| 角色 | 说明 | 例子 |
| --- | --- | --- |
| 事件源 | 产生事件的组件 | `JButton` |
| 事件对象 | 封装事件信息（时间、来源、参数） | `ActionEvent`、`MouseEvent`、`KeyEvent` |
| 事件监听器 | 注册到源上、事件发生时被回调 | `ActionListener`（函数式接口，可用 lambda） |

```java
JButton btn = new JButton("点击");
btn.addActionListener(e -> System.out.println("clicked: " + e.getActionCommand()));
btn.addActionListener(e -> System.out.println("第二个监听器"));  // 可注册多个，按注册顺序回调

// Swing 组件必须在 EDT（Event Dispatch Thread）上创建与访问
SwingUtilities.invokeLater(() -> {
    JFrame f = new JFrame("Demo");
    f.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    f.setSize(400, 300);
    f.setVisible(true);
});
```

::: danger 易错 · Swing 线程规则
所有对 Swing 组件的访问都要在 EDT 上进行；耗时任务（网络、IO、大计算）绝不能放在 `ActionListener` 里同步执行，否则界面**冻结**。正确做法是用 `SwingWorker`（`doInBackground` 做后台、`done` 回 EDT 更新 UI）或线程池 + `invokeLater` 回投结果。
:::

---

## 第 11 章 Swing 用户界面组件

### 11.1 布局管理（★★）
- `BorderLayout`（东/南/西/北/中）、`FlowLayout`、`GridLayout`（网格）、`GridBagLayout`（复杂）、`BoxLayout`。布局管理器决定组件如何随窗口缩放排列。

### 11.2 常用组件（★★）
- 文本输入：`JTextField`、`JPasswordField`、`JTextArea`。
- 选择组件：`JCheckBox`（复选）、`JRadioButton`（单选，配合 `ButtonGroup`）、`JSlider`（滑块）、`JComboBox`（下拉）。
- 菜单：`JMenuBar` / `JMenu` / `JMenuItem`，可设助记符与快捷键；弹出菜单 `JPopupMenu`。
- 对话框：`JOptionPane` 提供现成的确认/输入/消息框；`JFileChooser` 选择文件。

::: tip
GUI 章节以"会用即可"为目标，考试/面试多集中在**语言基础、集合、并发、JVM**，GUI 通常不是重点，理解事件委托模型与布局即可。
:::

### 11.3 深挖 · 布局与组件速查（★★）

| 布局管理器 | 排列方式 | 适用 |
| --- | --- | --- |
| `BorderLayout` | 东/南/西/北/中 五区（`JFrame` 默认） | 主窗体骨架 |
| `FlowLayout` | 从左到右、自动换行（`JPanel` 默认） | 一排按钮 |
| `GridLayout` | 等大网格 | 计算器键盘 |
| `GridBagLayout` | 网格 + 权重/跨格，最灵活也最复杂 | 复杂表单 |
| `BoxLayout` | 单行/单列 | 垂直堆叠 |

| 组件类别 | 常用类 | 关键事件/方法 |
| --- | --- | --- |
| 容器 | `JFrame`、`JPanel`、`JScrollPane` | `add`、`setLayout`、`revalidate` |
| 文本 | `JTextField`、`JPasswordField`、`JTextArea`、`JLabel` | `getText`、`setText`、`DocumentListener` |
| 按钮 | `JButton`、`JCheckBox`、`JRadioButton`（+`ButtonGroup`） | `ActionListener`、`ItemListener` |
| 选择 | `JComboBox`、`JList`、`JSlider`、`JSpinner` | `getSelectedItem`、`ListSelectionListener` |
| 菜单 | `JMenuBar` / `JMenu` / `JMenuItem` / `JPopupMenu` | `setMnemonic`、快捷键 |
| 对话框 | `JOptionPane`、`JFileChooser`、`JDialog` | `showMessageDialog` / `showConfirmDialog` |

```java
// 常用对话框与模型-视图分离示例
int ans = JOptionPane.showConfirmDialog(null, "确定删除？", "确认", JOptionPane.YES_NO_OPTION);

String[] data = {"Java", "Python", "Go"};
JList<String> list = new JList<>(data);           // JList 用 ListModel 存数据
list.addListSelectionListener(e -> {
    if (!e.getValueIsAdjusting()) System.out.println(list.getSelectedValue());
});
frame.add(new JScrollPane(list));                  // 放进滚动面板才自带滚动条
```

---

## 第 12 章 并发

### 12.1 线程与状态（★★★）
并发让多个任务"看似"同时执行（多核则真并行）。线程状态转换见下图：

![Java 线程状态](/java/java-threadstates.svg)

```java
Thread t = new Thread(() -> {          // 用 Runnable/lambda 创建
    System.out.println("running");
});
t.start();                             // 启动（不能重复 start）
// t.run();                            // 错误：只是普通方法调用，不在新线程
```

### 12.2 同步与锁（★★★）
多线程共享可变状态会产**竞态条件（race condition）**。Java 提供多种机制：

| 机制 | 说明 |
| --- | --- |
| `synchronized` 方法/块 | 内置锁（监视器锁），同一时刻仅一个线程进入 |
| `ReentrantLock` | 显式锁，可定时/可中断/公平锁 |
| `volatile` | 保证可见性（一个线程写、其他立即可见），**不保证原子性** |
| 原子类 `AtomicInteger` 等 | CAS 无锁原子更新 |
| `final` 字段 | 正确发布后不可变，天然线程安全 |
| `ThreadLocal` | 每线程独立副本，避免共享 |

::: danger 并发易错点
- **`synchronized` 保证原子性 + 可见性 + 有序性（一定程度）**，但锁对象必须同一把；锁 `this` 与锁 `类名.class` 不是同一把锁。
- `volatile` **不能替代锁**来计数自增（`i++` 仍非原子）；自增用 `AtomicInteger.incrementAndGet()`。
- 死锁：两个线程互相等待对方持有的锁——按**固定顺序**获取多把锁可避免。
- 不要使用已废弃的 `stop()`/`suspend()`（会破坏状态/死锁）。
:::

### 12.3 线程安全集合（★★★）
`java.util` 下的普通集合**非线程安全**。并发场景用 `java.util.concurrent`：
- **阻塞队列** `ArrayBlockingQueue`/`LinkedBlockingQueue`：生产者-消费者模型核心。
- **并发 Map/Set**：`ConcurrentHashMap`（分段/桶级锁，高并发读写）、`ConcurrentSkipListMap`（有序）。
- **写时复制** `CopyOnWriteArrayList`：读多写少场景，读无锁。
- **并行数组算法**：`Arrays.parallelSort`。

### 12.4 任务与线程池（★★★）
直接 `new Thread` 开销大且难管理，应使用**执行器（Executor）**线程池：
```java
ExecutorService pool = Executors.newFixedThreadPool(4);
Future<Integer> f = pool.submit(() -> {   // Callable 有返回值
    return 1 + 1;
});
Integer r = f.get();                      // 阻塞获取结果
pool.shutdown();
```
- `Callable<V>` 有返回值且可抛异常；`Runnable` 无返回值。
- `Future` 代表异步计算结果；`CompletableFuture` 支持链式/组合异步（Java 8+）。
- `fork-join` 框架适合分治型并行计算。

### 12.5 深挖 · 线程创建、状态与中断（★★★）

```java
// 方式 1：继承 Thread（不推荐，占用唯一的继承名额）
class MyThread extends Thread { @Override public void run() { /* ... */ } }
// 方式 2：实现 Runnable（推荐，任务与线程解耦）
new Thread(() -> System.out.println("runnable")).start();
// 方式 3：实现 Callable + FutureTask / 线程池（可拿返回值、可抛受检异常）
ExecutorService es = Executors.newSingleThreadExecutor();
Future<Integer> f = es.submit(() -> 42);
es.shutdown();
```

| `Thread.State` | 进入条件 | 回到 RUNNABLE 的条件 |
| --- | --- | --- |
| `NEW` | `new Thread(...)` 尚未 `start()` | `start()` |
| `RUNNABLE` | 就绪或正在运行（JVM 不区分二者） | — |
| `BLOCKED` | 等待进入 `synchronized` 监视器锁 | 拿到锁 |
| `WAITING` | `wait()`、`join()`、`LockSupport.park()` | `notify()`/`notifyAll()`、目标线程结束、`unpark()` |
| `TIMED_WAITING` | `sleep(t)`、`wait(t)`、`join(t)`、`parkNanos` | 超时或被唤醒 |
| `TERMINATED` | `run()` 正常结束或未捕获异常退出 | 终态，不可再 `start()` |

::: danger 易错 · 线程控制
- `start()` 才会开启新线程；直接调 `run()` 只是**当前线程里的普通方法调用**。同一个 `Thread` 对象**不能 `start()` 两次**（抛 `IllegalThreadStateException`）。
- 停止线程用**协作式中断**：`t.interrupt()` 只是设置中断标志，阻塞方法（`sleep`/`wait`/`join`）会抛 `InterruptedException` 并**清除标志**，捕获后应恢复 `Thread.currentThread().interrupt()` 或向上抛出；绝不要用废弃的 `stop()`/`suspend()`。
- `wait()` / `notify()` / `notifyAll()` 必须在**持有该对象监视器锁**的 `synchronized` 块内调用，否则抛 `IllegalMonitorStateException`；`wait()` 会**释放锁**，`sleep()` 不会。`notify()` 只唤醒一个，通常更稳妥用 `notifyAll()`；等待条件必须放在 `while` 循环里防**虚假唤醒**。
- 守护线程 `setDaemon(true)` 须在 `start()` 前设置；所有非守护线程结束后 JVM 直接退出，守护线程的 `finally` 不保证执行，不适合做关键清理。
:::

### 12.6 深挖 · synchronized、volatile 与 JMM（★★★）

```java
// synchronized 的三种写法，锁对象各不相同
public synchronized void a() { counter++; }              // 锁 this（当前实例）
public static synchronized void b() { total++; }          // 锁 类名.class（Class 对象）
public void c() { synchronized (lock) { counter++; } }    // 锁指定对象，粒度最小、推荐

// volatile：可见性 + 禁止重排序，但不保证复合操作原子性
private volatile boolean running = true;            // 典型的停止标志
private volatile int counter;                       // counter++ 仍非原子！要用 AtomicInteger
```

| 机制 | 原子性 | 可见性 | 有序性 | 开销 / 适用 |
| --- | --- | --- | --- | --- |
| `synchronized` | ✔ | ✔ | ✔（同一把锁内） | 悲观互斥，可重入，适合复合操作 |
| `volatile` | ✘ | ✔ | ✔（禁止特定重排） | 轻量，适合状态标志、单次发布的不可变对象 |
| `AtomicInteger`（CAS） | ✔（单次操作） | ✔ | ✔ | 无锁，适合计数；高竞争下自旋耗 CPU |
| `ReentrantLock` | ✔ | ✔ | ✔ | 可中断、可超时、可公平、需 `finally` 释放 |
| `final` 字段 | — | ✔（正确构造发布后） | ✔ | 不可变对象天然线程安全 |

**happens-before（JMM 的核心，判断"上一个写入能否被看到"）**：

| 规则 | 含义 |
| --- | --- |
| 程序次序 | 单线程内前面的操作 happens-before 后面的操作 |
| volatile | 对 volatile 变量的写 happens-before 之后对它的读 |
| 监视器锁 | `unlock` happens-before 之后对同一把锁的 `lock` |
| 线程启动 | `start()` happens-before 新线程中的任何操作 |
| 线程终止 | 线程中所有操作 happens-before 其他线程 `join()` 返回 / `isAlive()` 为 false |
| 传递性 | A hb B、B hb C ⇒ A hb C |

```java
// 死锁：两个线程以相反顺序获取两把锁（各持一把后互相等待）
Object lockA = new Object(), lockB = new Object();
Runnable r1 = () -> { synchronized (lockA) { synchronized (lockB) { } } };
Runnable r2 = () -> { synchronized (lockB) { synchronized (lockA) { } } };
// 预防：所有线程按**固定全局顺序**获取锁，或用 tryLock 超时后回退重试
```

### 12.7 工作示例 · 生产者-消费者（★★★）

```java
// 推荐：用 BlockingQueue，阻塞与线程安全都由它负责
BlockingQueue<Integer> q = new ArrayBlockingQueue<>(10);
Runnable producer = () -> {
    try {
        for (int i = 0; i < 5; i++) { q.put(i); System.out.println("生产 " + i); }
        q.put(-1);                                   // 哨兵，通知消费者结束
    } catch (InterruptedException e) { Thread.currentThread().interrupt(); }
};
Runnable consumer = () -> {
    try {
        while (true) {
            int x = q.take();
            if (x == -1) break;
            System.out.println("消费 " + x);
        }
    } catch (InterruptedException e) { Thread.currentThread().interrupt(); }
};
new Thread(producer).start();  new Thread(consumer).start();
```

```java
// 底层写法：wait / notifyAll（理解用，工程中优先用 BlockingQueue）
synchronized (queue) {
    while (queue.isEmpty()) queue.wait();            // 必须 while，防虚假唤醒
    Object item = queue.remove();
    queue.notifyAll();                               // 通知生产者
}
```

### 12.8 深挖 · 线程池参数与异步组合（★★★）

![ThreadPoolExecutor 参数与任务执行流程](/java/java-threadpool.svg)

| 参数 | 说明 |
| --- | --- |
| `corePoolSize` | 核心线程数，默认即使空闲也不回收 |
| `maximumPoolSize` | 最大线程数上限 |
| `keepAliveTime` + `unit` | 非核心线程的空闲存活时间 |
| `workQueue` | 任务队列，务必**有界**（`ArrayBlockingQueue`） |
| `threadFactory` | 自定义线程名、优先级、是否守护（排查问题很有用） |
| `handler` | 拒绝策略，默认 `AbortPolicy` 抛异常 |

执行顺序：**核心线程未满 → 建核心线程；否则入队；队列满且线程数 < maximum → 建临时线程；再满 → 触发拒绝策略**。

::: danger 易错 · 线程池
- `Executors.newFixedThreadPool` / `newSingleThreadExecutor` 用**无界** `LinkedBlockingQueue`，`newCachedThreadPool` 的 maximum 近乎无限，高并发下都可能 OOM。生产环境应显式 `new ThreadPoolExecutor(...)`，配有界队列和有意义的拒绝策略。
- `execute()` 抛出的异常会直接到未捕获异常处理器；`submit()` 会把异常**封装进 Future**，只有调用 `get()` 时才抛 `ExecutionException` —— 不 get 就等于吞了异常。
- `Future.get()` 会阻塞；`CompletableFuture` 支持 `thenApply` / `thenCompose` / `allOf` / `exceptionally` 组合异步，并可指定自定义线程池避免共用 `ForkJoinPool.commonPool()`。
:::

---

## 补充与进阶（教材相对单薄、工程必备）

### 补 1 JVM 内存模型与垃圾回收（★★★）
- **线程私有**：程序计数器、虚拟机栈（栈帧=方法调用）、本地方法栈。
- **线程共享**：**堆（对象实例，GC 主战场）**、**方法区/元空间（类信息、常量、静态变量、JIT 代码缓存）**。
- **垃圾回收**：判断对象是否存活用**可达性分析**（从 GC Roots 出发不可达即回收），而非引用计数。常见算法：标记-清除、复制（新生代）、标记-整理（老年代）；分代收集（Young/Old）是主流。
- `OutOfMemoryError`：堆/元空间不足；`StackOverflowError`：栈深度超限（如无限递归）。

![JVM 运行时数据区、GC 分代与可达性分析](/java/java-jvm.svg)

#### 补 1.1 GC Roots 与分代回收流程

**可达性分析**：从 GC Roots 出发沿引用链向下搜索，走过的对象判为存活，未走到的判为可回收（不像引用计数那样无法处理循环引用）。GC Roots 主要包括：

| GC Roots 来源 | 例子 |
| --- | --- |
| 虚拟机栈（栈帧局部变量表） | 方法参数、局部变量引用的对象 |
| 方法区静态字段 / 常量 | `static Object cache`、`String` 常量池引用 |
| 本地方法栈 JNI 引用 | Native 代码持有的对象 |
| 被同步锁持有的对象 | `synchronized` 锁定的对象 |
| JVM 内部引用 | 系统类加载器、常驻异常对象、JMX Bean 等 |

```text
新对象 → Eden
  └─ Eden 满 → Minor GC：存活对象复制到 Survivor（S0/S1 来回倒），年龄 +1
       └─ 年龄达到阈值（默认 15）或 Survivor 放不下 → 晋升老年代
            └─ 老年代满 → Full GC（标记-整理/清除，STW 时间更长）
```

> 大对象可能**直接进老年代**（避免新生代反复复制）；`Minor GC` 频繁但快，`Full GC` 少但停顿长，调优目标就是减少 Full GC 次数与时长。

#### 补 1.2 常见收集器与 JVM 参数

| 收集器 | 代 | 特点 |
| --- | --- | --- |
| Serial / Serial Old | 新生代 / 老年代 | 单线程 STW，适合小内存客户端 |
| Parallel Scavenge / Parallel Old | 新 / 老 | 多线程并行，吞吐优先（JDK 8 默认） |
| CMS | 老年代 | 低停顿、并发标记清除，但产生碎片、有并发失败风险（JDK 9 起废弃，14 移除） |
| G1 | 整堆分区 Region | 可预测停顿、整体标记-整理（JDK 9+ 默认） |
| ZGC / Shenandoah | 整堆 | 并发整理，TB 级堆仍保持毫秒级停顿 |

| 常用参数 | 含义 |
| --- | --- |
| `-Xms` / `-Xmx` | 堆初始 / 最大值（生产建议设成相等，避免动态扩容抖动） |
| `-Xss` | 每线程栈大小（影响可创建线程数） |
| `-XX:MaxMetaspaceSize` | 元空间上限（不设则受本机内存限制） |
| `-XX:+UseG1GC` / `-XX:MaxGCPauseMillis=200` | 指定 G1 及停顿目标 |
| `-XX:+HeapDumpOnOutOfMemoryError` | OOM 时自动导出堆转储，配合 MAT / jmap / jstack 排查 |

#### 补 1.3 四种引用强度

| 类型 | 回收时机 | 典型用途 |
| --- | --- | --- |
| 强引用 `Object o = new Object()` | 永不回收（只要可达） | 普通对象 |
| 软引用 `SoftReference` | 内存不足时回收 | 内存敏感缓存 |
| 弱引用 `WeakReference` | 下次 GC 即回收 | `WeakHashMap`、`ThreadLocal` 的键 |
| 虚引用 `PhantomReference` | 随时，仅用于收到回收通知 | 堆外内存（DirectBuffer）清理 |

::: danger 易错 · ThreadLocal
`ThreadLocal` 的 Key 是**弱引用**，但 Value 是强引用；在线程池中线程长期不销毁，Key 被回收后 Value 仍挂在 `ThreadLocalMap` 里造成**内存泄漏**。使用完毕务必在 `finally` 中调用 `remove()`。
:::

### 补 2 枚举与注解（★★）
```java
enum Size { SMALL, MEDIUM, LARGE }          // 枚举是类，可加字段/方法
public @interface Author { String name(); }  // 自定义注解
```
- 枚举 `switch` 友好、类型安全，优于 `static final int` 常量。
- 注解 `@Override/@Deprecated/@FunctionalInterface/@SuppressWarnings` 由编译器或框架读取；可配合反射做配置（Spring 的 `@Component` 等）。

#### 补 2.1 枚举的完整用法

```java
enum Size {
    SMALL("S", 1), MEDIUM("M", 2), LARGE("L", 3);   // 常量必须写在最前面，构造器隐式 private
    private final String code;
    private final int level;
    Size(String code, int level) { this.code = code; this.level = level; }
    public String getCode() { return code; }
    public static Size of(String code) {
        for (Size s : values()) if (s.code.equals(code)) return s;
        throw new IllegalArgumentException("未知尺寸: " + code);
    }
}
System.out.println(Size.SMALL.ordinal());       // 0 —— 序号，不要依赖它做持久化
System.out.println(Size.valueOf("LARGE"));      // LARGE（名字严格匹配，否则 IllegalArgumentException）
System.out.println(Size.of("M").getCode());     // M
```

- 枚举本质是 `java.lang.Enum` 的子类，隐式 `public static final`、构造器私有、**不可被继承**，天然线程安全且单例，是实现单例模式的推荐方式之一。
- `values()` 返回全部常量数组；`EnumSet`（位向量实现，极高效）、`EnumMap`（数组实现）是枚举专用集合；`switch` 对枚举支持良好且编译器能检查覆盖情况。
- 用枚举替代 `static final int` 常量：类型安全、可读、可携带字段与方法、不会被传入任意整数。

#### 补 2.2 元注解与运行时读取

| 元注解 | 作用 |
| --- | --- |
| `@Retention` | 生命周期：`SOURCE`（编译期，如 `@Override`）/`CLASS`（字节码，默认）/`RUNTIME`（可被反射读取，框架用） |
| `@Target` | 可标注位置：`TYPE`、`FIELD`、`METHOD`、`PARAMETER`、`CONSTRUCTOR`、`ANNOTATION_TYPE` … |
| `@Documented` / `@Inherited` | 是否进 javadoc / 是否可被子类继承 |
| `@Repeatable` | 同一位置可重复标注多次 |

```java
@Retention(RetentionPolicy.RUNTIME)
@Target(ElementType.METHOD)
public @interface Timed { String value() default ""; }   // 注解成员只能是基本类型/String/Class/枚举/注解及其数组

class Job { @Timed("export") public void run() {} }
Timed t = Job.class.getMethod("run").getAnnotation(Timed.class);
System.out.println(t.value());       // export
```

> 注解本身**不改变程序语义**，必须有人（编译器、`javac` 插件、反射代码、框架）去"读"它才产生效果。

### 补 3 日期与时间 java.time（★★★）
旧 `Date`/`Calendar` 设计糟糕且线程不安全，Java 8 引入 `java.time`：
- `LocalDate` / `LocalTime` / `LocalDateTime`：无时区本地时间。
- `Instant`：时间线上的点（UTC）；`ZonedDateTime`：带时区。
- 不可变、线程安全；计算用 `plusDays/with` 等，格式化用 `DateTimeFormatter`。
```java
LocalDate d = LocalDate.of(2026, 1, 1);
LocalDate next = d.plusDays(31);
String s = d.format(DateTimeFormatter.ISO_DATE);
```

#### 补 3.1 类族速查与工作示例

| 类 | 含义 | 典型用途 |
| --- | --- | --- |
| `LocalDate` / `LocalTime` / `LocalDateTime` | 无时区的日期 / 时间 / 日期时间 | 生日、营业时间、本地日程 |
| `Instant` | 时间线上的一个瞬间（UTC，时间戳） | 日志、跨时区存储、与 `Date` 互转 |
| `ZonedDateTime` / `ZoneId` | 带时区的时间 | 国际化、跨时区排期 |
| `Duration` | **基于秒/纳秒**的时间量 | "耗时 3.5 秒"、超时 |
| `Period` | **基于年/月/日**的日期量 | "再过 2 个月零 3 天" |
| `DateTimeFormatter` | 格式化 / 解析 | 不可变、线程安全，可复用为 `static final` |
| `TemporalAdjusters` | 复杂日期调整 | 下个周一、月末、本年第一天 |

```java
LocalDate d = LocalDate.of(2026, 1, 1);
System.out.println(d);                                   // 2026-01-01
System.out.println(d.plusDays(31));                      // 2026-02-01（返回新对象，d 不变）
System.out.println(d.with(TemporalAdjusters.lastDayOfMonth())); // 2026-01-31
System.out.println(d.getDayOfWeek());                    // THURSDAY
System.out.println(Period.between(d, LocalDate.of(2026, 3, 5))); // P2M4D

DateTimeFormatter fmt = DateTimeFormatter.ofPattern("yyyy年MM月dd日 HH:mm");
System.out.println(LocalDateTime.of(2026, 11, 13, 17, 5).format(fmt)); // 2026年11月13日 17:05

Instant now = Instant.now();
java.util.Date old = java.util.Date.from(now);           // 新 → 旧
Instant back = old.toInstant();                          // 旧 → 新
```

::: danger 易错 · 日期时间
- `java.time` 对象**不可变**：`plusDays`、`with`、`minusMonths` 都返回新对象，忘记接收返回值是常见 bug（旧 `Calendar` 则是可变对象）。
- 月份从 **1** 开始（`Month.JANUARY.getValue() == 1`），而旧 `Calendar.MONTH` 从 0 开始；星期 `getDayOfWeek()` 返回枚举。
- 格式化模式 `yyyy`（日历年）与 `YYYY`（周历年）不同，跨年周可能出诡异结果；`MM` 是月、`mm` 是分、`HH` 是 24 小时制。
- `SimpleDateFormat` **线程不安全**，多线程请改用 `DateTimeFormatter`；带时区的存储优先用 `Instant` 或 ISO-8601 字符串，避免隐式依赖服务器默认时区。
:::

### 补 4 函数式数据处理 Stream API（★★★）
`Stream` 把集合变成"可链式计算的数据流"，延迟求值、可并行：
```java
List<String> result = words.stream()
    .filter(w -> w.length() > 3)     // 过滤
    .map(String::toUpperCase)        // 映射
    .sorted()                        // 排序
    .collect(Collectors.toList());   // 终止收集
long count = words.parallelStream()
    .filter(w -> w.startsWith("a")).count();
```
- 中间操作（filter/map/sorted 等）返回新 Stream、惰性；终止操作（collect/count/forEach）才触发计算。
- 注意 Stream **只能消费一次**；并行流 `parallelStream()` 适合大数据 CPU 密集计算，但须确保线程安全。

![Stream 流水线与惰性求值](/java/java-stream.svg)

#### 补 4.1 中间操作 / 终止操作一览

| 类别 | 常用 API | 是否惰性 | 返回 |
| --- | --- | --- | --- |
| 中间 | `filter`、`map`、`flatMap`、`distinct`、`sorted`、`peek`、`limit`、`skip`、`mapToInt` | ✔（`sorted`/`distinct` 为有状态，需见到全部元素） | `Stream<T>` |
| 终止 | `collect`、`forEach`、`count`、`reduce`、`min`、`max`、`findFirst`、`anyMatch`、`allMatch`、`noneMatch`、`toArray` | ✘（触发整个流水线） | 具体值 / 集合 / `Optional` |

#### 补 4.2 工作示例 · 分组、归约与 Optional

```java
record Order(String buyer, String category, int amount) {}
List<Order> orders = List.of(
    new Order("Ann", "book", 30), new Order("Bob", "book", 20),
    new Order("Ann", "food", 15), new Order("Bob", "food", 45));

int total = orders.stream().mapToInt(Order::amount).sum();          // 110
Map<String, Integer> byBuyer = orders.stream()
    .collect(Collectors.groupingBy(Order::buyer,
             Collectors.summingInt(Order::amount)));               // {Ann=45, Bob=65}
Map<Boolean, List<Order>> parts = orders.stream()
    .collect(Collectors.partitioningBy(o -> o.amount >= 30));      // 按条件分两组
String joined = orders.stream().map(Order::buyer).distinct()
                      .collect(Collectors.joining(", "));          // "Ann, Bob"
Optional<Order> top = orders.stream().max(Comparator.comparingInt(Order::amount));
System.out.println(top.orElseThrow().amount());                     // 45

// reduce 三参数形式（初始值 / 累加器 / 并行合并器）
int sum = orders.parallelStream().reduce(0, (acc, o) -> acc + o.amount, Integer::sum); // 110
```

::: danger 易错 · Stream
- **只能消费一次**：终止操作后再用同一 Stream 会抛 `IllegalStateException`；要复用请重新 `list.stream()`，或用 `Supplier<Stream<T>>`。
- 中间操作**无副作用**：不要在 `filter`/`map` 里修改外部集合或累加计数器（并行流会出错），归约请用 `reduce`/`collect`；`peek` 只用于调试。
- `parallelStream()` 默认共用 `ForkJoinPool.commonPool()`，IO 密集任务别用它；有状态/有序操作（`sorted`、`limit`）会削弱并行收益，小数据量反而更慢。
- `List.of(...)`、数组、`Files.lines(...)`、`Stream.iterate`、`Stream.generate` 都能作为数据源；`Files.lines` 返回的流持有文件句柄，**必须 try-with-resources 关闭**。
- `Optional` 用于表达"可能无结果"，优先 `orElse`/`orElseGet`/`orElseThrow`/`map`，不要无脑 `get()`。
:::

### 补 5 文件与 I/O（NIO.2）（★★★）
```java
Path path = Path.of("data.txt");
List<String> lines = Files.readAllLines(path);          // 读全部行
Files.writeString(path, "hello", StandardOpenOption.APPEND); // 写
try (Stream<String> s = Files.lines(path)) {            // 流式读，省内存（必须关闭）
    s.forEach(System.out::println);
}
```
- `java.nio.file.Path` / `Files` / `Paths` 是 NIO.2 现代 API，比老的 `File` 更强大（复制/移动/遍历/属性/监视）。
- 字节流 `InputStream/OutputStream`、字符流 `Reader/Writer`；缓冲流 `BufferedReader/Writer` 提升性能；`try-with-resources` 自动关闭（见第 7 章）。

![I/O 体系：字节流、字符流与 NIO.2](/java/java-io.svg)

#### 补 5.1 NIO.2 常用 API

| 操作 | 写法 |
| --- | --- |
| 构造路径 | `Path p = Path.of("data", "2026", "a.txt");` |
| 路径解析 | `p.resolve("b.txt")`、`p.getParent()`、`p.getFileName()`、`p.toAbsolutePath().normalize()` |
| 判存在 / 属性 | `Files.exists(p)`、`Files.isRegularFile(p)`、`Files.size(p)`、`Files.getLastModifiedTime(p)` |
| 读写（小文件） | `Files.readString(p, UTF_8)`、`Files.writeString(p, s, UTF_8)`、`Files.readAllLines(p)`、`Files.readAllBytes(p)` |
| 读写（大文件） | `Files.lines(p, UTF_8)`（须关闭流）、`Files.newBufferedReader` |
| 文件操作 | `Files.copy` / `move` / `delete` / `createDirectories` / `createTempFile` |
| 遍历 | `Files.walk(p)`（**必须关闭流**）、`Files.list(p)`、`Files.find(...)` |
| 监视 | `WatchService` 监听目录创建/修改/删除事件 |
| 文件系统 | `FileSystems.getDefault()`、`FileSystem`、ZIP 文件系统 provider |

#### 补 5.2 工作示例 · 统计目录下 Java 文件行数

```java
Path dir = Path.of("src");
try (Stream<Path> paths = Files.walk(dir)) {        // walk 返回的流持有目录句柄，必须关闭
    long total = paths.filter(Files::isRegularFile)
                      .filter(p -> p.toString().endsWith(".java"))
                      .mapToLong(p -> {
                          try { return Files.lines(p, StandardCharsets.UTF_8).count(); }
                          catch (IOException e) { return 0L; }
                      }).sum();
    System.out.println("Java 文件总行数：" + total);
}
```

#### 补 5.3 序列化与常见陷阱

```java
// 对象序列化：类需 implements Serializable，字段也要可序列化
class User implements Serializable {
    private static final long serialVersionUID = 1L;
    private final String name;
    private transient String password;              // transient 字段不参与序列化
    User(String name, String password) { this.name = name; this.password = password; }
}
try (ObjectOutputStream oos = new ObjectOutputStream(Files.newOutputStream(Path.of("u.bin")))) {
    oos.writeObject(new User("ann", "secret"));     // 反序列化后 password 为 null
}
```

::: danger 易错 · I/O
- **字符编码必须显式指定**：`new FileReader("a.txt")` 使用平台默认编码，换机器就可能乱码；一律用 `Files.newBufferedReader(p, StandardCharsets.UTF_8)` 或 `InputStreamReader(is, UTF_8)`。
- `read()` 返回的是**单个字节/字符的 int**，读到末尾返回 −1，别用 `while (in.read() != null)`；读数组要用三参数 `read(buf, off, len)` 并检查实际读取长度。
- 关闭缓冲流时会自动关闭其包裹的底层流；只关底层流则可能**丢失缓冲区里尚未 flush 的数据**。
- `Files.lines` / `Files.walk` 返回的 `Stream` 必须放在 try-with-resources 中，否则文件/目录句柄泄漏。
- 序列化要显式声明 `serialVersionUID`；`transient`/`static` 字段不参与；Java 原生序列化有安全与兼容问题，跨语言/长期存储优先用 JSON（Jackson/Gson）。
:::

### 补 6 equals 与 hashCode 契约精解（★★★）

![equals/hashCode 契约与 HashSet 查找过程](/java/java-equals.svg)

这是面试高频且极易写错的点：
1. **自反** `x.equals(x)` 为 true；
2. **对称** `x.equals(y) ⇔ y.equals(x)`；
3. **传递** `x=y, y=z ⇒ x=z`；
4. **一致** 比较所用字段不变则结果不变；
5. `x.equals(null)` 返回 false（不要用 `== null` 之外的方式，先 `instanceof` 判断）。
6. **若 `a.equals(b)` 为 true，则 `a.hashCode() == b.hashCode()` 必须成立**——因此**覆盖 `equals` 必须同时覆盖 `hashCode`**，否则对象在 `HashSet`/`HashMap` 中"找不到自己"。

```java
@Override public boolean equals(Object o) {
    if (this == o) return true;
    if (!(o instanceof Point p)) return false;   // 类型 + null 安全
    return x == p.x && y == p.y;
}
@Override public int hashCode() {
    return Objects.hash(x, y);                    // 用同一组字段
}
```

::: danger String 与包装类的设计要点
- `String` 不可变 + 常量池：线程安全、可作 HashMap 键；但频繁拼接请用 `StringBuilder`。
- `Integer` 等缓存 -128~127（见第 5 章）；比较值永远用 `equals`。
- `BigDecimal` 用 `compareTo` 比较数值（不用 `equals`，因 `equals` 还比精度标度）。
:::

#### 补 6.1 只重写 equals 会发生什么（工作示例）

```java
class Key {
    final int id;
    Key(int id) { this.id = id; }
    @Override public boolean equals(Object o) {            // 只重写 equals
        return o instanceof Key k && k.id == id;
    }
    // 故意不重写 hashCode → 使用 Object 的地址派生哈希
}
Set<Key> set = new HashSet<>();
Key a = new Key(1);
set.add(a);
System.out.println(a.equals(new Key(1)));     // true   —— 逻辑上相等
System.out.println(set.contains(new Key(1))); // false  —— 哈希码不同，落到别的桶
set.add(new Key(1));
System.out.println(set.size());               // 2      —— 两个「相等」对象同时存在
```

`HashSet.contains` / `HashMap.get` 是**先按 hashCode 定位桶，再在桶内用 equals 逐个比**。哈希码不一致时根本不会调用 `equals`，所以"相等却找不到"。补上 `@Override public int hashCode() { return Integer.hashCode(id); }` 后输出变为 `true / true / 1`。

**实现清单**：① 用 `@Override` 让编译器校验签名（参数是 `Object`，不是具体类型）；② `equals` 与 `hashCode` 必须用**同一组字段**；③ 引用字段用 `Objects.equals`，数组用 `Arrays.equals`/`deepEquals`，浮点用 `Double.compare`；④ `hashCode` 用 `Objects.hash(...)`；⑤ 参与比较的字段最好声明 `final`；⑥ 有继承时，`getClass()` 严格同类型能保对称但拒绝子类，`instanceof` 允许子类但要小心子类新增字段破坏对称性。

---

### 补 7 Java 8 → 21 常用新特性速览（★★）

| 版本 | 关键特性 |
| --- | --- |
| **8（LTS）** | lambda / 方法引用、Stream API、`Optional`、接口 `default`+`static` 方法、`java.time`、重复注解、`CompletableFuture`、Metaspace 取代永久代 |
| 9 | 模块系统 JPMS、`List.of/Set.of/Map.of` 不可变集合工厂、接口 `private` 方法、`jshell`、try-with-resources 可用已有 final 变量、`takeWhile/dropWhile` |
| 10 | `var` 局部变量类型推断、G1 并行 Full GC |
| **11（LTS）** | 标准化 HTTP Client、`String.strip/isBlank/lines/repeat`、`Files.readString/writeString`、单文件源码直接 `java Hello.java`、ZGC（实验） |
| 14 | `switch` 表达式正式（`->` + `yield`）、`instanceof` 模式匹配预览、`record` 预览、有用的 NPE 详细提示 |
| 15 | 文本块 `"""` 正式、密封类预览 |
| 16 | `record` 正式、`instanceof` 模式匹配正式、Stream `toList()` 前置 |
| **17（LTS）** | 密封类 `sealed` 正式、switch 模式匹配预览、强封装 JDK 内部 API、移除 CMS |
| 18–20 | 默认 UTF-8、虚拟线程 / 结构化并发（预览）、记录模式匹配、`SequencedCollection` 前置 |
| **21（LTS）** | **虚拟线程**（`Executors.newVirtualThreadPerTaskExecutor()`）正式、序列集合 `SequencedCollection`、switch 模式匹配与记录模式正式、分代 ZGC |

```java
// 几处最常用新语法速写
var list = new ArrayList<String>();                       // Java 10+
String json = """
    {"name": "ann", "age": 18}
    """;                                                 // Java 15+ 文本块
int days = switch (month) {                              // Java 14+ switch 表达式
    case 1, 3, 5, 7, 8, 10, 12 -> 31;
    case 2 -> 28;
    default -> 30;
};
if (obj instanceof String s && s.length() > 3) {          // Java 16+ 模式匹配，直接绑定变量
    System.out.println(s.toUpperCase());
}
sealed interface Shape permits Circle, Square {}         // Java 17+ 限制可实现的子类
```

> 版本选择：生产环境优先 LTS（8 / 11 / 17 / 21），升级前注意 `--release` 编译目标、第三方库兼容性与 GC 变化。虚拟线程适合**IO 密集**高并发（不是 CPU 密集），能大幅简化"每请求一线程"模型，但仍是协作式调度，别在虚拟线程里做长时间 `synchronized` 阻塞。

### 补 8 工程常用类库与工具（★★）

| 工具 / 类 | 作用 |
| --- | --- |
| `java.util.Objects` | `requireNonNull`（参数校验）、`equals` / `hash` / `deepEquals` / `toString`（null 安全） |
| `Optional<T>` | 表达"可能无值"，配合 `map/filter/orElse/orElseThrow`，避免 NPE；不要用作字段或集合元素 |
| `Pattern` / `Matcher` | 正则，`Pattern.compile` 可复用；`String.matches` 每次都重编译，循环中勿用 |
| `StringJoiner` / `Collectors.joining` | 带分隔符拼接 |
| JUnit 5 | `@Test`、`assertEquals`、`assertThrows`、`@BeforeEach`；断言优先用带 message 的重载 |
| Maven / Gradle | 依赖管理与构建生命周期；坐标 `groupId:artifactId:version`；注意依赖冲突与传递依赖 |
| SLF4J + Logback | 日志门面 + 实现，参数化日志，级别可动态调整 |
| JDK 诊断工具 | `javap`（字节码）、`jps`/`jstack`（线程栈/死锁）、`jmap`/`jconsole`/`jcmd`（堆与 GC）、`jshell`（快速验证） |

```java
// JUnit 5 最小示例
import static org.junit.jupiter.api.Assertions.*;
class CalculatorTest {
    @Test void divides() {
        assertEquals(2, 6 / 3);
        assertThrows(ArithmeticException.class, () -> 1 / 0);
    }
}
```

::: tip 一条工程经验
遇到"想不通的行为"时，`javap -c -p 类名` 看字节码往往比猜更快：自动装箱在哪发生、lambda 编译成什么、`i++` 的执行顺序、泛型擦除后的桥方法，都能一目了然。
:::

---

## 附录 A 公式与结论速查

| 主题 | 要点 |
| --- | --- |
| 基本类型位数 | byte 8 / short 16 / int 32 / long 64 / float 32 / double 64 / char 16 / boolean — |
| 字符串 | `==` 比地址、`equals` 比内容；字面量入常量池 |
| 自动装箱缓存 | Integer/Long/Short/Byte:-128~127；Character:0~127；Boolean:TRUE/FALSE；Float/Double 无 |
| 继承 | 单继承、多接口；覆盖方法签名一致、可见性不收窄；`@Override` 校验 |
| Object | `equals`+`hashCode` 须成对重写；`toString` 建议重写 |
| 接口默认方法冲突 | 实现类必须显式重写 |
| lambda | 仅函数式接口（单抽象方法）；捕获变量须 effectively final |
| 泛型擦除 | 运行时无泛型；不能用基本类型、不能 `new T`、不能 `instanceof List<String>` |
| PECS | Producer `extends`、Consumer `super` |
| 集合 | ArrayList 随机快、LinkedList 增删快；HashMap O(1)、TreeMap 有序 O(log n) |
| HashMap | 容量 2 的幂；`(n-1)&hash`；链表≥8 树化、≤6 退化；需正确 `equals/hashCode` |
| 异常 | RuntimeException 未检查、其余 Exception 已检查；捕获子类在前 |
| 并发 | `synchronized` 原子+可见；`volatile` 仅可见不原子；自增用 `AtomicInteger` |
| 线程安全集合 | `ConcurrentHashMap`、阻塞队列、`CopyOnWriteArrayList` |
| JVM 内存 | 堆+方法区（共享）、栈+PC+本地栈（私有）；GC 用可达性分析 |
| java.time | `LocalDate/LocalDateTime/Instant` 不可变线程安全；`DateTimeFormatter` 格式化 |
| Stream | 中间操作惰性、终止才触发；只能消费一次；`parallelStream` 可并行 |
| JDK / JRE / JVM | JDK ⊃ JRE ⊃ JVM；**字节码**跨平台，各平台 JVM 实现不同；解释 + JIT 混合执行 |
| 初始化顺序 | 父静态 → 子静态 → 父实例字段/块/构造 → 子实例字段/块/构造；构造器勿调可覆盖方法 |
| 参数传递 | 只有**值传递**：可改引用指向对象的内容，不能让外部变量改指向 |
| 动态绑定 | 仅可覆盖的实例方法；字段 / `static` / `private` / `final` 均为静态绑定 |
| 接口默认方法 | 类优先；多接口同名默认方法必须显式重写；可用 `X.super.m()` 选其一 |
| lambda | 捕获变量 effectively final；`this` 指向外围对象；仅可用于函数式接口 |
| 桥方法 | 擦除后父类与子类签名不一致时，编译器合成 `compareTo(Object)` 之类转发方法 |
| 泛型协变 | 泛型**不协变**（`List<String>` ≠ `List<Object>`）；数组协变但运行时用 `ArrayStoreException` 兜底 |
| HashMap | `hash=(h)^(h>>>16)`；`index=(n-1)&hash`；容量 2 的幂、负载因子 0.75；树化 8 且容量≥64、退化 6 |
| fail-fast | `modCount` 检测结构性修改；删除用 `Iterator.remove()` 或 `removeIf` |
| JMM | happens-before 六规则；`volatile` 可见 + 禁重排，**不保证复合操作原子性** |
| 线程池 | 核心线程 → 有界队列 → 最大线程 → 拒绝策略；`submit` 的异常封装在 `Future` 里 |
| GC | 可达性分析（非引用计数）、GC Roots、新生代 Eden+S0/S1 与老年代、G1 为 JDK 9+ 默认 |
| java.time | 全部不可变；月份从 1 开始；`DateTimeFormatter` 线程安全；`Instant` 适合存储 |
| NIO.2 | `Path`/`Files`；`walk`/`lines` 的流必须关闭；字符编码显式 UTF-8 |
| 新特性 | 8 lambda/Stream、11 HTTP Client、17 密封类、21 虚拟线程（均为 LTS） |

## 附录 B 各章易错点速查

1. `boolean` 不是 0/1，不能参与整数运算或 `if(x=0)`。
2. 浮点数禁止用 `==` 比较；金额用 `BigDecimal`。
3. 整数字面量超 int 须加 `L`；`long` 运算避免溢出。
4. `String` 不可变；`+` 循环拼接性能差，用 `StringBuilder`。
5. `==` 比引用、`equals` 比内容（字符串/包装/对象）。
6. 自动装箱 `-128~127` 缓存导致 `==` 表现"诡异"，一律用 `equals`。
7. 重写 `equals` 必须重写 `hashCode`，且用同一组字段。
8. 覆盖（override）≠ 重载（overload）：override 签名一致、静态方法不参与多态。
9. 多态调用看"实际对象类型"；向下转型前用 `instanceof`。
10. 接口默认方法冲突必须显式解决；接口无实例字段。
11. lambda 捕获变量须 effectively final；函数式接口只能一个抽象方法。
12. 泛型不能用基本类型、`new T`、`instanceof 泛型`；静态上下文不能用类型变量。
13. PECS：生产者 `extends`、消费者 `super`，否则编译或失去灵活性。
14. `ArrayList` 随机访问快、`LinkedList` 增删快但有遍历成本，别误用。
15. `HashMap` 的键须正确 `equals/hashCode`；容量为 2 的幂、树化阈值 8。
16. 遍历集合时删除要用 `Iterator.remove()`，不能直接 `list.remove()`（ConcurrentModificationException）。
17. 捕获异常子类在前、父类在后；优先用 try-with-resources 关闭资源。
18. 断言默认关闭，不能用于参数校验；用日志而非 `println`。
19. `synchronized` 锁对象要一致；`volatile` 不保证原子性，自增用原子类。
20. 不要 `new Thread` 裸用，用线程池 `ExecutorService`；`Future.get()` 会阻塞。
21. `stop()/suspend()` 已废弃；死锁靠固定加锁顺序避免。
22. `Stream` 只能消费一次；并行流注意线程安全。
23. 旧 `Date`/`Calendar` 线程不安全，改用 `java.time`。
24. `Files.readAllLines` 等 NIO.2 API 更现代；IO 资源务必关闭。
25. 一个 `.java` 最多一个 public 类，文件名须匹配；`main` 必须 `public static void String[]`。
26. `List.of/Set.of/Map.of` 返回**完全不可变**集合，`sort/add/remove` 抛 `UnsupportedOperationException`；`Arrays.asList` 只是固定大小（`set` 可、`add` 不可）。
27. 构造器里调用可覆盖方法，会在子类字段初始化之前执行，可能读到 0/null。
28. Java 只有值传递：`swap(a,b)` 永远无效；能改对象内容，不能改外部变量的指向。
29. 字段不参与多态，`static` 方法是"隐藏"；只有可覆盖实例方法才动态绑定。
30. 真实的 `Comparable<T>` 只有一个 `compareTo`；多个接口默认方法冲突时实现类必须显式重写。
31. lambda 的 `this` 指向**外围对象**，匿名内部类的 `this` 指向自身；捕获局部变量须 effectively final。
32. `finally` 里 `return` 会覆盖 `try/catch` 的返回值并吞掉异常，绝对禁止。
33. `wait/notify/notifyAll` 必须在持有该对象锁的 `synchronized` 块内调用；等待条件用 `while` 防虚假唤醒。
34. `try` 块内声明的资源在 `finally` 中超出作用域，且 `close()` 抛受检异常——优先 `try-with-resources`。
35. 泛型不协变；擦除导致 `f(List<String>)` 与 `f(List<Integer>)` 签名冲突，不能重载。
36. 遍历中结构性修改集合会抛 `ConcurrentModificationException`；`java.util.concurrent` 的迭代器是弱一致性。
37. `HashMap` 键参与比较的字段放入后不可变；只重写 `equals` 不重写 `hashCode` 会"存进去找不到"。
38. `BigDecimal` 用字符串构造、用 `compareTo` 比较数值；`new BigDecimal(0.1)` 会带入浮点误差。
39. `volatile` 不保证 `i++` 原子；`wait()` 释放锁而 `sleep()` 不释放；`notify()` 只唤醒一个。
40. `Executors.newFixedThreadPool/newCachedThreadPool` 可能 OOM；`submit()` 抛的异常要 `get()` 才会暴露。
41. `Files.lines`/`Files.walk` 返回的 `Stream` 必须 try-with-resources 关闭；`SimpleDateFormat` 线程不安全。
42. `ThreadLocal` 用完必须在 `finally` 中 `remove()`，否则线程池场景会内存泄漏。
43. `String.matches` 每次重编译正则；循环中改用预编译的 `Pattern`；`peek` 只用于调试，别做业务副作用。
44. `record` 是 `final` 且组件不可变，**不能把 record 组件声明为 `transient`**；访问器是 `x()` 而非 `getX()`。
45. 关闭缓冲流会连带关闭底层流，只关底层流则可能丢失未 flush 的数据；`Files.readAllLines` 不适合大文件。
