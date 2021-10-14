import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    sessionUser: null,
    authenticated: false,

    users: [],
    projects: [],
    reports: []
  },
  
  //mutations. funcs that are solely responsible for manipulation store state
  mutations: {
    setUser: (state, sessionData) => state.sessionUser = sessionData,
    toggleAuthenticated: (state, data) => state.authenticated = data,
    
    setUsers: (state, data) => state.users = data,
    setProjects: (state, data) => state.projects = data,
    setReports: (state, data) => state.reports = data
  },
  
  //actions. methods used in the app to commit mutations
  actions: {
    setUser: (context, sessionData) => context.commit('setUser', sessionData),
    toggleAuthenticated: (context, data) => context.commit('toggleAuthenticated', data),
    
    setUsers: (context, data) => context.commit('setUsers', data),
    setProjects: (context, data) => context.commit('setProjects', data),
    setReports: (context, data) => context.commit('setReports', data)
  },

  //getters. methods used in the app to get store state data
  getters: {
    getSessionUser: state => state.sessionUser,
    isAuthenticated: state => state.authenticated,
    getResearchers: state => state.users.filter(user => user.researcher === true),
  
    getProjects: state => state.projects,
    getProjectsByCategory: (state, category) => state.projects.filter(project => project.category === category),
    
    getReports: state => state.reports
  }
})