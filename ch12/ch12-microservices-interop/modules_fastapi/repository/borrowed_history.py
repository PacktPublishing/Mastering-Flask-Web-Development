from typing import Dict, Any
from sqlalchemy.orm import Session
from modules_fastapi.models.db import BorrowedHist
from sqlalchemy import desc


class BorrowedHistRepository: 
    
    def __init__(self, sess:Session):
        self.sess:Session = sess
    
    def insert(self, bh: BorrowedHist) -> bool: 
        try:
            self.sess.add(bh)
            self.sess.commit()
            return True
        except Exception as e: 
            print(e)
        return False 
        
    
    def update(self, id:int, details:Dict[str, Any]) -> bool: 
       try:
             self.sess.query(BorrowedHist).filter(BorrowedHist.id == id).update(details)     
             self.sess.commit() 
             return True
       except Exception as e: 
            print(e)
       return False 
   
    def delete_empid(self, empid:str) -> bool: 
        try:
           self.sess.query(BorrowedHist).filter(BorrowedHist.empid == empid).delete()
           self.sess.commit()
           return True
        except Exception as e: 
            print(e)
        return False 
    
    def get_all_borrowed_hist(self):
        return self.sess.query(BorrowedHist).all() 
    
    def get_all_history_where(self, empid:str):
        return self.sess.query(BorrowedHist).filter(BorrowedHist.empid == empid).all() 
    
    