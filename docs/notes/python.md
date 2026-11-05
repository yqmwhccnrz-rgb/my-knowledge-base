---
summary: "9 章 Python 数据分析笔记：ndarray、numpy 函数、Series 与 DataFrame、数据清洗、分组聚合与可视化；修正了原笔记的若干错误，并补充视图/拷贝、标签对齐、apply/merge、透视表等实战知识点。"
---

# Python 数据分析笔记

> **这是一篇笔记**：9 章内容连续排在同一页，从上往下读即可；也可以点右侧「本页目录」跳到任意章节。

这份笔记由你的《python 数据分析.pdf》重排而来：原来的章节顺序、知识点、代码与表格都保留了，原 PDF 文字层缺失的汉字（如「导/入」「生成」「方差」等）已按上下文补全，**不准确的说法已修正**，并**补充**了大量原笔记略过但实战必备的内容（文中以「补充」「修正」标出，便于区分哪些是新增、哪些是你原来的）。

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

::: danger 修正 · 布尔类型的含义
原笔记里写「布尔类型 bool：0 为 True，0 为 False」，这句是**错的**。正确说法是：在 Python / numpy 中，**`0` 对应 `False`，非 0（包括负数）对应 `True`**。`True` 和 `False` 本身才是布尔值，参与数值运算时分别当作 `1` 和 `0`。
:::

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

::: tip 补充 · 创建方法一览表
| 用途 | 方法 |
| --- | --- |
| 基础构造 | `np.array()`、`np.copy()` |
| 预定义形状填充 | `np.zeros()`、`np.ones()`、`np.empty()`、`np.full()` |
| 基于数值范围生成 | `np.arange()`、`np.linspace()`、`np.logspace()` |
| 特殊矩阵生成 | `np.eye()`、`np.diag()` |
| 随机数组生成 | `np.random.rand()`、`np.random.randn()`、`np.random.randint()` |
| 高级构造方法 | `np.fromfunction()`、`np.loadtxt()` |
:::

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

::: tip 补充 · 索引切片类型
| 类型 | 说明 |
| --- | --- |
| 基本索引 | 用整数下标直接访问元素，索引从 0 开始 |
| 行 / 列切片 | 用冒号 `:` 选择行或列的子集 |
| 连续切片 | `start:stop:step`，从起始到结束按步长切片 |
| `slice` 函数 | `slice(start, stop, step)` 定义切片规则 |
| 布尔索引 | 用布尔条件筛选满足条件的元素，支持 `&`、`|` |
:::

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

::: danger 易错点 + 补充 · 切片返回「视图」
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

::: tip 补充 · NaN 会「传染」
含 `NaN` 的数组，直接 `np.sum` / `np.mean` 结果往往是 `NaN`。numpy 提供了一批「忽略 NaN」的版本：`np.nansum`、`np.nanmean`、`np.nanmax` 等，计算时会自动跳过 NaN。pandas 的统计方法默认 `skipna=True`（自动跳过），但 `np` 不会，这点要注意。
:::

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

::: danger 易错点 + 补充 · Series 运算按「标签」对齐
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

::: tip 补充 · 元素级变换：map / apply / applymap
原笔记没提这一组，但它们是数据清洗最常用的手段：

```python
s = pd.Series(['a', 'b', 'c'])
s.map({'a': 1, 'b': 2})          # 映射：按字典把值替换掉
s.apply(lambda x: x.upper())      # 对每个元素套用函数

df.apply(lambda col: col.mean())  # 默认按列套用函数，返回 Series
df.apply(lambda row: row['a'] + row['b'], axis=1)  # axis=1 按行套用
df.map(lambda x: x * 2)           # 逐元素变换（新版 pandas；老版叫 applymap）
```
:::

::: tip 补充 · 合并多张表：concat / merge / join
真实分析经常要把几张表拼起来，原笔记只讲了 numpy 的拼接，这里补上 pandas 的三板斧：

```python
pd.concat([df1, df2])            # 纵向拼接（按行叠）
pd.concat([df1, df2], axis=1)    # 横向拼接（按列并）
pd.merge(df1, df2, on='key')     # 按「键」做数据库式连接（类似 SQL 的 join）
df1.join(df2)                    # 按索引连接
```
:::

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

::: danger 修正 · 中文乱码
原笔记把「中文乱码」打成「中件乱码」，这里补正并给出稳妥方案。读取含中文的 CSV 若乱码，优先确认原文件编码再指定：

```python
pd.read_csv('文件.csv', encoding='utf-8')       # 标准 UTF-8
pd.read_csv('文件.csv', encoding='utf-8-sig')   # 带 BOM 的 UTF-8（Excel 导出常见）
pd.read_csv('文件.csv', encoding='gbk')         # 中文 Windows 导出的 GBK
```

::: tip 补充 · read_csv 常用参数
除了 `encoding`，这几个参数实战最高频：

```python
pd.read_csv('data.csv',
            sep=',',            # 分隔符，制表符文件用 '\t'
            header=0,           # 哪一行当列名，没有列名用 header=None
            index_col=0,        # 用第几列当行索引
            usecols=['a', 'b'], # 只读取指定列，省内存
            dtype={'id': str},  # 指定某列类型，避免 ID 被当成数字丢前导 0
            na_values=['NA', '?'],  # 把这些都认作缺失值
            parse_dates=['date'])   # 自动把某列解析成日期
```
:::

### 6.2 缺失值的处理

判断与统计：

```python
s.isna() / s.isnull()        # Series：两者完全等价
df.isna() / df.isnull()      # DataFrame：两者完全等价
s.isna().sum()               # Series 缺失值总数
df.isna().sum()              # 每列缺失值个数
df.isna().sum().sum()        # 全表缺失值总数
```

剔除缺失值：

```python
s.dropna()                   # 删除缺失的那一个值
df.dropna()                  # 只要有缺失就删掉整行
df.dropna(how='all')         # 只有整行全缺失才删
df.dropna(thresh=n)          # 至少有 n 个非缺失值才保留
df.dropna(axis=1)            # 删除有缺失的整列
df.dropna(subset=['列名'])   # 仅当指定列有缺失时才删该行
```

填充缺失值：

```python
df.fillna({'列名': 固定值})        # 用固定值填（按列指定）
df.fillna(df[['列名']].mean())    # 用该列平均值填
df.ffill()                        # 用前一个相邻值填（forward fill）
df.bfill()                        # 用后一个相邻值填（backward fill）
```

::: danger 易错点 + 补充 · dropna / fillna 默认不改原表
`dropna()`、`fillna()` 等**默认返回新对象，不会修改原 DataFrame**。如果想像「就地修改」一样，要么把结果赋回原变量 `df = df.dropna()`，要么加 `inplace=True`（如 `df.dropna(inplace=True)`）。
:::

### 6.3 重复值的处理

```python
df.duplicated()                          # 整行都相同的标记为重复（返回 True）
df.drop_duplicates()                     # 删除重复行
df.drop_duplicates(subset=['列名'])      # 按指定列判断重复
df.drop_duplicates(subset=['列名'], keep='last')  # 保留最后一次出现的
```

### 6.4 数据类型转换与数据变形

```python
df['列名'].astype('类型')               # 数值类型转换
df.T                                     # 转置
# 宽表 → 长表
pd.melt(df, id_vars=['不变列'], var_name='新列名', value_name='新值名')
# 长表 → 宽表
pd.pivot(df, index=['不变列'], columns='当列名', values='当值')
# 分列：按空格或 / 拆分，expand=True 展开成多列
df['列'].str.split(' ', expand=True)
```

数据分箱（把连续值变离散）：

```python
# 等距划分
pd.cut(数据, bins=5, labels=['低','中','高','高','高'])   # 整数=均分 n 段
pd.cut(数据, bins=[0, 18, 35, 60, 100], labels=[...])    # 自定义区间边界
# 等频划分（每段样本数大致相等）
pd.qcut(数据, 4)
```

修改列名 / 索引名：

```python
df.rename(columns={'旧': '新'}, index={'旧': '新'})
df.columns = ['a', 'b', 'c']     # 直接整体重命名，要写全所有列
df.index = [0, 1, 2]             # 整体重设索引，要写全
df.set_index('列名', inplace=True)
```

::: tip 补充 · 透视表与交叉表
`pivot` 只是「长转宽」的形状变换；真正的**分组聚合透视**用 `pivot_table`，它能对值做聚合（默认求均值）：

```python
df.pivot_table(index='地区', columns='年份', values='销量', aggfunc='sum')
pd.crosstab(df['地区'], df['渠道'])   # 交叉表：统计两维组合的频数
```
:::

### 6.5 时间数据的处理

```python
import pandas as pd
d = pd.Timestamp('2024-01-01 08:30')   # 单个时间戳
d.year / d.month / d.day / d.hour / d.minute / d.second   # 取各字段
d.quarter                              # 季度（1~4）
d.is_month_end                         # 是否月末
d.day_name()                           # 星期几
d.to_period('M')                       # 以月(M)/季(Q)/年(Y)/周(W)/天(D)为维度

pd.to_datetime('2024-01-01')                       # 字符串 → 时间戳
df['新列'] = pd.to_datetime(df['列'])               # 整列转换
pd.to_datetime(df['列'], errors='coerce')           # 解析失败填 NaT 而不是报错

df.set_index('date', inplace=True)                  # 把日期设为索引
d2 - d1                                            # 时间戳相减，得到时间差（天数）
pd.date_range('开始', '结束', freq='D')             # 按区间生成日期序列，D=天 W=周 Q=季
pd.date_range('开始', periods=10, freq='D')         # 生成指定个数的日期序列
```

::: tip 补充 · Series.dt 访问器
把列解析成 datetime 后，可以用 `.dt` 一次性提取整列的年月日等：

```python
df['date'] = pd.to_datetime(df['date'])
df['year']  = df['date'].dt.year
df['month'] = df['date'].dt.month
df['weekday'] = df['date'].dt.dayofweek   # 周几（0=周一）
```
:::

### 6.6 分组聚合

```python
df.groupby('分组字段')['聚合字段'].mean()        # 按字段分组后求均值
df.groupby('字段').groups                       # 查看分组情况
df.groupby('字段').get_group('组名')             # 取某个具体分组
df.groupby(['字段1', '字段2'])['字段'].sum()     # 多条件分组聚合
```

::: tip 补充 · 聚合函数进阶
除了 `mean()` / `sum()`，还能用 `count()`、`max()`、`min()`；用 `agg` 可以**一次算多个指标**，也能传自定义函数：

```python
df.groupby('部门')['工资'].agg(['mean', 'sum', 'max'])      # 多指标
df.groupby('部门')['工资'].agg(极差=lambda x: x.max() - x.min())
```
注意 `size()`（统计每组行数，含缺失）和 `count()`（统计非缺失个数）的区别。
:::

---

## 第7章 数据可视化

### 7.1 图表构成与工具对比

一张图通常由：标题、坐标轴、图形要素、图例、数据标签组成。

常用工具：

- **matplotlib**：底层、灵活，几乎所有图都能画，但代码偏多。
- **seaborn**：基于 matplotlib 的高级封装，统计类图表（分布、关系）几行就能出好看的效果。

### 7.2 matplotlib

```python
import matplotlib.pyplot as plt
```

通用流程（各类图基本一致）：创建画布 → 绘图 → 加标题 / 坐标轴标签 / 图例 / 网格 → 设刻度字体 / 范围 → 显示。

```python
# 折线图（看趋势）
plt.figure(figsize=(8, 4))
plt.plot(x, y, label='图例名', color='red', linewidth=2,
         linestyle='--', marker='o')     # marker='o' 把每个点画成圆点
plt.title('标题', fontsize=14)
plt.xlabel('x 轴', fontsize=12)
plt.ylabel('y 轴', fontsize=12)
plt.legend(loc='upper left')             # 图例位置
plt.grid(axis='y', alpha=0.3, linestyle='--')
plt.xticks(rotation=45, fontsize=10)     # 旋转 x 轴刻度
plt.ylim(0, 100)                         # 设 y 轴范围
for xi, yi in zip(x, y):                 # 在每个点上标数值
    plt.text(xi, yi, str(yi), ha='center', va='bottom', fontsize=10)
plt.show()
```

其他图：

```python
plt.bar(x, y, width=0.6, color='blue')     # 柱状图（看对比）
plt.barh(x, y)                             # 条形图（x/y 轴互换）
plt.pie(数据, labels=标签, autopct='%.1f%%',   # 饼图（看占比）
        startangle=90, explode=[0, 0.1, 0], shadow=True)
plt.scatter(x, y, alpha=0.6, s=30)         # 散点图（看两变量相关性）
plt.boxplot(值, tick_labels=标签)          # 箱线图（看分布与异常）
```

多图绘制：`f = plt.subplot(行, 列, 第几个)`，或一次性建多个子图：

```python
fig, axes = plt.subplots(2, 1, figsize=(8, 6))   # 2 行 1 列
axes[0].plot(x, y1)
axes[1].scatter(x, y2)
plt.tight_layout()                                # 自动优化排版
```

::: danger 修正 + 补充 · 中文显示与负号
原笔记只给了 `STHeiti` 一种字体，在 Windows / Linux 上会失效。更稳妥的做法是同时指定多个候选字体，并关掉 unicode minus（否则负号会显示成方块）：

```python
plt.rcParams['font.sans-serif'] = ['SimHei', 'PingFang SC', 'Microsoft YaHei', 'Arial']
plt.rcParams['axes.unicode_minus'] = False    # 解决负号显示为方块
```
用 seaborn 时同理：`sns.set_theme(style='whitegrid')` 会套用其默认字体，中文乱码时再叠加上面的 `rcParams` 设置即可。
:::

::: tip 补充 · 双坐标轴
左右两个量纲不同的指标想画在同一张图时，用 `twinx()` 共享 x 轴、再开一条 y 轴：

```python
ax1 = plt.gca()
ax1.bar(x, y1, color='skyblue')
ax2 = ax1.twinx()
ax2.plot(x, y2, color='orange')
```
:::

### 7.3 seaborn

```python
import seaborn as sns
sns.set_theme(style='whitegrid')             # 设整体主题风格
```

| 函数 | 作用 |
| --- | --- |
| `sns.histplot(data, x=)` | 直方图（看分布） |
| `sns.kdeplot(data, x=)` | 核密度估计图 |
| `sns.countplot(data, x=)` | 计数图 |
| `sns.scatterplot(data, x=, y=, hue=)` | 散点图（hue 按某列分组着色） |
| `sns.jointplot(data, x=, y=)` | 联合分布图（散点 + 边缘分布） |
| `sns.barplot(data, x=, y=)` | 条形图 |
| `sns.boxplot(data, x=, y=)` | 箱线图 |
| `sns.pairplot(data)` | 成对关系图（多变量两两散点） |

::: tip 补充 · 箱线图怎么读
箱线图用来一眼看分布和异常值，各要素（含图片补充）如下：

| 要素 | 含义 / 计算 |
| --- | --- |
| 离群值（异常值） | 位于上下须之外的点，需结合实际判断是否处理 |
| 上边缘 | `Q3 + 1.5 × IQR` |
| 上四分位数 Q3 | 箱体上边界（数据的 75% 分位） |
| 中位数 Q2 | 箱体中间的横线（50% 分位） |
| 下四分位数 Q1 | 箱体下边界（25% 分位） |
| 下边缘 | `Q1 − 1.5 × IQR` |

其中 `IQR = Q3 − Q1`（四分位距）。超出 `Q3 + 1.5×IQR` 或低于 `Q1 − 1.5×IQR` 的点通常被标记为离群值。
:::

---

## 第8章 易错点汇总

1. **切片与范围（左闭右开）**：`arr[开始:结束]` 取不到「结束」下标，要多取一个；`np.arange` 的结束值同样取不到，`np.linspace` 才包含两端点。
2. **list 与 ndarray 的加法**：原生 `list` 的 `+` 是拼接，`ndarray` 的 `+` 是逐元素相加，语义完全不同。
3. **`np.round` 银行家舍入**：采用「四舍六入五取偶」——`np.round(0.5) = 0`、`np.round(1.5) = 2`，和直觉的「≤4 舍去」不一样。
4. **`axis` 的方向**：`np.max(arr, axis=0)` 返回每列的极值（沿行方向压缩）；`axis=1` 返回每行的极值（沿列方向压缩），别记反。
5. **布尔索引的多条件**：多条件筛选用 `&` / `|`（不能写 `and` / `or`），且每个条件必须加括号：`arr[(arr > 10) & (arr < 60)]`。
6. **分位数参数区间**：pandas 的 `s.quantile()` 填 **0~1** 的数，numpy 的 `np.percentile()` 填 **0~100** 的数，两者不一样。
7. **去重与计数**：`drop_duplicates()` 与 `unique()` 内容一样但返回类型不同；`count()` 忽略缺失值；`df.sample()` 不填参数默认只取 1 条。
8. **排序**：`np.sort` 不改原数组，`arr.sort()` 原地改；`sort_values` 按值、`sort_index` 按索引，别混。
9. **（补充）切片返回视图**：`arr[1:4]` 这类切片和原数组共享内存，改了会影响原数组；要独立副本用 `arr.copy()`。
10. **（补充）Series 按标签对齐**：两个 Series 相加是按索引标签对齐、不是按位置，对不上的变 `NaN`。
11. **（补充）dropna / fillna 不改原表**：默认返回新对象，要么赋值回去，要么加 `inplace=True`。

---

## 第9章 知识点速查总结

### 9.1 核心脉络

> 数据收集 → 数据清洗 → 数据分析 → 数据可视化，一条线走完：`read_csv` 读 → `isna` / `dropna` / `fillna` 清洗 → `groupby` 聚合 → `plt` 绘图。

### 9.2 三大数据结构速查

| 结构 | 一句话 | 关键点 |
| --- | --- | --- |
| `ndarray` | numpy 多维数组 | 多维性、同质性、高效性 |
| `Series` | 一维带索引的数组 | 按标签 `loc` / 按位置 `iloc` |
| `DataFrame` | 多个 Series 组成的二维表格 | 行索引 `index` + 列名 `columns` |

### 9.3 高频函数速查

| 场景 | 函数 |
| --- | --- |
| 数组创建 | `np.arange`、`np.linspace`、`np.zeros`、`np.random.rand` |
| 数学函数 | `np.sqrt`、`np.exp`、`np.log`、`np.abs`、`np.round` |
| 统计函数 | `np.sum`、`np.mean`、`np.max(arr, axis=)`、`np.percentile` |
| 条件筛选 | 布尔索引 `arr[条件]`、`np.where` |
| 排序去重 | `np.sort`、`np.argsort`、`np.unique` |
| 缺失值 | `isna()`、`dropna()`、`fillna()`、`ffill()`、`bfill()` |
| 重复值 | `duplicated()`、`drop_duplicates()` |
| 数据变形 | `melt`、`pivot`、`cut`、`qcut`、`astype`、`set_index` |
| 合并表 | `pd.concat`、`pd.merge`、`df.join` |
| 时间处理 | `pd.Timestamp`、`pd.to_datetime`、`pd.date_range`、`resample` |
| 分组聚合 | `df.groupby('字段')['字段'].mean()`、`agg()` |

### 9.4 图表选型速查

| 想表达什么 | 用什么 |
| --- | --- |
| 数据趋势 | 折线图 `plt.plot` |
| 数据对比 | 柱 / 条形图 `plt.bar` / `plt.barh` |
| 占比 | 饼图 `plt.pie` |
| 两变量相关性 | 散点图 `plt.scatter` |
| 分布与异常 | 箱线图 `plt.boxplot` / `sns.histplot` |

### 9.5 易错点一句话版

- 切片与 `arange` 左闭右开；`np.round` 五取偶（银行家舍入）
- `axis=0` 沿行方向压缩（求每列）；`axis=1` 沿列方向压缩（求每行）
- `quantile` 参数是 0~1，`np.percentile` 是 0~100
- 布尔多条件用 `&` / `|`，且每个条件要加括号
- `df.sample()` 不填参数默认只取 1 条
- `count()` 忽略缺失值；`sort_values` 按值、`sort_index` 按索引
- 切片返回视图（共享内存），要副本用 `copy()`；Series 相加按标签对齐；`dropna` / `fillna` 默认不改原表
