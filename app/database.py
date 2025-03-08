from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

# .env faylını yükləmək
load_dotenv()

# DATABASE_URL-i .env faylından götürmək
DATABASE_URL = os.getenv("DATABASE_URL")

# SQLAlchemy engine yaratmaq
engine = create_engine(DATABASE_URL)

# Session yaratmaq
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# ORM modelləri üçün baza sinifi
Base = declarative_base()

# DB sessiyası üçün dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Verilənlər bazasında cədvəlləri yaratmaq üçün funksiya
def create_tables():
    from app.models import Course, User  # User modelinin əlavə olunduğuna əmin olun
    Base.metadata.create_all(bind=engine)

# Server işə düşəndə avtomatik cədvəlləri yarat
create_tables()
