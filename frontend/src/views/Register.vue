<script setup>
import API from "../api/api";
import { ref } from "vue";

const email = ref("");
const password = ref("");

async function register() {
  await API.post("/auth/register", {
    email: email.value,
    password: password.value,
  });
  alert("Registered successfully");
}
</script>

<template>
  <h2>Register</h2>
  <input v-model="email" placeholder="Email" />
  <input v-model="password" type="password" placeholder="Password" />
  <button @click="register">Register</button>
</template>
