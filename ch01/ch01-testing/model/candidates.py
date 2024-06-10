from datetime import date

class AdminUser:
    id:int
    position:str
    age:int
    emp_date:date
    emp_status:str
    username:str
    password:str
    utype:int
    firstname:str
    lastname:str
    def __init__(self, **kwargs ):
        self.id = kwargs.get('id', 0)
        self.position = kwargs.get('position', '')
        self.age = kwargs.get('age', 0)
        self.emp_date = kwargs.get('emp_date', None)
        self.emp_status = kwargs.get('emp_status', '')
        self.username = kwargs.get('username', '')
        self.password = kwargs.get('password', '')
        self.utype = kwargs.get('utype', 0)
        self.firstname = kwargs.get('firstname', '')
        self.lastname = kwargs.get('lastname', '')
     

class CounselorUser:
    id:int
    age:int
    position:str
    prof_started:date
    username:str
    password:str
    utype:int
    firstname:str
    lastname:str
    cid:str
    def __init__(self, **kwargs):
        self.id = kwargs.get('id', 0)
        self.age = kwargs.get('age', 0)
        self.position = kwargs.get('position', '')
        self.prof_started = kwargs.get('prof_started', None)
        self.username = kwargs.get('username', '')
        self.password = kwargs.get('password', '')
        self.utype = kwargs.get('utype', 0)
        self.firstname = kwargs.get('firstname', '')
        self.lastname = kwargs.get('lastname', '')
        self.cid = kwargs.get('cid', '')

class PatientUser:
    id:int 
    age:int
    gender:str
    cstatus:str
    address:str
    mobile:str
    occupation:str
    nationality:str
    cid:str
    counsel_started:date
    counsel_ended:date
    username:str
    password:str
    utype:int
    firstname:str
    lastname:str
    
    def __init__(self, **kwargs):
        self.id = kwargs.get('id', 0)
        self.age = kwargs.get('age', 0)
        self.gender = kwargs.get('gender', '')
        self.cstatus = kwargs.get('cstatus', '')
        self.address = kwargs.get('address', '')
        self.mobile = kwargs.get('mobile', '')
        self.occupation = kwargs.get('occupation', '')
        self.nationality = kwargs.get('nationality', '')
        self.cid = kwargs.get('cid', '')
        self.counsel_started = kwargs.get('counsel_started', '')
        self.counsel_ended = kwargs.get('counsel_ended', '')
        self.username = kwargs.get('username', '')
        self.password = kwargs.get('password', '')
        self.utype = kwargs.get('utype', 0)
        self.firstname = kwargs.get('firstname', '')
        self.lastname = kwargs.get('lastname', '')
    