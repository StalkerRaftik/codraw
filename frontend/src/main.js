import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";
import store from "./store/index";
import naive from "naive-ui";
import prepopulateStore from "@/store/prepopulate";

import $t from '@/i18n'
import bp from "@/breakpoints"

import "./assets/main.css";
import "vfonts/Lato.css";

const app = createApp(App, {});
app.use(router);
app.use(naive);
app.use(store);

app.config.globalProperties.$t = $t;
app.config.globalProperties.$bp = bp;


(async () => {
  await prepopulateStore();
  app.mount("#app");
})();
