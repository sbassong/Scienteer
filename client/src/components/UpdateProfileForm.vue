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

export default {
  name: 'UpdateProfileForm',

  data: () => ({
    name: current_user.name || null,
    email: current_user.email || null,
    bio: current_user.bio || null,
    // image: current_user.image || null', future addition to user table
    current_user: null //session user
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
      await UpdateProfile(current_user.id, profileBody)
      this.name = current_user.name || null
      this.email = current_user.email || null
      this.bio = current_user.bio || null
      // this.image = current_user.image || null
      this.$router.push('/users/profile')
    }
  },

  computed: {
    
  },
}
</script>

