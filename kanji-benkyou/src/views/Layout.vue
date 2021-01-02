<template>
  <a-layout>
    <a-layout-header> HEADER </a-layout-header>

    <a-layout-content>
      <slot />
    </a-layout-content>

    <a-layout-footer></a-layout-footer>
  </a-layout>
</template>

<script>
export default {
  name: 'Layout',
};
</script>

<style lang="sass"></style>
