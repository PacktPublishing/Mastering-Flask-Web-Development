from flask import current_app , jsonify, request, make_response
from flask.json import  dumps,  loads
from flask.json.provider import JSONProvider
from datetime import date
from app.model.db import Employee
from app.repository.employee import EmployeeRepository
from app.model.config import db_session
from app.exceptions.db import DuplicateRecordException, NoRecordException

@current_app.post('/employee/add')
def add_employee():
    emp_json = request.get_json()
    repo = EmployeeRepository(db_session)
    employee = Employee(**emp_json)
    result = repo.insert(employee)
    if result:
        content = jsonify(emp_json)
        current_app.logger.info('insert employee record successful')
        return make_response(content, 201)
    else:
        raise DuplicateRecordException("insert employee record encountered a problem", status_code=500)
    

@current_app.get('/employee/list/all')
def list_all_employee():
    repo = EmployeeRepository(db_session)
    records = repo.select_all()
    emp_rec = [rec.to_json() for rec in records]
    current_app.logger.info('retrieved a list of employees successfully')
    return jsonify(emp_rec)

@current_app.patch('/employee/update/<string:empid>')
def update_employee_name(empid:str):
    
    emp_json = request.get_json()
    repo = EmployeeRepository(db_session)
    result = repo.update(empid, emp_json)
    if result:
        content = jsonify(emp_json)
        current_app.logger.info('update employee firstname, middlename, and lastname successful')
        return make_response(content, 201)
    else:
        raise NoRecordException("update employee firstname, middlename, and lastname encountered a problem", status_code=500)
   


@current_app.put('/employee/update')
def update_employee():
    
    emp_json = request.get_json()
    repo = EmployeeRepository(db_session)
    result = repo.update(emp_json['empid'], emp_json)
   
    if result:
        content = jsonify(emp_json)
        current_app.logger.info('update employee record successful')
        return make_response(content, 201)
    else:
        raise NoRecordException("update employee record encountered a problem", status_code=500)
    

@current_app.delete('/employee/delete/<string:empid>')
def delete_employee(empid:str):
   
    repo = EmployeeRepository(db_session)
    result = repo.delete(empid)
    if result:
        content = jsonify(message=f'employee {empid} deleted')
        current_app.logger.info('delete employee record successful')
        return make_response(content, 201)
    else:
        raise NoRecordException("delete employee record encountered a problem", status_code=500)
   