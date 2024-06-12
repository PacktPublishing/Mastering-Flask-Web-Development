from flask import jsonify, current_app, request, make_response, abort

from app.model.db import Login
from app.repository.login import LoginRepository
from app.model.config import db_session

@current_app.post('/ch05/login/add')
async def add_login():
   async with db_session() as sess:
        async with sess.begin(): 
            repo = LoginRepository(sess)
            login_json = request.get_json()
            login = Login(**login_json)
            result = await repo.insert_login(login)
            if result:
                content = jsonify(login_json)
                return make_response(content, 201)
            else:
                abort(500)
        
            
@current_app.get("/ch05/login/list/all")
async def list_all_login():
    async with db_session() as sess:
        async with sess.begin(): 
            repo = LoginRepository(sess)
            records = await repo.select_all_login()
            login_rec = [rec.to_json() for rec in records]
            return make_response(login_rec, 201)
        