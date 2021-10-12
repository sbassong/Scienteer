import Vue from 'vue'
import App from './App.vue'
import VueRouter from 'vue-router'
import router from './router'
import Vuex from 'vuex'


Vue.config.productionTip = false

Vue.use(VueRouter)
Vue.use(Vuex)

const store = new Vuex.Store({
  state: {
    user: {},
    projects: [],
    reports: []
  },
  mutations: {
    // increment (state) {
    //   state.count++
    // }
  }
})


new Vue({
  render: h => h(App),
  router,
  store
}).$mount('#app')



