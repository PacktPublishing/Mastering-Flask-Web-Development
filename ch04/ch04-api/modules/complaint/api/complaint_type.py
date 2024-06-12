from flask import jsonify, request, make_response
from flask_restful import Resource

from model.config import db_session
from model.db import ComplaintType
from modules.complaint.repository.complaint_type import ComplaintTypeRepository

class ListComplaintTypeRestAPI(Resource):
    def get(self):
        repo = ComplaintTypeRepository(db_session)
        records = repo.select_all()
        comptype_rec = [rec.to_json() for rec in records]
        return make_response(jsonify(comptype_rec), 201)

class AddComplaintTypeRestAPI(Resource):
    def post(self):
        comptype_json = request.get_json()
        repo = ComplaintTypeRepository(db_session)
        comptype = ComplaintType(**comptype_json)
        result = repo.insert(comptype)
        if result:
            content = jsonify(comptype_json)
            return make_response(content, 201)
        else:
            content = jsonify(message="insert complaint type record encountered a problem")
            return make_response(content, 500)
        
class UpdateComplaintTypeNameRestAPI(Resource):
    def patch(self, id):
        comptype_json = request.get_json()
        repo = ComplaintTypeRepository(db_session)
        result = repo.update(id, comptype_json)
        if result:
            content = jsonify(comptype_json)
            return make_response(content, 201)
        else:
            content = jsonify(message="update complaint type name encountered a problem")
            return make_response(content, 500)

class DeleteComplaintTypeRestAPI(Resource):
    def delete(self, id):
        repo = ComplaintTypeRepository(db_session)
        result = repo.delete(id)
        if result:
            content = jsonify(message=f'complaint type {id} deleted')
            return make_response(content, 201)
        else:
            content = jsonify(message="delete complaint type record encountered a problem")
            return make_response(content, 500)
        
class UpdateComplaintTypeRestAPI(Resource):
    def put(self):
        cust_json = request.get_json()
        repo = ComplaintTypeRepository(db_session)
        result = repo.update(cust_json['id'], cust_json)
        if result:
            content = jsonify(cust_json)
            return make_response(content, 201)
        else:
            content = jsonify(message="update complaint type record encountered a problem")
            return make_response(content, 500)
  