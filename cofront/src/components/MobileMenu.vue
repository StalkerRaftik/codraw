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
          <n-divider
            title-placement="left"
            style="margin-top: 18px; margin-bottom: 18px"
          >
            Авторизация
          </n-divider>
          <n-space v-if="!logged" vertical>
            <n-button
              class="burger-buttons"
              quaternary
              size="large"
              type="info"
              href="#"
              tag="a"
              @click.prevent="routeTo('/login')"
              >Войти</n-button
            >
            <n-button
              class="burger-buttons"
              quaternary
              size="large"
              type="info"
              href="#"
              tag="a"
              @click.prevent="routeTo('/registration')"
              >Регистрация</n-button
            >
          </n-space>
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

export default {
  name: "MobileMenu",
  components: {
    Menu2,
    Search32Filled,
    DarkTheme24Regular,
    Icon,
  },
  props: {
    paths: { type: Array, default: () => [] },
    burgerSize: { type: [String, Number], default: 32 },
  },
  data() {
    return {
      logged: false,
      show: false,
    };
  },
  methods: {
    routeTo(path) {
      this.show = false;
      this.$router.push({ path });
    },
  },
};
</script>

<style scoped>
.second-buttons {
  margin-right: 16px;
}

.burger-buttons {
  width: 100%;
  display: flex;
  color: inherit;
  justify-content: left;
}
</style>
