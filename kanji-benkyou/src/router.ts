import { createWebHistory, createRouter } from 'vue-router';
import store from './store';

import Home from '@/views/Home.vue';
import Login from '@/views/Login.vue';
import Decks from '@/views/Decks.vue';
import FilteredJlpt from '@/views/FilteredJlpt.vue';

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
  {
    path: '/jlpt',
    name: 'JLPT',
    component: FilteredJlpt,
  },
];

const authRoutes = ['Decks'];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

router.beforeEach((to, from, next) => {
  if (authRoutes.includes(to.name) && !store.getters.isLogged) {
    next({ name: 'Login' });
  } else if (to.name === 'Login' && store.getters.isLogged) {
    next({ name: 'Home' });
  } else {
    next();
  }
});

export default router;
