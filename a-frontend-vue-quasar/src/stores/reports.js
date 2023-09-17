import { defineStore } from 'pinia';

export const useReportsStore = defineStore('reports', {
  state: () => ({
    reports: [],
  }),
  getters: {
    getReports: (state) => state.reports,
    getReportsByScienteerId: (state, scienteerId) => state.reports.filter(report => report.user_id === scienteerId),

  },
  actions: {
    setReports(reports) {
      this.reports = reports;
    }
  },
});
