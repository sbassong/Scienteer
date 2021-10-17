<template>
  <v-card class="mx-auto px-5 " align='center' justify='center' width='700' height="auto">
    <v-card-title class="justify-center">Report Builder</v-card-title>
    <form >
      <v-textarea v-model="content" label="Report content" required @change="$v.content.$touch()" @blur="$v.content.$touch()" counter filled shaped full-width auto-grow ></v-textarea>
      <v-text-field v-model="location" label="Location" @change="$v.location.$touch()" @blur="$v.location.$touch()" filled shaped ></v-text-field>
      <v-file-input v-model='image' label="Images" @change="$v.image.$touch()" @blur="$v.image.$touch()" accept="image/*" prepend-icon="mdi-camera" multiple></v-file-input>
      <v-row align="center" justify="center"><v-btn class="mr-4 mb-5 mt-2" @click='handleSubmit'>Submit Report</v-btn></v-row>
    </form>
  </v-card>
</template>

<script>
import {CreateReport} from '../services/report'
import { mapState } from 'vuex'

export default {
  name: 'ReportForm',

  props: {
    project: Object
  },

  data: () => ({
    content: '',
    location: null,
    image: null,
  }),

  methods: {
    async handleSubmit(event) {
      event.preventDefault()
      const reportBody = {
        content: this.content,
        location: this.location,
        image: this.image,
        user_id: this.user.id,
        project_id: this.project.id
      }
      await CreateReport(reportBody)
      this.content = ''
      this.location = null
      this.image = null 
      this.$router.push(`/project/${this.project.id}`)
    },

    computed: {
    ...mapState({
    user: state => state.user,
    authenticated: state => state.authenticated,
    }),
  }
  }
}

</script>
