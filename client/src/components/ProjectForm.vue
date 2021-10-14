<template>
  <form >
    <v-text-field v-model="title" label="Project Title" @change="$v.title.$touch()" @blur="$v.title.$touch()" required filled shaped ></v-text-field>
    <v-divider></v-divider>
    <v-select v-model="category" :categories="categories" :error-messages="selectErrors" label="Project Category" required @change="$v.category.$touch()" @blur="$v.category.$touch()"></v-select>
    <v-divider></v-divider>
    <v-textarea v-model="requirements" label="Scienteer Requirements" required @change="$v.requirements.$touch()" @blur="$v.requirements.$touch()" counter filled shaped full-width auto-grow ></v-textarea>
    <v-divider></v-divider>
    <v-textarea v-model="instructions" label="Project Instructions" required @change="$v.instructions.$touch()" @blur="$v.instructions.$touch()" counter filled shaped full-width auto-grow ></v-textarea>
    <v-row align="center" justify="center"><v-btn class="mr-4" @click='handleSubmit'>Submit Project</v-btn></v-row>
  </form>
</template>

<script>
import {CreateProject} from '../services/project'


export default {
  name: 'ProjectForm',

  data: () => ({
    title: '',
    category: null,
    requirements: '',
    instructions: '',
    current_user: null, //store current user here, then key into attr you need
    categories: ['Ecology', 'Microbiology', 'Marine Biology', 'Ornithology']
  }),

  methods: {
    async handleSubmit(event) {
      event.preventDefault()
      const projectBody = {
        title: this.title,
        category: this.category,
        requirements: this.requirements,
        instructions: this.instructions,
        // user_id: this.current_user.id,
      }
      await CreateProject(projectBody)
      this.title = ''
      this.category = null
      this.requirements = '' 
      this.instructions = '' 
      // this.current_user = null
      // this.$router.push(`/project/${res.data.id}`)
    }
  },
  computed: {
    selectErrors () {
      const errors = []
      if (!this.$v.category.$dirty) return errors
      !this.$v.category.required && errors.push('Item is required')
      return errors
    }
  }
}

</script>