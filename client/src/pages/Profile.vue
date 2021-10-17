<template>
  <v-container fluid fill-height>
    <v-navigation-drawer v-model="drawer" app>
      <v-sheet color="grey lighten-4" class="pa-4">
        <v-avatar class="mb-4" color="grey darken-1" size="64">
          <v-img :src="user.avatar ? user.avatar : 'https://i.imgur.com/tRxbS89.jpg'"></v-img>
        </v-avatar>
        <div>Name: {{user.name}}</div>
        <div>Email: {{user.email}}</div>
        <div>Role: {{user.researcher ? 'Researcher' : 'Scienteer'}}</div>
      </v-sheet>

      <v-sheet color="grey lighten-4" class="pa-4">
        <div>{{user.bio}}</div>
      </v-sheet>



      <v-sheet color="grey lighten-4" class="pa-4">
        <v-btn @click="overlayProfile = !overlay" color='primary' class='mb-5' rounded>Update Profile</v-btn>
        <v-btn @click="overlayPass = !overlay" color='purple' class='mb-5' dark rounded>Update Password</v-btn>
        <v-btn @click="overlayAv = !overlay" color='purple' class='mb-5' dark rounded>Update Avatar</v-btn>
        <v-btn @click="overlayP = !overlay" color='purple' class='mb-5' dark rounded>Build Project</v-btn>
      </v-sheet>
    </v-navigation-drawer>

    <v-overlay :absolute="absoluteProfile" :opacity='opacity' :value="overlayProfile">
      <UpdateProfileForm />
      <v-row align="center" justify="center"><v-btn  color="red" dark @click="overlayProfile = false">Cancel</v-btn></v-row>
    </v-overlay>

    <v-overlay :absolute="absolutePass" :opacity='opacity' :value="overlayPass">
      <UpdatePasswordForm />
      <v-row align="center" justify="center"><v-btn  color="red" dark @click="overlayPass = false">Cancel</v-btn></v-row>
    </v-overlay>

    <v-overlay :absolute="absoluteAv" :opacity='opacity' :value="overlayAv">
      <UpdateAvatarForm />
      <v-row align="center" justify="center"><v-btn  color="red" dark @click="overlayAv = false">Cancel</v-btn></v-row>
    </v-overlay>

    <v-overlay :absolute="absoluteP" :opacity='opacity' :value="overlayP">
      <ProjectForm />
      <v-row align="center" justify="center"><v-btn  color="red" dark @click="overlayP = false">Cancel</v-btn></v-row>
    </v-overlay>


    <v-container v-if='user.researcher === true'>
      <v-row>
        <v-col v-for="project in researcherProjects" :key="project.id" cols="4">
          <ProjectCard  :project='project' />
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
import UpdateProfileForm from '../components/UpdateProfileForm.vue'
import UpdatePasswordForm from '../components/UpdatePasswordForm.vue'
import UpdateAvatarForm from '../components/UpdateAvatarForm.vue'
import ProjectForm from '../components/ProjectForm.vue'
import { mapState } from 'vuex'

export default {
  name: 'Profile',
  components: {
    ProjectCard,
    ReportCard,
    UpdateProfileForm,
    UpdatePasswordForm,
    UpdateAvatarForm,
    ProjectForm
  },

  data:()=> ({
    opacity: 0.8,
    absoluteProfile: true,
    overlayProfile: false,
    absolutePass: true,
    overlayPass: false,
    absoluteAv: true,
    overlayAv: false,
    absoluteP: true,
    overlayP: false,

    researcherProjects: null,
    scienteerReports: null
  }),

  beforeMount() {
    this.getUserDetails()
  },

  methods: {
    selectProject(project_id) {
      this.$router.push(`/project/${project_id}`)
    },

    selectReport(report_id) {
      this.$router.push(`/report/${report_id}`)
    },

    getReports() {
      const reports = this.reports.filter(report => report.user_id === this.user.id)
      this.scienteerReports = reports
    },

    getProjects() {
      const projects = this.projects.filter(project => project.user_id === this.user.id)
      this.researcherProjects = projects
    },

    async getUserDetails() {
      if (this.user.researcher === true) this.getProjects()
      else this.getReports()
    }
  },

  computed: {
    ...mapState({
      user: state => state.user,
      authenticated: state => state.authenticated,
      reports: state => state.reports,
      projects: state => state.projects
    }),
  }
}
</script>