<template>
  <v-app-bar app color="white" flat v-if="user && authenticated">
      <router-link to='/'><v-img class="mr-3" src="https://i.imgur.com/fOsxALqm.png" height="64px" width="140px"></v-img></router-link>
      <v-tabs centered  class="ml-n9" color="purple darken-1">
        <v-tab><router-link to='/'><h2>Home</h2></router-link></v-tab>
        <v-tab><router-link to='/projects'><h2>Projects</h2></router-link></v-tab>
        <v-tab><router-link to='/researchers'><h2>Researchers</h2></router-link></v-tab>
        <v-tab><router-link to='/about'><h2>About</h2></router-link></v-tab>
        <v-tab><router-link to='/profile'><h2>Profile</h2></router-link></v-tab>
      </v-tabs>
      <h3>Welcome back {{user.name}}!</h3>
      <v-btn @click='handleLogOut' >Sign Out</v-btn>
  </v-app-bar>

  <v-app-bar app color="white" flat v-else>
      <router-link to='/'><v-img class="mr-3" src="https://i.imgur.com/fOsxALqm.png" height="64px" width="140px"></v-img></router-link>
      <v-tabs centered  class="ml-n9" color="purple darken-1">
        <v-tab><router-link to='/'><h2>Home</h2></router-link></v-tab>
        <v-tab><router-link to='/projects'><h2>Projects</h2></router-link></v-tab>
        <v-tab><router-link to='/researchers'><h2>Researchers</h2></router-link></v-tab>
        <v-tab><router-link to='/about'><h2>About</h2></router-link></v-tab>
      </v-tabs>
      <h3 @click="overlayRegister = !overlay">Join Us!</h3>

      <v-overlay :opacity="opacityRegister" :value="overlayRegister">
        <RegisterForm />
        <v-row align="center" justify="center"><v-btn  color="red" dark @click="overlayRegister = false">Cancel</v-btn></v-row>
      </v-overlay>

  </v-app-bar>
</template>


<script>
import { mapActions, mapState } from 'vuex'
import RegisterForm from './RegisterForm.vue'

export default {
  name: 'Nav',
  components: {
    RegisterForm
  },
  data:() => ({
    absoluteRegister: true,
    overlayRegister: false,
    opacityRegister: 0.8
  }),
  methods: {
    ...mapActions(['setUser', 'toggleAuthenticated']),

    async handleLogOut() {
      this.setUser(null)
      this.toggleAuthenticated(false)
      localStorage.clear()
      this.$router.push('/')
    },
  },

  computed: mapState({
    user: state => state.user,
    authenticated: state => state.authenticated
  }),
}
</script>

<style scoped>
h3 { width:15%; }
a { text-decoration:none; font-weight: bold ;}




</style>