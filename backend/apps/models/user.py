
from sqlalchemy import Column, Integer, String
from apps.database.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(100), unique=True, nullable=False)
    name = Column(String(150), unique=True, nullable=False)
    password = Column(String(200), nullable=False)