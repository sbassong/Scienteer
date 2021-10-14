<template>
  <v-container class='researcher' fluid fill-height>
    <v-row align='center' justify='space-around'>
      <v-container>
        <v-img max-width="500" src="researcher image goes here"></v-img>
      </v-container>
      
      <v-container>
        <p>Researcher.bio goes here</p>
      </v-container>
    </v-row>

    <v-container class='researcher-projects'>
      <v-row>
        <v-col v-for="project in researcher_projects" :key="project.id" cols="2">
          <ProjectCard @click='selectProject(project.id)' :project='project' />
        </v-col>
      </v-row>
    </v-container>

  </v-container>
</template>



<script>
import ProjectCard from '../components/ProjectCard'

export default {
  name: 'ResearcherDetails',
  data: () => ({
    researcher: null,
    researcher_projects: null
  }),
  components: {
    ProjectCard
  },
  mounted() {

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