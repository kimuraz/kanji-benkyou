<template>
  <Layout>
    <router-view />
  </Layout>
</template>

<script>
import Layout from '@/views/Layout';

export default {
  name: 'App',
  components: {
    Layout,
  },
  mounted() {
    if (!this.user?.token && localStorage.getItem('refreshToken')) {
      this.$store.dispatch('getToken', { refresh: true });
    }
  }
};
</script>

<style>
html, body {
  margin: 0;
  padding: 0;
}

#app {
  height: 100%;
  width: 100%;
  overflow: none;
}
</style>
