<template>
  <section>
    <h3>Showing {{ kanjis.length }} out of {{ total }}</h3>

    <a-pagination
      :current="page"
      :total="total"
      :pageSize="pageSize"
      @change="(pg) => $emit('page', pg)"
    />

    <div class="kanjis-list">
      <a-spin size="large" v-if="loading" />
      <kanji-card v-for="k in kanjis" :key="k.id" :kanji="k" />
    </div>

    <a-pagination
      :current="page"
      :total="total"
      :pageSize="pageSize"
      @change="(pg) => $emit('page', pg)"
    />
  </section>
</template>

<script>
import { ref } from 'vue';

import KanjiCard from '@/components/kanjis/KanjiCard';
import { PAGE_SIZE } from '@/api';

export default {
  name: 'KanjiSearchResults',
  emits: ['page'],
  components: {
    KanjiCard,
  },
  props: {
    loading: {
      type: Boolean,
      required: true,
    },
    page: {
      type: Number,
      required: true,
    },
    total: {
      type: Number,
      required: true,
    },
    kanjis: {
      type: Array,
      required: true,
    },
  },
  setup() {
    const pageSize = ref(PAGE_SIZE);

    return { pageSize };
  },
};
</script>

<style lang="scss">
.kanjis-list {
  display: flex;
  flex-wrap: wrap;
  justify-content: space-around;
  align-items: strech;
  margin-left: -15px;
}
</style>
