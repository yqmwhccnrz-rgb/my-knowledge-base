---
summary: "9 章 Python 数据分析笔记：ndarray、numpy 函数、Series 与 DataFrame、数据清洗、分组聚合与可视化，涵盖视图/拷贝、标签对齐、apply/merge、透视表等实战知识点。"
---

# Python 数据分析笔记

> **这是一篇笔记**：9 章内容连续排在同一页，从上往下读即可；也可以点右侧「本页目录」跳到任意章节。

::: info 笔记概要
- **所属课程**：Python 数据分析
- **核心内容**：用 numpy 的 `ndarray` 与 pandas 的 `Series`/`DataFrame` 完成数据的创建、清洗、变形、聚合与可视化，并用 matplotlib / seaborn 绘图
- **学习建议**：每个函数都要亲手敲一遍并观察返回值和形状（`shape`）；numpy 与 pandas 的「按位置」和「按标签」两种索引方式务必分清
- **关键词**：numpy、ndarray、pandas、Series、DataFrame、数据清洗、分组聚合、可视化
:::

## 全书目录

| 章节 | 主要内容 |
| --- | --- |
| 第 1 章 | 数据分析流程、ndarray 特性与数据类型 |
| 第 2 章 | ndarray 的创建、索引切片与运算（含广播、视图与拷贝） |
| 第 3 章 | numpy 数学 / 统计 / 比较与逻辑函数 |
| 第 4 章 | Series 的创建、属性、访问与常用方法（含索引对齐） |
| 第 5 章 | DataFrame 的创建、属性、访问与常用方法（含 apply、合并） |
| 第 6 章 | 数据导入导出、缺失值 / 重复值处理、清洗变形、时间数据、分组聚合 |
| 第 7 章 | matplotlib 与 seaborn 可视化（含中文显示、子图、双轴） |
| 第 8 章 | 易错点汇总 |
| 第 9 章 | 知识点速查总结 |

---

## 第1章 数据分析基础概念

### 1.1 数据分析的基本流程

导入（import）：

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
```

数据分析通常按下面这条线走：

> **数据收集**（文件 → `DataFrame`）→ **数据清洗**（缺失值、重复值、异常值）→ **数据分析**（统计、对比、分组聚合）→ **数据可视化**（出图）

### 1.2 ndarray 数组及其特性

`ndarray` 是 numpy 的核心多维数组对象，有三个关键特性：

1. **多维性**：可以是零维（标量）、一维、二维、三维……`shape` 用元组表示各维度长度。
2. **同质性**：数组里所有元素的类型必须相同；如果混入了不同类型的元素，numpy 会**强制转换成同一种类型**（例如整数和浮点数混在一起会变成浮点，字符串和数字混在一起会变成字符串）。
3. **高效性**：底层由 C 实现，向量化运算（一次对整个数组做运算）比 Python 的 `for` 循环快得多。

::: tip 提示
「向量化」是 numpy 快的根本原因：写 `a + b` 而不是写循环逐个相加，既简洁又高效。
:::

### 1.3 ndarray 的数据类型


numpy 的数据类型（dtype）按占用字节分得很细，下表整理自原笔记图片：

| 数据类型 | 说明 |
| --- | --- |
| `bool` | 布尔类型，取值 `True` / `False` |
| `int8` / `uint8` | 8 位（1 字节）有符号 / 无符号整型 |
| `int16` / `uint16` | 16 位（2 字节）整型 |
| `int32` / `uint32` | 32 位（4 字节）整型 |
| `int64` / `uint64` | 64 位（8 字节）整型 |
| `float16` | 半精度浮点 |
| `float32` | 单精度浮点 |
| `float64` | 双精度浮点（**默认浮点类型**） |
| `complex64` | 由两个 32 位浮点组成的复数 |
| `complex128` | 由两个 64 位浮点组成的复数 |

### 1.4 ndarray 的常用属性

| 属性 | 含义 | 示例 |
| --- | --- | --- |
| `shape` | 数组形状（各维度长度） | `arr.shape` |
| `ndim` | 维度数量 | `arr.ndim` |
| `size` | 总元素个数 | `arr.size` |
| `dtype` | 元素类型 | `arr.dtype` |
| `T` | 转置 | `arr.T` |
| `itemsize` | 单个元素占的字节数 | `arr.itemsize` |
| `nbytes` | 数组总内存占用量 | `arr.nbytes` |
| `flags` | 内存存储方式（如是否连续） | `arr.flags` |

---

## 第2章 ndarray 的创建与访问

### 2.1 创建方法

**基础构造**：`np.array(列表/嵌套列表)` 把 Python 序列变成数组；`np.copy(arr)` 做深拷贝。

**预定义形状填充**：

- 全 0：`np.zeros(shape)`
- 全 1：`np.ones(shape)`
- 固定值：`np.full(shape, 值)`
- 未初始化（值是内存里的随机垃圾，别直接用）：`np.empty(shape)`

**基于数值范围生成**：

- `np.arange(开始, 结束, 步)` —— **左闭右开，取不到结束值**，常用于时间序列、坐标网格
- `np.linspace(开始, 结束, 份数)` —— **包含两端点**，等间隔取 `份数` 个点
- `np.logspace(开始, 结束, 份数, base=底数)` —— 对数间隔；`base` 不写默认以 10 为底

**特殊矩阵生成**：

- 单位矩阵（主对角线为 1，其余为 0）：`np.eye(n)`
- 对角矩阵（只有对角线有值）：`np.diag([...])`

**随机数组生成**：

- 0~1 均匀分布：`np.random.rand(行, 列)`
- 指定区间均匀浮点：`np.random.uniform(开始, 结束, (行, 列))`
- 指定区间随机整数：`np.random.randint(开始, 结束, (行, 列))`
- 标准正态分布（均值 0、方差 1）：`np.random.randn(行, 列)`
- **设置随机种子**：`np.random.seed(数字)` —— 同一种子下生成的随机数组相同，便于复现实验结果

**高级构造方法**（原笔记图片补充）：`np.fromfunction(函数, shape)` 按坐标生成、`np.loadtxt('文件')` 从文本文件读入。


### 2.2 索引与切片

**一维数组**（从 0 开始）：

```python
arr[0]            # 取下标 0 的元素
arr[:]            # 取全部
arr[开始:结束]     # 左闭右开，取不到「结束」下标，所以要多取一个
arr[(arr > 10) & (arr < 60)]   # 布尔筛选：& 表示「和」、| 表示「或」
arr[slice(开始, 结束, 步)]      # 等价于 arr[开始:结束:步]，步可省略
```

**二维数组**：`arr[行, 列]` 这种逗号写法才是 numpy 的「同时指定行和列」，和 Python 列表的 `arr[行][列]` 不同。

```python
arr[行, 列]        # 取某个具体元素
arr[:, :]         # 取全部
arr[1, :]         # 取第 1 行全部
arr[1, 2:5]       # 取第 1 行、第 2 到第 4 列（左闭右开）
```


### 2.3 数组的运算

- **逐元素运算**：两个同形状数组的 `+ - * /` 是**对应位置元素**相加/相减/相乘/相除；而原生 Python 列表的 `+` 是**拼接**，语义完全不同。
- **数组 + 标量**：数组里每个元素都和这个标量做一次运算（加减乘除同理）。
- **广播（broadcast）**：当两个数组形状不完全一致时，numpy 会按规则「拉伸」较小数组使其兼容：

  1. 从**最右边**的维度开始对齐；
  2. 对应维度**相等**、或**其中一个为 1**，就能广播；否则报错。

```python
import numpy as np
a = np.array([[1, 2, 3],
              [4, 5, 6]])     # shape (2, 3)
b = np.array([10, 20, 30])    # shape (3,)
a + b
# b 沿 axis=0 广播成 (2, 3)：每一行都加上 [10, 20, 30]
# 结果：
# [[11, 22, 33],
#  [14, 25, 36]]
```

- **矩阵乘法**：用 `@` 符号（不是 `*`，`*` 是逐元素乘）：`a @ b`。

### 2.4 视图与拷贝（极易踩坑）

::: danger 易错点 · 切片返回「视图」
numpy 里**切片返回的是原数组的视图（view），共享同一块内存**；而**花式索引（整数数组）和布尔索引返回的是拷贝（copy），相互独立**。改了视图，原数组也会跟着变——这常常让人困惑。

```python
import numpy as np
a = np.arange(6)          # [0 1 2 3 4 5]
v = a[1:4]                # 视图，和 a 共享内存
v[0] = 999
print(a)                  # [0 999 2 3 4 5]  ← 原数组被改了！

c = a[[1, 2, 3]]          # 花式索引，是独立拷贝
c[0] = 0
print(a)                  # 不受影响，仍是 [0 999 2 3 4 5]
```

如果确实想要一份独立副本，用 `a.copy()`。
:::

---

## 第3章 numpy 常用函数

### 3.1 基本数学函数

| 函数 | 作用 |
| --- | --- |
| `np.sqrt(x)` | 平方根 |
| `np.exp(x)` | e 的 x 次幂 |
| `np.log(x)` | 自然对数（以 e 为底，即 ln x） |
| `np.sin(x)` / `np.cos(x)` | 正弦 / 余弦 |
| `np.abs(x)` | 绝对值 |
| `np.power(a, b)` | a 的 b 次幂 |
| `np.round(x)` | 四舍五入（见下方易错点：银行家舍入） |
| `np.ceil(x)` | 向上取整 |
| `np.floor(x)` | 向下取整 |
| `np.isnan(x)` | 检测缺失值（NaN） |

### 3.2 基本统计函数

| 函数 | 作用 |
| --- | --- |
| `np.sum` | 求和 |
| `np.mean` | 平均值 |
| `np.median` | 中位数 |
| `np.var` | 方差 |
| `np.std` | 标准差 |
| `np.max` / `np.min` | 最大值 / 最小值 |
| `np.argmax` / `np.argmin` | 最大值 / 最小值的**下标位置** |
| `np.percentile(x, q)` | 分位数，`q` 取 0~100 |
| `np.cumsum` / `np.cumprod` | 累积和 / 累积积 |

**按行 / 列统计**：`np.max(arr, axis=0)` 沿「行方向」压缩，返回**每一列**的最值；`axis=1` 沿「列方向」压缩，返回**每一行**的最值——别记反。


### 3.3 比较与逻辑函数

| 函数 | 作用 |
| --- | --- |
| `np.greater` / `np.less` | 是否大于 / 小于 |
| `np.equal` | 是否等于 |
| `np.logical_and` / `np.logical_or` / `np.logical_not` | 逻辑与 / 或 / 非 |
| `np.any` | 是否至少有一个元素为 `True` |
| `np.all` | 是否全部为 `True` |
| `np.where(条件, 符合, 不符合)` | 条件取值（类似三元运算的向量版） |

### 3.4 排序、去重、拼接与变形

- 排序：`np.sort(arr)` 返回新数组，**不改原数组**；`arr.sort()` **原地**修改原数组；`np.argsort(arr)` 返回排序后的下标。
- 去重：`np.unique(arr)`。
- 拼接：`np.concatenate([a, b])`；分割：`np.split(arr, 份数或位置)`。
- 变形：`np.reshape(arr, (行, 列))`。

---

## 第4章 pandas 之 Series

### 4.1 创建方式

```python
import pandas as pd
s = pd.Series([1, 2, 3])                       # 默认从 0 开始的整数索引
s = pd.Series([1, 2, 3], index=['a', 'b', 'c'])  # 自定义标签索引
s = pd.Series({'a': 1, 'b': 2, 'c': 3})          # 用字典创建，键即索引
```

### 4.2 属性与访问数据

| 属性 / 方法 | 含义 | 示例 |
| --- | --- | --- |
| `index` | 索引对象 | `s.index` |
| `values` | 值（numpy 数组） | `s.values` |
| `dtype` | 元素类型 | `s.dtype` |
| `shape` / `ndim` / `size` | 形状 / 维度 / 元素个数 | `s.shape` |
| `name` | 名称 | `s.name` |
| `loc[]` | 按**标签**索引或切片 | `s.loc['a']` |
| `iloc[]` | 按**位置**索引或切片（从 0 开始） | `s.iloc[0]` |
| `at[]` / `iat[]` | 按标签 / 按位置访问**单个**元素 | `s.at['a']` / `s.iat[0]` |

访问数据的几种方式：

```python
s['标签名']        # 按标签访问
s[条件]            # 布尔索引，直接得到索引和对应值
s.head(n)          # 看前 n 条，不填默认前 5 条
s.tail(n)          # 看后 n 条，不填默认后 5 条
```

带 `i` 的（`iloc` / `iat`）按**位置**，不带 `i` 的（`loc` / `at`）按**标签**——记住这一条就不会混。

### 4.3 常用方法

| 方法 | 作用 |
| --- | --- |
| `s.describe()` | 查看计数、均值、标准差等描述信息 |
| `s.count()` | 元素个数（**忽略缺失值**） |
| `s.isna()` / `s.isin()` | 判断是否为缺失值 / 是否在集合中 |
| `s.mean()` / `s.std()` / `s.var()` / `s.sum()` / `s.max()` / `s.median()` | 各类统计 |
| `s.sort_values()` / `s.sort_index()` | 按值排序 / 按索引排序 |
| `s.quantile()` | 分位数（填 **0~1** 的数，和 numpy 不同） |
| `s.mode()` | 众数 |
| `s.value_counts()` | 每个元素出现的次数 |
| `s.drop_duplicates()` / `s.unique()` | 去重（返回类型不同） |
| `s.nunique()` | 去重后的元素个数 |
| `s.diff()` | 相邻元素之差；`s.diff().abs()` 取差值绝对值 |

时间序列相关：

```python
idx = pd.date_range('2024-01-01', periods=10, freq='D')   # 生成日期索引，D=天
s.resample('M').mean()     # 重采样，M=按月求均值（也可用 Y 年 / Q 季 / W 周）
```

::: danger 易错点 · Series 运算按「标签」对齐
两个 Series 相加时，pandas 是**按索引标签对齐后再相加**，而不是按位置！标签对不上的位置会变成 `NaN`。这是 pandas 和 numpy 最容易被忽略的区别。

```python
import pandas as pd
s1 = pd.Series([1, 2, 3], index=['a', 'b', 'c'])
s2 = pd.Series([10, 20, 30], index=['c', 'b', 'a'])   # 顺序故意打乱
s1 + s2
# a    31   (1 + 30)
# b    22   (2 + 20)
# c    13   (3 + 10)
# dtype: int64
```
:::

---

## 第5章 pandas 之 DataFrame

### 5.1 创建方式

```python
import pandas as pd
# 由多个 Series 组成（键是列名）
df = pd.DataFrame({'列1': s1, '列2': s2})
# 由字典创建，可指定索引和列顺序
df = pd.DataFrame({'a': [1, 2], 'b': [3, 4]},
                  index=['x', 'y'],
                  columns=['a', 'b'])
```

### 5.2 属性与访问数据

| 属性 / 方法 | 含义 | 示例 |
| --- | --- | --- |
| `columns` | 列标签 | `df.columns` |
| `T` | 转置 | `df.T` |
| `loc[行, 列]` | 按**标签**访问 | `df.loc['x', 'a']` |
| `iloc[行, 列]` | 按**位置**访问 | `df.iloc[0, 0]` |
| `at[行, 列]` / `iat[行, 列]` | 按标签 / 位置访问单个值 | `df.at['x','a']` |

访问数据：

```python
df['列名']            # 取单列，返回 Series
df.列名               # 同上（列名是合法标识符时可用）
df[['列1', '列2']]    # 取多列，返回 DataFrame
df.head() / df.tail() # 看前 / 后 n 行，不填默认 5 行
df.sample(n)          # 随机抽样 n 条；不填参数默认只取 1 条
```

### 5.3 常用方法

| 方法 | 作用 |
| --- | --- |
| `df.head()` / `df.tail()` | 查看前 / 后 n 行 |
| `df.isin([...])` / `df.isna()` | 判断元素是否在集合中 / 是否为缺失值 |
| `df['列'].sum()` / `.mean()` / `.max()` / `.min()` / `.median()` / `.mode()` / `.var()` / `.std()` / `.quantile()` | 对某一列做统计 |
| `df.describe()` | 描述信息（数值列的统计概览） |
| `df.value_counts()` | 元素出现次数 |
| `df.drop_duplicates()` / `df.duplicated()` | 去重 / 查看是否重复 |
| `df.replace(...)` | 替换元素 |
| `df.cumsum()` | 累计和 |
| `df.sort_index(ascending=False)` | 按索引排序（`True` 升序，`False` 降序，默认升序） |
| `df.sort_values(by='列', ascending=...)` | 按值排序，可传多列列表做多条件排序 |
| `df.nlargest(n, columns=['列'])` / `df.nsmallest(n, columns=['列'])` | 返回最大 / 最小的 n 行 |



---

## 第6章 数据分析实战

### 6.1 数据的导入与导出

```python
import pandas as pd
df = pd.read_csv('文件夹/文件名.csv')     # 读 CSV
df.to_csv('文件夹/文件名.csv')            # 导出 CSV
df = pd.read_json('文件夹/文件名.json')   # 读 JSON
```

```python
import json
with open('文件.json', encoding='utf-8') as f:
    data = json.load(f)                  # 读到字典，再转成 DataFrame
```

::: danger 易错点 · dropna / fillna 默认不改原表
`dropna()`、`fillna()` 等**默认返回新对象，不会修改原 DataFrame**。如果想像「就地修改」一样，要么把结果赋回原变量 `df = df.dropna()`，要么加 `inplace=True`（如 `df.dropna(inplace=True)`）。
:::
