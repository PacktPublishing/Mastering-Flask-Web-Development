from werkzeug.exceptions import HTTPException
from flask import render_template, Response

class DatabaseException(HTTPException):
    code = 500
    description = 'Database encountered problem.'
    
    def get_response(self, environ=None):
        resp = Response()
        resp.response = render_template('error/generic.html', ex_message=self.description)
        return resp
    
class DuplicateRecordException(HTTPException):
    code = 500
    description = 'Record already exists.'
    
    def get_response(self, environ=None):
        resp = Response()
        resp.response = render_template('error/generic.html', ex_message=self.description)
        return resp

   
class EmptyListResultException(HTTPException):
    code = 500
    description = 'Empty query result.'
    
    def get_response(self, environ=None):
        resp = Response()
        resp.response = render_template('error/generic.html', ex_message=self.description)
        return resp
    
class NoRecordException(HTTPException):
    code = 500
    description = 'No single record retrieved.'
    
    def get_response(self, environ=None):
        resp = Response()
        resp.response = render_template('error/generic.html', ex_message=self.description)
        return resp