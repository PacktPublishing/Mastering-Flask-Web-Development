
from pydantic import BaseModel
from datetime import date

class BorrowerReq(BaseModel): 
    empid: str 
    firstname: str 
    lastname:str
   
        

