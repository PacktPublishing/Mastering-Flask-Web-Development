from main import graph
from py2neo import Relationship
from typing import Any, List, Dict

class TutorStudentsRelRepository:
    def __init__(self):
        pass
    
    def create_tutor_student_rel(self, details:Dict[str, Any]):
        try:
            tx = graph.begin()
            trains_with = Relationship.type("TRAINS_WITH")
            tutor_node = graph.query(f"MATCH (tut:Tutor) WHERE tut.tutor_id = '{details['tutor_id']}' Return tut").evaluate()
            student_node = graph.query(f"MATCH (st:Student) WHERE st.student_id = '{details['student_id']}' Return st").evaluate()
            graph.create(trains_with(tutor_node, student_node))
            graph.commit(tx)
            return True
        except Exception as e:
            print(e)   
        return False