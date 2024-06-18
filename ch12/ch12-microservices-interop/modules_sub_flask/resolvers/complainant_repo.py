from ariadne import QueryType, MutationType
from typing import List, Any, Dict
from modules_sub_flask.models.db import Complainant
from sqlalchemy.orm import Session


query = QueryType()
mutation = MutationType()

class ComplainantResolver:
    def __init__(self, sess:Session):
        self.sess = sess
    
    @mutation.field('complainant')
    def insert_complainant(self, obj, info, input) -> bool:
        try:
            
            complainant = Complainant(**input)
            self.sess.add(complainant)
            self.sess.commit()
            payload = {
                "success": True,
                "model": complainant
            }
        except Exception as e:
            print(e) 
            payload = {
                "success": False,
                "errors": [f"Complainant matching  not found"]
            }
        return payload
    
    def update_complainant(self, obj, info, id:int, details:Dict[str, Any]) -> bool:
        try:
            self.sess.query(Complainant).filter(Complainant.id == id).update(details)     
            self.sess.commit() 
            payload = {
                "success": True,
                "message": [f"Update Complainant succeeded."]
            }
           
        except Exception as e:
            print(e)
            payload = {
                "success": False,
                "errors": [f"Update Complainant found errors."]
            }
        return payload  
    
    def delete_complainant(self, obj, info, id:int) -> bool:
        try:
           self.sess.query(Complainant).filter(Complainant.id == id).delete()
           self.sess.commit()
           payload = {
                "success": True,
                "message": [f"Delete Complainant succeeded."]
            }
        except Exception as e:
            print(e)  
            payload = {
                "success": False,
                "errors": [f"Delete Complainant found errors."]
            }
        return payload
    
    def select_all_complainant(self, obj, info) -> List[Any]:
        complainants = self.sess.query(Complainant).all()
    
        try:
            records = [todo.to_json() for todo in complainants]
            print(records)
            payload = {
                "success": True,
                "complainants": records
            }
        except Exception as e:
            print(e)
            payload = {
                "success": False,
                "errors": [str("Empty records")]
            }
        return payload
        
    
    def select_complainant(self, obj, info, id:int) -> Any:
        admin =  self.sess.query(Complainant).filter(Complainant.id == id).one_or_none()
        return admin
    