from typing import Dict, Any
from modules.models.db.mongo_models import Checking, TutorLogin


class CheckingRepository:
    def __init__(self, login:TutorLogin):
        self.login = login
        
    def add_checking(self, details:Dict[str, Any]): 
        try:
           checking = Checking(**details)
           self.login.tutor.checkings.append(checking)
           self.login.update(tutor=self.login.tutor)
        except Exception as e:
            print(e)
            return False 
        return True
    
    def delete_checking(self, acct_number:str):
        try:
            checking = [acn for acn in self.login.tutor.checkings if acn.acct_number == acct_number]
            self.login.tutor.checkings.remove(checking[0])
            self.login.update(tutor=self.login.tutor)
        except Exception as e:
            print(e)
            return False 
        return True