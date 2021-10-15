<template>
  <v-container class='researchers' fluid fill-height>

    <v-row>
      <v-col v-for="researcher in getResearchers" :key="researcher.id" cols="4">
        <ResearcherCard @click='selectresearcher(researcher)' :researcher='researcher' />
      </v-col>
    </v-row>

  </v-container>
</template>


<script>
import { mapGetters } from 'vuex'
import ResearcherCard from '../components/ResearcherCard.vue'

export default {
  name: 'ResearchersList',
  components: {
    ResearcherCard
  },

  methods: {
    selectResearcher(researcher_id) {
      this.$router.push(`/researcher/${researcher_id}`)
    }
  },

  computed: {
    ...mapGetters(['getResearchers'])
  }
}
</script>

<style scoped>

</style>