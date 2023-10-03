<template>
  <v-app-bar app color="accent" flat v-if="user && authenticated">
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

  <v-app-bar app color="secondary" flat v-else>
      <router-link to='/'><v-img class="mr-3" src="https://i.imgur.com/fOsxALqm.png" height="64px" width="140px"></v-img></router-link>
      <v-tabs centered  class="ml-n9" color="purple darken-1">
        <v-tab><router-link to='/'><h2>Home</h2></router-link></v-tab>
        <v-tab><router-link to='/projects'><h2>Projects</h2></router-link></v-tab>
        <v-tab><router-link to='/researchers'><h2>Researchers</h2></router-link></v-tab>
        <v-tab><router-link to='/about'><h2>About</h2></router-link></v-tab>
      </v-tabs>
      <router-link to='/users/register'><h3>Join Us!</h3></router-link>

  </v-app-bar>
</template>


<script>
import { mapActions, mapState } from 'vuex'

export default {
  name: 'Nav',

  methods: {
    ...mapActions(['setUser', 'toggleAuthenticated']),

    async handleLogOut() {
      this.setUser(null)
      this.toggleAuthenticated(false)
      localStorage.clear()
      this.$router.push('/')
    },
  },

  computed: {
    ...mapState({
      user: state => state.user,
      authenticated: state => state.authenticated
    }),
  }
}
</script>

<style scoped>
h3 { width:15%; }
a { text-decoration:none; font-weight: bold ;}




</style>