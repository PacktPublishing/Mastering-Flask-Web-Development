from app.product import product_bp
from flask import request, jsonify
from app.product.repository.supplier import SupplierRepository

@product_bp.post("/supplier/add")
async def add_supplier():
    try:
        supplier_json = request.get_json()
        repo = SupplierRepository()
        result = await repo.insert_supplier(supplier_json)
        if result == False:
            return jsonify(message="error"), 500
        else:
            return jsonify(record=supplier_json)
    except  Exception as e:
        print(e)
    return jsonify(message="error"), 500

@product_bp.get("/category/list/all")
async def list_all_category():
    repo = SupplierRepository()
    result = await repo.select_all_supplier()
    return jsonify(records=result)