from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse

from sqlalchemy.orm import Session
from modules_fastapi.models.config import SessionFactory
from modules_fastapi.repository.faculty_borrower import FacultyBorrowerRepository
from modules_fastapi.models.requests import BorrowerReq
from modules_fastapi.models.db import FacultyBorrower

router = APIRouter()

def sess_db():
    db = SessionFactory()
    try:
        yield db
    finally:
        db.close()

@router.post("/faculty/borrower/add")
async def add_faculty_borrower(req:BorrowerReq, sess:Session = Depends(sess_db)):
   repo:FacultyBorrowerRepository = FacultyBorrowerRepository(sess)
   faculty = FacultyBorrower(empid=req.empid, firstname=req.firstname, lastname=req.lastname)
   result = repo.insert(faculty)
   if result == True:
        return JSONResponse(content=faculty.to_json())
   else: 
        return JSONResponse(content={'message':'create faculty borrower problem encountered'}, status_code=500)


@router.get("/faculty/borrower/list/all")
async def list_all_faculty_borrowers(sess:Session = Depends(sess_db)):
    repo:FacultyBorrowerRepository = FacultyBorrowerRepository(sess)
    result = repo.get_all_faculty_borrowers()
    return result