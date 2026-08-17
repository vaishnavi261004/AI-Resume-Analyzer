
import json

from sqlalchemy.orm import Session

from apps.models.analysis import Analysis


def save_analysis(
    db: Session,
    user_id: int,
    resume_name: str,
    job_description: str,
    ai_result: dict
):

    analysis = Analysis(
        user_id=user_id,
        resume_name=resume_name,
        job_description=job_description,
        match_score=ai_result.get("match_score"),

        strengths=json.dumps(
            ai_result.get("strengths", [])
        ),

        missing_skills=json.dumps(
            ai_result.get("missing_skills", [])
        ),

        suggestions=json.dumps(
            ai_result.get("suggestions", [])
        )
    )

    db.add(analysis)
    db.commit()
    db.refresh(analysis)

    return analysis