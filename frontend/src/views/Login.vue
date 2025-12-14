<script setup>
import { ref } from "vue";
import API from "../api/api";
import { ADMIN_EMAILS } from "../config/admin";
import { useRouter } from "vue-router";

const email = ref("");
const password = ref("");
const router = useRouter();

async function login() {
  const res = await API.post("/auth/login", {
    email: email.value,
    password: password.value,
  });

  localStorage.setItem("token", res.data.access_token);
  localStorage.setItem("email", email.value);

  const isAdmin = ADMIN_EMAILS.includes(email.value);
  localStorage.setItem("isAdmin", isAdmin ? "true" : "false");

  router.push("/sweets");
}
</script>


<template>
  <h2>Login</h2>
  <input v-model="email" placeholder="Email" />
  <input v-model="password" type="password" placeholder="Password" />
  <button @click="login">Login</button>
</template>
