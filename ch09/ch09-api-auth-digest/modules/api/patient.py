from flask import jsonify, current_app, request
from modules.repository.patient import PatientRepository
from modules.models.config import db_session
from modules.models.db import Patient
from modules import auth

@current_app.post('/patient/profile/add')
@auth.login_required(role="2")
async def add_patient_profile():
        patient_json = request.get_json()
        username = patient_json['username']
        if not username == 'None': 
           return jsonify(message="no valid username"), 201
        else:
            async with db_session() as sess:
                async with sess.begin(): 
                    repo = PatientRepository(sess)
                    patient = Patient(**patient_json)
                    result = await repo.insert_patient(patient)
                    if result == False:
                        return jsonify(message="error in insert"), 201
                    return jsonify(record=patient_json), 200

@current_app.delete('/patient/profile/delete/<int:id>')
@auth.login_required(role="2")
async def del_patient_profile_id(id:int):
    async with db_session() as sess:
      async with sess.begin(): 
          repo = PatientRepository(sess)
          result = await repo.delete_patient(id)
          if result == False:
               return jsonify(message="error in delete"), 500
          return jsonify(record="deleted record"), 200


@current_app.delete('/patient/profile/delete/<string:username>')
@auth.login_required(role="2")
async def del_patient_profile_username(username:str):
    async with db_session() as sess:
      async with sess.begin(): 
          repo = PatientRepository(sess)
          result = await repo.delete_patient_username(username)
          if result == False:
               return jsonify(message="error in delete"), 500
          return jsonify(record="deleted record"), 200