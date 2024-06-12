from app import create_app
from flask import jsonify, request
from app.exceptions.db import DuplicateRecordException
from werkzeug.exceptions import HTTPException

app, celery_app = create_app('../config_dev.toml')

@app.before_request
async def init_request():
    app.logger.info('executing ' + request.endpoint + ' starts')
    
@app.after_request
async def return_response(response):
    app.logger.info('executing ' + request.endpoint + ' stops')
    return response

@app.errorhandler(404)
async def not_found(e):
    return jsonify(error=str(e)), 404

@app.errorhandler(400)
async def bad_request(e):
    return jsonify(error=str(e)), 400

@app.errorhandler(DuplicateRecordException)
async def insert_record_exception(e):
    return jsonify(e.to_dict()), e.code

async def server_error(e):
    print(e)
    return jsonify(error=str(e)), 500

app.register_error_handler(500, server_error)
#app.register_error_handler(DuplicateRecordException, insert_record_exception)


@app.errorhandler(Exception)
async def handle_built_exception(e):
    if isinstance(e, HTTPException):
        return e
    return jsonify(error=str(e)), 500


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')

