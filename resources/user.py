from flask_restful import Resource
from flask import request

from models.db import db
from models.user import User

from werkzeug.utils import secure_filename
from middleware import create_token, strip_token, read_token, compare_password, gen_password, allowed_file
from aws import upload_file

#handles login
class Login(Resource):
  def post(self):
    data = request.get_json()
    user = User.find_user_by_email(data["email"]) 
    if user and compare_password(data["password"], user.password_digest):
      user = user.json()
      payload = {
        "id": user["id"],
        "email": user["email"],
        "bio": user["bio"],
        "avatar": user["avatar"],
        "researcher": user["researcher"]
      }
      token = create_token(payload)
      return {"user" : payload, "token": token}, 200
    return {"msg": "Unauthorized access"}, 401

  #handles checking for user session
class CheckSession(Resource):
  def get(self):
    token = strip_token(request)
    if token:
      payload = read_token(token)
      return payload, 200
    return {"msg": "Unauthorized access"}, 401


#handle register
class Register(Resource):
  def post(self):
    data = request.get_json()
    params = {
        "name": data['name'],
        "email": data['email'],
        "bio": '',
        "avatar": '',
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

#handles updating user avatar
class Update_user_avatar(Resource):
  def put(self, id):
    if "avatar" not in request.files:
      return {"msg": "Error"}, 400
    file = request.files['avatar']
    if file and allowed_file(file.filename):
      file.filename = secure_filename(file.filename)
      uploaded = upload_file(file)
      user = User.find_user_by_id(id)
      if user:
        for key in {"avatar": uploaded}:
          setattr(user, key, file[key])
      db.session.commit()
      return user.json(), 200
    return {"msg": "Error"}, 400

#handles getting all users
class Get_all_users(Resource):
  def get(self):
    raw_users = User.find_all_users()
    users = [user.json() for user in raw_users]
    return users






