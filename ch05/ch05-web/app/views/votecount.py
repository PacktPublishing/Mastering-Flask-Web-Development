from flask import current_app, jsonify, render_template, Response
from app import sock
from  datetime import datetime
from json import loads
from asyncio import run

from app.model.db import VoteCount
from app.repository.votecount import VoteCountRepository
from app.model.config import db_session


@current_app.route('/ch05/votecount/add')
async def add_vote_count_client():
    return render_template('vote_count_add.html')

@sock.route('/ch05/vote/save/ws')
def add_vote_count_server(ws):
    async def add_vote_count():
        while True:
            vote_count_json = ws.receive()
            print(vote_count_json)
            vote_count_dict = loads(vote_count_json)
            print(vote_count_dict)
            async with db_session() as sess:
               async with sess.begin(): 
                    repo = VoteCountRepository(sess)
                    vote_count = VoteCount(**vote_count_dict)
                    result = await repo.insert(vote_count)
                    if result:
                        ws.send("data added")
                    else:
                        ws.send("data not added")
    run(add_vote_count())
        