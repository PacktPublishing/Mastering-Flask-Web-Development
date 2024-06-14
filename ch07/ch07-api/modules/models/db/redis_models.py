
from redis_om import  HashModel, Field, get_redis_connection

redis_conn = get_redis_connection(decode_responses=True)


class SearchCourse(HashModel):
    code: str  = Field(index=True)
    title: str 
    description: str 
    req_hrs: float
    total_cost: float
    level: int
   
class SearchStudent(HashModel):
    std_id: str
    firstname: str
    midname: str
    lastname: str
    age: int
    email: str
    attainment: str
    occupation: str
    
    class Meta:
        database = redis_conn
        
class SearchTutor(HashModel):
    firstname: str
    lastname: str
    midname: str
    position: str
    email: str
    company: str  
        
    class Meta:
        database = redis_conn
        
