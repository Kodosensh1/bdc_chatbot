from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import Course
from app.schemas import CourseCreate, CourseUpdate

# Router yaradılması
router = APIRouter(
    prefix="/courses",
    tags=["courses"]
)

# Yeni kurs əlavə etmək üçün endpoint
@router.post("/", response_model=dict)
def create_course(course: CourseCreate, db: Session = Depends(get_db)):
    new_course = Course(name=course.name, description=course.description)
    db.add(new_course)
    db.commit()
    db.refresh(new_course)
    return {"message": "Yeni kurs əlavə edildi", "course": new_course}

# Bütün kursları gətirmək üçün endpoint
@router.get("/")
def list_courses(db: Session = Depends(get_db)):
    courses = db.query(Course).all()
    return courses

# Kursu ID ilə gətirmək üçün endpoint
@router.get("/{course_id}")
def get_course(course_id: int, db: Session = Depends(get_db)):
    course = db.query(Course).filter(Course.id == course_id).first()
    if course is None:
        raise HTTPException(status_code=404, detail="Kurs tapılmadı")
    return course

# Mövcud kursu yeniləmək üçün endpoint
@router.put("/{course_id}")
def update_course(course_id: int, updated_course: CourseUpdate, db: Session = Depends(get_db)):
    course = db.query(Course).filter(Course.id == course_id).first()
    if not course:
        raise HTTPException(status_code=404, detail="Kurs tapılmadı")

    course.name = updated_course.name
    course.description = updated_course.description
    db.commit()
    db.refresh(course)
    return {"message": "Kurs yeniləndi", "course": course}

# Kursu silmək üçün endpoint
@router.delete("/{course_id}")
def delete_course(course_id: int, db: Session = Depends(get_db)):
    course = db.query(Course).filter(Course.id == course_id).first()
    if not course:
        raise HTTPException(status_code=404, detail="Kurs tapılmadı")
    db.delete(course)
    db.commit()
    return {"message": "Kurs silindi"}
