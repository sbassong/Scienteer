import Axios from 'axios'

export const BASE_URL = 'http://localhost:5000/api'

const Client = Axios.create({
  baseURL: process.env.NODE_ENV === 'production' ? `${window.location.origin}` : 'http://localhost:5000/api'
})

// Intercepts every request axios makes
Client.interceptors.request.use(
  (config) => {
    const token = localStorage.getItem('token')
    if (token) {
        config.headers['authorization'] = `Bearer ${token}`
    }
    return config 
  },
  (error) => Promise.reject(error)
)


export default Client