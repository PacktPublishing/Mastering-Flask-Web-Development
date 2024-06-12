from reactivex import Observable, Observer, create
from reactivex.disposable import Disposable
from app.model.db import VoteCount
from app.repository.votecount import VoteCountRepository
from app.model.config import db_session
from json import dumps
from asyncio import ensure_future

async def extract_precinct_tally(rec_dict):
    del rec_dict['id']
    del rec_dict['election_id']
    del rec_dict['approved_date']
    return str(rec_dict)

async def create_tally_data(observer):
    async with db_session() as sess:
          async with sess.begin(): 
            repo = VoteCountRepository(sess)
            records = await repo.select_all_votecount()
            votecount_rec = [rec.to_json() for rec in records]
            print(votecount_rec)
            for vc in votecount_rec:
                rec_str = await extract_precinct_tally(vc)
                observer.on_next(rec_str)
            observer.on_completed()
            
def create_observable(loop) -> Observable:
  def on_subscribe(observer: Observer, scheduler):
     task = ensure_future(create_tally_data(observer), loop=loop)
     return Disposable(lambda: task.cancel())    
  return create(on_subscribe)