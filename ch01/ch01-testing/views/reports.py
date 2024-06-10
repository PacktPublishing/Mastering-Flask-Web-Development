   
from flask import render_template, request, make_response, Response
from services.utility import list_usernames

def create_reports_routes(app):
    @app.route('/users/list/usernames', methods=['GET'])
    def render_usernames():
        usernames = list_usernames()
        headers = dict()
        headers['Content-Disposition'] = 'attachment;filename=usernames.doc'
        resp = Response(response=render_template('reports/list_usernames.html', usernames=usernames), status=200, content_type='application/msword', headers=headers)
        return resp
