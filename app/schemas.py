from pydantic import BaseModel

class CourseCreate(BaseModel):
    name: str
    description: str

class CourseUpdate(BaseModel):
    name: str
    description: str

class Course(BaseModel):
    id: int
    name: str
    description: str

    class Config:
        from_attributes = True
