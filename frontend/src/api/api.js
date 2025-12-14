import axios from "axios";

const API = axios.create({
  baseURL: "https://sweet-shop-mgt-assignment-1.onrender.com/api", // backend render URL
});

API.interceptors.request.use((config) => {
  const token = localStorage.getItem("token");
  if (token) {
    config.headers.Authorization = `Bearer ${token}`;
  }
  return config;
});

export default API;
