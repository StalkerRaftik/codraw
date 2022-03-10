<template>
  <RegistrationTemplate
    title="Вход в аккаунт"
    button-title="Войти"
    :form-data="formData"
    :rules="rules"
    :ui-data="uiData"
    :disabled="disabled"
    @validated="login"
  />
</template>

<script>
import RegistrationTemplate from "@/components/PageInputTemplate";
import { client } from "@/axios";
import { useNotification } from "naive-ui";

export default {
  name: "Login",
  components: {
    RegistrationTemplate,
  },
  data() {
    return {
      disabled: false,
      notification: useNotification(),
      formData: {
        username: "",
        password: "",
      },
      uiData: {
        username: {
          placeholder: "Введите логин",
          label: "Логин",
          type: "text",
        },
        password: {
          placeholder: "Введите пароль",
          label: "Пароль",
          type: "password",
        },
      },
      rules: {
        username: [
          {
            required: true,
            message: "Это поле необходимо заполнить",
          },
        ],
        password: [
          {
            required: true,
            message: "Это поле необходимо заполнить",
          },
        ],
      },
    };
  },
  methods: {
    async login(postData) {
      this.disabled = true;
      try {
        const results = await client.post("/user/login/", postData);
        this.$store.commit("setAuthToken", results.data.token);
        await this.$store.dispatch("fetchUserData");
        await this.$router.push("/");
      } catch (e) {
        this.notification.error({
          title: "Неверно указан логин или пароль!",
          duration: 3000,
        });
      }
      this.disabled = false;
    },
  },
};
</script>

<style scoped></style>
