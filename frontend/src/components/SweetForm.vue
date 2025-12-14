<script setup>
import API from "../api/api";
import { ref } from "vue";

const emit = defineEmits(["added"]);

const name = ref("");
const category = ref("");
const price = ref(0);
const quantity = ref(0);

async function addSweet() {
  await API.post("/sweets", {
    name: name.value,
    category: category.value,
    price: price.value,
    quantity: quantity.value,
  });

  emit("added");
}
</script>

<template>
  <h3>Add Sweet (Admin)</h3>
  <input v-model="name" placeholder="Name" />
  <input v-model="category" placeholder="Category" />
  <input v-model="price" type="number" placeholder="Price" />
  <input v-model="quantity" type="number" placeholder="Quantity" />
  <button @click="addSweet">Add</button>
</template>
