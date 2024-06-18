from modules_sub_flask import create_app_sub
from flask_cors import CORS
from flask import request, jsonify

from ariadne import load_schema_from_path, make_executable_schema, \
    graphql_sync, snake_case_fallback_resolvers, ObjectType
from ariadne.explorer import ExplorerGraphiQL
from modules_sub_flask.resolvers.complainant_repo import ComplainantResolver
from modules_sub_flask.resolvers.category_repo import CategoryResolver
from modules_sub_flask.resolvers.complaint_repo import ComplaintResolver
from modules_sub_flask.resolvers.complaint_type_repo import ComplaintTypeResolver
from modules_sub_flask.models.config import db_session

flask_sub_app = create_app_sub("../config_dev_sub.toml")
CORS(flask_sub_app)

complainant_repo = ComplainantResolver(db_session)
category_repo = CategoryResolver(db_session)
comp_type_repo = ComplaintTypeResolver(db_session)
complaint_repo = ComplaintResolver(db_session)

query = ObjectType("Query")
query.set_field("listAllComplainants", complainant_repo.select_all_complainant)
query.set_field("listAllComplaints", complaint_repo.select_all_complaint)
query.set_field("listAllCategories", category_repo.select_all_category)
query.set_field("listAllComplaintTypes", comp_type_repo.select_all_complaint_types)

mutation = ObjectType("Mutation")
mutation.set_field("createComplainant", complainant_repo.insert_complainant)
mutation.set_field("createComplaint", complaint_repo.insert_complaint)
mutation.set_field("createCategory", category_repo.insert_category)
mutation.set_field("createComplaintType", comp_type_repo.insert_complaint_type)

type_defs = load_schema_from_path("./schema.graphql")
schema = make_executable_schema(
    type_defs, query, mutation, 
)

explorer_html = ExplorerGraphiQL().html(None)

@flask_sub_app.route("/graphql", methods=["GET"])
def graphql_explorer():
    return explorer_html, 200

@flask_sub_app.route("/graphql", methods=["POST"])
def graphql_server():
    data = request.get_json()
    success, result = graphql_sync(
        schema,
        data,
        context_value=request,
        debug=flask_sub_app.debug
    )
    status_code = 200 if success else 400
    return jsonify(result), status_code


