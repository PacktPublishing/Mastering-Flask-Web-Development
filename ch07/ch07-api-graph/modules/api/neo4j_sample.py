from py2neo import Node,  Relationship, NodeMatcher, Subgraph
from py2neo.cypher import Cursor
from flask import current_app, jsonify, request
from main import graph
from modules.repository.tutors import TutorNodeRepository

@current_app.post("/graph/trainer/add")
def create_node_trainer():
    data = request.get_json()
    tx = graph.begin()
    node_trainer = Node("Trainer", **data)
    
    graph.create(node_trainer)
    graph.commit(tx)
    return jsonify(message="done"), 201



@current_app.post("/graph/student/add")
def create_node_student():
    data = request.get_json()
    tx = graph.begin()
    node_student = Node("Student", **data)
    graph.create(node_student)
    graph.commit(tx)
    return jsonify(message="done"), 201

@current_app.post("/graph/trainer/student/rel")
def create_trainer_student_rel():
    data = request.get_json()
    tx = graph.begin()
    trains_with = Relationship.type("TRAINS_WITH")
    trainer_node = graph.query(f"MATCH (tr:Trainer) WHERE tr.tutor_id = '{data['tutor_id']}' Return tr").evaluate()
    student_node = graph.query(f"MATCH (st:Student) WHERE st.student_id = '{data['student_id']}' Return st").evaluate()
    graph.create(trains_with(trainer_node, student_node))
    graph.commit(tx)
    return jsonify(message="done"), 201

@current_app.delete("/graph/nodes/delete/<int:id>")
def delete_node(id:int):
    tx = graph.begin()
    user_cur:Cursor = graph.query(f'MATCH (n) WHERE id(n) = {id} RETURN n')
    user_sg:Subgraph = user_cur.to_subgraph()
    graph.delete(user_sg)
    graph.commit(tx)
    return jsonify(message="done"), 201

@current_app.delete("/graph/tutor/<string:tutor_id>")
def delete_tutor_id(tutor_id:str):
    tx = graph.begin()
    tutor_cur:Cursor = graph.query(f"MATCH (tr:Trainer) WHERE tr.tutor_id = '{tutor_id}' Return tr")
    tutor_sg:Subgraph = tutor_cur.to_subgraph()
    graph.delete(tutor_sg)
    graph.commit(tx)
    return jsonify(message="done"), 201


@current_app.delete("/graph/student/<string:student_id>")
def delete_student_id(student_id:str):
    tx = graph.begin()
    student_cur:Cursor = graph.query(f"MATCH (st:Student) WHERE st.student_id = '{student_id}' Return st")
    student_sg:Subgraph = student_cur.to_subgraph()
    graph.delete(student_sg)
    graph.commit(tx)
    return jsonify(message="done"), 201

@current_app.patch("/graph/student/update")
def update_student():
    data = request.get_json()
    tx = graph.begin()
    matcher = NodeMatcher(graph)
    student_node:Node  = matcher.match('Student', student_id=data['student_id']).first()
    if not student_node == None:
        del data['student_id']
        student_node.update(**data)
        graph.push(student_node)
        graph.commit(tx)
        return jsonify(message="done"), 201
    else:
        return jsonify(message="error"), 500
    

@current_app.get("/graph/tutor/list/all")
def list_all_tutors():
    tutor_cur:Cursor = graph.query(f"MATCH (tr:Trainer) Return tr")
    records = tutor_cur.data()
    return jsonify(records=records), 201

@current_app.get("/graph/tutor/<string:tutor_id>")
def get_tutor(tutor_id:str):
    repo = TutorNodeRepository()
    result = repo.get_tutor_node(tutor_id)
    return jsonify(record=result), 201