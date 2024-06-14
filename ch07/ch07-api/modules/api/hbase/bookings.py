from flask import current_app, jsonify, request
from datetime import datetime
from modules import pool
from modules.repository.hbase.bookings import BookingRepository

@current_app.post('/booking/add')
def add_booking():
    data = request.get_json()
    repo = BookingRepository(pool)
    result = repo.upsert_booking(data['id'], data['tutor_id'], data['stud_id'], data['date_booked'])
    if result == False:
        return jsonify(message="error encountered in booking record insert"), 500
    return jsonify(message="inserted booking record"), 201

@current_app.delete('/booking/delete/<string:rowkey>')
def delete_booking(rowkey:str):
    repo = BookingRepository(pool)
    result = repo.delete_record(rowkey)
    if result == False:
        return jsonify(message="error encountered in booking record deleted"), 500
    return jsonify(message="deleted booking record"), 201

@current_app.get('/booking/get/<string:tutor_id>')
def get_booking(tutor_id:str):
    repo = BookingRepository(pool)
    results = repo.select_tutor_bookings(tutor_id)
    return jsonify(records=results), 201

@current_app.get('/booking/list/all')
def list_all_booking():
    repo = BookingRepository(pool)
    results = repo.select_all_records()
    return jsonify(records=results), 201