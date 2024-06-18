from app.product import product_bp
from flask import request, jsonify
from app.product.repository.brand import BrandRepository

@product_bp.post("/brand/add")
async def add_brand():
    try:
        brand_json = request.get_json()
        repo = BrandRepository()
        result = await repo.insert_brand(brand_json)
        if result == False:
            return jsonify(message="error"), 500
        else:
            return jsonify(record=brand_json)
    except  Exception as e:
        print(e)
    return jsonify(message="error"), 500

@product_bp.get("/brand/list/all")
async def list_all_brands():
    repo = BrandRepository()
    result = await repo.select_all_brand()
    return jsonify(records=result)