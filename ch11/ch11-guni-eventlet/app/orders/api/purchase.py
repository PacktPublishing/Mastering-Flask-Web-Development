from app.orders import order_bp
from flask import request, jsonify
from app.orders.repository.purchase import PurchaseRepository

@order_bp.post("/purchae/add")
def add_purchase():
    try:
        purchase_json = request.get_json()
        repo = PurchaseRepository()
        result = repo.insert_purchase(purchase_json)
        if result == False:
            return jsonify(message="error"), 500
        else:
            return jsonify(record=purchase_json)
    except  Exception as e:
        print(e)
    return jsonify(message="error"), 500

@order_bp.get("/purchase/list/all")
def list_all_purchase():
    repo = PurchaseRepository()
    result = repo.select_all_purchase()
    return jsonify(records=result)