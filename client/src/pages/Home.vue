<template>
  <v-parallax dark
    src="https://cdn.vuetifyjs.com/images/backgrounds/vbanner.jpg">
    <v-row align="center" justify="center">
      <v-col class="text-center" cols="12">
        <WelcomeCard />
      </v-col>
    </v-row>
  </v-parallax>
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
  background-image: url("");
  background-position: center center;
  background-size: cover;
  /* height: 100%; */
  height: 100vh;
  background-color: transparent;
  background-repeat: no-repeat;
  background-size: 100% 100%;
  /* position: relative; */
  overflow-x: hidden;
}

</style>

