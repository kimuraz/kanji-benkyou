import { createWebHistory, createRouter } from 'vue-router';
import store from './store';

import Home from '@/views/Home';
import Login from '@/views/Login';
import Decks from '@/views/Decks';
import DeckDetail from '@/views/DeckDetail';
import FilteredJlpt from '@/views/FilteredJlpt';

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
    path: '/decks/:id',
    name: 'DeckDetail',
    component: DeckDetail,
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
