from app.models.db import Supplier
from app.models.db import database
from typing import Dict, Any


class SupplierRepository:
    
    def insert_supplier(self, details:Dict[str, Any]) -> bool: 
        try:
            with database.atomic() as tx:
                Supplier.create(**details)
                tx.commit()
                return True
        except Exception as e: 
            print(e)
        return False
    
    def update_supplier(self, details:Dict[str,Any]) -> bool: 
       try:
           with database.atomic() as tx:
                supplier = Supplier.get(Supplier.code==details["sid"])
                supplier.company = details["company"]
                supplier.email = details["email"]
                supplier.bank_name = details["bank_name"]
                supplier.bank_account = details["bank_account"]
                supplier.mobile = details["mobile"]
                supplier.approved_date = details["approved_date"]
                               
                supplier.save()
                tx.commit()
                return True
       except Exception as e: 
           print(e)
       return False
   
    def delete_supplier_sid(self, sid:str) -> bool: 
        try:
           with database.atomic() as tx:
            supplier = Supplier.get(Supplier.sid==sid)
            supplier.delete_instance()
            tx.commit()
            return True
        except Exception as e: 
            print(e)
        return False
    
    def delete_supplier_id(self, id:int) -> bool: 
        try:
           with database.atomic() as tx:
            supplier = Supplier.get(Supplier.id==id)
            supplier.delete_instance()
            tx.commit()
            return True
        except Exception as e: 
            print(e)
        return False
    
    def select_supplier_sid(self, sid:str): 
        supplier = Supplier.select(Supplier.sid==sid)
        return supplier.to_json()
    
    def select_supplier_id(self, id:int): 
        supplier = Supplier.select(Supplier.id==id)
        return supplier.to_json()
    
    def select_all_supplier(self): 
        suppliers = Supplier.select()
        records = [log.to_json() for log in suppliers]
        return records
    
    