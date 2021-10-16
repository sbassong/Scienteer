<template>
  <v-container class='researchers' fluid fill-height>

    <v-row>
      <v-col v-for="researcher in getResearchers" :key="researcher.id" cols="4">

        <ResearcherCard :researcher='researcher' />

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

  computed: {
    ...mapGetters(['getResearchers'])
  }
}
</script>

<style scoped>

</style>