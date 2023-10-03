<template>
  <v-card class="mx-auto px-5 " align='center' justify='center' width='700' height="auto">
    <v-card-title class="justify-center">Report Builder</v-card-title>
    <form >
      <v-textarea v-model="content" label="Report Content" required @change="$v.content.$touch()" @blur="$v.content.$touch()" counter filled shaped full-width auto-grow ></v-textarea>
      <v-text-field v-model="location" label="Location" @change="$v.location.$touch()" @blur="$v.location.$touch()" filled shaped ></v-text-field>
      <v-file-input v-model='image' label="Images" @change="$v.image.$touch()" @blur="$v.image.$touch()" accept="image/*" prepend-icon="mdi-camera" multiple></v-file-input>
      <v-row align="center" justify="center"><v-btn class="mr-4 mb-5 mt-2" @click='handleSubmit'>Submit Report</v-btn></v-row>
    </form>

    <GmapMap :center="userCoords" :zoom="zoom" style="width: 400px; height: 300px; margin: 20px auto" ref="mapRef" @dragend="handleDrag"></GmapMap>
  </v-card>
</template>

<script>
import {CreateReport, UpdateReportImg} from '../services/report'
import { mapActions, mapState } from 'vuex'

export default {
  name: 'ReportForm',

  props: {
    project: Object
  },

  data: () => ({
    content: '',
    location: null,
    image: null,

    map: null,
    zoom: 5,
    userCoords: {
      lat: 0,
      lng: 0
    },
    mapCoords:  {
      lat: 0,
      lng: 0
    }
  }),

  created() {
    if(localStorage.center) {
      this.userCoords = JSON.parse(localStorage.center)
    } else {
      this.$getLocation({})
        .then(coordinates => {
          this.setUserCoords(coordinates)
          this.userCoords = coordinates
        })
        .catch(error =>alert(error))
    }


    if(localStorage.zoom) {
      this.zoom = parseInt(localStorage.zoom)
    }
  },

  mounted() {
    this.$refs.mapRef.$mapPromise.then(map => this.map = map)
  },

  methods: {
    ...mapActions(['setUserCoords']),

    async handleSubmit(event) {
      event.preventDefault()
      const reportBody = {
        content: this.content,
        location: this.userCoords,
        user_id: this.user.id,
        project_id: this.project.id
      }
      const createdRep = await CreateReport(reportBody)
      console.log("crerep", createdRep)


      const imageBody = {
        image: this.image
      }
      let formData = new FormData()
      formData.append("image" , imageBody["image"])
      const updatedRep = await UpdateReportImg(createdRep.id, formData)
      console.log("uprep", updatedRep)

      this.content = ''
      this.location = null
      this.image = null 
      this.$router.push(`/project/${this.project.id}`)
    },

    handleDrag () {
      let center = {
        lat: this.map.getCenter().lat(),
        lng: this.map.getCenter().lng()
      }
      let zoom = this.map.getZoom()

      localStorage.center = JSON.stringify(center)
      localStorage.zoom = zoom;

      }
    },

    computed: {
    ...mapState({
    user: state => state.user,
    authenticated: state => state.authenticated,
    userCoordinates: state => state.userCoordinates,
    mapCoordinates: state => state.mapCoordinates,
    }),

    mapCoordinates() {
      if (!this.map) {
        return {
          lat: 0,
          lng: 0
        }
      }
      return {
        lat: this.map.getCenter().lat().toFixed(4),
        lng: this.map.getCenter().lng().toFixed(4)
      }
    }
  }
}

</script>
