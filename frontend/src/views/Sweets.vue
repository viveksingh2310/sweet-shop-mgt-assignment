<script setup>
import { ref, onMounted } from "vue";
import API from "../api/api";
import SweetList from "../components/SweetList.vue";
import AddSweet from "../components/AddSweet.vue";
import {isAdmin} from '../utils/auth'

const sweets = ref([]);

async function loadSweets() {
  const res = await API.get("/sweets");
  sweets.value = res.data;
}

onMounted(loadSweets);
</script>

<template>
  <h2>Sweets Inventory</h2>

  <AddSweet
  v-if="isAdmin()"
  :sweets="sweets"
  @added="loadSweets"
/>

  <hr />

  <!-- List & Actions -->
  <SweetList
    :sweets="sweets"
    @updated="loadSweets"
  />
</template>
