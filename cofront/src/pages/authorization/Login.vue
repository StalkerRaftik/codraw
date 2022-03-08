<template>
  <n-form ref="formRef" inline :label-width="80" :model="formValue">
    <n-form-item label="Логин" path="login">
      <n-input v-model:value="formValue.login" placeholder="Введите логин" />
    </n-form-item>
    <n-form-item label="Пароль" path="password">
      <n-input v-model:value="formValue.password" placeholder="Введите пароль" />
    </n-form-item>
    <n-form-item>
      <n-button @click="validate"> Validate </n-button>
    </n-form-item>
  </n-form>
  <pre
    >{{ JSON.stringify(formValue, null, 2) }}
</pre
  >
</template>

<script>
export default {
  name: "Login",
  data() {
    return {
      formValue: {},
    };
  },
  methods: {
    validate() {
      return true;
    }
  },
};
</script>

<style scoped></style>
