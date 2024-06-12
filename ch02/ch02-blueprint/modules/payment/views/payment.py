from flask import render_template, request, flash, abort

from modules.payment import payment_bp
from modules.payment.repository.payment import PaymentTypeRepository, PaymentRepository
from modules.order.services.order import get_all_order_no

from main import   app
from modules.model.db import PaymentType, Payment
from modules.model.config import db_session

@payment_bp.route('/payment/type/add', methods = ['GET', 'POST'])
def add_payment_type():
    if request.method == 'POST':
        app.logger.info('add_payment_type POST view executed')
        repo = PaymentTypeRepository(db_session)
        payType = PaymentType(name=request.form['name'])
        result = repo.insert(payType)
        return render_template('add_payment_scheme_form.html'), 200 
    app.logger.info('add_payment_type GET view executed')
    return render_template('add_payment_scheme_form.html'), 200 

@payment_bp.route('/payment/add', methods = ['GET', 'POST'])
def add_payment():
    if request.method == 'POST':
        app.logger.info('add_payment POST view executed')
        repo_type = PaymentTypeRepository(db_session)
        ptypes = repo_type.select_all()
        orders = get_all_order_no(db_session)
        repo = PaymentRepository(db_session)
        payment = Payment(order_no=request.form['order_no'], mode_payment=int(request.form['mode']),
                          ref_no=request.form['ref_no'], date_payment=request.form['date_payment'],
                          amount=request.form['amount'])
        result = repo.insert(payment)
        if result == False:
            abort(500)
        return render_template('add_payment_form.html', orders=orders, ptypes=ptypes), 200 
    app.logger.info('add_payment GET view executed')
    repo_type = PaymentTypeRepository(db_session)
    ptypes = repo_type.select_all()
    orders = get_all_order_no(db_session)
    return render_template('add_payment_form.html', orders=orders, ptypes=ptypes), 200 

@payment_bp.route('/payment/list', methods = ['GET'])
def list_payments():
    repo = PaymentRepository(db_session)
    payments = repo.select_all()
    flash('List of payments')
    return render_template('list_payments.html', payments=payments), 200
