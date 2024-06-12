from flask import render_template, request, flash, abort, current_app
from modules.model.db import PaymentType, Payment
from modules.payment.repository.payment import PaymentTypeRepository, PaymentRepository
from modules.order.services.order import get_all_order_no
from modules.payment import payment_bp
from modules import db



@payment_bp.route('/payment/type/add', methods = ['GET', 'POST'])
def add_payment_type():
    if request.method == 'POST':
        current_app.logger.info('add_payment_type POST view executed')
        repo = PaymentTypeRepository(db)
        payType = PaymentType(name=request.form['name'])
        result = repo.insert(payType)
        return render_template('add_payment_scheme_form.html'), 200 
    current_app.logger.info('add_payment_type GET view executed')
    return render_template('add_payment_scheme_form.html'), 200 

@payment_bp.route('/payment/add', methods = ['GET', 'POST'])
def add_payment():
    if request.method == 'POST':
        current_app.logger.info('add_payment POST view executed')
        repo_type = PaymentTypeRepository(db)
        ptypes = repo_type.select_all()
        orders = get_all_order_no(db)
        repo = PaymentRepository(db)
        payment = Payment(order_no=request.form['order_no'], mode_payment=int(request.form['mode']),
                          ref_no=request.form['ref_no'], date_payment=request.form['date_payment'],
                          amount=request.form['amount'])
        result = repo.insert(payment)
        if result == False:
            abort(500)
        return render_template('add_payment_form.html', orders=orders, ptypes=ptypes), 200 
    current_app.logger.info('add_payment GET view executed')
    repo_type = PaymentTypeRepository(db)
    ptypes = repo_type.select_all()
    orders = get_all_order_no(db)
    return render_template('add_payment_form.html', orders=orders, ptypes=ptypes), 200 

@payment_bp.route('/payment/list', methods = ['GET'])
def list_payments():
    repo = PaymentRepository(db)
    payments = repo.select_all()
    flash('List of payments')
    return render_template('list_payments.html', payments=payments), 200
