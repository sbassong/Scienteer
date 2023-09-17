import About from './pages/About';
import Home from './pages/Home';
import Profile from './pages/Profile';
import ResearchersList from './pages/ResearchersList';
import ResearcherDetails from './pages/ResearcherDetails';
import ProjectsList from './pages/ProjectsList';
import ProjectDetails from './pages/ProjectDetails';
import ReportDetails from './pages/ReportDetails';
import LoginFormPage from './pages/LoginFormPage';
import RegisterFormPage from './pages/RegisterFormPage';
import UpdateProjectForm from './components/UpdateProjectForm';


const routes = [
  {path: '/', component: Home, name: 'Home'},
  {path: '/users/login', component: LoginFormPage, name: 'LoginFormPage'}, 
  {path: '/users/register', component: RegisterFormPage, name: 'RegisterFormPage'}, 
  {path: '/projects/project/update', component: UpdateProjectForm, name: 'UpdateProjectForm'}, 
  {path: '/about', component: About, name: 'About'},
  {path: '/profile', component: Profile, name: 'Profile'},
  {path: '/researchers', component: ResearchersList, name: 'ResearchersList'},
  {path: '/researcher/:researcher_id', component: ResearcherDetails, name: 'ResearcherDetails', props: true},
  {path: '/projects', component: ProjectsList, name: 'ProjectsList'},
  {path: '/project/:project_id', component: ProjectDetails, name: 'ProjectDetails', props: true},
  {path: '/report/:report_id', component: ReportDetails, name: 'ReportDetails', props: true},

  // Always leave this as last one,
  // but you can also remove it
  {
    path: '/:catchAll(.*)*',
    component: () => import('pages/ErrorNotFound.vue'),
  },
];

export default routes;
