<template>
  <div id="example" v-html="example"></div>
</template>
<script setup lang="ts">
import example from "../example.md";
const props = defineProps({
  msg: String,
});
</script>