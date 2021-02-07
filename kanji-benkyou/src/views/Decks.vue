<template>
  <div id="decks">
    <header>
      <a-button @click="showDeckForm = true">
        <plus-outlined />
        New Deck
      </a-button>
    </header>
    <main>
      <deck-form :visible="showDeckForm" @close="showDeckForm = false" />

      <deck-list />
    </main>
  </div>
</template>

<script>
import { ref } from 'vue';

import { PlusOutlined } from '@ant-design/icons-vue';

import DeckForm from '@/components/decks/DeckForm';
import DeckList from '@/components/decks/DeckList';

export default {
  name: 'Decks',
  components: {
    PlusOutlined,
    DeckForm,
    DeckList,
  },
  setup() {
    const showDeckForm = ref(false);

    return { showDeckForm };
  },
};
</script>

<style lang="scss">
#decks {
  padding: 20px;
  width: 60vw;
}

@media screen and (max-width: 812px) {
  width: 100vw;
}
</style>
