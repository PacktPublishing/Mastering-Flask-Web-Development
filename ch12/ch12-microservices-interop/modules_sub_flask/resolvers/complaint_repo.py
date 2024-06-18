from ariadne import QueryType, MutationType
from typing import List, Any, Dict
from modules_sub_flask.models.db import Complaint
from sqlalchemy.orm import Session

query = QueryType()
mutation = MutationType()

class ComplaintResolver:
    def __init__(self, sess:Session):
        self.sess = sess
    
    @mutation.field('complaint')
    def insert_complaint(self, obj, info, input) -> bool:
        try:
            
            complaint = Complaint(**input)
 
            self.sess.add(complaint)
            self.sess.flush()
            self.sess.commit()
            payload = {
                "success": True,
                "model": complaint
            }
           
        except Exception as e:
            print(e) 
            payload = {
                "success": False,
                "errors": [f"Complaint matching  not found"]
            }
        return payload
    
    def update_complaint_ticketId(self, obj, info, ticketId:str, details:Dict[str, Any]) -> bool:
        try:
            self.sess.query(Complaint).filter(Complaint.ticketId== ticketId).update(details)     
            self.sess.commit() 
            payload = {
                "success": True,
                "message": [f"Update Complaint succeeded."]
            }
           
        except Exception as e:
            print(e)
            payload = {
                "success": False,
                "errors": [f"Update Complaint Type found errors."]
            }
        return payload  
    
    def delete_complaint_ticketId(self, obj, info, ticketId:str) -> bool:
        try:
           self.sess.query(Complaint).filter(Complaint.ticketId == ticketId).delete()
           self.sess.commit()
           payload = {
                "success": True,
                "message": [f"Delete Complaint succeeded."]
            }
        except Exception as e:
            print(e)  
            payload = {
                "success": False,
                "errors": [f"Delete Complaint found errors."]
            }
        return payload
    
    def select_all_complaint(self, obj, info) -> List[Any]:
        complaints = self.sess.query(Complaint).all()
    
        try:
            records = [todo.to_json() for todo in complaints]
            
            payload = {
                "success": True,
                "complaints": records
            }
            print(payload)
            return payload
        except Exception as e:
            print(e)
            payload = {
                "success": False,
                "errors": [str("Empty records")]
            }
        return payload
        
    
    def select_complaint(self, obj, info, id:int) -> Any:
        complaint =  self.sess.query(Complaint).filter(Complaint.id == id).one_or_none()
        return complaint
    

    