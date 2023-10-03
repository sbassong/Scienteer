<template>
  <v-card class="mx-auto px-5 " align='center' justify='center' width='700' height="auto">
    <v-card-title class="justify-center">Project Builder</v-card-title>
    <form >
      <v-text-field v-model="title" label="Project Title" @change="$v.title.$touch()" @blur="$v.title.$touch()" required filled shaped ></v-text-field>
      <v-file-input v-model='image' label="Image" @change="$v.image.$touch()" @blur="$v.image.$touch()" accept="image/*" prepend-icon="mdi-camera"></v-file-input>
      <v-select v-model="select" :items="categories" :error-messages="selectErrors" label="Project Category" required @change="$v.select.$touch()" @blur="$v.select.$touch()"></v-select>
      <v-textarea v-model="requirements" label="Scienteer Requirements" required @change="$v.requirements.$touch()" @blur="$v.requirements.$touch()" counter filled shaped full-width auto-grow ></v-textarea>
      <v-textarea v-model="instructions" label="Project Instructions" required @change="$v.instructions.$touch()" @blur="$v.instructions.$touch()" counter filled shaped full-width auto-grow ></v-textarea>
      <v-row align="center" justify="center"><v-btn class="mr-4 mb-5 mt-2" @click='handleSubmit'>Submit Project</v-btn></v-row>
    </form>
  </v-card>
</template>

<script>
import {CreateProject, UpdateProjectImg} from '../services/project'
import {validationMixin} from 'vuelidate'
import {required} from 'vuelidate/lib/validators'
import { mapState } from 'vuex'


export default {
  name: 'ProjectForm',
  mixins: [validationMixin],

  validations: {
    select: { required },
  },

  data: () => ({
    select: null,

    title: '',
    category: null,
    requirements: '',
    instructions: '',
    image: '',
    categories: ['Ecology', 'Microbiology', 'Marine Biology', 'Ornithology']
  }),

  methods: {
    async handleSubmit(event) {
      event.preventDefault()

      const projectBody = {
        title: this.title,
        category: this.whichCategory(),
        requirements: this.requirements,
        instructions: this.instructions,
        user_id: this.user.id
      }

      const imageBody = {
        image: this.image,
      }

      let formData = new FormData()
      formData.append("image" , imageBody["image"])
    
      
      const createdProj = await CreateProject(projectBody)

      const updatedProj = await UpdateProjectImg(createdProj.id, formData)


      this.title = ''
      this.requirements = '' 
      this.instructions = '' 
      this.image = ''
      this.$router.push(`/project/${updatedProj.id}`)
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
      !this.$v.select.required && errors.push('category is required')
      return errors
    },

    ...mapState({
      user: state => state.user,
      authenticated: state => state.authenticated
    }),
  }
}

</script>