from werkzeug.exceptions import HTTPException
from flask import render_template, Response

class MissingFileException(HTTPException):
    code = 500
    description = "Uploaded file does not exist."
        
    def get_response(self, environ=None):
        resp = Response()
        resp.response = render_template('error/generic.html', ex_message=self.description)
        return resp
    
class NoneFilenameException(HTTPException):
    code = 500
    description = "No filename provided."
        
    def get_response(self, environ=None):
        resp = Response()
        resp.response = render_template('error/generic.html', ex_message=self.description)
        return resp

class InvalidTypeException(HTTPException):
    code = 500
    description = "Filetype not supported."
        
    def get_response(self, environ=None):
        resp = Response()
        resp.response = render_template('error/generic.html', ex_message=self.description)
        return resp
    
class TooLargeException(HTTPException):
    code = 500
    description = "Content is too large for processing."
        
    def get_response(self, environ=None):
        resp = Response()
        resp.response = render_template('error/generic.html', ex_message=self.description)
        return resp
    
class FileSavingException(HTTPException):
    code = 500
    description = "Problem encountered during saving."
        
    def get_response(self, environ=None):
        resp = Response()
        resp.response = render_template('error/generic.html', ex_message=self.description)
        return resp