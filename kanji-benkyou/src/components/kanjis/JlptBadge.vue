<template>
  <a-tag class="jlpt-level" :color="color">
    JLPT {{ level }} 
  </a-tag>
</template>

<script>
import { computed } from 'vue';
export default {
  name: 'JlptBadge',
  props: {
    level: {
      type: Number,
      required: true,
    },
  },
  setup(props) {
    const COLORS = ['purple', 'blue', 'cyan', 'green', 'lime'];
    const color = computed(() => COLORS[props.level - 1]);

    return {
      color,
    }
  },
};
</script>

<style lang="scss">
.jlpt-level {
  font-size: 1rem;
}
</style>
