import VueRouter from 'vue-router'

import About from './pages/About'
import Home from './pages/Home'
import LoginForm from './components/LoginForm'
import RegisterForm from './components/RegisterForm'


const routes = [
  {path: '/', component: Home, name: 'Home'},
  {path: '/about', component: About, name: 'About'},
  {path: '/auth/login', component: LoginForm, name: 'LoginForm'},
  {path: '/auth/register', component: RegisterForm, name: 'RegisterForm'}
]

export default new VueRouter({ routes, mode: 'history' })