<template>
  <PageInputTemplate
    ref="templateRef"
    title="Создать новый аккаунт"
    button-title="Зарегистрироваться"
    :form-data="formData"
    :rules="rules"
    :ui-data="uiData"
    :disabled="disabled"
    @validated="register"
  />
</template>

<script>
import PageInputTemplate from "@/components/PageInputTemplate";
import { client } from "@/axios";
import $t from "@/i18n";
import { parseResponseException } from "@/utils";
import { useNotification } from "naive-ui";

export default {
  name: "Registration",
  components: {
    PageInputTemplate,
  },
  data() {
    return {
      disabled: false,
      notification: useNotification(),
      formData: {
        username: "",
        password: "",
        passwordRepeat: "",
        email: "",
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
        passwordRepeat: {
          placeholder: "Повторите пароль",
          label: "Пароль(еще раз)",
          type: "password",
        },
        email: {
          placeholder: "example@mail.com",
          label: "Почтовый адрес",
          type: "email",
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
        passwordRepeat: [
          {
            validator: (rule, value) => {
              const data = this.$refs.templateRef.mutableFormData;
              if (value === "") {
                return new Error("Это поле необходимо заполнить");
              }
              if (value !== data.password) {
                return new Error("Пароли не совпадают!");
              }
            },
            required: true,
          },
        ],
        email: [
          {
            required: true,
            message: "Это поле необходимо заполнить",
          },
        ],
      },
    };
  },
  methods: {
    $t,
    async register(data) {
      this.disabled = true;
      const postData = { ...data };
      delete postData["passwordRepeat"];
      try {
        const results = await client.post("/user/signup/", postData);
        this.$store.commit("setAuthToken", results.data.token);
        await this.$store.dispatch("fetchUserData");
        await this.$router.push("/");
      } catch (e) {
        this.notification.error({
          title: "Регистрация завершилась неудачно!",
          content: parseResponseException(e),
          duration: 10 * 1000,
        });
      } finally {
        this.disabled = false;
      }
    },
  },
};
</script>

<style scoped></style>
