from fastapi import APIRouter
from app.nlp import get_response  # NLP funksiyasını import et
from pydantic import BaseModel

router = APIRouter()

# Pydantic model (Request body üçün)
class ChatRequest(BaseModel):
    message: str

# Chat endpointi
@router.post("/chat/")
def chat_endpoint(request: ChatRequest):
    response = get_response(request.message)
    return {"reply": response}
