from pydantic import BaseModel ,ConfigDict 

class StudentRequest(BaseModel):
    name : str
    age : int


class StudentUpdate(BaseModel):
    name : str | None = None
    age : int | None = None

class StudentResponse(BaseModel):
    model_config=ConfigDict(from_attributes=True)

    id : int
    name : str
    age : int


         