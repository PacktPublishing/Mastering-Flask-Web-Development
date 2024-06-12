from typing import List, Any, Dict
from app.model.db import Employee
from flask import current_app
from sqlalchemy.orm import Session

class EmployeeRepository:
    def __init__(self, sess:Session):
        self.sess = sess
        current_app.logger.info('EmployeeRepository instance created')
        
    def insert(self, emp:Employee) -> bool:
        try:
            self.sess.add(emp)
            self.sess.commit()
            current_app.logger.info('EmployeeRepository inserted record')
            return True
        except Exception as e:
            current_app.logger.error(f'EmployeeRepository insert error: {e}') 
        return False
    
    def update(self, empid:str, details:Dict[str, Any]) -> bool:
        try:
            self.sess.query(Employee).filter(Employee.empid == empid).update(details)     
            self.sess.commit() 
            current_app.logger.info('EmployeeRepository updated record')
            return True
        except Exception as e:
            current_app.logger.error(f'EmployeeRepository update error: {e}') 
        return False  
    
    def delete(self, empid:str) -> bool:
        try:
           login = self.sess.query(Employee).filter(Employee.empid == empid).delete()
           self.sess.commit()
           current_app.logger.info('EmployeeRepository deleted record')
           return True
        except Exception as e:
           current_app.logger.error(f'EmployeeRepository delete error: {e}')  
        return False
    
    def select_all(self) -> List[Any]:
        emps = self.sess.query(Employee).all()
        current_app.logger.info('EmployeeRepository retrieved all record')
        return emps
    
     
    def select_one(self, empid:str) -> Any:
        emp =  self.sess.query(Employee).filter(Employee.empid == empid).one_or_none()
        current_app.logger.info('EmployeeRepository retrieved one record')
        return emp