<template>

  <v-card class="mx-auto report-card" max-width="344" @click='selectReport(report.id)'>
    <v-img :src=" report.image ? report.image : 'https://cdn.vuetifyjs.com/images/cards/sunshine.jpg'" height="200px"></v-img>
    <v-card-title>{{report.user_id}}</v-card-title>
    <v-card-subtitle>{{report.content}}</v-card-subtitle>
  </v-card>

</template>


<script>
export default {
  name: 'ReportCard',
  props: {
    report: Object
  },

  methods: {
    selectReport(report_id) {
      this.$router.push(`/report/${report_id}`)
    }
  },
}
</script>

<style scoped>

</style>

