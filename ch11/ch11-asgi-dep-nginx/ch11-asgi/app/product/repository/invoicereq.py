from app.models.db import InvoiceRequest
from app.models.db import database
from app import conn_mgr
from typing import Dict, Any

class InvoiceRequestRepository:
    async def insert_invoice_req(self, details:Dict[str, Any]) -> bool: 
        try:
            async with database.atomic_async() as tx:
                await conn_mgr.create(InvoiceRequest, **details)
                await tx.commit()
                return True
        except Exception as e: 
            print(e)
        return False
    
    async def update_invoice_req(self, details:Dict[str,Any]) -> bool: 
       try:
           async with database.atomic_async():
                invreq = await conn_mgr.get(InvoiceRequest, code=details["code"])
                invreq.pcode = details["pcode"]
                invreq.purchase_date = details["purchase_date"]
                
                await conn_mgr.update(invreq, only=("pcode", "purchase_date", ))
                return True
       except Exception as e: 
           print(e)
       return False
   
    async def delete_invreq_code(self, code:str) -> bool: 
        try:
           async with database.atomic_async():
            invreq = await conn_mgr.get(InvoiceRequest, code=code)
            await conn_mgr.delete(invreq)
            return True
        except Exception as e: 
            print(e)
        return False
    
    async def delete_invreq_id(self, id:int) -> bool: 
        try:
           async with database.atomic_async():
            invreq = await conn_mgr.get(InvoiceRequest, id=id)
            await conn_mgr.delete(invreq)
            return True
        except Exception as e: 
            print(e)
        return False
    
    async def select_invreq_code(self, code:str): 
        invreq = await conn_mgr.get(InvoiceRequest, code=code)
        return invreq.to_json()
    
    async def select_invreq_id(self, id:int): 
        invreq = await conn_mgr.get(InvoiceRequest, id=id)
        return invreq.to_json()
    
    async def select_all_invreq(self): 
        increqs = await conn_mgr.execute(InvoiceRequest.select())
        records = [log.to_json() for log in increqs]
        return records
    
    