from main import graph
from py2neo import Node, NodeMatcher, Subgraph
from py2neo.cypher import Cursor
from typing import Any, List, Dict

class TutorNodeRepository:
    def __init__(self):
        pass
    
    def insert_tutor_node(self, details:Dict[str, Any]):
        try:
            tx = graph.begin()
            node_tutor = Node("Tutor", **details)
            graph.create(node_tutor)
            graph.commit(tx)
            return True
        except Exception as e:
            print(e)
        return False
    
    def update_tutor_node(self, details:Dict[str, Any]):
        try:
            tx = graph.begin()
            matcher = NodeMatcher(graph)
            tutor_node:Node  = matcher.match('Tutor', tutor_id=details['tutor_id']).first()
            if not tutor_node == None:
                del details['tutor_id']
                tutor_node.update(**details)
                graph.push(tutor_node)
                graph.commit(tx)
                return True
            else:
                return False
        except Exception as e:
            print(e)
        return False 
    
    def delete_tutor_node(self, tutor_id:str):
        try:
            tx = graph.begin()
            tutor_cur:Cursor = graph.query(f"MATCH (tut:Tutor) WHERE tut.tutor_id = '{tutor_id}' Return tut")
            tutor_sg:Subgraph = tutor_cur.to_subgraph()
            graph.delete(tutor_sg)
            graph.commit(tx)
            return True
        except Exception as e:
            print(e)
        return False
    
    def get_tutor_node(self, tid:str):
        matcher = NodeMatcher(graph)
        tutor_node:Node  = matcher.match('Tutor', tutor_id=tid).first()
        record = dict(tutor_node)
        return record
    
    def select_tutor_nodes(self):
        tutor_cur:Cursor = graph.query(f"MATCH (tr:Tutor) Return tr")
        records = tutor_cur.data()
        return records