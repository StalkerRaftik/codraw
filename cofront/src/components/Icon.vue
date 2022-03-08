<template>
  <n-icon
    class="icon"
    :style="{ cursor: clickable ? 'pointer' : 'default' }"
    :size="size"
  >
    <slot></slot>
  </n-icon>
</template>

<script>
// Just flex-centerized icon
export default {
  name: "Icon",
  props: {
    size: { type: [Number, String], default: 24 },
  },
  computed: {
    clickable() {
      return !!this?.$attrs?.onClick;
    },
  },
};
</script>

<style scoped>
.icon {
  display: flex;
  align-items: center;
  flex-direction: column;
  cursor: auto;
}
</style>
