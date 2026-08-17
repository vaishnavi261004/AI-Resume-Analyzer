
from pydantic import BaseModel
from datetime import datetime

from pydantic import BaseModel
from datetime import datetime


class AnalysisCreate(BaseModel):
    job_description: str


class AnalysisResponse(BaseModel):
    id: int
    resume_name: str
    match_score: int
    strengths: str
    missing_skills: str
    suggestions: str
    created_at: datetime

    class Config:
        from_attributes = True

class ResumeAnalysisRequest(BaseModel):
    job_description: str