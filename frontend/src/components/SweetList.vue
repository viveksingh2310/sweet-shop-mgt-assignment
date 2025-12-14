<script setup>
import API from "../api/api";
import { isAdmin } from "../utils/auth";
import { ref } from "vue";

const props = defineProps({
  sweets: Array,
});

const emit = defineEmits(["updated"]);

const purchaseQty = ref({});
const restockQty = ref({});

async function purchase(id) {
  const qty = purchaseQty.value[id] || 1;

  if (qty <= 0) {
    alert("Purchase quantity must be greater than 0");
    return;
  }

  try {
    await API.post(`/sweets/${id}/purchase`, {
      quantity: qty,
    });

    purchaseQty.value[id] = 1; // reset
    emit("updated");
  } catch (err) {
    alert(err.response?.data?.detail || "Purchase failed");
  }
}

async function restock(id) {
  const qty = restockQty.value[id] || 10;

  if (qty <= 0) {
    alert("Restock quantity must be greater than 0");
    return;
  }

  try {
    await API.post(`/sweets/${id}/restock`, {
      quantity: qty,
    });

    restockQty.value[id] = 10;
    emit("updated");
  } catch (err) {
    alert(err.response?.data?.detail || "Restock failed");
  }
}

async function remove(id) {
  if (!confirm("Are you sure you want to delete this sweet?")) return;

  try {
    await API.delete(`/sweets/${id}`);
    emit("updated");
  } catch (err) {
    alert("Only admin can delete sweets");
  }
}
</script>

<template>
  <ul>
    <li v-for="s in sweets" :key="s.id">
      <strong>{{ s.name }}</strong>
      (₹{{ s.price }}) — Qty: {{ s.quantity }}

      <input
        type="number"
        min="1"
        v-model.number="purchaseQty[s.id]"
        placeholder="Qty"
        style="width: 70px; margin-left: 8px"
      />
      <button @click="purchase(s.id)">Buy</button>

      <template v-if="isAdmin()">
        <input
          type="number"
          min="1"
          v-model.number="restockQty[s.id]"
          placeholder="Restock"
          style="width: 80px; margin-left: 10px"
        />
        <button @click="restock(s.id)">Restock</button>
        <button @click="remove(s.id)">Delete</button>
      </template>
    </li>
  </ul>
</template>
