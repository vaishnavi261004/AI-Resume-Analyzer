
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from apps.database.database import get_db
from apps.models.analysis import Analysis
from apps.services.auth.dependencies import get_current_user

router = APIRouter(
    prefix="/history",
    tags=["History"]
)


@router.get("/")
def get_history(
    db: Session = Depends(get_db),
    current_user: int = Depends(get_current_user)
):

    history = (
        db.query(Analysis)
        .filter(Analysis.user_id == current_user)
        .order_by(Analysis.created_at.desc())
        .all()
    )

    return history