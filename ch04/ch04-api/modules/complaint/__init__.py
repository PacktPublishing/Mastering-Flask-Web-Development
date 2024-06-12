from flask import Blueprint
from flask_restful import Api

complaint_bp = Blueprint('complaint_bp', __name__)


from modules.complaint.api.complaint import AddComplaintRestAPI, ListComplaintRestAPI, UpdateComplainantRestAPI, UpdateComplaintRestAPI, DeleteComplaintRestAPI
from modules.complaint.api.category import AddCategoryRestAPI, ListCategoryRestAPI, UpdateCategoryNameRestAPI, UpdateCategoryRestAPI, DeleteCategoryRestAPI
from modules.complaint.api.complaint_details import AddComplaintDetailsRestAPI, ListComplaintDetailsRestAPI, UpdateComplaintDetailsRestAPI, UpdateComplaintStatusResolutionRestAPI, DeleteComplaintDetailsRestAPI
from modules.complaint.api.complaint_type import AddComplaintTypeRestAPI, ListComplaintTypeRestAPI, UpdateComplaintTypeNameRestAPI, UpdateComplaintTypeRestAPI, DeleteComplaintTypeRestAPI

api = Api(complaint_bp)
api.add_resource(AddComplaintRestAPI, '/complaint/add', endpoint='add_complaint')
api.add_resource(ListComplaintRestAPI, '/complaint/list/all', endpoint='list_all_complaint')
api.add_resource(UpdateComplainantRestAPI, '/complaint/update/complainant/<int:id>', endpoint='update_complainant')
api.add_resource(UpdateComplaintRestAPI, '/complaint/update', endpoint='update_complaint')
api.add_resource(DeleteComplaintRestAPI, '/complaint/delete/<int:id>', endpoint='delete_complaint')

api.add_resource(AddComplaintDetailsRestAPI, '/complaint/details/add', endpoint='add_complaint_details')
api.add_resource(ListComplaintDetailsRestAPI, '/complaint/details/list/all', endpoint='list_all_complaint_details')
api.add_resource(UpdateComplaintDetailsRestAPI, '/complaint/details/status/resolution/<int:compid>', endpoint='update_complaint_status_reso')
api.add_resource(UpdateComplaintStatusResolutionRestAPI, '/complaint/details/update', endpoint='update_complaint_details')
api.add_resource(DeleteComplaintDetailsRestAPI, '/complaint/details/delete/<int:compid>', endpoint='delete_complaint_details')

api.add_resource(AddComplaintTypeRestAPI, '/complaint/type/add', endpoint='add_complaint_type')
api.add_resource(ListComplaintTypeRestAPI, '/complaint/type/list/all', endpoint='list_all_complaint_type')
api.add_resource(UpdateComplaintTypeNameRestAPI, '/complaint/type/update/name/<int:id>', endpoint='update_complaint_type_name')
api.add_resource(UpdateComplaintTypeRestAPI, '/complaint/type/update', endpoint='update_complaint_type')
api.add_resource(DeleteComplaintTypeRestAPI, '/complaint/type/delete/<int:id>', endpoint='delete_complaint_type')

api.add_resource(AddCategoryRestAPI, '/category/add', endpoint='add_category')
api.add_resource(ListCategoryRestAPI, '/category/list/all', endpoint='list_all_category')
api.add_resource(UpdateCategoryNameRestAPI, '/category/update/name/<int:id>', endpoint='update_category')
api.add_resource(UpdateCategoryRestAPI, '/category/update', endpoint='update_category_details')
api.add_resource(DeleteCategoryRestAPI, '/category/delete/<int:id>', endpoint='delete_category')