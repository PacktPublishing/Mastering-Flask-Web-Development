from app.models.db import InvoiceRequest
from app.models.db import database
from typing import Dict, Any

class InvoiceRequestRepository:
    def insert_invoice_req(self, details:Dict[str, Any]) -> bool: 
        try:
            with database.atomic() as tx:
                InvoiceRequest.create(**details)
                tx.commit()
                return True
        except Exception as e: 
            print(e)
        return False
    
    def update_invoice_req(self, details:Dict[str,Any]) -> bool: 
       try:
           with database.atomic() as tx:
                invreq = InvoiceRequest.get(InvoiceRequest.code==details["code"])
                invreq.pcode = details["pcode"]
                invreq.purchase_date = details["purchase_date"]
                
                invreq.save()
                tx.commit()
                return True
       except Exception as e: 
           print(e)
       return False
   
    def delete_invreq_code(self, code:str) -> bool: 
        try:
           with database.atomic() as tx:
            invreq = InvoiceRequest.get(InvoiceRequest.code==code)
            invreq.delete_instance()
            tx.commit()
            return True
        except Exception as e: 
            print(e)
        return False
    
    def delete_invreq_id(self, id:int) -> bool: 
        try:
           with database.atomic() as tx:
            invreq = InvoiceRequest.get(InvoiceRequest.id==id)
            invreq.delete_instance()
            tx.commit()
            return True
        except Exception as e: 
            print(e)
        return False
    
    def select_invreq_code(self, code:str): 
        invreq = InvoiceRequest.select(InvoiceRequest.code==code)
        return invreq.to_json()
    
    def select_invreq_id(self, id:int): 
        invreq = InvoiceRequest.select(InvoiceRequest.id==id)
        return invreq.to_json()
    
    def select_all_invreq(self): 
        increqs = InvoiceRequest.select()
        records = [log.to_json() for log in increqs]
        return records
    
    