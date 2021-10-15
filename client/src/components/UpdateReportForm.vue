<template>
  <form >
    <v-textarea v-model="content" label="Report content" @change="$v.content.$touch()" @blur="$v.content.$touch()" counter filled shaped full-width auto-grow ></v-textarea>
    <v-divider></v-divider>
    <v-text-field v-model="location" label="Location" @change="$v.location.$touch()" @blur="$v.location.$touch()" filled shaped ></v-text-field>
    <v-divider></v-divider>
    <v-file-input v-model='image'  label="Images" @change="$v.image.$touch()" @blur="$v.image.$touch()" accept="image/*" prepend-icon="mdi-camera" multiple></v-file-input>
    <v-divider></v-divider>
    <v-btn class="mr-4" @click='handleSubmit'>Resubmit Report</v-btn>
  </form>
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
