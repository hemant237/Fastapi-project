from pydantic import BaseModel , ConfigDict
from app.schemas.department import DepartmentResponse


class EmployeeRequest(BaseModel):
    name : str
    department_id : int
    salary : int

class EmployeeResponse(BaseModel):
    id : int
    name : str
    department_id : int
    salary : int
    department : DepartmentResponse

    model_config=ConfigDict(from_attributes=True)

class EmployeeUpdate(BaseModel):
    name : str | None = None
    department_id : int | None = None  
    salary : int | None = None  

    
