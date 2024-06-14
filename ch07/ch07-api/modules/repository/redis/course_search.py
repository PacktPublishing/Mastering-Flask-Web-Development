from modules.models.db.redis_models import SearchCourse
from typing import Dict, Any

class SearchCourseRepository:
    
    def __init__(self):
        pass
    
    def insert_course(self, details:Dict[str, Any]):
        try:
            course = SearchCourse(**details)
            course.save()
            return True
        except Exception as e:
            print(e)
        return False
    
    def update_course(self, details:Dict[str, Any]):
        try:
            record = SearchCourse.get(details['pk'])
            record.update(**details)
            return True
        except Exception as e:
            print(e)
        return False
    
    def delete_course(self, pk):
        try:
            SearchCourse.delete(pk)
            return True
        except Exception as e:
            print(e)
        return False
    
    def select_course(self, pk):
        try:
            record = SearchCourse.get(pk)
            return record.dict()
        except Exception as e:
            print(e)
        return None
    
        
    def select_all_course(self):
        records = list()
        for id in SearchCourse.all_pks():
            records.append(SearchCourse.get(id).dict())
        return records
    
    