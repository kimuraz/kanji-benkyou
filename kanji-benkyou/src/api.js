import axios from 'axios';

const api = axios.create({
  baseURL: process.env.VUE_APP_API_URL,
});

api.interceptors.request.use(
  (config) => {
    const token = localStorage.getItem('accessToken');
    const unauthPaths = ['/kanjis/search'];
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
