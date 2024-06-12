from flask import render_template, request, flash, current_app
from app.model.db import db, DeliveryOfficer, Shipping
from app.repository.delivery_officer import DeliveryOfficerRepository
from app.repository.shipping import ShippingRepository
from app.services.customer import get_all_cid
from app.services.payment import get_all_payid
from app.services.delivery import get_all_did
from app.exceptions.db import DuplicateRecordException

@current_app.route('/delivery/officer/add', methods = ['GET', 'POST'])
def add_delivery_officer():
    if request.method == 'POST':
        current_app.logger.info('add_delivery_officer POST view executed')
        repo = DeliveryOfficerRepository(db)
        officer = DeliveryOfficer(id=int(request.form['id']), firstname=request.form['firstname'],
                                  middlename=request.form['middlename'], lastname=request.form['lastname'],
                                  mobile=request.form['mobile'], address=request.form['address'],
                                  email=request.form['email'], status=request.form['status'])
        result = repo.insert(officer)
        return render_template('shipping/add_delivery_officer_form.html'), 200 
    current_app.logger.info('add_delivery_officer GET view executed')
    return render_template('shipping/add_delivery_officer_form.html'), 200 

@current_app.route('/shipping/add', methods = ['GET', 'POST'])
def add_shipping():
    customers = get_all_cid(db)
    payments = get_all_payid(db)
    deliveryofficers = get_all_did(db)
    if request.method == 'POST':
        repo = ShippingRepository(db)
        shipping = Shipping(pay_id=int(request.form['pay_id']), cid=int(request.form['cid']), did=int(request.form['did']),
                            amount=float(request.form['amount']), status=request.form['status'],
                            date_shipping=request.form['date_shipping'])
        result = repo.insert(shipping)
        if result == False:
            raise DuplicateRecordException()
    return render_template('shipping/add_shipping_form.html', customers=customers, payments=payments,
                           deliveryofficers=deliveryofficers)
    
@current_app.route('/shipping/list', methods = ['GET'])
def list_shipping():
    repo = ShippingRepository(db)
    shippings = repo.select_all()
    flash('List of shipping')
    return render_template('shipping/list_shipping.html', shippings=shippings), 200
