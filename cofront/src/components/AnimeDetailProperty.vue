<template>
  <n-space class="property-wrapper" :size="[0,0]">
    <n-text depth="3" style="margin-right: 4px">
      {{ propertyName }}:
    </n-text>
    <slot/>
  </n-space>
</template>

<script>
export default {
  name: "AnimeDetailProperty",
  props: {
    propertyName: {type: String, required: true},
  },
}
</script>

<style scoped>
.property-wrapper {
  font-size: 16px !important;
}
</style>