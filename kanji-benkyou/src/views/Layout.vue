<template>
  <a-layout>
    <a-layout-header> HEADER </a-layout-header>

    <a-layout-content
      :style="{ overflow: 'auto', minHeight: 'calc(100vh - 134px)' }"
    >
      <slot />
    </a-layout-content>

    <a-layout-footer :style="{ textAlign: 'center', borderTop: '1px solid #f0f2f5' }">
      KanjiBenkyou
    </a-layout-footer>
  </a-layout>
</template>

<script>
export default {
  name: 'Layout',
};
</script>

<style lang="sass"></style>
