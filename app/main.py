import uvicorn
from fastapi import FastAPI
from app.api.v1 import extract, flashcard, auth, translate
from app.core.config import settings

app = FastAPI(
    title="Flashcard AI Backend",
    description="Backend API for AI-powered flashcard generation",
    version="1.0.0"
)


# Include routers
# app.include_router(auth.router, prefix="/api/v1", tags=["auth"])
# app.include_router(flashcard.router, prefix="/api/v1", tags=["flashcard"])
app.include_router(extract.router, prefix="/api/v1", tags=["extract"])
app.include_router(translate.router, prefix="/api/v1", tags=["translate"])


@app.get("/")
async def root():
    return {"message": "Flashcard AI Backend API"}

if __name__ == "__main__":
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
