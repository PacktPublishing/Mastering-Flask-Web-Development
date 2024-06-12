from flask import render_template, request

from modules.login import login_bp
from modules.login.repository.customer import CustomerRepository
from modules.login.services.login import get_login_id
from exceptions.db import DuplicateRecordException

from main import app
from modules.model.db import Customer
from modules.model.config import db_session

@login_bp.route('/customer/add', methods=['GET', 'POST']) 
def add_customer():
    repo = CustomerRepository(db_session)
    if request.method == 'POST':
        app.logger.info('add_customer POST view executed')
        cust = Customer(id=int(request.form['id']), firstname=request.form['firstname'],
                        lastname=request.form['lastname'], middlename=request.form['middlename'],
                        address=request.form['address'], email=request.form['email'],
                        mobile=request.form['mobile'], status=request.form['status'])
        result = repo.insert(cust)
        if result == False:
            raise DuplicateRecordException()
    app.logger.info('add_customer GET view executed')
    logins = get_login_id(2, db_session)
    return render_template('customer_details_form.html', logins=logins), 200