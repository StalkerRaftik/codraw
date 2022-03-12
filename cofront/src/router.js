import { createWebHistory, createRouter } from "vue-router";
import Home from "@/pages/home/Home";
import Login from "@/pages/authorization/Login";
import Registration from "@/pages/authorization/Registration";
import Profile from "@/pages/Profile";

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
  {
    path: "/registration",
    name: "Register",
    component: Registration,
    meta: {
      hideFooter: true,
    },
  },
    {
    path: "/me",
    name: "Profile",
    component: Profile,
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
