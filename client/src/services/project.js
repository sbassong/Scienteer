import Client from './api'


export const GetAllProjects = async () => {
    const res = await Client.get(`projects`)
    return res.data
}

export const GetProjectByCategory = async (category) => {
    const res = await Client.get(`projects/category/${category}`)
    return res.data
}

export const GetProjectById = async (project_id) => {
    const res = await Client.get(`project/${project_id}`)
    return res.data
}

export const GetProjectsByUserId = async (user_id) => {
    const res = await Client.get(`projects/researcher/${user_id}`)
    return res.data
}

export const CreateProject = async (data) => {
    const res = await Client.post(`projects`, data)
    return res.data
}

export const UpdateProject = async (project_id, data) => {
    const res = await Client.put(`project/${project_id}`, data)
    return res.data
}

export const DeleteProject = async (project_id) => {
    const res = await Client.delete(`project/${project_id}`)
    return res.data
}



