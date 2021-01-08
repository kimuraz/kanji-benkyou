import { createStore } from 'vuex';
import api from './api';
import { notification } from 'ant-design-vue';

const store = createStore({
  state() {
    return {
      user: {
        name: '',
        email: '',
        token: '',
      },
      decks: [],
      loadingDecks: false,
    };
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
  },
  // TODO: Separate newTOkena and refresh toke methods!
  actions: {
    async getToken(
      context,
      { client_id, grant_type, client_secret, backend, token, refresh }
    ) {
      const refreshToken = localStorage.getItem('refreshToken');
      const tokenLabel = refresh ? 'refresh_token' : 'token';
      localStorage.removeItem('accessToken');
      localStorage.removeItem('refreshToken');

      if (!refreshToken && refresh) {
        window.location = '/login';
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
            [tokenLabel]: refresh ? refreshToken : token,
          }
        );
        localStorage.setItem('accessToken', data.access_token);
        localStorage.setItem('refreshToken', data.refresh_token);
        context.commit('setUser', {
          name: '',
          email: '',
          token: data.access_token,
        });
        setTimeout(() => {
          context.dispatch('getToken', {
            client_id,
            grant_type: 'refresh_token',
            client_secret,
            backend,
            token: null,
            refresh: true,
          });
        }, data.expires_in);
      } catch (err) {
        if (refresh && err.reponse?.status === 401) {
          window.location = '/login';
        } else {
          console.error(err);
          notification.error({
            message: 'Error',
            description: err.message,
          });
        }
      }
    },
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

          await context.dispatch('getToken', {
            grant_type: 'convert_token',
            // Generated on django admin
            client_id: process.env.VUE_APP_DJANGO_GOOGLE_APP_ID,
            client_secret: process.env.VUE_APP_DJANGO_GOOGLE_APP_SECRET,
            backend: 'google-oauth2',
            token: Object.values(gRes).find(v => !!v.access_token).access_token,
          });

          context.dispatch('getDecks');
        } catch (err) {
          console.error(err);
        }
      });
    },

    async getDecks(context) {
      try {
        context.state.loadingDecks = true;
        const { data } = await api.get('/decks/');
        context.commit('setDecks', data);
      } catch (err) {
        console.error(err);
      }
    },

    async newDeck(context, deck) {
      try {
        const { data } = await api.post('/decks/', deck);
        context.commit('addDeck', data);
        console.log(data);
        notification.success({
          message: 'Deck saved!',
          description: `${name} was successfully saved!`,
        });
      } catch (err) {
        console.error(err);
        notification.error({
            message: 'Error',
            description: 'Could not save this deck, please try again.',
        });
        throw err;
      }
    },
  },
});

export default store;
