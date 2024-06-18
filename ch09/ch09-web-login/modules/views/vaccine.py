from flask import render_template, current_app, request, flash
from modules.repository.login import LoginRepository
from modules.models.config import db_session

@current_app.route('/vaccine/add', methods = ['GET', 'POST'])
async def add_vaccine():
    return render_template('vaccine/add_vaccine.html'), 200

@current_app.route('/vaccine/center/add', methods = ['GET', 'POST'])
async def add_vaccine_center():
    return render_template('vaccine/add_vaccine_center.html'), 200


@current_app.route('/vaccine/registration', methods = ['GET', 'POST'])
async def add_vaccine_registration():
    return render_template('vaccine/add_vaccine_registration.html'), 200

@current_app.route('/vaccine/inventory', methods = ['GET', 'POST'])
async def add_vaccine_inventory():
    return render_template('vaccine/add_vaccine_inventory.html'), 200

@current_app.route('/vaccination/card', methods = ['GET', 'POST'])
async def add_vaccination_card():
    return render_template('vaccine/add_vaccine_card.html'), 200