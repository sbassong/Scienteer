<template>
  <div class="q-pa-md row items-center q-gutter-md .card-wrapper">
    <q-card class="my-card">
      <q-card-section class="bg-purple text-white">
        <div class="text-h6">Ready to join the Scienteer community?</div>
      </q-card-section>

      <q-card-actions align="around">
        <q-btn color="white" text-color="black" label="Sign up" />
        <q-btn to="/login" color="primary" glossy label="Sign in" />
      </q-card-actions>
    </q-card>
  </div>
</template>

<script>
export default {
  setup() {
    return {
      lorem: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.'
    };
  },
};
</script>

<style lang="sass" scoped>
.my-card
  width: 100%
  max-width: 400px
</style>
