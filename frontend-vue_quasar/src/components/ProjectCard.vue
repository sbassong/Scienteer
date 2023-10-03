<template>
  <v-hover v-slot="{ hover }">
    <v-card class="mx-auto" max-width="344" max-height="400" @click='selectProject(project.id)'>

      <v-img :src="project.image ? project.image : 'https://cdn.vuetifyjs.com/images/cards/sunshine.jpg'" height="200px'">
        <v-expand-transition>
          <div v-if="hover" class="d-flex px-4 transition-fast-in-fast-out purple darken-2 v-card--reveal text-p white--text" style="height: 100%;">
            <h4>reqs:</h4> <br/>
            {{project.requirements.slice(0, 250) }}
            </div>
        </v-expand-transition>
      
      </v-img>
      <v-card-title>{{project.title}}</v-card-title>
      <v-card-subtitle>{{project.category}}</v-card-subtitle>


    </v-card>
  </v-hover>
</template>


<script>
export default {
  name: 'ProjectCard',
  props: {
    project: Object
  },

  methods: {
    selectProject(project_id) {
      this.$router.push(`/project/${project_id}`)
    },
  }
}
</script>

<style scoped>

</style>

