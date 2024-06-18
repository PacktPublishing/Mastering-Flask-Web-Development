from app.models.db import Customer
from app.models.db import database
from app import conn_mgr
from typing import Dict, Any


class CustomerRepository:
    
    async def insert_customer(self, details:Dict[str, Any]) -> bool: 
        try:
            async with database.atomic_async() as tx:
                await conn_mgr.create(Customer, **details)
                await tx.commit()
                return True
        except Exception as e: 
            print(e)
        return False
    
    async def update_customer(self, details:Dict[str,Any]) -> bool: 
       try:
           async with database.atomic_async():
                customer = await conn_mgr.get(Customer, username=details["username"])
                customer.custid = details["custid"]
                customer.type = details["type"]
                customer.firstname = details["firstname"]
                customer.lastname = details["lastname"]
                customer.position = details["position"]
                customer.email = details["email"]
                customer.mobile = details["mobile"]
                customer.enrolled_date = details["enrolled_date"]
                
                await conn_mgr.update(customer, only=("custid", "type", "firstname", "lastname", "position", "email", "mobile", "enrolled_date"))
                return True
       except Exception as e: 
           print(e)
       return False
   
    async def delete_customer_username(self, username:str) -> bool: 
        try:
           async with database.atomic_async():
            customer = await conn_mgr.get(Customer, username=username)
            await conn_mgr.delete(customer)
            return True
        except Exception as e: 
            print(e)
        return False
    
    async def delete_customer_id(self, custid:str) -> bool: 
        try:
           async with database.atomic_async():
            customer = await conn_mgr.get(Customer, custid=custid)
            await conn_mgr.delete(customer)
            return True
        except Exception as e: 
            print(e)
        return False
    

    async def select_customer_username(self, username:str): 
        customer = await conn_mgr.get(Customer, username=username)
        return customer.to_json()
    
    async def select_customer_empid(self, custid:str): 
        customer = await conn_mgr.get(Customer, custid=custid)
        return customer.to_json()
    
    async def select_all_login(self): 
        custs = await conn_mgr.execute(Customer.select())
        records = [log.to_json() for log in custs]
        return records
    
    