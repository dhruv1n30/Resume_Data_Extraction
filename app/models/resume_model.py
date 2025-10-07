from pydantic import HttpUrl, EmailStr, BaseModel


class EducationItem(BaseModel):
    degree: str
    institution: str
    field_of_study: str | None
    year: str | None


class ExperienceItem(BaseModel):
    title: str
    company: str
    start_date: str
    end_date: str | None
    is_current: bool | None
    description: str | None


class ResumeExtractionResponse(BaseModel):
    name: str
    email: EmailStr | None
    phone: str | None
    summary: str | None
    links: list[HttpUrl]
    education: list[EducationItem]
    experience: list[ExperienceItem]
    skills: list[str]
