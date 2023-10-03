import { api } from '../boot/axios';

export const LoginUser = async (data) => {
  const res = await api.post('/login', data);
  localStorage.setItem('token', res.data.token);
  return res.data.user;
};

export const RegisterUser = async (data) => {
  const res = await api.post('/register', data);
  return res.data;
};

export const CheckSession = async () => {
  const res = await api.get('/session');
  return res.data;
};
