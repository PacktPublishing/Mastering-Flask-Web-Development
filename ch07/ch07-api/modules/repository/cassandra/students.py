from modules.models.db.cassandra_models import Student
from datetime import datetime
from typing import Dict, Any

class StudentRepository:
    def __init__(self):
        pass
    
    def insert_student(self, details:Dict[str, Any]):
        try:
            Student.create(**details)
            return True
        except Exception as e:
            print(e)
        return False
    
    def update_student(self, details:Dict[str, Any]):
        try:
            rec = Student.objects.filter(std_id=str(details['std_id'])).allow_filtering().get()
            del details['id']
            del details['std_id']
            rec.update(**details)
            return True
        except Exception as e:
            print(e)
        return False
    
    
    def delete_student_std_id(self, id:str):
        try:
            rec = Student.objects.filter(std_id=id).allow_filtering().get()
            rec.delete()
            return True
        except Exception as e:
            print(e)
        return False
    
    def search_by_std_id(self, std_id:str):
        result = Student.objects.filter(std_id=std_id).allow_filtering().get()
        records = dict(result)
        return records
    
    def search_by_ids(self, id:str, std_id:str):
        result = Student.objects.filter(id=id, std_id=std_id).get()
        records = dict(result)
        return records
    
    def search_all_students(self):
        result = Student.objects.all()
        records = [std.get_json() for std in result]
        return records