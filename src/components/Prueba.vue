<template>
    <div>
        <div ref="container">
            $$
            {{ frac(1, 2) }}
            $$
        </div>
        <div v-html="htmlContent"></div>
    </div>
</template>
<script setup lang="ts">
import { watch, ref } from "vue";
import markdownIt from 'markdown-it';
import markdownItKatex from 'markdown-it-katex';

function frac(a, b) {
    return `\\frac{${a}}{${b}}`
}

const container = ref<HTMLDivElement>(null);
const htmlContent = ref(null);

const md = markdownIt().use(markdownItKatex)

watch(container, () => {
    console.log(container.value.textContent.trim())

    htmlContent.value = md.render(container.value.textContent.trim())
})

</script>