from flask_restful import Resource
from flask import request

from models.db import db
from models.user import User

from middleware import create_token, strip_token, read_token, compare_password, gen_password


#handles login
class Login(Resource):
  def post(self):
    data = request.get_json()
    user = User.find_user_by_email(data["email"]) 
    if user and compare_password(data["password"], user.password_digest):
      user = user.json()
      payload = {
        "id": user["id"],
        "email": user["email"]
      }
      token = create_token(payload)
      return {"user" : payload, "token": token}, 200
    return {"msg": "Unauthorized access"}, 404

  #handles checking for user session
  def get(self):
    token = strip_token(request)
    payload = read_token(token)
    if payload:
      return payload, 200
    return {"msg": "Unauthorized access"}, 404


#handle register
class Register(Resource):
  def post(self):
    data = request.get_json()
    params = {
        "name": data['name'],
        "email": data['email'],
        "bio": data['bio'],
        "researcher": data['researcher'],
        "password_digest": gen_password(data['password'])
    }
    user = User(**params)
    user.create()
    return user.json(), 201

#handles updates to password
class Update_user_password(Resource):
  def put(self, id):
    data = request.get_json()
    user = User.find_user_by_id(id)
    if user and compare_password(data["old_password"], user.password_digest):
      password_digest = gen_password(data["new_password"])
      user.password_digest = password_digest
      db.session.commit()
      return {"msg": "User password updated!"}, 200
    return {"msg": "Unauthorized credentials"}, 404


#handles updates to other profile attr
class Update_user_profile(Resource):
  def put(self, id):
    data = request.get_json()
    user = User.find_user_by_id(id)
    if user:
      for key in data:
        setattr(user, key, data[key])
      db.session.commit()
      return user.json(), 200
    return {"msg": "Unmatched user"}, 404






