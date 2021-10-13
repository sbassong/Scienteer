<template>
  <v-hover v-slot="{ hover }">
    <v-card class="mx-auto" max-width="344">

      <v-img src="https://cdn.vuetifyjs.com/images/cards/sunshine.jpg" height="200px"></v-img>
      <v-card-title>Researcher Name goes here</v-card-title>

      <v-expand-transition>
        <div v-if="hover" class="d-flex transition-fast-in-fast-out orange darken-2 v-card--reveal text-h2 white--text" style="height: 100%;"> Bio goes here</div>
      </v-expand-transition>

    </v-card>
  </v-hover>
</template>

<script>
export default {
  name: 'ResearcherCard',
  props: {

  }
}
</script>

<style scoped>

</style>