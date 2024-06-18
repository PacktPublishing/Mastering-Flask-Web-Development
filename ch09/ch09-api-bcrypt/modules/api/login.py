from flask import jsonify, current_app, request
from modules.repository.login import LoginRepository
from modules.models.config import db_session
from modules.models.db import Login
from modules import bcrypt

import asyncio

@current_app.post('/login/signup')
async def add_signup():
     login_json = request.get_json()
     password = login_json["password"]
     passphrase = bcrypt.generate_password_hash(password).decode('utf-8') 
     async with db_session() as sess:
          async with sess.begin(): 
            repo = LoginRepository(sess)
            login = Login(username=login_json["username"], password=passphrase, role=login_json["role"])
            result = await repo.insert_login(login)
            if result == False:
                return jsonify(message="error in insert"), 201
            return jsonify(record=login_json), 200

@current_app.post('/login/auth')
async def login_valid_user():
    login_json = request.get_json()
    username = login_json["username"]
    password = login_json["password"]
    async with db_session() as sess:
      async with sess.begin(): 
          repo = LoginRepository(sess)
          login_rec = await repo.select_login_username(username)
          if len(login_rec) == 0:
               return jsonify(message="user does not exist"), 403
          login:Login = login_rec[0]
          if bcrypt.check_password_hash(login.password, password) == True:
                return jsonify(record="authenticated user"), 201
          else:
               return jsonify(message="invalid user"), 403
          
          
@current_app.get("/logout")
async def logout():
    return jsonify(record="logged-out user"), 201