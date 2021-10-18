import Client from './api'

export const UpdateUserPW = async (user_id, data) => {
    const res = await Client.update(`/users/profile_pw/${user_id}`, data)
    return res.data
}

export const UpdateProfile = async (user_id, data) => {
    const res = await Client.put(`/users/profile/${user_id}`, data)
    return res.data
}

export const UpdateAvatar = async (user_id, data) => {
    const res = await Client.put(`/users/profile_avatar/${user_id}`, data)
    return res.data
}

export const GetAllUsers = async () => {
    const res = await Client.get(`/users`)
    return res.data
}

export const DeleteUser = async (user_id) => {
    const res = await Client.delete(`/user/${user_id}`)
    localStorage.removeItem('token')
    return res.data
}
