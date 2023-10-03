<template>
  <v-container class='report' fluid fill-height>

      <v-container>
        <p class="font-weight-bold">Content</p>
        <p class="font-weight-regular">{{report.content}}</p>
      </v-container>

      <v-container>
        <p class="font-weight-bold">Location</p>
        <p class="font-weight-regular">{{report.location}}</p>
      </v-container>

      <v-container>
        <p class="font-weight-bold">Image</p>
        <v-img max-width="300" :src="report.image"></v-img>
      </v-container>

      <v-row v-if='user.researcher === false && authenticated && user.id === report.user_id' align='center' justify='space-around'>
        <v-btn @click="overlayReport = !overlay">Edit Report</v-btn>
        <v-btn @click="deleteReport">Delete Report</v-btn>

      </v-row>

      <v-overlay :absolute="absoluteReport" :opacity='opacity' :value="overlayReport">
          <UpdateReportForm :report="report"/>
          <v-row align="center" justify="center"><v-btn  color="red" dark @click="overlayReport = false">Cancel</v-btn></v-row>
    </v-overlay>
  </v-container>
</template>



<script>
import {GetReportById, DeleteReport} from '../services/report'
import UpdateReportForm from '../components/UpdateReportForm.vue'
import { mapState } from 'vuex'

export default {
  name: 'ReportDetails',
  components: {
    UpdateReportForm
  },

  data: () => ({
    report: null,
    overlayReport: false,
    absoluteReport: true,
    opacity: 0.8,
  }),
  
  mounted() {
    this.getReportById()
  },
  methods: {
    async getReportById() {
      const report = await GetReportById(this.$route.params.report_id)
      this.report = report.data
    },

    async deleteReport() {
      await DeleteReport(this.report.id)
      this.$router.push(`/project/${this.report.project_id}`)
    }
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