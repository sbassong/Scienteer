<template>
  <v-container class='report' fluid fill-height>

      <v-container>
        <p class="font-weight-bold">Content</p>
        <p class="font-weight-regular">report content will go here</p>
      </v-container>

      <v-container>
        <p class="font-weight-bold">Location</p>
        <p class="font-weight-regular">location will go here</p>
      </v-container>

      <v-container>
        <p class="font-weight-bold">Content</p>
        <v-img max-width="300" src="report image goes here"></v-img>
      </v-container>

  </v-container>
</template>



<script>

export default {
  name: 'ReportDetails',
  components: {

  },

  data: () => ({
    report: null,
  }),
  
  mounted() {

  },
  methods: {
    
  }
}
</script>


<style scoped>

</style>