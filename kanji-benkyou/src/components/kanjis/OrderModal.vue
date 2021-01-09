<template>
  <a-modal
    :title="kanji.kanji"
    :visible="visible"
    @ok="$emit('close')"
    :closable="false"
  >
    <div style="text-align: center">
      <img v-if="kanjiImg" :src="kanjiImg" style="height: 28vh;"/>
      <a-alert
        v-if="error"
        :message="error"
        description="We are already recording this error to improve in a near future! Usually this error is caused because it's a very uncommon kanji!"
        type="error"
        show-icon
      />
    </div>

    <template #footer>
      <a-button type="primary" @click="$emit('close')"> OK </a-button>
    </template>
  </a-modal>
</template>

<script>
import { ref, onMounted } from 'vue';
import api from '@/api';

export default {
  name: 'OrderModal',
  emits: ['close'],
  props: {
    kanji: Object,
    visible: Boolean,
  },
  setup(props) {
    let kanjiImg = ref(null);
    let loading = ref(true);
    let error = ref(null);

    onMounted(async () => {
      try {
        const { data } = await api.get(
          `/kanji_order/?kanji=${props.kanji.kanji}`
        );
        kanjiImg.value = data.svg;
        loading.value = false;
      } catch (e) {
        console.error(e);
        error.value = `Order for kanji: ${props.kanji.kanji} not found!`;
      }
    });

    return { loading, kanjiImg, error };
  },
};
</script>

<style lang="sass"></style>
