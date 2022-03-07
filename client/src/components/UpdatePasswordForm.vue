<template>
  <v-card class="mx-auto px-5 " align='center' justify='center' width='700' height="auto">
    <v-card-title class="justify-center">Update Password</v-card-title>
    <form >
      <v-text-field v-model="old_password" label="Old Password" @change="$v.password.$touch()" @blur="$v.password.$touch()"></v-text-field>
      <v-text-field v-model="new_password" label="New Password" @change="$v.password.$touch()" @blur="$v.password.$touch()"></v-text-field>
      <v-text-field v-model="c_new_password" label="Confirm New Password" @change="$v.password.$touch()" @blur="$v.password.$touch()"></v-text-field>
      <v-row align="center" justify="center"><v-btn class="mr-4 mb-5 mt-2" @click='handleSubmit'>Update Password</v-btn></v-row>
    </form>
  </v-card>
</template>

<script>
import {UpdateUserPW} from '../services/user'
import { mapState } from 'vuex'

export default {
  name: 'UpdatePasswordForm',

  data: () => ({
    old_password: '',
    new_password: '',
    c_new_password: '',
  }),

  methods: {
    async handleSubmit(event) {
      event.preventDefault()
      const passwordBody = {
        old_password: this.old_password,
        new_password: this.new_password
      }
      const mess = await UpdateUserPW(this.user.id, passwordBody)
      console.log(mess)
      this.old_password = ''
      this.new_password = ''
      this.c_new_password = ''
      this.$router.push('/users/profile')
    }
  },

  computed: {
    ...mapState({
    user: state => state.user,
    authenticated: state => state.authenticated,
    }),
  },
}
</script>

