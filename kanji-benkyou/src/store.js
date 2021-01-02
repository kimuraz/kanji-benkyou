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
    };
  },
  mutations: {
    setUser(state, user) {
      state.user = { ...user };
    },
  },
  actions: {
    gLogin() {
      console.log(process.env)
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

          localStorage.setItem('accessToken', res.access_token);
          localStorage.setItem('refreshToken', res.refresh_token);
        } catch (err) {
          console.error(err);
        }
      });
    },
  },
});

export default store;
