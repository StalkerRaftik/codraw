import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";
import { store } from './store/index'
import naive from 'naive-ui'

import './assets/main.css';
import 'vfonts/Lato.css'

const app = createApp(App);
app.use(router)
app.use(naive);
app.use(store)
app.mount("#app");
