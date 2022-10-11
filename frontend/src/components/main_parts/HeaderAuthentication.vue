<template>
  <div>
    <div v-if="$bp.md.matches">
      <n-dropdown v-if="user" :options="options">
        <n-button text type="primary" size="large">{{
          user.username
        }}</n-button>
      </n-dropdown>
      <div v-else>
        <n-button
          v-for="option in options"
          :key="option.key"
          quaternary
          style="margin-right: 8px"
          @click="option.props.onClick"
          >{{ option.label }}
        </n-button>
      </div>
    </div>
    <n-space v-else vertical>
      <n-divider
        title-placement="left"
        style="margin-top: 18px; margin-bottom: 18px"
      >
        {{ user ? user.username : "Авторизация" }}
      </n-divider>
      <n-button
        v-for="option in options"
        :key="option.key"
        class="burger-buttons"
        quaternary
        size="large"
        type="info"
        href="#"
        tag="a"
        @click.prevent="option.props.onClick"
      >
        {{ option.label }}
      </n-button>
    </n-space>
  </div>
</template>

<script>
import { h } from "vue";
import { NIcon } from "naive-ui";
import {
  PersonCircleOutline as UserIcon,
  LogOutOutline as LogoutIcon,
} from "@vicons/ionicons5";

// TODO: Profile deletion

const renderIcon = (icon) => {
  return () => {
    console.log(
      h(NIcon, null, {
        default: () => h(icon),
      })
    );
    return h(NIcon, null, {
      default: () => h(icon),
    });
  };
};

export default {
  name: "HeaderAuth",
  data() {
    return {
      optionsLogged: [
        {
          label: "Профиль",
          key: "profile",
          icon: renderIcon(UserIcon),
          props: {
            onClick: () => {
              this.$router.push("/me");
            },
          },
        },
        {
          label: "Выйти",
          key: "logout",
          icon: renderIcon(LogoutIcon),
          props: {
            onClick: () => {
              this.$store.dispatch("logout");
              this.$router.push("/");
            },
          },
        },
      ],
      optionsNotLogged: [
        {
          label: "Войти",
          key: "login",
          props: {
            onClick: () => {
              this.$router.push("/login");
            },
          },
        },
        {
          label: "Регистрация",
          key: "registration",
          props: {
            onClick: () => {
              this.$router.push("/registration");
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
    options() {
      return this.user ? this.optionsLogged : this.optionsNotLogged;
    },
  },
};
</script>

<style scoped></style>
