# Cloudflare Pages Functions 与 KV 绑定说明

本目录下的 `functions/` 为站点提供后端能力（收藏笔记、保存答题记录），
随 GitHub 推送由 Cloudflare Pages 自动部署，**无需额外构建**。

## 你只需做一步（一次性）

代码已经写好，但需要一个 KV 存储空间。请在 Cloudflare 后台完成绑定：

1. 打开 Cloudflare 控制台 → 你的 **Pages 项目** → **设置 → Functions → KV 命名空间绑定**。
2. 点击「添加绑定」：
   - 变量名称（Binding）填：**`KB_KV`**（必须与代码里的 `env.KB_KV` 完全一致）
   - 命名空间：选「创建一个新的」或已有的，命名为 `kb-kv` 即可。
3. 保存。之后每次 `git push` 部署后，接口自动可用。

## 接口

- `GET  /api/favorites` —— 取当前用户的收藏笔记 ID 列表
- `POST /api/favorites` —— 收藏/取消收藏，body：`{ "id": "welcome", "action": "add" | "remove" }`
- `GET  /api/records`   —— 取当前用户的答题记录
- `POST /api/records`   —— 保存一条记录，body：`{ "note": "C", "score": 8, "total": 10 }`

## 用户身份

站点开启了 Cloudflare Access（邮箱登录），后端会直接读取
`Cf-Access-Authenticated-User-Email` 头来确定用户，无需另做登录系统；
若关闭 Access，则回退为前端匿名 ID（存储在 localStorage）。

## 费用

Cloudflare 免费额度即可覆盖：Pages Functions 约 10 万次请求/天，
KV 每天 10 万读 / 1 千写、1GB 存储，个人站点完全够用。
