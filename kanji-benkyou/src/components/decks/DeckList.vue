<template>
  <div>
    <a-list :loading="loading" :data-source="decks">
      <template #renderItem="{ item }">
        <a-list-item>
          <template #actions>
            <router-link :to="`/decks/${item.id}`">
              <a-button type="primary" ghost>View</a-button>
            </router-link>
            <router-link :to="`/decks/${item.id}/play`">
              <a-button type="primary">Quiz</a-button>
            </router-link>
            <a-button @click="emitEvt('edit', item.id)" shape="round">
              <template #icon>
                <edit-outlined />
              </template>
            </a-button>
            <a-button
              @click="emitEvt('delete', item.id)"
              shape="round"
              type="danger"
            >
              <template #icon>
                <delete-outlined />
              </template>
            </a-button>
          </template>

          <a-list-item-meta :description="item.description">
            <template #title>{{ item.name }}</template>
          </a-list-item-meta>
        </a-list-item>
      </template>
    </a-list>
  </div>
</template>

<script>
import { computed, onMounted } from 'vue';
import { useStore } from 'vuex';
import { EditOutlined, DeleteOutlined } from '@ant-design/icons-vue';

export default {
  name: 'DeckList',
  components: {
    DeleteOutlined,
    EditOutlined,
  },
  emits: ['edit', 'delete', 'quiz'],
  setup(props, { emit }) {
    const store = useStore();
    const decks = computed(() => store.state.decks);
    const loading = computed(() => store.state.loadingDecks);

    onMounted(() => {
      store.dispatch('getDecks');
    });

    const emitEvt = (evt, id) => {
      emit(evt, id);
    };

    return { loading, decks, emitEvt };
  },
};
</script>

<style lang="sass"></style>
