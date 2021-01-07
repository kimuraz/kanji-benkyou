<template>
  <a-modal :visible="visible" @cancel="$emit('close')" @ok="save" title="Deck">
    <a-form ref="deckForm" :model="form" :rules="rules">
      <a-form-item ref="name" label="Name" name="name">
        <a-input v-model:value="form.name" />
      </a-form-item>

      <a-form-item ref="description" label="Description" name="description">
        <a-input v-model:value="form.description" />
      </a-form-item>
    </a-form>
  </a-modal>
</template>

<script>
import { ref, reactive } from 'vue';
import { useStore } from 'vuex';

export default {
  name: 'DeckForm',
  emits: ['close'],
  setup(props, { emit }) {
    const deckForm = ref(null);
    const store = useStore();
    const visible = ref(props.visible);
    const form = reactive({
      name: '',
      description: '',
    });

    const rules = {
      name: [
        {
          required: true,
          message: 'Please fill the deck name',
          trigger: 'blur',
        },
        { min: 1, max: 100, message: 'Max length is 100', trigger: 'blur' },
      ],
    };

    const save = async () => {
      try {
        await deckForm.value.validate();
        await store.dispatch('newDeck', form);
        emit('close');
      } catch (err) {
        console.error(err);
      }
    };

    return { rules, form, deckForm, save, visible };
  },
};
</script>
