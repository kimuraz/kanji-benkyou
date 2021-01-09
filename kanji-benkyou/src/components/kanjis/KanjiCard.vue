<template>
  <a-card class="kanji-card">
    <template #cover>
      <h1>{{ kanji.kanji }}</h1>
    </template>

    <div class="data">
      <jlpt-badge v-if="kanji.jlpt" :level="kanji.jlpt" />
      <div>
        <a-tag color="gold">Grade: </a-tag>
        <a-tag>{{ kanji.grade || '-' }}</a-tag>
      </div>
      <div>
        <a-tag color="geekblue">Strokes: </a-tag>
        <a-tag>{{ kanji.stroke_count }}</a-tag>
        <info-circle-outlined
          :style="{ cursor: 'pointer' }"
          @click="showOrder = true"
        />
      </div>
      <div>
        <a-tag color="pink"> 訓(くん):</a-tag>
        <a-tag v-for="reading in kanji.kun_readings" :key="reading">
          {{ reading }}
        </a-tag>
        <a-tag v-if="!kanji.kun_readings.length"> ? </a-tag>
      </div>
      <div>
        <a-tag color="orange"> 音(おん):</a-tag>
        <a-tag v-for="reading in kanji.on_readings" :key="reading">
          {{ reading }}
        </a-tag>
        <a-tag v-if="!kanji.on_readings.length"> ? </a-tag>
      </div>
      <div>
        <a-tag color="volcano"> Meanings: </a-tag>
        <br />
        <a-tag v-for="meaning in kanji.meanings" :key="meaning">
          <span class="meaning">{{ meaning }}</span>
        </a-tag>
        <a-tag v-if="!kanji.meanings.length"> ? </a-tag>
      </div>
    </div>
  </a-card>
  <order-modal
    v-if="showOrder"
    :visible="showOrder"
    :kanji="kanji"
    @close="showOrder = false"
  />
</template>

<script>
import { ref } from 'vue';
import JlptBadge from './JlptBadge';
import { InfoCircleOutlined } from '@ant-design/icons-vue';
import OrderModal from './OrderModal';

export default {
  name: 'KanjiCard',
  components: {
    JlptBadge,
    InfoCircleOutlined,
    OrderModal,
  },
  props: {
    kanji: Object,
  },
  setup() {
    const showOrder = ref(false);

    return { showOrder };
  },
};
</script>

<style lang="scss" scoped>
.kanji-card {
  margin: 10px;
  width: 29vw;
  h1 {
    font-size: 5rem;
    text-align: center;
    margin: 0;
  }
  .data {
    > div {
      margin: 5px 0;
      width: fit-content;
    }
  }
  .meaning {
    text-transform: capitalize();
  }
}

@media screen and (max-width: 768px) {
  .kanji-card {
    width: 85vw;
  }
}
</style>
