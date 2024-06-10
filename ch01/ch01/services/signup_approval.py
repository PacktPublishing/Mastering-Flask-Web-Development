from repository.user import insert_user
from repository.admin import insert_admin
from repository.counselor import insert_counselor
from repository.patient import insert_patient
from typing import Dict, Any
from datetime import date

def user_approval_service(utype:int, model: Any) -> bool:
    try:
        insert_user(id=model.id, user=model.username, passw=model.password, user_approved=date.today())
        if utype == 1:
            insert_admin(id=model.id, age=model.age, fname=model.firstname, lname=model.lastname, position=model.position, emp_started=model.emp_date, emp_status=model.emp_status)
        elif utype == 2:
            insert_counselor(id=model.id, fname=model.firstname, lname=model.lastname, age=model.age, position=model.position, cid=model.cid, prof_started=model.prof_started)
        elif utype == 3:
            insert_patient(id=model.id, fname=model.firstname, lname=model.lastname, age=model.age, gender=model.gender, mobile=model.mobile, address=model.address, civil_status=model.cstatus, nationality=model.nationality, occupation=model.occupation, cid=model.cid, counsel_ended=model.counsel_ended, counsel_started=model.counsel_started )
        return True
    except Exception as e:
        print(e)
    return False