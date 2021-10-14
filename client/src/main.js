import Vue from 'vue'
import App from './App.vue'
import VueRouter from 'vue-router'
import router from './router'
import vuetify from './plugins/vuetify'
import Vuelidate from 'vuelidate'
import store from './store/index'

Vue.config.productionTip = false

Vue.use(VueRouter)
Vue.use(Vuelidate)

new Vue({
  render: h => h(App),
  router,
  vuetify,
  store
}).$mount('#app')




