from app.product import product_bp
from flask import request, jsonify
from app.product.repository.category import CategoryRepository

@product_bp.post("/category/add")
def add_category():
    try:
        category_json = request.get_json()
        repo = CategoryRepository()
        result = repo.insert_category(category_json)
        if result == False:
            return jsonify(message="error"), 500
        else:
            return jsonify(record=category_json)
    except  Exception as e:
        print(e)
    return jsonify(message="error"), 500

@product_bp.get("/category/list/all")
def list_all_category():
    repo = CategoryRepository()
    result = repo.select_all_category()
    return jsonify(records=result)