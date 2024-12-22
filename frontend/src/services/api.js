import axios from "axios";

const API_BASE_URL = "http://127.0.0.1:8000/api";

export const extractData = async (file) => {
  const formData = new FormData();
  formData.append("file", file);
  const response = await axios.post(`${API_BASE_URL}/extract`, formData, {
    headers: {
      "Content-Type": "multipart/form-data",
    },
  });
  return response.data;
};

export const translateText = async (text) => {
  const response = await axios.post(`${API_BASE_URL}/translate`, { text });
  return response.data;
};
