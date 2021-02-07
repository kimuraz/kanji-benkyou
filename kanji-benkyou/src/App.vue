<template>
  <Layout>
    <router-view v-if="!loading" />
  </Layout>
</template>

<script>
import Layout from '@/views/Layout';

export default {
  name: 'App',
  components: {
    Layout,
  },
  data() {
    return {
      loading: true,
    };
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
      } finally {
        this.loading = false;
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
