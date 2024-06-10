from __main__ import app
    
from flask import render_template, request, Response
from repository.signup import insert_signup, select_all_signup, select_single_signup
from services.signup_approval import user_approval_service
from model.candidates import AdminUser, CounselorUser, PatientUser
from urllib.parse import parse_qsl

@app.route('/signup/form', methods= ['GET'])
def signup_users_form():
    resp = Response(response=render_template('add_signup.html'), status=200, content_type="text/html")
    return resp

@app.route('/signup/submit', methods= ['POST'])
def signup_users_submit():
    username = request.form['username']
    password = request.form['password']
    user_type = request.form['utype']
    firstname = request.form['firstname']
    lastname = request.form['lastname']
    cid = request.form['cid']
    insert_signup(user=username, passw=password, utype=user_type, fname=firstname, lname=lastname, cid=cid)
    return render_template('add_signup_submit.html', message='Added new user!'), 200

@app.route('/signup/list', methods = ['GET'])
def signup_list_users():
    candidates = select_all_signup()
    print(candidates)
    return render_template('reports/list_candidates.html', records=candidates), 200

@app.route('/signup/approve', methods = ['GET', 'POST'])
@app.route('/signup/approve/<int:utype>', methods = ['GET', 'POST'])
def signup_approve(utype:int=None):
    if (request.method == 'GET'):
        id = request.args['id']
        user = select_single_signup(id)
        utype = user[3]
        if utype == 1:
            adm = AdminUser()
            adm.username = user[1]
            adm.password = user[2]
            adm.utype = user[3]
            adm.firstname = user[4]
            adm.lastname = user[5]
            return render_template('approve_admin_candidate.html', adm=adm, utype=utype), 200
        elif utype == 2:
            cnsl = CounselorUser()
            cnsl.username = user[1]
            cnsl.password = user[2]
            cnsl.utype = user[3]
            cnsl.firstname = user[4]
            cnsl.lastname = user[5]
            cnsl.cid = user[6]
            return render_template('approve_counselor_candidate.html', cnsl=cnsl, utype=utype), 200
        elif utype == 3:
            pat = PatientUser()
            pat.username = user[1]
            pat.password = user[2]
            pat.utype = user[3]
            pat.firstname = user[4]
            pat.lastname = user[5]
            return render_template('approve_patient_candidate.html', pat=pat, utype=utype), 200        
    else:
        utype = int(utype)
        if int(utype) == 1:
            adm = request.get_data()
            adm_dict = dict(parse_qsl(adm.decode('utf-8')))
            adm_model = AdminUser(**adm_dict)
            user_approval_service(int(utype), adm_model)
        elif int(utype) == 2:
            cnsl = request.get_data()
            cnsl_dict = dict(parse_qsl(cnsl.decode('utf-8')))
            cnsl_model = CounselorUser(**cnsl_dict)
            user_approval_service(int(utype), cnsl_model)
        elif int(utype) == 3:
            pat = request.get_data()
            pat_dict = dict(parse_qsl(pat.decode('utf-8')))
            pat_model = PatientUser(**pat_dict)
            user_approval_service(int(utype), pat_model)
        return render_template('approved_user.html', message='approved'), 200