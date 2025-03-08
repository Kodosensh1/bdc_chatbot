import os
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqladmin import Admin, ModelView
from app.database import create_tables, engine
from app.models import Course, User
from app.api.courses import router as courses_router
from app.api.chatbot import router as chatbot_router
from app.api.users import router as users_router  # Əgər istifadəçi API-niz varsa
from app.api.chatbot import router as chatbot_router  # Chat API-ni əlavə edirik
  # Chat API-ni əlavə edirik

# .env faylını yükləyirik
load_dotenv()

# Verilənlər bazasında cədvəlləri yaradırıq (əgər hələ yaradılmayıbsa)
create_tables()

# FastAPI tətbiqi
app = FastAPI()

# CORS konfiqurasiyası
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Sağlamlıq yoxlaması endpointi
@app.get("/")
def health_check():
    return {"message": "BDC Chatbot API is running!"}

# **Bütün API-ları daxil edirik**
app.include_router(courses_router)   # /courses API-ları
app.include_router(chatbot_router)   # /chat API-ları
app.include_router(users_router)     # /users API-ları (əgər varsa)
app.include_router(chatbot_router)      # /chat API-ları (yeni əlavə edildi)

# **SQLAdmin admin panelini qururuq və base_url-i "/admin" olaraq təyin edirik**
admin = Admin(app, engine, base_url="/admin")

# **Admin panelində Course modeli üçün görünüş**
class CourseAdmin(ModelView, model=Course):
    column_list = [Course.id, Course.name, Course.description]
    include_in_schema = True  # Docs-da görünəcək

# **Admin panelində User modeli üçün görünüş (əgər varsa)**
class UserAdmin(ModelView, model=User):
    column_list = [User.id, User.username, User.email]
    include_in_schema = True  # Docs-da görünəcək

admin.add_view(CourseAdmin)
admin.add_view(UserAdmin)

# **Serveri işə salırıq**
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000, reload=True)
