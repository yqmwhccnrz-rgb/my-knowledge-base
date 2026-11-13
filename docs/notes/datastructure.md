---
summary: "数据结构与算法 精要笔记，共 9 章：覆盖数据结构（线性表、栈与队列、串、数组与广义表、树与二叉树、图、查找、排序）与算法设计（分治、贪心、回溯、分支限界、动态规划）两大部分，并补充红黑树等自平衡结构。含关键算法 C 代码、工作示例、对比表、6 张自绘图（二叉树遍历、图、AVL 旋转、B-树、哈希、算法范式）、公式速查与易错点。"
---

# 数据结构笔记（C语言版）

::: info 笔记概要
- **所属课程**：数据结构与算法（计算机类 / 软件类专业核心基础课）。
- **核心内容**：数据结构＝逻辑结构 × 存储结构 × 运算。三大逻辑结构（线性／树形／图状）覆盖第 2–6 章，再叠加查找（第 7 章）与排序（第 8 章）两大主题；第 1 章给出数据、抽象数据类型（ADT）与算法复杂度的方法论；第 9 章系统梳理五大算法设计范式（分治／贪心／回溯／分支限界／动态规划）以及红黑树等自平衡查找结构。
- **学习建议**：每条"定义—存储表示—基本运算实现—时间／空间复杂度"都要能默写；算法以 C 语言描述，重点在"为什么这么存、这么算，复杂度是多少"。本笔记在通读教材基础上补充了**关键算法的完整 C 代码**、**工作示例**、**AVL 四种旋转判别**、**B/B+ 树区别**、**哈希装填因子分析**、**各排序稳定性与适用场景对照**，以及第 9 章五大算法设计范式和红黑树等自平衡结构，并修正了若干易混表述。
:::

## 全书目录

| 章 | 主题 | 核心考点 | 重要度 |
| --- | --- | --- | --- |
| 1 | 绪论 | 数据／数据结构／ADT 概念；算法 5 特性；时间／空间复杂度与 O 记号 | ★ 客观题 |
| 2 | 线性表 | 顺序表与单链表（增删查）、循环／双向链表、有序表合并 | ★★★ |
| 3 | 栈和队列 | 顺序栈／链栈、递归与栈、循环队列（队满判据）、链队、应用（数制转换／表达式求值／括号匹配） | ★★★ |
| 4 | 串、数组和广义表 | 串的模式匹配（BF/KMP 含 next 手算）、数组压缩存储、广义表 | ★★★ |
| 5 | 树和二叉树 | 二叉树 5 性质、遍历与恢复、线索化、哈夫曼树（含构造代码与 WPL 例题） | ★★★ |
| 6 | 图 | 邻接矩阵／邻接表、DFS/BFS（含代码）、最小生成树、最短路径、拓扑排序、关键路径 | ★★★ |
| 7 | 查找 | 折半／BST（含增删代码）／AVL／B-树／B+树／散列表（含代码与 ASL 表） | ★★★ |
| 8 | 排序 | 插／交／选／并／基 5 类排序（含 7 段完整代码）、内外部排序、复杂度与稳定性 | ★★★ |
| 9 | 算法设计与分析 | 分治（主定理）、贪心（选择性质）、回溯、分支限界、动态规划；红黑树 | ★★★ |

---

## 第 1 章 绪论

### 1.1 数据结构的研究内容（★）
程序＝算法＋数据结构（Wirth）。数据结构研究"数据的逻辑结构、存储结构以及在其上定义的运算"，它介于数学、计算机硬件与软件之间，是核心基础课。

### 1.2 基本概念和术语（★★）

| 术语 | 含义 |
| --- | --- |
| 数据 Data | 能被计算机处理的一切符号的总称 |
| 数据元素 | 数据的基本单位，作为一个整体处理（又称元素、记录、结点） |
| 数据项 | 不可分割的最小单位（如学号、姓名） |
| 数据对象 | 性质相同的数据元素集合（数据的子集） |
| 数据结构 | 相互之间存在一种或多种特定关系的数据元素集合 |

数据结构包含**逻辑结构**与**存储结构**两个层次：

- 逻辑结构（与存储无关，是数学模型）：① 集合 ② 线性结构 ③ 树形结构 ④ 图状／网状结构。
- 存储结构（物理结构）：① 顺序存储 ② 链式存储 ③ 索引存储 ④ 散列存储。

::: tip 逻辑结构 vs 存储结构
逻辑结构回答"数据之间是什么关系"，存储结构回答"这些关系在计算机里怎么放"。同一种逻辑结构（如线性表）可以有顺序、链式等多种存储结构。
:::

### 1.3 抽象数据类型 ADT（★★）
ADT ＝ 数据对象 ＋ 数据关系 ＋ 基本操作集。定义时只规定"做什么"（接口），不规定"怎么做"（实现），实现依赖于具体存储结构。

### 1.4 算法和算法分析（★★★）
算法是解决某类问题的有限长操作序列，具备五大特性：**有穷性、确定性、可行性、输入（0 个或多个）、输出（1 个或多个）**。

评价标准：正确性、可读性、健壮性、高效性（时间 ＋ 空间）。

**时间复杂度**：用 O 记号描述渐近时间复杂度 `T(n) = O(f(n))`，表示随问题规模 n 增大，执行时间的增长率与 f(n) 相同。计算步骤：找基本语句 → 算其频度 f(n) → 取数量级 `O(f(n))`。多项式取最高次幂、忽略系数（定理 1.1）。

常见数量级（由快到慢）：`O(1)` → `O(log n)` → `O(n)` → `O(n log n)` → `O(n²)` → `O(n³)` → `O(2ⁿ)`。**指数阶 O(2ⁿ) 效率极低，n 稍大即不可用**，应优选多项式阶。

最好／最坏／平均时间复杂度：除特别说明，本笔记与教材讨论的均为**最坏情况**时间复杂度（执行时间上界）。

**空间复杂度** `S(n) = O(f(n))`。若辅助空间与输入规模无关（为常数），称算法**原地工作**，辅助空间 `O(1)`。

::: danger 易错 · 复杂度
- 复杂度看的是"增长率"，不是具体步数；常量再大也是 `O(1)`（如固定 10000 次循环仍是 `O(1)`）。
- `O(log n)` 中的 log 默认以 2 为底（对数阶循环常见写法 `i = i * 2`，频度 ≈ log₂n）。
- 嵌套循环复杂度由**最深层基本语句**的频度决定，不是简单相乘各层上限（注意 `for j=1..i` 这类依赖外层变量的循环，如 `Σi·Σj` 实际为 `O(n³)` 而非 `O(n²)`）。

**工作示例**：下面这段代码的复杂度是 `O(n²)` 还是 `O(n³)`？
```c
for (i = 1; i <= n; i++)
    for (j = 1; j <= i; j++)
        x++;
```
基本语句 `x++` 的频度 `Σ_{i=1}^{n} Σ_{j=1}^{i} 1 = Σ i = n(n+1)/2`，故为 `O(n²)`（内循环上界依赖 `i`，不是独立的 `n`）。若写成 `for j=1..n` 才是 `O(n²)` 的两倍仍 `O(n²)`；若再加一层 `for k=1..j` 则频度为 `O(n³)`。
:::

---

## 第 2 章 线性表

### 2.1 定义与特点（★★）
线性表是 n 个数据元素的有限序列，元素间是**一对一**的线性关系（除首元无前驱、末元无后继外，其余各有唯一前驱与后继）。

### 2.2 顺序存储——顺序表（★★★）
用一组地址连续的存储单元依次存放。第 i 个元素地址：`LOC(aᵢ) = LOC(a₁) + (i−1)×L`（L 为元素字节数）。
- **插入**：平均移动 n/2 个元素，时间复杂度 `O(n)`。
- **删除**：平均移动 (n−1)/2 个元素，时间复杂度 `O(n)`。
- 随机存取 `O(1)`；但插入／删除需大量移动，且需预先分配空间（溢出或浪费）。

**关键算法（顺序表取值、插入、删除）**：
```c
// 取值：O(1)
Status GetElem(SqList L, int i, ElemType &e) {
    if (i < 1 || i > L.length) return ERROR;  // 位置合法性
    e = L.elem[i - 1];                         // 第 i 个存于 elem[i-1]
    return OK;
}

// 按值查找：O(n)，平均 ASL ≈ (n+1)/2
int LocateElem(SqList L, ElemType e) {
    for (int i = 0; i < L.length; i++)
        if (L.elem[i] == e) return i + 1;       // 查找成功返回序号
    return 0;                                   // 失败返回 0
}

// 插入：平均移动 n/2，O(n)
Status ListInsert(SqList &L, int i, ElemType e) {
    if (i < 1 || i > L.length + 1) return ERROR; // 合法范围 1..L.length+1
    if (L.length == MAXSIZE) return ERROR;        // 已满
    for (int j = L.length - 1; j >= i - 1; j--)
        L.elem[j + 1] = L.elem[j];               // 后移
    L.elem[i - 1] = e;
    ++L.length;
    return OK;
}

// 删除：平均移动 (n-1)/2，O(n)
Status ListDelete(SqList &L, int i) {
    if (i < 1 || i > L.length) return ERROR;
    for (int j = i; j <= L.length - 1; j++)
        L.elem[j - 1] = L.elem[j];               // 前移
    --L.length;
    return OK;
}
```

::: tip 工作示例 · 顺序表插入
在长度为 8 的表中第 5 个位置插入 25：需把第 5～8 个元素依次后移一位，再将 25 放入第 5 位，表长变为 9。当 `i = n+1`（表尾插入）时无需移动，所以最坏情况是 `i=1`（移 n 个），最好情况是 `i=n+1`（移 0 个），**平均移动 n/2**。
:::

### 2.3 链式存储——单链表（★★★）
结点 ＝ 数据域 ＋ 指针域。引入**头结点**（位于首元结点之前，其指针指向首元）可统一空表与非空表的处理。
- **头指针**始终指向链表第一个结点（有头结点时即指向头结点）；**首元结点**是第一个数据结点。
- 按值查找 `O(n)`；插入／删除**只需修改指针、不移动元素**，但需先定位前驱 `O(n)`。

**关键算法（单链表取/查/插/删/建表）**：
```c
// 按值查找：O(n)
LNode *LocateElem(LinkList L, ElemType e) {
    p = L->next;
    while (p && p->data != e) p = p->next;
    return p;   // 成功返回结点地址，失败返回 NULL
}

// 在第 i 个位置插入 e：O(n)（找前驱占主导）
Status ListInsert(LinkList &L, int i, ElemType e) {
    p = L; j = 0;
    while (p && j < i - 1) { p = p->next; ++j; }  // 找第 i-1 个结点
    if (!p || j > i - 1) return ERROR;             // i>n+1 或 i<1
    s = new LNode; s->data = e;
    s->next = p->next; p->next = s;                // 先接后继，再改前驱
    return OK;
}

// 删除第 i 个结点：O(n)
Status ListDelete(LinkList &L, int i) {
    p = L; j = 0;
    while (p->next && j < i - 1) { p = p->next; ++j; }
    if (!(p->next) || j > i - 1) return ERROR;
    q = p->next; p->next = q->next;                // 跳过并释放
    delete q;
    return OK;
}

// 前插法建表（逆位序输入）：O(n)
void CreateList_H(LinkList &L, int n) {
    L = new LNode; L->next = NULL;
    for (int i = 0; i < n; i++) {
        p = new LNode; cin >> p->data;
        p->next = L->next; L->next = p;            // 头插
    }
}

// 后插法建表（正位序输入）：O(n)
void CreateList_R(LinkList &L, int n) {
    L = new LNode; L->next = NULL; r = L;
    for (int i = 0; i < n; i++) {
        p = new LNode; cin >> p->data; p->next = NULL;
        r->next = p; r = p;                        // 尾插
    }
}
```

::: danger 易错 · 指针修改顺序（单链表插入）
在 p 之后插入 s，必须 **先** `s->next = p->next;` **后** `p->next = s;`。若颠倒会丢失 p 的后继链。删除 p 的后继 q：`p->next = q->next;` 后再 `free/delete q`。
:::

### 2.4 单链表与顺序表比较

| 比较项 | 顺序表 | 单链表 |
| --- | --- | --- |
| 存取 | 随机 `O(1)` | 顺序 `O(n)` |
| 插入／删除 | `O(n)`（移动） | 找前驱 `O(n)` ＋ 改链 `O(1)` |
| 空间 | 预分配、可能浪费／溢出 | 动态、每结点多指针域 |
| 适用 | 频繁查、表长稳定 | 频繁增删、表长变化大 |

### 2.5 其他链表（★★）
- **循环链表**：表尾指针指向头结点，从任一结点可遍历全表；判空为 `rear->next == head`。
- **双向链表**：结点含 `prior` 与 `next`，删除／插入需同时修改两个方向的指针（共 4 步指针操作），便于"向上／向下"双向遍历。
  ```c
  // 双链表插入（在 p 前/后）：注意 4 步指针修改顺序
  Status ListInsert_DuL(DuLinkList &L, int i, ElemType e) {
      if (!(p = GetElem_DuL(L, i))) return ERROR;   // p 指向第 i 个
      s = new DuLNode; s->data = e;
      s->prior = p->prior; s->next = p;
      p->prior->next = s; p->prior = s;             // 先接前驱侧，再接 p
      return OK;
  }
  ```

### 2.6 有序表合并（★★★）
将两个**有序**顺序表合并为一个有序表（归并，`O(n+m)`）；以及一元多项式相加（链表按指数有序）。

```c
// 有序顺序表归并：O(n+m)，空间 O(n)
void MergeList_Sq(SqList LA, SqList LB, SqList &LC) {
    LC.length = LA.length + LB.length;
    LC.elem = new ElemType[LC.length];
    i = 0; j = 0; k = 0;
    while (i < LA.length && j < LB.length) {
        if (LA.elem[i] <= LB.elem[j]) LC.elem[k++] = LA.elem[i++];
        else LC.elem[k++] = LB.elem[j++];
    }
    while (i < LA.length) LC.elem[k++] = LA.elem[i++];
    while (j < LB.length) LC.elem[k++] = LB.elem[j++];
}
```

::: tip 顺序表合并
归并两个有序表时，谁小先取谁，指针各推进；时间 `O(n+m)`、空间 `O(n+m)`（新表）。这是后面"归并排序"的微观版本。
:::

---

## 第 3 章 栈和队列

### 3.1 定义和特点（★★★）
- **栈 Stack**：只允许在一端（栈顶）插入删除的线性表，**LIFO**（后进先出）。
- **队列 Queue**：只允许在一端（队尾）插入、另一端（队头）删除，**FIFO**（先进先出）。

### 3.2 栈的表示与实现（★★★）
- 顺序栈：用数组，`top` 指向栈顶；判空 `top==base`，上溢 `top-base==stacksize`。
- 链栈：链表头作栈顶，无栈满问题。
- **共享栈**：两个栈底分别在数组两端，向中间增长，提高空间利用率。

**关键算法（顺序栈、链栈）**：
```c
// 顺序栈入栈/出栈
Status Push(SqStack &S, SElemType e) {
    if (S.top - S.base == S.stacksize) return ERROR;  // 栈满
    *S.top++ = e;
    return OK;
}
Status Pop(SqStack &S, SElemType &e) {
    if (S.top == S.base) return ERROR;                // 栈空
    e = *--S.top;
    return OK;
}

// 链栈入栈（链表头为栈顶，无需判满）
Status Push(LinkStack &S, SElemType e) {
    p = new StackNode; p->data = e;
    p->next = S; S = p;                               // 头插即入栈
    return OK;
}
```

### 3.3 栈与递归（★★★）
递归本质是利用**系统栈（递归工作栈）**保存每层调用的返回地址、局部变量等。可借助栈将递归改写为非递归（阶乘、斐波那契、汉诺塔）。
- 优缺点：递归代码简洁但时空开销大（栈帧）；非递归效率高但实现复杂。

### 3.4 队列的表示与实现（★★★）
- **循环队列（顺序）**：克服"假溢出"。约定：队空 `front==rear`；**队满 `(rear+1)%MAX == front`**；元素个数 `(rear - front + MAX) % MAX`。常牺牲一个单元区分空满，或用 `tag`／计数字段。
- **链队**：队头指针 `front`、队尾指针 `rear`；入队改 `rear`，出队改 `front->next`；判空 `front==rear`。

**关键算法（循环队列、链队）**：
```c
// 循环队列入队/出队：O(1)
Status EnQueue(SqQueue &Q, QElemType e) {
    if ((Q.rear + 1) % MAXQSIZE == Q.front) return ERROR; // 队满（牺牲一单元）
    Q.base[Q.rear] = e;
    Q.rear = (Q.rear + 1) % MAXQSIZE;
    return OK;
}
Status DeQueue(SqQueue &Q, QElemType &e) {
    if (Q.front == Q.rear) return ERROR;                  // 队空
    e = Q.base[Q.front];
    Q.front = (Q.front + 1) % MAXQSIZE;
    return OK;
}

// 链队出队：注意删最后一个元素时要重置 rear 指向头结点
Status DeQueue(LinkQueue &Q, QElemType &e) {
    if (Q.front == Q.rear) return ERROR;
    p = Q.front->next; e = p->data;
    Q.front->next = p->next;
    if (Q.rear == p) Q.rear = Q.front;     // 最后一个元素被删，rear 回指头结点
    delete p;
    return OK;
}
```

::: danger 易错 · 循环队列
- 循环队列"队满"不能用 `rear==front` 判（与队空冲突），必须牺牲一个单元或用 `tag`／计数。
- `rear` 通常指向"队尾元素的下一个空位"（常用约定），不是队尾元素本身；下标运算务必 `%MAX`。
- 链队出队最后一个元素时，要同时把 `rear` 置空（指向头结点），否则 `rear` 成为野指针。
:::

### 3.5 应用（★★★）
- 栈：数制转换、括号匹配、表达式求值（中缀→后缀，用栈算后缀）、函数调用／递归、迷宫、回溯（八皇后）。
- 队列：层序遍历、缓冲区、BFS、操作系统作业调度。

::: tip 工作示例 · 数制转换（十进制 → 八进制）
不断 `N % 8` 取余压栈、`N = N / 8`，直至 N 为 0；最后依次弹栈输出即得八进制。栈保证"余数逆序输出"。例如 N=100：`100%8=4`(压)、`N=12`；`12%8=4`(压)、`N=1`；`1%8=1`(压)、`N=0`；弹栈得 `144₈`。
:::

---

## 第 4 章 串、数组和广义表

### 4.1 串的定义与存储（★★）
串是字符的有限序列。存储：定长顺序、堆分配、块链。基本运算：赋值、比较、连接、求子串、定位（index）等。

### 4.2 串的模式匹配（★★★）
- **BF（朴素）算法**：逐字符回溯，最坏 `O(n×m)`（n 主串长、m 模式串长）。
- **KMP 算法**：利用**失配函数 next**（或优化 `nextval`）避免主串指针回退，时间 **`O(n+m)`**。

**关键算法（BF、KMP、get_next）**：
```c
// BF 朴素匹配：最坏 O(n*m)
int Index_BF(SString S, SString T, int pos) {
    i = pos; j = 1;
    while (i <= S.length && j <= T.length) {
        if (S[i] == T[j]) { ++i; ++j; }       // 继续比对
        else { i = i - j + 2; j = 1; }          // 回溯重来
    }
    if (j > T.length) return i - T.length;      // 成功
    else return 0;
}

// KMP 匹配：O(n+m)，主串指针 i 不回溯
int Index_KMP(SString S, SString T, int pos) {
    i = pos; j = 1;
    while (i <= S.length && j <= T.length) {
        if (j == 0 || S[i] == T[j]) { ++i; ++j; }
        else j = next[j];                        // 模式串右滑
    }
    if (j > T.length) return i - T.length;
    else return 0;
}

// 求 next 数组：O(m)
void get_next(SString T, int next[]) {
    i = 1; next[1] = 0; j = 0;
    while (i < T[0]) {                          // T[0] 存串长
        if (j == 0 || T[i] == T[j]) { ++i; ++j; next[i] = j; }
        else j = next[j];
    }
}
```

- `next[j]` ＝ 模式串中第 j 个字符前（不含 j）的真前缀与真后缀最长的相同长度 ＋ 1（即"最长相等前后缀长度 ＋ 1"）。
- `nextval`：当 `next[j]` 位置字符与 j 位置字符相同时进一步回退，减少无效比较。

::: tip KMP 核心
KMP 的精髓是"模式串自己跟自己比"，预先算出每个位置失配后该跳到哪。手算 next：对每个 j，找 `p₁…p_{j-1}` 的最长相等前后缀长度 k，则 `next[j]=k+1`（`next[1]=0`）。
:::

::: danger 易错 · next 手算（例题）
求模式 `ababaabab` 的 next 与 nextval（下标从 1 起）：
| j | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 字符 | a | b | a | b | a | a | b | a | b |
| next | 0 | 1 | 1 | 2 | 3 | 4 | 2 | 3 | 4 |
手算要点：j=5 时前缀 `abab`、后缀 `abab` 最长相等前后缀长 3 → next[5]=4；j=6 时前缀 `ababa` 最长相等前后缀为 `aba`（长 3）→ next[6]=4。务必是"真"前后缀（不含自身）。
:::

### 4.3 数组（★★★）
数组是下标→存储地址的映射，维度固定、随机存取。
- **行优先／列优先**存储：以二维数组 `a[m][n]` 为例，行优先 `LOC(i,j)=base+(i×n+j)×L`；列优先 `LOC(i,j)=base+(j×m+i)×L`。务必分清两种顺序！
- **特殊矩阵压缩**：
  - 对称矩阵：只存下三角（或上三角），`k = i(i−1)/2 + j`（i≥j 时，否则交换 i、j）。
  - 三角矩阵：类似，再加常数偏移。
  - **稀疏矩阵**：三元组表 `(i, j, v)` 或十字链表（行／列指针交叉）。

### 4.4 广义表（★★）
广义表是线性表的推广，元素可为原子或子表，可递归、可共享（如 `A=(a,(b,c),())`）。存储用头尾链表或扩展线性链表。`GetHead` / `GetTail` 是基本操作：如 `GetHead((a,b,c))=a`，`GetTail((a,b,c))=(b,c)`。

::: danger 易错 · 矩阵压缩与 KMP
- 行优先 vs 列优先地址公式不同，考试常考互换；下标从 1 还是 0 起要确认。
- next 数组手算最易错：是"真"前后缀（不含自身）；`next[1]=0`，失配后模式串从第 `next[j]` 位（从 1 计）继续。
:::

---

## 第 5 章 树和二叉树

### 5.1 树（★★）
树是 n 个结点的有限集，空或满足：有且仅有一个根；其余分为 m 个互不相交的子树。术语：度、叶子／分支结点、孩子／双亲／兄弟、层次、深度（高度）、森林（m 棵互不相交的树）。

### 5.2 二叉树（★★★）
二叉树每个结点至多两棵子树（左右有序，可为空）。
**五大性质**：
1. 第 i 层最多 `2^{i−1}` 个结点（i≥1）。
2. 深度为 k 的二叉树最多 `2ᵏ − 1` 个结点。
3. 任何二叉树，叶子数 `n₀` ＝ 分支数为 2 的结点数 `n₂ ＋ 1`（即 **`n₀ = n₂ + 1`**）。
4. 完全二叉树（按层序编号）中，结点 i 的双亲为 `⌊i/2⌋`，左孩子 `2i`、右孩子 `2i+1`（i≤⌊n/2⌋ 时为分支结点）。
5. 有 n 个结点的完全二叉树深度为 `⌊log₂n⌋ + 1`。

- **满二叉树**：每层都满；**完全二叉树**：除最后一层，其余满且最后一层左连续。

### 5.3 存储结构（★★）
- 顺序：仅适用于完全二叉树（按层序存数组，用性质 4 算关系）。
- 链式：二叉链表（`data + lchild + rchild`）最常用；三叉链表（增 `parent`）便于找双亲。

### 5.4 遍历（★★★）
- **先序（根左右）、中序（左根右）、后序（左右根）**：递归定义；层序（队列，自顶向下、同层从左到右）。
- 由遍历序列恢复树：必须包含**中序** ＋（先序 或 后序）才能唯一确定；仅有先序＋后序不能唯一确定。
- 中序遍历二叉排序树得到有序序列。

**关键算法（递归遍历、非递归中序）**：
```c
// 递归中序遍历（改 cout 位置即得先序/后序）
void InorderTraverse(BiTree T) {
    if (T) {
        InorderTraverse(T->lchild);  // 左
        cout << T->data;             // 根（先序把此句放最前，后序放最后）
        InorderTraverse(T->rchild);  // 右
    }
}

// 非递归中序（用栈模拟递归工作栈）
void InorderTraverse(BiTree T) {
    InitStack(S); p = T;
    while (p || !StackEmpty(S)) {
        if (p) { Push(S, p); p = p->lchild; }     // 一路向左
        else { Pop(S, q); cout << q->data; p = q->rchild; }  // 访问后转右
    }
}
```

::: tip 工作示例 · 遍历恢复树
已知先序 `ABDECF`、中序 `DBEAFC`：先序首字符 A 为根；中序中 A 左边 `DBE` 为左子树、右边 `FC` 为右子树；递归可得唯一二叉树。仅靠先序 `ABDECF` + 后序 `DEBFCA` **不能**唯一确定（左右子树划分不唯一）。
:::

### 5.5 线索二叉树（★★）
利用 n 个结点的二叉树中 `n+1` 个空指针，指向前驱／后继（`ltag/rtag` 区分指向孩子还是线索），便于无栈中序遍历。

### 5.6 树、森林与二叉树（★★）
- 树→二叉树：孩子兄弟表示法（左孩子、右兄弟）。
- 森林→二叉树：各树转二叉树后，根之间以右指针相连。
- 遍历对应：树先根↔二叉树先序；树后根↔二叉树中序；森林先序／中序↔二叉树先序／中序。

### 5.7 哈夫曼树与编码（★★★）
- 带权路径长度 `WPL = Σ wᵢ × lᵢ`；**哈夫曼树**是 WPL 最小的二叉树（最优二叉树）。
- 构造：每次取权值最小的两棵合并，新结点权为二者之和，重复至单树。
- **哈夫曼编码**：左／右分支记 0/1，叶子对应字符，是前缀码（无歧义、压缩率高）。

**关键算法（构造哈夫曼树）**：
```c
void CreateHuffmanTree(HuffmanTree &HT, int n) {
    if (n <= 1) return;
    m = 2 * n - 1;
    HT = new HTNode[m + 1];                         // 0 号单元不用
    for (i = 1; i <= m; ++i)
        HT[i].parent = HT[i].lchild = HT[i].rchild = 0;
    for (i = 1; i <= n; ++i) cin >> HT[i].weight;   // 读 n 个叶子权值
    for (i = n + 1; i <= m; ++i) {                  // n-1 次"选-删-并"
        Select(HT, i - 1, s1, s2);                  // 选双亲为 0 且权最小两结点
        HT[s1].parent = HT[s2].parent = i;
        HT[i].lchild = s1; HT[i].rchild = s2;
        HT[i].weight = HT[s1].weight + HT[s2].weight;
    }
}
```

::: danger 易错 · 二叉树
- 性质 3（`n₀=n₂+1`）只对二叉树成立，对一般树不成立。
- "先序＋后序"不能唯一确定二叉树；"中序＋先序"或"中序＋后序"可以。
- 哈夫曼树不唯一（权值相同时合并顺序可变），但 WPL 唯一最小；编码长度取决于合并路径。

::: tip 工作示例 · 哈夫曼 WPL
权值 `w=(5,29,7,8,14,23,3,11)`，n=8 → m=15。合并过程：先并 3、5→8；再并 7、8→15；…最终 WPL = `23×2+11×3+5×4+3×4+29×2+14×3+7×4+8×4 = 271`。
:::

![](/ds/ds-tree.svg)

---

## 第 6 章 图

### 6.1 定义与术语（★★）
图 `G=(V, E)`。无向图边 `(u,v)`；有向图弧 `<u,v>`。度（无向）／入度出度（有向）；连通（无向）／强连通（有向）；连通分量／强连通分量；生成树（n 顶点 n−1 边、连通无环）；生成森林。

### 6.2 存储（★★★）
- **邻接矩阵**：`|V|×|V|` 矩阵，无向图对称、空间 `O(|V|²)`；适合稠密图，查边 `O(1)`。
- **邻接表**：顶点表 ＋ 边链表，空间 `O(|V|+|E|)`；适合稀疏图。
- 还有十字链表（有向）、邻接多重表（无向，便于删边）。

### 6.3 遍历（★★★）
- **DFS**（栈／递归）：`O(|V|+|E|)`；
- **BFS**（队列）：`O(|V|+|E|)`。均生成遍历树／森林。

**关键算法（DFS 邻接矩阵、BFS）**：
```c
// DFS：从 v 出发，递归访问邻接点
void DFS_AM(AMGraph G, int v) {
    cout << v; visited[v] = true;
    for (w = 0; w < G.vexnum; w++)
        if (G.arcs[v][w] != 0 && !visited[w]) DFS_AM(G, w);
}

// BFS：队列保证"先访问的顶点其邻接点先被访问"
void BFS(Graph G, int v) {
    cout << v; visited[v] = true;
    InitQueue(Q); EnQueue(Q, v);
    while (!QueueEmpty(Q)) {
        DeQueue(Q, u);
        for (w = FirstAdjVex(G, u); w >= 0; w = NextAdjVex(G, u, w))
            if (!visited[w]) {
                cout << w; visited[w] = true; EnQueue(Q, w);
            }
    }
}
```
> 注：邻接表实现的 DFS/BFS 仅把"按矩阵查邻接点"改为"沿边链表扫描"，时间复杂度同为 `O(|V|+|E|)`。

### 6.4 应用（★★★）

| 问题 | 算法 | 时间复杂度 | 要点 |
| --- | --- | --- | --- |
| 最小生成树 MST | Prim | `O(\|V\|²)` | 适合稠密图（与边数无关） |
| 最小生成树 MST | Kruskal | `O(\|E\| log \|E\|)` | 适合稀疏图（并查集） |
| 单源最短路径 | Dijkstra | `O(\|V\|²)`（堆优化 `O((V+E)logV)`） | **不能处理负权边** |
| 各顶点最短路径 | Floyd | `O(\|V\|³)` | 可处理负权（无负权回路） |
| 拓扑排序 | Kahn / DFS | `O(\|V\|+\|E\|)` | AOV 网，可判有环 |
| 关键路径 | AOE | `O(\|V\|+\|E\|)` | 最长路径，求 ve/vl、e/l |

**关键算法（Prim、Dijkstra）**：
```c
// Prim：从顶点 u 出发，closedge[j]={adjvex,lowcost}
void MiniSpanTree_Prim(AMGraph G, VerTexType u) {
    k = LocateVex(G, u);
    for (j = 0; j < G.vexnum; ++j)
        if (j != k) closedge[j] = {u, G.arcs[k][j]};
    closedge[k].lowcost = 0;                         // U={u}
    for (i = 1; i < G.vexnum; ++i) {
        k = Min(closedge);                            // 选当前最小边
        cout << closedge[k].adjvex << G.vexs[k];      // 输出边
        closedge[k].lowcost = 0;                      // 顶点并入 U
        for (j = 0; j < G.vexnum; ++j)                // 用新顶点更新最小边
            if (G.arcs[k][j] < closedge[j].lowcost)
                closedge[j] = {G.vexs[k], G.arcs[k][j]};
    }
}

// Dijkstra：O(n^2)，无负权；D 为最短距离，Path 记录前驱
void ShortestPath_DIJ(AMGraph G, int v0) {
    n = G.vexnum;
    for (v = 0; v < n; ++v) {
        S[v] = false; D[v] = G.arcs[v0][v];
        Path[v] = (D[v] < MaxInt) ? v0 : -1;
    }
    S[v0] = true; D[v0] = 0;
    for (i = 1; i < n; ++i) {                         // 其余 n-1 个顶点
        min = MaxInt;
        for (w = 0; w < n; w++)
            if (!S[w] && D[w] < min) { v = w; min = D[w]; }
        S[v] = true;
        for (w = 0; w < n; w++)
            if (!S[w] && D[v] + G.arcs[v][w] < D[w]) {
                D[w] = D[v] + G.arcs[v][w]; Path[w] = v;
            }
    }
}
```

::: tip 工作示例 · Dijkstra 读路径
从源点 `v0` 到终点 `v5`：沿 `Path[5]→Path[3]→Path[4]→0` 反向得到路径 `0→4→3→5`。每轮把"距离最小的未确定顶点"加入 S 集，并用它松弛其余顶点。
:::

### 6.4.1 Kruskal 算法（代码）

Kruskal 与 Prim 思想相反：Prim 是"加点"（每次并入离已选集合最近的顶点），Kruskal 是"加边"（每次选全局最短且不成环的边），用**并查集**判环，更适合稀疏图。

```c
// Kruskal：边按权升序，并查集避免成环，O(E log E)
void MiniSpanTree_Kruskal(MGraph G) {
    Sort(edges);                               // 边按权升序排序
    InitVexSet(vexset, G.vexnum);              // 并查集：每个顶点自成一集合
    for (i = 0; i < G.arcnum; ++i) {
        v1 = LocateVex(G, edges[i].Head);
        v2 = LocateVex(G, edges[i].Tail);
        vs1 = Find(vexset, v1); vs2 = Find(vexset, v2);
        if (vs1 != vs2) {                       // 两端不在同一集合 ⇒ 加此边无环
            cout << edges[i].Head << edges[i].Tail;
            Union(vexset, vs1, vs2);            // 合并两集合
        }
    }
}
```

### 6.4.2 Floyd 算法（各顶点对最短路，代码＋例题）

Floyd 用动态规划：以 `k` 为中转点递推 `D[i][j] = min(D[i][j], D[i][k]+D[k][j])`，三维可优化为二维（覆盖写）。可处理负权边（只要无负权回路），时间 `O(V³)`。

```c
void ShortestPath_Floyd(AMGraph G, int D[][MAX], int Path[][MAX]) {
    for (i = 0; i < G.vexnum; ++i)
        for (j = 0; j < G.vexnum; ++j) {
            D[i][j] = G.arcs[i][j];
            Path[i][j] = (D[i][j] < MaxInt && i != j) ? i : -1;
        }
    for (k = 0; k < G.vexnum; ++k)             // 允许以 k 为唯一中转点
        for (i = 0; i < G.vexnum; ++i)
            for (j = 0; j < G.vexnum; ++j)
                if (D[i][k] + D[k][j] < D[i][j]) {   // 经 k 更短则更新
                    D[i][j] = D[i][k] + D[k][j];
                    Path[i][j] = Path[k][j];
                }
}
```

::: tip 工作示例 · Floyd 一步更新
设 A、B、C 三点，边 `A-B=3`、`B-C=4`、`A-C=10`。初始 `D[A][C]=10`；当 `k=B` 时，`D[A][B]+D[B][C]=3+4=7 < 10`，于是 `D[A][C]` 被更新为 `7`（绕 B 更短）。最终 `Path[A][C]=B`，沿 `Path` 逐层回溯得 `A→B→C`。
:::

### 6.4.3 拓扑排序（代码）

AOV 网（顶点表活动、有向边表先后约束）。**Kahn 算法**维护入度为 0 的顶点栈，逐个输出并把后继入度减 1；若最终输出顶点数 `< n` 说明存在回路（无法进行拓扑排序）。

```c
void TopologicalSort(ALGraph G, int indegree[]) {
    InitStack(S); count = 0;
    for (i = 0; i < G.vexnum; ++i)
        if (indegree[i] == 0) Push(S, i);      // 入度为 0 入栈
    while (!StackEmpty(S)) {
        Pop(S, i); cout << i; ++count;          // 输出顶点
        for (p = G.vertices[i].firstarc; p; p = p->nextarc) {
            k = p->adjvex;
            if (!(--indegree[k])) Push(S, k);   // 后继入度−1，归零则入栈
        }
    }
    if (count < G.vexnum) cout << " 存在回路！";
}
```

### 6.4.4 关键路径（ve/vl 例题）

AOE 网（边表活动、边权＝工期），关键路径是"从源点到汇点的最长路径"，其长度＝最短总工期；缩短非关键活动不缩短总工期。计算：
- **ve（最早发生时间）**：源点 `ve[0]=0`，`ve[j]=max{ve[i]+<i,j>的权}`，自前向后。
- **vl（最迟发生时间）**：汇点 `vl[n-1]=ve[n-1]`，`vl[i]=min{vl[j]−<i,j>的权}`，自后向前。
- 活动 `a=<i,j>`：`e=ve[i]`（最早开始），`l=vl[j]−权`（最迟开始）；`e==l` 的活动为**关键活动**，连成关键路径。

::: tip 工作示例 · 关键路径演算
活动与权：v0→v1:3，v0→v2:2，v1→v3:4，v2→v3:1，v3→v4:6，v2→v4:3。
- ve：ve[0]=0；ve[1]=3；ve[2]=2；ve[3]=max(3+4, 2+1)=7；ve[4]=max(7+6, 2+3)=13。
- vl：vl[4]=13；vl[3]=13−6=7；vl[2]=min(7−1, 13−3)=6；vl[1]=7−4=3；vl[0]=min(3−3, 6−2)=0。
- 关键活动（e=l）：v0→v1(0=0)、v1→v3(3=3)、v3→v4(7=7)；关键路径 **v0→v1→v3→v4**，总工期 **13**。
:::

::: danger 易错 · 图
- Dijkstra **不支持负权边**；有负权用 Bellman-Ford / SPFA；有负权回路则最短路无意义。
- 拓扑排序仅在 AOV 网（活动顶点、边表优先关系）上有意义；若输出顶点数 < n 说明有环。
- 关键路径是"最长路径"（决定工期），不是最短；缩短非关键活动不缩短总工期。
- 邻接矩阵无向图对称；邻接表空间与边数相关。
:::

![](/ds/ds-graph.svg)

---

## 第 7 章 查找

### 7.1 基本概念（★★）
查找：在数据结构上找出关键字等于给定值的记录。**平均查找长度 ASL** ＝ `Σ pᵢ × cᵢ`（cᵢ 为第 i 个记录的比较次数）。

### 7.2 静态查找（★★★）
- 顺序查找：`ASL≈(n+1)/2`，`O(n)`，对表无要求。
- **折半查找**：要求**有序且顺序存储**；每次折半，`O(log n)`；判定树为平衡二叉树，`ASL≈log₂(n+1)−1`。
- 分块查找（索引顺序）：块内无序、块间有序，`ASL` 介于两者之间。

**关键算法（折半查找）**：
```c
int Search_Bin(SSTable ST, KeyType key) {
    low = 1; high = ST.length;
    while (low <= high) {                 // 注意是 <=，low==high 时还要比一次
        mid = (low + high) / 2;
        if (key == ST.R[mid].key) return mid;
        else if (key < ST.R[mid].key) high = mid - 1;
        else low = mid + 1;
    }
    return 0;                             // 查找失败
}
```

::: tip 工作示例 · 折半查找
有序表 `(5,16,20,27,30,36,44,55,60,67,71)` 查 27：`mid=6`(36)>27→high=5；`mid=3`(20)<27→low=4；`mid=4`(27)=27 成功，比较 3 次。查 65：最终 `low>high` 失败。
:::

### 7.3 动态查找（★★★）
- **二叉排序树 BST**：中序遍历有序；查找／插入／删除平均 `O(log n)`，最坏（退化为单支）`O(n)`。删除分叶子、独子、双子三种情况，双子时用前驱／后继替代最稳。
- **平衡二叉树 AVL**：任一结点左右子树深度差（平衡因子 BF）绝对值 ≤ 1。插入／删除后若失衡，通过 **LL / RR / LR / RL** 四种旋转调整，维持 `O(log n)`。
- **B-树（m 阶）**：平衡多路查找树，每个结点最多 m−1 个关键字、m 个孩子；用于**外存**索引；插入可能分裂、删除可能合并／借位，所有叶子在同一层。
  - **B+树**：非叶结点只作索引（关键字重复出现在叶子），叶子用指针串成有序链表，**范围查询／全表扫描高效**，是数据库索引主流。
  - **红黑树**（补充）：自平衡二叉查找树（1972 年 Bayer 提出，后由 Guibas/Sedgewick 定型），满足五条性质：① 结点非红即黑；② 根结点为黑；③ 红结点的孩子必为黑（无连续红结点）；④ 任一结点到其所有后代 NIL 叶子的路径上含相同数目的黑结点（黑高一致）；⑤ 叶子（NIL）为黑。由③④⑤可推：从根到叶的最长路径不超过最短路径的 2 倍，故树高 ≈ 2log₂(n+1)，查找／插入／删除均 **O(log n)**。与 AVL 相比：AVL 平衡更严（查询略快），红黑树插入删除旋转更少（增删略快），工程实现（C++ STL `map`、Java `TreeMap`、Linux 内核）多选用红黑树。**伸展树（splay）** 则每次访问后将结点旋到根，均摊 O(log n)，利于局部性访问。

**关键算法（BST 查找、插入、删除-双子情况）**：
```c
// 查找：O(h)
BSTree SearchBST(BSTree T, KeyType key) {
    if (!T || key == T->data.key) return T;
    if (key < T->data.key) return SearchBST(T->lchild, key);
    else return SearchBST(T->rchild, key);
}

// 插入（新结点必为叶子）：O(h)
void InsertBST(BSTree &T, ElemType e) {
    if (!T) {
        S = new BSTNode; S->data = e;
        S->lchild = S->rchild = NULL; T = S;
    }
    else if (e.key < T->data.key) InsertBST(T->lchild, e);
    else if (e.key > T->data.key) InsertBST(T->rchild, e);
}

// 删除（双子情形：用左子树最右下结点=前驱替代）
// 找到后：
q = p; s = p->lchild;
while (s->rchild) { q = s; s = s->rchild; }   // 找前驱（左子树最右）
p->data = s->data;
if (q != p) q->rchild = s->lchild;             // 重接 q 的右子树
else q->lchild = s->lchild;                     // 前驱恰为左孩子
delete s;
```

::: tip 红黑树 vs AVL
两者都保证 O(log n)；AVL 平衡因子严格 ∈{-1,0,1}、查询更快但增删旋转多；红黑树仅保证"黑平衡"、增删代价更低，是大多数语言标准库与系统的首选。
:::

::: tip AVL 四种失衡与旋转（补充）
失衡结点 `BF=+2`（左重）→ 看左孩子 BF：左孩子 `BF≥0` 用 **LL**（右旋）；左孩子 `BF<0` 用 **LR**（先左后右）。`BF=−2`（右重）→ 看右孩子 BF：右孩子 `BF≤0` 用 **RR**（左旋）；右孩子 `BF>0` 用 **RL**（先右后左）。旋转后整树仍保持 BST 中序有序且高度降低。
:::

**关键算法（AVL 旋转）**：
```c
// AVL 树：平衡因子 BF = 左子树高 − 右子树高，∈{−1,0,1}
typedef struct AVLNode {
    ElemType data;
    int bf;                       // 平衡因子
    struct AVLNode *lchild, *rchild;
} *AVLTree;

// 右旋（处理 LL）：以 p 为轴，左孩子 lc 上升为根
void R_Rotate(AVLTree &p) {
    lc = p->lchild;
    p->lchild = lc->rchild;       // lc 的右子树挂到 p 的左
    lc->rchild = p;
    p = lc;                        // lc 成为新根
}

// 左旋（处理 RR）：以 p 为轴，右孩子 rc 上升为根
void L_Rotate(AVLTree &p) {
    rc = p->rchild;
    p->rchild = rc->lchild;       // rc 的左子树挂到 p 的右
    rc->lchild = p;
    p = rc;
}

// 左平衡（插入在左子树导致 p 失衡 BF=2）：再分 LL / LR
void LeftBalance(AVLTree &p) {
    lc = p->lchild;
    if (lc->bf == 1) {             // LL 型：左孩子左重 → 直接右旋
        p->bf = lc->bf = 0;
        R_Rotate(p);
    } else {                       // LR 型：左孩子右重 → 先左旋 lc 再右旋 p
        rd = lc->rchild;
        if (rd->bf == 1) { p->bf = -1; lc->bf = 0; }
        else             { p->bf = 0;  lc->bf = 1; }
        rd->bf = 0;
        L_Rotate(lc); R_Rotate(p);
    }
}
// 右平衡 RightBalance 对称（处理 RR / RL），此处略。
```

![](/ds/ds-avl.svg)

### 7.3.1 B-树插入与分裂（m 阶）

**插入**：若目标叶子结点关键字数 `< m−1`，直接按序插入；否则该结点溢出（关键字数达 `m`），取**中位数关键字上移至父结点**，该结点分裂为左右两结点；若父结点也溢出则继续向上分裂，直至根——根分裂会使**树高 +1**。

**删除**（与插入相反）：删除后关键字数低于下限 `⌈m/2⌉−1` 时，先向左右兄弟"借"一个（父结点对应关键字下沉到本结点、兄弟的一个关键字上升补父）；借不到则与兄弟合并，并下迁父结点一个关键字——可能使**树高 −1**。

::: tip 工作示例 · B-树（m=3）分裂
某结点插入后变为 `[52,55,58]`（3 个关键字 > m−1=2）溢出：取中位数 `55` 上移至父结点，左 `[52]`、右 `[58]` 各成新结点（详见示意图"③ 插入分裂"）。若父结点因此也变为 3 个关键字，则继续向上分裂。
:::

![](/ds/ds-btree.svg)

### 7.4 散列表（★★★）
- **哈希函数**：除留余数法 `H(key)=key mod p`（p 取不大于表长的最大素数最佳）、直接定址、数字分析、平方取中、折叠法等。
- **冲突处理**：
  - 开放定址：线性探测（易"聚集"）、二次探测、伪随机探测；
  - **链地址法**（同义词拉链）：不易聚集，装载因子 α 可 >1，常用。
- **装填因子** `α = 记录数 / 表长`，决定 ASL；α 越大冲突越多。链地址法 `ASL≈1+α/2`。

**关键算法（线性探测查找）**：
```c
int SearchHash(HashTable HT, KeyType key) {
    H0 = H(key);                                  // 散列地址
    if (HT[H0].key == NULLKEY) return -1;         // 空 → 不存在
    if (HT[H0].key == key) return H0;             // 一次命中
    for (i = 1; i < m; ++i) {
        Hi = (H0 + i) % m;                         // 线性探测下一个地址
        if (HT[Hi].key == NULLKEY) return -1;
        if (HT[Hi].key == key) return Hi;
    }
    return -1;
}
```

| 处理冲突方法 | 查找成功 ASL | 查找失败 ASL |
| --- | --- | --- |
| 线性探测法 | `½(1+1/(1−α))` | `½(1+1/(1−α)²)` |
| 二次探测法 | `−log₂(1−α)`（近似） | `1/(1−α)` |
| 链地址法 | `1 + α/2` | `α + e^{−α}` |

::: danger 易错 · 查找
- 折半查找必须"有序 ＋ 顺序存储"；链表不能折半。
- BST 退化成单支时退化为 `O(n)`，故实际多用 AVL／红黑树／B-树。
- 哈希"冲突"不可避免（鸽巢原理），只能减少与处理；线性探测会产生"一次聚集"。
- B-树阶 m：最多 m−1 个关键字、m 棵子树；根至少 2 棵子树（除非是叶子）。
:::

![](/ds/ds-hash.svg)

---

## 第 8 章 排序

### 8.1 基本概念（★★）
- **稳定性**：关键字相等记录在排序前后相对次序不变 → 稳定（如直接插入、冒泡、归并、基数）；否则不稳定（如希尔、快速、简单选择、堆）。
- 内／外部排序：记录全在内存为内部排序；需外存为外部排序。
- 分类（按扩大有序区方式）：插入类、交换类、选择类、归并类、分配类（基数，无需比较）。
- 效率指标：比较次数 ＋ 移动次数 ＋ 辅助空间。

### 8.2 插入排序（★★★）
- 直接插入：最好 `O(n)`、平均／最坏 `O(n²)`；稳定；适合基本有序、小规模。
- 折半插入：减少比较（`O(n log n)` 比较）但不减移动，仍为 `O(n²)`。
- 希尔排序：按增量分组插入，打破相邻比较，平均 `O(n^{1.3})` 左右；**不稳定**。

**关键算法（直接插入、折半插入）**：
```c
// 直接插入排序：监视哨 r[0]，最好 O(n)，最坏/平均 O(n^2)，稳定
void InsertSort(SqList &L) {
    for (i = 2; i <= L.length; ++i)
        if (L.r[i].key < L.r[i-1].key) {
            L.r[0] = L.r[i];                       // 暂存到监视哨
            L.r[i] = L.r[i-1];
            for (j = i - 2; L.r[0].key < L.r[j].key; --j)
                L.r[j+1] = L.r[j];                 // 记录后移
            L.r[j+1] = L.r[0];                      // 插入
        }
}

// 折半插入排序：比较降至 O(n log n)，移动仍 O(n^2)
void BInsertSort(SqList &L) {
    for (i = 2; i <= L.length; ++i) {
        L.r[0] = L.r[i]; low = 1; high = i - 1;
        while (low <= high) {                        // 折半找插入位置
            mid = (low + high) / 2;
            if (L.r[0].key < L.r[mid].key) high = mid - 1;
            else low = mid + 1;
        }
        for (j = i - 1; j >= high + 1; --j) L.r[j+1] = L.r[j];
        L.r[high + 1] = L.r[0];
    }
}
```

**希尔排序（代码＋例题）**：
```c
// 希尔排序：按增量 dk 分组做直接插入，逐步缩小 dk，O(n^{1.3})，不稳定
void ShellInsert(SqList &L, int dk) {
    for (i = dk + 1; i <= L.length; ++i)
        if (L.r[i].key < L.r[i - dk].key) {
            L.r[0] = L.r[i];
            for (j = i - dk; j > 0 && L.r[0].key < L.r[j].key; j -= dk)
                L.r[j + dk] = L.r[j];        // 组内后移
            L.r[j + dk] = L.r[0];
        }
}
void ShellSort(SqList &L, int dlta[], int t) {
    for (k = 0; k < t; ++k) ShellInsert(L, dlta[k]);  // 增量序列，如 5,3,1
}
```

::: tip 工作示例 · 希尔排序
序列 `49,38,65,97,76,13,27,49,55,04`，取 `dk=5`：`(49,13)(38,27)(65,49)(97,55)(76,04)` 各组内插入排序 → `13,27,49,55,04,49,38,65,97,76`；再 `dk=3`、`dk=1` 逐步缩距，最终有序。增量互质可避免某些间隔始终不被比较。
:::

### 8.3 交换排序（★★★）
- 冒泡排序：最好 `O(n)`（加 flag 提前结束）、最坏 `O(n²)`；稳定。
- **快速排序**：选枢轴划分，递归；平均 `O(n log n)`、最坏（已序／逆序选端点为轴）`O(n²)`；**不稳定**；可用"三者取中"选轴、小数组转插入改善。

**关键算法（冒泡、快排 Partition/QSort）**：
```c
// 冒泡排序：flag 提前结束，最好 O(n)，最坏 O(n^2)，稳定
void BubbleSort(SqList &L) {
    m = L.length - 1; flag = 1;
    while (m > 0 && flag == 1) {
        flag = 0;
        for (j = 1; j <= m; j++)
            if (L.r[j].key > L.r[j+1].key) {
                t = L.r[j]; L.r[j] = L.r[j+1]; L.r[j+1] = t;
                flag = 1;                           // 本趟发生交换
            }
        --m;
    }
}

// 快速排序：平均 O(n log n)，最坏 O(n^2)，不稳定
int Partition(SqList &L, int low, int high) {
    L.r[0] = L.r[low]; pivotkey = L.r[low].key;     // 首元素作枢轴
    while (low < high) {
        while (low < high && L.r[high].key >= pivotkey) --high;
        L.r[low] = L.r[high];
        while (low < high && L.r[low].key <= pivotkey) ++low;
        L.r[high] = L.r[low];
    }
    L.r[low] = L.r[0]; return low;                   // 枢轴归位
}
void QSort(SqList &L, int low, int high) {
    if (low < high) {
        pivotloc = Partition(L, low, high);
        QSort(L, low, pivotloc - 1);
        QSort(L, pivotloc + 1, high);
    }
}
void QuickSort(SqList &L) { QSort(L, 1, L.length); }
```

### 8.4 选择排序（★★★）
- 简单选择：无论初始状态均 `O(n²)`；**不稳定**（如 `2,2,1`）。
- **堆排序**：建大顶堆后反复取堆顶，`O(n log n)` 且最坏也是 `O(n log n)`；**不稳定**；空间 `O(1)`；适合大数据。

**关键算法（堆调整、堆排序）**：
```c
// 筛选法调整堆（大根堆）：O(log n)
void HeapAdjust(SqList &L, int s, int m) {
    rc = L.r[s];
    for (j = 2 * s; j <= m; j *= 2) {
        if (j < m && L.r[j].key < L.r[j+1].key) ++j;  // 取较大孩子
        if (rc.key >= L.r[j].key) break;
        L.r[s] = L.r[j]; s = j;
    }
    L.r[s] = rc;
}
// 堆排序：建堆 O(n) + n-1 次调整，最坏仍 O(n log n)，不稳定，空间 O(1)
void HeapSort(SqList &L) {
    n = L.length;
    for (i = n / 2; i > 0; --i) HeapAdjust(L, i, n);  // 自底向上建大根堆
    for (i = n; i > 1; --i) {
        swap(L.r[1], L.r[i]);                          // 堆顶与末尾交换
        HeapAdjust(L, 1, i - 1);
    }
}
```

**简单选择排序（代码）**：
```c
// 简单选择排序：每趟选最小与未排序首元素交换，O(n^2)，不稳定
void SelectSort(SqList &L) {
    for (i = 1; i < L.length; ++i) {
        k = i;                                   // 记录最小者位置
        for (j = i + 1; j <= L.length; ++j)
            if (L.r[j].key < L.r[k].key) k = j;
        if (k != i) { t = L.r[i]; L.r[i] = L.r[k]; L.r[k] = t; }
    }
}
```

### 8.5 归并排序（★★★）
- 2-路归并：分治合并，时间 **稳定 `O(n log n)`**、空间 `O(n)`；**稳定**；适合外部排序与链表。

**关键算法（Merge、MergeSort）**：
```c
// 合并两个有序段 R[low..mid] 与 R[mid+1..high]
void Merge(RedType R[], RedType T[], int low, int mid, int high) {
    i = low; j = mid + 1; k = low;
    while (i <= mid && j <= high)
        if (R[i].key <= R[j].key) T[k++] = R[i++];
        else T[k++] = R[j++];
    while (i <= mid) T[k++] = R[i++];
    while (j <= high) T[k++] = R[j++];
}
// 归并排序（递归）：O(n log n)，稳定，空间 O(n)
void MergeSort(SqList &L) {
    MSort(L.r, L.r, 1, L.length);
}
```

### 8.6 基数排序（★★）
- 按"位"分配-收集（LSD/MSD），不需比较关键字；时间 `O(d(n+r))`（d 位数、r 基数）；**稳定**；适合整数／字符串等长码。

**基数排序（代码＋例题）**：
```c
// 基数排序（LSD，按位从低到高分配-收集，r=10 个桶）：O(d(n+r))，稳定
void RadixSort(SqList &L) {
    for (i = 1; i <= L.length; ++i) L.r[i].next = i + 1;  // 建静态链表
    L.r[L.length].next = 0;
    for (key = 1; key <= KeyNum; ++key) {                  // 每位一次分配+收集
        front[0..9] = 0; rear[0..9] = 0;                   // 10 个桶首尾指针
        for (p = L.r[0].next; p; p = L.r[p].next) {
            d = L.r[p].key 的第 key 位数字;
            if (!front[d]) front[d] = p; else L.r[rear[d]].next = p;
            rear[d] = p;
        }
        j = 0;                                             // 收集：10 桶首尾相接
        for (d = 0; d < 10; ++d) if (front[d]) {
            L.r[j].next = front[d]; j = rear[d];
        }
        L.r[j].next = 0;
    }
}
```

::: tip 工作示例 · 基数排序
序列 `278,109,063,930,589,184,505,269,008,083`，先按**个位**分配收集，再按**十位**、**百位**，三趟后得有序序列。每趟只做"取位—入桶—串接"，不发生关键字间比较。
:::

### 8.7 外部排序（★★）
- 多路平衡归并 ＋ 置换-选择生成初始归并段 ＋ **最佳归并树**（哈夫曼思想）减少归并趟数／IO。

| 排序 | 平均时间 | 最坏时间 | 空间 | 稳定性 |
| --- | --- | --- | --- | --- |
| 直接插入 | `O(n²)` | `O(n²)` | `O(1)` | 稳定 |
| 折半插入 | `O(n²)` | `O(n²)` | `O(1)` | 稳定 |
| 希尔 | `O(n^{1.3})` | `O(n²)` | `O(1)` | 不稳定 |
| 冒泡 | `O(n²)` | `O(n²)` | `O(1)` | 稳定 |
| 快速 | `O(n log n)` | `O(n²)` | `O(log n)` | 不稳定 |
| 简单选择 | `O(n²)` | `O(n²)` | `O(1)` | 不稳定 |
| 堆 | `O(n log n)` | `O(n log n)` | `O(1)` | 不稳定 |
| 2-路归并 | `O(n log n)` | `O(n log n)` | `O(n)` | 稳定 |
| 基数 | `O(d(n+r))` | `O(d(n+r))` | `O(n+r)` | 稳定 |

::: danger 易错 · 排序
- 快排最坏发生在"每次划分极不均衡"（如已序且选端点为轴），用随机／三者取中选轴。
- 堆排序建堆 `O(n)`（自底向上下沉），之后每次取顶 `O(log n)`，共 `O(n log n)`，**不受初始序影响**。
- 稳定性易记反：插／冒／归／基 稳；希／快／选／堆 不稳。
- 基数排序"不比较关键字"，靠分配收集；适合定长多关键字。
:::

---

## 第 9 章 算法设计与分析（补充）

::: info 本章定位
第 1–8 章以"数据结构"为主线；本章以"算法设计"为主线，把散落在各章的算法思想（递归分治、贪心求 MST/最短路、回溯求 N 皇后、动态规划求最短路等）归纳成五大范式，并补充红黑树等自平衡查找结构。这部分是算法分析与设计课程的核心，也常与数据结构联合命题。
:::

### 9.1 五大范式一览（★★★）

| 范式 | 核心思想 | 典型问题 | 关键性质 |
| --- | --- | --- | --- |
| 分治法 | 分解 → 递归解决 → 合并 | 归并排序、快速排序、二分查找、大整数乘法 | 子问题独立且规模相近 |
| 贪心法 | 每步取当前局部最优 | 活动安排、Huffman、Prim、Kruskal、Dijkstra、可拆背包 | 贪心选择性质 ＋ 最优子结构 |
| 动态规划 | 记忆化重叠子问题 | 0-1 背包、LCS、矩阵连乘、Floyd | 最优子结构 ＋ 重叠子问题 |
| 回溯法 | 深度优先遍历解空间树 ＋ 剪枝 | N 皇后、0-1 背包、子集和、m 着色 | 求全部解 ／ 一个解 |
| 分支限界法 | 优先队列层次遍历解空间树 ＋ 限界函数 | 0-1 背包（最优）、TSP | 求一个最优解，效率高于回溯 |

### 9.2 分治法与 Master 定理（★★★）
分治三步骤：分解（原问题 → 若干规模更小的子问题）、解决（递归求解子问题）、合并（子问题解 → 原问题解）。递归方程 `T(n) = aT(n/b) + f(n)`（a≥1，b>1）。
**主定理**：记 `c = log_b a`，比较 `f(n)` 与 `n^c`：
1. 若 `f(n) = O(n^{c−ε})`（ε>0），则 `T(n) = Θ(n^c)`；
2. 若 `f(n) = Θ(n^c log^k n)`，则 `T(n) = Θ(n^c log^{k+1} n)`；
3. 若 `f(n) = Ω(n^{c+ε})` 且正规（`a f(n/b) ≤ c f(n)`），则 `T(n) = Θ(f(n))`。
例：归并排序 a=b=2 ⇒ c=1，`f(n)=Θ(n)` 属第 2 类 ⇒ `Θ(n log n)`；二分查找 a=1，b=2 ⇒ c=0，`f(n)=Θ(1)` ⇒ `Θ(log n)`。

### 9.3 贪心算法（★★★）
两个基本要素：**贪心选择性质**（整体最优可由一系列局部最优达到，不依赖子问题解）＋ **最优子结构**（问题最优解包含子问题最优解）。
- 典型：活动安排（按结束时间最早选，`O(n log n)`）、Huffman、Prim/Kruskal、Dijkstra。
- **陷阱**：贪心不保证全局最优。如硬币面值 `{1,5,11}`、找 15 分，贪心给 `11+1+1+1=4` 枚，而 `5+5+5=3` 枚更优。**0-1 背包不能用贪心（须 DP），可拆背包可用贪心**。

### 9.4 回溯法（★★★）
解空间树：① **子集树**（每层 2 叉，`2ⁿ` 叶子，如 0-1 背包、子集和、装载）；② **排列树**（`n!` 叶子，如 N 皇后、TSP、全排列）。算法 ＝ 深度优先遍历解空间树 ＋ **约束函数**（剪去不满足约束的分支）＋ **限界函数**（剪去不可能更优的分支）。N 皇后：每行放一后，约束为不同列、不同正/反对角线。

![](/ds/ds-algo.svg)

**关键算法（N 皇后回溯，子集树／排列树见上图）**：
```c
// N 皇后回溯：每行放一后，约束为不同列、不同正/反对角线
int x[N + 1];                         // x[k] = 第 k 行皇后所在列
int Place(int k) {                    // 判断第 k 行能否放 x[k] 列
    for (i = 1; i < k; ++i)
        if (x[i] == x[k] || abs(x[i] - x[k]) == abs(i - k)) return 0;
    return 1;
}
void NQueens(int k, int n) {
    if (k > n) { 输出一组解; return; }   // 已放完 n 个皇后 ⇒ 一组解
    for (col = 1; col <= n; ++col) {
        x[k] = col;
        if (Place(k)) NQueens(k + 1, n);  // 满足约束才向下搜索，否则剪枝
    }
}
```

::: tip 工作示例 · 回溯剪枝
4 皇后从第一行逐列试放：放 (1,1) 后，第二行不能再放第 1 列（同列）也不能放第 2 列（主对角 `|1-2|=|1-2|`）；若整行都冲突则该分支回溯。最终得到全部合法布局（4 皇后有 2 解）。
:::

### 9.5 分支限界法（★★）
与回溯同围绕解空间树，但目标为"求一个最优解"，采用**优先队列**（最大收益或最小耗费优先）做层次遍历；用**限界函数**估计子树优劣，剪去不可能产生更优解的分支。一般求最优解时效率高于回溯（回溯偏"搜全部"）。常用于 0-1 背包、TSP 的最优解求解。

### 9.6 动态规划（★★★）
基本要素：**最优子结构** ＋ **重叠子问题**。设计步骤：定义状态 → 写状态转移方程 → 定边界 → 选计算序（自底向上或带备忘自顶向下）。
- 0-1 背包：`dp[i][c] = max(dp[i−1][c], dp[i−1][c−w_i] + v_i)`。
- 最长公共子序列 LCS、矩阵连乘、Floyd（各顶点最短路）均属 DP。

::: tip 工作示例 · 0-1 背包（DP）
容量 `C=10`，物品 `(w,v)={(2,6),(2,3),(6,5),(5,4),(4,6)}`。`dp[i][c]` 表示前 `i` 件、容量限制 `c` 下的最大价值。
状态转移：`dp[i][c] = max(dp[i-1][c], dp[i-1][c-w_i] + v_i)`（`c ≥ w_i`，否则沿用 `dp[i-1][c]`）；边界 `dp[0][*]=0`。
填表后 `dp[5][10]=15`，对应选物品 **1、2、5**（重 `2+2+4=8 ≤ 10`，价值 `6+3+6=15`）。注意与"可拆背包"不同：0-1 背包每件只能选 0 或 1 次，必须 DP，贪心（按 `v/w` 降序）不能保证最优。
:::

::: danger 易错 · 算法范式
- 贪心 vs DP：都需最优子结构；但贪心每步不依赖子问题解（只看当前局部），DP 每步依赖子问题解。可拆背包贪心得最优，0-1 背包必须 DP。
- 回溯 vs 分支限界：回溯深度优先求"全部/一个"解，分支限界（优先队列）求"一个最优"解、效率更高。
- 分治要求子问题独立；若子问题重叠（如朴素 Fibonacci 递归）应改记忆化/DP，否则指数级。
- 主定理先算 `c=log_b a`，再与 `f(n)` 比阶；第 2 类别忘了 `log^{k+1}n`。
- 红黑树"黑高一致"保证高度 ≈2log(n+1)，是工程首选；AVL 更平衡但增删旋转多。
:::

---

## 附录 A 公式与结论速查

| 类别 | 公式／结论 |
| --- | --- |
| 顺序表地址 | `LOC(aᵢ)=LOC(a₁)+(i−1)L`；行优先二维 `a[i][j]=base+(i×n+j)L` |
| 顺序表增删 | 平均移动 `n/2`、`(n−1)/2`，`O(n)` |
| 单链表插入 | 先 `s->next=p->next` 后 `p->next=s`；平均 `O(n)` |
| 时间复杂度阶 | `O(1)<O(log n)<O(n)<O(n log n)<O(n²)<O(n³)<O(2ⁿ)` |
| 循环队列 | 队空 `front==rear`；队满 `(rear+1)%MAX==front`；长度 `(rear-front+MAX)%MAX` |
| 串匹配 | BF `O(n·m)`；KMP `O(n+m)`，`next[j]`=最长相等前后缀长+1 |
| 二叉树性质 | `n₀=n₂+1`；第 i 层 ≤ `2^{i−1}`；深度 k 最多 `2ᵏ−1`；完全树深度 `⌊log₂n⌋+1` |
| 哈夫曼 WPL | `WPL=Σ wᵢlᵢ`（最小） |
| 折半查找 ASL | `≈log₂(n+1)−1`，`O(log n)` |
| AVL | 平衡因子 `BF∈{−1,0,1}`，失衡用 LL/RR/LR/RL 旋转，`O(log n)` |
| 哈希 ASL（链地址） | `≈1+α/2`（α 为装填因子） |
| 图 MST | Prim `O(V²)`、Kruskal `O(E log E)` |
| 图 最短路 | Dijkstra `O(V²)`（无负权）、Floyd `O(V³)` |
| 排序（稳定且最坏不退化） | 堆排序、归并排序 |
| 排序（不稳定） | 希尔、快速、简单选择、堆 |
| 分治主定理 | `T(n)=aT(n/b)+f(n)`，`c=log_b a`；比阶定 `Θ` |
| 红黑树 | 5 性质保黑高一致；树高 ≈2log₂(n+1)，`O(log n)` |
| 贪心要素 | 贪心选择性质 ＋ 最优子结构 |
| 回溯解空间树 | 子集树 `2ⁿ` 叶、排列树 `n!` 叶；约束/限界剪枝 |

## 附录 B 各章易错点速查

1. 数据结构＝逻辑结构（集合／线性／树／图）× 存储结构（顺序／链式／索引／散列）。
2. 算法 5 特性：有穷、确定、可行、输入、输出；复杂度看增长率而非具体步数。
3. 顺序表插入／删除需移动元素（平均 `O(n)`）；链表只需改指针但需先找前驱。
4. 单链表插入必须 `s->next=p->next` 在前、`p->next=s` 在后。
5. 循环队列队满用 `(rear+1)%MAX==front`，不能再用 `rear==front`（与队空冲突）。
6. 栈 LIFO、队列 FIFO；递归靠系统栈实现，可借栈改写为非递归。
7. KMP 用 next/nextval 避免主串回退，`O(n+m)`；next 为最长相等前后缀长度 ＋1。
8. 矩阵压缩务必分清行优先／列优先；对称矩阵只存下三角。
9. 二叉树 `n₀=n₂+1` 仅对二叉树成立；"先序＋后序"不能确定一棵二叉树。
10. 遍历恢复树必须含中序；二叉排序树中序遍历有序。
11. 哈夫曼树 WPL 最小但不唯一；编码为前缀码。
12. 图的 DFS/BFS 均 `O(V+E)`；Dijkstra 不能处理负权边。
13. 拓扑排序顶点数 < n 说明有环；关键路径是最长路径（决定工期）。
14. 静态查找折半要求"有序 ＋ 顺序存储"；链表不能折半。
15. BST 退化单支退化为 `O(n)`；实际用 AVL／B-树等平衡结构。
16. AVL 失衡四类：LL(右旋)／RR(左旋)／LR(先左后右)／RL(先右后左)。
17. B-树阶 m：最多 m−1 关键字、m 子树；B+树叶子串链表利于范围查询。
18. 哈希冲突不可避免；线性探测有聚集；链地址法 α 可 >1。
19. 排序稳定性：插／冒／归／基 稳，希／快／选／堆 不稳。
20. 快排最坏 `O(n²)`（已序且选端点轴）；堆排序最坏仍是 `O(n log n)`。
21. 基数排序不比较关键字，靠分配-收集，适合定长码。
22. 外排序用多路归并 ＋ 最佳归并树减少 IO 趟数。
23. 贪心 vs DP：都需最优子结构；贪心不依赖子问题解，DP 依赖；可拆背包贪心、0-1 背包须 DP。
24. 回溯（深度优先、求全部解）vs 分支限界（优先队列、求一个最优解）：后者求最优时更高效。
25. 分治要求子问题独立；子问题重叠（朴素 Fibonacci）应改记忆化/DP，否则指数级。
26. 主定理先算 `c=log_b a` 再比阶；第 2 类莫忘 `log^{k+1}n`。
27. 红黑树靠"黑高一致"保证高度 ≈2log(n+1)；AVL 更平衡但增删旋转多，工程多取红黑树。
