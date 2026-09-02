from fastapi import APIRouter, Depends ,HTTPException 
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.employee import Employee
from app.models.department import Department
from app.schemas.employee import EmployeeRequest, EmployeeResponse ,EmployeeUpdate

from app.core.security import get_current_user , require_admin
from app.models.user import User

router=APIRouter()

@router.post("/employees",response_model=EmployeeResponse,
             status_code=201)

def create_employee(
    employee : EmployeeRequest,
    db : Session = Depends(get_db),
    current_user : User = Depends(require_admin)
):

    department = db.get(Department,employee.department_id)

    if department is None:
        raise HTTPException(
            status_code = 404,
            detail = "Employee Not Found"
        )

    db_employee=Employee(name = employee.name,
                         department_id = employee.department_id,
                         salary = employee.salary)

    db.add(db_employee)
    db.commit()
    db.refresh(db_employee)

    return db_employee

@router.get("/employees/",response_model=list[EmployeeResponse])
def get_employees(
    db : Session =Depends(get_db),
    current_user : User = Depends(get_current_user)
):
    employees=db.query(Employee).all()

    return employees

@router.get("/employee/{employee_id}",response_model=EmployeeResponse)
def get_employee(
    employee_id : int,
    db : Session = Depends(get_db)
):
    employee = db.get(Employee,employee_id)

    if employee is None:
        raise HTTPException(
            status_code=404,
            detail="Employee Not Found"
        )

    return employee

@router.patch("/employees/{employee_id}",
              response_model=EmployeeResponse)
def update_employee(
    employee_id : int,
    employee : EmployeeUpdate,
    db : Session = Depends(get_db)
):
    existing_employee=db.get(Employee,employee_id)

    if existing_employee is None:
        raise HTTPException(
            status_code=404,
            detail="Employee Not Found"
        )
    if employee.department_id is not None:
        department=db.get(Department,employee.department_id)

        if department is None:
            raise HTTPException(
                status_code=404,detail="Department Not Found"
            )

    update_data=employee.model_dump(exclude_unset=True)

    for key , value in update_data.items():
        setattr(existing_employee,key,value)

    db.commit()
    db.refresh(existing_employee)

    return existing_employee     

@router.delete("/employees/{employee_id}")
def delete_employee(
    employee_id : int,
    db : Session = Depends(get_db),
    current_user : User = Depends(require_admin)
):
    employee = db.get(Employee,employee_id)

    if employee is None:
        raise HTTPException(
            status_code=404,
            detail="Employee NOt Found"
        )

    db.delete(employee)
    db.commit()

    return{ "message" : "Employee Deleted Successfully"}




