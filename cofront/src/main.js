import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";
import store from "./store/index";
import naive from "naive-ui";
import prepopulateStore from "@/store/prepopulate";

import "./assets/main.css";
import "vfonts/Lato.css";

const app = createApp(App, {});
app.use(router);
app.use(naive);
app.use(store);

(async () => {
  await prepopulateStore();
  app.mount("#app");
})();
