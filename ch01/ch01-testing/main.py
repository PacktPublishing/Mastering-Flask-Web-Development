from flask import Flask
import toml
import json
from converter.date_converter import DateConverter

from views.index import create_index_routes
from views.signup import create_signup_routes
from views.examination import create_examination_routes
from views.reports import create_reports_routes
from views.admin import create_admin_routes
from views.login import create_login_routes
from views.profile import create_profile_routes
from views.certificates import create_certificates_routes

app = Flask(__name__, template_folder='pages')
# app.config.from_file('config.toml', toml.load)
# app.config.from_file("config.json", load=json.load)
# app.config.from_pyfile('myconfig.py')


app.url_map.converters['date'] = DateConverter

@app.route('/', methods = ['GET'])
def index():
    return "This is an online personal counseling system (OPCS)"

# place here the imports for APIs
create_index_routes(app)
create_signup_routes(app)
create_examination_routes(app)
create_reports_routes(app)
create_admin_routes(app)
create_login_routes(app)
create_profile_routes(app)
create_certificates_routes(app)
from views.contract import ContractView, DeleteContractByPIDView, ListUnpaidContractView

app.add_url_rule('/contract/patient/add/form', view_func=ContractView.as_view('contract-view'))
app.add_url_rule('/contract/patient/delete', view_func=DeleteContractByPIDView.as_view('delete-contract-view'))
app.add_url_rule('/contract/unpaid/patients', view_func=ListUnpaidContractView.as_view('list-unpaid-view'))

if __name__ == '__main__':
    # app.run(debug=True) 
    app.run()
    
    # ImportError cannot import name 'app' from '__main__'
