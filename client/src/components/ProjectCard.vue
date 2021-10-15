<template>
  <v-hover v-slot="{ hover }">
    <v-card class="mx-auto" max-width="344">

      <v-img :src="project.image ? project.image : 'https://cdn.vuetifyjs.com/images/cards/sunshine.jpg'" height="200px'"></v-img>
      <v-card-title>{{project.title}}</v-card-title>
      <v-card-subtitle>{{project.category}}</v-card-subtitle>

      <v-expand-transition>
        <div v-if="hover" class="d-flex transition-fast-in-fast-out orange darken-2 v-card--reveal text-h2 white--text" style="height: 100%;">{{project.requirements}}</div>
      </v-expand-transition>

    </v-card>
  </v-hover>
</template>


<script>
export default {
  name: 'ProjectCard',
  props: {
    project: Object
  }
}
</script>

<style scoped>

</style>

