import axios from 'axios';

const API_BASE_URL = 'http://localhost:8000';

export const login = async (email, password) => {
  const response = await axios.post(`${API_BASE_URL}/auth/login`, { email, password });
  return response.data;
};

export const getFiles = async () => {
  const response = await axios.get(`${API_BASE_URL}/files`);
  return response.data;
};