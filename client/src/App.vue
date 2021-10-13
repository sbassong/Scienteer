<template>
  <v-app>
    <v-app-bar>
      <Nav />
    </v-app-bar>

    <v-main>
      <router-view> </router-view> 
    </v-main>
  </v-app>
</template>

<script>

import Nav from './components/Nav.vue'

export default {
  name: 'App',
  components: {
    Nav
  },

  data: () => ({
    //
  }),
};
</script>

<style scoped>
a {
    text-decoration: none;
  }
</style>