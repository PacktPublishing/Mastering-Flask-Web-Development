from flask import jsonify, current_app, request
from modules.repository.admin import AdminRepository
from modules.models.config import db_session
from modules.models.db import Administrator
from modules import auth

@current_app.post('/admin/profile/add')
@auth.login_required
async def add_admin_profile():
        admin_json = request.get_json()
        username = admin_json['username']
        if not username == 'None': 
           return jsonify(message="no valid username"), 201
        else:
           async with db_session() as sess:
             async with sess.begin(): 
                repo = AdminRepository(sess)
                admin = Administrator(**admin_json)
                result = await repo.insert_admin(admin)
                if result == False:
                    return jsonify(message="error in insert"), 201
                return jsonify(record=admin_json), 200
        
    
@current_app.delete('/admin/profile/del/<int:id>')
@auth.login_required
async def del_admin_profile_id(id:int):
    async with db_session() as sess:
      async with sess.begin(): 
          repo = AdminRepository(sess)
          result = await repo.delete_admin(id)
          if result == False:
               return jsonify(message="error in delete"), 201
          return jsonify(record="deleted record"), 200
        


@current_app.delete('/admin/profile/del/<string:username>')
@auth.login_required
async def del_admin_profile_username(username:str):
    async with db_session() as sess:
      async with sess.begin(): 
          repo = AdminRepository(sess)
          result = await repo.delete_admin_username(username)
          if result == False:
               return jsonify(message="error in insert"), 201
          return jsonify(record="deleted record"), 200