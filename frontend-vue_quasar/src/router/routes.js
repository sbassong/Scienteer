import HomePage from '../pages/HomePage.vue';
import RegisterFormPage from '../pages/RegisterFormPage.vue';
import LoginFormPage from '../pages/LoginFormPage.vue';
// import Profile from '../pages/Profile.vue';
// import ResearchersList from '../pages/ResearchersList.vue';
// import ResearcherDetails from '../pages/ResearcherDetails.vue';
// import ProjectsList from '../pages/ProjectsList.vue';
// import ProjectDetails from '../pages/ProjectDetails.vue';
// import ReportDetails from '../pages/ReportDetails.vue';
// import UpdateProjectForm from '../components/UpdateProjectForm.vue';

const routes = [
  { path: '/', component: HomePage, name: 'HomePage' },
  { path: '/register', component: RegisterFormPage, name: 'RegisterFormPage' },
  { path: '/login', component: LoginFormPage, name: 'LoginFormPage' },
  // { path: '/profile', component: Profile, name: 'Profile' },
  // {
  //   path: '/researchers/',
  //   component: ResearchersList,
  //   name: 'ResearchersList',
  // },
  // {
  //   path: '/:researcher_id',
  //   component: ResearcherDetails, name: 'ResearcherDetails', props: true,
  // },
  // {
  //   path: '/projects',
  //   component: ProjectsList,
  //   name: 'ProjectsList',
  // },
  // {
  //   path: '/:project_id/update', component: UpdateProjectForm,
  //   name: 'UpdateProjectForm', props: true,
  // },
  // {
  //   path: '/:project_id', component: ProjectDetails, name: 'ProjectDetails', props: true,
  // },
  // {
  //   path: '/report/:report_id', component: ReportDetails, name: 'ReportDetails', props: true,
  // },

  // Always leave this as last one,
  // but you can also remove it
  {
    path: '/:catchAll(.*)*',
    component: () => import('pages/ErrorNotFound.vue'),
  },
];

export default routes;
