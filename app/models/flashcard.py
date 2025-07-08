from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class FlashcardBase(BaseModel):
    """Base flashcard model with common fields"""
    question: str = Field(..., description="The question or front of the flashcard")
    answer: str = Field(..., description="The answer or back of the flashcard")
    category: Optional[str] = Field(default="general", description="Category of the flashcard")

class FlashcardCreate(FlashcardBase):
    """Model for creating a new flashcard"""
    pass

class FlashcardUpdate(BaseModel):
    """Model for updating a flashcard"""
    question: Optional[str] = Field(None, description="The question or front of the flashcard")
    answer: Optional[str] = Field(None, description="The answer or back of the flashcard")
    category: Optional[str] = Field(None, description="Category of the flashcard")

class Flashcard(FlashcardBase):
    """Complete flashcard model with all fields"""
    id: int = Field(..., description="Unique identifier for the flashcard")
    created_at: str = Field(..., description="Timestamp when the flashcard was created")
    
    class Config:
        json_schema_extra = {
            "example": {
                "id": 1,
                "question": "What is the capital of France?",
                "answer": "Paris",
                "category": "geography",
                "created_at": "2024-01-01T00:00:00Z"
            }
        }

class FlashcardResponse(BaseModel):
    """Response model for flashcard operations"""
    success: bool
    data: Optional[Flashcard] = None
    message: str
    error: Optional[str] = None

class FlashcardListResponse(BaseModel):
    """Response model for flashcard list operations"""
    success: bool
    data: list[Flashcard] = []
    total: int = 0
    skip: int = 0
    limit: int = 100
    message: str
    error: Optional[str] = None 