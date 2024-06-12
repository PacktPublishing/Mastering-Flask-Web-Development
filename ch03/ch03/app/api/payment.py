from flask import current_app , jsonify, request, make_response
from flask.json import dumps,  loads
from flask.json.provider import JSONProvider
from datetime import date
from app.model.db import Payment
from app.repository.payment import PaymentRepository
from app.model.config import db_session

@current_app.post('/payment/add')
def add_payment():
   
        payment_json = request.get_json()
        repo = PaymentRepository(db_session)
        payment = Payment(**payment_json)
        result = repo.insert(payment)
        if result:
            content = jsonify(payment_json)
            current_app.logger.info('insert payment record successful')
            return make_response(content, 201)
        else:
            content = jsonify(message="insert payment record encountered a problem")
            return make_response(content, 500)
  

@current_app.get('/payment/list/all')
def list_all_payment():
    repo = PaymentRepository(db_session)
    records = repo.select_all()
    payment_rec = [rec.to_json() for rec in records]
    current_app.logger.info('retrieved a list of payment successfully')
    return make_response(jsonify(payment_rec), 201)


@current_app.delete('/order/delete/<string:pid>')
def delete_payment(pid:str):
   
        repo = PaymentRepository(db_session)
        result = repo.delete(pid)
        if result:
            content = jsonify(message=f'payment {pid} deleted')
            current_app.logger.info('delete payment record successful')
            return make_response(content, 201)
        else:
            content = jsonify(message="delete payment record encountered a problem")
            return make_response(content, 500)
   