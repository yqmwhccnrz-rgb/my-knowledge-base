import DefaultTheme from 'vitepress/theme'
import { h } from 'vue'
import Quiz from './Quiz.vue'
import OriginalLink from './OriginalLink.vue'
import LogoutButton from './LogoutButton.vue'
import './custom.css'

export default {
  extends: DefaultTheme,
  enhanceApp({ app }) {
    app.component('Quiz', Quiz)
    app.component('OriginalLink', OriginalLink)
  },
  Layout: () => h(DefaultTheme.Layout, null, {
    'layout-bottom': () => h(LogoutButton)
  })
}
