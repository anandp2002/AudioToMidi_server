from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.config import settings
from app.api.v1.endpoints import transcribe

app = FastAPI(title=settings.PROJECT_NAME)

# Set all CORS enabled origins
if settings.BACKEND_CORS_ORIGINS:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.BACKEND_CORS_ORIGINS,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
        expose_headers=["X-Conversion-Time"],
    )

app.include_router(transcribe.router, prefix=settings.API_V1_STR, tags=["transcription"])

@app.get("/")
def read_root():
    return {"message": "Welcome to the MP3 to MIDI Converter API"}
