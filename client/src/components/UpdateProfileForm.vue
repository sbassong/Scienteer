<template>
  <form >
    <v-text-field v-model="name" label="Name" @change="$v.name.$touch()" @blur="$v.name.$touch()"></v-text-field>
    <v-text-field v-model="email" label="Email" @change="$v.email.$touch()" @blur="$v.email.$touch()"></v-text-field>
    <v-text-field v-model="bio" label="Bio" @change="$v.bio.$touch()" @blur="$v.bio.$touch()"></v-text-field>
    <!-- <v-text-field v-model="image" label="Image" @change="$v.image.$touch()" @blur="$v.image.$touch()"></v-text-field> -->
    <v-btn class="mr-4" @click='handleSubmit'>Update Profile</v-btn>
  </form>
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
    // image: this.user.image || null', future addition to user table
  }),

  methods: {
    async handleSubmit(event) {
      event.preventDefault()
      const profileBody = {
        name: this.name,
        email: this.email,
        bio: this.bio,
        // image: this.image 
      }
      await UpdateProfile(this.user.id, profileBody)
      this.name = this.user.name || null
      this.email = this.user.email || null
      this.bio = this.user.bio || null
      // this.image = this.user.image || null
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

