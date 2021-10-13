import Vue from 'vue'
import App from './App.vue'
import VueRouter from 'vue-router'
import router from './router'
import Vuex from 'vuex'
import vuetify from './plugins/vuetify'
import Vuelidate from 'vuelidate'


Vue.config.productionTip = false

Vue.use(VueRouter)
Vue.use(Vuex)
Vue.use(Vuelidate)

const store = new Vuex.Store({
  state: {
    users: [],
    projects: [],
    reports: [],
    session_user: null,
    authenticated: false
  },
  mutations: {
    set_users(state, data) {
      state.users = data
    },
    set_projects(state, data) {
      state.projects = data
    },
    set_report(state, data) {
      state.reports = data
    },
    set_session_user(state, data) {
      state.session_user = data
    },
    toggle_authenticated(state) {
      state.authenticated = true
    }
  }
})


new Vue({
  render: h => h(App),
  router,
  vuetify,
  store
}).$mount('#app')



