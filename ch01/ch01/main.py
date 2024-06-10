from flask import Flask
import toml
import json
from converter.date_converter import DateConverter

app = Flask(__name__, template_folder='pages')
# app.config.from_file('config.toml', toml.load)
# app.config.from_file("config.json", load=json.load)
# app.config.from_pyfile('myconfig.py')


app.url_map.converters['date'] = DateConverter

@app.route('/', methods = ['GET'])
def index():
    return "This is an online personal counseling system (OPCS)"

# place here the imports for custom APIs
import views.index
import views.certificates
import views.signup
import views.examination
import views.reports
import views.admin
import views.login
import views.profile
from views.contract import ContractView, DeleteContractByPIDView, ListUnpaidContractView

app.add_url_rule('/certificate/terminate/<string:counselor>/<date:effective_date>/<string:patient>', 'show_honor_dissmisal', views.certificates.show_honor_dissmisal)
app.add_url_rule('/contract/patient/add/form', view_func=ContractView.as_view('contract-view'))
app.add_url_rule('/contract/patient/delete', view_func=DeleteContractByPIDView.as_view('delete-contract-view'))
app.add_url_rule('/contract/unpaid/patients', view_func=ListUnpaidContractView.as_view('list-unpaid-view'))

if __name__ == '__main__':
    # app.run(debug=True) 
    app.run()