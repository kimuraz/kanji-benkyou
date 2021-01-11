<template>
  <a-layout>
      <a-menu
        mode="horizontal"
        :selectedKeys="[$route.name]"
        theme="dark"
      >
        <a-menu-item key="Home">
          <router-link :to="{ name: 'Home' }">
            <home-outlined />
            Home
          </router-link>
        </a-menu-item>

        <a-menu-item key="JLPT">
          <router-link :to="{ name: 'JLPT' }">
            <file-protect-outlined />
            JLPT
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

    <a-layout-content
      :style="{ overflow: 'auto', minHeight: 'calc(100vh - 117px)' }"
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
import {
  BookOutlined,
  FileProtectOutlined,
  HomeOutlined,
  UserOutlined,
} from '@ant-design/icons-vue';
import { useStore } from 'vuex';

export default {
  name: 'Layout',
  components: {
    BookOutlined,
    FileProtectOutlined,
    HomeOutlined,
    UserOutlined,
  },
  setup() {
    const store = useStore();
    const user = computed(() => store.state.user);

    return { user };
  },
};
</script>

<style lang="sass"></style>
