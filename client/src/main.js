import Vue from 'vue'
import App from './App.vue'
import VueGeolocation from 'vue-browser-geolocation'
import * as VueGoogleMaps from 'vue2-google-maps'
import VueRouter from 'vue-router'
import Vuelidate from 'vuelidate'

import vuetify from './plugins/vuetify'
import router from './router'
import store from './store/index'

const GMAPS_KEY=process.env.VUE_APP_GOOGLE_MAPS_API_KEY

Vue.config.productionTip = false
Vue.use(VueRouter)
Vue.use(VueGeolocation)
Vue.use(Vuelidate)

Vue.use(VueGoogleMaps, {
  load: {
    key: `${GMAPS_KEY}`
  }
})

new Vue({
  render: h => h(App),
  router,
  vuetify,
  store
}).$mount('#app')




