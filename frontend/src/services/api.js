import axios from "axios";

const API = axios.create({
  baseURL: "http://127.0.0.1:8000",
  timeout: 10000,
});

// Optional: interceptors (future-ready)
API.interceptors.response.use(
  (response) => response,
  (error) => {
    console.error("API Error:", error);
    return Promise.reject(error);
  }
);

export const analyzeNews = async (data) => {
  const response = await API.post("/analyze", data);
  return response.data;
};
