
from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime
from datetime import datetime
from sqlalchemy.sql import func


from apps.database.database import Base


class Analysis(Base):

    __tablename__ = "analysis"

    id = Column(Integer, primary_key=True, index=True)

    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    resume_name = Column(String(255), nullable=False)

    job_description = Column(Text, nullable=False)

    match_score = Column(Integer, nullable=False)

    strengths = Column(Text, nullable=False)

    missing_skills = Column(Text, nullable=False)

    suggestions = Column(Text, nullable=True)

    created_at = Column(DateTime(timezone=True), server_default=func.now())