<template>
  <v-container class='researchers' fluid fill-height>

    <v-row>
      <v-col v-for="researcher in researchers" :key="researcher.id" cols="4">
        <ResearcherCard @click='selectresearcher(researcher)' :researcher='researcher' />
      </v-col>
    </v-row>

  </v-container>
</template>


<script>
import ResearcherCard from '../components/ResearcherCard.vue'

export default {
  name: 'ResearchersList',
  components: {
    ResearcherCard
  },
  data: () => ({
    Researchers: null
  }),
  mounted() {

  },
  methods: {
    selectResearcher(researcher_id) {
      this.$router.push(`/researcher/${researcher_id}`)
    },
  }
}
</script>

<style scoped>

</style>