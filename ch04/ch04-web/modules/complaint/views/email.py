
from flask import render_template, request, session, redirect
from flask_mail import Message
from mail_config import mail

from modules.complaint.forms.models import EmailComplaintForm
from complaint import complaint_bp


@complaint_bp.route("/complaint/email")
def email_complaint():
    form:EmailComplaintForm = EmailComplaintForm()
    if request.method == 'GET':
        return render_template('email_form.html', form=form), 200
    if form.validate_on_submit():
       try:
           recipients = [rec for rec in str(form.to.data).split(';')]
           msg = Message(form.subject, sender = 'your_email@gmail.com', recipients = recipients)
           msg.body = form.message.data
           mail.send(msg)
           form:EmailComplaintForm = EmailComplaintForm()
           return render_template('email_.html', form=form, message='Email sent.'), 200
       except:
         return render_template('email_.html', form=form), 500
    else:
        return render_template('email_.html', form=form), 500
   
   

