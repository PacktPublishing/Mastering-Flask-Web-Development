from flask import render_template, request, flash

from modules.shipping import shipping_bp
from modules.shipping.repository.delivery_officer import DeliveryOfficerRepository
from modules.shipping.repository.shipping import ShippingRepository
from modules.login.services.customer import get_all_cid
from modules.payment.services.payment import get_all_payid
from modules.shipping.services.delivery import get_all_did

from main import  app
from modules.model.db import  DeliveryOfficer, Shipping
from exceptions.db import DuplicateRecordException
from modules.model.config import db_session

@shipping_bp.route('/delivery/officer/add', methods = ['GET', 'POST'])
def add_delivery_officer():
    if request.method == 'POST':
        app.logger.info('add_delivery_officer POST view executed')
        repo = DeliveryOfficerRepository(db_session)
        officer = DeliveryOfficer(id=int(request.form['id']), firstname=request.form['firstname'],
                                  middlename=request.form['middlename'], lastname=request.form['lastname'],
                                  mobile=request.form['mobile'], address=request.form['address'],
                                  email=request.form['email'], status=request.form['status'])
        result = repo.insert(officer)
        return render_template('add_delivery_officer_form.html'), 200 
    app.logger.info('add_delivery_officer GET view executed')
    return render_template('add_delivery_officer_form.html'), 200 

@shipping_bp.route('/shipping/add', methods = ['GET', 'POST'])
def add_shipping():
    customers = get_all_cid(db_session)
    payments = get_all_payid(db_session)
    deliveryofficers = get_all_did(db_session)
    if request.method == 'POST':
        repo = ShippingRepository(db_session)
        shipping = Shipping(pay_id=int(request.form['pay_id']), cid=int(request.form['cid']), did=int(request.form['did']),
                            amount=float(request.form['amount']), status=request.form['status'],
                            date_shipping=request.form['date_shipping'])
        result = repo.insert(shipping)
        if result == False:
            raise DuplicateRecordException()
    return render_template('add_shipping_form.html', customers=customers, payments=payments,
                           deliveryofficers=deliveryofficers)
    
@shipping_bp.route('/shipping/list', methods = ['GET'])
def list_shipping():
    repo = ShippingRepository(db_session)
    shippings = repo.select_all()
    flash('List of shipping')
    return render_template('list_shipping.html', shippings=shippings), 200
