import axios from "axios";

const API = "http://localhost:8000";

export const encryptMessage = async (text) => {
  const res = await axios.post(`${API}/encrypt`, { text });
  return res.data;
};

export const decryptMessage = async (cipher) => {
  const res = await axios.post(`${API}/decrypt`, { cipher });
  return res.data;
};
