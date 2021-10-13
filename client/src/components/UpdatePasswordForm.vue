<template>
  <form >
    
    <v-text-field v-model="old_password" label="Password" @change="$v.password.$touch()" @blur="$v.password.$touch()"></v-text-field>
    <v-text-field v-model="old_password" label="Password" @change="$v.password.$touch()" @blur="$v.password.$touch()"></v-text-field>
    <v-text-field v-model="password" label="Password" @change="$v.password.$touch()" @blur="$v.password.$touch()"></v-text-field>
    <v-btn class="mr-4" @click='handleSubmit'>Update Password</v-btn>
  </form>
</template>

<script>
import {UpdateUserPW} from '../services/user'

export default {
  name: 'UpdatePasswordForm',

  data: () => ({
    old_password: '',
    new_password: '',
    c_new_password: '',
    current_user: null, //session user
  }),

  methods: {
    async handleSubmit(event) {
      event.preventDefault()
      const passwordBody = {
        old_password: this.old_password,
        new_password: this.new_password
      }
      await UpdateUserPW(passwordBody)
      this.old_password = ''
      this.new_password = ''
      this.c_new_password = ''
      this.$router.push('/users/profile')
    }
  },

  computed: {
    
  },
}
</script>

