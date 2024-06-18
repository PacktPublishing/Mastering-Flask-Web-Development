from flask import current_app, request, jsonify
from modules.repository.doctor import DoctorRepository
from modules.models.config import db_session
from modules.models.db import Doctor
from modules import auth

@current_app.post('/doctor/profile/add')
@auth.login_required(role="1")
async def add_doctor_profile():
  doctor_json = request.get_json()
  username = doctor_json["username"]
  if not username == 'None': 
      return jsonify(message="no valid username"), 201
  else:
      async with db_session() as sess:
        async with sess.begin(): 
          repo = DoctorRepository(sess)
          doc = Doctor(**doctor_json)
          result = await repo.insert_doctor(doc)
          if result == False:
              return jsonify(message="error in insert"), 201
          return jsonify(record=doctor_json), 200


@current_app.delete('/doctor/profile/delete/<int:id>')
@auth.login_required(role="1")
async def del_doctor_profile_id(id:int):
    async with db_session() as sess:
      async with sess.begin(): 
          repo = DoctorRepository(sess)
          result = await repo.delete_doc(id)
          if result == False:
               return jsonify(message="error in delete"), 201
          return jsonify(record="deleted record"), 200


@current_app.delete('/doctor/profile/delete/<string:username>')
async def del_doctor_profile_username(username:str):
    async with db_session() as sess:
      async with sess.begin(): 
          repo = DoctorRepository(sess)
          result = await repo.delete_doc_username(username)
          if result == False:
               return jsonify(message="error in delete"), 201
          return jsonify(record="deleted record"), 200