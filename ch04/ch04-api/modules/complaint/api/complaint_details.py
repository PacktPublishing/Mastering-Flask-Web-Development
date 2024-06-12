from flask import jsonify, request, make_response
from flask_restful import Resource

from main_cache import cache
from model.config import db_session
from model.db import ComplaintDetails
from modules.complaint.repository.complaint_details import ComplaintDetailsRepository

class ListComplaintDetailsRestAPI(Resource):
    @cache.cached(timeout=50)
    def get(self):
        repo = ComplaintDetailsRepository(db_session)
        records = repo.select_all()
        compdetails_rec = [rec.to_json() for rec in records]
        return make_response(jsonify(compdetails_rec), 201)

class AddComplaintDetailsRestAPI(Resource):
    def post(self):
        compdetails_json = request.get_json()
        repo = ComplaintDetailsRepository(db_session)
        print(compdetails_json)
        compdetails = ComplaintDetails(**compdetails_json)
      
        result = repo.insert(compdetails)
        if result:
            content = jsonify(compdetails_json)
            return make_response(content, 201)
        else:
            content = jsonify(message="insert complaint details record encountered a problem")
            return make_response(content, 500)
        
class UpdateComplaintStatusResolutionRestAPI(Resource):
    def patch(self, compid):
        compdetails_json = request.get_json()
        repo = ComplaintDetailsRepository(db_session)
        result = repo.update(compid, compdetails_json)
        if result:
            content = jsonify(compdetails_json)
            return make_response(content, 201)
        else:
            content = jsonify(message="update complaint status and resolution encountered a problem")
            return make_response(content, 500)

class DeleteComplaintDetailsRestAPI(Resource):
    def delete(self, compid):
        repo = ComplaintDetailsRepository(db_session)
        result = repo.delete(compid)
        if result:
            content = jsonify(message=f'complaint details {compid} deleted')
            return make_response(content, 201)
        else:
            content = jsonify(message="delete complaint details record encountered a problem")
            return make_response(content, 500)
        
class UpdateComplaintDetailsRestAPI(Resource):
    def put(self):
        compdetails_json = request.get_json()
        repo = ComplaintDetailsRepository(db_session)
        result = repo.update(compdetails_json['compid'], compdetails_json)
        if result:
            content = jsonify(compdetails_json)
            return make_response(content, 201)
        else:
            content = jsonify(message="update complaint details record encountered a problem")
            return make_response(content, 500)
  