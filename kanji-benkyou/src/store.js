import { createStore } from 'vuex';
import api from './api';
import { notification } from 'ant-design-vue';
import router from './router';

const store = createStore({
  state() {
    return {
      user: {
        username: '',
        first_name: '',
        last_name: '',
        email: '',
        isLogged: false,
      },
      decks: [],
      loadingDecks: false,
    };
  },
  getters: {
    isLogged: (state) => state.user.isLogged,
  },
  mutations: {
    setUser(state, user) {
      state.user = { ...user };
    },
    setDecks(state, decks) {
      state.loadingDecks = false;
      state.decks = decks;
    },
    addDeck(state, deck) {
      state.decks.push(deck);
    },
    editDeck(state, deck) {
      state.decks.splice(
        state.decks.findIndex((d) => d.id === deck.id),
        1,
        { ...deck }
      );
    },
    removeDeck(state, id) {
      state.decks.splice(
        state.decks.findIndex((d) => d.id === id),
        1
      );
    },
  },
  actions: {
    async getProfile({ commit }) {
      try {
        const { data } = await api.get('/profile/');
        commit('setUser', { ...data, isLogged: true });
      } catch (err) {
        if (err.response?.status === 401) {
          router.push({ name: 'Login' });
        } else {
          console.error(err);
          notification.error({
            message: 'Error',
            description: err.message,
          });
        }
      }
    },
    async getToken(
      { dispatch },
      { client_id, grant_type, client_secret, backend, token, refresh }
    ) {
      const tokenLabel = refresh ? 'refresh_token' : 'token';
      localStorage.removeItem('accessToken');
      localStorage.removeItem('refreshToken');

      if (!token && refresh) {
        router.push({ name: 'Login' });
        return;
      }

      try {
        const { data } = await api.post(
          `/auth/${refresh ? 'token' : 'convert-token'}`,
          {
            grant_type,
            client_id,
            client_secret,
            backend,
            [tokenLabel]: token,
          }
        );
        localStorage.setItem('accessToken', data.access_token);
        localStorage.setItem('refreshToken', data.refresh_token);
        setTimeout(() => {
          dispatch('gRefresh');
        }, data.expires_in);
      } catch (err) {
        if (refresh && err.reponse?.status === 401) {
          router.push({ name: 'Login' });
        } else {
          console.error(err);
          notification.error({
            message: 'Error',
            description: err.message,
          });
        }
      }
    },
    async gRefresh({ dispatch }) {
      await dispatch('getToken', {
        client_id: process.env.VUE_APP_DJANGO_GOOGLE_APP_ID,
        client_secret: process.env.VUE_APP_DJANGO_GOOGLE_APP_SECRET,
        backend: 'google-oauth2',
        grant_type: 'refresh_token',
        token: localStorage.getItem('refreshToken'),
        refresh: true,
      });
    },
    gLogin({ dispatch }) {
      window.gapi.load('client:auth2', async () => {
        try {
          await window.gapi.client.init({
            apiKey: process.env.VUE_APP_GOOGLE_API_KEY,
            clientId: process.env.VUE_APP_GOOGLE_CLIENT_ID,
            scope:
              'https://www.googleapis.com/auth/userinfo.email https://www.googleapis.com/auth/userinfo.profile openid',
          });

          const gRes = await window.gapi.auth2.getAuthInstance().signIn();

          await dispatch('getToken', {
            grant_type: 'convert_token',
            // Generated on django admin
            client_id: process.env.VUE_APP_DJANGO_GOOGLE_APP_ID,
            client_secret: process.env.VUE_APP_DJANGO_GOOGLE_APP_SECRET,
            backend: 'google-oauth2',
            token: Object.values(gRes).find((v) => !!v.access_token)
              .access_token,
          });

          localStorage.setItem('refreshType', 'gRefresh');
          dispatch('getProfile');
          dispatch('getDecks');
          router.replace({ name: 'Home' });
        } catch (err) {
          console.error(err);
        }
      });
    },

    async getDecks({ commit, state }) {
      try {
        state.loadingDecks = true;
        const { data } = await api.get('/decks/');
        commit('setDecks', data.results);
      } catch (err) {
        console.error(err);
      }
    },

    async newDeck({ commit }, deck) {
      try {
        const { data } = await api.post('/decks/', deck);
        commit('addDeck', data);
        console.log(data);
        notification.success({
          message: 'Deck saved!',
          description: `${name} was successfully saved!`,
        });
      } catch (err) {
        console.error(err);
        if (err.response?.data?.err === 'max_decks_per_user') {
          notification.error({
            message: 'Error',
            description:
              'Max number of decks reached, delete a deck to start a new one.',
          });
          throw err;
        }
        notification.error({
          message: 'Error',
          description: 'Could not save this deck, please try again.',
        });
        throw err;
      }
    },
    async edit({ commit }, deck) {
      try {
        const { data } = await api.patch(`/decks/${deck.id}`, deck);
        commit('editDeck', data);
      } catch (err) {
        console.error(err);
        notification.error({
          message: 'Error',
          description:
            'An error occurred whie deleting this deck, please try again.',
        });
      }
    },
    async deleteDeck({ commit }, id) {
      try {
        await api.delete(`/decks/${id}`);
        commit('removeDeck', id);
      } catch (err) {
        console.error(err);
        notification.error({
          message: 'Error',
          description:
            'An error occurred whie deleting this deck, please try again.',
        });
      }
    },
  },
});

export default store;
