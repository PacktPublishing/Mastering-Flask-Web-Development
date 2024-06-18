from app.users import users_bp
from flask import request, jsonify
from app.users.repository.customer import CustomerRepository 

@users_bp.post("/customer/add")
async def add_customer():
    customer_json = request.get_json()
    if customer_json["role"] == 2:
        repo = CustomerRepository()
        result = await repo.insert_customer(customer_json)
        if result == False:
            return jsonify(message="error"), 500
        else:
            return jsonify(record=customer_json)
    else:
        if result == False:
            return jsonify(message="role error"), 500