from flask import render_template, request, abort, current_app
from modules.model.db import Products
from modules.product.repository.product import ProductRepository
from modules.product import product_bp
from modules import db


@product_bp.route('/products/add', methods = ['GET', 'POST'])
def add_product():
    if request.method == 'POST':
        current_app.logger.info('add_product POST view executed')
        prod = Products(name=request.form['name'],
                        code=request.form['code'], price=request.form['price']) 
        repo = ProductRepository(db)
        result = repo.insert(prod)
        if result == False:
            abort(500)
        return render_template('add_prod_form.html'), 200 
    current_app.logger.info('add_product GET view executed')
    return render_template('add_prod_form.html'), 200 
    
@product_bp.route('/products/list', methods = ['GET'])
def list_all_prods():
    repo = ProductRepository(db)
    prods = repo.select_all()
    return render_template('list_products.html', prods=prods), 200 