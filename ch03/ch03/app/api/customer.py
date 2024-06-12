from flask import current_app , jsonify, request, make_response
from flask.json import  dumps,  loads
from flask.json.provider import JSONProvider
from datetime import date
from app.model.db import Customer
from app.repository.customer import CustomerRepository
from app.model.config import db_session

@current_app.post('/customer/add')
def add_customer():
  
        cust_json = request.get_json()
        repo = CustomerRepository(db_session)
        customer = Customer(**cust_json)
        result = repo.insert(customer)
        if result:
            content = jsonify(cust_json)
            current_app.logger.info('insert customer record successful')
            return make_response(content, 201)
        else:
            content = jsonify(message="insert customer record encountered a problem")
            return make_response(content, 500)
   

@current_app.get('/customer/list/all')
def list_all_customer():
    repo = CustomerRepository(db_session)
    records = repo.select_all()
    cust_rec = [rec.to_json() for rec in records]
    current_app.logger.info('retrieved a list of customers successfully')
    return make_response(jsonify(cust_rec), 201)

@current_app.patch('/customer/update/<string:cid>')
def update_customer_name(cid:str):
   
        cust_json = request.get_json()
        repo = CustomerRepository(db_session)
        result = repo.update(cid, cust_json)
        if result:
            content = jsonify(cust_json)
            current_app.logger.info('update customer firstname, middlename, and lastname successful')
            return make_response(content, 201)
        else:
            content = jsonify(message="update customer firstname, middlename, and lastname encountered a problem")
            return make_response(content, 500)
   


@current_app.put('/customer/update')
def update_customer():
   
        cust_json = request.get_json()
        repo = CustomerRepository(db_session)
        result = repo.update(cust_json['cid'], cust_json)
        if result:
            content = jsonify(cust_json)
            current_app.logger.info('update customer record successful')
            return make_response(content, 201)
        else:
            content = jsonify(message="update customer record encountered a problem")
            return make_response(content, 500)
  

@current_app.delete('/customer/delete/<string:cid>')
def delete_customer(cid:str):
   
        repo = CustomerRepository(db_session)
        result = repo.delete(cid)
        if result:
            content = jsonify(message=f'customer {cid} deleted')
            current_app.logger.info('delete customer record successful')
            return make_response(content, 201)
        else:
            content = jsonify(message="delete customer record encountered a problem")
            return make_response(content, 500)
   