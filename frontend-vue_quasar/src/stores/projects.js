import { defineStore } from 'pinia';

export const useProjectsStore = defineStore('projects', {
  state: () => ({
    projects: [],
  }),
  getters: {
    getProjects: (state) => state.projects,
    getProjectsByCategory: (state, category) => state.projects.filter(project => project.category === category),
    getProjectsByResearcherId: (state, researcherId) => state.projects.filter(project => project.user_id === researcherId),
  },
  actions: {
    setProjects(projects) {
      this.projects = projects;
    }
  },
});
