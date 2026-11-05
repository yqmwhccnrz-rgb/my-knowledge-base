# 第7章 字符串

## 7.1 字符数组与字符串

```c
char word[] = {'H', 'e', 'l', 'l', 'o', '!'};
```

| word[0] | word[1] | word[2] | word[3] | word[4] | word[5] |
| --- | --- | --- | --- | --- | --- |
| H | e | l | l | o | ! |

::: danger 易错点
这**不是 C 语言的字符串**，因为不能用字符串的方式做计算 —— 它缺少结尾的 0。
:::

**字符串**：以 0（整数 0）结尾的一串字符。

- `0` 或 `'\0'` 是一样的，但是和 `'0'`（字符 0）不同
- `0` 标志字符串的结束，但它不是字符串的一部分；计算字符串长度的时候不包含这个 0
- 字符串以数组的形式存在，以数组或指针的形式访问（更多的是以指针的形式）
- C 语言的字符串是以字符数组的形态存在的
- 不能对字符串用运算符做运算
- 通过数组的方式可以遍历字符串
- 唯一特殊的地方是字符串字面量可以用来初始化字符数组，以及标准库提供了一系列字符串函数（`string.h`）

::: warning 订正 · '\0' 与整数 0 的大小
原笔记写「`'\0'` 是一个字节，整数 `0` 是四个字节」。在 C 里，**字符常量 `'\0'` 的类型是 `int`**（通常 4 字节），并不是 `char`；只有把它存进 `char` 数组时，才按 `char` 占 1 字节。

准确的记法是：`'\0'` 与 `0` **值相等**（都是 0），`sizeof('\0') == sizeof(int)`，而 `sizeof(char) == 1`。字符串末尾那一个字节是 0，与 `'0'`（ASCII 48）完全不同。
:::

::: info 补充 · 字符串长度与数组长度
`char s[] = "hello";` 的数组长度是 **6**（5 个字符 + 1 个 `'\0'`），`strlen(s)` 是 **5**。`sizeof` 算存储空间，`strlen` 算到第一个 `'\0'` 之前的字符数，两者别混用。
:::

## 7.2 字符串常量与指针

```c
char *s = "Hello, world!";
```

`s` 是一个指针，初始化为指向一个字符串常量。由于这个常量所在的地方是**只读区域**，所以实际上应该是 `const char *s`；但由于历史原因，编译器接受不带 `const` 的写法。然而试图对 `s` 所指的字符串做写操作会导致严重的后果。

如果需要修改字符串，应该用数组：

```c
char s[] = "Hello, world!";
```

**指针还是数组？**

| | 含义 |
| --- | --- |
| `char *str = "Hello";` | 字符串常量，只读；`str` 可改指向 |
| `char word[] = "Hello";` | 在本地变量空间里复制了一份，可改内容；`word` 不可改指向 |

- 数组：这个字符串「在这里」（作为本地变量空间，自动被回收）
- 指针：这个字符串「不知道在哪」（处理参数、动态分配空间）
- 如果要**构造**一个字符串 → 数组；如果要**处理**一个字符串 → 指针

::: danger 订正 · 请写 const
`char *s = "Hello";` 在 C 里能编译，但 `s[0] = 'h';` 是**未定义行为**（多数平台直接段错误）。写成 `const char *s = "Hello";` 后，这类错误会在**编译期**被拦下。C++ 早已要求必须写 `const`，C 只是因为历史兼容才放行 —— 新代码一律加 `const`。
:::

## 7.3 字符串的输入输出

```c
char string[8];
scanf("%s", string);
printf("%s", string);
```

- `scanf` 读一个单词（到空格、tab 或回车为止）
- `scanf` 是**不安全**的，因为不知道要读的内容的长度（可能越界）

**安全的输入**：

```c
char string[8];
scanf("%7s", string);
```

在 `%` 和 `s` 之间的数字表示最多允许读的字符数量，这个数字应该比数组长度**小 1**（给结尾的 `'\0'` 留位置）。

::: info 补充 · 更推荐 fgets
`scanf("%s")` 有两个硬伤：遇空格就停、宽度必须手算且容易和数组长度不同步。更稳妥的是：

```c
char buf[128];
if (fgets(buf, sizeof buf, stdin) != NULL) {
    buf[strcspn(buf, "\n")] = '\0';   /* 去掉末尾换行 */
}
```

`fgets` 会把宽度和 `'\0'` 一起算好，并保留空格。注意它**会**把换行符读进来，所以要处理。
:::

**空字符串**：

```c
char buffer[100] = "";   /* 空字符串，buffer[0] == '\0' */
char buffer[] = "";      /* 这个数组的长度只有 1！只放得下结尾的 '\0' */
```

::: danger 易错点
```c
char *string;
scanf("%s", string);     /* 严重错误 */
```
以为 `char *` 就是「字符串类型」，定义了一个字符串类型的变量 `string` 就可以直接使用了。由于没有对 `string` 初始化为 0（没有指向任何有效空间），所以不一定每次运行都出错，但随时可能崩。指针必须先指向一块有效内存（数组、`malloc` 的结果）再写入。
:::

## 7.4 程序参数

```c
int main(int argc, char const *argv[])
```

- `argv[0]` 是命令本身
- 当使用 Unix 的符号链接时，反映的是符号链接的名字
- `argc` 是参数个数，`argv[argc]` 保证为 `NULL`

::: info 补充
`argc` / `argv` 的名字只是约定，可以改，但类型必须是 `int` 和 `char **` 等价形式。命令行参数都是**字符串**，要当数字用需要 `strtol`（比 `atoi` 好在能检测转换失败）。
:::

## 7.5 单字符输入输出

```c
int putchar(int c);   /* 向标准输出写一个字符；返回写了的字符，EOF(-1) 表示写失败 */
int getchar(void);    /* 从标准输入读一个字符 */
```

`getchar` 的返回类型是 `int` 而不是 `char`，是为了能返回 `EOF`（-1）。

输入结束标志：Windows → `Ctrl-Z`；Unix / macOS → `Ctrl-D`。

::: danger 补充 · 别用 char 接 getchar
```c
char c;
while ((c = getchar()) != EOF) { ... }   /* 可能死循环或提前结束 */
```
若 `char` 是无符号的，`EOF`(-1) 会被转成 255，永远不等于 `EOF`；若是有符号的，值为 0xFF 的合法字符会被误判为 `EOF`。**变量必须是 `int`**。
:::

## 7.6 字符串函数（string.h）

**strlen —— 求字符串长度**：

```c
size_t strlen(const char *s);
```

返回 `s` 的字符串长度（不包括结尾的 0）。

::: info 补充 · 返回值是 size_t
`strlen` 返回无符号的 `size_t`，写 `if (strlen(s) - 1 < 0)` 永远不会成立（会回绕成很大的正数）。另外 `strlen` 是 O(n)，在循环条件里反复调用会让算法退化成 O(n²)。
:::

**strcmp —— 比较两个字符串**：

```c
int strcmp(const char *s1, const char *s2);
```

原笔记写「返回：0 表示 s1 == s2；1 表示 s1 > s2；-1 表示 s1 < s2（教材简化说法）」，并在旁边补了一句说明标准实际规定返回 ASCII 差值。

::: warning 订正 · 只判断符号
标准只规定返回值是**负 / 0 / 正**，并不保证是 ±1。常见实现返回首个不同字符的差值（例如 `strcmp("b","a")` 可能返回 1，但 `strcmp("z","a")` 返回 25）。所以：

```c
if (strcmp(a, b) == 0)  { /* 相等 */ }
if (strcmp(a, b) > 0)   { /* a 更大 */ }
if (strcmp(a, b) == 1)  { /* 错：依赖具体实现 */ }
```

需要只比较前 n 个字符用 `strncmp`。
:::

**strcpy —— 拷贝字符串**：

```c
char *strcpy(char *restrict dst, const char *restrict src);
```

- 把 `src` 的字符串拷到 `dst`（**目的在前，源在后**）
- `restrict` 表明 `src` 和 `dst` 不重叠（C99）
- 返回 `dst`，为了能链起代码来
- 类似地还有 `strcat`（字符串拼接），同样是目的在前、源在后

复制一个字符串（先申请空间，再拷贝）：

```c
char *dst = (char *)malloc(strlen(src) + 1);
strcpy(dst, src);
```

::: tip 提示
申请 `strlen(src) + 1` 个字节而不是 `strlen(src)` —— 多出的 1 个字节放结尾的 `'\0'`。
:::

::: danger 补充 · strcpy / strcat 的溢出风险
这两个函数**不检查目标空间大小**，是历史上缓冲区溢出漏洞的主要来源。更安全的是 `snprintf(dst, sizeof dst, "%s", src)`，或在明确边界时用 `strncpy`（但它不保证补 `'\0'`，必须手动加）。`strncat` 的 n 参数是"还可追加的最大字符数"，也容易用错。
:::

**字符串中找字符**：

```c
char *strchr(const char *s, int c);    /* 从前往后找 */
char *strrchr(const char *s, int c);   /* 从后往前找 */
```

**字符串中找字符串**：

```c
char *strstr(const char *s1, const char *s2);
char *strcasestr(const char *s1, const char *s2);   /* 忽略大小写 */
```

返回 `NULL` 表示没有找到。

::: info 补充 · strcasestr 不是标准 C
`strcasestr` 来自 POSIX / GNU 扩展，MSVC 上没有，编译时要定义 `_GNU_SOURCE` 之类的宏。可移植做法是自己转小写后比较，或用平台对应的函数（Windows 上是 `_stristr`）。另外这些函数返回的指针指向**原字符串内部**，不要 `free`。
:::

<OriginalLink />
