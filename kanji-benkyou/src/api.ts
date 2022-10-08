import axios from 'axios';

export const PAGE_SIZE = 30;

const api = axios.create({
  baseURL: import.meta.env.VITE_APP_API_URL,
});

api.interceptors.request.use(
  (config) => {
    const token = localStorage.getItem('accessToken');
    const unauthPaths = ['/kanjis'];
    if (token && !unauthPaths.some(p => config.url.includes(p))) {
      Object.assign(config.headers, { Authorization: `Bearer ${token}` });
    }
    return config;
  },
  (err) => {
    return Promise.reject(err);
  }
);

export default api;
