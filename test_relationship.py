from app.database import SessionLocal
from app.models.department import Department 
from app.models.employee import Employee

db= SessionLocal()

department = db.query(Department).filter(
    Department.name == "IT"
).first()

employee = Employee(name="Hemant")

department.employees.append(employee)

db.commit()
db.refresh(employee)

print ("Employee ID :",employee.id)
print("Employee Name :",employee.name)
print("Department Id :",department.id)
print("Department Name :",employee.department.name)

db.close()