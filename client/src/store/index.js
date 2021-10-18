import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    user: null,
    authenticated: false,
    userCoordinates: {
      lat: 0,
      lng: 0
    },
    mapCoordinates: {
      lat: 0,
      lng: 0
    },


    users: [],
    projects: [],
    reports: [],
    
  },
  
  //mutations. funcs that are solely responsible for manipulation store state
  mutations: {
    setUser: (state, data) => state.user = data,
    toggleAuthenticated: (state, data) => state.authenticated = data,
    setUserCoords: (state, data) => state.userCoordinates = data,
    setMapCoords: (state, data) => state.mapCoordinates = data,
    
    setUsers: (state, data) => state.users = data,
    setProjects: (state, data) => state.projects = data,
    setReports: (state, data) => state.reports = data,
  },
  
  //actions. methods used in the app to commit mutations
  actions: {
    setUser: (context, data) => context.commit('setUser', data),
    toggleAuthenticated: (context, data) => context.commit('toggleAuthenticated', data),
    setUserCoords: (context, data) => context.commit('setUserCoords', data),
    setMapCoords: (context, data) => context.commit('setMapCoords', data),
    
    setUsers: (context, data) => context.commit('setUsers', data),
    setProjects: (context, data) => context.commit('setProjects', data),
    setReports: (context, data) => context.commit('setReports', data),
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