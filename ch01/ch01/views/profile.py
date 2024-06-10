from __main__ import app
from flask import request, render_template
from model.profile import Profile
from model.candidates import AdminUser


@app.route('/profile', methods=['GET', 'POST'])
def ask_profile():
    if request.method == 'GET':
        p = Profile()
        return render_template('/profile.html', p=p ), 200
    else:
        p = request.get_data()
        a = AdminUser()
        
        name = request.form['id']
        return name, 200
        


