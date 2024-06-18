
from flask import request, jsonify, current_app
from modules.repository.login import LoginRepository
from modules import tracer

from flask_openapi3 import Tag

add_login_tag = Tag(name="add_login", description="Creates a user login.")
update_login_username_tag = Tag(name="update_username", description="Updates login username")
delete_login_tag = Tag(name="delete_login", description="Deletes a user login.")
list_login_tag = Tag(name="list_login", description="List all user credentials.")
get_login_tag = Tag(name="get_login", description="Get a single user login.")

@current_app.post("/login/add", summary="Adds user login to the database.", tags=[add_login_tag])
def add_login():
    """
    API for creating user credentials.
    """
    with tracer.start_as_current_span('users_span'):
        login_json = request.get_json()
        repo = LoginRepository()
        result = repo.insert_login(login_json)
        if result == False:
            return jsonify(message="error"), 500
        else:
            return jsonify(record=login_json)

@current_app.get("/login/list/all", summary="List all login records.", tags=[list_login_tag])
def list_login():
    """
    API for retrieving all the records from the olms database.
    """
    with tracer.start_as_current_span('users_span'):
        repo = LoginRepository()
        result = repo.select_all_login()
        print(result)
        return jsonify(records=result)

@current_app.get("/login/rec/<string:username>", summary="Retrieves a specific login user through its username.", tags=[get_login_tag])
def get_login(username:str):
  with tracer.start_as_current_span('users_span'):
    repo = LoginRepository()
    result = repo.select_login_username(username)
    return jsonify(records=result)

@current_app.patch("/login/update", summary="Updates the username of a specific login.", tags=[update_login_username_tag])
def update_username():
  with tracer.start_as_current_span('users_span'):
    login_json = request.get_json()
    repo = LoginRepository()
    result = repo.change_password(login_json)
    if result == False:
        return jsonify(message="error"), 500
    else:
        return jsonify(record=login_json)

@current_app.delete("/login/delete/<string:username>", summary="Deletes a specific login.", tags=[delete_login_tag])    
def delete_login(username:str):
  with tracer.start_as_current_span('users_span'):
    repo = LoginRepository()
    result = repo.delete_login(username)
    if result == False:
        return jsonify(message="error"), 500
    else:
        return jsonify(message="deleted")