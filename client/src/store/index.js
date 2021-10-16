import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    user: null,
    authenticated: false,

    users: [],
    projects: [],
    reports: [],

    ecoProjects: [],
    microProjects: [],
    marProjects: [],
    orPorjects: [],

    researcherDetails: {}, //RD
    researcherProjects: [], //RPs

    projectDetails: {}, //PD
    projectReports: {}, //PRs
    
    reportDetails: {}, // RDs
    
  },
  
  //mutations. funcs that are solely responsible for manipulation store state
  mutations: {
    setUser: (state, data) => state.user = data,
    toggleAuthenticated: (state, data) => state.authenticated = data,
    
    setUsers: (state, data) => state.users = data,
    setProjects: (state, data) => state.projects = data,
    setReports: (state, data) => state.reports = data,

    RD: (state, data) => state.researcherDetails = data,
    RPs: (state, data) => state.researcherProjects = data,
    PD: (state, data) => state.projectDetails = data,
    PRs: (state, data) => state.projectReports = data,
    RDs: (state, data) => state.reportDetails = data,
  },
  
  //actions. methods used in the app to commit mutations
  actions: {
    setUser: (context, data) => context.commit('setUser', data),
    toggleAuthenticated: (context, data) => context.commit('toggleAuthenticated', data),
    
    setUsers: (context, data) => context.commit('setUsers', data),
    setProjects: (context, data) => context.commit('setProjects', data),
    setReports: (context, data) => context.commit('setReports', data),


    RD: (context, data) => context.commit('RD', data),
    RPs: (context, data) => context.commit('RPs', data),
    PD: (context, data) => context.commit('PD', data),
    PRs: (context, data) => context.commit('PRs', data),
    RDs: (context, data) => context.commit('RDs', data),
  },

  //getters. methods used in the app to get store state data
  getters: {
    getSessionUser: state => state.user,
    isAuthenticated: state => state.authenticated,
    getResearchers: state => state.users.filter(user => user.researcher === true),
    getResearcherById: (state, researcher_id) => state.users.filter(user => user.id === researcher_id),
  
    getProjects: state => state.projects,
    getProjectsByCategory: (state, category) => state.projects.filter(project => project.category === category),
    getProjectsByResearcherId: (state, researcherId) => state.projects.filter(project => project.user_id === researcherId),
    
    getReports: state => state.reports,
    getReportsByScienteerId: (state, scienteerId) => state.projects.filter(report => report.user_id === scienteerId),
  }
})