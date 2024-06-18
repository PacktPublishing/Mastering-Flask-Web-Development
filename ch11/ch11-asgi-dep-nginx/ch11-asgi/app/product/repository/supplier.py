from app.models.db import Supplier
from app.models.db import database
from app import conn_mgr
from typing import Dict, Any


class SupplierRepository:
    
    async def insert_supplier(self, details:Dict[str, Any]) -> bool: 
        try:
            async with database.atomic_async() as tx:
                await conn_mgr.create(Supplier, **details)
                await tx.commit()
                return True
        except Exception as e: 
            print(e)
        return False
    
    async def update_supplier(self, details:Dict[str,Any]) -> bool: 
       try:
           async with database.atomic_async():
                supplier = await conn_mgr.get(Supplier, code=details["sid"])
                supplier.company = details["company"]
                supplier.email = details["email"]
                supplier.bank_name = details["bank_name"]
                supplier.bank_account = details["bank_account"]
                supplier.mobile = details["mobile"]
                supplier.approved_date = details["approved_date"]
                               
                await conn_mgr.update(supplier, only=("sid", "company", "email", "bank_name", "bank_account", "mobile", "approved_date"))
                return True
       except Exception as e: 
           print(e)
       return False
   
    async def delete_supplier_sid(self, sid:str) -> bool: 
        try:
           async with database.atomic_async():
            supplier = await conn_mgr.get(Supplier, sid=sid)
            await conn_mgr.delete(supplier)
            return True
        except Exception as e: 
            print(e)
        return False
    
    async def delete_supplier_id(self, id:int) -> bool: 
        try:
           async with database.atomic_async():
            supplier = await conn_mgr.get(Supplier, id=id)
            await conn_mgr.delete(supplier)
            return True
        except Exception as e: 
            print(e)
        return False
    
    async def select_supplier_sid(self, sid:str): 
        supplier = await conn_mgr.get(Supplier, sid=sid)
        return supplier.to_json()
    
    async def select_supplier_id(self, id:int): 
        supplier = await conn_mgr.get(Supplier, id=id)
        return supplier.to_json()
    
    async def select_all_supplier(self): 
        suppliers = await conn_mgr.execute(Supplier.select())
        records = [log.to_json() for log in suppliers]
        return records
    
    