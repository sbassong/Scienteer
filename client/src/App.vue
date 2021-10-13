<template>
  <v-app>
    <!-- <v-app-bar
      
    </v-app-bar> -->

    <v-main>
      <!-- <RegisterForm /> -->
      <LoginForm />
    </v-main>
  </v-app>
</template>

<script>

// import RegisterForm from './components/RegisterForm.vue'
import LoginForm from './components/LoginForm.vue'

export default {
  name: 'App',
  components: {
    // RegisterForm,
    LoginForm
  },

  data: () => ({
    //
  }),
};
</script>
