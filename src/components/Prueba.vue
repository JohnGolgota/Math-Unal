<template>
    <div>
        <div ref="container">
            <h1>asd</h1>
            $$
            {{ frac(1, 2) }}
            {{ frac(3,4) }}
            {{ frac(3,4) }}
            {{ frac(3,4) }}
            {{ frac(3,4) }}
            $$
        </div>
        <div v-html="htmlContent"></div>
    </div>
</template>
<script setup>
import { watch, ref, onMounted } from "vue";
import markdownIt from 'markdown-it';
import markdownItKatex from 'markdown-it-katex';

function frac(a, b) {
    return `\\frac{${a}}{${b}}`
}

const container = ref(null);
const htmlContent = ref(null);

const md = markdownIt({
    html: true
}).use(markdownItKatex)
onMounted(() => {
    console.log(container.value.innerHTML)
    htmlContent.value = md.render(container.value.textContent)
})
</script>