---
summary: "数据库原理及应用 全面详解笔记，共 17 章：数据库系统概述、关系数据库、SQL 与 MySQL 基础、数据库创建与管理、数据表管理与数据操纵、数据查询、视图与索引、安全性管理、并发控制与封锁、备份还原与日志、数据库设计概述与需求分析、关系模式规范化理论、概念结构与逻辑结构设计、物理设计与运行维护、存储过程与函数、触发器与事件、编程语言连接 MySQL。覆盖三级模式两级映像、关系代数与完整性约束、DDL/DML/DQL/DCL、多表连接与子查询、B+树索引与最左前缀、事务 ACID 与隔离级别、MVCC 与两段锁、备份恢复与 binlog/redo/undo、函数依赖与 1NF–BCNF/4NF、ER 图向关系模式转换、数据库设计六阶段、存储过程/触发器/事件与预处理防注入。含 19 张自绘图、大量可运行 SQL 示例与工作例题、跨章综合题、语法速查与 92 条易错点，并对课件中的缺漏与笔误作了补充修正。"
---

# 数据库原理及应用笔记

::: info 笔记概要
- **所属课程**：数据库原理及应用（计算机类 / 软件工程等专业核心基础课）。
- **核心内容**：以「**关系数据库**」为主线——先用三级模式与数据独立性说明数据库系统为何这样组织，再用关系模型与关系代数建立数学基础，接着落到 SQL 与 MySQL 的库表管理、查询、视图索引，然后进入**共享与可靠**（安全、事务并发、备份恢复），最后回到**设计方法论**（需求分析 → 概念/逻辑/物理设计 → 规范化）与**服务端编程**（存储过程、触发器、事件、程序连接）。重点抓三条线：① **结构与抽象**（三级模式、关系模式、ER 模型）；② **语言与手算**（SQL 各子句执行顺序、关系代数表达式、范式分解、事务调度可串行化）；③ **机制与权衡**（索引加速与写入代价、隔离级别与并发性、规范化与反规范化、备份粒度与恢复时间）。
- **学习建议**：每条 SQL 都要能回答「先执行哪个子句、中间结果是什么、NULL 如何处理」；每个范式都要能举出「异常 → 函数依赖 → 分解」的完整链条；每个设计决策都要说明「牺牲了什么换来了什么」。本笔记在系统学习课程课件的基础上，补齐了课件未展开的实现机制、标准术语与可运行示例，并对课件中缺漏或不够严谨的内容作了补充与订正说明。
- **本版说明**：**全面详解版**——17 章正文之外，设深挖专题、跨章综合例题精讲、易混概念对照表与「补充与修正汇总」逐条列出课件缺漏与订正；19 张自绘图均已逐格核对，每章配对比表、可运行 SQL 示例、带结果的工作例题、`danger` 易错辨析与 `tip` 补充；附录 A 为语法公式速查，附录 B 为 92 条易错点。文中「课件修正」标注课件本身需订正之处，「补充」标注课件未展开但应掌握的现代知识。
:::

## 全书目录

| 章 | 主题 | 核心考点 | 重要度 |
| --- | --- | --- | --- |
| 1 | 数据库系统概述 | 数据/信息/DB/DBMS/DBS、数据管理三阶段、三级模式两级映像、数据独立性 | ★★★ |
| 2 | 关系数据库 | 关系与关系模式、码、三类完整性、关系代数八运算、关系演算 | ★★★ |
| 3 | SQL 与 MySQL 基础 | SQL 特点与分类（DDL/DML/DQL/DCL）、MySQL 体系与执行流程 | ★★★ |
| 4 | 数据库创建和管理 | 存储引擎、CREATE/ALTER/DROP DATABASE、字符集与校对规则 | ★★ |
| 5 | 数据表管理与数据操纵 | 数据类型、六类约束、CREATE/ALTER TABLE、INSERT/UPDATE/DELETE | ★★★ |
| 6 | 数据查询 | SELECT 子句与执行顺序、WHERE、GROUP BY/HAVING、连接、子查询、集合运算 | ★★★ |
| 7 | 视图和索引 | 视图定义与可更新条件、B+树索引、聚簇/二级索引、最左前缀与覆盖索引 | ★★★ |
| 8 | 数据库安全性管理 | 用户/权限/角色、GRANT/REVOKE、权限层级、SQL 注入与最小权限 | ★★★ |
| 9 | 并发控制与封锁 | 事务 ACID、四类并发异常、四种隔离级别、X/S 锁、三级封锁协议、2PL、MVCC | ★★★ |
| 10 | 备份还原和日志管理 | 备份分类、mysqldump、binlog/redo/undo、恢复与主从复制 | ★★★ |
| 11 | 数据库设计与需求分析 | 设计六阶段、需求分析、数据流图与数据字典 | ★★ |
| 12 | 关系模式规范化理论 | 函数依赖、Armstrong 公理、1NF–BCNF/4NF、无损连接与保持依赖分解 | ★★★ |
| 13 | 概念结构与逻辑结构设计 | ER 图、联系类型、冲突合并、ER 向关系模式转换 | ★★★ |
| 14 | 物理设计、实施与运维 | 索引选择、聚簇与分区、实施、试运行与维护、性能调优 | ★★ |
| 15 | 存储过程与函数 | 编程基础、内置函数、存储过程、自定义函数、游标 | ★★★ |
| 16 | 触发器和事件 | 触发器 BEFORE/AFTER、NEW/OLD、事件调度器 | ★★ |
| 17 | 编程语言连接 MySQL | 连接 API、游标、事务、预处理语句、连接池 | ★★★ |
| 补 | 补充与修正汇总 | 课件缺漏订正与现代数据库技术 | ★★ |
| 综 | 综合例题精讲 | 跨章 SQL、规范化、ER 设计、事务调度大题 | 复习用 |
| 附 A / B | 速查 | SQL 语法公式速查表、92 条易错点清单 | 复习用 |

---

## 第 1 章 数据库系统概述

### 1.1 基本概念与数据管理技术的发展（★★）

| 概念 | 含义 |
| --- | --- |
| 数据 Data | 描述事物的符号记录（数字、文字、图像、音频…），是信息的载体 |
| 信息 Information | 数据经加工后对人有用的知识；具有可感知、可存储、可传递、可加工等特征 |
| 数据库 DB | **长期存储**在计算机内、**有组织**、**可共享**、**统一管理**的相关数据集合 |
| 数据库管理系统 DBMS | 位于用户与 OS 之间的一层数据管理软件：定义、操纵、控制、维护数据库 |
| 数据库系统 DBS | 数据库 + DBMS + 应用系统 + 数据库管理员 DBA + 用户 + 硬件/软件平台 |
| 数据处理 | 对数据进行收集、存储、加工、传播；**数据管理**是其中的核心（分类、组织、编码、存储、检索、维护） |

| 阶段 | 特点 | 问题 |
| --- | --- | --- |
| 人工管理（20 世纪 50 年代前） | 数据不保存、由应用程序自带、无专门软件 | 数据不共享、冗余大、数据与程序不独立 |
| 文件系统（50 年代后期–60 年代） | 数据以文件长期保存、由文件系统管理 | 共享性差、冗余大、**数据与程序独立性差**、文件间无联系 |
| **数据库系统（60 年代后期起）** | 数据结构化、共享性高冗余低、**数据独立性高**、由 DBMS 统一管理与控制 | 需要专门的软件与 DBA，系统复杂 |

DBMS 的主要功能：① **数据定义**（DDL）；② **数据操纵**（DML）；③ **数据库运行管理**（并发、安全、完整性、事务）；④ **建立与维护**（转储、恢复、重组织、性能监视）；⑤ 数据通信与转换。

![数据库系统组成与三级模式两级映像](/db/db-architecture.svg)

### 1.2 三级模式结构与两级映像（★★★）

| 层次 | 又称 | 描述 | 数量 |
| --- | --- | --- | --- |
| **外模式** | 子模式 / 用户模式 | 某个用户或应用看到并使用的**局部**数据的逻辑结构与特征 | 每个数据库可有多个 |
| **模式** | 概念模式 / 逻辑模式 | 全体数据的**整体**逻辑结构与特征，是所有用户的公共数据视图 | **只有一个** |
| **内模式** | 存储模式 | 数据的物理存储结构与存储方式（索引、压缩、加密、记录格式） | **只有一个** |

**两级映像**：
- **外模式／模式映像**：定义局部与全局逻辑结构的对应。模式改变（如加字段、加表）时，只需 DBA 改映像，**应用程序不必改** → 保证**逻辑独立性**。
- **模式／内模式映像**：定义逻辑结构与物理存储的对应。存储结构改变（换存储引擎、加索引、换文件组织）时，改映像即可 → 保证**物理独立性**。

::: tip 补充 · 课件未点明的「两级映像」意义（课件修正）
课件列出了三级模式的名称，但未把「两级映像」与「数据独立性」的因果关系讲透。答题标准链条是：
**三级模式 → 两级映像 → 数据独立性**。
其中「**模式只有一个、内模式只有一个、外模式可有多个**」是高频选择题考点；另外「视图」正是外模式在 SQL 中的实现手段（第 7 章）。
:::

::: danger 易错 · 数据独立性
- 「逻辑独立性」是**外模式/模式**映像给的；「物理独立性」是**模式/内模式**映像给的，别对调。
- 数据独立性 ≠ 数据不被修改，而是「**上一层不必随下一层改动而改写**」；应用程序基于外模式编写。
- 三级模式是**体系结构**概念；「关系模式」是第 2 章的**数据结构**概念，二者别混。
:::

### 1.3 数据模型与三个世界（★★）

| 世界 | 概念 | 对应模型 |
| --- | --- | --- |
| 现实世界 | 客观存在的事物及其联系 | — |
| 信息世界 | 实体、属性、联系、码、实体型、实体集 | **概念模型（E-R 模型）** |
| 计算机世界 | 记录、字段（数据项）、文件、关键字 | **逻辑模型 / 物理模型** |

数据模型三要素：**数据结构**（静态特性）、**数据操作**（动态特性）、**数据的完整性约束**（约束条件）。

| 逻辑模型 | 结构 | 优缺点 |
| --- | --- | --- |
| 层次模型 | 树形（一对多） | 查询效率高；不能直接表示多对多、插入删除限制多 |
| 网状模型 | 图（可多对多） | 能表示复杂联系；结构复杂、编程需了解物理路径 |
| **关系模型** | 二维表 | 数学基础扎实、结构简单、数据独立性高、集合操作；查询需优化 |
| 面向对象 / 对象关系 | 对象、类、继承 | 适合复杂数据类型；实现复杂 |
| E-R 模型 | 实体-联系图 | 属**概念模型**，用于设计阶段而非 DBMS 实现 |

::: tip 补充 · 现代数据库生态（课件提及「新技术与国产数据库」，此处系统展开）
- **NoSQL**：键值（Redis）、文档（MongoDB）、列族（HBase/Cassandra）、图（Neo4j）；用 BASE 与最终一致性换取水平扩展与灵活模式。
- **NewSQL / 分布式**：TiDB、OceanBase、CockroachDB、PolarDB；兼顾 SQL/ACID 与分布式扩展，常基于 Raft/Paxos + 分布式事务。
- **国产数据库**：达梦 DM、人大金仓 KingbaseES、openGauss、OceanBase、TiDB、PolarDB、GaussDB、TDSQL；多用于信创与政企核心系统。
- **云数据库 / HTAP / 湖仓一体**：RDS、Serverless DB、Aurora；OLTP 与 OLAP 融合（TiDB TiFlash）、Lakehouse（Iceberg/Hudi/Delta Lake）。
- **典型选型**：强事务与复杂查询 → 关系型；高并发简单键值缓存 → Redis；海量日志/时序 → 列族/时序库；关系网络 → 图数据库。
:::

---

## 第 2 章 关系数据库

### 2.1 关系模型的基本概念（★★★）

| 术语 | 定义 | SQL 对应 |
| --- | --- | --- |
| 域 Domain | 一组具有相同数据类型的值的集合 | 数据类型 + 取值约束 |
| 元组 Tuple | 笛卡尔积中的一个元素 | 一行 / 一条记录 |
| 属性 Attribute | 关系的一列，每列有域名 | 字段 / 列 |
| 关系 Relation | `D₁×D₂×…×Dₙ` 的**有限子集**，即元组的集合 | 表（严格说是满足规范化的二维表） |
| 关系模式 | `R(U, D, DOM, F)`，常简写 `R(A₁, A₂, …, Aₙ)` | `CREATE TABLE` 的表结构 |
| 关系数据库模式 | 全体关系模式的集合 | 数据库 schema |

**关系的六条性质**（区分「关系」与随便一张表）：① 列同质（同一列来自同一域）；② 不同列可同域但须不同名；③ 列的次序可换；④ 行的次序可换；⑤ **任意两元组不能完全相同**（集合无重复元素）；⑥ **每个分量必须是不可再分的原子值**（即满足 1NF，不允许「表中有表」）。

![关系模型、码与三类完整性](/db/db-relational.svg)

### 2.2 码与三类完整性约束（★★★）

| 码 | 定义 |
| --- | --- |
| 超码 Superkey | 能唯一标识元组的属性集（可能含多余属性） |
| **候选码 Candidate key** | 最小的超码（去掉任一属性即不再唯一），可有多个 |
| **主码 Primary key** | 从候选码中选定的一个，用于唯一标识元组 |
| 主属性 / 非主属性 | 包含在**任一候选码**中的属性 / 其余属性 |
| 全码 All-key | 关系模式的全部属性构成候选码 |
| **外码 Foreign key** | 本关系中不是主码、但对应另一关系主码的属性（组） |

| 完整性 | 规则 | 违反示例 |
| --- | --- | --- |
| **实体完整性** | 主码的任何属性**不能取 NULL 且不能重复** | 学生表插入两条相同学号 |
| **参照完整性** | 外码取值要么为 NULL，要么等于被参照关系中某元组的主码值 | SC 表出现不存在的学号 |
| **用户定义完整性** | 针对具体应用的语义约束（NOT NULL/UNIQUE/CHECK/触发器） | 年龄为 −5、成绩 > 100 |

::: danger 易错 · 参照完整性与外码
- 外码**不一定**是本关系主码的一部分，但常与它共同构成主码（如 SC 表的 `(Sno, Cno)`）。
- 外码可以为 NULL（表示"暂未关联"），但**若该外码同时是主码属性，则不能为 NULL**（受实体完整性约束）。
- 违反参照完整性时的处理：`RESTRICT/NO ACTION`（拒绝）、`CASCADE`（级联）、`SET NULL`（置空）。
- 实体完整性只约束**主码**，普通 UNIQUE 列在 SQL 标准里允许多个 NULL（MySQL InnoDB 亦如此）。
:::

### 2.3 关系代数（★★★）

关系代数是**过程化**的查询语言，运算对象与结果都是关系（封闭性）。传统集合运算（并、差、交、笛卡尔积）要求两关系**相容**（属性数目相同且对应域相同）。

| 运算 | 记号 | 含义 |
| --- | --- | --- |
| 并 | `R ∪ S` | 属于 R 或 S 的元组（去重） |
| 差 | `R − S` | 属于 R 但不属于 S 的元组 |
| 交 | `R ∩ S` | 同时属于两者的元组，`R∩S = R − (R − S)` |
| 笛卡尔积 | `R × S` | R 的每个元组与 S 的每个元组拼接；基数 `= |R|×|S|`，度数 `= 属性数之和` |
| **选择** | `σ_F(R)` | 按条件 F **选行**（水平方向） |
| **投影** | `π_A(R)` | 选出指定属性**列**并**去重**（垂直方向） |
| **连接** | `R ⋈_{AθB} S` | `σ_条件(R × S)`；等值连接、自然连接（自动按同名属性等值并去掉重复列） |
| **除** | `R ÷ S` | 找出"与 S 中所有值都配对"的 R 中属性值，常用来表达"全部/所有" |

![关系代数八种运算](/db/db-algebra.svg)

::: tip 工作示例 · 用关系代数写查询（教学库 S / C / SC）
```text
① 查询 CS 系学生姓名：
   π_Sname(σ_Sdept='CS'(Student))
② 查询选修了「数据库」且成绩 > 80 的学生姓名（三关系连接）：
   π_Sname(σ_Cname='数据库' ∧ Grade>80 (Student ⋈ SC ⋈ Course))
③ 查询选修了「全部课程」的学生学号（除运算的经典用法）：
   π_Sno,Cno(SC) ÷ π_Cno(Course)
④ 查询未选修任何课程的学生姓名：
   π_Sname(Student) − π_Sname(Student ⋈ SC)
```
**要点**：自然连接会**自动按同名属性**拼接并去掉重复列；若两表没有同名属性却直接写 `⋈`，结果退化为笛卡尔积，是常见错误。除运算几乎总对应 SQL 中的 `NOT EXISTS … NOT EXISTS` 双重否定或 `GROUP BY + HAVING COUNT` 写法。
:::

**关系演算**（补充）：以数理逻辑谓词为基础，是**非过程化**的。元组关系演算（如 ALPHA：`GET W (Student.Sname): Student.Sdept='CS'`）、域关系演算（如 QBE）。SQL 在表达能力上等价于关系代数 + 关系演算，且**具有关系完备性**；实际 SQL 还带聚合、分组、更新等超出的能力。

::: tip 补充 · 连接运算的三个易漏点
- **等值连接 vs 自然连接**：前者保留两列同名属性，后者去重只留一列。
- **外连接**：左外连接保留左表全部元组、右表无匹配补 NULL；另有右外连接、全外连接（MySQL 不直接支持 FULL OUTER JOIN，可用 `LEFT JOIN UNION RIGHT JOIN` 模拟）。
- **悬浮元组**：自然连接中因无匹配而被丢弃的元组；外连接正是为保留它们。
:::

---

## 第 3 章 SQL 的基本概念和 MySQL 简介

### 3.1 SQL 的特点与分类（★★★）

SQL（Structured Query Language）是关系数据库的**标准语言**，集 DDL、DML、DQL、DCL 于一体，高度非过程化（说「要什么」而非「怎么取」），面向集合操作，可独立使用也可嵌入宿主语言。

| 类别 | 全称 | 主要语句 | 作用对象 |
| --- | --- | --- | --- |
| **DDL** 数据定义 | Data Definition Language | `CREATE / ALTER / DROP / TRUNCATE` | 表、视图、索引、数据库等**结构** |
| **DML** 数据操纵 | Data Manipulation Language | `INSERT / UPDATE / DELETE` | 表中的数据 |
| **DQL** 数据查询 | Data Query Language | `SELECT`（有时归入 DML） | 数据检索 |
| **DCL** 数据控制 | Data Control Language | `GRANT / REVOKE` | 权限 |
| **TCL** 事务控制 | Transaction Control Language | `START TRANSACTION / COMMIT / ROLLBACK / SAVEPOINT` | 事务 |

![SQL 分类与 MySQL 执行流程](/db/db-sql.svg)

::: tip 补充 · 课件只讲「数据查询/定义/操纵/控制」四功能，需补两点
① 标准 SQL 还有 **TCL 事务控制**（COMMIT/ROLLBACK/SAVEPOINT），且 `TRUNCATE` 属 DDL（隐式提交、不可回滚、重置自增值）而非 DML；② DDL 在 MySQL 中大多**隐式提交**，无法被事务回滚（MySQL 8.0 的部分原子 DDL 除外），这与 `DELETE` 可回滚形成鲜明对比。
:::

### 3.2 MySQL 体系结构与一条 SQL 的执行路径（★★★）

```text
客户端 → 连接层（连接管理/认证/线程池）
      → 服务层（SQL 接口 → 解析器 → 预处理器 → 优化器 → 执行器 + 查询缓存[8.0 已移除]）
      → 存储引擎层（InnoDB / MyISAM / MEMORY，插件式）
      → 文件系统（数据文件、日志文件）
```

| 步骤 | 做什么 |
| --- | --- |
| 连接 | TCP 握手、身份认证、权限读取、分配线程；连接建立后权限不再随管理员改动即时生效（需重连或 FLUSH PRIVILEGES） |
| 解析 | 词法/语法分析生成解析树，检查表与列是否存在 |
| 预处理 | 语义检查、视图展开、权限校验 |
| **优化** | 基于代价选择索引、决定连接顺序与算法、改写子查询；`EXPLAIN` 可查看执行计划 |
| 执行 | 调用存储引擎 API 逐行取数，返回结果集 |

::: danger 易错 · SQL 标准与 MySQL 方言
- SQL 标准用 `||` 拼接字符串，MySQL 用 `CONCAT()`（除非开启 `PIPES_AS_CONCAT`）。
- MySQL 的 `LIMIT n OFFSET m`（或 `LIMIT m, n`）是方言，标准 SQL 用 `OFFSET … FETCH FIRST … ROWS ONLY`。
- 反引号 `` ` `` 是 MySQL 标识符引用符，标准 SQL 用双引号；字符串统一用单引号。
- 聚合函数与 `GROUP BY`：MySQL 在非 `ONLY_FULL_GROUP_BY` 模式下允许 SELECT 非分组列，结果**不确定**；标准 SQL 与严格模式都禁止。
:::

---

## 第 4 章 数据库的创建和管理

### 4.1 存储引擎（★★★）

**存储引擎**决定数据如何存储、如何建索引、如何更新与查询，是 MySQL 插件式体系的核心。

| 引擎 | 事务 | 锁粒度 | 外键 | 索引结构 | 适用 |
| --- | --- | --- | --- | --- | --- |
| **InnoDB（MySQL 5.5+ 默认）** | ✔ ACID | **行锁** + MVCC | ✔ | 聚簇 B+树 | OLTP、高并发写、需事务/崩溃恢复 |
| MyISAM | ✘ | 表锁 | ✘ | 非聚簇 B+树 | 只读/读多写少、全文索引（旧版）、`COUNT(*)` 快 |
| MEMORY | ✘ | 表锁 | ✘ | 哈希（默认） | 临时表、缓存；重启丢数据 |
| ARCHIVE | ✘ | 行锁 | ✘ | 压缩 | 归档日志，只支持 INSERT/SELECT |
| CSV | ✘ | 表锁 | ✘ | — | 以 CSV 文件存，便于交换 |

```sql
SHOW ENGINES;                                   -- 查看支持的引擎
SHOW VARIABLES LIKE 'default_storage_engine';  -- 查看默认引擎
CREATE TABLE t (id INT) ENGINE = InnoDB;       -- 建表时指定
ALTER TABLE t ENGINE = MyISAM;                 -- 转换引擎（会锁表并重建）
```
InnoDB 的四大特性：**事务（ACID）、行级锁、外键、崩溃恢复（redo/undo）**；这也是它与 MyISAM 最常考的区别。

![存储引擎、字符集与库管理](/db/db-storage.svg)

### 4.2 数据库管理语句（★★）

```sql
CREATE DATABASE IF NOT EXISTS teaching
  DEFAULT CHARACTER SET utf8mb4
  DEFAULT COLLATE utf8mb4_0900_ai_ci;      -- MySQL 8.0 默认
SHOW DATABASES;
SHOW CREATE DATABASE teaching;
ALTER DATABASE teaching DEFAULT CHARACTER SET utf8mb4;
USE teaching;
DROP DATABASE IF EXISTS teaching;
```

| 概念 | 说明 |
| --- | --- |
| 字符集 charset | 字符与二进制编码的映射；MySQL 的 `utf8` 实为 **utf8mb3**（最多 3 字节），**存不了 emoji 与部分生僻字**，应统一用 **utf8mb4**（4 字节真 UTF-8） |
| 校对规则 collation | 同一字符集内比较与排序的规则；`_ci` 大小写不敏感、`_cs` 敏感、`_bin` 按二进制比较 |
| 层级 | 服务器 → 数据库 → 表 → 列，未显式指定时逐层继承 |

::: danger 易错 · 字符集与建库
- `DROP DATABASE` 会删除库中**所有表与数据**且不可回滚；生产环境必须先备份。
- 「改了库的默认字符集」**不会**自动转换已有表/列的字符集，需 `ALTER TABLE … CONVERT TO CHARACTER SET utf8mb4`。
- 字符集不一致会导致 JOIN 时索引失效或报 `Illegal mix of collations`；工程上全库统一 utf8mb4。
:::

---

## 第 5 章 数据表的管理和表中数据操纵

### 5.1 常用数据类型（★★）

| 类别 | 类型 | 要点 |
| --- | --- | --- |
| 整数 | `TINYINT(1B) / SMALLINT(2B) / MEDIUMINT(3B) / INT(4B) / BIGINT(8B)` | `INT(11)` 的 11 只是**显示宽度**，不限制取值范围（配合 ZEROFILL 才生效，8.0.17 起废弃） |
| 定点/浮点 | `DECIMAL(M,D)` / `FLOAT` / `DOUBLE` | **金额必须用 DECIMAL**，FLOAT/DOUBLE 有二进制精度误差 |
| 字符串 | `CHAR(n)` / `VARCHAR(n)` / `TEXT` / `BLOB` | CHAR 定长、末尾空格处理不同；VARCHAR 变长需 1~2 字节记长度；`n` 在 MySQL 4.0+ 是**字符数**不是字节数 |
| 日期时间 | `DATE / TIME / DATETIME / TIMESTAMP / YEAR` | `TIMESTAMP` 占 4 字节且受时区影响、范围 1970–2038；`DATETIME` 占 8 字节、与时区无关 |
| 枚举集合 | `ENUM / SET` | ENUM 单选、内部按序号存；改枚举项代价大，慎用 |
| 其他 | `JSON`（5.7+）、`BOOLEAN`（=TINYINT(1)）、`BIT` | JSON 列可用Generated Column + 索引优化 |

![数据类型与六类完整性约束](/db/db-datatype.svg)

### 5.2 六类列约束与建表（★★★）

| 约束 | 写法 | 作用 |
| --- | --- | --- |
| `PRIMARY KEY` | 列级或表级 | 实体完整性；自动 NOT NULL + UNIQUE；**每表最多一个**（可组合多列） |
| `FOREIGN KEY … REFERENCES` | 表级 | 参照完整性；要求被参照列有唯一索引，两表通常同为 InnoDB |
| `UNIQUE` | 列级/表级 | 唯一性；**允许多个 NULL**（MySQL） |
| `NOT NULL` | 列级 | 禁止 NULL |
| `DEFAULT` | 列级 | 未给值时填默认值 |
| `CHECK` | 列级/表级 | 域约束（MySQL 8.0.16 起才真正生效，之前仅解析忽略） |
| `AUTO_INCREMENT` | 列级 | 自增，必须被索引，通常作代理主键 |

```sql
CREATE TABLE Student (
  Sno   CHAR(7)      PRIMARY KEY,
  Sname VARCHAR(20)  NOT NULL,
  Ssex  ENUM('男','女') DEFAULT '男',
  Sage  SMALLINT     CHECK (Sage BETWEEN 10 AND 60),
  Sdept VARCHAR(20)  DEFAULT 'CS'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE Course (
  Cno     CHAR(2) PRIMARY KEY,
  Cname   VARCHAR(40) NOT NULL UNIQUE,
  Ccredit SMALLINT NOT NULL DEFAULT 2
);

CREATE TABLE SC (
  Sno   CHAR(7) NOT NULL,
  Cno   CHAR(2) NOT NULL,
  Grade SMALLINT CHECK (Grade BETWEEN 0 AND 100),
  PRIMARY KEY (Sno, Cno),                       -- 组合主码
  CONSTRAINT fk_sc_s FOREIGN KEY (Sno) REFERENCES Student(Sno)
      ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT fk_sc_c FOREIGN KEY (Cno) REFERENCES Course(Cno)
      ON DELETE RESTRICT
);
```

**表结构维护**：
```sql
DESC Student;                                        -- 或 SHOW COLUMNS FROM Student;
ALTER TABLE Student ADD COLUMN Semail VARCHAR(50);
ALTER TABLE Student MODIFY COLUMN Sname VARCHAR(30) NOT NULL;
ALTER TABLE Student CHANGE COLUMN Semail Email VARCHAR(60);
ALTER TABLE Student DROP COLUMN Email;
ALTER TABLE Student RENAME TO Stu;
DROP TABLE IF EXISTS SC;                             -- 先删子表再删父表
```

### 5.3 数据操纵 DML（★★★）

```sql
INSERT INTO Student(Sno,Sname,Ssex,Sage,Sdept) VALUES
  ('2021001','李勇','男',20,'CS'),
  ('2021002','刘晨','女',19,'CS');
INSERT INTO Student VALUES ('2021003','王敏','女',18,'MA');  -- 省略列名须按表结构全列顺序给值
INSERT INTO Stu_CS(Sno,Sname) SELECT Sno,Sname FROM Student WHERE Sdept='CS';  -- 插入查询结果

UPDATE Student SET Sage = Sage + 1 WHERE Sdept = 'CS';       -- 务必带 WHERE！
UPDATE SC SET Grade = Grade * 1.05 WHERE Cno = '1' AND Grade < 60;

DELETE FROM SC WHERE Grade IS NULL;                          -- 判空只能用 IS NULL
DELETE FROM Student WHERE Sno = '2021004';
TRUNCATE TABLE tmp_log;                                     -- DDL：清全表、不可回滚、重置自增值
```

::: danger 易错 · DELETE / TRUNCATE / DROP
| | DELETE | TRUNCATE | DROP |
| --- | --- | --- | --- |
| 类型 | DML | **DDL** | DDL |
| 可带 WHERE | ✔ | ✘ | ✘ |
| 可回滚（事务内） | ✔ | **✘（隐式提交）** | ✘ |
| 释放空间/重置自增 | 不一定 | ✔ | ✔（连表结构一起删） |
| 触发 DELETE 触发器 | ✔ | ✘ | ✘ |

另外：`UPDATE/DELETE` 忘记写 `WHERE` 会作用于**全表**（生产事故高发）；MySQL 可用 `sql_safe_updates=1` 强制要求 WHERE 中含键列。
:::

---

## 第 6 章 数据表中的数据查询

> 本章例题统一使用教学数据库（结果与 SQLite/MySQL 一致，已实际执行验证）：
> `Student(Sno,Sname,Ssex,Sage,Sdept)`、`Course(Cno,Cname,Ccredit)`、`SC(Sno,Cno,Grade)`；
> 4 名学生（李勇 CS/20、刘晨 CS/19、王敏 MA/18、张立 IS/19），4 门课，7 条选课记录（含 1 条 Grade 为 NULL）。

### 6.1 SELECT 语法与真正的执行顺序（★★★）

```sql
SELECT [ALL|DISTINCT] <目标列表达式> [AS 别名], ...
FROM <表名/视图> [JOIN … ON …]
[WHERE <行条件>]
[GROUP BY <分组列> [HAVING <组条件>]]
[ORDER BY <排序列> [ASC|DESC]]
[LIMIT <行数> [OFFSET <偏移>]];
```

**书写顺序 ≠ 执行顺序**，真实逻辑顺序（高频考点）：

```text
① FROM / JOIN      生成中间关系（笛卡尔积 + ON 过滤）
② WHERE            对每一行做行级过滤（此时不能用聚合函数与 SELECT 别名）
③ GROUP BY         分组
④ HAVING           对每一组过滤（可用聚合函数；一般不能用 SELECT 别名，MySQL 扩展允许）
⑤ SELECT           计算目标列表达式、DISTINCT 去重
⑥ ORDER BY         排序（可用别名）
⑦ LIMIT/OFFSET     取前若干行
```

![SELECT 子句与执行顺序](/db/db-select.svg)

::: tip 工作示例 · 单表与分组查询（含实际结果）
```sql
-- ① 条件查询：CS 系且年龄小于 20 的学生
SELECT Sname, Sage FROM Student WHERE Sdept='CS' AND Sage<20;
-- 结果：刘晨 | 19

-- ② 分组 + HAVING：人数不少于 2 的系及其平均年龄
SELECT Sdept, COUNT(*) AS n, AVG(Sage) AS avg_age
FROM Student GROUP BY Sdept HAVING COUNT(*) >= 2;
-- 结果：CS | 2 | 19.5

-- ③ 聚合函数忽略 NULL
SELECT COUNT(*) AS all_rows, COUNT(Grade) AS graded FROM SC;
-- 结果：7 | 6   （COUNT(*) 计全部行，COUNT(列) 跳过 NULL）

-- ④ DISTINCT + 排序 + 分页
SELECT DISTINCT Sdept FROM Student ORDER BY Sdept ASC LIMIT 2;
-- 结果：CS / IS
```
**常见陷阱**：`WHERE Grade <> NULL` 永远为空（NULL 比较结果是 UNKNOWN），必须写 `Grade IS NOT NULL`；`AVG` 同样忽略 NULL，若想把 NULL 当 0 应写 `AVG(COALESCE(Grade,0))`。
:::

| 常用谓词 / 函数 | 说明 |
| --- | --- |
| `BETWEEN a AND b` / `IN (…)` / `LIKE '模式'` | 范围 / 集合 / 模糊匹配（`%` 任意串、`_` 单字符，`ESCAPE` 转义） |
| `IS NULL` / `IS NOT NULL` | 判空 |
| `COUNT / SUM / AVG / MAX / MIN` | 聚合函数，除 `COUNT(*)` 外都**忽略 NULL**；`SUM` 遇全 NULL 返回 NULL |
| `AND / OR / NOT` | 三值逻辑：TRUE / FALSE / **UNKNOWN**，`NOT IN` 遇子查询含 NULL 会返回空结果 |
| `CASE WHEN … THEN … ELSE … END` | 条件表达式（可实现行列转换、分组打标） |
| `COALESCE / IFNULL` | 用默认值替换 NULL |

### 6.2 多表连接（★★★）

| 连接 | 结果 | 记忆 |
| --- | --- | --- |
| `INNER JOIN … ON` | 两表都匹配的行 | 交集 |
| `LEFT [OUTER] JOIN` | 左表全部 + 右表匹配（无匹配补 NULL） | 左表不丢 |
| `RIGHT [OUTER] JOIN` | 右表全部 + 左表匹配 | 右表不丢 |
| `CROSS JOIN` | 笛卡尔积 | 忘写 ON 的后果 |
| 自连接 | 表与自身连接，须起别名 | 查「同系」「上下级」 |
| `UNION / UNION ALL` | 纵向合并结果集（列数、类型相容） | UNION 去重且排序，UNION ALL 不去重更快 |

![连接类型、子查询与集合运算](/db/db-join.svg)

::: tip 工作示例 · 三表连接与 LEFT JOIN 的 NULL 陷阱（含实际结果）
```sql
-- ① 选修「数据库」且成绩 > 80 的学生姓名（三表内连接）
SELECT s.Sname, sc.Grade
FROM Student s
JOIN SC sc     ON s.Sno = sc.Sno
JOIN Course co ON sc.Cno = co.Cno
WHERE co.Cname = '数据库' AND sc.Grade > 80;
-- 结果：李勇 | 92

-- ② 统计每名学生的选课门数（含一门未选的学生）
SELECT s.Sname, COUNT(sc.Cno) AS cnt
FROM Student s LEFT JOIN SC sc ON s.Sno = sc.Sno
GROUP BY s.Sno, s.Sname ORDER BY cnt DESC, s.Sname;
-- 结果：李勇 3 / 刘晨 2 / 张立 1 / 王敏 1
```
**关键**：左外连接后必须用 `COUNT(右表列)` 而不是 `COUNT(*)`——否则没选课的学生也会被计为 1（因为补的 NULL 行仍是一行）。王敏虽有一门成绩为 NULL，但**选课记录存在**，故计数为 1；若误写 `COUNT(sc.Grade)` 会得到 0。
:::

### 6.3 子查询与集合运算（★★★）

| 类型 | 写法 | 说明 |
| --- | --- | --- |
| 标量子查询 | `WHERE Sage > (SELECT AVG(Sage) FROM Student)` | 返回单值 |
| `IN` 子查询 | `WHERE Sno IN (SELECT Sno FROM SC …)` | 返回一列多行；含 NULL 时小心 |
| 比较 + `ANY/ALL` | `> ANY(…)`（大于最小）/ `> ALL(…)`（大于最大） | 与聚合 MAX/MIN 等价 |
| `EXISTS` 相关子查询 | `WHERE EXISTS (SELECT 1 FROM SC WHERE …)` | 逐行求值、找到即停，通常效率高 |
| `NOT EXISTS` 双重否定 | 表达「全部 / 所有」 | 对应关系代数除运算 |
| 派生表 / CTE | `FROM (SELECT …) AS t` / `WITH cte AS (…)` | MySQL 8.0 支持 CTE 与窗口函数 |

::: tip 工作示例 · 子查询与「全部」表达（含实际结果）
```sql
-- ① 有成绩高于全体平均成绩的学生姓名
SELECT Sname FROM Student
WHERE Sno IN (SELECT Sno FROM SC WHERE Grade > (SELECT AVG(Grade) FROM SC));
-- 结果：李勇 / 刘晨

-- ② 无人选修的课程（NOT EXISTS）
SELECT Cname FROM Course co
WHERE NOT EXISTS (SELECT 1 FROM SC sc WHERE sc.Cno = co.Cno);
-- 结果：操作系统

-- ③ 等价于「选修了全部课程的学生」的两种写法
-- 写法 A：双重否定
SELECT Sname FROM Student s
WHERE NOT EXISTS (
  SELECT 1 FROM Course c
  WHERE NOT EXISTS (SELECT 1 FROM SC sc WHERE sc.Sno=s.Sno AND sc.Cno=c.Cno));
-- 写法 B：分组计数
SELECT Sno FROM SC GROUP BY Sno
HAVING COUNT(DISTINCT Cno) = (SELECT COUNT(*) FROM Course);
```
**易错**：`NOT IN` 的子查询只要含一个 NULL，整个结果恒为空（`x NOT IN (1,2,NULL)` → UNKNOWN）；应改用 `NOT EXISTS` 或给子查询加 `WHERE col IS NOT NULL`。
:::

::: tip 补充 · 查询优化与执行计划（课件未展开）
`EXPLAIN SELECT …` 的关键列：`type`（`system > const > eq_ref > ref > range > index > ALL`，出现 **ALL 即全表扫描**）、`possible_keys / key`（候选与实际使用索引）、`rows`（预估扫描行数）、`Extra`（`Using index` 覆盖索引、`Using filesort` 需额外排序、`Using temporary` 用临时表）。
索引失效的典型原因：对索引列做函数/运算（`WHERE YEAR(date)=2024`）、隐式类型转换（字符串列传数字）、`LIKE '%abc'` 前置通配、违反最左前缀、`OR` 连接非索引列、优化器判断全表扫描更便宜。**改写目标：让条件能直接命中索引列本身。**
:::

::: danger 易错 · 查询章
- `WHERE` 不能用聚合函数与 `SELECT` 定义的别名；`HAVING` 才用于组过滤。
- `GROUP BY` 后 SELECT 只能出现分组列或聚合表达式（严格模式 `ONLY_FULL_GROUP_BY`）。
- `ORDER BY` 默认 ASC，`NULL` 在 MySQL 升序中排**最前**（Oracle 中排最后）。
- `LIMIT` 必须配合 `ORDER BY` 才有确定的「前 N 名」语义。
- `UNION` 会去重（有排序开销），业务确认无重复时优先 `UNION ALL`。
:::

---

## 第 7 章 视图和索引

### 7.1 视图（★★★）

**视图**是由一个或多个基本表（或其它视图）通过 `SELECT` 定义的**虚拟表**：数据库中只保存视图的**定义**（数据字典中），不保存其数据；查询视图时动态执行底层 SELECT（称为「视图消解」）。

```sql
CREATE [OR REPLACE] VIEW v_CS_Student AS
  SELECT Sno, Sname, Sage FROM Student WHERE Sdept = 'CS'
  WITH [CASCADED|LOCAL] CHECK OPTION;      -- 限定通过视图的更新必须仍满足视图条件
SELECT * FROM v_CS_Student WHERE Sage >= 19;
SHOW CREATE VIEW v_CS_Student;
ALTER VIEW v_CS_Student AS SELECT Sno, Sname FROM Student WHERE Sdept='CS';
DROP VIEW IF EXISTS v_CS_Student;
```

| 优点 | 说明 |
| --- | --- |
| 简化查询 | 把复杂的多表连接/子查询封装成一张「表」 |
| **逻辑独立性** | 基本表结构变化时可改视图定义而**不改应用程序**（外模式的实现） |
| 安全 | 只暴露允许的行与列，隐藏敏感字段 |
| 定制视角 | 不同用户看到不同的数据子集 |

**可更新视图的限制**（MySQL）：含 `DISTINCT / GROUP BY / HAVING / UNION / 子查询 / 聚合函数 / 多表连接（多数情形）/ 常量列` 的视图通常**不可更新**；`WITH CHECK OPTION` 会拒绝使行"从视图中消失"的修改。

![视图与可更新性](/db/db-view.svg)

### 7.2 索引（★★★）

索引是**独立于数据的、有序的数据结构**，用于加速检索；本质是「以空间换时间 + 以写入代价换读取速度」。

| 分类维度 | 类型 | 特点 |
| --- | --- | --- |
| 数据结构 | **B+树**（InnoDB 默认）、HASH（MEMORY / 自适应哈希）、全文 FULLTEXT、空间 R-Tree | B+树支持范围查询与排序，HASH 只适等值 |
| 物理存储 | **聚簇索引（主键索引）** / 二级（辅助）索引 | 聚簇索引叶子节点存**整行数据**，一张表只有一个；二级索引叶子存**主键值**，查完整行需**回表** |
| 逻辑约束 | 普通 / 唯一 UNIQUE / 主键 PRIMARY / 全文 | UNIQUE 自动建唯一索引 |
| 列数 | 单列 / **联合（复合）索引** | 联合索引遵守**最左前缀原则** |

```sql
CREATE INDEX idx_sdept ON Student(Sdept);
CREATE UNIQUE INDEX uk_cname ON Course(Cname);
CREATE INDEX idx_sc ON SC(Sno, Grade);          -- 联合索引
ALTER TABLE Student DROP INDEX idx_sdept;
SHOW INDEX FROM Student;
EXPLAIN SELECT * FROM Student WHERE Sdept='CS';
```

![B+树索引、最左前缀与覆盖索引](/db/db-index.svg)

::: tip 补充 · B+树、最左前缀与覆盖索引（课件只讲「索引管理」语句，未讲原理）
**B+树**：非叶子节点只存键值与指针（扇出大、树高通常 3~4 层），**所有数据都在叶子层且叶子间有双向链表**，因此范围查询 `BETWEEN / > / ORDER BY` 只需顺序扫叶子。对比 B 树：B 树各层都可能存数据，范围查询要中序遍历。

**最左前缀**：联合索引 `(Sdept, Sage, Sno)` 相当于按 `Sdept` 排序，同值内按 `Sage`、`Sno` 排序。
```text
✔ WHERE Sdept='CS'
✔ WHERE Sdept='CS' AND Sage=19
✔ WHERE Sdept='CS' AND Sage>18          （Sage 用范围后，其后的 Sno 不再用于定位）
✘ WHERE Sage=19                          （跳过了最左列）
✘ WHERE Sdept LIKE '%S'                  （前置通配）
```
**覆盖索引**：若 `SELECT` 的列全都包含在某个索引中，引擎直接返回索引数据、**无需回表**（`EXPLAIN` 显示 `Using index`）。这也是「不要盲目 `SELECT *`」的定量理由。

**索引不是越多越好**：每个索引都要占用磁盘、在 `INSERT/UPDATE/DELETE` 时维护 B+树、并参与优化器代价估算；高频写入表应克制建索引，优先给「高选择性 + 高频 WHERE/ORDER BY/JOIN 列」建。
:::

::: danger 易错 · 索引
- 主键自动建聚簇索引；没有显式主键时 InnoDB 选第一个非空唯一索引，再没有就生成隐藏 `rowid`。
- 二级索引存的是**主键值**而非行指针，所以主键宜短且单调（长主键会让所有二级索引变大）。
- `WHERE` 中对索引列使用函数、隐式类型转换、`!= / NOT IN`（多数情况）、前置 `%` 都会导致索引失效。
- `NULL` 值也可以被索引；但低选择性列（如性别）建单列索引通常无用（优化器宁可全表扫描）。
- 视图是**虚表**，索引是**实结构**；不能对普通视图建索引（物化视图除外，MySQL 不原生支持）。
:::

---

## 第 8 章 数据库安全性管理

### 8.1 用户、权限与角色（★★★）

数据库安全性指防止**非法使用**造成的数据泄露、更改或破坏。MySQL 的身份由 `'user'@'host'` 二元组唯一确定（`'root'@'localhost'` 与 `'root'@'%'` 是不同账号）。

```sql
-- 用户管理
CREATE USER 'app'@'%' IDENTIFIED BY 'Str0ng!Pass';
ALTER USER 'app'@'%' IDENTIFIED BY 'New!Pass';
RENAME USER 'app'@'%' TO 'app_ro'@'%';
DROP USER IF EXISTS 'app'@'%';
SELECT USER(), CURRENT_USER();        -- 连接身份 vs 生效权限身份

-- 授权与回收
GRANT SELECT, INSERT ON teaching.Student TO 'app'@'%';
GRANT ALL PRIVILEGES ON teaching.* TO 'admin'@'localhost' WITH GRANT OPTION;
REVOKE INSERT ON teaching.Student FROM 'app'@'%';
SHOW GRANTS FOR 'app'@'%';

-- 角色（MySQL 8.0+）
CREATE ROLE 'r_reader', 'r_writer';
GRANT SELECT ON teaching.* TO 'r_reader';
GRANT 'r_reader' TO 'app'@'%';
SET DEFAULT ROLE 'r_reader' TO 'app'@'%';
```

| 权限层级 | 作用范围 | 存储表（mysql 系统库） |
| --- | --- | --- |
| 全局 | 所有数据库 | `mysql.user` |
| 数据库 | 指定库所有对象 | `mysql.db` |
| 表 / 列 | 指定表或列 | `mysql.tables_priv` / `columns_priv` |
| 例程 | 存储过程与函数 | `mysql.procs_priv` |

![用户、权限、角色与注入防御](/db/db-security.svg)

### 8.2 SQL 注入与安全实践（★★★）

```python
# 危险：字符串拼接
sql = f"SELECT * FROM users WHERE name='{name}' AND pwd='{pwd}'"
# 若 name 输入  ' OR '1'='1' --  则条件恒成立，绕过认证

# 正确：参数化查询（预处理语句）
cur.execute("SELECT * FROM users WHERE name=%s AND pwd=%s", (name, pwd))
```
**原理**：参数化把 SQL **结构与数据**分离，参数永远被当作字面值而非可解析的 SQL 片段，因此注入串无法改变语法树。注意表名/列名不能参数化，若要动态须用**白名单映射**。

| 安全原则 | 落地做法 |
| --- | --- |
| 最小权限 | 应用账号只授所需库表的 `SELECT/INSERT/UPDATE`，不给 `DROP/FILE/SUPER`、不给 `WITH GRANT OPTION` |
| 账号隔离 | 不同应用不同账号；禁止应用直连 `root`，禁止 `'%'` 通配主机 |
| 传输与存储加密 | TLS 连接；密码加盐哈希（应用层）；敏感列加密/脱敏；备份文件加密 |
| 审计 | 开启审计/通用日志、慢查询日志、定期审阅 `mysql.user` |
| 运维 | 及时打补丁、限制网络暴露（只内网/安全组）、定期备份并**演练恢复** |

::: danger 易错 · 权限与注入
- `GRANT` 创建用户是旧语法，MySQL 8.0 起必须先 `CREATE USER` 再 `GRANT`。
- `REVOKE` 不会删除用户，只回收权限；删除用户须 `DROP USER`。
- 授权后不必 `FLUSH PRIVILEGES`（`GRANT/CREATE USER` 会自动生效）；只有直接改 `mysql.user` 表才需要。
- 「前端做校验」不能替代参数化查询；转义函数（`mysql_real_escape_string`）也容易因字符集设置不当被绕过。
:::

---

## 第 9 章 数据库并发控制与封锁

### 9.1 事务与 ACID（★★★）

**事务**是用户定义的一个数据库操作序列，这些操作要么全做、要么全不做，是不可分割的逻辑工作单位。

```sql
START TRANSACTION;   -- 或 BEGIN
  UPDATE account SET balance = balance - 100 WHERE id = 1;
  UPDATE account SET balance = balance + 100 WHERE id = 2;
  SAVEPOINT sp1;
  -- 校验 …
  -- ROLLBACK TO SAVEPOINT sp1;   -- 部分回滚
COMMIT;              -- 或 ROLLBACK（全部回滚）
```

| 特性 | 含义 | InnoDB 实现 |
| --- | --- | --- |
| **A 原子性** | 事务内操作全做或全不做 | **undo log**（记录反向操作，回滚时重放） |
| **C 一致性** | 事务使库从一个一致状态到另一个一致状态 | 由 A/I/D 共同保障 + 业务约束与完整性约束 |
| **I 隔离性** | 并发事务之间互不干扰 | **锁 + MVCC + 隔离级别** |
| **D 持久性** | 提交后修改永久保存，即使崩溃 | **redo log + WAL + 两阶段提交** |

![事务状态、ACID 与实现机制](/db/db-transaction.svg)

::: tip 补充 · 课件只讲「事务及其性质」，需补上 ACID 缩写与实现映射
课件用中文描述四个性质但未给出 **ACID** 术语，也未说明它们分别由哪套日志/机制保障。上表是考研与面试的标准答案：**A↔undo、D↔redo、I↔锁/MVCC、C↔最终结果**。另外 MySQL 默认 `autocommit=1`，单条 DML 自动成为一个事务；显式事务需 `START TRANSACTION` 或 `SET autocommit=0`。
:::

### 9.2 四类并发异常与四种隔离级别（★★★）

并发若不加以控制，会产生四类经典不一致：

| 异常 | 现象 | 例子 |
| --- | --- | --- |
| **丢失修改** | 两个事务同时读同一行并写回，后提交覆盖了先提交的更新 | T1、T2 同时把余额 100 各减 10，结果 90 而非 80 |
| **脏读** | 读到另一个事务**尚未提交**的修改，对方回滚后该数据根本不存在 | T1 改 A=200 未提交，T2 读 200，T1 回滚 |
| **不可重复读** | 同一事务内两次读同一行，值不同（另一事务 **UPDATE 并提交**） | 第一次读 100，第二次读 90 |
| **幻读** | 同一事务内按同一条件两次查询，**行数**不同（另一事务 **INSERT/DELETE 并提交**） | 第一次 3 行，第二次 4 行 |

| 隔离级别 | 脏读 | 不可重复读 | 幻读 | 说明 |
| --- | --- | --- | --- | --- |
| `READ UNCOMMITTED` 读未提交 | 可能 | 可能 | 可能 | 最低，几乎不加锁读 |
| `READ COMMITTED` 读已提交 | **不可能** | 可能 | 可能 | Oracle/PostgreSQL 默认；MVCC 每次读生成新 ReadView |
| `REPEATABLE READ` 可重复读 | 不可能 | **不可能** | 可能* | **MySQL InnoDB 默认**；配合 Next-Key Lock 已基本避免幻读 |
| `SERIALIZABLE` 可串行化 | 不可能 | 不可能 | **不可能** | 读也加锁，并发度最低 |

`*` 标准 SQL 允许 RR 出现幻读；InnoDB 用 **MVCC（快照读）+ Next-Key Lock（当前读）** 在 RR 下也基本消除了幻读，这是 MySQL 相对标准的重要增强。

```sql
SELECT @@transaction_isolation;                          -- MySQL 8.0（旧版为 @@tx_isolation）
SET SESSION TRANSACTION ISOLATION LEVEL READ COMMITTED;
SET GLOBAL  TRANSACTION ISOLATION LEVEL REPEATABLE READ;
```

![并发异常、隔离级别与封锁协议](/db/db-concurrency.svg)

::: danger 易错 · 不可重复读 vs 幻读
- **不可重复读**针对同一行的 **UPDATE**（值变了）；**幻读**针对满足条件的**行数变化**（INSERT/DELETE）。
- 解决不可重复读只需对读到的行加 S 锁并保持到事务结束；解决幻读还必须锁住**范围（间隙）**，即 Next-Key Lock（记录锁 + 间隙锁）。
- 「丢失修改」是最低级别也不能容忍的，一级封锁协议即可防止；它不在 SQL 标准四级别表里单列，但常出现在教材并发异常清单中。
:::

### 9.3 封锁、封锁协议与两段锁（★★★）

| 锁 | 别名 | 相容性 |
| --- | --- | --- |
| **排他锁 X**（写锁） | Exclusive | 与其它任何锁都不相容；加 X 锁后他人既不能读也不能写 |
| **共享锁 S**（读锁） | Shared | 多个 S 可共存，但与 X 互斥 |
| 意向锁 IS/IX | 表级 | 表明"表里某行将被加 S/X"，避免逐行检查表锁冲突 |
| 间隙锁 / Next-Key Lock | 范围 | InnoDB RR 下防止幻读 |

**三级封锁协议**：

| 协议 | 规则 | 防止 |
| --- | --- | --- |
| 一级 | 事务 T 修改数据 R 前加 **X 锁，直到事务结束**才释放 | **丢失修改** |
| 二级 | 一级 + 读 R 前加 **S 锁，读完即释放** | 丢失修改 + **脏读** |
| 三级 | 一级 + 读 R 前加 **S 锁，直到事务结束**才释放 | 再加 **不可重复读** |

**两段锁协议 2PL**：事务分两个阶段——**扩展阶段**只获得锁不释放，**收缩阶段**只释放锁不获得。遵守 2PL 的并发调度**一定是可串行化的**（充分条件，非必要）；但 2PL **不能避免死锁**。

**可串行化调度**：多个事务并发执行的结果，与某一串行执行次序的结果相同。判据可用**优先图（冲突图）**：若图中无环，则调度冲突可串行化。

**死锁**：两个事务互相等待对方已持有的锁。
- 预防：一次封锁法（一次性申请全部资源，降低并发）、顺序封锁法（按统一顺序加锁，难维护）；
- 诊断与解除：**超时法**、**等待图法（检测环）**；选择**代价最小**的事务回滚并释放其锁；
- InnoDB 内建死锁检测（`innodb_deadlock_detect`），并会自动回滚较小的事务；也支持 `innodb_lock_wait_timeout` 超时。

::: tip 补充 · MVCC 如何做到「读不加锁」（课件未覆盖）
InnoDB 每行有隐藏列 `DB_TRX_ID`（最后修改事务 ID）、`DB_ROLL_PTR`（指向 undo log 中旧版本）；多版本通过回滚指针串成**版本链**。事务发起一致性读时生成 **ReadView**（含当前活跃事务 ID 列表、最小/最大事务 ID），沿版本链找到「对当前 ReadView 可见」的版本返回。
- `READ COMMITTED`：**每条 SELECT 都生成新 ReadView** → 能看到别的事务新提交的修改（不可重复读）。
- `REPEATABLE READ`：**只在第一次普通 SELECT 生成 ReadView**，之后复用 → 可重复读。
- 快照读（普通 SELECT）走 MVCC 不加锁；当前读（`SELECT … FOR UPDATE` / `LOCK IN SHARE MODE` / `UPDATE` / `DELETE`）走锁与 Next-Key Lock。
:::

---

## 第 10 章 数据库备份还原和日志管理

### 10.1 备份分类与常用命令（★★★）

| 维度 | 分类 | 说明 |
| --- | --- | --- |
| 备份内容 | **逻辑备份**（mysqldump / mysqlpump / mydumper，导出 SQL 语句）／**物理备份**（直接拷贝数据文件，XtraBackup） | 逻辑备份跨版本好、慢；物理备份快、适合大库 |
| 数据范围 | **完全备份**（全量）／**增量备份**（自上次备份以来的变化）／**差异备份**（自上次全量以来的变化） | 增量恢复要按序回放所有增量，差异只需全量+最后一次差异 |
| 运行状态 | 冷备（停机）／温备（只读）／**热备**（在线不中断，InnoDB + XtraBackup） | 生产一般热备 |
| 一致性 | 一致性备份（含 `--single-transaction`）／非一致性 | `mysqldump --single-transaction` 借 MVCC 取得一致快照且**不锁表** |

```bash
# 逻辑备份（单库 / 全库 / 仅结构 / 带 binlog 位点）
mysqldump -u root -p --single-transaction --routines --triggers \
          --master-data=2 teaching > teaching_$(date +%F).sql
mysqldump -u root -p --all-databases > full.sql
mysqldump -u root -p --no-data teaching > schema.sql

# 还原
mysql -u root -p teaching < teaching_2026-11-13.sql
# 或在 mysql 客户端内：SOURCE /path/teaching.sql;

# 时间点恢复（PITR）：先还原全量，再重放 binlog 到误操作之前
mysqlbinlog --stop-datetime="2026-11-13 14:29:59" mysql-bin.000003 | mysql -u root -p
```

![备份策略、恢复与三类日志](/db/db-backup.svg)

### 10.2 MySQL 日志体系（★★★）

| 日志 | 所属层 | 内容 | 主要用途 |
| --- | --- | --- | --- |
| **binlog 二进制日志** | Server 层 | **逻辑**日志，记录所有 DDL/DML 变更（statement / row / mixed 格式） | **主从复制**、**时间点恢复**、审计 |
| **redo log 重做日志** | InnoDB 层 | **物理**日志，记录"某页某偏移改成什么" | **崩溃恢复**（持久性）、WAL 顺序写提升性能 |
| **undo log 回滚日志** | InnoDB 层 | 记录数据被修改前的旧值 | **事务回滚**（原子性）+ **MVCC 版本链** |
| error log | Server | 启动/运行/停止的错误与警告 | 故障诊断 |
| slow query log | Server | 超过 `long_query_time` 的 SQL | 慢查询优化 |
| general log | Server | 全部客户端语句 | 审计（开销大，慎开） |
| relay log | 从库 | 从主库接收的 binlog 副本 | 主从复制 |

```text
一条 UPDATE 的日志协作（两阶段提交 2PC）：
① 记录 undo（保存旧值）       ② 修改内存中的 Buffer Pool 页
③ 写 redo log（prepare 状态） ④ 写 binlog
⑤ redo log 改写成 commit
```
**为什么要两阶段提交**：binlog 与 redo 分属两层，若「redo 已提交但 binlog 没写」→ 主库有数据、从库没有；反之从库多数据。2PC 以 binlog 是否完整写入作为最终提交依据，保证**主库与从库一致**。崩溃恢复时：redo 为 prepare 且 binlog 完整 → 提交；redo 为 prepare 但 binlog 不完整 → 回滚。

::: danger 易错 · 日志与恢复
- `TRUNCATE` 是 DDL、隐式提交，**不能靠 undo 回滚**；误删表只能靠备份 + binlog 恢复。
- binlog 是 **Server 层**逻辑日志，redo 是 **InnoDB 层**物理日志；MyISAM 没有 redo。
- 「有备份」≠「能恢复」：RPO（最多丢多少数据）由备份频率 + binlog 决定，RTO（多久恢复）由备份大小与回放速度决定；必须**定期演练恢复**。
- `mysqldump` 默认不加 `--single-transaction` 时会锁表；MyISAM 表无法用该参数保证一致性。
- 主从复制是**高可用/读扩展**手段，**不是备份**：主库误删会同步到从库，仍须独立备份与延迟从库。
:::

---

## 第 11 章 数据库设计概述及需求分析

### 11.1 数据库设计的六个阶段（★★★）

| 阶段 | 输入 | 主要工作 | 产出 |
| --- | --- | --- | --- |
| ① 需求分析 | 用户业务现状 | 调查组织机构、业务流程、数据流向与处理需求，明确数据/功能/性能/安全约束 | **需求说明书**、数据流图 DFD、数据字典 |
| ② 概念结构设计 | 需求说明书 | 抽象出实体、属性、联系，形成独立于具体 DBMS 的概念模型 | **E-R 图**（第 13 章） |
| ③ 逻辑结构设计 | E-R 图 + 选定数据模型 | 把概念模型转换为关系模式，并做**规范化**与用户外模式设计 | 关系模式集、视图定义（第 12、13 章） |
| ④ 物理结构设计 | 逻辑模式 + DBMS/硬件 | 选存储引擎、建索引、聚簇、分区、确定存储参数与存储路径 | 物理设计方案（第 14 章） |
| ⑤ 数据库实施 | 物理设计 | 建库建表、装载数据、编写与调试应用程序、试运行 | 可运行的数据库与应用 |
| ⑥ 运行与维护 | 上线系统 | 性能监控与调优、备份恢复、安全审计、结构变更、重组织与重构 | 持续运维记录 |

::: tip 补充 · 课件按章节分散讲设计，需补「六阶段」这条主线
课件第 11 章讲设计任务与需求分析、第 13 章讲概念/逻辑设计、第 14 章讲物理设计与实施维护，但**没有把六阶段串成一条完整链路**（术语「六阶段」在课件文本中未出现）。答题时应能一口气写出上表，并说明各阶段的**输入与产出**；其中「概念结构设计独立于具体 DBMS」与「逻辑结构设计依赖所选数据模型」是两个高频判断点。
:::

### 11.2 需求分析：DFD 与数据字典（★★）

**数据流图 DFD** 四要素：外部实体（矩形）、处理过程（圆/矩形框）、数据流（箭头）、数据存储（双线/开口矩形）。自顶向下逐层分解，刻画「数据从哪来、经什么处理、存到哪里」。

**数据字典**是系统中全部数据的描述集合，通常包含：
```text
数据项（名称、类型、长度、取值范围、含义、与其它项的逻辑关系）
数据结构（若干数据项/结构的组合）
数据流（来源、去向、组成、流量）
数据存储（结构、存取频度、存取方式）
处理过程（输入、输出、处理逻辑简述）
```
**数据字典在需求分析阶段建立，并在后续设计阶段不断充实**；它是「元数据」（描述数据的数据），存放在系统目录/数据字典中，不是用户数据本身。

![数据库设计六阶段与需求产物](/db/db-design.svg)

---

## 第 12 章 关系模式的规范化理论

### 12.1 为什么要规范化：四类异常（★★★）

设有不合理的关系模式：
```text
SLC(Sno, Sdept, Sloc, Cno, Grade)
-- 学号、系名、系所在楼、课程号、成绩；一个学生可选多门课
```
函数依赖集：
```text
(Sno, Cno) →f Grade       （完全依赖）
Sno → Sdept               （部分依赖：Sdept 只依赖主码的一部分）
Sno → Sloc
Sdept → Sloc              （传递依赖）
候选码 = (Sno, Cno)
```
它引发四类异常：

| 异常 | 例子 |
| --- | --- |
| **数据冗余** | 某学生选 10 门课，其 Sdept、Sloc 重复 10 次；某系 500 学生，Sloc 重复 500 次 |
| **插入异常** | 新生尚未选课 → `Cno` 为空（主码不能为空），无法录入学生与系信息 |
| **删除异常** | 某学生退掉最后一门课，删除该元组时把「该系在几楼」也一起丢了 |
| **更新异常** | 系搬楼要修改该系所有学生的所有选课行，漏改即不一致 |

### 12.2 函数依赖与 Armstrong 公理（★★★）

| 概念 | 定义 |
| --- | --- |
| 函数依赖 `X → Y` | 对 R 的任意合法关系，任意两元组若在 X 上取值相同，则在 Y 上必相同 |
| 平凡函数依赖 | `Y ⊆ X`（如 `(Sno,Cno) → Sno`），恒成立 |
| **完全函数依赖** `X →f Y` | Y 依赖整个 X，不依赖 X 的任一真子集 |
| **部分函数依赖** `X →p Y` | Y 只依赖 X 的某个真子集 |
| **传递函数依赖** | `X → Y`、`Y → Z`、`Y ↛ X`、`Z ⊄ Y` ⇒ `X →t Z` |

**Armstrong 公理系统**（自反律、增广律、传递律，是**完备且可靠**的推理规则）：
```text
A1 自反律：若 Y ⊆ X ⊆ U，则 X → Y
A2 增广律：若 X → Y 且 Z ⊆ U，则 XZ → YZ
A3 传递律：若 X → Y 且 Y → Z，则 X → Z
推论：合并规则 (X→Y, X→Z ⇒ X→YZ)、分解规则 (X→YZ ⇒ X→Y)、伪传递规则 (X→Y, WY→Z ⇒ WX→Z)
```
**属性闭包 `X⁺`**：由 X 在函数依赖集 F 下能推出的全部属性。算法：从 `X⁺=X` 开始，反复把满足 `A ⊆ X⁺` 的 `A→B` 中的 B 并入，直到不再变化。若 `X⁺ = U`，则 X 是**超码**；若再无真子集满足，则是**候选码**。

::: tip 工作示例 · 求候选码（含完整推导）
设 `R(A,B,C,D,E)`，`F = { AB→C, C→D, D→E, E→A }`，求候选码。

```text
① 分类：L 类（只在左出现）B；R 类（只在右）无；N 类（都不出现）无；LR 类 A,C,D,E
② B 必属于候选码。求 B⁺ = {B}，无法再扩 → 不是码
③ 逐个把 LR 属性加入 B 再求闭包：
   (AB)⁺ = {A,B} → AB→C 加 C → C→D 加 D → D→E 加 E = {A,B,C,D,E} ✔ 候选码
   (BC)⁺ = {B,C} → C→D → D→E → E→A = {A,B,C,D,E} ✔ 候选码
   (BD)⁺ = {B,D} → D→E → E→A → (AB 已含? A、B、C? 由 AB→C 得 C) = 全部 ✔ 候选码
   (BE)⁺ = {B,E} → E→A → AB→C → C→D = 全部 ✔ 候选码
④ 故候选码为 AB、BC、BD、BE（四个）；主属性 = {A,B,C,D,E} 全部，非主属性为空
```
**结论**：R 中所有属性都是主属性 → 至少属于 3NF；再检查决定因素是否都含码（如 `C→D` 中 C 不是码）→ **不属于 BCNF**。
:::

### 12.3 范式与分解（★★★）

| 范式 | 判定条件（逐级包含） | 消除的问题 |
| --- | --- | --- |
| **1NF** | 每个属性都是**不可再分的原子值** | 消除「表中有表」 |
| **2NF** | 1NF + 每个**非主属性完全函数依赖**于每个候选码 | 消除非主属性对码的**部分依赖** |
| **3NF** | 2NF + 每个非主属性**不传递依赖**于码 | 消除非主属性的**传递依赖** |
| **BCNF** | 1NF + **每一个非平凡函数依赖 X→Y 中 X 都含候选码**（即决定因素必为超码） | 消除**主属性**对码的部分/传递依赖 |
| **4NF** | BCNF + 每个非平凡**多值依赖** X→→Y 中 X 含码 | 消除独立的多值事实造成的冗余 |

等价表述：**3NF** 允许 `X→A` 中 A 是主属性（可"放松"），BCNF 完全不允许决定因素不含码。

![函数依赖、范式判定与模式分解](/db/db-normalization.svg)

::: tip 工作示例 · 从 1NF 一步步分解到 3NF（完整链条）
```text
R = SLC(Sno, Sdept, Sloc, Cno, Grade)
F = { (Sno,Cno)→Grade, Sno→Sdept, Sno→Sloc, Sdept→Sloc }
候选码 (Sno,Cno)；非主属性 Sdept, Sloc, Grade

【判定】Sdept、Sloc 只依赖 Sno（主码的一部分）→ 部分依赖 ⇒ 仅 1NF
【分解到 2NF】按「导致部分依赖的决定因素」拆：
   SC(Sno, Cno, Grade)        F1 = {(Sno,Cno)→Grade}      码 (Sno,Cno) → 2NF/3NF/BCNF
   SL(Sno, Sdept, Sloc)       F2 = {Sno→Sdept, Sno→Sloc, Sdept→Sloc}  码 Sno
【判定 SL】Sno→Sdept→Sloc 且 Sdept ↛ Sno ⇒ Sloc 传递依赖于码 ⇒ 2NF 但不是 3NF
【分解到 3NF】
   SD(Sno, Sdept)             F3 = {Sno→Sdept}
   DL(Sdept, Sloc)            F4 = {Sdept→Sloc}
最终：SC、SD、DL 均达 BCNF，且四类异常全部消除
```
**每步都要能答**：违反哪个范式、依据哪条函数依赖、按什么拆、拆完有没有丢东西。
:::

::: tip 补充 · BCNF、4NF 与「无损连接 / 保持依赖」（课件只讲到 3NF）
课件第 12 章明确定义了 1NF、2NF、3NF，**未出现 BCNF、4NF、Armstrong 公理、候选码闭包、无损连接与保持依赖**，需系统补上：

**BCNF 反例**：`STJ(S, T, J)`（学生、教师、课程），`F = {(S,J)→T, (S,T)→J, T→J}`，候选码 `(S,J)` 与 `(S,T)`。所有属性都是主属性 ⇒ 满足 3NF；但 `T→J` 中 T 不含码 ⇒ **不满足 BCNF**。分解为 `ST(S,T)` + `TJ(T,J)` 达 BCNF，但**丢失了 `(S,J)→T`**（说明 BCNF 分解不保证保持依赖）。
**4NF 反例**：`CTB(Course, Teacher, Book)`，一门课有多位教师、多套教材且二者相互独立 ⇒ 存在非平凡多值依赖 `Course→→Teacher`、`Course→→Book`，属 BCNF 但不是 4NF；分解为 `CT(Course,Teacher)`、`CB(Course,Book)`。

**模式分解的两条质量判据**：
- **无损连接性**：分解后各子关系自然连接能**精确还原**原关系（不产生伪元组、不丢失元组）。二元分解 `R→R1,R2` 无损 ⟺ `(R1∩R2) → (R1−R2)` 或 `(R1∩R2) → (R2−R1)` 在 `F⁺` 中。上例 `SL→SD+DL`：交集 `Sdept`，`Sdept→Sloc` 成立 ⇒ 无损。
- **保持依赖性**：分解后各子模式上函数依赖集的并集能逻辑蕴含原 F（保证约束仍可**局部检查**，不必每次做连接）。
- 定理：任何关系模式都可分解为 **3NF 且同时满足无损连接与保持依赖**；BCNF 一定无损但**不一定保持依赖**——这正是工程上常停在 3NF 的原因。
:::

::: danger 易错 · 规范化
- 2NF/3NF 只约束**非主属性**；BCNF 连**主属性**也管。全主属性的关系模式「至少 3NF」但未必 BCNF。
- 「范式越高越好」不绝对：规范化减少冗余却增加**连接开销**，读多写少的报表/数据仓库常主动**反规范化**（冗余列、汇总表、宽表）。
- 分解必须同时检查**无损连接**与**保持依赖**，只满足其一的分解仍可能有害。
- 传递依赖要求中间属性 `Y ↛ X`（若 Y 也能决定 X，则是相互决定，不构成传递依赖）。
:::

---

## 第 13 章 概念结构设计和逻辑结构设计

### 13.1 E-R 模型（★★★）

| 元素 | 图形 | 说明 |
| --- | --- | --- |
| 实体型 | 矩形 | 学生、课程、部门 |
| 属性 | 椭圆 | 学号、姓名；**码属性加下划线** |
| 联系 | 菱形 | 选课、隶属；连线标注 `1:1 / 1:n / m:n` |
| 特殊 | 双矩形（弱实体）、双菱形（标识联系）、ISA 三角形（泛化/继承） | 课件未展开 |

**三类联系与转换思路**：

| 联系 | 例子 | 转换方式 |
| --- | --- | --- |
| 1:1 | 班级 ↔ 班长 | 在任一方加入另一方主码 + 联系属性；或单独建关系（较少） |
| **1:n** | 系 ↔ 学生 | 在 **n 端**关系中加入 1 端主码作外码 + 联系属性（不单独建表） |
| **m:n** | 学生 ↔ 课程 | **必须新建**一个关系，主码为两端主码的组合，含联系自身的属性（如成绩） |
| 多元 / 自联系 | 供应商-项目-零件 / 员工-经理 | 新建关系；自联系用角色名区分两个外码 |

![E-R 图、联系类型与向关系模式转换](/db/db-er.svg)

::: tip 工作示例 · 把 E-R 图转成关系模式（完整答案）
某教学系统：
- 实体：`系(系号, 系名, 系主任)`、`学生(学号, 姓名, 性别)`、`课程(课程号, 课程名, 学分)`
- 联系：`系—学生` 为 **1:n**（"隶属于"，含属性"入学年份"）；`学生—课程` 为 **m:n**（"选修"，含属性"成绩"）

```text
① 系(系号 PK, 系名, 系主任)                       ← 实体直接转
② 学生(学号 PK, 姓名, 性别, 系号 FK, 入学年份)     ← 1:n 把 1 端码与联系属性并入 n 端
③ 课程(课程号 PK, 课程名, 学分)
④ 选修(学号 FK, 课程号 FK, 成绩, PRIMARY KEY(学号,课程号))  ← m:n 必须独立建表
```
**得分点**：① 每个实体一个关系；② 1:n 不单独建表；③ m:n 单独建表且组合主码；④ 联系属性不能丢；⑤ 标出 PK/FK。
:::

**概念结构设计的四种冲突**（合并各局部 E-R 图时须消除）：
| 冲突 | 表现 | 处理 |
| --- | --- | --- |
| 属性冲突 | 同名异义 / 异名同义、类型或取值域不同 | 统一命名与域 |
| 命名冲突 | 同名不同实体、同实体不同名 | 统一术语表 |
| 结构冲突 | 同一对象在一处作实体、另一处作属性；联系类型不一致 | 按全局语义统一（通常抽象为实体） |
| 域/约束冲突 | 不同局部图的码或联系基数不同 | 协商解决 |

**逻辑结构设计**还要：① 按规范化理论优化关系模式；② 设计用户**外模式**（视图），保证逻辑独立性与安全；③ 定义完整性约束与触发器；④ 评估连接代价决定是否反规范化。

---

## 第 14 章 数据库物理结构设计、实施和运行维护

### 14.1 物理设计的内容（★★）

| 任务 | 具体决策 |
| --- | --- |
| 确定存储结构 | 选存储引擎（InnoDB）、是否聚簇、行格式、表空间与数据文件路径 |
| **设计索引** | 对高频查询的 WHERE / JOIN / ORDER BY / GROUP BY 列建索引；联合索引按最左前缀排布；避免过度索引 |
| 聚簇（簇集） | 把经常一起访问、具有相同聚簇码的元组物理相邻存放（MySQL 中主键即聚簇） |
| **分区 / 分表** | RANGE（按日期）、LIST（按地区）、HASH/KEY（均匀打散）、子分区；分区裁剪减少扫描 |
| 确定系统配置 | Buffer Pool 大小、连接数、日志大小、刷盘策略、隔离级别 |
| 评估 | 估算存储空间、I/O 次数与响应时间，权衡时间/空间/维护代价 |

::: tip 补充 · 分区与分库分表（课件只提「存储策略」）
- **分区**：逻辑上一张表、物理上多个段，应用**无感**；分区键必须出现在唯一索引中（MySQL 限制）。
- **分库分表**：水平拆分（按用户 ID 取模/范围）、垂直拆分（按列拆冷热）；引入**分片键选择、跨片 JOIN、分布式事务、全局唯一 ID（雪花算法）、分页与排序**等难题，通常借助中间件（ShardingSphere、MyCat）或分布式数据库（TiDB、OceanBase）。
- **读写分离**：主库写、从库读，靠 binlog 复制；须处理**主从延迟**带来的"刚写就读不到"（可强制读主库或等待 GTID）。
:::

### 14.2 实施、试运行与运维（★★）

```text
① 用 DDL 建库建表、定义完整性约束与视图
② 数据装载（批量导入：LOAD DATA INFILE / mysqlimport，注意先禁索引与外键加速）
③ 编写调试应用程序，联调测试
④ 试运行：小流量验证功能与性能，实测并调整索引/参数
⑤ 正式运行：监控（QPS、慢查询、连接数、锁等待、磁盘、复制延迟）
⑥ 维护：定期备份与恢复演练、转储与重组织、统计信息更新（ANALYZE TABLE）、
        安全审计与权限回收、版本升级与补丁、结构变更（在线 DDL：pt-osc / gh-ost）
```

| 常见性能问题 | 排查与对策 |
| --- | --- |
| 慢查询 | 慢查询日志 → `EXPLAIN` → 补/改索引、改写 SQL、避免 `SELECT *` |
| 锁等待 / 死锁 | `SHOW ENGINE INNODB STATUS`、缩短事务、按固定顺序更新、降隔离级别 |
| 连接数打满 | 排查长事务与连接泄漏，用连接池、限制 `max_connections` |
| 磁盘/内存 | 冷热分离、归档历史表、调整 Buffer Pool、清理 binlog 过期 |

::: danger 易错 · 设计与实施
- 「概念结构设计**独立于**具体 DBMS」；「逻辑结构设计**依赖**所选数据模型」；「物理结构设计**依赖**具体 DBMS 与硬件」。
- 视图设计属于**逻辑结构设计**阶段（外模式），不是物理设计。
- 分区表不是"多张表"，应用 SQL 无需改写；分库分表则需要应用层/中间件配合。
- 规范化到 3NF 是设计**起点**而非终点，实际系统常因性能做有意识的反规范化，并用触发器/应用逻辑维护冗余一致性。
:::

---

## 第 15 章 存储过程与函数

### 15.1 MySQL 编程基础（★★）

| 元素 | 语法 |
| --- | --- |
| 改结束符 | `DELIMITER //`（因为过程体内部含大量 `;`，必须临时换分隔符） |
| 局部变量 | `DECLARE v_name VARCHAR(20) DEFAULT '';`（须在 `BEGIN` 后最前面） |
| 赋值 | `SET v = 10;` / `SELECT col INTO v FROM t WHERE …;` |
| 用户变量 / 系统变量 | `@v`（会话级） / `@@global.var`、`@@session.var` |
| 分支 | `IF … THEN … ELSEIF … ELSE … END IF;` / `CASE … WHEN … THEN … END CASE;` |
| 循环 | `WHILE … DO … END WHILE` / `REPEAT … UNTIL … END REPEAT` / `LOOP … LEAVE label; … END LOOP` |
| 内置函数 | 字符串 `CONCAT/SUBSTRING/TRIM/UPPER`、数值 `ROUND/CEIL/FLOOR`、日期 `NOW/DATE_ADD/DATEDIFF`、聚合 `COUNT/SUM/AVG`、条件 `IFNULL/COALESCE/CASE` |

### 15.2 存储过程（★★★）

**存储过程**是预编译并存储在数据库中的一段 SQL 程序，可由 `CALL` 调用，可带参数并多次复用。

```sql
DELIMITER //
CREATE PROCEDURE sp_get_student(IN p_sdept VARCHAR(20), OUT p_cnt INT)
BEGIN
  DECLARE v_avg DECIMAL(5,2);
  SELECT COUNT(*), AVG(Sage) INTO p_cnt, v_avg
  FROM Student WHERE Sdept = p_sdept;
  SELECT p_sdept AS dept, p_cnt AS cnt, v_avg AS avg_age;
END //
DELIMITER ;

CALL sp_get_student('CS', @n);
SELECT @n;
DROP PROCEDURE IF EXISTS sp_get_student;
```

| 参数模式 | 含义 |
| --- | --- |
| `IN` | 输入（默认），过程内可读、修改不传回 |
| `OUT` | 输出，过程内赋值后由调用者读取 |
| `INOUT` | 既输入又输出 |

| 优点 | 缺点 |
| --- | --- |
| 减少网络传输（多语句一次调用）、预编译执行快、封装业务逻辑、便于权限控制 | 与应用代码耦合、调试与版本管理困难、移植性差、占数据库 CPU（业务逻辑应尽量放应用层） |

### 15.3 自定义函数与游标（★★）

```sql
-- 标量函数：必须有返回值、声明特征
DELIMITER //
CREATE FUNCTION fn_grade_level(g INT) RETURNS VARCHAR(10)
DETERMINISTIC
BEGIN
  RETURN CASE WHEN g IS NULL THEN '未考'
              WHEN g >= 90 THEN '优秀'
              WHEN g >= 60 THEN '及格'
              ELSE '不及格' END;
END //
DELIMITER ;
SELECT Sname, fn_grade_level(Grade) FROM Student JOIN SC USING(Sno);

-- 游标：逐行处理结果集（DECLARE 顺序：变量 → 游标 → HANDLER）
DELIMITER //
CREATE PROCEDURE sp_loop_score()
BEGIN
  DECLARE done INT DEFAULT 0;
  DECLARE v_sno CHAR(7); DECLARE v_g INT;
  DECLARE cur CURSOR FOR SELECT Sno, Grade FROM SC;
  DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = 1;
  OPEN cur;
  read_loop: LOOP
    FETCH cur INTO v_sno, v_g;
    IF done = 1 THEN LEAVE read_loop; END IF;
    IF v_g IS NULL THEN UPDATE SC SET Grade = 0 WHERE Sno = v_sno; END IF;
  END LOOP;
  CLOSE cur;
END //
DELIMITER ;
```

::: danger 易错 · 存储过程与函数
| | 存储过程 PROCEDURE | 函数 FUNCTION |
| --- | --- | --- |
| 调用 | `CALL sp()` | `SELECT fn()`，可嵌入 SQL 表达式 |
| 返回值 | 通过 OUT 参数/结果集，可无返回值 | **必须** `RETURNS` 且 `RETURN` 单值 |
| 参数 | IN / OUT / INOUT | 只有 IN |
| 事务 | 过程内可 `COMMIT/ROLLBACK`（须自行管理） | 一般不允许显式事务 |
| 声明特征 | 可选 | 必须声明 `DETERMINISTIC / NO SQL / READS SQL DATA` 之一（开启 binlog 时） |

游标 `NOT FOUND` 处理器必须在**游标 DECLARE 之后**；否则 `FETCH` 到末尾会直接报错而不是置 done。
:::

---

## 第 16 章 触发器和事件

### 16.1 触发器（★★★）

**触发器**是由 `INSERT/UPDATE/DELETE` 事件**自动触发**执行的一段特殊存储过程，不能被 `CALL` 直接调用，用于维护衍生数据、审计日志、复杂完整性约束。

```sql
DELIMITER //
CREATE TRIGGER trg_sc_before_insert
BEFORE INSERT ON SC
FOR EACH ROW
BEGIN
  IF NEW.Grade < 0 OR NEW.Grade > 100 THEN
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = '成绩必须在 0~100 之间';
  END IF;
END //

CREATE TRIGGER trg_student_after_delete
AFTER DELETE ON Student
FOR EACH ROW
BEGIN
  INSERT INTO student_audit(Sno, Sname, op_time, op_type)
  VALUES (OLD.Sno, OLD.Sname, NOW(), 'DELETE');
END //
DELIMITER ;

SHOW TRIGGERS;
DROP TRIGGER IF EXISTS trg_sc_before_insert;
```

| 要点 | 说明 |
| --- | --- |
| 触发时机 | `BEFORE`（可校验/改写 `NEW` 值）/ `AFTER`（审计、级联维护） |
| 粒度 | MySQL 只支持 **`FOR EACH ROW` 行级**触发器，不支持语句级 |
| `NEW` / `OLD` | `NEW` = 新行（INSERT/UPDATE 可用）；`OLD` = 旧行（UPDATE/DELETE 可用）；**INSERT 无 OLD、DELETE 无 NEW** |
| 组合 | 一张表同一时机同一事件可有多个触发器（MySQL 5.7+），执行顺序可用 `FOLLOWS/PRECEDES` 指定；旧版本每种最多一个 |
| 限制 | 触发器内**不能对触发表本身再做 DML**（会报「Can't update table … already in use」）；不能显式事务控制 |

### 16.2 事件调度器（★★）

**事件**是按时间计划由**事件调度器线程**执行的一段 SQL，可一次性或周期性运行，类似数据库内的定时任务（对比 Linux crontab）。

```sql
SET GLOBAL event_scheduler = ON;         -- 或配置文件 event_scheduler=ON
DELIMITER //
CREATE EVENT ev_purge_log
ON SCHEDULE EVERY 1 DAY STARTS '2026-11-14 02:00:00'
DO BEGIN
  DELETE FROM access_log WHERE create_time < DATE_SUB(NOW(), INTERVAL 90 DAY);
END //
DELIMITER ;
ALTER EVENT ev_purge_log DISABLE;        -- 停用
SHOW EVENTS;
DROP EVENT IF EXISTS ev_purge_log;
```

| 对比 | 触发器 | 事件 |
| --- | --- | --- |
| 触发源 | **表上的 DML 操作**（数据变化） | **时间**（到达计划时刻） |
| 频率 | 每次 DML 逐行触发 | 一次或周期性 |
| 典型用途 | 完整性校验、审计、级联维护 | 定时清理、统计汇总、报表生成 |

![存储过程、触发器与事件](/db/db-program.svg)

::: danger 易错 · 触发器与事件
- 触发器与触发它的语句在**同一事务**内，触发器失败或 `SIGNAL` 抛错会使整个语句回滚。
- 触发器隐式执行的 SQL 对应用「不可见」，是排查数据被莫名修改的常见盲区；上线前应 `SHOW TRIGGERS` 盘点。
- 触发器开销随 DML 量线性增长，大批量导入时可临时禁用或改用批处理校验。
- 事件依赖 `event_scheduler=ON`，默认可能关闭；创建成功但没执行应先查该变量与 `SHOW EVENTS` 的状态。
:::

---

## 第 17 章 使用编程语言连接 MySQL 数据库

### 17.1 连接流程与两种主流 API（★★★）

```text
① 加载驱动 / 导入模块 → ② 建立连接（主机、端口、库、用户、密码、字符集）
→ ③ 创建游标/Statement → ④ 执行 SQL（参数化） → ⑤ 取结果集
→ ⑥ 事务提交或回滚 → ⑦ 关闭游标与连接（或归还连接池）
```

```python
# Python（PyMySQL，参数化 + 显式事务）
import pymysql
conn = pymysql.connect(host='127.0.0.1', port=3306, user='app',
                       password='***', database='teaching',
                       charset='utf8mb4', autocommit=False)
try:
    with conn.cursor() as cur:
        cur.execute("SELECT Sname, Sage FROM Student WHERE Sdept=%s AND Sage>%s",
                    ('CS', 18))                 # %s 是占位符，不是字符串拼接
        for name, age in cur.fetchall():
            print(name, age)
        cur.execute("UPDATE Student SET Sage=Sage+1 WHERE Sno=%s", ('2021001',))
    conn.commit()
except Exception:
    conn.rollback()
    raise
finally:
    conn.close()
```

```java
// Java（JDBC，PreparedStatement 防注入）
String sql = "SELECT Sname, Sage FROM Student WHERE Sdept=? AND Sage>?";
try (Connection c = DriverManager.getConnection(url, user, pwd);
     PreparedStatement ps = c.prepareStatement(sql)) {
    ps.setString(1, "CS");
    ps.setInt(2, 18);
    try (ResultSet rs = ps.executeQuery()) {
        while (rs.next()) System.out.println(rs.getString("Sname"));
    }
}
```

| 对比 |  Statements | PreparedStatement / 参数化 |
| --- | --- | --- |
| SQL 结构 | 每次拼接完整字符串 | 结构预编译，参数单独绑定 |
| 注入风险 | 高 | **无** |
| 重复执行 | 每次重新解析 | 可复用执行计划，更快 |
| NULL / 特殊字符 | 需手工转义 | 驱动自动处理 |

### 17.2 事务边界与连接池（★★★）

```python
# 关闭 autocommit 后，多条语句才属于同一事务
conn.autocommit(False)
try:
    cur.execute("UPDATE account SET bal=bal-100 WHERE id=1")
    cur.execute("UPDATE account SET bal=bal+100 WHERE id=2")
    conn.commit()
except Exception:
    conn.rollback()
```

**连接池**（HikariCP / Druid / DBUtils.PooledDB）：预先建立并复用物理连接，避免每次请求都做 TCP 握手与认证（昂贵）；需配置最小/最大连接数、空闲超时、连接有效性检测（`SELECT 1`）、等待超时。

| 实践要点 | 说明 |
| --- | --- |
| 参数化查询 | 所有外部输入必须绑定参数；动态表名/列名用**白名单** |
| 最小权限账号 | 应用连接不要 `root`，按功能分读写账号 |
| 显式事务 | 关闭 autocommit，明确 commit/rollback；事务尽量**短**，避免长事务持锁 |
| 资源释放 | `try-with-resources` / `finally` 关闭 ResultSet、Statement、Connection（归还池） |
| 字符集统一 | 连接串指定 `utf8mb4`，防乱码与隐式转换导致的索引失效 |
| 错误处理 | 捕获唯一键冲突、外键失败、死锁（1213）与锁等待超时（1205），必要时**有限次重试** |

![编程连接、预处理与连接池](/db/db-connection.svg)

::: tip 补充 · 课件以 API 调用为主，需补的工程结论
课件第 17 章大量篇幅展示 Python/Java 连接示例，但**未系统讲「预处理语句防注入」「连接池」「事务边界」「资源释放」**四件事。生产代码的关键不在「能不能连上」，而在：① 一律参数化；② 用连接池且正确归还；③ 显式事务、及时提交；④ 处理死锁/超时重试；⑤ 应用账号最小权限。这些同时也是面试高频考点。
:::

---

## 各章深挖专题

### 深 1 · NULL 与三值逻辑（贯穿查询、约束、索引）

```text
SQL 逻辑值：TRUE / FALSE / UNKNOWN
NULL = NULL        → UNKNOWN（不是 TRUE！）
NOT UNKNOWN        → UNKNOWN
WHERE 只保留 TRUE 的行，FALSE 与 UNKNOWN 都被丢弃
```
| 场景 | 陷阱 | 正确写法 |
| --- | --- | --- |
| 判空 | `WHERE col = NULL` 恒空 | `col IS NULL` / `IS NOT NULL` |
| 聚合 | `SUM/AVG/MAX/MIN/COUNT(col)` 忽略 NULL | 需当 0 时用 `COALESCE(col,0)`；`COUNT(*)` 计全部行 |
| `NOT IN` | 子查询含 NULL → 结果恒空 | 改 `NOT EXISTS` 或加 `IS NOT NULL` |
| 外连接 | 补 NULL 的行仍参与 `COUNT(*)` | 用 `COUNT(右表列)` |
| 唯一约束 | MySQL 的 UNIQUE 允许多个 NULL | 需"非空唯一"时显式加 `NOT NULL` |
| 排序 | MySQL 升序时 NULL 排最前 | 用 `ORDER BY col IS NULL, col` 控制 |

### 深 2 · 关系代数 ↔ SQL 对照表

| 关系代数 | SQL |
| --- | --- |
| `σ_F(R)` | `SELECT * FROM R WHERE F` |
| `π_A(R)` | `SELECT DISTINCT A FROM R` |
| `R ∪ S` | `SELECT … FROM R UNION SELECT … FROM S` |
| `R − S` | `SELECT … FROM R EXCEPT SELECT … FROM S`（MySQL 用 `NOT EXISTS` / `LEFT JOIN … IS NULL`） |
| `R ∩ S` | `INTERSECT`（MySQL 用 `INNER JOIN` / `IN`） |
| `R × S` | `CROSS JOIN` |
| `R ⋈ S` | `JOIN … ON` / `NATURAL JOIN` |
| `R ÷ S` | 双重 `NOT EXISTS` 或 `GROUP BY + HAVING COUNT(DISTINCT)` |
| `γ_{G, agg}(R)` | `SELECT G, agg(…) FROM R GROUP BY G`（分组聚合是关系代数的扩展） |

::: tip 工作示例 · 除运算的两种 SQL 写法
查询「选修了全部课程的学生学号」：
```sql
-- 写法 A：双重否定（严格对应除运算）
SELECT DISTINCT s.Sno FROM SC s
WHERE NOT EXISTS (
  SELECT 1 FROM Course c
  WHERE NOT EXISTS (SELECT 1 FROM SC x WHERE x.Sno=s.Sno AND x.Cno=c.Cno));
-- 写法 B：计数法（课程无重复、SC 无重复选课时等价）
SELECT Sno FROM SC GROUP BY Sno
HAVING COUNT(DISTINCT Cno) = (SELECT COUNT(*) FROM Course);
```
教学库上两种写法在本例都返回**空集**（无人选修全部 4 门课）。若把课程表只留 3 门，李勇（选 1、2、3）才会被选出。
:::

### 深 3 · 索引选择与执行计划诊断

```text
表 SC(Sno, Cno, Grade)，现有联合索引 idx_sc(Sno, Grade)
① WHERE Sno='2021001'                       ✔ 用最左列
② WHERE Sno='2021001' AND Grade>80           ✔ 两列都用（范围列之后停止）
③ WHERE Grade>80                            ✘ 跳过最左列（全表/全索引扫描）
④ WHERE Sno LIKE '%001'                     ✘ 前置通配
⑤ WHERE Sno+''='2021001'                    ✘ 对索引列做运算
⑥ SELECT Grade FROM SC WHERE Sno='2021001'  ✔ 覆盖索引，无需回表
```
`EXPLAIN` 中 `type=ALL` 或 `rows` 极大、`Extra` 出现 `Using filesort / Using temporary` 是优化信号；但数据量很小时优化器选择全表扫描是**正确**的（随机 I/O 比顺序扫更贵），不要机械地"强制索引"。

### 深 4 · 事务调度可串行化判定（优先图）

**题**：两个事务（A、B 为数据项）
```text
T1: R(A)  W(A)  R(B)  W(B)
T2: R(A)  W(A)  R(B)  W(B)
调度 S: R1(A) R2(A) W1(A) W2(A) R2(B) W2(B) R1(B) W1(B)
```
**解**：列出**冲突操作**（不同事务、同一数据项、至少一个写）：
```text
A 上：R2(A) 在 W1(A) 之前 → T2 → T1；W1(A) 在 W2(A) 之前 → T1 → T2  ⇒ 出现环
B 上：W2(B) 在 R1(B) 之前 → T2 → T1；R2(B) 在 W1(B) 之前 → T2 → T1
优先图：T1 ⇄ T2（有环）⇒ 该调度**不是冲突可串行化**的
```
若优先图无环，则拓扑序即等价的串行次序（如 T1→T2）。**2PL 保证可串行化但不保证无死锁**；时间戳排序、乐观并发控制（OCC/MVCC）是另外的实现路线。

### 深 5 · 无损连接与保持依赖的验证

对 `SL(Sno,Sdept,Sloc)` 分解为 `SD(Sno,Sdept)` + `DL(Sdept,Sloc)`：
```text
① 交集 R1∩R2 = {Sdept}
② R1−R2 = {Sno}；R2−R1 = {Sloc}
③ 检查 Sdept→Sno？不成立；Sdept→Sloc？F 中有 ✔ ⇒ 无损连接
④ 保持依赖：F1={Sno→Sdept}、F2={Sdept→Sloc}，
   二者的并集可推出原 F 中 Sno→Sloc（传递）✔ ⇒ 保持依赖
```
作为对照，BCNF 分解 `STJ → ST + TJ` 虽无损，却丢失 `(S,J)→T`（不保持依赖）——这正是「3NF 可同时保证无损+保持依赖，BCNF 只能保证无损」的具体例证。

### 深 6 · MySQL 8.0 重要新特性（补充）

| 特性 | 说明 |
| --- | --- |
| **CTE 与递归 CTE** | `WITH cte AS (…) SELECT …`；`WITH RECURSIVE` 处理树形/层级数据 |
| **窗口函数** | `ROW_NUMBER / RANK / DENSE_RANK / LAG / LEAD / SUM() OVER(PARTITION BY …)`，不折叠行 |
| JSON 增强 | JSON 类型、JSON 函数、函数索引（Generated Column） |
| 角色、原子 DDL、降序索引、不可见索引 | 权限批量管理、DDL 崩溃安全、排序优化、索引灰度下线 |
| `utf8mb4_0900_ai_ci` 默认校对 | 真正 UTF-8、性能更好 |
| 移除查询缓存 | 高并发下命中率低且锁竞争严重，改用应用层缓存（Redis） |
| `CHECK` 约束生效、隐藏列、EXPLAIN ANALYZE | 完整性增强与执行计划实测 |

### 深 7 · 数据库新技术与选型速览（补充）

```text
单机关系型 MySQL/PostgreSQL       → 事务、复杂查询、中等规模
缓存 Redis                       → 热点数据、会话、限流、分布式锁
文档 MongoDB / 搜索 Elasticsearch → 半结构化、全文检索
列族 HBase / 时序 InfluxDB       → 海量写入、监控指标
图 Neo4j                         → 关系网络、路径分析
分布式/HTAP TiDB、OceanBase      → 水平扩展 + 强一致事务
分析型 ClickHouse / 数据仓库      → 列存、OLAP 聚合
```
选型三问：① 是否需要 **ACID 强事务**？② 数据规模与增长是否需要**水平扩展**？③ 查询模式是**点查/范围**还是**大规模聚合**？此外要考虑运维能力、生态兼容（MySQL 协议）、成本与国产化要求。

### 深 8 · 常见 SQL 书写规范与性能清单

```text
✔ 明确列名，避免 SELECT *
✔ 条件中的列保持"裸列"，不做函数/运算/隐式转换
✔ 大表分页避免 LIMIT 1000000, 20，改用游标式 WHERE id > last_id LIMIT n
✔ 用 EXISTS 替代大 IN 集合；UNION ALL 优先于 UNION
✔ 批量插入用多值 INSERT / LOAD DATA，减少往返
✔ 事务尽量短，按固定顺序更新多行以防死锁
✔ 定期 ANALYZE TABLE 更新统计信息，检查慢查询日志
✘ 在生产库直接跑无 WHERE 的 UPDATE/DELETE（先 SELECT 验证范围）
✘ 用触发器隐式维护核心业务逻辑（难以排查）
```

## 综合例题精讲（跨章）

> 按「读题 → 写 SQL / 画模式 → 完整结果 → 结论」展开。所有 SQL 例题结果均已在教学库实际执行验证。

### 综 1 · SQL 综合查询（第 5、6 章）

**题**：基于教学库 `Student / Course / SC`，写出 5 条查询并给出结果。

```sql
-- ① CS 系年龄小于 20 的学生姓名与年龄
SELECT Sname, Sage FROM Student WHERE Sdept='CS' AND Sage<20;
-- → 刘晨 | 19

-- ② 人数不少于 2 的系、人数与平均年龄
SELECT Sdept, COUNT(*) AS n, AVG(Sage) AS avg_age
FROM Student GROUP BY Sdept HAVING COUNT(*)>=2;
-- → CS | 2 | 19.5

-- ③ 选修「数据库」且成绩 > 80 的学生（三表连接）
SELECT s.Sname, sc.Grade FROM Student s
JOIN SC sc ON s.Sno=sc.Sno JOIN Course co ON sc.Cno=co.Cno
WHERE co.Cname='数据库' AND sc.Grade>80;
-- → 李勇 | 92

-- ④ 统计每位学生选课门数（含 0 门）
SELECT s.Sname, COUNT(sc.Cno) AS cnt FROM Student s
LEFT JOIN SC sc ON s.Sno=sc.Sno
GROUP BY s.Sno, s.Sname ORDER BY cnt DESC, s.Sname;
-- → 李勇 3 / 刘晨 2 / 张立 1 / 王敏 1

-- ⑤ 无人选修的课程（NOT EXISTS）
SELECT Cname FROM Course c
WHERE NOT EXISTS (SELECT 1 FROM SC sc WHERE sc.Cno=c.Cno);
-- → 操作系统
```
**易错复盘**：④ 若写 `COUNT(*)` 会把补 NULL 的行也计入；若写 `COUNT(sc.Grade)` 则王敏那门（Grade 为 NULL）会被漏掉，得到 0。⑤ 若改用 `NOT IN (SELECT Cno FROM SC)` 恰好也成立（SC.Cno 无 NULL），但一旦子查询含 NULL 就会整体返回空集。

### 综 2 · 从 1NF 分解到 BCNF（第 2、12 章）

**题**：`SLC(Sno,Sdept,Sloc,Cno,Grade)`，`F={(Sno,Cno)→Grade, Sno→Sdept, Sno→Sloc, Sdept→Sloc}`。指出范式级别、异常，给出分解并验证无损与保持依赖。

**解**：
```text
① 候选码 (Sno,Cno)（由 F 推：Sno、Cno 必须同时出现才能决定 Grade；Sno→Sdept/Sloc）
② 非主属性 Sdept、Sloc 只依赖 Sno ⇒ 对码部分依赖 ⇒ 仅 1NF
③ 异常：冗余（系楼重复）、插入（新生未选课无法录）、删除（退课丢系信息）、更新（搬楼改多行）
④ 分解到 2NF（按部分依赖拆）：
   SC(Sno,Cno,Grade)    F1={(Sno,Cno)→Grade}
   SL(Sno,Sdept,Sloc)  F2={Sno→Sdept, Sno→Sloc, Sdept→Sloc}
⑤ SL 中 Sno→Sdept→Sloc 且 Sdept↛Sno ⇒ 传递依赖 ⇒ 2NF 非 3NF
⑥ 分解到 3NF：SD(Sno,Sdept)、DL(Sdept,Sloc)
⑦ 最终 SC、SD、DL 三个关系均达 BCNF（每个决定因素都含码）
⑧ 无损验证（SL→SD+DL）：交集 Sdept，Sdept→Sloc ∈ F⁺ ⇒ 无损连接
   保持依赖：{Sno→Sdept} ∪ {Sdept→Sloc} 可推出 Sno→Sloc ⇒ 保持依赖
```
**结论**：该分解同时满足无损连接、保持依赖与 BCNF，是理想结果；但并非所有模式都能三者兼得（BCNF 分解可能丢依赖，此时常停在 3NF）。

### 综 3 · E-R 图转关系模式（第 11、13 章）

**题**：图书借阅系统——`读者(借书证号, 姓名, 单位)`、`图书(书号, 书名, 作者, 库存)`；一个读者可借多本、一本可被多人借（**m:n**，联系含 `借期、还期`）；`单位(单位号, 名称)` 与读者是 **1:n**。给出关系模式集。

**解**：
```text
① 单位(单位号 PK, 名称)
② 读者(借书证号 PK, 姓名, 单位号 FK)            ← 1:n 把 1 端码并入 n 端（不单独建表）
③ 图书(书号 PK, 书名, 作者, 库存)
④ 借阅(借书证号 FK, 书号 FK, 借期, 还期,
        PRIMARY KEY(借书证号, 书号, 借期))      ← m:n 必须独立建表，联系属性不能丢
```
**为什么主码要加借期**：同一读者可能多次借同一本书，仅 `(证号,书号)` 会冲突；若业务规定「同一时刻不能重复借」，也可用代理主码 `借阅ID` + 唯一约束。四类常见失分：1:n 单独建了表、m:n 没独立建表、漏了联系属性、没标 PK/FK。

### 综 4 · 事务调度可串行化（第 9 章）

**题**：判断调度 `S = R1(A) R2(A) W1(A) W2(A) R2(B) W2(B) R1(B) W1(B)` 是否冲突可串行化。

**解**：冲突对（不同事务、同一数据项、至少一写）：
```text
A：R2(A) 先于 W1(A) → T2→T1；W1(A) 先于 W2(A) → T1→T2
B：R2(B) 先于 W1(B) → T2→T1；W2(B) 先于 R1(B) → T2→T1
优先图含 T1⇄T2 环 ⇒ 不是冲突可串行化调度
```
若要修正，可让 T1 与 T2 遵守**两段锁协议**（各自一次性申请所需 X 锁，事务结束统一释放），所得调度必可串行化，但可能出现死锁需要检测与回滚。

### 综 5 · 并发异常与隔离级别（第 9 章）

**题**：余额 `A=100`。T1、T2 都执行「读 A、减 10、写回」。若不加控制最终结果可能是多少？如何用隔离级别与锁避免？

**解**：
```text
不加控制：T1、T2 同时读到 100，各算出 90 并写回 → 最终 90（应 80）⇒ 丢失修改
```
对策：
- **一级封锁协议**：写前对 A 加 X 锁并保持到事务结束，第二个事务必须等待 → 最终 80。
- **原子更新**：`UPDATE account SET bal=bal-10 WHERE id=1`（数据库对该行加行锁）→ 同样避免。
- **悲观锁**：`SELECT bal FROM account WHERE id=1 FOR UPDATE` 后再更新。
- **乐观锁**：`UPDATE … SET bal=bal-10 WHERE id=1 AND bal=100`，检查 affected rows，失败则重试。
- **隔离级别**：`READ UNCOMMITTED` 连脏读都允许；`SERIALIZABLE` 可完全避免但并发度最低。**仅提高隔离级别并不能自动解决"读-改-写"型丢失修改**（RR 下两个事务都能读到快照 100），必须配合行锁或原子更新——这是最常见的 misconceptions。

### 综 6 · 索引与 EXPLAIN 诊断（第 6、7 章）

**题**：`SC(Sno,Cno,Grade)` 上有联合索引 `idx(Sno,Grade)`，判断下列 4 条 SQL 能否用上索引，并说明如何改写。

```text
① WHERE Sno='2021001' AND Grade>80        ✔ 最左列等值 + 第二列范围（用到两列）
② WHERE Grade>80                           ✘ 跳过最左列，退化为全索引/全表扫描
   → 改写：新建以 Grade 打头的索引，或补上 Sno 条件
③ WHERE SUBSTRING(Sno,1,4)='2021'         ✘ 对索引列用函数
   → 改写：Sno LIKE '2021%'（前缀匹配可用索引）或使用生成列 + 索引
④ SELECT Grade FROM SC WHERE Sno='2021001' ✔ 覆盖索引，Extra 显示 Using index，无需回表
```
**诊断顺序**：慢查询日志定位 → `EXPLAIN` 看 `type/key/rows/Extra` → 检查是否违反最左前缀或列被函数包裹 → 补/改索引或改写 SQL → 复测。小表全表扫描是优化器的合理选择，不必强行加索引。

### 综 7 · 备份与时间点恢复方案（第 10 章）

**题**：某库每日 02:00 全量备份，binlog 保留 7 天。今日 14:30 误执行 `DROP TABLE orders`，如何恢复且尽量少丢数据？

**解**：
```text
① 立即停止写入 / 切流量，防止二次破坏；确认 binlog 文件未过期
② 在临时实例还原今日 02:00 的全量备份：mysql -u root -p < full_0200.sql
③ 用 mysqlbinlog 重放 02:00 之后到 14:29:59 的 binlog（跳过 DROP 语句）：
   mysqlbinlog --start-datetime="2026-11-13 02:00:00" \
               --stop-datetime="2026-11-13 14:29:59" mysql-bin.000003 | mysql -u root -p
   或按位点 --start-position / --stop-position 精确跳过误操作（更可靠）
④ 校验数据一致性后，导出 orders 表并回灌生产库
⑤ 复盘：加权限管控（应用账号不应有 DROP）、开启延迟从库、定期演练恢复
```
**RPO / RTO**：本方案 RPO ≈ 0（binlog 完整时可精确到误操作前一刻），RTO 取决于全量备份体积与 binlog 回放时长。注意 **TRUNCATE/DROP 是 DDL、隐式提交，无法用回滚或 undo 撤销**。

### 综 8 · 服务端编程与防注入综合（第 8、15、16、17 章）

**题**：实现「插入一条选课记录，成绩须在 0~100，且写审计日志」，要求应用层参数化、数据库层校验与审计各司其职。

```sql
-- 数据库层：BEFORE 触发器做域校验
DELIMITER //
CREATE TRIGGER trg_sc_check BEFORE INSERT ON SC FOR EACH ROW
BEGIN
  IF NEW.Grade IS NOT NULL AND (NEW.Grade<0 OR NEW.Grade>100) THEN
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT='Grade out of range';
  END IF;
END //
-- AFTER 触发器写审计
CREATE TRIGGER trg_sc_audit AFTER INSERT ON SC FOR EACH ROW
BEGIN
  INSERT INTO sc_audit(Sno,Cno,Grade,op_time) VALUES(NEW.Sno,NEW.Cno,NEW.Grade,NOW());
END //
DELIMITER ;
```
```python
# 应用层：参数化 + 显式事务（绝不拼接 SQL）
try:
    with conn.cursor() as cur:
        cur.execute("INSERT INTO SC(Sno,Cno,Grade) VALUES(%s,%s,%s)",
                    (sno, cno, grade))
    conn.commit()
except Exception:
    conn.rollback()
    raise
finally:
    conn.close()
```
**分工原则**：**结构完整性**（PK/FK/CHECK/触发器）放数据库层保证所有写入路径都受约束；**业务逻辑**尽量放应用层便于测试与版本管理；**参数化查询**在应用层杜绝注入；触发器与业务语句在同一事务，抛错即整体回滚。

## 补充与修正汇总（对照课件）

> 「**修正**」＝课件表述需订正或明确边界；「**补充**」＝课件以提纲为主、未展开但应掌握的知识。所属课程一律泛化表述，笔记正文不写版次、作者与出版社。

| # | 章节 | 类型 | 课件现状 | 补充 / 修正内容 |
| --- | --- | --- | --- | --- |
| 1 | 1.2 | **修正** | 列出三级模式，未点明「两级映像」与数据独立性的因果 | 补外模式/模式映像 → 逻辑独立性、模式/内模式映像 → 物理独立性；强调模式与内模式各一个、外模式多个 |
| 2 | 1.3 | 补充 | 提及新技术与国产数据库 | 系统补 NoSQL 四类、NewSQL/分布式、HTAP/湖仓一体、国产数据库与选型三问 |
| 3 | 2.2 | 补充 | 讲实体与参照完整性 | 补**用户定义完整性**（NOT NULL/UNIQUE/CHECK/触发器）与外码为 NULL 的边界、违约处理（RESTRICT/CASCADE/SET NULL） |
| 4 | 2.3 | 补充 | 列关系代数运算 | 补自然连接去重列、外连接与悬浮元组、除运算 ↔ SQL 双重否定 / GROUP BY+HAVING 的对应 |
| 5 | 2.3 | 补充 | 讲关系代数 | 补关系演算（元组/域）与「SQL 具有关系完备性」 |
| 6 | 3.1 | **补充** | 只讲「查询/定义/操纵/控制」四功能 | 补 **DDL/DML/DQL/DCL/TCL** 标准分类、`TRUNCATE` 属 DDL、DDL 隐式提交不可回滚 |
| 7 | 3.2 | 补充 | MySQL 简介 | 补一条 SQL 的完整执行路径（连接→解析→预处理→优化器→执行器→存储引擎）、`EXPLAIN` |
| 8 | 3.2 | 修正 | 未区分标准 SQL 与方言 | 明确 `CONCAT` vs `\|\|`、`LIMIT` vs `FETCH FIRST`、反引号 vs 双引号、`ONLY_FULL_GROUP_BY` |
| 9 | 4.1 | 补充 | 列 InnoDB/MyISAM/MEMORY | 补 InnoDB 四特性、行锁 vs 表锁、聚簇索引、崩溃恢复，以及引擎选择的业务判据 |
| 10 | 4.2 | 修正 | 给 `CREATE DATABASE` 语法 | 强调 MySQL `utf8` 实为 utf8mb3、**必须 utf8mb4**；改库默认字符集不转换既有列 |
| 11 | 5.1 | 补充 | 列数据类型 | 补 `INT(11)` 只是显示宽度、金额必须 DECIMAL、`TIMESTAMP` 时区与 2038 问题、JSON/生成列 |
| 12 | 5.2 | 补充 | 讲约束 | 补 MySQL 8.0.16 前 `CHECK` 仅解析不生效、UNIQUE 允许多个 NULL、`AUTO_INCREMENT` 条件 |
| 13 | 5.3 | 补充 | INSERT/UPDATE/DELETE | 补 `TRUNCATE` 与三者对照、`INSERT … SELECT`、忘写 WHERE 的全表事故与 `sql_safe_updates` |
| 14 | 6.1 | **补充** | 给 SELECT 语法格式 | 补**真实执行顺序** FROM→WHERE→GROUP BY→HAVING→SELECT→ORDER BY→LIMIT，及 WHERE 不能用别名/聚合 |
| 15 | 6.1 | 补充 | 讲谓词 | 补三值逻辑与 NULL 全套陷阱（IS NULL、NOT IN 含 NULL、COUNT 差异、聚合忽略 NULL） |
| 16 | 6.2 | 补充 | 讲多关系查询 | 补 LEFT/RIGHT/CROSS JOIN、自连接、`UNION` vs `UNION ALL`、LEFT JOIN 后 `COUNT(右表列)` 的必要性 |
| 17 | 6.3 | 补充 | 讲子查询 | 补 `EXISTS` 与非相关子查询效率、`NOT EXISTS` 表达「全部」、CTE/派生表、除运算两种写法 |
| 18 | 6.x | **补充** | 未讲查询优化 | 补 `EXPLAIN` 各列含义、索引失效六类场景、覆盖索引、分页优化 |
| 19 | 7.1 | 补充 | 讲视图管理 | 补「视图是外模式实现 → 逻辑独立性」、可更新视图限制清单、`WITH CHECK OPTION` |
| 20 | 7.2 | **补充（重点）** | 只讲索引管理语句 | 系统补 **B+树结构、聚簇/二级索引与回表、最左前缀、覆盖索引、索引失效与「索引不是越多越好」** |
| 21 | 8.x | **补充** | 讲用户/权限/角色 | 补权限四层级与系统表、`CREATE USER` 先于 `GRANT`、**SQL 注入原理与参数化查询**、最小权限与审计 |
| 22 | 9.1 | **修正 + 补充** | 用中文描述事务四性质，标题出现「**事物**的隔离级别」笔误 | 订正为「**事务**」；补 **ACID 缩写**与「A↔undo、D↔redo、I↔锁/MVCC、C↔最终结果」实现映射 |
| 23 | 9.2 | 补充 | 讲并发不一致与隔离级别 | 补**丢失修改/脏读/不可重复读/幻读**四异常对照表、`@@transaction_isolation`、InnoDB RR 下 Next-Key Lock 基本消除幻读 |
| 24 | 9.3 | **补充（重点）** | 讲排它锁/共享锁与封锁 | 补三级封锁协议、**2PL 两段锁**、优先图与冲突可串行化、死锁检测与解除、意向锁/间隙锁 |
| 25 | 9.x | **补充** | 未出现 MVCC | 补 undo 版本链、隐藏列、ReadView，解释 RC 每次生成 / RR 首次生成，以及快照读 vs 当前读 |
| 26 | 10.x | **补充** | 讲 mysqldump 与日志类型 | 补 **binlog（Server 逻辑）/redo（InnoDB 物理）/undo** 三者分工、**WAL 与两阶段提交**、时间点恢复 PITR、RPO/RTO、主从复制不是备份 |
| 27 | 11.x | **补充** | 分章讲设计任务 | 补「**六阶段**」主线与各阶段输入/产出、DFD 四要素、数据字典五项内容 |
| 28 | 12.x | **补充（重点）** | 明确定义 1NF/2NF/3NF，**未出现 BCNF** | 补 **Armstrong 公理与属性闭包**、候选码求法、**BCNF 与 4NF/多值依赖**、**无损连接与保持依赖**、3NF 与 BCNF 的取舍定理 |
| 29 | 13.x | 补充 | 讲 E-R 表示与转换 | 补 1:1 / 1:n / m:n 三条转换规则、四类 E-R 冲突、弱实体与泛化、外模式设计属逻辑阶段 |
| 30 | 14.x | 补充 | 讲物理设计任务 | 补索引/聚簇/分区具体决策、分区 vs 分库分表、读写分离与主从延迟、在线 DDL 与运维监控清单 |
| 31 | 15–16 | 补充 | 详细讲存储过程/触发器/事件 | 补 MODIFIES 特征声明、游标 DECLARE 顺序与 NOT FOUND HANDLER、`NEW/OLD` 可用事件矩阵、触发器与事件对照 |
| 32 | 17.x | **补充** | 大量 Python/Java 连接示例 | 补**参数化预处理防注入、连接池、显式事务边界、资源释放、死锁重试**五项工程结论 |
| 33 | 全书 | 补充 | 以 MySQL 5.x 语法为主 | 补 MySQL 8.0 CTE/窗口函数/角色/原子 DDL/降序索引/JSON/移除查询缓存 |
| 34 | 全书 | 修正 | 课件公式多为 PPT 图片、SQL 结果零散 | 本笔记所有 SQL 例题均在关系库实际执行验证并附结果，范式、调度、恢复方案均给出可复核的完整步骤 |

## 易混概念对照表（速记）

| A | B | 关键区别 |
| --- | --- | --- |
| DB / DBMS / DBS | — | 数据集合 / 管理软件 / 含人、应用、硬件的完整系统 |
| 外模式 | 模式 | 用户局部视图（可多个） / 全局逻辑结构（唯一）；视图是外模式实现 |
| 逻辑独立性 | 物理独立性 | 由外模式/模式映像给 / 由模式/内模式映像给 |
| 概念结构设计 | 逻辑结构设计 | 独立于 DBMS（E-R） / 依赖数据模型（关系模式） |
| 候选码 | 主码 / 超码 | 最小唯一集（可多个） / 选定的一个 / 可能含多余属性 |
| 主属性 | 非主属性 | 属于任一候选码 / 其余；2NF/3NF 只管非主属性 |
| 实体完整性 | 参照完整性 | 主码非空唯一 / 外码须引用存在值或 NULL |
| 自然连接 | 等值连接 | 自动同名等值且去重列 / 保留两列、条件可任意 |
| WHERE | HAVING | 分组前行过滤（不能用聚合） / 分组后组过滤（可用聚合） |
| DELETE | TRUNCATE / DROP | DML 可回滚可带 WHERE / DDL 隐式提交、重置自增 / 连结构一起删 |
| 视图 | 基本表 / 索引 | 虚表只存定义 / 实存数据 / 实存的有序结构 |
| 聚簇索引 | 二级索引 | 叶子存整行（唯一） / 叶子存主键值、需回表 |
| 脏读 | 不可重复读 / 幻读 | 读到未提交 / 同行的值被 UPDATE 改 / 结果集行数被 INSERT/DELETE 改 |
| 一级 / 二级 / 三级封锁协议 | 2PL | 分别防丢失修改 / 加防脏读 / 加防不可重复读；2PL 保证可串行化但可能死锁 |
| X 锁 | S 锁 | 写锁，与其它全互斥 / 读锁，多 S 可共存、与 X 互斥 |
| 2NF | 3NF / BCNF | 消非主属性部分依赖 / 消传递依赖 / 所有决定因素含码 |
| 无损连接 | 保持依赖 | 能精确还原原关系 / 约束可局部检查；3NF 可兼得，BCNF 只保证无损 |
| 1:n 转换 | m:n 转换 | 并入 n 端作外码（不建表） / 必须独立建表且组合主码 |
| binlog | redo / undo | Server 逻辑、复制与 PITR / InnoDB 物理、崩溃恢复 / 回滚与 MVCC |
| 主从复制 | 备份 | 高可用与读扩展，误删会同步 / 独立副本，可恢复到过去时刻 |

## 附录 A SQL 语法与公式速查

| # | 主题 | 语法 / 公式 |
| --- | --- | --- |
| 1 | 三级模式 | 外模式（多个）— 外模式/模式映像 → 逻辑独立性；模式（唯一）— 模式/内模式映像 → 物理独立性；内模式（唯一） |
| 2 | 关系模式 | `R(U, D, DOM, F)`，简写 `R(A₁,…,Aₙ)`；关系 = 元组的有限集合 |
| 3 | 关系代数 | `σ_F(R)` 选择、`π_A(R)` 投影、`R⋈S` 连接、`R÷S` 除、`R∪S / R−S / R∩S / R×S` |
| 4 | 除运算 | `π_{Sno,Cno}(SC) ÷ π_{Cno}(Course)` = 选修全部课程的学生 |
| 5 | 建库 | `CREATE DATABASE [IF NOT EXISTS] db DEFAULT CHARACTER SET utf8mb4 [COLLATE …];` |
| 6 | 建表 | `CREATE TABLE t (col type [约束], …, [表级约束]) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;` |
| 7 | 六类约束 | `PRIMARY KEY / FOREIGN KEY … REFERENCES / UNIQUE / NOT NULL / DEFAULT / CHECK` |
| 8 | 外键动作 | `ON DELETE {RESTRICT\|CASCADE\|SET NULL\|NO ACTION}`（UPDATE 同理） |
| 9 | 改表 | `ALTER TABLE t ADD / MODIFY / CHANGE / DROP COLUMN …; RENAME TO …` |
| 10 | 插入 | `INSERT INTO t [(cols)] VALUES (…),(…);` / `INSERT INTO t SELECT …` |
| 11 | 更新删除 | `UPDATE t SET c=… WHERE …;` / `DELETE FROM t WHERE …;` / `TRUNCATE TABLE t;` |
| 12 | SELECT 书写 | `SELECT [DISTINCT] … FROM … [JOIN … ON …] [WHERE …] [GROUP BY … [HAVING …]] [ORDER BY …] [LIMIT …]` |
| 13 | SELECT 执行序 | FROM/JOIN → WHERE → GROUP BY → HAVING → SELECT → ORDER BY → LIMIT |
| 14 | 判空 | `IS NULL / IS NOT NULL`；`COALESCE(x, 默认值)` / `IFNULL` |
| 15 | 模糊匹配 | `LIKE '%串%'`，`_` 单字符，`ESCAPE` 转义；前置 `%` 无法用索引 |
| 16 | 聚合 | `COUNT(*) 计全部行`；`COUNT(col)/SUM/AVG/MAX/MIN` 忽略 NULL |
| 17 | 连接 | `INNER JOIN / LEFT JOIN / RIGHT JOIN / CROSS JOIN / 自连接（别名）` |
| 18 | 集合 | `UNION`（去重）/ `UNION ALL`（不去重）/ `INTERSECT` / `EXCEPT`（MySQL 用 JOIN/NOT EXISTS 模拟） |
| 19 | 子查询 | `IN / ANY / ALL / EXISTS / NOT EXISTS`；派生表 `FROM (SELECT …) AS t` |
| 20 | CTE | `WITH cte AS (SELECT …) SELECT * FROM cte;`；递归 `WITH RECURSIVE` |
| 21 | 窗口函数 | `ROW_NUMBER() OVER (PARTITION BY … ORDER BY …)`、`RANK / LAG / LEAD` |
| 22 | 视图 | `CREATE [OR REPLACE] VIEW v AS SELECT … [WITH CHECK OPTION];` |
| 23 | 索引 | `CREATE [UNIQUE] INDEX idx ON t(c1,c2);` / `DROP INDEX` / `SHOW INDEX` / `EXPLAIN` |
| 24 | 最左前缀 | 联合索引 `(a,b,c)` 可用 `a`、`a,b`、`a,b,c`；范围列之后不再用于定位 |
| 25 | 用户权限 | `CREATE USER 'u'@'h' IDENTIFIED BY '…';` / `GRANT privileges ON db.t TO …;` / `REVOKE` / `SHOW GRANTS` |
| 26 | 角色 | `CREATE ROLE r; GRANT … TO r; GRANT r TO 'u'@'h'; SET DEFAULT ROLE r TO 'u'@'h';` |
| 27 | 事务 | `START TRANSACTION; … SAVEPOINT sp; … COMMIT / ROLLBACK [TO sp];` |
| 28 | ACID | A↔undo log；C↔完整性约束 + A/I/D；I↔锁 + MVCC；D↔redo log + WAL |
| 29 | 隔离级别 | `READ UNCOMMITTED / READ COMMITTED / REPEATABLE READ(MySQL 默认) / SERIALIZABLE` |
| 30 | 查看隔离级别 | `SELECT @@transaction_isolation;`（MySQL 8.0；旧版 `@@tx_isolation`） |
| 31 | 显式加锁 | `SELECT … FOR UPDATE`（X）/ `LOCK IN SHARE MODE`（S，8.0 可用 `FOR SHARE`） |
| 32 | 三级封锁 | 一级：写前 X 锁至事务末（防丢失修改）；二级：+读 S 锁读完放（防脏读）；三级：+读 S 锁至末（防不可重复读） |
| 33 | 2PL | 扩展阶段只加锁、收缩阶段只放锁 ⇒ 冲突可串行化（充分非必要），不保证无死锁 |
| 34 | 备份 | `mysqldump -u root -p --single-transaction --routines --triggers --master-data=2 db > db.sql` |
| 35 | 还原 | `mysql -u root -p db < db.sql`；`SOURCE /path/db.sql;` |
| 36 | PITR | `mysqlbinlog --start-datetime=… --stop-datetime=… mysql-bin.00000N \| mysql -u root -p` |
| 37 | 日志分工 | binlog（Server/逻辑，复制+PITR）、redo（InnoDB/物理，崩溃恢复）、undo（回滚+MVCC） |
| 38 | 两阶段提交 | redo prepare → 写 binlog → redo commit；崩溃时按 binlog 是否完整决定提交或回滚 |
| 39 | 函数依赖 | `X→Y`；完全 `X→f Y`、部分 `X→p Y`、传递 `X→t Z` |
| 40 | Armstrong | A1 自反律、A2 增广律、A3 传递律；推论：合并/分解/伪传递 |
| 41 | 闭包 | `X⁺` 反复并入满足 `A⊆X⁺` 的 `A→B` 中的 B；`X⁺=U` ⇒ X 为超码 |
| 42 | 范式 | 1NF 原子值；2NF 消非主属性部分依赖；3NF 消传递依赖；BCNF 决定因素含码；4NF 消非平凡多值依赖 |
| 43 | 二元分解无损 | `R→R1,R2` 无损 ⟺ `(R1∩R2)→(R1−R2)` 或 `(R1∩R2)→(R2−R1)` 在 `F⁺` 中 |
| 44 | ER 转换 | 实体→关系；1:1 任一方加外码；1:n 在 n 端加 1 端码；m:n 独立建表（组合主码 + 联系属性） |
| 45 | 六阶段 | 需求分析 → 概念结构 → 逻辑结构 → 物理结构 → 实施 → 运行维护 |
| 46 | 存储过程 | `DELIMITER // CREATE PROCEDURE p(IN a INT, OUT b INT) BEGIN … END // DELIMITER ;` |
| 47 | 函数 | `CREATE FUNCTION f(x INT) RETURNS type DETERMINISTIC BEGIN RETURN …; END` |
| 48 | 游标 | `DECLARE cur CURSOR FOR …; DECLARE CONTINUE HANDLER FOR NOT FOUND SET done=1; OPEN/FETCH/CLOSE` |
| 49 | 触发器 | `CREATE TRIGGER trg BEFORE\|AFTER INSERT\|UPDATE\|DELETE ON t FOR EACH ROW BEGIN … NEW./OLD. … END` |
| 50 | 事件 | `SET GLOBAL event_scheduler=ON; CREATE EVENT e ON SCHEDULE EVERY 1 DAY DO …;` |
| 51 | 参数化 | Python `cur.execute("… WHERE a=%s AND b=%s",(x,y))`；Java `PreparedStatement` + `setString/setInt` |
| 52 | 例题结果 | 教学库：CS|2|19.5；李勇|92；选课数 3/2/1/1；COUNT(*)=7 / COUNT(Grade)=6；无人选修=操作系统 |

## 附录 B 易错点速查

1. DBS ≠ DB：数据库系统还包含 DBMS、应用、DBA、用户与硬件平台。
2. 文件系统阶段的根本缺陷是**数据共享性差、冗余大、数据独立性差**，不只是"速度慢"。
3. 三级模式中模式与内模式**各只有一个**，外模式可以有多个。
4. 逻辑独立性来自外模式/模式映像，物理独立性来自模式/内模式映像，别对调。
5. 视图是外模式在 SQL 中的实现，不是内模式。
6. 概念模型（E-R）**独立于**具体 DBMS；逻辑模型依赖数据模型，物理模型依赖 DBMS 与硬件。
7. 数据模型三要素是数据结构、数据操作、完整性约束，不含"数据字典"。
8. 国产数据库、NoSQL、NewSQL 属于不同分类维度，不能混为一谈。

9. 关系要求**元组不重复、分量原子**；允许重复行的"表"严格说不是关系。
10. 关系模式中列的次序与行的次序都可任意交换，不影响语义。
11. 候选码可有多个，主码只能选一个；全码指全部属性共同构成码。
12. 外码在本关系中不一定是主码，但取值必须引用被参照关系中存在的主码值或为 NULL。
13. 实体完整性只约束主码；MySQL 的 UNIQUE 列允许多个 NULL。
14. 外码违反时可选 RESTRICT/CASCADE/SET NULL，默认是拒绝。
15. 自然连接会按**同名属性**自动等值并去掉重复列；等值连接保留两列。
16. 若无同名属性却写 `R⋈S`，结果退化为笛卡尔积。
17. 投影 `π` 会去重；SQL 的 `SELECT` 默认不去重，须显式 `DISTINCT`。

18. SQL 是非过程化、面向集合的语言；一次操作作用于元组集合而非单条记录。
19. `TRUNCATE` 属于 **DDL**、隐式提交、不可回滚、重置自增值；`DELETE` 是 DML。
20. MySQL 中大多数 DDL 隐式提交，不能被事务回滚。
21. `CONCAT` 是 MySQL 方言，标准 SQL 用 `||`；`LIMIT` 也不是标准 SQL。
22. 反引号用于标识符、单引号用于字符串；双引号在默认模式下也可作字符串。

23. MySQL 的 `utf8` 是 utf8mb3，存不了 emoji；应统一 `utf8mb4`。
24. 改数据库默认字符集**不会**转换已有表/列，需 `CONVERT TO CHARACTER SET`。
25. InnoDB 支持事务、行锁、外键、崩溃恢复；MyISAM 是表锁、无事务、无外键。
26. `SHOW ENGINES` 看支持引擎，`ALTER TABLE … ENGINE=` 会锁表并重建。

27. `INT(11)` 的 11 是显示宽度，不限制取值范围。
28. 金额必须用 `DECIMAL`，`FLOAT/DOUBLE` 有二进制精度误差。
29. `TIMESTAMP` 受时区影响且有 2038 问题；`DATETIME` 与时区无关、范围更大。
30. `CHAR` 定长、`VARCHAR` 变长；MySQL 中 `VARCHAR(n)` 的 n 是字符数。
31. 组合主码要写成表级约束 `PRIMARY KEY(c1,c2)`。
32. 建表顺序：先父表后子表；删表顺序：先子表后父表。
33. MySQL 8.0.16 之前的 `CHECK` 只解析不生效，不能依赖它做校验。
34. `UPDATE/DELETE` 不带 WHERE 作用于全表，生产环境应开 `sql_safe_updates`。

35. SELECT 的书写顺序不是执行顺序；真实顺序是 FROM→WHERE→GROUP BY→HAVING→SELECT→ORDER BY→LIMIT。
36. `WHERE` 不能用聚合函数，也不能用 SELECT 中定义的别名。
37. `HAVING` 用于**组**过滤；没有 GROUP BY 时聚合函数把整个结果当一组。
38. 严格模式下 `GROUP BY` 后 SELECT 只能出现分组列或聚合表达式。
39. `NULL = NULL` 结果是 UNKNOWN；判空必须用 `IS NULL / IS NOT NULL`。
40. `COUNT(*)` 计全部行，`COUNT(col)` 跳过 NULL；`AVG/SUM` 也忽略 NULL。
41. `NOT IN` 子查询只要含一个 NULL，整个结果恒为空 → 改 `NOT EXISTS`。
42. LEFT JOIN 后统计"个数"必须用 `COUNT(右表列)`，用 `COUNT(*)` 会把补 NULL 行算进去。
43. `UNION` 去重（有排序开销），确认无重复时优先 `UNION ALL`。
44. `LIMIT` 必须配合 `ORDER BY` 才有确定的"前 N 名"；深分页用游标式 `WHERE id > last_id`。

45. 视图只存定义不存数据；查询时被"消解"为底层 SELECT。
46. 含 DISTINCT/GROUP BY/HAVING/UNION/聚合/子查询的视图通常**不可更新**。
47. `WITH CHECK OPTION` 拒绝使行不再满足视图条件的更新。
48. 索引不是虚表，它是实际占用磁盘的有序结构；不能对普通视图建索引。
49. B+树叶子层有链表，适合范围查询；HASH 索引只适合等值。
50. 联合索引遵守最左前缀；跳过最左列、前置 `%`、对索引列用函数都会失效。
51. 二级索引叶子存主键值，查非索引列需**回表**；覆盖索引可避免回表。
52. 索引越多写入越慢，低选择性列（如性别）建单列索引通常无效。

53. MySQL 身份是 `'user'@'host'`，`localhost` 与 `%` 是两个不同账号。
54. MySQL 8.0 起须先 `CREATE USER` 再 `GRANT`，旧版隐式创建用户的写法已废弃。
55. `REVOKE` 只收权限不删用户；删用户用 `DROP USER`。
56. `GRANT/CREATE USER` 自动生效，不需要 `FLUSH PRIVILEGES`。
57. 前端校验与字符串转义都不能替代**参数化查询**；动态表名须用白名单。

58. 事务四个特性缩写为 **ACID**：原子性、一致性、隔离性、持久性。
59. A 靠 undo log、D 靠 redo log、I 靠锁与 MVCC，C 是前三者共同保障的结果。
60. MySQL 默认 `autocommit=1`；单条 DML 自动提交，显式事务需 `START TRANSACTION`。
61. 脏读读到**未提交**数据；不可重复读是同行的值被改；幻读是行数变化。
62. 不可重复读针对 UPDATE，幻读针对 INSERT/DELETE；解决幻读要锁**范围**（Next-Key Lock）。
63. MySQL InnoDB 默认隔离级别是 **REPEATABLE READ**（Oracle/PostgreSQL 是 READ COMMITTED）。
64. 提高隔离级别**不能**自动解决"读-改-写"型丢失修改，仍需行锁/原子更新/乐观锁。
65. 一级封锁协议防丢失修改、二级加防脏读、三级加防不可重复读。
66. 2PL 保证冲突可串行化但**不保证无死锁**；优先图有环则调度不可串行化。
67. X 锁与任何锁互斥；多个 S 锁可共存但与 X 互斥。
68. 快照读走 MVCC 不加锁；`FOR UPDATE` 等当前读走锁。
69. RC 每条 SELECT 生成新 ReadView，RR 只在第一次普通 SELECT 生成。

70. binlog 是 Server 层逻辑日志（复制/PITR），redo 是 InnoDB 层物理日志（崩溃恢复）。
71. undo log 同时服务于事务回滚与 MVCC 版本链；MyISAM 没有 redo/undo。
72. 两阶段提交以 binlog 是否完整决定崩溃后提交或回滚，保证主从一致。
73. `TRUNCATE/DROP` 是 DDL、隐式提交，误删只能靠备份 + binlog 恢复。
74. 主从复制**不是备份**（误删会同步到从库），仍需独立备份与恢复演练。
75. RPO 看备份频率 + binlog，RTO 看备份体积与回放速度；有备份不等于能恢复。

76. 数据库设计六阶段顺序不能颠倒；数据字典在需求分析阶段建立并持续充实。
77. DFD 四要素：外部实体、处理、数据流、数据存储。
78. 「概念结构设计独立于 DBMS」「逻辑结构设计依赖数据模型」「物理设计依赖 DBMS」——三句常考。

79. 2NF 只消除**非主属性**对码的部分依赖；3NF 再消除传递依赖。
80. 全主属性的关系至少 3NF，但可能因"决定因素不含码"而不满足 BCNF。
81. BCNF 要求每个非平凡函数依赖的决定因素都含候选码；4NF 再处理多值依赖。
82. `X→Z` 为传递依赖还要求 `Y↛X`，否则是相互决定。
83. 二元分解无损判据：`(R1∩R2)→(R1−R2)` 或 `(R1∩R2)→(R2−R1)` 在 F⁺ 中。
84. 3NF 分解可同时保证无损与保持依赖；BCNF 保证无损但可能丢失依赖。
85. 范式越高并非越好：连接开销上升，读多写少的分析场景常主动反规范化。

86. 1:n 联系**不单独建表**（把 1 端码并入 n 端）；m:n 必须独立建表且用组合主码。
87. 联系自身的属性（成绩、借期）在转换时不能丢。
88. E-R 合并的四类冲突：属性、命名、结构、域/约束冲突。
89. 视图/外模式设计属于**逻辑结构设计**阶段，不属于物理设计。

90. 分区表逻辑上仍是一张表、应用无感；分库分表需要分片键与中间件。
91. 规范化到 3NF 是设计起点，实际系统常为性能有意识反规范化并维护冗余一致性。
92. 生产代码的重点不是"能连上数据库"，而是参数化防注入、连接池归还、显式事务、短事务与死锁重试。

