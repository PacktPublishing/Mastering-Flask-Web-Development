from flask import render_template, request, session, flash, current_app


from app.model.db import db, Orders
from app.repository.order import OrderRepository
from app.services.customer import get_all_cid
from app.services.product import get_all_pid

from app.exceptions.db import DatabaseException

@current_app.route('/orders/add', methods=['GET', 'POST'])
def add_order():
    if request.method == 'POST':
        current_app.logger.info('add_order POST view executed')
        repo = OrderRepository(db)
        order = Orders(cid=int(request.form['cid']), pid=int(request.form['pid']),
                       order_no=request.form['order_no'], order_date=request.form['order_date'])
        result = repo.insert(order)
        if result == False:
            raise DatabaseException()
        customers = get_all_cid(db)
        products = get_all_pid(db)
        return render_template('order/add_order_form.html', customers=customers, products=products), 200
    current_app.logger.info('add_order GET view executed')
    customers = get_all_cid(db)
    products = get_all_pid(db)
    return render_template('order/add_order_form.html', customers=customers, products=products), 200

@current_app.route('/orders/list', methods=['GET'])
def list_orders():
    repo = OrderRepository(db)
    orders = repo.select_all()
    flash('List of orders')
    return render_template('order/list_orders.html', orders=orders), 200