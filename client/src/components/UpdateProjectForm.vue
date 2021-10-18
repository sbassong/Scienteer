<template>
  <v-card class="mx-auto px-5 " align='center' justify='center' width='700' height="auto">
  <v-card-title class="justify-center">Update project form</v-card-title>
  <form >
    <v-text-field v-model="title" label="Project Title" @change="$v.title.$touch()" @blur="$v.title.$touch()" filled shaped ></v-text-field>
    <!-- <v-select v-model="select" :items="categories" :error-messages="selectErrors" label="Project Category" required  @change="$v.select.$touch()" @blur="$v.select.$touch()"></v-select> -->
    <v-textarea v-model="requirements" label="Scienteer Requirements" @change="$v.requirements.$touch()" @blur="$v.requirements.$touch()" counter filled shaped full-width auto-grow ></v-textarea>
    <v-textarea v-model="instructions" label="Project Instructions"  @change="$v.instructions.$touch()" @blur="$v.instructions.$touch()" counter filled shaped full-width auto-grow ></v-textarea>
    <v-row align="center" justify="center"><v-btn class="mr-4 mb-5 mt-2" @click='handleSubmit'>Resubmit Project</v-btn></v-row>
  </form>
  </v-card>
</template>

<script>
import {UpdateProject, UpdateProjectImg} from '../services/project'
import {validationMixin} from 'vuelidate'
import {required} from 'vuelidate/lib/validators'
import { mapState } from 'vuex'

export default {
  name: 'UpdateProjectForm',
  mixins: [validationMixin],

  validations: {
    select: { required },
  },

  props: {
    project: Object
  },

  data: () => ({
    select: null,

    title: this.project.title || null,
    category: this.project.category || null,
    requirements: this.project.requirements || null,
    instructions: this.project.instructions || null,
    image: this.project.image || null,
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

      const imageBody = {
        image: this.image,
      }

      let formData = new FormData()
      formData.append("image" , imageBody["image"])

      const upPro = await UpdateProject(this.project.id, projectBody)

      const upProjImg = await UpdateProjectImg(upPro.id, formData)
      console.log(upProjImg)

      this.title = this.project.title
      this.category = this.project.category
      this.requirements = this.project.requirements
      this.instructions =  this.project.instructions
      this.image =  this.project.image 
      this.$router.push(`/project/${this.project.id}`)
    },

    whichCategory() {
      if (this.select === 'Ecology') return "Ecology"
      else if (this.select === 'Microbiology') return "Microbiology"
      else if (this.select === 'Marine Biology') return "Marine Biology"
      else return "Ornithology"
    }
  },

  computed: {
    selectErrors () {
      const errors = []
      if (!this.$v.select.$dirty) return errors
      !this.$v.select.required && errors.push('Item is required')
      return errors
    },

    ...mapState(['user', 'authenticated', 'projects']),
  }
}


</script>