from flask import render_template, request, flash

from modules.order import order_bp
from modules.order.repository.order import OrderRepository
from modules.login.services.customer import get_all_cid
from modules.product.services.product import get_all_pid

from main import app
from modules.model.db import Orders
from exceptions.db import DatabaseException
from modules.model.config import db_session

@order_bp.route('/orders/add', methods=['GET', 'POST'])
def add_order():
    if request.method == 'POST':
        app.logger.info('add_order POST view executed')
        repo = OrderRepository(db_session)
        order = Orders(cid=int(request.form['cid']), pid=int(request.form['pid']),
                       order_no=request.form['order_no'], order_date=request.form['order_date'])
        result = repo.insert(order)
        if result == False:
            raise DatabaseException()
        customers = get_all_cid(db_session)
        products = get_all_pid(db_session)
        return render_template('add_order_form.html', customers=customers, products=products), 200
    app.logger.info('add_order GET view executed')
    customers = get_all_cid(db_session)
    products = get_all_pid(db_session)
    return render_template('add_order_form.html', customers=customers, products=products), 200

@order_bp.route('/orders/list', methods=['GET'])
def list_orders():
    repo = OrderRepository(db_session)
    orders = repo.select_all()
    flash('List of orders')
    return render_template('list_orders.html', orders=orders), 200