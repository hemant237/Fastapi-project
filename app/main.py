from fastapi import FastAPI

from app.database import Base, engine
from app.models.student import Student
from app.routers.students import router as student_router
from app.models.student import Student
from app.models.employee import Employee
from app.models.department import Department
from app.routers.employees import router as employee_router
from app.routers.auth import router as auth_router

Base.metadata.create_all(bind=engine)

app=FastAPI()

app.include_router(student_router)
app.include_router(employee_router)
app.include_router(auth_router)