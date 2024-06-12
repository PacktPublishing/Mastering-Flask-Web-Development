from quart import jsonify, current_app, request, make_response

from app.model.db import Login
from app.repository.login import LoginRepository
from app.model.config import db_session

async def add_login():
   async with db_session() as sess:
            repo = LoginRepository(sess)
            login_json = request.get_json()
            login = Login(**login_json)
            result = await repo.insert(login)
            if result:
                content = jsonify(login_json)
                return await make_response(content, 201)
            else:
                content = jsonify(message="insert complaint details record encountered a problem")
                return await make_response(content, 500)
        
async def list_all_login():
    async with db_session() as sess:
        async with sess.begin(): 
            repo = LoginRepository(sess)
            records = await repo.select_all_login()
            login_rec = [rec.to_json() for rec in records]
            return await make_response(login_rec, 201)
        