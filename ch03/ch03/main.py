
from app import create_app
from app.exceptions.db import DuplicateRecordException
from werkzeug.exceptions import HTTPException
from flask import jsonify, request, abort, Response
from flask.json.provider import JSONProvider
from datetime import date, datetime
import orjson
import json
import werkzeug.wrappers
import werkzeug.wsgi

class OrjsonJsonProvider(JSONProvider):
    def __init__(self, *args, **kwargs):
        self.options = kwargs
        super().__init__(*args, **kwargs)

    def dumps(self, obj, **kwargs):
        print("dumps")
        return orjson.dumps(obj, option=orjson.OPT_NON_STR_KEYS).decode('utf-8')

    def loads(self, s, **kwargs):
        print("dumps")
        return orjson.loads(s)
    

class ImprovedJsonProvider(JSONProvider):
    def __init__(self, *args, **kwargs):
        self.options = kwargs
        super().__init__(*args, **kwargs)
    
    def default(self, o):
        print('done')
        if isinstance(o, date):
            return o.strftime("%m/%d/%Y")
        elif isinstance(o, date):
            return o.strftime("%m/%d/%Y, , %H:%M:%S")
        return super().default(self, o)

    def dumps(self, obj, **kwargs):
        kwargs.setdefault("default", self.default)
        kwargs.setdefault("ensure_ascii", True)
        kwargs.setdefault("sort_keys", True)
        return json.dumps(obj, **kwargs)

    def loads(self, s: str | bytes, **kwargs):
        s_dict:dict = json.loads(s.decode('utf-8'))
        s_sanitized = dict((k, v) for k, v in s_dict.items() if v)
        s_str = json.dumps(s_sanitized)
        return json.loads(s_str, **kwargs)
    
class AppMiddleware:
    def __init__(self, app):
        self.app = app

    def __call__(self, environ, start_response):
        request = werkzeug.wrappers.Request(environ)
        api_path = request.url
        print(f'accessing URL endpoint: {api_path} ')
        iterator:werkzeug.wsgi.ClosingIterator = self.app(environ, start_response)
        response = werkzeug.wrappers.Response(start_response)
        print(f'exiting URL endpoint: {api_path} ')
        print(f'{response.access_control_allow_origin}')

        return iterator

app = create_app('../config_dev.toml')
#app.json_encoder = CustomJSONEncoder
app.json = ImprovedJsonProvider(app)
app.wsgi_app = AppMiddleware(app.wsgi_app)


@app.before_request
def before_request_func():
    api_method = request.method
    if api_method in ['POST', 'PUT', 'PATCH']:
        if request.json == '' or request.json == None:
            abort(500, description="request body is empty")
    api_endpoint_func = request.endpoint
    api_path = request.path
    app.logger.info(f'accessing URL endpoint: {api_path}, function name: {api_endpoint_func} ')

@app.after_request
def after_request_func(response:Response):
    api_endpoint_func = request.endpoint
    api_path = request.path
    resp_allow_origin = response.access_control_allow_origin
    app.logger.info(f"access_control_allow_origin header: {resp_allow_origin}")
    app.logger.info(f'exiting URL endpoint: {api_path}, function name: {api_endpoint_func} ')
    return response

@app.errorhandler(404)
def not_found(e):
    return jsonify(error=str(e)), 404

@app.errorhandler(400)
def bad_request(e):
    return jsonify(error=str(e)), 400

def server_error(e):
    print(e)
    return jsonify(error=str(e)), 500

@app.errorhandler(DuplicateRecordException)
def insert_record_exception(e):
    return jsonify(e.to_dict()), e.status_code

app.register_error_handler(500, server_error)
#app.register_error_handler(DuplicateRecordException, insert_record_exception)

@app.errorhandler(Exception)
def handle_built_exception(e):
    if isinstance(e, HTTPException):
        return e
    return jsonify(error=str(e)), 500

if __name__ == "__main__":
    app.run()
    
