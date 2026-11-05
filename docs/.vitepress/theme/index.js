import DefaultTheme from 'vitepress/theme'
import { h } from 'vue'
import Gate from './Gate.vue'
import Quiz from './Quiz.vue'
import OriginalLink from './OriginalLink.vue'
import './custom.css'

export default {
  extends: DefaultTheme,
  enhanceApp({ app }) {
    app.component('Quiz', Quiz)
    app.component('OriginalLink', OriginalLink)
  },
  Layout: () => h(Gate, null, { default: () => h(DefaultTheme.Layout) })
}
