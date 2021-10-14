<template>
  <v-container class='project' fluid fill-height>
    <v-row align='center' justify='space-around'>
      <v-container>
        <v-img max-width="300" src="project image goes here"></v-img>
      </v-container>
      <v-container>
        <p>Requirements will go here</p>
      </v-container>
      <v-container>
        <p>Instructions go here</p>
      </v-container>
    </v-row>

    <v-container class='project-reports'>
      <v-row>
        <v-col v-for="report in project_reports" :key="report.id" cols="1">
          <ReportCard :report='report' />
        </v-col>
      </v-row>
    </v-container>

  </v-container>
</template>



<script>
import ReportCard from '../components/ReportCard'

export default {
  name: 'ProjectDetails',
  data: () => ({
    project: null,
    project_reports: null
  }),
  components: {
    ReportCard
  },
  mounted() {

  },
  methods: {
    
  }
}
</script>


<style scoped>

</style>