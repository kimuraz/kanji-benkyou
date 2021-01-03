<template>
  <a-card class="kanji-card">
    <template #cover>
      <h1>{{ kanji.kanji }}</h1>
    </template>

    <div class="data">
      <div>
        <a-tag color="gold">grade: </a-tag>
        <a-tag>{{ kanji.grade || '-' }}</a-tag>
      </div>
      <div>
        <a-tag color="geekblue">Strokes: </a-tag>
        <a-tag>{{ kanji.stroke_count }}</a-tag>
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
</template>

<script>
export default {
  name: 'KanjiCard',
  props: {
    kanji: {
      type: Object,
      required: true,
    },
  },
};
</script>

<style lang="scss" scoped>
.kanji-card {
  margin: 10px;
  width: 29vw;
  h1 {
    font-size: 4rem;
    text-align: center;
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
