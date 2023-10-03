import { api } from '../boot/axios';

export const UpdateUserPW = async (userId, data) => {
  const res = await api.put(`/users/profile_pw/${userId}`, data);
  return res.data;
};

export const UpdateProfile = async (userId, data) => {
  const res = await api.put(`/users/profile/${userId}`, data);
  return res.data;
};

export const UpdateAvatar = async (userId, data) => {
  const res = await api.put(`/users/profile_avatar/${userId}`, data);
  return res.data;
};

export const GetAllUsers = async () => {
  const res = await api.get('/users');
  return res.data;
};

export const DeleteUser = async (userId) => {
  const res = await api.delete(`/user/${userId}`);
  localStorage.removeItem('token');
  return res.data;
};
