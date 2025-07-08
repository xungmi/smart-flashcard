from fastapi import APIRouter
from app.services.nlp import translate_en_to_vi

router = APIRouter(prefix="/v1/translate", tags=["translate"])

@router.post("/en_to_vi")
def translate_text_en_to_vi(payload: dict):
    en_text = payload.get("text", "")
    vi_text = translate_en_to_vi(en_text)
    return {"translated": vi_text}


from fastapi import APIRouter
from pydantic import BaseModel
from app.services.nlp import translate_en_to_vi

router = APIRouter(prefix="/v1/translate", tags=["translate"])

class TranslateRequest(BaseModel):
    text: str

class TranslateResponse(BaseModel):
    translated: str

@router.post("/en_to_vi", response_model=TranslateResponse)
def translate_text_en_to_vi(payload: TranslateRequest):
    en_text = payload.text.strip()
    vi_text = translate_en_to_vi(en_text)
    return {"translated": vi_text}
