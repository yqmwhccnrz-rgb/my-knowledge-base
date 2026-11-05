# PDF 与图片原文示例

这一页演示「保留原文」这件事在网站里长什么样：PDF 不转换成网页，而是原样提供在线预览和下载；图片按原文件展示。

## PDF 原件在线预览

下面的框里就是仓库中那个 PDF 文件本身，浏览器会用它自带的阅读器打开，翻页、缩放、搜索都可以用。

<iframe src="/files/sample.pdf" style="width:100%;height:520px;border:1px solid var(--vp-c-divider);border-radius:8px"></iframe>

如果内嵌预览在你的浏览器里不显示，也可以直接 [在新窗口打开 PDF](/files/sample.pdf) 或 [下载 PDF 原件](/files/sample.pdf)。

## 图片原件

图片不做二次加工，按原文件渲染：

![示意图](/images/sample-diagram.svg)

## 以后怎么放自己的文件

- PDF 放进 `docs/public/files/`，在文章里写一个链接或内嵌框即可
- 图片放进 `docs/public/images/`，用 Markdown 图片语法引用
- Markdown 原文由构建前的同步脚本自动复制到 `docs/public/originals/`，每篇文章底部会自动出现「查看原文 / 下载原文」

<OriginalLink />
