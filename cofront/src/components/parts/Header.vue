<template>
  <n-card class="header" :bordered="false">
    <n-input
      v-if="bp.lg.matches"
      class="search"
      type="text"
      size="large"
      placeholder="Поиск аниме"
    />
    <n-modal v-model:show="showSearchModal">
      <n-card class="modal-search">
        <n-input type="text" size="large" placeholder="Поиск аниме" />
      </n-card>
    </n-modal>

    <MobileMenu
      v-if="bp.xs.matches"
      :paths="paths"
      @showSearch="showSearch"
      @switchTheme="switchTheme"
    />
    <n-space v-else justify="space-between" align="center">
      <n-space align="center">
        <div class="Navigation">
          <router-link
            v-for="path in paths"
            :to="path.to"
            :key="path.key"
          >
            <n-button class="nav-btn" quaternary size="large" tag="a">
              {{ path.label }}
            </n-button>
          </router-link>
        </div>
        <Icon v-if="bp.md.matches" @click="showSearch" size="24">
          <Search32Filled />
        </Icon>
      </n-space>
      <n-space justify="end" align="center">
        <Icon @click="switchTheme" size="24" style="margin-right: 8px">
          <DarkTheme24Regular />
        </Icon>
        <div v-if="!logged">
          <router-link to="/login">
            <n-button quaternary style="margin-right: 8px"
              >Войти
            </n-button></router-link
          >
          <router-link to="/registration"
            ><n-button quaternary>Регистрация </n-button></router-link
          >
        </div>
      </n-space>
    </n-space>
  </n-card>
</template>

<script>
import Search32Filled from "@vicons/fluent/Search32Filled";
import DarkTheme24Regular from "@vicons/fluent/DarkTheme24Regular";

import useBreakpoints from "vue-next-breakpoints";
import MobileMenu from "@/components/MobileMenu";
import Icon from "@/components/Icon";

export default {
  name: "Header",
  setup() {
    const bp = useBreakpoints({
      xs: 550,
      md: 1200,
      lg: [1201],
    });
    return { bp };
  },
  components: {
    Search32Filled,
    DarkTheme24Regular,
    Icon,
    MobileMenu,
  },
  data() {
    return {
      showSearchModal: false,
      logged: false,
      paths: [
        {
          key: "main_menu",
          label: "Главная",
          selected: false,
          to: "/",
        },
        {
          key: "anime_list",
          label: "Аниме",
          selected: false,
          to: "/",
        },
        {
          key: "forum",
          label: "Форум",
          selected: false,
          to: "/",
        },
      ],
    };
  },
  methods: {
    switchTheme() {
      this.$store.dispatch("switchTheme");
    },
    showSearch() {
      this.showSearchModal = true;
    },
  },
};
</script>

<style scoped>
.header {
  border-radius: 0;
  border-bottom-width: 0px;
}

.Navigation {
  margin-left: 2vw;
}

.nav-btn {
  margin-right: 8px;
  font-size: 20px;
}

.search {
  position: absolute;
  left: calc(50% - 15vw);
  width: 30vw;
}

.modal-search {
  width: 80vw;
  border-radius: 15px;
}
</style>
