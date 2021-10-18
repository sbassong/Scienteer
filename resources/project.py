from flask_restful import Resource
from flask import request

from models.db import db
from models.project import Project

from werkzeug.utils import secure_filename
from middleware import create_token, strip_token, read_token, compare_password, gen_password, allowed_file
from aws import upload


#grabs all projects and creates project
class Projects(Resource):
    def get(self):
        raw_projects = Project.find_all_projects()
        projects = [project.json() for project in raw_projects]
        return projects, 200

    def post(self):
        data = request.get_json()
        params = {
            "title": data['title'],
            "category": data['category'],
            "image": '',
            "requirements": data['requirements'],
            "instructions": data['instructions'],
            "scienteers": [],
            "user_id": data['user_id']
        }
        project = Project(**params)
        project.create()
        return project.json(), 201


#update, delete, and get projectDetails
class Project_by_id(Resource):
    def get(self, id):
        project = Project.find_project_by_id(id)
        if project:
            return project.json(), 200
        return 'Project not found', 404

    def put(self, id):
        data = request.get_json()
        # token = strip_token(request)
        # payload = read_token(token)
        # if payload:
        project = Project.find_project_by_id(id)
        # if payload["id"] == str(project.user_id):
        for key in data:
            setattr(project, key, data[key])
        db.session.commit()
        return project.json(), 200
            # return {"msg": "Unauthorized credentials"}, 401
        # return {"msg": "Unauthorized access"}, 404

    def delete(self, id):
        # token = strip_token(request)
        # payload = read_token(token)
        # if payload:
        project = Project.find_project_by_id(id)
        # if payload["id"] == str(project.user_id):
        db.session.delete(project)
        db.session.commit()
        return {"msg": "Project deleted!"}, 200
        # return {"msg": "Unauthorized credentials"}, 401
        # return {"msg": "Unauthorized access"}, 404


#handles get projects for category display
class Projects_by_category(Resource):
    def get(self, category):
        raw_projects = Project.find_projects_by_category(category)
        projects = [project.json() for project in raw_projects]
        return projects, 200


#handles projects of researcherDetail page
class Project_by_user_id(Resource):
    def get(self, user_id):
        raw_projects = Project.find_projects_by_user_id(user_id)
        projects = [project.json() for project in raw_projects]
        return projects, 200


class Update_project_image(Resource):
    def put(self, id):
        if "image" not in request.files:
            return {"msg": "Error"}, 400
        file = request.files['image']
        if file and allowed_file(file.filename):
            file.filename = secure_filename(file.filename)
            uploaded = upload(file)
            project = Project.update(id, {"image": uploaded})
            return project, 200
        return {"msg": "Error, Upload didn't work"}, 400

class Update_project_scienteers(Resource):
    def put(self, id):
        data = request.get_json()
        project = Project.find_project_by_id(id)
        if project:
            project.scienteers.append(data)
            db.session.commit()
            return project.json(), 200
        return {"msg": "Project not found"}, 404
    