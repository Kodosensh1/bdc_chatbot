from fastapi import APIRouter

router = APIRouter(
    prefix="/users",
    tags=["users"]
)

@router.get("/")
def get_users():
    return {"message": "Bu, istifadəçilər üçün API endpointidir"}
