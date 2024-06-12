from flask import jsonify, current_app, request, make_response
from app.services.vote_count import create_observable
from json import loads
from asyncio import get_event_loop, Future

from app.repository.vote import VoteRepository
from app.model.config import db_session
from app.model.db import Vote

@current_app.get("/ch05/votecount/tally")
async def list_votecount_tally():
    done = Future()
    loop = get_event_loop()
    
    def on_completed():
        done.set_result(0)
        
    tally = []
    disposable = create_observable(loop).subscribe(
                    on_next = lambda i: tally.append(i),
                    on_error = lambda e: print("Error Occurred: {0}".format(e)),
                    on_completed = on_completed)
    await done
    disposable.dispose()
    return jsonify(tally=tally), 201



@current_app.get('/ch05/vote/candidate/<int:election_id>/<string:cand_id>')     
async def vote_count(election_id:int, cand_id:str):
  async with db_session() as sess:
        async with sess.begin(): 
            repo = VoteRepository(sess)
            records = await repo.count_votes_by_candidate(cand_id, election_id)
            return jsonify(value=records), 201