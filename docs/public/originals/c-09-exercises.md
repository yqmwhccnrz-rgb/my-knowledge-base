# 附录 练习题

原笔记附录共 14 道经典题，覆盖循环、数组、函数与基本算法。下面保留原题思路与参考代码（PDF 文字层丢失的汉字已补全），并为每题补上容易忽略的边界条件或复杂度说明。

| 题号 | 题目 | 主要知识点 |
| --- | --- | --- |
| 1 | 找零计算器 | `while` 循环、`/` 和 `%` |
| 2 | 输出百以内的素数 | 嵌套循环、`break` |
| 3 | 输出前 50 个素数 | 计数器 + `while` |
| 4 | 凑硬币 | 穷举（多重循环） |
| 5 | 求和 | `for` 循环累加 |
| 6 | 整数的逆序输出 | 整数分解（`%10`、`/10`） |
| 7 | 整数正序输出 | 整数分解 + mask |
| 8 | 求最大公约数 | 辗转相除法 |
| 9 | 水仙花数 | 整数分解 |
| 10 | 九九乘法表 | 嵌套循环 |
| 11 | 统计素数并求和 | 素数判断 + 计数器 |
| 12 | 猜数字游戏（让计算机猜） | 二分查找 |
| 13 | 构造素数表 | 筛法（数组） |
| 14 | 井字棋 | 二维数组、函数 |

::: warning 订正 · 题目名称
PDF 里因文字层缺字，出现了「仙花数」「分查找」「最公约数」「99 乘法表」等标题。正确名称依次是**水仙花数**、**二分查找**、**最大公约数**、**九九乘法表**。下表已按正确名称列出。
:::

## 1. 找零计算器

**思路**：输入金额，按面额从大到小用贪心法计算各面额需要的张数（`/` 算张数、`%` 算余额）。

```c
#include <stdio.h>

int main() {
    int money, n, i;
    int faces[] = {100, 50, 20, 10, 5, 1};

    printf("请输入金额：");
    scanf("%d", &money);

    for (i = 0; i < 6; i++) {
        n = money / faces[i];
        money %= faces[i];
        if (n > 0) {
            printf("%d 元：%d 张\n", faces[i], n);
        }
    }
    return 0;
}
```

::: info 补充
贪心对人民币这类**规范面额系统**是最优的；若换成任意面额集合（如 `{1, 3, 4}`，凑 6），贪心会给出 4+1+1 而不是最优的 3+3，那时要用动态规划。另外应校验 `money >= 0`。
:::

## 2. 输出百以内的素数

**思路**：素数只能被 1 和自身整除。嵌套循环逐个判断 2~99 的每个数。

```c
#include <stdio.h>

int main() {
    int i, j, isPrime;
    for (i = 2; i < 100; i++) {
        isPrime = 1;
        for (j = 2; j < i; j++) {
            if (i % j == 0) { isPrime = 0; break; }
        }
        if (isPrime) { printf("%d ", i); }
    }
    return 0;
}
```

::: info 补充
内层只需试除到 `j * j <= i`，复杂度从 O(n²) 降到 O(n√n)。还可以跳过所有偶数。注意 `j * j` 在 `i` 很大时可能溢出，写成 `j <= i / j` 更稳。
:::

## 3. 输出前 50 个素数

**思路**：计数器统计已找到的素数个数，找满 50 个就停。

```c
#include <stdio.h>

int main() {
    int x = 2, cnt = 0, i, isPrime;
    while (cnt < 50) {
        isPrime = 1;
        for (i = 2; i < x; i++) {
            if (x % i == 0) { isPrime = 0; break; }
        }
        if (isPrime) { printf("%d ", x); cnt++; }
        x++;
    }
    return 0;
}
```

## 4. 凑硬币（一角、两角、五角凑出 10 元以下的金额）

**思路**：穷举五角和两角的个数，一角的个数由余额推算（单位统一为角，金额 < 100）。

```c
#include <stdio.h>

int main() {
    int amount;             /* 单位：角 */
    int x, y, z, count = 0;

    printf("请输入金额（角，10 元以下）：");
    scanf("%d", &amount);

    for (x = 0; x <= amount / 5; x++) {       /* 五角个数 */
        for (y = 0; y <= amount / 2; y++) {   /* 两角个数 */
            z = amount - 5 * x - 2 * y;       /* 剩余由一角补 */
            if (z >= 0) {
                printf("%d个五角 %d个两角 %d个一角\n", x, y, z);
                count++;
            }
        }
    }
    printf("共 %d 种凑法\n", count);
    return 0;
}
```

## 5. 求和

**思路**：循环累加，注意 `sum` 初始化为 0。

```c
#include <stdio.h>

int main() {
    int n, i, sum = 0;
    printf("请输入 n：");
    scanf("%d", &n);
    for (i = 1; i <= n; i++) { sum += i; }
    printf("1 到 %d 的和是 %d\n", n, sum);
    return 0;
}
```

::: info 补充
有闭式公式 `n * (n + 1) / 2`，复杂度 O(1)；但循环版也要防溢出：先除后乘（`n % 2 == 0 ? (n/2)*(n+1) : n*((n+1)/2)`）能撑到更大的 n。
:::

## 6. 整数的逆序输出

**思路**：反复 `%10` 取个位、`/10` 去个位，把取出的位接到结果尾部。

```c
#include <stdio.h>

int main() {
    int x, digit, ret = 0;
    printf("请输入一个整数：");
    scanf("%d", &x);
    while (x > 0) {
        digit = x % 10;
        ret = ret * 10 + digit;
        x /= 10;
    }
    printf("逆序为 %d\n", ret);
    return 0;
}
```

## 7. 整数正序输出（逐位分解）

**思路**：先构造最高位的 mask（10、100、…），再反复 `/mask` 取最高位、`%mask` 去掉最高位。

```c
#include <stdio.h>

int main() {
    int x, mask = 1, t;
    printf("请输入一个整数：");
    scanf("%d", &x);

    t = x;
    while (t > 9) {          /* 构造最高位的 mask */
        t /= 10;
        mask *= 10;
    }
    do {
        printf("%d", x / mask);
        if (mask > 9) printf(" ");
        x %= mask;
        mask /= 10;
    } while (mask > 0);

    return 0;
}
```

::: info 补充
`x = 0` 时 mask 保持 1，会正确输出 `0`；`x` 为负数时 `t > 9` 不成立，但 `x / mask` 为负，需要先取绝对值并处理 `INT_MIN`（其绝对值溢出）。
:::

## 8. 求最大公约数

**思路**：辗转相除法（欧几里得算法）：`gcd(a, b) = gcd(b, a % b)`，直到 b 为 0。

```c
#include <stdio.h>

int main() {
    int a, b, t;
    printf("请输入两个整数：");
    scanf("%d %d", &a, &b);
    while (b != 0) {
        t = a % b;
        a = b;
        b = t;
    }
    printf("最大公约数是 %d\n", a);
    return 0;
}
```

::: info 补充
复杂度 O(log min(a,b))。输入含 0 时也成立（`gcd(a, 0) = a`）；含负数时结果可能为负，先取绝对值更符合直觉。最小公倍数可用 `a / gcd * b`（先除后乘防溢出）。
:::

## 9. 水仙花数

**思路**：三位数等于其各位数字的**立方和**。分解出百位、十位、个位后判断。

```c
#include <stdio.h>

int main() {
    int i, a, b, c;
    for (i = 100; i <= 999; i++) {
        a = i / 100;         /* 百位 */
        b = i / 10 % 10;     /* 十位 */
        c = i % 10;          /* 个位 */
        if (a*a*a + b*b*b + c*c*c == i) {
            printf("%d\n", i);
        }
    }
    return 0;
}
```

::: info 补充
100~999 中共有 4 个：153、370、371、407。别和「各位数字之和」混淆 —— 那是判断能否被 3 整除的规则。
:::

## 10. 九九乘法表

**思路**：嵌套循环，外层控制行（1~9），内层控制列（1~行号）。

```c
#include <stdio.h>

int main() {
    int i, j;
    for (i = 1; i <= 9; i++) {
        for (j = 1; j <= i; j++) {
            printf("%d×%d=%d\t", j, i, i * j);
        }
        printf("\n");
    }
    return 0;
}
```

## 11. 统计素数并求和

**思路**：在 100~200 之间判断素数，是素数则计数并累加。判断时只需试除到 `j * j <= i`。

```c
#include <stdio.h>

int main() {
    int i, j, isPrime, count = 0, sum = 0;
    for (i = 100; i <= 200; i++) {
        isPrime = 1;
        for (j = 2; j * j <= i; j++) {
            if (i % j == 0) { isPrime = 0; break; }
        }
        if (isPrime) { count++; sum += i; }
    }
    printf("素数个数：%d，和：%d\n", count, sum);
    return 0;
}
```

## 12. 猜数字游戏（给出一个数字，让计算机猜）

**思路**：人在心中想一个 1~100 的数，计算机用**二分查找**猜，人回答「大了 / 小了 / 对了」。

```c
#include <stdio.h>

int main() {
    int low = 1, high = 100, mid;
    char ans;

    printf("请在心中想一个 1~100 的数，按回车开始\n");
    getchar();

    while (low <= high) {
        mid = (low + high) / 2;
        printf("我猜是 %d？(大了L / 小了S / 对了Y)：", mid);
        scanf(" %c", &ans);
        if (ans == 'Y' || ans == 'y') {
            printf("我猜中啦！\n"); return 0;
        } else if (ans == 'L' || ans == 'l') {
            high = mid - 1;         /* 猜大了 */
        } else {
            low = mid + 1;          /* 猜小了 */
        }
    }
    printf("不可能！你骗我！\n");
    return 0;
}
```

::: warning 订正 · 提示文字要和输出一致
原代码的提示只写 `L/S/对Y`，没说明 L、S 分别代表什么，很容易答反。上面把提示改成「大了 L / 小了 S」，与 `high = mid - 1`、`low = mid + 1` 的分支对应。另外 `scanf(" %c")` 中 `%c` **前面的空格不能删** —— 它用来吃掉上一次输入留下的换行符。

`mid = (low + high) / 2` 在 `low + high` 很大时可能溢出，通用写法是 `low + (high - low) / 2`。
:::

## 13. 构造素数表

**思路**：筛法（埃拉托斯特尼筛法）：把每个素数的倍数全部划掉，剩下的就是素数。

```c
#include <stdio.h>

int main() {
    const int n = 100;
    int prime[n + 1];       /* 0 表示是素数，1 表示被划掉 */
    int i, j;

    for (i = 0; i <= n; i++) { prime[i] = 0; }

    for (i = 2; i * i <= n; i++) {
        if (prime[i] == 0) {
            for (j = i * i; j <= n; j += i) {
                prime[j] = 1;
            }
        }
    }

    for (i = 2; i <= n; i++) {
        if (prime[i] == 0) { printf("%d ", i); }
    }
    return 0;
}
```

::: info 补充
复杂度 O(n log log n)，比逐个数试除快得多。`j` 从 `i * i` 开始是因为更小的倍数已被更小的素数划掉了。

注意 `const int n = 100;` 在 C 里**不是编译期常量**，`int prime[n+1]` 属于 VLA（C99 起支持，C11 起为可选特性，MSVC 不支持）。要兼容所有编译器，用 `#define N 100` 或 `enum { N = 100 };`，或直接 `malloc`。另外 0 和 1 不是素数，输出从 2 开始是对的。
:::

## 14. 井字棋

**思路**：用 3×3 二维数组存棋盘，双方轮流落子，每次落子后检查横、竖、对角线是否连成一条线。

```c
#include <stdio.h>

char board[3][3];       /* ' ' 空，'X'，'O' */

void init(void) {
    int i, j;
    for (i = 0; i < 3; i++)
        for (j = 0; j < 3; j++)
            board[i][j] = ' ';
}

void draw(void) {
    printf(" %c | %c | %c \n", board[0][0], board[0][1], board[0][2]);
    printf("---+---+---\n");
    printf(" %c | %c | %c \n", board[1][0], board[1][1], board[1][2]);
    printf("---+---+---\n");
    printf(" %c | %c | %c \n", board[2][0], board[2][1], board[2][2]);
}

int win(char c) {
    int i;
    for (i = 0; i < 3; i++) {
        if (board[i][0] == c && board[i][1] == c && board[i][2] == c) return 1;
        if (board[0][i] == c && board[1][i] == c && board[2][i] == c) return 1;
    }
    if (board[0][0] == c && board[1][1] == c && board[2][2] == c) return 1;
    if (board[0][2] == c && board[1][1] == c && board[2][0] == c) return 1;
    return 0;
}

int main(void) {
    int x, y, turn = 0;
    char c;

    init();
    draw();

    while (turn < 9) {
        c = (turn % 2 == 0) ? 'X' : 'O';
        printf("%c 落子，输入行列（0-2 0-2）：", c);
        scanf("%d %d", &x, &y);
        if (x < 0 || x > 2 || y < 0 || y > 2 || board[x][y] != ' ') {
            printf("无效位置，重新输入\n");
            continue;
        }
        board[x][y] = c;
        draw();
        if (win(c)) { printf("%c 获胜！\n", c); return 0; }
        turn++;
    }
    printf("平局！\n");
    return 0;
}
```

::: info 补充
`scanf("%d %d", &x, &y)` 若读到非法字符会返回 0，而 `x`、`y` 保持未初始化 —— 此时后面的越界判断也是不可靠的。应检查返回值并清空输入缓冲：

```c
if (scanf("%d %d", &x, &y) != 2) {
    while (getchar() != '\n') { }
    printf("请输入两个数字\n");
    continue;
}
```
:::

<OriginalLink />
