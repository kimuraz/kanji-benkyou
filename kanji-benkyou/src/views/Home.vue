<template>
  <div id="home">
    <a-row justify="center">
      <a-col :sm="12" :md="9" :lg="8">
        <a-input-search
          size="large"
          v-model:value="state.q"
          @search="search()"
          placeholder="Search for a kanji"
        />
      </a-col>
    </a-row>

    <a-row>
      <div class="results">
        <a-spin v-if="state.loading" size="large" />
        <a-empty v-if="!state.results" :description="false" />

        <div class="cards-content" v-if="state.results">
          <kanji-card v-for="k in state.results" :key="k.id" :kanji="k" />
        </div>
      </div>
    </a-row>
  </div>
</template>

<script>
import { reactive, watch } from 'vue';
import { notification } from 'ant-design-vue';

import api from '@/api';

import KanjiCard from '@/components/kanjis/KanjiCard';

export default {
  name: 'Home',
  components: {
    KanjiCard,
  },
  setup() {
    const state = reactive({
      q: '',
      page: 0,
      loading: false,
      results: [],
    });

    const search = async (page = 0) => {
      try {
        state.loading = true;
        state.results = [];
        const { data } = await api.get(
          `/kanjis?q=${state.q}&page=${page}`
        );
        state.results = data.results;
      } catch (error) {
        if (error.response?.status !== 404) {
          notification.error({
            message: 'Error',
            description: error.message,
          });
        } else {
          state.results = null;
        }
      } finally {
        state.loading = false;
      }
    };

    watch(
      () => state.page,
      () => {
        search();
      }
    );

    return { state, search };
  },
};
</script>

<style lang="scss">
#home {
  padding: 20px;
  height: 100%;
  min-height: 100%;
}

.results {
  margin-top: 20px;
}

.loading-empty {
  width: 100%;
  margin: 20px;
  text-align: center;
}
.cards-content {
  display: flex;
  flex-wrap: wrap;
  justify-content: space-around;
  align-items: strech;
}
</style>
