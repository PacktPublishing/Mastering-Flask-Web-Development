from app import sock
from flask import jsonify, current_app, request, make_response

from simple_websocket import  Client
from app.repository.vote import VoteRepository
from app.model.config import db_session
from app.model.db import Vote
from json import dumps, loads
from asyncio import run

@current_app.post("/ch05/check/vote/counts/client")
def bulk_check_vote_count():
    ws = Client('ws://127.0.0.1:5000/ch05/check/vote/counts/ws', headers={"Access-Control-Allow-Origin": "*"})
    candidates = request.get_json()
    for candidate in candidates:
            try:
                print(f'client sent: {candidate}')
                ws.send(dumps(candidate))
                vote_count = ws.receive()
                print(f'client recieved: {vote_count}')
            except Exception as e:
                print(e) 
    return jsonify(message="done client transaction"), 201
  
@sock.route("/ch05/check/vote/counts/ws")
def bulk_check_vote_count_ws(websocket):
   async def vote_count():
      while True:
        try:
          candidate = websocket.receive()
          candidate_map = loads(candidate)
          print(f'server received: {candidate_map}')
          async with db_session() as sess:
            async with sess.begin(): 
               repo = VoteRepository(sess)
               count = await repo.count_votes_by_candidate(candidate_map["cand_id"], int(candidate_map["election_id"]))
               vote_count_data = {"cand_id": candidate_map["cand_id"], "vote_count": count}
               websocket.send(dumps(vote_count_data))
               print(f'server sent: {candidate_map}')
        except  Exception as e:
          print(e)
          break 
   run(vote_count())
