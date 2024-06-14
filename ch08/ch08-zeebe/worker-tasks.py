from pyzeebe import ZeebeWorker, create_insecure_channel
import asyncio
from modules.settings import Zeebe
import json
from datetime import date

from modules.models.config import db_session, init_db
from modules.doctors.repository.diagnosis import DiagnosisRepository

print('starting the Zeebe worker...')
print('initialize database connectivity...')
init_db()

channel = create_insecure_channel()
worker = ZeebeWorker(channel, max_connection_retries=Zeebe.ZEEBE_MAX_CONNECTION_RETRIES)

@worker.task(task_type="select_diagnosis", **Zeebe.TASK_DEFAULT_PARAMS)
async def select_diagnosis(docid, patientid):
    async with db_session() as sess:
         async with sess.begin(): 
            try:
               repo = DiagnosisRepository(sess)
               records = await repo.select_diag_doc_patient(docid, patientid)
               diagnosis_rec = [rec.to_json() for rec in records]
               diagnosis_str = json.dumps(diagnosis_rec, default=json_date_serializer)
               return {"data": diagnosis_str}
            except Exception as e:
               print(e)
            return {"data": json.dumps([])}
         
@worker.task(task_type="retrieve_analysis", **Zeebe.TASK_DEFAULT_PARAMS)
async def retrieve_analysis(records):
   try:
      records_diagnosis = json.loads(records)
      diagnosis_text = [dt['resolution'] for dt in records_diagnosis]
      return {"result": diagnosis_text}
   except Exception as e:
      print(e)
   return {"result": []} 

def json_date_serializer(obj):
    if isinstance(obj, date):
        return obj.isoformat()
    raise TypeError ("Type %s not serializable" % type(obj))

if __name__ == "__main__":
   loop = asyncio.get_event_loop()
   loop.run_until_complete(worker.work()) 
   
