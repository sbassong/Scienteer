import { api } from '../boot/axios';

export const GetAllReports = async () => {
  const res = await api.get('/reports');
  return res.data;
};

export const GetReportById = async (reportId) => {
  const res = await api.get(`/report/${reportId}`);
  return res.data;
};

export const GetReportsByProjectId = async (projectId) => {
  const res = await api.get(`/reports/project/${projectId}`);
  return res.data;
};

export const CreateReport = async (data) => {
  const res = await api.post('/reports', data);
  return res.data;
};

export const UpdateReport = async (reportId, data) => {
  const res = await api.put(`/report/${reportId}`, data);
  return res.data;
};

export const UpdateReportImg = async (reportId, data) => {
  const res = await api.put(`/report/report_img/${reportId}`, data);
  return res.data;
};

export const DeleteReport = async (reportId) => {
  const res = await api.delete(`/report/${reportId}`);
  return res.data;
};
