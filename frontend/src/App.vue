<template>
  <nav>
    <router-link to="/">Sweets</router-link> |
    <router-link to="/login">Login</router-link> |
    <router-link to="/register">Register</router-link>
  </nav>

  <router-view />
</template>

<style>
nav {
  padding: 10px;
}
nav a {
  margin-right: 10px;
}
</style>
