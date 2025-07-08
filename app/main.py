from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.v1 import extract, flashcard, auth
from app.core.config import settings

app = FastAPI(
    title="Flashcard AI Backend",
    description="Backend API for AI-powered flashcard generation",
    version="1.0.0"
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(auth.router, prefix="/api/v1", tags=["auth"])
# app.include_router(flashcard.router, prefix="/api/v1", tags=["flashcard"])
# app.include_router(extract.router, prefix="/api/v1", tags=["extract"])


@app.get("/")
async def root():
    return {"message": "Flashcard AI Backend API"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000) 
