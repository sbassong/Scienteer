from flask_restful import Resource
from flask import request

from models.db import db
from models.project import Project

from middleware import create_token, strip_token, read_token, compare_password, gen_password

#grabs all projects and creates project
class Projects(Resource):
    def get(self):
        raw_projects = Project.find_all_projects()
        projects = [project.json() for project in raw_projects]
        return projects

    def post(self):
        data = request.get_json()
        params = {}
        for k in data.keys():
            params[k] = data[k]
        project = Project(**params)
        project.create()
        return project.json(), 201

#update and delete project
class Project_by_id(Resource):
    def put(self, id):
        data = request.get_json()
        token = strip_token(request)
        payload = read_token(token)
        if payload:
            project = Project.find_project_by_id(id)
            if payload["id"] == project["user_id"]:
                for key in data.keys():
                    project[key] = data[key]
                db.session.commit()
                return project.json()
            return {"msg": "Unauthorized credentials"}
        return {"msg": "Unauthorized access"}, 404

    def delete(self, id):
        token = strip_token(request)
        payload = read_token(token)
        if payload:
            project = Project.find_project_by_id(id)
            if payload["id"] == project["user_id"]:
                db.session.delete(project)
                db.session.commit()
                return {"msg": "Project deleted!", "payload": project.id}
            return {"msg": "Unauthorized credentials"}
        return {"msg": "Unauthorized access"}, 404

#handles get projects for category display
class Projects_by_category(Resource):
    def get(self, category):
        raw_projects = Project.find_projects_by_category(category)
        projects = [project.json() for project in raw_projects]
        return projects

#handles projects of researcherDetail page
class Project_by_user_id(Resource):
    def get(self, user_id):
        raw_projects = Project.find_projects_by_user_id(user_id)
        projects = [project.json() for project in raw_projects]
        return projects
