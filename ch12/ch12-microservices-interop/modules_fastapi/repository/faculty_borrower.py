from typing import Dict, Any
from sqlalchemy.orm import Session
from modules_fastapi.models.db import FacultyBorrower
from sqlalchemy import desc


class FacultyBorrowerRepository: 
    
    def __init__(self, sess:Session):
        self.sess:Session = sess
    
    def insert(self, fb: FacultyBorrower) -> bool: 
        try:
            self.sess.add(fb)
            self.sess.commit()
            return True
        except Exception as e: 
            print(e)
        return False 
        
    
    def update(self, id:int, details:Dict[str, Any]) -> bool: 
       try:
             self.sess.query(FacultyBorrower).filter(FacultyBorrower.id == id).update(details)     
             self.sess.commit() 
             return True
       except Exception as e: 
            print(e)
       return False 
   
    def delete_empid(self, empid:str) -> bool: 
        try:
           self.sess.query(FacultyBorrower).filter(FacultyBorrower.empid == empid).delete()
           self.sess.commit()
           return True
        except Exception as e: 
            print(e)
        return False 
    
    def get_all_faculty_borrowers(self):
        return self.sess.query(FacultyBorrower).all() 
    
    def get_all_borrowers_where(self, empid:str):
        return self.sess.query(FacultyBorrower).filter(FacultyBorrower.empid == empid).all() 
    
    