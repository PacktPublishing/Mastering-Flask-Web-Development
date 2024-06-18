from flask import jsonify, current_app, request
from modules.repository.vaccine import VaccineRepository
from modules.models.config import db_session
from modules.models.db import Vaccine
from modules import auth

@current_app.post('/vaccine/add')
@auth.login_required(role="1")
async def add_vaccine():
  vac_json = request.get_json()
  async with db_session() as sess:
    async with sess.begin(): 
      repo = VaccineRepository(sess)
      vac = Vaccine(**vac_json)
      result = await repo.insert_vaccine(vac)
      if result == False:
          return jsonify(message="error in insert"), 201
      return jsonify(record=vac_json), 200

@current_app.delete('/vaccine/delete/<int:id>')
@auth.login_required(role="0")
async def del_vaccine(id:int):
    async with db_session() as sess:
      async with sess.begin(): 
          repo = VaccineRepository(sess)
          result = await repo.delete_vaccine(id)
          if result == False:
               return jsonify(message="error in delete"), 500
          return jsonify(record="deleted record"), 200
      
@current_app.delete('/vaccine/delete/<string:vacid>')
async def del_vaccine_vacid(vacid:str):
    async with db_session() as sess:
      async with sess.begin(): 
          repo = VaccineRepository(sess)
          result = await repo.delete_vaccine_vacid(vacid)
          if result == False:
               return jsonify(message="error in delete"), 500
          return jsonify(record="deleted record"), 200