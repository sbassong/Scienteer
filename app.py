from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from flask_migrate import Migrate
# from werkzeug.utils import secure_filename

# from Scienteer.middleware import SECRET_KEY

from models.db import db
from models import user, report, project

from resources.user import Login, Register, Update_user_password, Update_user_profile, Get_all_users
from resources.project import Projects, Project_by_id, Project_by_user_id, Projects_by_category
from resources.report import Reports, Report_by_id, Report_by_project_id

app = Flask(__name__)
CORS(app)
api = Api(app)


app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://localhost:5432/scienteer_db"
app.config['SQLALCHEMY_ECHO'] = True

db.init_app(app)
migrate = Migrate(app, db)


api.add_resource(Login, '/auth/login')
api.add_resource(Register, '/auth/register')
api.add_resource(Get_all_users, '/users')
api.add_resource(Update_user_profile, '/users/profile/<string:id>')
api.add_resource(Update_user_password, '/users/profile_pw/<string:id>')

api.add_resource(Projects, '/projects')
api.add_resource(Project_by_id, '/project/<string:id>')
api.add_resource(Project_by_user_id, '/projects/researcher/<string:user_id>')
api.add_resource(Projects_by_category, '/projects/category/<string:category>')

api.add_resource(Reports, '/reports')
api.add_resource(Report_by_id, '/report/<string:id>')
api.add_resource(Report_by_project_id, '/reports/project/<string:project_id>')
# api.add_resource(Report_image, '/report/image/<string:id>')



if __name__ == '__main__':
    app.run(debug=True)
