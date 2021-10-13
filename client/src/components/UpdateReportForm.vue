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

export default {
  name: 'UpdateReportForm',

  data: () => ({
    content: referenced_report.content || null,
    location: referenced_report.location || null,
    image: referenced_report.image || null,
    current_user: null, //store current user here, then key into attr you need
    parent_project: null, //this should come as props from parent component or store. maybe it'll be whole project obj
    referenced_report: null // this should come from the store or parent container
  }),

  methods: {
    async handleSubmit(event) {
      event.preventDefault()
      const reportBody = {
        content: this.content,
        location: this.location,
        image: this.image,
        // user_id: this.current_user.id,
        // project_id: this.parent_project.id
      }
      await UpdateReport(reportBody)
      this.content = referenced_report.content || null
      this.location = referenced_report.location || null
      this.image = referenced_report.image || null
      // this.current_user = null
      // this.parent_project = null
      // this.$router.push(`/project/${parent_project.id}`)
    },
  
  }
}

</script>
