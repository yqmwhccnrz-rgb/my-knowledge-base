# 我的知识库

一个面向学习、备考与日常查阅的个人知识网站，使用 **VitePress** 构建静态页面，通过 **GitHub + Cloudflare Pages** 自动部署。网站支持课程笔记、随机习题、英语练习、听力训练、收藏、答题记录和 PDF 导出。

## 在线访问

- 网站：<https://my-knowledge-base-e0h.pages.dev/>
- 仓库：<https://github.com/yqmwhccnrz-rgb/my-knowledge-base>

站点开启了 **Cloudflare Access** 邮箱门禁，访客需要通过邮箱验证后访问。

## 内容规模

当前仓库包含：

- **26 篇笔记页面**：25 篇课程笔记 + 1 篇全站学习地图
- **4220 道习题**：覆盖 25 个科目、6 种题型
- **75 段英语听力材料**
- **200 条听写训练**
- **5 类英语练习**
- **226 张课程插图**

## 主要功能

### 课程笔记与学习地图

笔记覆盖以下学科：

| 分类 | 科目 |
| --- | --- |
| 公共基础 | 高等数学、微观经济学、宏观经济学、计量经济学、利息理论 |
| CPA | 会计、审计、税法、经济法、财务成本管理、公司战略与风险管理 |
| 金融 | 金融学、证券投资学 |
| 计算机基础 | C 语言、Java、Python、MATLAB、数据结构、计算机组成原理、操作系统、计算机网络、数据库 |
| 数据科学 | 数据挖掘、机器学习、机器学习理论 |

笔记页面支持：

- VitePress 自动生成侧边栏与页面目录
- 全站本地搜索
- KaTeX 数学公式渲染
- 代码高亮、表格、提示框与例题卡片
- 桌面端和移动端响应式排版
- 收藏笔记
- 将当前笔记导出为 PDF

[全站学习地图](docs/notes/study-map.md) 按 CPA、408、经济金融、数据科学四条路线组织先修关系、跨科概念、符号口径和计算题索引。

### 习题测试

- 从 25 个科目中选择题源与题量，随机抽题
- 支持单选、多选、判断、填空、程序设计和计算分析
- 提交后即时判分并展示解析
- 填空题支持多个可接受答案
- 程序设计题支持拆空填写
- 计算分析题展示参考答案，不计入得分
- 登录用户可保存和查看答题记录

### 英语练习

包含五种模式：

- 词组填空
- 词组短语背诵
- 短篇阅读
- 写作练习
- 翻译练习

支持 CET-4 / CET-6 难度切换。写作和翻译提供思路提纲、关键词组提示及参考范文/译文。

### 听力与听写

- 英语听力：75 段材料，按章节与片段筛选，支持原文、翻译和题干切换，播放时逐句高亮
- 听力训练：200 条盲听听写，听录音后输入答案，可逐题核对原文、翻译、正确率和漏词

### 应用与个性化

- **PWA**：可安装到桌面或手机主屏幕，缓存已访问页面供离线阅读
- **收藏夹**：登录用户可收藏常用笔记
- **答题记录**：保存每次练习成绩
- **PDF 导出**：通过浏览器打印功能将笔记另存为 PDF
- **可调侧栏**：支持拖拽调整目录宽度

## 技术栈

| 层级 | 技术 |
| --- | --- |
| 静态站点 | VitePress 1.x |
| 页面组件 | Vue 3 |
| 数学公式 | markdown-it-katex + KaTeX |
| 样式 | 自定义 CSS，移动端响应式布局 |
| 部署 | Cloudflare Pages |
| 后端 | Cloudflare Pages Functions |
| 数据存储 | Cloudflare KV |
| 访问控制 | Cloudflare Access |
| 离线能力 | Service Worker + PWA |

## 本地开发

要求安装 Node.js 与 npm。

```bash
npm install
npm run dev
```

开发服务器默认运行在 <http://localhost:5173>。

构建与本地预览：

```bash
npm run build
npm run preview
```

构建产物位于 `docs/.vitepress/dist/`，预览服务器默认运行在 <http://localhost:4173>。

其他脚本：

```bash
npm run sync       # 检查 docs/public 下的 PDF 与图片资源
npm run formulas   # 可选的公式图片渲染脚本
```

> 本地 `vitepress preview` 只提供静态页面，不运行 Cloudflare Pages Functions，因此 `/api/favorites` 和 `/api/records` 在本地预览中返回 404 属于预期现象。

## 自动部署

仓库连接 Cloudflare Pages，推送到 GitHub 后会触发自动构建和部署。

部署流程：

1. GitHub 接收 `main` 分支更新
2. Cloudflare Pages 执行 `npm run build`
3. 生成 `docs/.vitepress/dist/`
4. 发布到 <https://my-knowledge-base-e0h.pages.dev/>

## 收藏与答题记录

后端代码位于 `functions/`，使用 Cloudflare Pages Functions 和 KV。

首次部署需要在 Cloudflare 控制台完成一次 KV 绑定：

1. 创建 KV 命名空间，例如 `kb-kv`
2. 进入 Pages 项目的 **Settings → Bindings**
3. 添加 KV 绑定，变量名填写 `KB_KV`
4. 重新部署项目

接口：

| 方法 | 路径 | 用途 |
| --- | --- | --- |
| GET / POST | `/api/favorites` | 获取或修改收藏 |
| GET / POST | `/api/records` | 获取或保存答题记录 |

用户身份优先读取 Cloudflare Access 的登录邮箱；未启用 Access 时回退到前端匿名访客 ID。

## 目录结构

```text
my-knowledge-base/
├── docs/
│   ├── notes/                  # 课程笔记与学习地图
│   ├── public/
│   │   ├── data/               # 习题、听力、听写和英语练习数据
│   │   ├── formulas/           # 公式图片资源
│   │   ├── math/ 等学科目录     # 课程插图
│   │   ├── listening/          # 听力音频
│   │   ├── dictation/          # 听写音频
│   │   ├── sw.js               # Service Worker
│   │   └── manifest.webmanifest
│   └── .vitepress/
│       ├── config.mjs          # 导航、侧栏、搜索和页面元信息
│       └── theme/              # Vue 组件、收藏接口和自定义样式
├── functions/                  # Cloudflare Pages Functions
├── scripts/
│   ├── notes_source/           # 笔记镜像源，供维护脚本使用
│   ├── sync-originals.mjs
│   └── render_formulas.py
├── package.json
└── README.md
```

## 内容维护

- 常规笔记维护直接编辑 `docs/notes/*.md`
- 新增笔记后，首页卡片和侧边栏会根据目录自动更新
- `scripts/notes_source/` 是笔记镜像源；运行公式渲染或内容维护脚本时，注意与 `docs/notes/` 保持同步
- 习题数据位于 `docs/public/data/questions.json`
- 听力和听写数据分别位于 `listening.json`、`dictation.json`
- 英语练习数据位于 `reading.json`
- 课程插图放在 `docs/public/` 下对应学科目录

### 内容规范

- 数学公式统一使用 KaTeX 的 `$...$` 或 `$$...$$`
- 代码、API、命令和 SQL 使用代码格式
- 同一知识点块内保持一致的排版和符号口径
- 新增内容应补充到对应章节，不随意重排已有结构
- CPA 原始教材、讲义、习题答案和文本提取件不得上传到本仓库

## 本地检查

```bash
npm run build
npm run preview
```

构建完成后，建议检查：

- 首页与学习地图导航
- 笔记目录和搜索
- 数学公式与表格
- 习题提交与解析
- 移动端布局
- PDF 导出与收藏入口
