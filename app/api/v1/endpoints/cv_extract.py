from fastapi import File, APIRouter, UploadFile, HTTPException

from app.services.llm import extract_resume_data
from app.models.resume_model import ResumeExtractionResponse

router = APIRouter()


@router.get("/check")
async def health_check():
    return {"message": "API is Healthy"}

@router.post("/resume", response_model=ResumeExtractionResponse)
async def extract_resume(file: UploadFile = File(...)):
    if not file.filename.endswith(".pdf"):
        raise HTTPException(status_code=400, detail="Only PDF files are allowed")

    try:
        contents = await file.read()
        extracted_data = extract_resume_data(contents)
        return extracted_data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e)) from e
