from app.product import product_bp
from flask import request, jsonify
from app.product.repository.stock import StockRepository

@product_bp.post("/stock/add")
async def add_stock():
    try:
        stock_json = request.get_json()
        repo = StockRepository()
        result = await repo.insert_stock(stock_json)
        if result == False:
            return jsonify(message="error"), 500
        else:
            return jsonify(record=stock_json)
    except  Exception as e:
        print(e)
    return jsonify(message="error"), 500

@product_bp.get("/stock/list/all")
async def list_all_stock():
    repo = StockRepository()
    result = await repo.select_all_stock()
    return jsonify(records=result)