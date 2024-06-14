from typing import Dict, Any
from modules.models.db.mongo_models import PayPal, TutorLogin


class PayPalRepository:
    def __init__(self, login:TutorLogin):
        self.login = login
        
    def add_creditcard(self, details:Dict[str, Any]): 
        try:
           paypal = PayPal(**details)
           self.login.tutor.paypal = paypal
           self.login.update(tutor=self.login.tutor)
        except Exception as e:
            print(e)
            return False 
        return True
    
    def delete_creditcard(self):
        try:
            self.login.tutor.update(paypal=None)
            self.login.update(tutor=self.login.tutor)
        except Exception as e:
            print(e)
            return False 
        return True