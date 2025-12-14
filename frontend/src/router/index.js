import { createRouter, createWebHistory } from "vue-router";
import Login from "../views/Login.vue";
import Register from "../views/Register.vue";
import Sweets from "../views/Sweets.vue";

const routes = [
  { path: "/", redirect: "/sweets" },
  { path: "/login", component: Login },
  { path: "/register", component: Register },
  { path: "/sweets", component: Sweets },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
