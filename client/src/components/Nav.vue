<template>
  <v-app-bar app color="white" flat v-if="current_user && authenticated">
      <router-link to='/'><v-img class="mr-3" src="https://i.imgur.com/fOsxALqm.png" height="64px" width="140px"></v-img></router-link>
      <v-tabs centered  class="ml-n9 tabs-cont" color="grey darken-1">
        <v-tab><router-link to='/'><h2>Home</h2></router-link></v-tab>
        <v-tab><router-link to='/projects'><h2>Projects</h2></router-link></v-tab>
        <v-tab><router-link to='/researchers'><h2>Researchers</h2></router-link></v-tab>
        <v-tab><router-link to='/about'><h2>About</h2></router-link></v-tab>
        <v-tab><router-link to='/profile'><h2>Profile</h2></router-link></v-tab>
      </v-tabs>
      <h3>Welcome back {{current_user.name}}!</h3>
      <v-btn>Sign Out</v-btn>
  </v-app-bar>

  <v-app-bar app color="white" flat v-else>
      <router-link to='/'><v-img class="mr-3" src="https://i.imgur.com/fOsxALqm.png" height="64px" width="140px"></v-img></router-link>
      <v-tabs centered  class="ml-n9" color="grey darken-1">
        <v-tab><router-link to='/'><h2>Home</h2></router-link></v-tab>
        <v-tab><router-link to='/projects'><h2>Projects</h2></router-link></v-tab>
        <v-tab><router-link to='/researchers'><h2>Researchers</h2></router-link></v-tab>
        <v-tab><router-link to='/about'><h2>About</h2></router-link></v-tab>
      </v-tabs>
      <router-link to='/'><h3>Join Us!</h3></router-link>
      
  </v-app-bar>

</template>


<script>

export default {
  name: 'Nav',
  data:()=> ({
    current_user: null,
    authenticated: null,
  }),
  methods: {
    async LogUserOut() {

    }
  }
}
</script>

<style scoped>
h3 { width:15%; }
a { text-decoration:none; font-weight: bold ;}




</style>