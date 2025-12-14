<script setup>
import { ref } from "vue";
import API from "../api/api";
import { isAdmin } from "../utils/auth";

const props = defineProps({
  sweets: Array,
});

const emit = defineEmits(["added"]);

const name = ref("");
const category = ref("Indian");
const price = ref("");
const quantity = ref("");

const categories = [
  "Indian",
  "Syrupy",
  "Dry/Fudge",
  "Laddu",
  "Pudding/Halva",
  "Milk-Based",
  "Fried",
  "Frozen",
];

async function addSweet() {
  const exists = props.sweets.some(
    (s) => s.name.toLowerCase() === name.value.toLowerCase()
  );

  if (exists) {
    alert("Sweet with this name already exists");
    return;
  }

  try {
    await API.post("/sweets", {
      name: name.value,
      category: category.value,
      price: Number(price.value),
      quantity: Number(quantity.value),
    });

    emit("added");

    name.value = "";
    price.value = "";
    quantity.value = "";
  } catch (err) {
    if (err.response?.status === 403) {
      alert("Only admin can add sweets");
    } else {
      alert("Failed to add sweet");
    }
  }
}
</script>

<template>
  <!-- ADMIN ONLY -->
  <div v-if="isAdmin()">
    <h3>Add Sweet</h3>

    <input v-model="name" placeholder="Name" />

    <select v-model="category">
      <option v-for="c in categories" :key="c" :value="c">
        {{ c }}
      </option>
    </select>

    <input v-model.number="price" placeholder="Price" type="number" />

    <input
      v-model.number="quantity"
      placeholder="Quantity"
      type="number"
    />

    <button @click="addSweet">Add Sweet</button>
  </div>
</template>
