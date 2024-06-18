from app.orders import order_bp
from flask import request, jsonify
from app.orders.repository.cart_item import CartItemRepository

@order_bp.post("/cart/item/add")
def add_cart_item():
    try:
        item_json = request.get_json()
        repo = CartItemRepository()
        result = repo.insert_cart_item(item_json)
        if result == False:
            return jsonify(message="error"), 500
        else:
            return jsonify(record=item_json)
    except  Exception as e:
        print(e)
    return jsonify(message="error"), 500

@order_bp.get("/cart/item/list/all")
def list_all_cart_item():
    repo = CartItemRepository()
    result = repo.select_all_cart_items()
    return jsonify(records=result)