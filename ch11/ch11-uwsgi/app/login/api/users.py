from app.login import login_bp
from flask import request, jsonify
from app.login.repository.login import LoginRepository

@login_bp.post("/login/add")
def add_login():
    login_json = request.get_json()
    repo = LoginRepository()
    result = repo.insert_login(login_json)
    if result == False:
        return jsonify(message="error"), 500
    else:
        return jsonify(record=login_json)

@login_bp.get("/login/list/all")
def list_login():
    repo = LoginRepository()
    result = repo.select_all_login()
    print(result)
    return jsonify(records=result)

@login_bp.get("/login/rec/<string:username>")
def get_login(username:str):
    repo = LoginRepository()
    result = repo.select_login_username(username)
    return jsonify(records=result)

@login_bp.patch("/login/update")
def update_username():
    login_json = request.get_json()
    repo = LoginRepository()
    result = repo.change_password(login_json)
    if result == False:
        return jsonify(message="error"), 500
    else:
        return jsonify(record=login_json)

@login_bp.delete("/login/delete/<string:username>")    
def delete_login(username:str):
    repo = LoginRepository()
    result = repo.delete_login(username)
    if result == False:
        return jsonify(message="error"), 500
    else:
        return jsonify(message="deleted")