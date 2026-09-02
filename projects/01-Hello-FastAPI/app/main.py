from fastapi import FastAPI

from app.routers.students import router as student_router
from app.routers.employees import router as employee_router
from app.routers.auth import router as auth_router

app=FastAPI(title="Hemant")

app.include_router(student_router)
app.include_router(employee_router)
app.include_router(auth_router)