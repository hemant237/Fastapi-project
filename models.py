from sqlalchemy import Integer,String
from sqlalchemy.orm import DeclarativeBase,Mapped,mapped_column


class Base(DeclarativeBase):
    pass

class Student(Base):
    __tablename__="students"

    id : Mapped[int]=mapped_column(Integer,primary_key=True)
    name : Mapped[str] = mapped_column(String)
    age : Mapped[int] = mapped_column(Integer)

    
