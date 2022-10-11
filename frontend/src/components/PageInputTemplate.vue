<template>
  <n-space justify="center" align="center" style="height: 100%">
    <n-card
      :title="this.title"
      size="huge"
      :style="{ width: $bp.lg.matches ? '600px' : 'auto' }"
    >
      <n-form ref="formRef" :rules="rules" :model="mutableFormData" :disabled="disabled">
        <n-form-item
          v-for="key in Object.keys(mutableFormData)"
          :key="key"
          :label="uiData[key].label"
          :path="key"
        >
          <n-input
            v-model:value="mutableFormData[key]"
            :type="uiData[key].type"
            :placeholder="uiData[key].placeholder"
            v-on:keyup.enter="validate"
          />
        </n-form-item>
        <n-space justify="center">
          <n-form-item>
            <n-button
              @click.prevent="validate"
              :style="{ width: $bp.lg.matches ? '200px' : 'auto' }"
              :disabled="disabled"
            >
              {{ buttonTitle }}
            </n-button>
          </n-form-item>
        </n-space>
      </n-form>
    </n-card>
  </n-space>
</template>

<script>
export default {
  name: "RegistrationTemplate",
  props: {
    uiData: { type: Object, required: true },
    formData: { type: Object, required: true },
    disabled: {type: Boolean, required: true },
    rules: { type: Object, required: false },
    title: { type: String, default: "" },
    buttonTitle: { type: String, default: "" },
  },
  data() {
    return {
      mutableFormData: JSON.parse(JSON.stringify(this.formData)),
    };
  },
  methods: {
    async validate() {
      let hasErrors = false;
      await this.$refs.formRef.validate((errors) => {
        hasErrors = Boolean(errors && errors.length > 0);
      });

      if (!hasErrors) {
        this.$emit('validated', this.mutableFormData);
      }
    },
  },
};
</script>

<style scoped></style>
