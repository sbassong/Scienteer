<template>
  <v-container class='home' fluid fill-height>
    <WelcomeCard />
  </v-container>
</template>

<script>
import WelcomeCard from '../components/WelcomeCard.vue' 
export default {
  name: 'Home',
  components: {
    WelcomeCard
  }
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

