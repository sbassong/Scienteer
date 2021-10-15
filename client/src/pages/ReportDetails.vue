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

  </v-container>
</template>



<script>
import {GetReportById} from '../services/report'

export default {
  name: 'ReportDetails',
  components: {

  },

  data: () => ({
    report: null
  }),
  
  mounted() {
    this.getReportById()
  },
  methods: {
    async getReportById() {
      const report = await GetReportById(this.$route.params.report_id)
      this.report = report.data
    }
  }
}
</script>


<style scoped>

</style>