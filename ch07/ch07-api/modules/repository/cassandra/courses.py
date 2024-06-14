from modules.models.db.cassandra_models import Course
from datetime import datetime
from typing import Dict, Any

class CourseRepository:
    def __init__(self):
        pass
    
    def insert_course(self, details:Dict[str, Any]):
        try:
            Course.create(**details)
            return True
        except Exception as e:
            print(e)
        return False
    
    def update_course(self, details:Dict[str, Any]):
        try:
            rec = Course.objects.filter(code=str(details['code'])).allow_filtering().get()
            del details['id']
            del details['code']
            rec.update(**details)
            return True
        except Exception as e:
            print(e)
        return False
     
    def delete_course_code(self, code):
        try:
            rec = Course.objects.filter(code=code).allow_filtering().get()
            rec.delete()
            return True
        except Exception as e:
            print(e)
        return False
    
    def search_by_code(self, code:str):
        result = Course.objects.filter(code=code).allow_filtering().get()
        records = dict(result)
        return records
    
    def search_all_courses(self):
        result = Course.objects.all()
        records = [course.get_json() for course in result]
        return records