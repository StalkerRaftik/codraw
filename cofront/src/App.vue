<template>
  <div id="app">
    <n-config-provider :theme="theme">
      <n-notification-provider>
        <div class="sctructure">
          <Header />
          <n-el class="main-content">
            <router-view />
          </n-el>
          <Footer v-if="!this.$route?.meta?.hideFooter === true" />
        </div>
      </n-notification-provider>
    </n-config-provider>
  </div>
</template>

<script>
import Header from "@/components/parts/Header";
import Footer from "@/components/parts/Footer";

export default {
  name: "header",
  components: {
    Header,
    Footer,
  },
  computed: {
    theme() {
      return this.$store.getters.theme;
    },
  },
};
</script>

<style scoped>
.sctructure {
  width: 100vw;
  height: 100vh;
  display: grid;
  grid-template-rows: auto 1fr auto;
}
.main-content {
  color: var(--text-color-base);
  background-color: var(--body-color);
}
</style>
