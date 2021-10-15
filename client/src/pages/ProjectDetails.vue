<template>
  <v-container class='project' fluid fill-height>

    <v-row align='center' justify='space-around'>
      <v-container>
        <v-img max-width="300" src="project.image"></v-img>
      </v-container>

      <v-container>
        <p>{{project.requirements}}</p>
      </v-container>

      <v-container>
        <p>{{project.instructions}}</p>
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
import { GetProjectById} from '../services/project'
import { GetReportsByProjectId} from '../services/report'

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
    this.getProjectById()
    this.getReportsProjectId()
  },
  methods: {
    async getProjectById() {
      const res = await GetProjectById(this.$route.params.id)
      this.project = res.data
    },

    async getReportsProjectId() {
      const res = await GetReportsByProjectId(this.$route.params.id)
      this.project_reports = res.data
    }
  }

}
</script>


<style scoped>

</style>