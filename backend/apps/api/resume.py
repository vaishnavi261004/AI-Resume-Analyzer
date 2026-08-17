
from fastapi import APIRouter, UploadFile, File
import shutil
import os
from fastapi import Form
from fastapi.responses import JSONResponse
from apps.schemas.analysis import ResumeAnalysisRequest
from apps.services.ai.groq_service import analyze_resume

from apps.services.resume.parser import extract_text

from sqlalchemy.orm import Session
from fastapi import Depends

from apps.database.database import get_db
from apps.services.auth.dependencies import get_current_user
from apps.services.analysis.analysis_services import save_analysis
from apps.models.analysis import Analysis 
from apps.services.auth.dependencies import get_current_user  

router = APIRouter(
    prefix="/resume",
    tags=["Resume"]
)

UPLOAD_FOLDER = "apps/uploads"


@router.post("/upload")
async def upload_resume(file: UploadFile = File(...)):

    os.makedirs(UPLOAD_FOLDER, exist_ok=True)

    file_path = os.path.join(
        UPLOAD_FOLDER,
        file.filename
    )

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    resume_text = extract_text(file_path)

    return {
        "filename": file.filename,
        "text": resume_text
    }
@router.post("/analyze")
async def analyze(
    file: UploadFile = File(...),
    job_description: str = Form(...),
    db: Session = Depends(get_db),
    current_user: int = Depends(get_current_user)
):

    os.makedirs(UPLOAD_FOLDER, exist_ok=True)

    file_path = os.path.join(
        UPLOAD_FOLDER,
        file.filename
    )

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    resume_text = extract_text(file_path)

    result = analyze_resume(
        resume_text,
        job_description
    )

    analysis = Analysis(
    user_id=current_user,
    resume_name=file.filename,
    job_description=job_description,
    match_score=result["match_score"],
    strengths="\n".join(result["strengths"]),
    missing_skills="\n".join(result["missing_skills"]),
    suggestions="\n".join(result["suggestions"])
)

    db.add(analysis)
    db.commit()
    save_analysis(
        db=db,
        user_id=current_user,
        resume_name=file.filename,
        job_description=job_description,
        ai_result=result
    )
    print(result)
    # return result
    return JSONResponse(content=result)