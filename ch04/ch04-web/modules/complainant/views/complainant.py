from flask import render_template, request


from modules.complainant import complainant_bp
from main_cache import cache
from modules.complainant.forms.models import ComplainantForm

from model.config import db_session
from model.db import Complainant
from modules.complainant.repository.complainant import ComplainantRepository
from modules.login.repository.login import LoginRepository

@complainant_bp.route('/complainant/add', methods=['GET', 'POST'])
def add_complainant():
    form:ComplainantForm = ComplainantForm()
    login_repo = LoginRepository(db_session)
    users = login_repo.select_all()
    form.id.choices = [(f"{u.id}", f"{u.username}") for u in users]
    if request.method == 'GET':
        return render_template('complainant_add.html', form=form), 200
    else:
        if form.validate_on_submit():
            details = dict()
            details["id"] = int(form.id.data)
            details["firstname"] = form.firstname.data
            details["lastname"]  = form.lastname.data
            details["middlename"] = form.middlename.data
            details["email"] = form.email.data
            details["mobile"] = form.mobile.data
            details["address"] = form.address.data
            details["zipcode"] = form.zipcode.data
            details["status"]  = form.status.data
            details["date_registered"] = form.date_registered.data
            complainant:Complainant = Complainant(**details)
            complainant_repo:ComplainantRepository = ComplainantRepository(db_session)
            result = complainant_repo.insert(complainant)
            if result:
                records = complainant_repo.select_all()
                return render_template('complainant_list_all.html', records=records), 200
            else:
                return render_template('complainant_add.html', form=form), 500
        else:
            return render_template('complainant_add.html', form=form), 500

@complainant_bp.route('/complainant/list/all', methods=['GET'])
@cache.cached(timeout=50, key_prefix="all_complaints")
def list_all_complainant():
     repo:ComplainantRepository = ComplainantRepository(db_session)
     records = repo.select_all()
     return render_template('complainant_list_all.html', records=records), 200