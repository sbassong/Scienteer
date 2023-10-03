<template>
    <div class="home">
      <WelcomeCard />
    </div>
</template>

<script>
import { defineComponent } from 'vue';
import WelcomeCard from '../components/WelcomeCard.vue';
// import { mapState } from 'vuex'

export default defineComponent({
  name: 'HomePage',
  components: {
    WelcomeCard,
  },

  data: () => ({
    items: [
      { src: '../assets/quasar-logo-vertical.svg' },
    ],
  }),

  // computed: mapState({
  // user: state => state.user,
  // authenticated: state => state.authenticated
  // }),
});

</script>

<style lang="scss" scoped>

</style>
