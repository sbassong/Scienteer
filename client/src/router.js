import VueRouter from 'vue-router'

import About from './pages/About'
import Home from './pages/Home'
import Profile from './pages/Profile'
import ResearchersList from './pages/ResearchersList'
import ResearcherDetails from './pages/ResearcherDetails'
import ProjectsList from './pages/ProjectsList'
import ProjectDetails from './pages/ProjectDetails'

const routes = [
  {path: '/', component: Home, name: 'Home'},
  {path: '/about', component: About, name: 'About'},
  {path: '/profile', component: Profile, name: 'Profile'},
  {path: '/researchers', component: ResearchersList, name: 'ResearchersList'},
  {path: '/researcher/:researcher_id', component: ResearcherDetails, name: 'ResearcherDetails'},
  {path: '/projects', component: ProjectsList, name: 'ProjectsList'},
  {path: '/project/:project_id', component: ProjectDetails, name: 'ProjectDetails'}
]

export default new VueRouter({ routes, mode: 'history' })