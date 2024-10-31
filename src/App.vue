<script setup lang="ts">
import MathBlockRender from "./components/MathBlockRender.vue";
const msg = "Euler's identity $e^{i\\pi}+1=0$ is a beautiful formula in $\\mathbb{R}^2$.";
</script>

<template>
  <MathBlockRender :msg="msg" />
</template>
