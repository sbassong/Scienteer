<template>
  <v-card class="mx-auto px-5 " align='center' justify='center' width='700' height="auto">
    <v-card-title class="justify-center">Update Report</v-card-title>
    <form >
      <v-textarea v-model="content" label="Report content" @change="$v.content.$touch()" @blur="$v.content.$touch()" counter filled shaped full-width auto-grow ></v-textarea>
      <v-text-field v-model="location" label="Location" @change="$v.location.$touch()" @blur="$v.location.$touch()" filled shaped ></v-text-field>
      <v-file-input v-model='image'  label="Images" @change="$v.image.$touch()" @blur="$v.image.$touch()" accept="image/*" prepend-icon="mdi-camera" multiple></v-file-input>
      <v-row align="center" justify="center"><v-btn class="mr-4 mb-5 mt-2" @click='handleSubmit'>Resubmit Report</v-btn></v-row>
    </form>
  </v-card>
</template>

<script>
import {UpdateReport} from '../services/report'
import { mapState } from 'vuex'

export default {
  name: 'UpdateReportForm',

  props: {
    report: Object
  },

  data: () => ({
    content: this.report.content || null,
    location: this.report.location || null,
    image: this.report.image || null,
  }),

  methods: {
    async handleSubmit(event) {
      event.preventDefault()
      const reportBody = {
        content: this.content,
        location: this.location,
        image: this.image,
        user_id: this.report.user_id,
        project_id: this.report.project.id
      }
      await UpdateReport(this.report.id, reportBody)
      this.content = this.report.content || null
      this.location = this.report.location || null
      this.image = this.report.image || null
      this.$router.push(`/report/${this.report.id}`)
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
