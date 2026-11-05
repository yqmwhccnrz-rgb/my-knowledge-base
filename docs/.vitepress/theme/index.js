import DefaultTheme from 'vitepress/theme'
import { h } from 'vue'
import Quiz from './Quiz.vue'
import LogoutButton from './LogoutButton.vue'
import ColumnResizer from './ColumnResizer.vue'
import FavoriteButton from './FavoriteButton.vue'
import InstallApp from './InstallApp.vue'
import './custom.css'

export default {
  extends: DefaultTheme,
  enhanceApp({ app }) {
    app.component('Quiz', Quiz)
    app.component('FavoriteButton', FavoriteButton)
    app.component('InstallApp', InstallApp)
  },
  Layout: () => h(DefaultTheme.Layout, null, {
    'doc-top': () => h(FavoriteButton),
    // 右上角导航区：在「首页/笔记/习题测试」右侧加「安装 App」入口
    'nav-bar-content-after': () => h(InstallApp),
    // 手机端：放进展开菜单的底部
    'nav-screen-content-after': () => h(InstallApp),
    'layout-bottom': () => [h(LogoutButton), h(ColumnResizer)]
  })
}
