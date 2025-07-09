from fastapi import APIRouter
from pydantic import BaseModel
from app.services.nlp.translate import translate_en_to_vi

router = APIRouter(prefix="/translate", tags=["translate"])

class TranslateRequest(BaseModel):
    text: str

class TranslateResponse(BaseModel):
    translated: str

@router.post("/en_to_vi", response_model=TranslateResponse)
def translate_text_en_to_vi(payload: TranslateRequest):
    en_text = payload.text.strip()
    vi_text = translate_en_to_vi(en_text)
    return {"translated": vi_text}
