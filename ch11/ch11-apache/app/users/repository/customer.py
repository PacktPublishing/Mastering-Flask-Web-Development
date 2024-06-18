from app.models.db import Customer
from app.models.db import database
from typing import Dict, Any


class CustomerRepository:
    
    def insert_customer(self, details:Dict[str, Any]) -> bool: 
        try:
            with database.atomic() as tx:
                Customer.create(**details)
                tx.commit()
                return True
        except Exception as e: 
            print(e)
        return False
    
    def update_customer(self, details:Dict[str,Any]) -> bool: 
       try:
           with database.atomic() as tx:
                customer = Customer.get(Customer.username==details["username"])
                customer.custid = details["custid"]
                customer.type = details["type"]
                customer.firstname = details["firstname"]
                customer.lastname = details["lastname"]
                customer.position = details["position"]
                customer.email = details["email"]
                customer.mobile = details["mobile"]
                customer.enrolled_date = details["enrolled_date"]
                
                customer.save()
                tx.commit()
                return True
       except Exception as e: 
           print(e)
       return False
   
    def delete_customer_username(self, username:str) -> bool: 
        try:
           with database.atomic() as tx:
            customer = Customer.get(Customer.username==username)
            customer.delete_instance()
            tx.commit()
            return True
        except Exception as e: 
            print(e)
        return False
    
    def delete_customer_id(self, custid:str) -> bool: 
        try:
           with database.atomic() as tx:
            customer = Customer.get(Customer.custid==custid)
            customer.delete_instance()
            tx.commit()
            return True
        except Exception as e: 
            print(e)
        return False
    

    def select_customer_username(self, username:str): 
        customer = Customer.select(Customer.username==username)
        return customer.to_json()
    
    def select_customer_empid(self, custid:str): 
        customer = Customer.select(Customer.custid==custid)
        return customer.to_json()
    
    def select_all_login(self): 
        custs = Customer.select()
        records = [log.to_json() for log in custs]
        return records
    
    