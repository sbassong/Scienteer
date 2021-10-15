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

      <v-divider></v-divider>

      <v-sheet color="grey lighten-4" class="pa-4">
        <v-btn @click="overlayProfile = !overlay" color='primary' class='mb-5' rounded>Update Password</v-btn>
        <v-btn @click="overlayPW = !overlay" color='purple' class='mb-5' dark rounded>Update Profile</v-btn>
      </v-sheet>
    </v-navigation-drawer>

    <v-overlay :absolute="absolutePass" :opacity='opacity' :value="overlayPass">
      <UpdatePasswordForm />
      <v-row align="center" justify="center"><v-btn  color="red" dark @click="overlayPass = false">Cancel</v-btn></v-row>
    </v-overlay>

    <v-overlay :absolute="absoluteProfile" :opacity='opacity' :value="overlayProfile">
      <UpdateProfileForm />
      <v-row align="center" justify="center"><v-btn  color="red" dark @click="overlayProfile = false">Cancel</v-btn></v-row>
    </v-overlay>

    <v-container v-if='user.researcher === true'>
      <v-row>
        <v-col v-for="project in researcherProjects" :key="project.id" cols="4">
          <ProjectCard @click='selectProject(project.id)' :project='project' />
        </v-col>
      </v-row>
    </v-container>

    <v-container v-else>
      <v-row>
        <v-col v-for="report in scienteerReports" :key="report.id" cols="4">
          <ReportCard @click='selectReport(report.id)' :report='report' />
        </v-col>
      </v-row>
    </v-container>
    
  </v-container>
</template>

<script>
import ProjectCard from '../components/ProjectCard.vue'
import ReportCard from '../components/ReportCard.vue'
import UpdateProfileForm from '../components/UpdateProfileForm.vue'
import UpdatePasswordForm from '../components/UpdatePasswordForm.vue'
import { mapState, mapGetters} from 'vuex'

export default {
  name: 'Profile',
  components: {
    ProjectCard,
    ReportCard,
    UpdateProfileForm,
    UpdatePasswordForm
  },

  data:()=> ({
    opacity: 0.8,
    absoluteProfile: true,
    overlayProfile: false,
    absolutePass: true,
    overlayPass: false
  }),

  methods: {
    selectProject(project_id) {
      this.$router.push(`/project/${project_id}`)
    },

    selectReport(report_id) {
      this.$router.push(`/report/${report_id}`)
    },
  },

  computed: {
    ...mapState({
    user: state => state.user,
    authenticated: state => state.authenticated,
    }),

    ...mapGetters({
      scienteerReports: `getReportsByScienteerId${this.user.id}`, 
      researcherProjects: `getProjectsByResearcherId${this.user.id}`
    })
  }
}
</script>