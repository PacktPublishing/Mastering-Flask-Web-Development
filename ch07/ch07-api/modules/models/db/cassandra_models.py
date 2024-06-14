import uuid
from cassandra.cqlengine.columns import UUID, Text, Float, DateTime, Integer, Blob
from cassandra.cqlengine.models import Model
from cassandra.cqlengine.management import sync_table

class Course(Model):
    id      = UUID(primary_key=True, default=uuid.uuid4)
    code    = Text(primary_key=True, max_length=20, required=True,clustering_order="ASC")
    title   = Text(required=True, max_length=100)
    req_hrs = Float(required=True, default = 0)
    total_cost = Float(required=True, default = 0.0)
    course_offered  = DateTime()
    level = Integer(required=True, default=-1)
    description   = Text(required=False, max_length=200)
    
    def get_json(self):
        return {
            'id': str(self.id),
            'code': self.code,
            'title' : self.title,
            'req_hrs': self.req_hrs,
            'total_cost': self.total_cost,
            'course_offered': self.course_offered,
            'level': self.level,
            'description': self.description
    }
        
class DegreeLevel(Model):
    id      = UUID(primary_key=True, default=uuid.uuid4)
    code    = Integer(primary_key=True,required=True,clustering_order="ASC")
    description = Text(required=True)
      
    def get_json(self):
        return {
            'id': str(self.id),
            'code': self.code,
            'description': self.description
    }
        
class StudentLogin(Model):
    id = UUID(primary_key=True, default=uuid.uuid4)
    std_id = Text(primary_key=True,required=True, max_length=12, clustering_order="ASC")
    username = Text(required=True, max_length=60)
    password = Text(required=True, max_length=60)
    enc_password = Blob(required=True)
    
    def get_json(self):
        return {
            'id': str(self.id),
            'std_id': self.std_id,
            'username': self.username,
            'password' : self.password,
            'enc_password': str(self.enc_password, encoding='utf-8')
            
    }
    
class Student(Model):
    id = UUID(primary_key=True, default=uuid.uuid4)
    std_id = Text(primary_key=True,required=True, max_length=12, clustering_order="ASC")
    firstname = Text(required=True, max_length=60)
    midname = Text(required=True, max_length=60)
    lastname = Text(required=True, max_length=60)
    age = Integer(required=True, default=0)
    email = Text(required=True)
    attainment = Text(required=True, max_length=20)
    occupation = Text(required=True, max_length=100)
    
    def get_json(self):
        return {
            'id': str(self.id),
            'std_id': self.std_id,
            'firstname': self.firstname,
            'midname' : self.midname,
            'lastname': self.lastname,
            'age': self.age,
            'email': self.email,
            'attainment': self.attainment, 
            'occupation': self.occupation
    }

class StudentPerf(Model):
    id = UUID(primary_key=True, default=uuid.uuid4)
    std_id = Text(primary_key=True,required=True, max_length=12)
    course_code = Text(required=True, max_length=20)
    exam_title = Text(required=True, max_length=30)
    rating = Float(required=True, default = 0.0)
    status = Text(required=True, max_length=50)
    remarks = Text(required=True, max_length=100)
       
    def get_json(self):
        return {
            'id': str(self.id),
            'std_id': self.std_id,
            'course_code': self.course_code,
            'exam_title' : self.exam_title,
            'rating': self.rating,
            'status': self.status,
            'remarks': self.remarks 
    }
    
sync_table(Course)
sync_table(DegreeLevel)
sync_table(Student)
sync_table(StudentPerf)