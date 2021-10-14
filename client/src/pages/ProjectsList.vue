<template>
  <v-container class='projects' fluid fill-height>

    <v-col cols="12" class="py-2">
      <v-btn-toggle v-model="text" tile color="deep-purple accent-3" group>
        <v-btn @click="filterProjects" value="All">All</v-btn>
        <v-btn @click="filterProjects" value="Ecology">Ecology</v-btn>
        <v-btn @click="filterProjects" value="Microbiology">Microbiology</v-btn>
        <v-btn @click="filterProjects" value="Marine Biology">Marine Biology</v-btn>
        <v-btn @click="filterProjects" value="Ornithology">Ornithology</v-btn>
      </v-btn-toggle>
    </v-col>

    <v-container>
      <v-row>
        <v-col v-for="project in projects" :key="project.id" cols="4">
          <ProjectCard @click='selectProject(project.id)' :project='project' />
        </v-col>
      </v-row>
    </v-container>

  </v-container>
</template>


<script>
import ProjectCard from '../components/ProjectCard.vue'

export default {
  name: 'ProjectsList',
  components: {
    ProjectCard
  },
  data: () => ({
    projects: null
  }),
  mounted() {

  },
  methods: {
    selectProject(project_id) {
      this.$router.push(`/project/${project_id}`)
    },

    // filterProjects(e){
    //   if (e.target.value === 'All'){
    //     this.projects = allprojects
    //   }
    //   else if (e.target.value === 'Ecology'){
    //     this.projects = allprojects.filter(project => project.category = 'Ecology')
    //   }
    //   else if (e.target.value === 'Microbiology'){
    //     this.projects = allprojects.filter(project => project.category = 'Microbiology')
    //   }
    //   else if (e.target.value === 'Marine Biology'){
    //     this.projects = allprojects.filter(project => project.category = 'Marine Biology')
    //   }
    //   else {
    //     this.projects = allprojects.filter(project => project.category = 'Ornithology')
    //   }
    // }
  }
}
</script>

<style scoped>

</style>