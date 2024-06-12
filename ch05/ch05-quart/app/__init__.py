
from quart import Quart
import toml
from app.model.config import init_db

from app.api.home import home, welcome
from app.api.login import add_login, list_all_login

def create_app(config_file):
    app = Quart(__name__, template_folder='../app/pages', static_folder="../app/resources")
    app.config.from_file(config_file, toml.load)
    init_db()
    
    app.add_url_rule('/ch05/home', view_func=home, endpoint='home')
    app.add_url_rule('/ch05/welcome', view_func=welcome, endpoint='welcome')
    app.add_url_rule('/ch05/login/add', view_func=add_login, endpoint='add_login')
    app.add_url_rule('/ch05/login/list/all', view_func=list_all_login, endpoint='list_all_login')
    
    return app

