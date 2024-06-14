
from flask import current_app, jsonify, request
from datetime import datetime
from modules import pool
from modules.repository.hbase.payments import PaymentRepository

@current_app.post('/payment/details/add')
def add_payment_details():
    data = request.get_json()
    repo = PaymentRepository(pool)
    result = repo.upsert_details(data['id'], data['tutor_id'], data['stud_id'], 
                                       data['ccode'], data['fee'])
    if result == False:
        return jsonify(message="error encountered in payment details record insert"), 500
    return jsonify(message="inserted payment details record"), 201

@current_app.post('/payment/charge/add')
def add_payment_charge():
    data = request.get_json()
    repo = PaymentRepository(pool)
    result = repo.upsert_payment(data['id'], data['receipt_id'], data['amount'])
    if result == False:
        return jsonify(message="error encountered in payment record insert"), 500
    return jsonify(message="inserted payment record"), 201


@current_app.delete('/payment/delete/<string:rowkey>')
def delete_payment_record(rowkey:str):
    repo = PaymentRepository(pool)
    result = repo.delete_record(rowkey)
    if result == False:
        return jsonify(message="error encountered in payment record deleted"), 500
    return jsonify(message="deleted payment record"), 201

@current_app.delete('/payment/delete/details/<string:rowkey>')
def delete_payment_record_details(rowkey:str):
    repo = PaymentRepository(pool)
    result = repo.delete_payment_details(rowkey)
    if result == False:
        return jsonify(message="error encountered in payment details record deleted"), 500
    return jsonify(message="deleted payment details record"), 201

@current_app.delete('/payment/delete/items/<string:rowkey>')
def delete_payment_record_items(rowkey:str):
    repo = PaymentRepository(pool)
    result = repo.delete_payment_items(rowkey)
    if result == False:
        return jsonify(message="error encountered in payment items record deleted"), 500
    return jsonify(message="deleted payment items record"), 201

@current_app.get('/payment/get/<string:tutor_id>')
def get_tutor_payments(tutor_id:str):
    repo = PaymentRepository(pool)
    results = repo.select_records_tutor(tutor_id)
    return jsonify(records=results), 201

@current_app.post('/payment/select/details')
def project_tutor_details():
    data = request.get_json()
    repo = PaymentRepository(pool)
    results = repo.select_records_ids(data['rowkeys'], data['cols'])
    return jsonify(records=results), 201

@current_app.get('/payment/list/all')
def list_all_payments():
    repo = PaymentRepository(pool)
    results = repo.select_all_records()
    print(results)
    return jsonify(records=results), 201