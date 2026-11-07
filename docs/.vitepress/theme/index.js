import DefaultTheme from 'vitepress/theme'
import { h } from 'vue'
import Quiz from './Quiz.vue'
import Listening from './Listening.vue'
import Dictation from './Dictation.vue'
import LogoutButton from './LogoutButton.vue'
import LayoutFix from './LayoutFix.vue'
import ColumnResizer from './ColumnResizer.vue'
import FavoriteButton from './FavoriteButton.vue'
import InstallApp from './InstallApp.vue'
import Favorites from './Favorites.vue'
import './custom.css'

export default {
  extends: DefaultTheme,
  enhanceApp({ app }) {
    app.component('Quiz', Quiz)
    app.component('Listening', Listening)
    app.component('Dictation', Dictation)
    app.component('FavoriteButton', FavoriteButton)
    app.component('InstallApp', InstallApp)
    app.component('Favorites', Favorites)
  },
  Layout: () => h(DefaultTheme.Layout, null, {
    'doc-top': () => h(FavoriteButton),
    // 左侧边栏顶部：收藏夹（VitePress 侧边栏槽位名为 sidebar-nav-before）
    'sidebar-nav-before': () => h(Favorites),
    // 右上角导航区：在「首页/笔记/习题测试」右侧加「安装 App」入口
    'nav-bar-content-after': () => h(InstallApp),
    // 手机端：放进展开菜单的底部
    'nav-screen-content-after': () => h(InstallApp),
    // 两根分隔条：分别拖拽一级目录与二级目录宽度
    'layout-bottom': () => [h(LogoutButton), h(LayoutFix), h(ColumnResizer)]
  })
}
