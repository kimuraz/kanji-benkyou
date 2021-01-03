<template>
  <a-row justify="center" :style="{ marginTop: '10vh'}">
    <a-col :sm="10" :md="8" :lg="6">
      <a-card class="login-card">
        <h2>Login</h2>
        <a-row>
          <a-col :sm="12" :md="6">
            <img src="@/assets/btn_google_signin.png" @click="gLogin" />
          </a-col>
        </a-row>
      </a-card>
    </a-col>
  </a-row>
</template>

<script>
import { useStore } from 'vuex';
export default {
  name: 'Login',
  setup() {
    const store = useStore();

    function gLogin() {
      store.dispatch('gLogin');
    }

    return { gLogin };
  },
};
</script>

<style>
.login-card {
  width: fit-content;
}
.login-card img {
  cursor: pointer;
}
</style>
