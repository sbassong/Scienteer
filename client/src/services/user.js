import Client from './api'

export const UpdateUserPW = async (user_id, data) => {
    const res = await Client.post(`users/profile_pw/${user_id}`, data)
    return res.data
}

export const UpdateProfile = async (user_id, data) => {
    const res = await Client.put(`users/profile/${user_id}`, data)
    return res.data
}

export const GetAllUsers = async () => {
    const res = await Client.get(`users`)
    return res.data
}
