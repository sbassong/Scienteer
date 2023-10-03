import { defineStore } from 'pinia';

export const useUsersStore = defineStore('users', {
  state: () => ({
      users: [],
      researchers: [],
      scienteers: []
  }),
  getters: {
    getUsers: (state) => state.users,
    getResearchers: (state) => state.researchers,
    getResearcherById: (state, researcher_id) => state.researchers.filter(researcher => researcher.user_id === researcher_id),
    getScieenters: (state) => state.scienteers,
    getScienteerById: (state, scienteer_id) => state.users.filter(scienteer => scienteer.user_id === scienteer_id),
  },
  actions: {
    setUsers(users) {
      this.users = users;
    },
    setScienteers(scienteers) {
      this.scienteers = scienteers;
    },
    setResearchers(researchers) {
      this.researchers = researchers;
    }
  },
});
