<template>
  <div>
    <n-dropdown v-if="user" :options="options">
      <n-button text type="primary" size="large">{{ user.username }}</n-button>
    </n-dropdown>
    <div v-else>
      <router-link to="/login">
        <n-button quaternary style="margin-right: 8px"
          >Войти
        </n-button></router-link
      >
      <router-link to="/registration"
        ><n-button quaternary>Регистрация </n-button></router-link
      >
    </div>
  </div>
</template>

<script>
import { h } from "vue";
import { NIcon } from "naive-ui";
import {
  PersonCircleOutline as UserIcon,
  LogOutOutline as LogoutIcon,
} from "@vicons/ionicons5";

const renderIcon = (icon) => {
  return () => {
    return h(NIcon, null, {
      default: () => h(icon),
    });
  };
};

export default {
  name: "HeaderAuth",
  data() {
    return {
      options: [
        {
          label: "Профиль",
          key: "profile",
          icon: renderIcon(UserIcon),
          props: {
            onClick: () => {
              // TODO
              // ALSO TODO MOBILE PROFILE LOGO
            },
          },
        },
        {
          label: "Выйти",
          key: "logout",
          icon: renderIcon(LogoutIcon),
          props: {
            onClick: () => {
              this.$store.commit("setAuthToken", "");
              this.$router.go(this.$router.currentRoute);
            },
          },
        },
      ],
    };
  },
  computed: {
    user() {
      return this.$store.getters.user;
    },
  },
};
</script>

<style scoped></style>
