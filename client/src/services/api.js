import Axios from 'axios'

const Client = Axios.create({
  baseURL:
    process.env.NODE_ENV === 'production'
      ? `${process.env.VUE_APP_API_URL}/api`
      : 'http://localhost:5000/api'
})


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