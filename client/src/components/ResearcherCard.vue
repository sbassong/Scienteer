<template>
  <v-hover v-slot="{ hover }">
    <v-card class="mx-auto" max-width="344" @click='selectResearcher(researcher.id)'>

      <v-img :src="researcher.image ? researcher.image : 'https://cdn.vuetifyjs.com/images/cards/sunshine.jpg'" height="200px"></v-img>
      <v-card-title>{{researcher.name}}</v-card-title>

      <v-expand-transition>
        <div v-if="hover" class="d-flex transition-fast-in-fast-out orange darken-2 v-card--reveal text-h2 white--text" style="height: 100%;">{{researcher.bio}}</div>
      </v-expand-transition>

    </v-card>
  </v-hover>
</template>

<script>
export default {
  name: 'ResearcherCard',
  props: {
    researcher: Object
  },

  methods: {
    selectResearcher(researcher_id) {
      this.$router.push(`/researcher/${researcher_id}`)
    }
  },
}
</script>

<style scoped>

</style>