<template>
  <n-space
    justify="center"
    align="center"
    style="height: 100%; margin-right: 0; margin-top: 4px"
  >
    <n-card
      title="Профиль"
      size="huge"
      :style="{ width: $bp.lg.matches ? '600px' : 'auto' }"
    >
      <n-list>
        <n-list-item v-for="(mas, key) in profileData" :key="key">
          <template #prefix>
            <div
              style="width: 150px; text-align: right; overflow-wrap: break-word"
            >
              <n-text type="info" strong>{{ $t(mas[0]) }}:</n-text>
            </div>
          </template>
          {{ $t(mas[1]) }}
        </n-list-item>
      </n-list>
      <template #action>
        <n-button
          strong
          secondary
          type="primary"
          @click="showInputModal = true"
        >
          Изменить данные
        </n-button>
      </template>
    </n-card>
    <n-modal
      v-model:show="showInputModal"
      :on-after-leave="() => (this.buttonText = buttonEnum.INITIAL)"
    >
      <PageInputTemplate
        title="Изменить данные"
        :button-title="buttonText"
        :form-data="formData"
        :ui-data="uiData"
        :disabled="disabled"
        @validated="changeData"
      />
    </n-modal>
  </n-space>
</template>

<script>
import PageInputTemplate from "@/components/PageInputTemplate";
import { client } from "@/axios";
import { useNotification } from "naive-ui";
import { parseResponseException } from "@/utils";

const buttonTextEnum = {
  INITIAL: "Изменить",
  SUBMIT: "Вы точно уверены?",
};

export default {
  name: "Login",
  components: {
    PageInputTemplate,
  },
  data() {
    return {
      showInputModal: false,
      disabled: false,
      user: this.$store.getters.user,
      notification: useNotification(),
      formData: {
        username: "",
        password: "",
      },
      uiData: {
        username: {
          placeholder: this.$store.getters.user.username,
          label: "Изменить логин",
          type: "text",
        },
        password: {
          placeholder: "********",
          label: "Изменить пароль",
          type: "password",
        },
      },
      buttonEnum: buttonTextEnum,
      buttonText: buttonTextEnum.INITIAL,
    };
  },
  computed: {
    profileData() {
      const priority = {
        id: 100,
        username: 99,
        password: 98,
        email: 97,
        is_staff: 96,
      };
      const getPriority = (key) => priority[key] || 0;
      return [...Object.entries(this.user), ["password", "**********"]].sort(
        (f, s) => getPriority(s[0]) - getPriority(f[0])
      );
    },
  },
  methods: {
    async changeData(patchData) {
      if (this.buttonText === this.buttonEnum.INITIAL) {
        this.buttonText = this.buttonEnum.SUBMIT;
        return;
      }
      this.buttonText = this.buttonEnum.INITIAL;
      patchData = Object.fromEntries(
        Object.entries(patchData).filter((arr) => Boolean(arr[1]))
      );
      if (Object.keys(patchData).length === 0) {
        this.notification.warning({
          title: "Вы ничего не выбрали!",
          duration: 3000,
        });
        return;
      }
      this.disabled = true;
      try {
        await client.patch(`/user/${this.user.id}/`, patchData);
        await this.$store.dispatch("fetchUserData");
        await this.$router.push("/");
        this.notification.success({
          title: "Данные были успешно обновлены!",
          duration: 3000,
        });
      } catch (e) {
        this.notification.error({
          title: `Ошибка!`,
          content: parseResponseException(e),
          duration: 10000,
        });
      }
      this.disabled = false;
    },
  },
};
</script>
