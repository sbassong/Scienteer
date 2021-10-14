<template>
  <v-container v-if='user && authenticated' class='home' fluid fill-height>
    <v-carousel cycle>
      <v-carousel-item v-for="(item,i) in items" :key="i" :src="item.src" reverse-transition="fade-transition" transition="fade-transition"></v-carousel-item>
    </v-carousel>
  </v-container>

  <v-container v-else class='home' fluid fill-height>
    <WelcomeCard />
  </v-container>
</template>

<script>
import WelcomeCard from '../components/WelcomeCard.vue'
import { mapState } from 'vuex'

export default {
  name: 'Home',
  components: {
    WelcomeCard
  },

  data: () => ({
    items: [
      {src: 'https://i.imgur.com/UwdB6ms.jpg'},
      {src: 'https://i.imgur.com/j9hwy6v.jpg'},
      {src: 'https://i.imgur.com/k4pnH3c.jpg'}
    ]
  }),

  computed: mapState({
  user: state => state.user,
  authenticated: state => state.authenticated
  }),
}
</script>

<style scoped>
.home {
  background-image: url("https://i.imgur.com/H72Sdq7.jpg?1");
  background-position: center center;
  background-size:cover;
  background-color: transparent;
  background-repeat: no-repeat;
  position: relative;
  overflow: hidden;
}

</style>

