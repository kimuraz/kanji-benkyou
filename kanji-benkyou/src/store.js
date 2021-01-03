import { createStore } from 'vuex';
import api from './api';

const store = createStore({
  state() {
    return {
      user: {
        name: '',
        email: '',
        token: '',
      },
      decks: [],
    };
  },
  mutations: {
    setUser(state, user) {
      state.user = { ...user };
    },
    setDecks(state, decks) {
      state.decks = decks;
    },
  },
  actions: {
    gLogin(context) {
      window.gapi.load('client:auth2', async () => {
        try {
          await window.gapi.client.init({
            apiKey: process.env.VUE_APP_GOOGLE_API_KEY,
            clientId: process.env.VUE_APP_GOOGLE_CLIENT_ID,
            scope:
              'https://www.googleapis.com/auth/userinfo.email https://www.googleapis.com/auth/userinfo.profile openid',
          });

          const gRes = await window.gapi.auth2.getAuthInstance().signIn();

          const res = await api.post('/auth/convert-token', {
            grant_type: 'convert_token',
            // Generated on django admin
            client_id: process.env.VUE_APP_DJANGO_GOOGLE_APP_ID,
            client_secret: process.env.VUE_APP_DJANGO_GOOGLE_APP_SECRET,
            backend: 'google-oauth2',
            token: gRes.xc.access_token,
          });

          localStorage.setItem('accessToken', res.data.access_token);
          localStorage.setItem('refreshToken', res.data.refresh_token);

          context.commit('setUser', {
            name: '',
            email: '',
            token: res.data.access_token,
          });
          context.dispatch('getDecks');
        } catch (err) {
          console.error(err);
        }
      });
    },

    async getDecks(context) {
      try {
        const { data } = await api.get('/decks/');
        context.commit('setDecks', data);
      } catch (err) {
        console.error(err);
      }
    },
  },
});

export default store;
