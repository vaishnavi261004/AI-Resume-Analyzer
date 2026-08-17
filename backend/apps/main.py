
from fastapi import FastAPI
from sqlalchemy import text
from apps.database.database import engine, Base
from apps.api.auth import router as auth_router
from apps.models.user import User
from apps.api.resume import router as resume_router
from apps.api.history import router as history_router

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="AI Resume Analyzer",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:5500"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(auth_router)
app.include_router(resume_router)
app.include_router(history_router)
@app.get("/")
def root():
    return {"message":  "AI Resume Analyzer"}

@app.get("/db-test")
def db_test():
    with engine.connect() as connection:
        result = connection.execute(text("SELECT 1"))
        return {"database": "Connected", "result" : result.scalar()}