<template>
  <v-app id='app'>
    <Nav />
      <v-main >
        <router-view></router-view> 
      </v-main>
  </v-app>
</template>

<script>

import Nav from './components/Nav.vue'
import { CheckSession } from './services/auth'
import { GetAllUsers } from './services/user'
import { GetAllProjects } from './services/project'
import { GetAllReports } from './services/report'
import { mapActions, mapState } from 'vuex'

export default {
  name: 'App',
  components: {
    Nav
  },

  mounted() {
    
  },

  created() {
    console.log('this is created')
    this.getData()
    this.checkToken()
  },

  methods: {
    ...mapActions(['setUser','toggleAuthenticated', 'setUsers', 'setProjects', 'setReports']),

    async checkToken() {
      const token = await localStorage.getItem('token')
      if (token) {
        const sessionUser = await CheckSession(token)
        this.setUser(sessionUser)
        this.toggleAuthenticated(true)
        localStorage.setItem('authenticated', '1')
      }
    },

    async getData() {
      const users = await GetAllUsers()
      this.setUsers(users.data)
      const projects = await GetAllProjects()
      this.setProjects(projects.data)
      const reports = await GetAllReports()
      this.setReports(reports.data)
    } 
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

</style> >

