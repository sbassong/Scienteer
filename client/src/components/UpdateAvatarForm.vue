<template>
  <v-card class="mx-auto px-5 " align='center' justify='center' width='700' height="auto">
    <v-card-title class="justify-center">Update Avatar</v-card-title>
    <form >
      <v-file-input v-model='avatar' label="Avatar" @change="$v.avatar.$touch()" @blur="$v.avatar.$touch()" accept="image/*" prepend-icon="mdi-camera"></v-file-input>
      <v-row align="center" justify="center"><v-btn class="mr-4 mb-5 mt-2" @click='handleSubmit'>Submit Avatar</v-btn></v-row>
    </form>
  </v-card>
</template>

<script>
import {UpdateAvatar} from '../services/user'
import { mapState } from 'vuex'

export default {
  name: 'UpdateAvatarForm',

  data: () => ({
    avatar: ''
  }),

  methods: {
    async handleSubmit(event) {
      event.preventDefault()
      let avatarBody = new FormData()
      avatarBody.append('avatar', this.avatar)
      const res = await UpdateAvatar(this.user.id, avatarBody)
      console.log(res)
      this.avatar = ''
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

