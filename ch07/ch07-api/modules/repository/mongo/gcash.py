from typing import Dict, Any
from modules.models.db.mongo_models import GCash, TutorLogin


class GCashRepository:
    def __init__(self, login:TutorLogin):
        self.login = login
        
    def add_creditcard(self, details:Dict[str, Any]): 
        try:
           gcash = GCash(**details)
           self.login.tutor.gcash = gcash
           self.login.update(tutor=self.login.tutor)
        except Exception as e:
            print(e)
            return False 
        return True
    
    def delete_creditcard(self):
        try:
            self.login.tutor.update(gcash=None)
            self.login.update(tutor=self.login.tutor)
        except Exception as e:
            print(e)
            return False 
        return True