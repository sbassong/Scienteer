import Client from './api'


export const GetAllReports = async () => {
    const res = await Client.get(`reports`)
    return res.data
}

export const GetReportById = async (report_id) => {
    const res = await Client.get(`report/${report_id}`)
    return res.data
}


export const GetReportsByProjectId = async (project_id) => {
    const res = await Client.get(`reports/project/${project_id}`)
    return res.data
}

export const CreateReport = async (data) => {
    const res = await Client.post(`reports`, data)
    return res.data
}

export const UpdateReport = async (report_id, data) => {
    const res = await Client.put(`report/${report_id}`, data)
    return res.data
}

export const UpdateReportImg = async (report_id, data) => {
    const res = await Client.put(`report/report_img/${report_id}`, data)
    return res.data
}

export const DeleteReport = async (report_id) => {
    const res = await Client.delete(`report/${report_id}`)
    return res.data
}
