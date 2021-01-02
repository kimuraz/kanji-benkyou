<template>
  <a-row>
    <a-col :sm="10" :md="8" :lg="6">
      <a-card class="login-card">
        <img src="@/assets/btn_google_signin.png" @click="gLogin" />
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
