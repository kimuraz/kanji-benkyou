<template>
  <a-layout>
    <a-layout-header>
      <a-menu
        mode="horizontal"
        :selectedKeys="[routeName]"
        theme="dark"
        :style="{ marginTop: '10px', width: 'fit-content', marginLeft: 'auto' }"
      >
        <a-menu-item key="Home">
          <router-link :to="{ name: 'Home' }">
            <home-outlined />
            Home
          </router-link>
        </a-menu-item>

        <a-menu-item key="Decks" v-if="user.token">
          <router-link :to="{ name: 'Decks' }">
            <book-outlined />
            Decks
          </router-link>
        </a-menu-item>

        <a-menu-item key="Login" v-if="!user.token">
          <router-link :to="{ name: 'Login' }">
            <user-outlined />
            Login
          </router-link>
        </a-menu-item>
      </a-menu>
    </a-layout-header>

    <a-layout-content
      :style="{ overflow: 'auto', minHeight: 'calc(100vh - 134px)' }"
    >
      <slot />
    </a-layout-content>

    <a-layout-footer
      :style="{ textAlign: 'center', borderTop: '1px solid #f0f2f5' }"
    >
      KanjiBenkyou
    </a-layout-footer>
  </a-layout>
</template>

<script>
import { computed } from 'vue';
import { useRouter } from 'vue-router';
import {
  BookOutlined,
  HomeOutlined,
  UserOutlined,
} from '@ant-design/icons-vue';
import { useStore } from 'vuex';

export default {
  name: 'Layout',
  components: {
    HomeOutlined,
    UserOutlined,
    BookOutlined,
  },
  setup() {
    const { currentRoute } = useRouter();
    const store = useStore();
    const routeName = computed(() => currentRoute.name);
    const user = computed(() => store.state.user);

    return { routeName, user };
  },
};
</script>

<style lang="sass"></style>
