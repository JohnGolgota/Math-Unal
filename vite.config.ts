import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import markdownIt from 'markdown-it';
import markdownItKatex from 'markdown-it-katex';

// https://vite.dev/config/
export default defineConfig({
  plugins: [vue(),{
    name: 'markdown-plugin',
    transform(code, id) {
      if (id.endsWith('.md')) {
        const md = markdownIt()
          .use(markdownItKatex)
        const htmlContent = md.render(code)
        return `export default ${JSON.stringify(htmlContent)}`
      }
    },
  }],
})
