from flask import Flask
from main_cache import cache
import toml

from model.config import init_db
from flask_session import Session 

init_db()

app = Flask(__name__)   
app.config.from_file('config-dev.toml', toml.load)
sess = Session()

cache.init_app(app)
sess.init_app(app)
    
   
from modules.home import home_bp
from modules.complaint import complaint_bp
   
app.register_blueprint(home_bp, url_prefix='/ch04')
app.register_blueprint(complaint_bp, url_prefix='/ch04')
cache.clear()


if __name__ == '__main__':
    app.run(port=5001)

