import { defineStore } from 'pinia';

export const useAuthStore = defineStore('auth', {
  state: () => ({
    user: null,
    authenticated: false,
  }),
  getters: {
    getSessionUser: (state) => state.user,
    isAuthenticated: (state) => state.authenticated,
  },
  actions: {
    setUser(user) {
      this.user = user;
    },
    toggleAuthenticated(bool) {
      this.authenticated = bool;
    }
  },
});
