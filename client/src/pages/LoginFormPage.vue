<template>
  <v-container fluid fill-height>
    <v-card class="mx-auto px-5" width='600' height="auto">
    <v-card-title class="justify-center">Login Form</v-card-title>
      <form>
        <v-text-field v-model="email" label="Email" :error-messages="emailErrors" placeholder="Enter email here" name='enail' required @change="$v.email.$touch()" @blur="$v.email.$touch()"></v-text-field>
        <v-text-field v-model="password" label="Password" required placeholder="Enter password here" name='password' @change="$v.password.$touch()" @blur="$v.password.$touch()"></v-text-field>
        <v-row align="center" justify="center">
          <v-btn class="mr-4 mb-5 mt-2" @click='handleSubmit'>Login</v-btn>
        </v-row>
      </form>
    </v-card>
  </v-container>
</template>

<script>
import {LoginUser} from '../services/auth'
import {validationMixin} from 'vuelidate'
import {required, email} from 'vuelidate/lib/validators'
import {mapState, mapActions} from 'vuex'

export default {
  name: 'LoginFormPage',
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
    ...mapActions(['setUser','toggleAuthenticated']),

    async handleSubmit(event) {
      event.preventDefault()
      const loginBody = {
        email: this.email,
        password: this.password
      }
      const payload = await LoginUser(loginBody)
      this.setUser(payload)
      this.toggleAuthenticated(true)
      // this.$router.push('/profile')
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

    computed: {
    ...mapState({
      user: state => state.user,
      authenticated: state => state.authenticated
    }),
  }
  },
}
</script>

