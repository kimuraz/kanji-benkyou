<template>
  <div id="deck-detail">
    <a-skeleton v-if="loading" />
    <template v-else>
      <h1>{{ deck.name }}</h1>
    </template>
  </div>
</template>

<script>
import { ref, onMounted } from 'vue';
import { useStore } from 'vuex';
import { useRoute } from 'vue-router';
import { notification } from 'ant-design-vue';

import api from '@/api.js';

export default {
  name: 'DeckDetail',
  setup() {
    const store = useStore();
    const route = useRoute();
    const deck = ref(null);
    const loading = ref(true);

    deck.value = store.state.decks.find(
      (d) => d.id === parseInt(route.params.id)
    );

    onMounted(async () => {
      if (!deck.value) {
        try {
          const { data } = await api.get(`/decks/${route.params.id}`);
          deck.value = data;
        } catch (err) {
          console.error(err);

          notification.error({
            message: 'Error',
            description: err.response?.data || err.message,
          });
        }
      }
      loading.value = false;
    });

    return { deck, loading };
  },
};
</script>

<style lang="scss">
#deck-detail {
  padding: 20px;
}
</style>
