<template>
  <div>
    <q-page-sticky position="top-left" :offset="[18, 18]">
      <q-btn :to='backLink' fab text-color="black" icon='keyboard_arrow_left' color="default" />
    </q-page-sticky>
  </div>
</template>

<script>
import { defineComponent } from 'vue';

export default defineComponent({
  name: 'PreviousButton',
  props: {
    backLink: String,
  },

  data: () => ({
  }),
});
</script>

<style>

</style>
