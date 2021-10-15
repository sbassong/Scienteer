<template>
  <v-container fluid fill-height>
    <v-navigation-drawer v-model="drawer" app>
      <v-sheet color="grey lighten-4" class="pa-4">
        <v-avatar class="mb-4" color="grey darken-1" size="64">
          <v-img :src="user.image"></v-img>
        </v-avatar>
        <div>{{user.name}}</div>
        <div>{{user.email}}</div>
      </v-sheet>

      <v-divider></v-divider>

      <v-sheet color="grey lighten-4" class="pa-4">
        <div>{{user.bio}}</div>
      </v-sheet>
    </v-navigation-drawer>

    <v-container v-if='current_user.researcher === true'>
      <v-row>
        <v-col v-for="project in researcherProjects" :key="project.id" cols="4">
          <ProjectCard @click='selectProject(project.id)' :project='project' />
        </v-col>
      </v-row>
    </v-container>

    <v-container v-else>
      <v-row>
        <v-col v-for="report in scienteerReports" :key="report.id" cols="4">
          <ReportCard :report='report' />
        </v-col>
      </v-row>
    </v-container>
    
  </v-container>
</template>

<script>
import ProjectCard from '../components/ProjectCard.vue'
import ReportCard from '../components/ReportCard.vue'
import { mapState, mapGetters} from 'vuex'

export default {
  name: 'Profile',
  components: {
    ProjectCard,
    ReportCard
  },

  computed: {
    ...mapState({
    user: state => state.user,
    authenticated: state => state.authenticated,
    }),

    ...mapGetters({
      scienteerReports: 'getReportsByScienteerId', 
      researcherProjects: 'getProjectsByResearcherId'
    })
  }
}
</script>