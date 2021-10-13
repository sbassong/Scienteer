<template>
  <v-app>
    <!-- <v-app-bar
      
    </v-app-bar> -->

    <v-main>
      <ProjectForm />
    </v-main>
  </v-app>
</template>

<script>

import ProjectForm from './components/ProjectForm.vue'

export default {
  name: 'App',
  components: {
    ProjectForm
  },

  data: () => ({
    //
  }),
};
</script>
