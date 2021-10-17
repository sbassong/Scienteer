<template>
  <v-container class='researcher' fluid fill-height>
    <v-row align='center' justify='space-around'>
      <v-container>
        <v-img max-width="500" :src="researcher.avatar ? researcher.avatar : 'https://cdn.vuetifyjs.com/images/cards/sunshine.jpg'"></v-img>
      </v-container>
      
      <v-container>
        <p>Name: {{researcher.name}} </p>
        <p>Email: {{researcher.email}} </p>
        <h4>Bio:</h4>
        <p>{{researcher.bio}} </p>
      </v-container>
    </v-row>

    <v-container class='researcher-projects'>
      <h3>{{researcher.name}}'s ongoing projects:</h3>
      <v-row>
        <v-col v-for="project in researcher_projects" :key="project.id" cols="2">
          <ProjectCard :project='project' />
        </v-col>
      </v-row>
    </v-container>

  </v-container>
</template>



<script>
import { mapState } from 'vuex'
import ProjectCard from '../components/ProjectCard'

export default {
  name: 'ResearcherDetails',
  data:() => ({
    researcher: null,
    researcher_projects: null,
  }),

  components: {
    ProjectCard
  },

  mounted(){
    this.getProjectsByUserId()
  },

  methods: {
    async getProjectsByUserId() {
        const res = await this.users.filter(user => user.id === this.$route.params.researcher_id)
        this.researcher = res[0]
        const ress = await this.projects.filter(project => project.user_id === this.$route.params.researcher_id)
        this.researcher_projects = ress
    }
  },

  computed: {
    ...mapState(['users', 'projects'])
  }
}
</script>


<style scoped>

</style>