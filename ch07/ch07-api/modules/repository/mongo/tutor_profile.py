from typing import Dict, Any
from modules.models.db.mongo_models import TutorLogin, Tutor

class TutorProfileRepository:
    
    def __init__(self):
        pass
        
    def add_tutor_profile(self, details:Dict[str, Any]) -> bool: 
        try:
            login = TutorLogin.objects(id=details['id']).get()
            del details['id']
            profile = Tutor(**details)
            login.update(tutor=profile)
        except Exception as e:
            print(e)
            return False 
        return True
    
    def delete_tutor_profile(self, id:int) -> bool: 
        try:
            login = TutorLogin.objects(id=id).get()
            login.update(tutor=None)
        except Exception as e:
            print(e)
            return False 
        return True
    
    