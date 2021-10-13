<template>
  <form >
    <v-text-field v-model="email" label="Email" :error-messages="emailErrors" placeholder="Enter email here" name='enail' required @change="$v.email.$touch()" @blur="$v.email.$touch()"></v-text-field>
    <v-text-field v-model="password" label="Password" required placeholder="Enter password here" name='password' @change="$v.password.$touch()" @blur="$v.password.$touch()"></v-text-field>
    <v-btn class="mr-4" @click='handleSubmit'>Login</v-btn>
  </form>
</template>

<script>
import {LoginUser} from '../services/auth'
import {validationMixin} from 'vuelidate'
import {required, email} from 'vuelidate/lib/validators'

export default {
  name: 'LoginForm',
  mixins: [validationMixin],

  validations: {
    email: { required, email },
    password: { required },
  },

  data: () => ({
    email: '',
    password: ''
  }),

  methods: {
    async handleSubmit(event) {
      event.preventDefault()
      const loginBody = {
        email: this.email,
        password: this.password
      }
      await LoginUser(loginBody)
      this.email = ''
      this.password = ''
      this.$router.push('/')
    }
  },

  computed: {
    emailErrors () {
      const errors = []
      if (!this.$v.email.$dirty) return errors
      !this.$v.email.email && errors.push('Must be valid email')
      !this.$v.email.required && errors.push('Email is required')
      return errors
    },
  },
}
</script>

