import DefaultTheme from 'vitepress/theme'
import { h } from 'vue'
import Quiz from './Quiz.vue'
import LogoutButton from './LogoutButton.vue'
import ColumnResizer from './ColumnResizer.vue'
import FavoriteButton from './FavoriteButton.vue'
import './custom.css'

export default {
  extends: DefaultTheme,
  enhanceApp({ app }) {
    app.component('Quiz', Quiz)
    app.component('FavoriteButton', FavoriteButton)
  },
  Layout: () => h(DefaultTheme.Layout, null, {
    'doc-top': () => h(FavoriteButton),
    'layout-bottom': () => [h(LogoutButton), h(ColumnResizer)]
  })
}
