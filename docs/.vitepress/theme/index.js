import DefaultTheme from 'vitepress/theme'
import { h } from 'vue'
import Quiz from './Quiz.vue'
import LogoutButton from './LogoutButton.vue'
import './custom.css'

export default {
  extends: DefaultTheme,
  enhanceApp({ app }) {
    app.component('Quiz', Quiz)
  },
  Layout: () => h(DefaultTheme.Layout, null, {
    'layout-bottom': () => h(LogoutButton)
  })
}
