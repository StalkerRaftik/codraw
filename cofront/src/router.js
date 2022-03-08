import { createWebHistory, createRouter } from "vue-router";
import Home from "@/pages/home/Home";
import Login from "@/pages/authorization/Login";

const routes = [
  {
    path: "",
    name: "Home",
    component: Home,
  },
  {
    path: "/login",
    name: "Login",
    component: Login,
    meta: {
      hideFooter: true,
    },
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
