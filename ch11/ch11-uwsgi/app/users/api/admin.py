from app.users import users_bp
from flask import request, jsonify
from app.users.repository.admin import AdminRepository

@users_bp.post("/admin/add")
def add_admin():
    admin_json = request.get_json()
    if admin_json["role"] == 1:
        repo = AdminRepository()
        result = repo.insert_admin(admin_json)
        if result == False:
            return jsonify(message="error"), 500
        else:
            return jsonify(record=admin_json)
    else:
        if result == False:
            return jsonify(message="role error"), 500

@users_bp.get("/admin/list/all")
def list_admin():
    repo = AdminRepository()
    result = repo.select_all_admin()
    print(result)
    return jsonify(records=result)

@users_bp.get("/admin/rec/<string:username>")
def get_admin(username:str):
    repo = AdminRepository()
    result = repo.select_admin_username(username)
    return jsonify(records=result)

@users_bp.patch("/admin/update")
def update_admin():
    admin_json = request.get_json()
    repo = AdminRepository()
    result = repo.update_admin(admin_json)
    if result == False:
        return jsonify(message="error"), 500
    else:
        return jsonify(record=admin_json)

@users_bp.delete("/admin/delete/<string:username>")    
def delete_login(username:str):
    repo = AdminRepository()
    result = repo.delete_admin_username(username)
    if result == False:
        return jsonify(message="error"), 500
    else:
        return jsonify(message="deleted")