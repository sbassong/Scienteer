<template>
  <v-container class='researcher' fluid fill-height>
    <v-row align='center' justify='space-around'>
      <v-container>
        <v-img max-width="500" :src="researcher.avatar ? researcher.avatar : 'https://cdn.vuetifyjs.com/images/cards/sunshine.jpg'"></v-img>
      </v-container>
      
      <v-container>
        <p>{{researcher.name}} </p>
        <p>{{researcher.email}} </p>
        <p>{{researcher.bio}} </p>
      </v-container>
    </v-row>

    <v-container class='researcher-projects'>
      <v-row>
        <v-col v-for="project in researcher_projects" :key="project.id" cols="2">
          <ProjectCard :project='project' />
        </v-col>
      </v-row>
    </v-container>

  </v-container>
</template>



<script>
import { mapActions, mapState } from 'vuex'
import ProjectCard from '../components/ProjectCard'
import {GetProjectsByUserId} from '../services/project'
import {GetAllUsers} from '../services/user'

export default {
  name: 'ResearcherDetails',
  data:() => ({
    researcher: null,
    researcher_projects: null,
  }),

  components: {
    ProjectCard
  },
  mounted() {
        this.getProjectsByUserId()

  },


  beforeMounted(){
    this.getProjectsByUserId()
  },

  methods: {
    ...mapActions(['RD', 'RPs']),
    async getProjectsByUserId() {
        const res = await GetAllUsers()
        const res1 = res.filter(user => user.id === this.$route.params.researcher_id)
        this.researcher = res1[0]
        this.RD(res)
        console.log(this.researcher)
        const ress = await GetProjectsByUserId(this.$route.params.researcher_id)
        this.researcher_projects = ress
        this.RPs(ress)
        // const ress = await GetProjectsByUserId(this.$route.params.researcher_id)
        // this.researcher_projects = ress

      console.log('researcher', this.researcher, 'projects', this.researcher_projects)
    },
  },

  computed: {
    ...mapState(['researcherDetails', 'researcherProjects'])
  }
}
</script>


<style scoped>

</style>