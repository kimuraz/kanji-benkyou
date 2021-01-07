import { createWebHistory, createRouter } from 'vue-router';

import Home from '@/views/Home';
import Login from '@/views/Login';
import Decks from '@/views/Decks';

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home,
  },
  {
    path: '/login',
    name: 'Login',
    component: Login,
  },
  {
    path: '/decks',
    name: 'Decks',
    component: Decks,
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
