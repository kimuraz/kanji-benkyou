<template>
  <div id="filtered-jlpt">
    <div class="filters">
      <jlpt-badge
        v-for="lvl in 5"
        @click="!loading && getKanjis(lvl, 1)"
        :key="lvl"
        :level="lvl"
        :active="lvl === activeLevel"
      />
    </div>

    <h3>Showing {{ kanjis.length }} out of {{ ttl }}</h3>

    <!-- pageSize=1 is a hack for controlling correctly this component-->
    <a-pagination
      v-model:current="page"
      :total="2"
      :pageSize="1"
      @change="(pg) => getKanjis(activeLevel, pg)"
    />

    <div class="kanjis-list">
      <a-spin size="large" v-if="loading" />
      <kanji-card v-for="k in kanjis" :key="k.id" :kanji="k" />
    </div>

    <a-pagination
      v-model:current="page"
      :total="2"
      :pageSize="1"
      @change="(pg) => getKanjis(activeLevel, pg)"
    />
  </div>
</template>

<script>
import { reactive, toRefs, onMounted } from 'vue';
import JlptBadge from '@/components/kanjis/JlptBadge';
import KanjiCard from '@/components/kanjis/KanjiCard';

import api from '@/api';

export default {
  name: 'FilteredJlpt',
  components: {
    JlptBadge,
    KanjiCard,
  },
  setup() {
    const state = reactive({
      activeLevel: 5,
      page: 1,
      kanjis: [],
      ttl: 0,
      maxPage: 1,
      loading: true,
    });

    const getKanjis = async (lvl, curPage = 1) => {
      state.kanjis = [];
      state.loading = true;
      const { data } = await api.get(
        `/kanji_by_jlpt/?jlpt=${lvl}&page=${curPage}`
      );
      state.activeLevel = lvl;
      state.page = curPage;
      state.kanjis = data.results.map((k) => ({ id: k._id, ...k._source }));
      state.maxPage = Math.ceil(data.total / data.page_size);
      state.ttl = data.total;
      state.loading = false;
    };

    onMounted(() => {
      getKanjis(5);
    });

    return { getKanjis, ...toRefs(state) };
  },
};
</script>

<style lang="scss">
#filtered-jlpt {
  padding: 20px;
  .filters {
    margin-left: 20px;
    margin-bottom: 20px;
    > span {
      cursor: pointer;
    }
  }
  .kanjis-list {
    display: flex;
    flex-wrap: wrap;
    justify-content: space-around;
    align-items: strech;
    margin-left: -15px;
  }
}
</style>
