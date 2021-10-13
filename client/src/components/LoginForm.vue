<template>
  <form >
    <v-text-field v-model="email" label="Email" :error-messages="emailErrors" placeholder="Enter email here" name='enail' required @change="$v.email.$touch()" @blur="$v.email.$touch()"></v-text-field>
    <v-text-field v-model="password" label="Password" required placeholder="Enter password here" name='password' @change="$v.password.$touch()" @blur="$v.password.$touch()"></v-text-field>

    <v-btn class="mr-4" @click='handleSubmit'>Login</v-btn>

  </form>
</template>


<script>
import {LoginUser} from '../services/auth'

export default {
  name: 'LoginForm',
  data: () => ({
      valid: false,
      firstname: '',
      lastname: '',
      nameRules: [
        v => !!v || 'Name is required',
        v => v.length <= 10 || 'Name must be less than 10 characters',
      ],
      email: '',
      emailRules: [
        v => !!v || 'E-mail is required',
        v => /.+@.+/.test(v) || 'E-mail must be valid',
      ],
  }),
  methods: {
    handleChange(event) {
      this[event.target.name] = event.target.value
    },
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
  }
}
</script>

<script>
  export default {
    data: () => ({
      valid: false,
      firstname: '',
      lastname: '',
      nameRules: [
        v => !!v || 'Name is required',
        v => v.length <= 10 || 'Name must be less than 10 characters',
      ],
      email: '',
      emailRules: [
        v => !!v || 'E-mail is required',
        v => /.+@.+/.test(v) || 'E-mail must be valid',
      ],
    }),
  }
</script>