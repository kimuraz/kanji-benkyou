<template>
  <a-tag @click="$emit('click')" class="jlpt-level" :color="active ? color : 'grey'"> JLPT N{{ level }} </a-tag>
</template>

<script>
import { computed } from 'vue';
export default {
  name: 'JlptBadge',
  emits: ['click'],
  props: {
    level: {
      type: Number,
      required: true,
    },
    active: {
      type: Boolean,
      required: false,
      default: true,
    },
  },
  setup(props) {
    const COLORS = ['purple', 'blue', 'cyan', 'green', 'lime'];
    const color = computed(() => COLORS[props.level - 1]);

    return {
      color,
    };
  },
};
</script>

<style lang="scss">
.jlpt-level {
  font-size: 1rem;
}
</style>
