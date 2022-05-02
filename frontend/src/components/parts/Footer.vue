<template>
  <n-config-provider :theme="darkTheme">
    <n-card class="footer" :bordered="false">
      <n-space justify="start" align="center">
        <n-button-group size="large">
          <n-button tag="a" href="#">
            <template #icon>
              <n-icon>
                <BookContacts20Filled />
              </n-icon>
            </template>
            О нас</n-button
          >
          <n-button tag="a" href="#"
            ><template #icon>
              <n-icon>
                <Info28Regular />
              </n-icon> </template
            >Контакты</n-button
          >
        </n-button-group>
      </n-space>
    </n-card>
  </n-config-provider>
</template>

<script>
import { darkTheme } from "naive-ui";
import Info28Regular from "@vicons/fluent/Info28Regular";
import BookContacts20Filled from "@vicons/fluent/BookContacts20Filled";
export default {
  name: "Footer",
  components: {
    BookContacts20Filled,
    Info28Regular,
  },
  data() {
    return {
      darkTheme,
    };
  },
};
</script>

<style scoped>
.footer {
  border-radius: 0px;
}
</style>