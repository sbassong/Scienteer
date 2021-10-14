<template>
  <v-container fluid fill-height>
    <v-navigation-drawer v-model="drawer" app>
      <v-sheet color="grey lighten-4" class="pa-4">
        <v-avatar class="mb-4" color="grey darken-1" size="64">
          <v-im src="current_user.image"></v-im>
        </v-avatar>
        <div>current_user.name</div>
        <div>current_user.email</div>
      </v-sheet>

      <v-divider></v-divider>

      <v-sheet color="grey lighten-4" class="pa-4">
        <div>current_user.bio</div>
      </v-sheet>
    </v-navigation-drawer>

    <v-container v-if='current_user.researcher === true'>
      <v-row>
        <v-col v-for="project in user_projects" :key="project.id" cols="4">
          <ProjectCard @click='selectProject(project.id)' :project='project' />
        </v-col>
      </v-row>
    </v-container>

    <v-container v-else>
      <v-row>
        <v-col v-for="report in user_reports" :key="report.id" cols="4">
          <ReportCard :report='report' />
        </v-col>
      </v-row>
    </v-container>
    
  </v-container>
</template>

<script>
import ProjectCard from '../components/ProjectCard.vue'
import ReportCard from '../components/ReportCard.vue'

export default {
  name: 'Profile',
  components: {
    ProjectCard,
    ReportCard
  },

  data:()=>({
    current_user: null,
    user_projects: null,
    user_reports: null
  }),

  methods:{

  },


}
</script>