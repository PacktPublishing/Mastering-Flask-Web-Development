from flask import Flask, make_response, render_template
import toml
from sock_config import sock
from celery_config import celery_init_app

from exceptions.custom import MissingFileException, InvalidTypeException, NoneFilenameException, TooLargeException, FileSavingException

app = Flask(__name__, template_folder='pages', static_folder="resources")
app.config.from_file("config_dev.toml", toml.load)
celery_app = celery_init_app(app)

@app.errorhandler(404)
def not_found(e):
    return make_response(render_template("error/404.html", title="Page not found"), 404)

@app.errorhandler(400)
def bad_request(e):
    return make_response(render_template("error/400.html", title="Bad request"), 400)

def server_error(e):
    print(e)
    return make_response(render_template("error/500.html", title="Internal server error"), 500) 

@app.errorhandler(MissingFileException)
def missing_file_exception(e):
    print(e)
    return e.get_response()

@app.errorhandler(InvalidTypeException)
def invalid_type_exception(e):
    print(e)
    return e.get_response()

@app.errorhandler(TooLargeException)
def too_large_exception(e):
    print(e)
    return e.get_response()

@app.errorhandler(NoneFilenameException)
def none_filename_exception(e):
    print(e)
    return e.get_response() 

@app.errorhandler(FileSavingException)
def file_saving_exception(e):
    print(e)
    return e.get_response()

app.register_error_handler(500, server_error)

from modules.home import home_bp
from modules.equations import eqn_bp
from modules.realtime import rt_bp
from modules.external import external_bp
from modules.rendition import rendition_bp
from modules.upload import upload_bp
from modules.internal import internal_bp

with app.app_context():
    sock.init_app(app)
    app.register_blueprint(home_bp, url_prefix='/ch06')
    app.register_blueprint(eqn_bp, url_prefix='/ch06')
    app.register_blueprint(rt_bp, url_prefix='/ch06')
    app.register_blueprint(external_bp, url_prefix='/ch06')
    app.register_blueprint(rendition_bp, url_prefix='/ch06')
    app.register_blueprint(upload_bp, url_prefix='/ch06')
    app.register_blueprint(internal_bp, url_prefix='/ch06')


if __name__ == "__main__":
    app.run()