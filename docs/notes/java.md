---
summary: "Java 程序设计 精要笔记，全书 12 章覆盖 Java 核心语言与基础类库：Java 平台与开发环境、基本程序结构、对象与类、继承、接口与 lambda、异常与日志、泛型、集合框架、GUI 事件、Swing、并发；并补充 JVM 内存模型与 GC、枚举与注解、java.time、Stream API、NIO.2 文件 I/O、equals/hashCode 契约等进阶知识点。含 4 张自绘图（集合框架、异常体系、线程状态、JVM 内存）与大量代码示例、公式速查及易错点。"
---

# Java 程序设计笔记

::: info 笔记概要
- **所属课程**：Java 程序设计（计算机类 / 软件工程等专业核心基础课，及软件开发方向通用语言课）。
- **核心内容**：Java 以"一次编写、到处运行"的 JVM 平台 + 庞大类库著称。笔记按"语言基础 → 面向对象（类/继承/接口/泛型）→ 核心类库（集合/异常/IO/并发）→ 图形界面"主线展开，覆盖第 1–12 章；并在文末补充教材相对单薄、但工程必备的进阶主题（JVM 内存与 GC、枚举/注解、java.time、Stream、NIO.2、对象契约）。
- **学习建议**：Java 是"强类型 + 面向对象 + 自动内存管理"的语言，学习要抓住三条线——① 语法（类型/运算符/控制流/字符串）是否熟练；② 面向对象三要素（封装/继承/多态）与接口、泛型如何落地；③ 类库（集合、异常、并发、IO）的 API 与适用场景。本笔记在每个关键知识点都配了可运行的代码示例，并补充了教材未深入但易考易错的点（如自动装箱缓存范围、HashMap 底层、equals/hashCode 契约、PECS 通配符、线程安全集合等）。
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
| 补 | 进阶与补充 | JVM 内存/GC、枚举/注解、java.time、Stream、NIO.2、对象契约 | ★★★ |

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
- 文件读取：`Scanner new Scanner(Path.of("a.txt"))` 或 `Files.readAllLines(Path.of(...))`（详见补充五）。

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

---

## 第 5 章 继承

### 5.1 类、超类与子类（★★★）
```java
public class Manager extends Employee {      // is-a 关系
    private double bonus;
    @Override
    public double getSalary() {              // 覆盖（override）
        return super.getSalary() + bonus;    // super 调用父类方法
    }
}
```
- **覆盖规则**：子类方法签名须与父类一致；修饰符不能更严格（如父类 `public` 子类不能降为 `protected`）；`@Override` 注解让编译器帮你校验是否真在覆盖。
- **多态**：`Employee e = new Manager(); e.getSalary();` 运行时按**实际对象类型**调用 `Manager` 版本（动态绑定）。

::: danger 易错 · 继承与多态
- **静态方法不能被覆盖**，只会被隐藏（调用取决于编译期引用类型）。
- 子类**不能**访问父类的 `private` 成员，应通过 `protected` 或访问器。
- 强制类型转换 `Manager m = (Manager) e;` 前务必用 `instanceof` 判断，否则 `ClassCastException`：
  `if (e instanceof Manager m) { ... }`（模式匹配，Java 16+ 可直接绑定变量）。
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

---

## 第 6 章 接口、lambda 表达式与内部类

### 6.1 接口（★★★）
接口是**一组公开方法签名**的契约，Java 8 后可有默认/静态/私有方法。
```java
public interface Comparable<T> {
    int compareTo(T other);          // 抽象方法
    default void log() { ... }       // 默认方法（实现类可不重写）
    static Comparable<?> of() { ... }// 静态方法
}
```
- 类用 `implements` 实现接口，可实现多个（弥补单继承不足）。
- **接口 vs 抽象类**：接口无状态（不能有实例字段，Java 9+ 允许 `private` 方法但无字段），一个类只能继承一个类但可实现多个接口。
- **默认方法冲突**：类同时继承的多个接口有同名默认方法时，必须在该类中**显式重写**以消除歧义（`接口.super.方法()` 选择其一）。
- **克隆**：`Cloneable` 是"标记接口"（无方法），仅作信号。

### 6.2 lambda 表达式与函数式接口（★★★）
lambda 是"可传递的代码块"，用于简化仅有一个抽象方法的**函数式接口**。
```java
List<String> names = List.of("Bob", "Alice", "Carol");
names.sort((a, b) -> a.compareTo(b));            // lambda
names.sort(Comparator.comparing(String::length)); // 方法引用
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

---

## 第 7 章 异常、断言、日志与调试

### 7.1 异常分类（★★★）
异常层次见下图（`Throwable` 为根）：

![Java 异常体系](/java/java-exceptions.svg)

- **Error**：系统级严重错误（如 `OutOfMemoryError`），不应也不应捕获。
- **Exception**：
  - **RuntimeException（未检查）**：代码逻辑错误导致（空指针、越界、类型转换、除零），编译器**不强制**处理，应通过改代码避免。
  - **其他 Exception（已检查/checked）**：如 `IOException`，编译器**强制** `try-catch` 或 `throws` 声明。

### 7.2 捕获与处理（★★★）
```java
try {
    FileInputStream in = new FileInputStream("a.txt");
    // ...
} catch (FileNotFoundException e) {        // 子类异常在前
    e.printStackTrace();
} catch (IOException e) {                 // 父类在后
    logger.log(Level.SEVERE, "read failed", e);
} finally {
    in.close();                           // 无论是否异常都执行（释放资源）
}
```
- **捕获顺序**：子类必须写在父类之前。
- **try-with-resources**（推荐）：资源实现 `AutoCloseable`，自动关闭，无需 `finally`：
```java
try (BufferedReader br = Files.newBufferedReader(Path.of("a.txt"))) {
    return br.readLine();
} catch (IOException e) { ... }   // 异常自动关闭后抛出
```
- **异常链**：`throw new RuntimeException("包装", cause);` 用 `getCause()` 追溯根因。

### 7.3 断言与日志（★★）
- `assert cond : "message";` 用于**内部不变量**检查，生产环境默认关闭（`-ea` 开启），不可用于参数校验（用户可关）。
- 日志用 `java.util.logging`（JUL）或 Log4j/SLF4J；比 `System.out.println` 更可控（级别、处理器、格式器、可关闭）。

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
    private T first; private U second;
    public <V> V merge(V v) { ... }      // 泛型方法
}
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

---

## 补充与进阶（教材相对单薄、工程必备）

### 补 1 JVM 内存模型与垃圾回收（★★★）
JVM 运行时数据区结构见下图：

![JVM 运行时数据区](/java/java-jvm.svg)

- **线程私有**：程序计数器、虚拟机栈（栈帧=方法调用）、本地方法栈。
- **线程共享**：**堆（对象实例，GC 主战场）**、**方法区/元空间（类信息、常量、静态变量、JIT 代码缓存）**。
- **垃圾回收**：判断对象是否存活用**可达性分析**（从 GC Roots 出发不可达即回收），而非引用计数。常见算法：标记-清除、复制（新生代）、标记-整理（老年代）；分代收集（Young/Old）是主流。
- `OutOfMemoryError`：堆/元空间不足；`StackOverflowError`：栈深度超限（如无限递归）。

### 补 2 枚举与注解（★★）
```java
enum Size { SMALL, MEDIUM, LARGE }          // 枚举是类，可加字段/方法
public @interface Author { String name(); }  // 自定义注解
```
- 枚举 `switch` 友好、类型安全，优于 `static final int` 常量。
- 注解 `@Override/@Deprecated/@FunctionalInterface/@SuppressWarnings` 由编译器或框架读取；可配合反射做配置（Spring 的 `@Component` 等）。

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

### 补 5 文件与 I/O（NIO.2）（★★★）
```java
Path path = Path.of("data.txt");
List<String> lines = Files.readAllLines(path);          // 读全部行
Files.writeString(path, "hello", StandardOpenOption.APPEND); // 写
try (Stream<String> s = Files.lines(path)) { ... }      // 流式读，省内存
```
- `java.nio.file.Path` / `Files` / `Paths` 是 NIO.2 现代 API，比老的 `File` 更强大（复制/移动/遍历/属性/监视）。
- 字节流 `InputStream/OutputStream`、字符流 `Reader/Writer`；缓冲流 `BufferedReader/Writer` 提升性能；`try-with-resources` 自动关闭（见第 7 章）。

### 补 6 equals 与 hashCode 契约精解（★★★）
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
