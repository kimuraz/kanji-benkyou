<template>
  <div id="home">
    <a-row justify="center">
      <a-col :sm="12" :md="9" :lg="8">
        <a-input-search
          size="large"
          v-model:value="q"
          @search="search()"
          placeholder="Search for a kanji"
        />
      </a-col>
    </a-row>

    <a-row>
      <kanji-search-results
        v-if="results && results.length"
        @page="search"
        :loading="loading"
        :page="page"
        :total="total"
        :kanjis="results"
      />
    </a-row>
  </div>
</template>

<script>
import { toRefs, reactive } from 'vue';
import { notification } from 'ant-design-vue';

import api, { PAGE_SIZE } from '@/api';

import KanjiSearchResults from '@/components/kanjis/KanjiSearchResults';

export default {
  name: 'Home',
  components: {
    KanjiSearchResults,
  },
  setup() {
    const state = reactive({
      q: '',
      page: 1,
      loading: false,
      total: 0,
      results: [],
    });

    const search = async (page = 1) => {
      try {
        state.loading = true;
        state.results = [];
        const { data } = await api.get(
          `/kanjis?q=${state.q}&offset=${PAGE_SIZE * (page-1)}`
        );
        state.results = data.results;
        state.total = data.count;
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

    return { ...toRefs(state), search };
  },
};
</script>

<style lang="scss">
#home {
  padding: 20px;
  height: 100%;
  min-height: 100%;
}
</style>
