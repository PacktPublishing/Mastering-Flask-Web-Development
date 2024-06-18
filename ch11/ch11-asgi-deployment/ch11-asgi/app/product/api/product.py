from app.product import product_bp
from flask import request, jsonify
from app.product.repository.product import ProductRepository

@product_bp.post("/product/add")
async def add_product():
    try:
        prod_json = request.get_json()
        repo = ProductRepository()
        result = await repo.insert_product(prod_json)
        if result == False:
            return jsonify(message="error"), 500
        else:
            return jsonify(record=prod_json)
    except  Exception as e:
        print(e)
    return jsonify(message="error"), 500

@product_bp.get("/product/list/all")
async def list_all_product():
    repo = ProductRepository()
    result = await repo.select_all_product()
    return jsonify(records=result)