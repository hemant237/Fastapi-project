from sqlalchemy import ForeignKey,String
from sqlalchemy.orm import Mapped,mapped_column,relationship
from app.database import Base

class Employee(Base):
    __tablename__="employees"

    id : Mapped[int] = mapped_column(primary_key=True)

    name : Mapped[str] = mapped_column(String)

    salary : Mapped[int]

    department_id : Mapped[int] = mapped_column(ForeignKey("departments.id"))

    department=relationship("Department",back_populates="employees")




