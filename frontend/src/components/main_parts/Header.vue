<template>
  <n-card class="header" :bordered="false">
    <n-input
        v-if="$bp.md.matches"
        class="search"
        type="search"
        size="large"
        :style="$bp.lg.matches ? {width: '30vw',  left: 'calc(50% - 15vw)'}  : {width: '24vw',  left: 'calc(50% - 12vw)' }"
        placeholder="Поиск аниме"
    />
    <n-modal v-model:show="showSearchModal">
      <n-card class="modal-search">
        <n-input type="search" :size="large" placeholder="Поиск аниме"/>
      </n-card>
    </n-modal>

    <MobileMenu
        v-if="!$bp.md.matches"
        :paths="paths"
        @showSearch="showSearch"
        @switchTheme="switchTheme"
    />
    <n-space v-else justify="space-between" align="center">
      <n-space align="center">
        <div class="Navigation">
          <router-link v-for="path in paths" :to="path.to" :key="path.key">
            <n-button class="nav-btn" quaternary size="large" tag="a">
              {{ path.label }}
            </n-button>
          </router-link>
        </div>
        <Icon v-if="!$bp.md.matches" @click="showSearch" size="24">
          <SearchIcon/>
        </Icon>
      </n-space>
      <n-space justify="end" align="center">
        <Icon @click="switchTheme" size="24" style="margin-right: 8px">
          <ChangeThemeIcon/>
        </Icon>
        <HeaderAuth style="margin-right: 8px"/>
      </n-space>
    </n-space>
  </n-card>
</template>

<script>
import {Search32Filled as SearchIcon} from "@vicons/fluent";
import {DarkTheme24Regular as ChangeThemeIcon} from "@vicons/fluent";
import HeaderAuth from "@/components/main_parts/HeaderAuthentication";
import MobileMenu from "@/components/main_parts/MobileHeader";
import Icon from "@/components/Icon";

export default {
  name: "Header",
  components: {
    SearchIcon,
    ChangeThemeIcon,
    Icon,
    MobileMenu,
    HeaderAuth,
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
          to: {name: "AnimeList", query: {page: 1}},
        },
        // {
        //   key: "forum",
        //   label: "Форум",
        //   selected: false,
        //   to: "/",
        // },
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
  border-bottom-width: 0;
  box-shadow: 0 1px 1px rgba(0, 0, 0, 0.3);
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
}

.modal-search {
  width: 80vw;
  border-radius: 15px;
}
</style>
