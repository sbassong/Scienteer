<template>
  <v-container class='project' fluid fill-height>

    <v-row align='center' justify='space-around'>
      <v-container>
        <v-img max-width="300" :src="project.image ? project.image : 'https://i.imgur.com/H72Sdq7.jpg?1'"></v-img>
      </v-container>

      <v-container>
        <p>{{project.requirements}}</p>
      </v-container>

      <v-container>
        <p>{{project.instructions}}</p>
      </v-container>
    </v-row>

    <v-container class='project-reports'>
      <v-row v-if='user.researcher === true && authenticated && user.id === project.user_id' align='center' justify='space-around'>
        <v-btn @click="overlayProject = !overlay">Edit Project</v-btn>
        <v-btn @click="deleteProject">Delete Project</v-btn>
      </v-row>
      <v-row v-if='user.researcher === false && authenticated' align='center' justify='space-around'>
        <v-btn @click="overlayReport = !overlay">Submit Report</v-btn>
      </v-row>
      <v-row>
        <v-col v-for="report in project_reports" :key="report.id" cols="1">
          <ReportCard @click='selectReport(report.id)' :report='report' />
        </v-col>
      </v-row>
    </v-container>

    <v-overlay :absolute="absoluteReport" :opacity='opacity' :value="overlayReport">
      <ReportForm :project="project"/>
      <v-row align="center" justify="center"><v-btn  color="red" dark @click="overlayReport = false">Cancel</v-btn></v-row>
    </v-overlay>

    <v-overlay :absolute="absoluteProject" :opacity='opacity' :value="overlayProject">
      <UpdateProjectForm :project="project"/>
      <v-row align="center" justify="center"><v-btn  color="red" dark @click="overlayProject = false">Cancel</v-btn></v-row>
    </v-overlay>
  </v-container>
</template>



<script>
import ReportCard from '../components/ReportCard'
import ReportForm from '../components/ReportForm.vue'
import UpdateProjectForm from '../components/UpdateProjectForm.vue'
import { GetProjectById, DeleteProject} from '../services/project'
import { GetReportsByProjectId} from '../services/report'
import { mapState } from 'vuex'

export default {
  name: 'ProjectDetails',
  data: () => ({
    project: null,
    project_reports: null,
  
    overlayProject: false,
    absoluteProject: true,
    overlayReport: false,
    absoluteReport: true,
    opacity: 0.8,
  }),
  components: {
    ReportCard,
    ReportForm,
    UpdateProjectForm
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
    },

    selectReport(report_id) {
      this.$router.push(`/report/${report_id}`)
    },

    async deleteProject() {
      await DeleteProject(this.project.id)
      this.$router.push(`/projects`)
    },
  },

  computed: {
    ...mapState({
    user: state => state.user,
    authenticated: state => state.authenticated,
    }),
  }

}
</script>


<style scoped>

</style>