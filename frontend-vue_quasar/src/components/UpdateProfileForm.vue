<template>
  <v-card class="mx-auto px-5 " align='center' justify='center' width='700' height="auto">
    <v-card-title class="justify-center">Update Profile</v-card-title>
    <form >
      <v-text-field v-model="name" label="Name" @change="$v.name.$touch()" @blur="$v.name.$touch()"></v-text-field>
      <v-text-field v-model="email" label="Email" @change="$v.email.$touch()" @blur="$v.email.$touch()"></v-text-field>
      <v-text-field v-model="bio" label="Bio" @change="$v.bio.$touch()" @blur="$v.bio.$touch()"></v-text-field>
      <v-row align="center" justify="center"><v-btn class="mr-4 mb-5 mt-2" @click='handleSubmit'>Update Profile</v-btn></v-row>
    </form>
  </v-card>
</template>

<script>
import {UpdateProfile} from '../services/user'
import { mapState } from 'vuex'

export default {
  name: 'UpdateProfileForm',

  data: () => ({
    name: this.user.name || null,
    email: this.user.email || null,
    bio: this.user.bio || null,
  }),

  methods: {
    async handleSubmit(event) {
      event.preventDefault()
      const profileBody = {
        name: this.name,
        email: this.email,
        bio: this.bio,
      }
      await UpdateProfile(this.user.id, profileBody)
      this.name = this.user.name || null
      this.email = this.user.email || null
      this.bio = this.user.bio || null
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

