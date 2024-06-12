from werkzeug.exceptions import HTTPException

class DatabaseException(HTTPException):
    code = 500
    description = ""
        
    def __init__(self, message, status_code=None, payload=None):
        super().__init__()
        self.description = message
        if status_code is not None:
            self.code = status_code
        self.payload = payload

    def to_dict(self):
        rv = dict(self.payload or ())
        rv['description'] = self.description
        rv['code'] = self.code
        return rv
    
class DuplicateRecordException(HTTPException):
    code = 500
    description = ""
        
    def __init__(self, message, status_code=None, payload=None):
        super().__init__()
        self.description = message
        if status_code is not None:
            self.code = status_code
        self.payload = payload

    def to_dict(self):
        rv = dict(self.payload or ())
        rv['description'] = self.description
        rv['code'] = self.code
        return rv

   
class EmptyListResultException(HTTPException):
    code = 500
    description = ""
        
    def __init__(self, message, status_code=None, payload=None):
        super().__init__()
        self.description = message
        if status_code is not None:
            self.code = status_code
        self.payload = payload

    def to_dict(self):
        rv = dict(self.payload or ())
        rv['description'] = self.description
        rv['code'] = self.code
        return rv
    
class NoRecordException(HTTPException):
    code = 500
    description = ""
        
    def __init__(self, message, status_code=None, payload=None):
        super().__init__()
        self.description = message
        if status_code is not None:
            self.code = status_code
        self.payload = payload

    def to_dict(self):
        rv = dict(self.payload or ())
        rv['description'] = self.description
        rv['code'] = self.code
        return rv