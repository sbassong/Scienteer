<template>
  <v-container fluid fill-height>
    <v-card class="mx-auto px-5 " align='center' justify='center' width='700' height="auto">
      <v-card-title class="justify-center">Register Form</v-card-title>
      <form>
        <v-text-field v-model="name" label="Name" required :error-messages="nameErrors" :counter="30"   @change="$v.name.$touch()" @blur="$v.name.$touch()"></v-text-field>
        <v-text-field v-model="email" label="Email" required :error-messages="emailErrors"  @change="$v.email.$touch()" @blur="$v.email.$touch()"></v-text-field>
        <v-text-field v-model="password" label="Password" required  @change="$v.password.$touch()" @blur="$v.password.$touch()"></v-text-field>
        <v-text-field v-model="c_password" label="Confirm Password" required  @change="$v.c_password.$touch()" @blur="$v.c_password.$touch()"></v-text-field>
        <v-select v-model="select" :items="roles" :error-messages="selectErrors" label="Role" required @change="$v.select.$touch()" @blur="$v.select.$touch()"></v-select>
        
        <v-row align="center" justify="center">
          <v-btn class="mr-4 mb-5 mt-2" @click='handleSubmit'  v-if='password !== c_password' disabled>Register</v-btn>
          <v-btn class="mr-4 mb-5 mt-2" @click='handleSubmit'  v-else>Register</v-btn>
        </v-row>
      </form>
    </v-card>
</v-container>
</template>

<script>
import {RegisterUser} from '../services/auth'
import {validationMixin} from 'vuelidate'
import {required, maxLength, email} from 'vuelidate/lib/validators'

export default {
  name: 'RegisterFormPage',
  mixins: [validationMixin],

  validations: {
    name: { required, maxLength: maxLength(30) },
    email: { required, email },
    password: { required },
    select: { required },
  },

  data: () => ({
    name: '',
    email: '',
    password: '',
    c_password: '',
    select: null,
    researcher: null,
    roles: ["Scienteer", "Researcher"]
  }),

  methods: {
    async handleSubmit(event) {
      event.preventDefault()
      const userBody = {
        name: this.name,
        email: this.email,
        password: this.password,
        researcher: this.scienteerOrNo()
      }
      await RegisterUser(userBody)
      this.name = ''
      this.email = ''
      this.password = '' 
      this.researcher = null
      this.$router.push('/users/login')
    },

    scienteerOrNo() {
      if (this.selected === 'Scienteer') return false
      return true
      
  },

  computed: {
    selectErrors () {
      const errors = []
      if (!this.$v.select.$dirty) return errors
      !this.$v.select.required && errors.push('Item is required')
      return errors
    },
    nameErrors () {
      const errors = []
      if (!this.$v.name.$dirty) return errors
      !this.$v.name.maxLength && errors.push('Name must be at most 10 characters long')
      !this.$v.name.required && errors.push('Name is required.')
      return errors
    },
    emailErrors () {
      const errors = []
      if (!this.$v.email.$dirty) return errors
      !this.$v.email.email && errors.push('Must be valid email')
      !this.$v.email.required && errors.push('Email is required')
      return errors
    },
  },
}
}
</script>
