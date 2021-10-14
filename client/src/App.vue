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
import { mapActions, mapState } from 'vuex'

export default {
  name: 'App',
  components: {
    Nav
  },

  mounted() {
    const token = localStorage.getItem('token')
    if (token) this.checkToken(token)
  },

  methods: {
    ...mapActions(['setUser','toggleAuthenticated']),

    async checkToken(token) {
      const sessionUser = await CheckSession(token)
      this.setUser(sessionUser)
      this.toggleAuthenticated(true)
      localStorage.setItem('authenticated', '1')
    }
  },
  computed: mapState({
    user: state => state.user,
    authenticated: state => state.authenticated
  }),
};
</script>

<style scoped>

</style> >

