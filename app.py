from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from flask_migrate import Migrate
from models.db import db
# from models import user, report, project
# from resources.user import 
# from resources.project import 
# from resources.report import 

app = Flask(__name__)
CORS(app)
api = Api(app)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://localhost:5432/flask_artsy"
app.config['SQLALCHEMY_ECHO'] = True

db.init_app(app)
migrate = Migrate(app, db)


# api.add_resource(Login, '/users/login')
# api.add_resource(Register, '/users/register')

# api.add_resource()
# api.add_resource()

# api.add_resource()
# api.add_resource()

if __name__ == '__main__':
    app.run(debug=True)
