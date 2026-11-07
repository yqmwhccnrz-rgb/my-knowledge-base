// 公开配置端点：仅当同时配置了 TURNSTILE_SITEKEY 与 TURNSTILE_SECRET 时才返回 sitekey，
// 保证"前端显示 widget"与"后端强制校验"状态一致（要么都开，要么都关）。
import { json } from '../../_helpers.js'

export async function onRequest(context) {
  const { env } = context
  const sitekey =
    env.TURNSTILE_SITEKEY && env.TURNSTILE_SECRET ? env.TURNSTILE_SITEKEY : ''
  return json({ turnstileSitekey: sitekey })
}
