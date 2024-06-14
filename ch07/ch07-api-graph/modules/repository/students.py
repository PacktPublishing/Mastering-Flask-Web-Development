from main import graph
from py2neo import Node, NodeMatcher, Subgraph, Transaction
from py2neo.cypher import Cursor
from typing import Any, List, Dict

class StudentNodeRepository:
    def __init__(self):
        pass
    
    def insert_student_node(self, details:Dict[str, Any]):
        try:
            tx:Transaction = graph.begin()
            node_trainer = Node("Tutor", **details)
            graph.create(node_trainer)
            graph.commit(tx)
            return True
        except Exception as e:
            print(e)
        return False
    
    def update_student_node(self, details:Dict[str, Any]):
        try:
            tx = graph.begin()
            matcher = NodeMatcher(graph)
            student_node:Node  = matcher.match('Student', student_id=details['student_id']).first()
            if not student_node == None:
                del details['student_id']
                student_node.update(**details)
                graph.push(student_node)
                graph.commit(tx)
                return True
            else:
                return False
        except Exception as e:
            print(e)
        return False 
    
    def delete_student_node(self, student_id:str):
        try:
            tx = graph.begin()
            student_cur:Cursor = graph.query(f"MATCH (st:Student) WHERE st.student_id = '{student_id}' Return st")
            student_sg:Subgraph = student_cur.to_subgraph()
            graph.delete(student_sg)
            graph.commit(tx)
            return True
        except Exception as e:
            print(e)
        return False
    
    def get_student_node(self, student_id:str):
        matcher = NodeMatcher(graph)
        student_node:Node  = matcher.match('Student', student_id=student_id).first()
        record = dict(student_node)
        return record
    
    def select_student_nodes(self):
        student_cur:Cursor = graph.query(f"MATCH (st:Student) Return st")
        records = student_cur.data()
        return records
        