from typing import Dict, Any
from modules.models.db.mongo_models import Savings, TutorLogin

class SavingsRepository:
    def __init__(self):
        pass
        
    def add_savings(self, details:Dict[str, Any]): 
        try:
           login = TutorLogin.objects(id=details['id']).get()
           del details['id']
           savings = Savings(**details)
           login.update(push__tutor__savings=savings)
        except Exception as e:
            print(e)
            return False 
        return True
    
    def delete_savings(self, details:Dict[str, Any]):
        try:
            login = TutorLogin.objects(id=details['id']).get()
            login.update(pull__tutor__savings__acct_number=details['acct_number'])
        except Exception as e:
            print(e)
            return False 
        return True