<template>
  <a-card class="kanji-card">
    <template #cover>
      <h1>{{ kanji.kanji }}</h1>
    </template>

    <div class="data">
      <jlpt-badge v-if="kanji.jlpt" :level="kanji.jlpt" />
      <a-button
        class="top-right"
        type="primary"
        shape="circle"
        :size="size"
        :loading="generatingPDF"
        @click="genPDF"
      >
        <template #icon>
          <download-outlined />
        </template>
        <a
          :href="pdfURL"
          v-show="false"
          ref="pdfLink"
          v-if="pdfURL"
          target="_blank"
          download
          @click.stop
        />
      </a-button>
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
        <a-tag v-if="!kanji.kun_readings || !kanji.kun_readings.length">
          ?
        </a-tag>
      </div>
      <div>
        <a-tag color="orange"> 音(おん):</a-tag>
        <a-tag v-for="reading in kanji.on_readings" :key="reading">
          {{ reading }}
        </a-tag>
        <a-tag v-if="!kanji.on_readings || !kanji.on_readings.length">
          ?
        </a-tag>
      </div>
      <div>
        <a-tag color="volcano"> Meanings: </a-tag>
        <br />
        <a-tag v-for="meaning in kanji.meanings" :key="meaning">
          <span class="meaning">{{ meaning }}</span>
        </a-tag>
        <a-tag v-if="!kanji.meanings || !kanji.meanings.length"> ? </a-tag>
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
import { notification } from 'ant-design-vue';
import { InfoCircleOutlined, DownloadOutlined } from '@ant-design/icons-vue';

import JlptBadge from './JlptBadge';
import OrderModal from './OrderModal';

import api from '@/api';

export default {
  name: 'KanjiCard',
  components: {
    DownloadOutlined,
    InfoCircleOutlined,
    JlptBadge,
    OrderModal,
  },
  props: {
    kanji: Object,
  },
  setup(props) {
    const showOrder = ref(false);
    const pdfLink = ref();
    const pdfURL = ref('');
    const generatingPDF = ref(false);
    const genPDF = async () => {
      generatingPDF.value = true;
      try {
        const { data } = await api.get(
          `/kanji_pdf/?kanji=${props.kanji.kanji}`
        );
        pdfURL.value = data.url;
        setTimeout(() => {
          pdfLink.value.click();
        }, 200);
      } catch (err) {
        console.log(err);
        if (err?.response?.status === 404) {
          notification.error({
            message: 'Error',
            description: 'Kanji pdf file not found.',
          });
        }
      } finally {
        generatingPDF.value = false;
      }
    };

    return { showOrder, pdfLink, generatingPDF, genPDF, pdfURL };
  },
};
</script>

<style lang="scss" scoped>
.kanji-card {
  margin: 10px;
  width: 22vw;
  position: relative;
  .top-right {
    position: absolute;
    top: 10px;
    right: 10px;
  }
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
