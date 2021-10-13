<template>
  <form >
    <v-text-field v-model="name" placeholder="Enter name here" name='name' :error-messages="nameErrors" :counter="30" label="Name" required @change="$v.name.$touch()" @blur="$v.name.$touch()"></v-text-field>
    <v-text-field v-model="email" label="Email" :error-messages="emailErrors" placeholder="Enter email here" name='enail' required @change="$v.email.$touch()" @blur="$v.email.$touch()"></v-text-field>
    <v-text-field v-model="password" label="Password" required placeholder="Enter password here" name='password' @change="$v.password.$touch()" @blur="$v.password.$touch()"></v-text-field>
    <v-select v-model="select" :items="roles" :error-messages="selectErrors" label="Role" required @change="$v.select.$touch()" @blur="$v.select.$touch()"></v-select>
    <v-btn class="mr-4" @click='handleSubmit'>Register</v-btn>
  </form>
</template>

<script>
import {RegisterUser} from '../services/auth'
import {validationMixin} from 'vuelidate'
import {required, maxLength, email} from 'vuelidate/lib/validators'

export default {
  name: 'RegisterForm',
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
