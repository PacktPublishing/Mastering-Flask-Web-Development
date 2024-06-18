from ariadne import QueryType, MutationType
from typing import List, Any, Dict
from modules_sub_flask.models.db import ComplaintType
from sqlalchemy.orm import Session


query = QueryType()
mutation = MutationType()

class ComplaintTypeResolver:
    def __init__(self, sess:Session):
        self.sess = sess
    
 
    def insert_complaint_type(self, obj, info, name) -> bool:
        try:
            complaint_type = ComplaintType(name)
            self.sess.add(complaint_type)
            self.sess.commit()
            payload = {
                "success": True,
                "model": complaint_type
            }
        except Exception as e:
            print(e) 
            payload = {
                "success": False,
                "errors": [f"Complaint Type matching  not found"]
            }
        return payload
    
    def update_complaint_type(self, obj, info, id:int, details:Dict[str, Any]) -> bool:
        try:
            self.sess.query(ComplaintType).filter(ComplaintType.id == id).update(details)     
            self.sess.commit() 
            payload = {
                "success": True,
                "message": [f"Update Complaint Type succeeded."]
            }
           
        except Exception as e:
            print(e)
            payload = {
                "success": False,
                "errors": [f"Update Complaint Type found errors."]
            }
        return payload  
    
    def delete_complaint_type(self, obj, info, id:int) -> bool:
        try:
           self.sess.query(ComplaintType).filter(ComplaintType.id == id).delete()
           self.sess.commit()
           payload = {
                "success": True,
                "message": [f"Delete Complaint Type succeeded."]
            }
        except Exception as e:
            print(e)  
            payload = {
                "success": False,
                "errors": [f"Delete Complaint Type found errors."]
            }
        return payload
    
    def select_all_complaint_types(self, obj, info) -> List[Any]:
        complaint_types = self.sess.query(ComplaintType).all()
    
        try:
            records = [todo.to_json() for todo in complaint_types]
            print(records)
            payload = {
                "success": True,
                "complaint_types": records
            }
        except Exception as e:
            print(e)
            payload = {
                "success": False,
                "errors": [str("Empty records")]
            }
        return payload
        
    
    def select_complaint_type(self, obj, info, id:int) -> Any:
        ct =  self.sess.query(ComplaintType).filter(ComplaintType.id == id).one_or_none()
        return ct
    