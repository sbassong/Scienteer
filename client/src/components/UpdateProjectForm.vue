<template>
  <form >
    <v-text-field v-model="title" label="Project Title" @change="$v.title.$touch()" @blur="$v.title.$touch()" filled shaped ></v-text-field>
    <v-divider></v-divider>
    <v-select v-model="category" :categories="categories" :error-messages="selectErrors" label="Project Category"  @change="$v.category.$touch()" @blur="$v.category.$touch()"></v-select>
    <v-divider></v-divider>
    <v-textarea v-model="requirements" label="Scienteer Requirements" @change="$v.requirements.$touch()" @blur="$v.requirements.$touch()" counter filled shaped full-width auto-grow ></v-textarea>
    <v-divider></v-divider>
    <v-textarea v-model="instructions" label="Project Instructions"  @change="$v.instructions.$touch()" @blur="$v.instructions.$touch()" counter filled shaped full-width auto-grow ></v-textarea>
    <v-btn class="mr-4" @click='handleSubmit'>Resubmit Project</v-btn>
  </form>
</template>

<script>
import {UpdateProject} from '../services/project'

export default {
  name: 'UpdateProjectForm',

  data: () => ({
    title: referenced_project.title || null,
    category: referenced_project.category || null,
    requirements: referenced_project.requirements || null,
    instructions: referenced_project.instructions || null,
    current_user: null, //store current user here, then key into attr you need
    categories: ['Ecology', 'Microbiology', 'Marine Biology', 'Ornithology'],
    referenced_project: null //store project here, will come from store or parent component
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
      await UpdateProject(referenced_project.id, projectBody)
      this.title = referenced_project.title || null
      this.category = referenced_project.category || null
      this.requirements = referenced_project.requirements || null
      this.instructions =  referenced_project.instructions || null
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