import { api } from '../boot/axios';

export const GetAllProjects = async () => {
  const res = await api.get('/projects');
  return res.data;
};

export const GetProjectByCategory = async (category) => {
  const res = await api.get(`/projects/category/${category}`);
  return res.data;
};

export const GetProjectById = async (projectId) => {
  const res = await api.get(`/project/${projectId}`);
  return res.data;
};

export const GetProjectsByUserId = async (userId) => {
  const res = await api.get(`/projects/researcher/${userId}`);
  return res.data;
};

export const CreateProject = async (data) => {
  const res = await api.post('/projects', data);
  return res.data;
};

export const UpdateProject = async (projectId, data) => {
  const res = await api.put(`/project/${projectId}`, data);
  return res.data;
};

export const UpdateProjectImg = async (projectId, data) => {
  const res = await api.put(`/project/project_img/${projectId}`, data);
  return res.data;
};

export const UpdateProjectScienteers = async (projectId, data) => {
  const res = await api.put(`/project/project_scienteers/${projectId}`, data);
  return res.data;
};

export const DeleteProject = async (projectId) => {
  const res = await api.delete(`/project/${projectId}`);
  return res.data;
};
