from flask import jsonify, request, make_response
from flask_restful import Resource
from main_cache import cache
from model.config import db_session
from model.db import Complaint
from modules.complaint.repository.complaint import ComplaintRepository

class ListComplaintRestAPI(Resource):
    @cache.memoize(timeout=30)
    def get(self):
  
        repo = ComplaintRepository(db_session)
        records = repo.select_all()
        complaint_rec = [rec.to_json() for rec in records]
        return make_response(jsonify(complaint_rec), 201)

class AddComplaintRestAPI(Resource):
   
    def post(self):
        complaint_json = request.get_json()
        repo = ComplaintRepository(db_session)
        complaint = Complaint(**complaint_json)
        result = repo.insert(complaint)
        if result:
            content = jsonify(complaint_json)
            return make_response(content, 201)
        else:
            content = jsonify(message="insert complaint record encountered a problem")
            return make_response(content, 500)
        
class UpdateComplainantRestAPI(Resource):
    def patch(self, id):
        complaint_json = request.get_json()
        repo = ComplaintRepository(db_session)
        result = repo.update(id, complaint_json)
        if result:
            content = jsonify(complaint_json)
            return make_response(content, 201)
        else:
            content = jsonify(message="update complainant ID encountered a problem")
            return make_response(content, 500)

class DeleteComplaintRestAPI(Resource):
    def delete(self, id):
        repo = ComplaintRepository(db_session)
        result = repo.delete(id)
        if result:
            content = jsonify(message=f'customer {id} deleted')
            return make_response(content, 201)
        else:
            content = jsonify(message="delete complaint record encountered a problem")
            return make_response(content, 500)
        
class UpdateComplaintRestAPI(Resource):
    def put(self):
        complaint_json = request.get_json()
        repo = ComplaintRepository(db_session)
        result = repo.update(complaint_json['id'], complaint_json)
        if result:
            content = jsonify(complaint_json)
            return make_response(content, 201)
        else:
            content = jsonify(message="update complaint record encountered a problem")
            return make_response(content, 500)
  