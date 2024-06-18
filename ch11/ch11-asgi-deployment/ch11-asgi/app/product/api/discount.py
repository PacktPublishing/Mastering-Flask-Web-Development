from app.product import product_bp
from flask import request, jsonify
from app.product.repository.discount import DiscountRepository

@product_bp.post("/discount/add")
async def add_discount():
    try:
        discount_json = request.get_json()
        repo = DiscountRepository()
        result = await repo.insert_discount(discount_json)
        if result == False:
            return jsonify(message="error"), 500
        else:
            return jsonify(record=discount_json)
    except  Exception as e:
        print(e)
    return jsonify(message="error"), 500

@product_bp.get("/discount/list/all")
async def list_all_discount():
    repo = DiscountRepository()
    result = await repo.select_all_discount()
    return jsonify(records=result)