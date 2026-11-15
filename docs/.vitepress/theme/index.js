import DefaultTheme from 'vitepress/theme'
import { h } from 'vue'
import { useData } from 'vitepress'
import Quiz from './Quiz.vue'
import Listening from './Listening.vue'
import Dictation from './Dictation.vue'
import Reading from './Reading.vue'
import LogoutButton from './LogoutButton.vue'
import LayoutFix from './LayoutFix.vue'
import ColumnResizer from './ColumnResizer.vue'
import OutlineToggle from './OutlineToggle.vue'
import FavoriteButton from './FavoriteButton.vue'
import ExportPdf from './ExportPdf.vue'
import InstallApp from './InstallApp.vue'
import Favorites from './Favorites.vue'
import HomeNotes from './HomeNotes.vue'
import './custom.css'

export default {
  extends: DefaultTheme,
  enhanceApp({ app }) {
    app.component('Quiz', Quiz)
    app.component('Listening', Listening)
    app.component('Dictation', Dictation)
    app.component('Reading', Reading)
    app.component('FavoriteButton', FavoriteButton)
    app.component('InstallApp', InstallApp)
    app.component('Favorites', Favorites)
  },
  Layout: () => {
    const { frontmatter } = useData()
    return h(DefaultTheme.Layout, null, {
      // 首页笔记区：默认网格（features）留空不渲染，这里用左右滑动轮播替换，
      // 一次显示一张，支持触摸滑动 / 箭头 / 圆点切换
      'home-features-after': () => {
        const cards = frontmatter.value?.noteCards
        if (cards && cards.length) return h(HomeNotes, { cards })
        return null
      },
      // 收藏与导出共用一个 flex 行，保证两个按钮高度、基线、间距完全一致
      'doc-top': () => h('div', { class: 'kb-doc-actions' }, [h(FavoriteButton), h(ExportPdf)]),
      // 左侧边栏顶部：收藏夹（VitePress 侧边栏槽位名为 sidebar-nav-before）
      'sidebar-nav-before': () => h(Favorites),
      // 右上角导航区：在「首页/笔记/习题测试」右侧加「安装 App」入口
      'nav-bar-content-after': () => h(InstallApp),
      // 手机端：放进展开菜单的底部
      'nav-screen-content-after': () => h(InstallApp),
      // 两根分隔条：分别拖拽一级目录与二级目录宽度
      'layout-bottom': () => [h(LogoutButton), h(LayoutFix), h(ColumnResizer), h(OutlineToggle)]
    })
  }
}
