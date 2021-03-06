from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from flask_migrate import Migrate
import os

from models.db import db
from models import user, report, project

from resources.user import Login, Register, Update_user_password, Update_user_profile, Get_all_users, CheckSession, Update_user_avatar, Delete_user
from resources.project import Projects, Project_by_id, Project_by_user_id, Projects_by_category, Update_project_image, Update_project_scienteers
from resources.report import Reports, Report_by_id, Report_by_project_id, Update_report_image


app = Flask(__name__)
CORS(app)
api = Api(app)


DATABASE_URL = os.getenv('DATABASE_URL')
os.getenv('APP_SECRET')

if DATABASE_URL:
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL.replace(
        "://", "ql://", 1)
    app.config['SQLALCHEMY_ECHO'] = False
    app.env = 'production'
else:
    app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://localhost:5432/scienteer_db"
    app.config['SQLALCHEMY_ECHO'] = True


db.init_app(app)
migrate = Migrate(app, db)

# USERS
api.add_resource(Login, '/api/auth/login')
api.add_resource(CheckSession, '/api/auth/session')
api.add_resource(Register, '/api/auth/register')
api.add_resource(Get_all_users, '/api/users')
api.add_resource(Update_user_profile, '/api/users/profile/<string:id>')
api.add_resource(Update_user_password, '/api/users/profile_pw/<string:id>')
api.add_resource(Update_user_avatar, '/api/users/profile_avatar/<string:id>')
api.add_resource(Delete_user, '/api/user/<string:id>')

# PROJECTS
api.add_resource(Projects, '/api/projects')
api.add_resource(Project_by_id, '/api/project/<string:id>')
api.add_resource(Project_by_user_id, '/api/projects/researcher/<string:user_id>')
api.add_resource(Projects_by_category, '/api/projects/category/<string:category>')
api.add_resource(Update_project_image, '/api/project/project_img/<string:id>')
api.add_resource(Update_project_scienteers, '/api/project/project_scienteers/<string:id>')

# REPORTS
api.add_resource(Reports, '/api/reports')
api.add_resource(Report_by_id, '/api/report/<string:id>')
api.add_resource(Report_by_project_id, '/api/reports/project/<string:project_id>')
api.add_resource(Update_report_image, '/api/report/report_img/<string:id>')


if __name__ == '__main__':
    app.run()
