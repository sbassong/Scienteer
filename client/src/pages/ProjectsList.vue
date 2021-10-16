<template>
  <v-container class='projects' fluid fill-height>

    <v-col cols="12" class="py-2">
      <v-btn-toggle tile color="deep-purple accent-3" group>
        <v-btn @click="filterProjects" value="All">All</v-btn>
        <v-btn @click="filterProjects" value="Ecology">Ecology</v-btn>
        <v-btn @click="filterProjects" value="Microbiology">Microbiology</v-btn>
        <v-btn @click="filterProjects" value="Marine Biology">Marine Biology</v-btn>
        <v-btn @click="filterProjects" value="Ornithology">Ornithology</v-btn>
      </v-btn-toggle>
    </v-col>

    <v-container fluid fill-height>
      <v-row>
        <v-col v-for="project in allProjects" :key="project.id" cols="4">
          <ProjectCard :project='project' />
        </v-col>
      </v-row>
    </v-container>

  </v-container>
</template>


<script>
import { mapState } from 'vuex'
import ProjectCard from '../components/ProjectCard.vue'

export default {
  name: 'ProjectsList',
  components: {
    ProjectCard
  },

  data: () => ({
    allProjects: null,
  }),

  mounted() {
    this.renderProjects()
  },

  methods: {
    filterProjects(e){
      if (e.target.value === 'Ornithology')this.allProjects = this.projects.filter(project => project.category === e.target.value)
      else if (e.target.value === 'Ecology') this.allProjects = this.projects.filter(project => project.category === e.target.value)
      else if (e.target.value === 'Microbiology') this.allProjects = this.projects.filter(project => project.category === e.target.value)
      else if (e.target.value === 'Marine Biology') this.allProjects = this.projects.filter(project => project.category === e.target.value)
      else this.allProjects = this.projects
    },

    renderProjects () {
      this.allProjects = this.projects
    }
  },

  computed: {
    ...mapState(['projects']),
  }
}
</script>

<style scoped>

</style>