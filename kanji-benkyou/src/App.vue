<template>
  <Layout>
    <router-view />
  </Layout>
</template>

<script>
import Layout from '@/views/Layout.vue';

export default {
  name: 'App',
  components: {
    Layout,
  },
  async mounted() {
    if (localStorage.getItem('refreshToken')) {
      try {
        await this.$store.dispatch(localStorage.getItem('refreshType'));
        this.$nextTick(() => {
          this.$store.dispatch('getProfile');
          this.$route.name === 'Login' && this.$router.push({ name: 'Home' });
        });
      } catch (err) {
        return;
      }
    }
  },
};
</script>

<style>
html,
body {
  margin: 0;
  padding: 0;
}

#app {
  height: 100%;
  width: 100%;
  overflow: none;
}
</style>
