<template>
  <form >
    <v-text-field v-model="title" label="Project Title" @change="$v.title.$touch()" @blur="$v.title.$touch()" filled shaped ></v-text-field>
    <v-select v-model="category" :categories="categories" :error-messages="selectErrors" label="Project Category"  @change="$v.category.$touch()" @blur="$v.category.$touch()"></v-select>
    <v-textarea v-model="requirements" label="Scienteer Requirements" @change="$v.requirements.$touch()" @blur="$v.requirements.$touch()" counter filled shaped full-width auto-grow ></v-textarea>
    <v-textarea v-model="instructions" label="Project Instructions"  @change="$v.instructions.$touch()" @blur="$v.instructions.$touch()" counter filled shaped full-width auto-grow ></v-textarea>
    <v-btn class="mr-4" @click='handleSubmit'>Resubmit Project</v-btn>
  </form>
</template>

<script>
import {UpdateProject} from '../services/project'
import { mapState } from 'vuex'

export default {
  name: 'UpdateProjectForm',

  props: {
    project: Object
  },

  data: () => ({
    title: this.project.title || null,
    category: this.project.category || null,
    requirements: this.project.requirements || null,
    instructions: this.project.instructions || null,
    categories: ['Ecology', 'Microbiology', 'Marine Biology', 'Ornithology'],
  }),

  methods: {
    async handleSubmit(event) {
      event.preventDefault()
      const projectBody = {
        title: this.title,
        category: this.category,
        requirements: this.requirements,
        instructions: this.instructions,
        user_id: this.project.user_id,
      }
      await UpdateProject(this.project.id, projectBody)
      this.title = this.project.title || null
      this.category = this.project.category || null
      this.requirements = this.project.requirements || null
      this.instructions =  this.project.instructions || null
      this.$router.push(`/project/${this.project.id}`)
    }
  },

  computed: {
    selectErrors () {
      const errors = []
      if (!this.$v.category.$dirty) return errors
      !this.$v.category.required && errors.push('Item is required')
      return errors
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