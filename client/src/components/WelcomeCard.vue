<template>
  <v-hover v-slot="{ hover }">
    <v-card shaped class="mx-auto" max-width="40%" max-height="300">

      <v-card-text>
        <v-card-title class="justify-center"><h2>Ready to join the network? Hover over here!</h2></v-card-title>
      </v-card-text >

      <v-expand-transition>
        <v-card-text>
        <v-row v-if="hover" align="center" justify="space-around" class="d-flex transition-fast-in-fast-out darken-2 v-card--reveal text-h2 " style="height: 100%;">
          <v-btn @click="overlayRegister = !overlay" color='primary' class='mb-5' rounded>Create account!</v-btn>
          <v-btn @click="overlayLogin = !overlay" color='accent' class='mb-5' dark rounded>Have an account?</v-btn>
        </v-row>

        <v-overlay :absolute="absoluteRegister" :opacity='opacity' :value="overlayRegister">
          <RegisterForm />
          <v-row align="center" justify="center"><v-btn  color="red" dark @click="overlayRegister = false">Cancel</v-btn></v-row>
        </v-overlay>

        <v-overlay :absolute="absoluteLogin" :opacity='opacity' :value="overlayLogin">
          <LoginForm />
          <v-row align="center" justify="center"><v-btn  color="red" dark @click="overlayLogin = false">Cancel</v-btn></v-row>
        </v-overlay>

        </v-card-text>
      </v-expand-transition>

    </v-card>
  </v-hover>
</template>

<script>
import LoginForm from './LoginForm.vue'
import RegisterForm from './RegisterForm.vue'

export default {
  name: 'WelcomeCard',
  components: {
    LoginForm,
    RegisterForm
  },

  data:()=> ({
    absoluteRegister: true,
    overlayRegister: false,
    absolutelogin: true,
    overlayLogin: false,
    opacity: 0.8
  })
}
</script>

<style scoped>

</style>