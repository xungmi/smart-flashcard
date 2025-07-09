from fastapi import APIRouter
from pydantic import BaseModel
from app.services.nlp.example_gen import create_example_sentence

router = APIRouter(prefix="/nlp", tags=["example_gen"])

class ExampleRequest(BaseModel):
    word: str

class ExampleResponse(BaseModel):
    sentence: str

@router.post("/example", response_model=ExampleResponse)
async def generate_example(req: ExampleRequest):
    sentence = create_example_sentence(req.word)
    return {"sentence": sentence}
