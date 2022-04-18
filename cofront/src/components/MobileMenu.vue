<template>
  <n-space align="center" justify="space-between">
    <Icon @click="show = true" :size="burgerSize" style="margin-right: 24px">
      <Menu2 />
    </Icon>
    <n-modal v-model:show="show" style="width: 80vw" :auto-focus="false">
      <n-card title="Меню">
        <n-scrollbar style="max-height: 60vh">
          <n-space vertical>
            <n-button
              v-for="path in paths"
              :key="path.key"
              class="burger-buttons"
              quaternary
              type="primary"
              size="large"
              tag="a"
              @click.prevent="routeTo(path.to)"
            >
              {{ path.label }}
            </n-button>
          </n-space>
          <HeaderAuth @click="show = false" />
        </n-scrollbar>
      </n-card>
    </n-modal>
    <n-space align="center" justify="end">
      <Icon class="second-buttons" @click="$emit('switchTheme')" size="24">
        <DarkTheme24Regular />
      </Icon>
      <Icon class="second-buttons" @click="$emit('showSearch')" size="24">
        <Search32Filled />
      </Icon>
    </n-space>
  </n-space>
</template>

<script>
import Menu2 from "@vicons/tabler/Menu2";
import Search32Filled from "@vicons/fluent/Search32Filled";
import DarkTheme24Regular from "@vicons/fluent/DarkTheme24Regular";
import Icon from "@/components/Icon";
import HeaderAuth from "@/components/HeaderAuth";

export default {
  name: "MobileMenu",
  components: {
    Menu2,
    Search32Filled,
    DarkTheme24Regular,
    Icon,
    HeaderAuth,
  },
  props: {
    paths: { type: Array, default: () => [] },
    burgerSize: { type: [String, Number], default: 32 },
  },
  data() {
    return {
      user: this.$store.getters.user,
      logged: false,
      show: false,
    };
  },
  methods: {
    routeTo(path) {
      this.show = false;
      this.$router.push(path);
    },
  },
};
</script>

<style scoped>
.second-buttons {
  margin-right: 16px;
}
</style>
