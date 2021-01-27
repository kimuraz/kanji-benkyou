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
    if (localStorage.getItem('refreshToken')) {
      this.$store.dispatch('getProfile');
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
