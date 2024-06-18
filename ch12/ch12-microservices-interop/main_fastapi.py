from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from modules_fastapi.api import faculty


fast_app = FastAPI()
fast_app.add_middleware(
    CORSMiddleware, allow_origins=['*'],
    allow_credentials=True, allow_methods=['*'], allow_headers=['*'])
fast_app.include_router(faculty.router, prefix='/ch12')



