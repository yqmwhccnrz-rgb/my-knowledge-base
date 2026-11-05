# 第8–9章 枚举与结构体

## 第8章 枚举

### 8.1 枚举的定义

枚举是一种用户定义的数据类型，用关键字 `enum` 按如下语法声明：

```c
enum 枚举类型名字 { 名字0, …, 名字n };
```

枚举类型名字通常并不真的使用，要的是括号里的名字，因为它们就是**常量符号**，类型是 `int`，值依次从 0 到 n：

```c
enum colors { red, yellow, green };
```

这就创建了三个常量，`red` 的值是 0，`yellow` 是 1，`green` 是 2。

当需要一些可以排列起来的常量值时，定义枚举的意义就是给这些常量值起了名字。

::: info 补充 · 枚举 vs `#define` vs `const`
`#define RED 0` 只是文本替换，没有类型、调试器里看不到名字；`const int RED = 0;` 在 C 里不是编译期常量（不能作 `case` 标签、不能定义数组长度）；枚举常量是真正的编译期整型常量，还能被调试器显示成 `red`。C23 起可以用 `enum color : unsigned char { ... };` 显式指定底层类型，节省空间。
:::

### 8.2 枚举的使用

```c
#include <stdio.h>

enum color { red, yellow, green };

void f(enum color c);

int main(void) {
    enum color t = red;
    scanf("%d", &t);
    f(t);
    return 0;
}

void f(enum color c) {
    printf("%d\n", c);
}
```

- 枚举量可以作为值
- 枚举类型可以跟上 `enum` 作为类型
- 但是实际上是以整数来做内部计算和外部输入输出

::: warning 订正 · 扫进枚举变量要小心
`scanf("%d", &t)` 要求 `t` 的底层类型恰好与 `int` 兼容。标准只保证枚举常量是 `int`，**枚举类型本身**的兼容整数类型由实现选择（虽然通常是 `int`）。更稳妥的做法是先读入 `int`，做范围校验后再赋给枚举变量。
:::

### 8.3 套路：自动计数的枚举

```c
enum COLOR { RED, YELLOW, GREEN, NumCOLORS };
```

最后那个名字 `NumCOLORS` 自动等于枚举量的个数（这里是 3）。这样需要遍历所有枚举量、或者需要建一个以枚举量做下标的数组的时候就很方便了：

```c
#include <stdio.h>

enum COLOR { RED, YELLOW, GREEN, NumCOLORS };

int main(int argc, char const *argv[]) {
    int color = -1;
    char *ColorNames[NumCOLORS] = { "red", "yellow", "green", };
    char *colorName = NULL;

    printf("输入你喜欢的颜色的代码：");
    scanf("%d", &color);

    if (color >= 0 && color < NumCOLORS) {
        colorName = ColorNames[color];
    } else {
        colorName = "unknown";
    }

    printf("你喜欢的颜色是%s\n", colorName);
    return 0;
}
```

::: tip 提示
这个套路的关键约定是：**计数项永远放最后、永远不显式赋值**。中间插入新枚举量时，`NumCOLORS` 会自动跟着变，数组长度和循环上界都不用手改。字符串数组建议写成 `const char *`，理由见第 7 章。
:::

### 8.4 枚举量指定值

声明枚举量时可以指定值：

```c
enum COLOR { RED = 1, YELLOW, GREEN = 5, NumCOLORS };
```

未指定值的名字是前一个值 + 1（所以 `YELLOW` 是 2，`NumCOLORS` 是 6）。

```c
#include <stdio.h>

enum COLOR { RED = 1, YELLOW, GREEN = 5, NumCOLORS };

int main(int argc, char const *argv[]) {
    printf("code for GREEN is %d\n", GREEN);
    return 0;
}
```

::: danger 易错点
枚举只是 int：即使给枚举类型的变量赋一个不存在的整数值，也没有任何 warning 或 error。（C23 起若指定了底层类型，超出范围的行为由实现定义。）所以**不要**把枚举当成「自动校验的有限集合」，边界检查仍要自己写 —— 上例中的 `if (color >= 0 && color < NumCOLORS)` 不能省。

另外注意：一旦中间手动指定了大数值（如 `GREEN = 5`），`NumCOLORS` 就不再等于**枚举个数**了（这里变成 6，但只有 3 个颜色）。「自动计数」套路要求**所有值都不显式指定**。
:::

### 8.5 小结

- 枚举类型可以当作类型使用，但是实际上很少需要这么用
- 如果有意义上排列的名字，枚举比 `const int` 方便
- 枚举比宏（macro）好，因为枚举有类型信息，调试时能看到名字

---

## 第9章 结构体

### 9.1 结构体的定义

结构体是用户定义的复合数据类型，把相关联的数据组合在一起：

```c
struct date {
    int year;
    int month;
    int day;
};
```

**匿名结构体**：定义时不写名字，仅当场定义变量（一次性使用）。

**`typedef` 起别名，简化使用**：

```c
typedef struct {
    int year;
    int month;
    int day;
} Date;
```

之后就可以直接写 `Date today;`。

::: info 补充 · struct 标签与 typedef 的区别
`struct date { ... };` 之后要写 `struct date today;`（C 里 `struct` 不能省）；`typedef` 之后写 `Date today;`。两者可以并存：

```c
typedef struct date { ... } Date;
```

需要在结构体内部引用自身（如链表节点）时，**必须**有标签：`typedef struct Node { struct Node *next; } Node;`，因为 typedef 的名字在定义完成前还不可用。
:::

### 9.2 结构体变量

- **结构体变量赋值**：同类型的结构体变量可以直接整体赋值（`today = other;`）
- **结构体嵌套**：结构体的成员可以是另一个结构体
- **访问结构体成员**：变量名 + `.` 来操作

```c
Date today;
today.year  = 2026;
today.month = 11;
```

如果是指针的话要用变量名 + `->` 来操作：

```c
Date *p = &today;
p->day = 4;          /* 等价于 (*p).day = 4; */
```

### 9.3 结构体与函数、数组、指针

- **结构体作为函数参数**：整体传值（会复制整个结构体）；结构体大的时候用指针传参更高效，只读时加 `const`
- **结构体数组**：

```c
Date dates[10];
dates[0].year = 2020;
```

- **结构体指针**：函数内通过 `->` 修改调用处的结构体

```c
void set_date(Date *p, int y, int m, int d) {
    p->year  = y;
    p->month = m;
    p->day   = d;
}
```

::: danger 补充 · 结构体不能用 == 比较
即使两个结构体所有成员都相等，`a == b` 也是**编译错误**（`==` 不支持结构体类型）。因为填充字节（padding）的内容不确定，标准也不打算逐字节比较。要自己写比较函数，或逐成员比较；同理也不能直接 `memcmp` 整个结构体。

赋值（`a = b`）倒是合法的，且会正确处理填充字节之外的所有成员。
:::

### 9.4 内存对齐

结构体在内存中的大小**不一定等于**各成员之和。编译器为了让访问速度更快，会让每个成员对齐到其类型大小的整数倍地址上（填充 padding 字节）。

::: tip 例题
```c
struct { char c; int i; };
```

在典型 32/64 位平台上大小是 **8** 而不是 5 —— `char` 之后填充了 3 个字节，让 `int` 对齐到 4 的整数倍地址。
:::

::: tip 提示
成员的排列顺序会影响结构体大小：把大的成员放前面通常更省空间。可以用 `sizeof` 查看实际大小。
:::

::: info 补充 · 对齐的实用工具
- `offsetof(struct S, member)`（`<stddef.h>`）能直接看某个成员的偏移，验证填充位置；
- `_Alignof(type)` / `alignof`（C11）查看类型对齐要求；
- `#pragma pack(1)` 或 `__attribute__((packed))` 可取消填充，但会导致**非对齐访问**，在部分架构上变慢甚至触发异常，主要用于与外部二进制格式/硬件寄存器严格对应时；
- 结构体末尾还可以放**柔性数组成员** `char data[];`（C99），配合一次 `malloc(sizeof(S) + n)` 分配，避免二次分配和指针间接访问。

注意：示例大小 8 是常见平台的结果，标准并不保证；请用 `sizeof` 实测，不要写死。
:::

<OriginalLink />
