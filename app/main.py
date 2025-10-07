from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.v1.endpoints import cv_extract

app = FastAPI(title="Resume Extractor API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

app.include_router(cv_extract.router, prefix="/api/v1/extract", tags=["genai"])


@app.get("/")
def read_root():
    return {"message": "Welcome to the Resume Extractor API"}
