from flask import jsonify, current_app, request, make_response, abort

from app.model.db import Member
from app.repository.member import MemberRepository
from app.model.config import db_session
from asyncio import create_task, ensure_future, InvalidStateError
from app.exceptions.db import DuplicateRecordException

@current_app.post("/ch05/member/add")
async def add_member():
    async with db_session() as sess:
        async with sess.begin(): 
            repo = MemberRepository(sess)
            member_json = request.get_json()
            member = Member(**member_json)
            try:
                insert_task = create_task(repo.insert(member))
                await insert_task
                result = insert_task.result()
                if result:
                    content = jsonify(member_json)
                    return make_response(content, 201)
                else:
                    raise DuplicateRecordException("insert member record failed")
            except InvalidStateError:
                abort(500)

@current_app.get("/ch05/member/list/all")
async def list_all_member():
     async with db_session() as sess:
        async with sess.begin(): 
            repo = MemberRepository(sess)
            list_member_task = ensure_future(repo.select_all_member())
            await list_member_task
            records = list_member_task.result()
            member_rec = [rec.to_json() for rec in records]
            return make_response(member_rec, 201)

