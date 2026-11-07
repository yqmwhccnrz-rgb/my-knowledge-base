# 我的知识库

基于 **VitePress** 构建的静态知识网站，通过 **GitHub** 自动部署到 **Cloudflare Pages**。

## 网站地址

🌐 https://my-knowledge-base-e0h.pages.dev/

> 站点开启了 Cloudflare Access（邮箱 + 验证码）门禁，访客需通过验证后访问。

## 功能

- **笔记**：C 语言、Python 数据分析、Matlab、税法（CPA）、会计（CPA）五篇，导航随 `docs/notes/` 目录自动生成。
- **习题测试**：1177 道选择题 / 多选题 / 判断题 / 填空题 / 代码题 / 程序设计题 / 计算分析题，可选笔记来源与题量，提交后即时判分并给出解析（计算分析题展示参考答案、不计分）。
- **英语听力**：75 段六级真题录音，按章 + 每 3 题分组，提供英文原文、中文翻译、英文题干的独立显示切换，播放时按真实句首时间逐句高亮跟读。
- **听力训练**：200 题盲听听写，共 5 个单元（短文 / 对话 / 篇章 / 讲座 / 综合），每题 50–80 词完整句子；听录音 → 打字写答案 → 逐题查看英文原文与中文翻译，并给出听写正确率与漏词。
- **可安装 App（PWA）**：支持「添加到主屏幕 / 桌面」安装为独立应用，并缓存已访问页面供离线阅读。音频体积较大且使用 Range 请求，**不进入离线缓存**。
- **收藏与答题记录（需后端）**：登录用户可收藏笔记、保存并查看答题记录（数据存于 Cloudflare KV）。

## 技术栈

- 前端：VitePress 1.x（静态站，纯前端）
- 部署：Cloudflare Pages（GitHub 推送自动部署）
- 后端：Cloudflare Pages Functions + KV（收藏 / 答题记录）

## 本地开发

```bash
npm install
npm run dev      # 本地预览 http://localhost:5173
npm run build    # 构建到 docs/.vitepress/dist
```

## 后端配置（收藏 / 答题记录）

后端已随仓库提供（`functions/`），但需要在 Cloudflare 控制台给 Pages 项目绑定一个 KV：

1. Cloudflare 控制台 → **Storage & Databases → Workers KV** → 创建一个命名空间（如 `kb-kv`）。
2. Pages 项目 → **Settings → Bindings** → 添加 KV 绑定，变量名填 **`KB_KV`**（须与代码一致）。
3. **Deployments** 重新部署一次即可生效。

接口：`GET/POST /api/favorites`（收藏）、`GET/POST /api/records`（答题记录）。
用户身份直接复用 Cloudflare Access 登录邮箱，无需另做登录系统。
