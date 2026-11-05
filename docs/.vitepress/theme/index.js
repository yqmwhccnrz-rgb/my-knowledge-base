import DefaultTheme from 'vitepress/theme'
import Quiz from './Quiz.vue'
import OriginalLink from './OriginalLink.vue'
import './custom.css'

export default {
  extends: DefaultTheme,
  enhanceApp({ app }) {
    app.component('Quiz', Quiz)
    app.component('OriginalLink', OriginalLink)
  }
}
