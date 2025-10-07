import base64

from io import BytesIO

from openai import OpenAI

from app.core.config import settings
from app.models.resume_model import ResumeExtractionResponse
from app.services.pdf_to_image import get_pdf_images

client = OpenAI(api_key=settings.GEMINI_API_KEY , base_url="https://generativelanguage.googleapis.com/v1beta/openai/")


def extract_resume_data(pdf_content: bytes) -> ResumeExtractionResponse:
    images = get_pdf_images(pdf_content)
    if not images:
        raise ValueError("No images could be extracted from the PDF")

    # Convert images to base64
    base64_images = []
    for img in images:
        buffered = BytesIO()
        img.save(buffered, format="JPEG")
        img_str = base64.b64encode(buffered.getvalue()).decode()
        base64_images.append(f"data:image/jpeg;base64,{img_str}")

    prompt = """
    Analyze the resume image(s) and extract the following information:
    - Name
    - Email
    - Phone
    - Education (list of degrees, institutions, and years)
    - Experience (list of jobs with titles, companies, dates, and descriptions)
    - Skills (list of skills)
    
    For education and experience, use arrays of objects. If information is missing, use null or empty arrays.
    """

    messages = [
        {
            "role": "system",
            "content": "You are a helpful assistant that extracts structured data from resume images using vision."
        },
        {
            "role": "user",
            "content": [
                {"type": "text", "text": prompt}
            ] + [{"type": "image_url", "image_url": {"url": img_b64}} for img_b64 in base64_images]
        }
    ]

    response = client.beta.chat.completions.parse   (
        model="gemini-2.5-pro",  # Vision-capable model
        messages=messages,
        response_format=ResumeExtractionResponse
    )

    extracted_json = response.choices[0].message.parsed

    return extracted_json
