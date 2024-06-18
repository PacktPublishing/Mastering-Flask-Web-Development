from app.product import product_bp
from flask import request, jsonify
from app.product.repository.invoicereq import InvoiceRequestRepository

@product_bp.post("/invoice/request/add")
async def add_invoice_request():
    try:
        invreq_json = request.get_json()
        repo = InvoiceRequestRepository()
        result = await repo.insert_invoice_req(invreq_json)
        if result == False:
            return jsonify(message="error"), 500
        else:
            return jsonify(record=invreq_json)
    except  Exception as e:
        print(e)
    return jsonify(message="error"), 500

@product_bp.get("/invoice/request/list/all")
async def list_all_invoice_request():
    repo = InvoiceRequestRepository()
    result = await repo.select_all_invreq()
    return jsonify(records=result)