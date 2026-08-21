from fastapi import APIRouter,Depends ,HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.student import Student
from app.schemas.student import StudentRequest,StudentResponse,StudentUpdate

router=APIRouter()


## POST DATA
@router.post("/students",
             response_model=StudentResponse,
             status_code=201)

def create_student(
    student : StudentRequest,
    db : Session = Depends(get_db)
):

    db_student=Student(
        name=student.name,
        age=student.age
    )

    db.add(db_student)
    db.commit()
    db.refresh(db_student)

    return db_student

## GET DATA
@router.get("/students",
            response_model=list[StudentResponse])

def get_students(
    db : Session = Depends(get_db)
):

    students=db.query(Student).all()

    return students


#GET DATA BY ID
@router.get("/students/{student_id}",
            response_model=StudentResponse)

def get_student(
    student_id : int,
    db : Session = Depends(get_db)
):
    student=db.get(Student,student_id)

    if student is None:
        raise HTTPException(
            status_code=404,
            detail="Student Not Found"
        )
    return student

@router.put("/students/{student_id}",
             response_model=StudentResponse)

def update_student(
    student_id : int,
    student : StudentRequest,
    db : Session = Depends(get_db)
):

    existing_student=db.get(Student,student_id)

    if existing_student is None:
        raise HTTPException(
            ststus_code=404,
            detail="Student not Found"
        )

    existing_student.name=student.name
    existing_student.age=student.age

    db.commit()
    db.refresh(existing_student)

    return existing_student

## PATCH ENDPOINT
@router.patch("/students/{student_id}",
              response_model=StudentResponse)
def update_student_partial(
    student_id : int,
    student : StudentUpdate,
    db : Session =Depends(get_db)
):

    existing_student=db.get(Student,student_id)

    if existing_student is None:
        raise HTTPException(
            status_code=404,
            detail="Student Not Found"
        )
    
    update_data=student.model_dump(
        exclude_unset=True
    )

    for key,value in update_data.items():
        setattr(existing_student,key,value)

    db.commit()
    db.refresh(existing_student)

    return existing_student

@router.delete(
    "/students/{student_id}"
)    
def delete_students(
    student_id : int,
db : Session = Depends(get_db)
):

    student=db.get(Student,student_id)

    if student is None :
        raise HTTPException(
            status_code=404,
            detail="Student Not Found"
        )

    db.delete(student)
    db.commit()

    return {"message": "Student Deleted Successfully"}


    

