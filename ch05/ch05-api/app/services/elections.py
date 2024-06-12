from flask import current_app
from flask.signals import Namespace
#from blinker import Signal, Namespace
from app.repository.election import ElectionRepository
from app.model.config import db_session
from app.model.db import Election
from datetime import datetime

election_ns = Namespace()
check_election = election_ns.signal('check_election')
approve_election= election_ns.signal('approve_election')
list_elections = election_ns.signal('list_elections')

@check_election.connect
async def check_election_event(app, election_date):
    async with db_session() as sess:
        async with sess.begin(): 
            repo = ElectionRepository(sess)
            records = await repo.select_all_election()
            election_rec = [rec.to_json() for rec in records if rec.election_date == datetime.strptime(election_date, '%Y-%m-%d').date()]
            if len(election_rec) > 0:
                return True
            return False

@approve_election.connect
async def create_election_event(app, details):
    try:
        async with db_session() as sess:
            repo = ElectionRepository(sess)
            election = Election(**details)
            result = await repo.insert_election(election)
            if result:
                return True
            else:
                return False
    except:
        return False

@list_elections.connect
async def list_elections_event(app):
    async with db_session() as sess:
        async with sess.begin(): 
            repo = ElectionRepository(sess)
            records = await repo.select_all_election()
            election_rec = [rec.to_json() for rec in records]
            return election_rec