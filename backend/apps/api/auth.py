
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from apps.database.database import get_db
from apps.models.user import User
from apps.schemas.user import UserCreate, UserResponse
from apps.services.auth.hash import hash_password, verify_password
from apps.schemas.user import UserLogin, Token
from apps.services.auth.jwt_handler import create_token

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)

@router.get("/")
def test():
    return {
        "message" : "Authentication route is working"
    }

@router.post("/register", response_model=UserResponse)
def register_user(user: UserCreate, db: Session = Depends(get_db)):
    # Check if the user already exists
    existing_user = db.query(User).filter(User.email == user.email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    # Hash the password before storing it
    hashed_password = hash_password(user.password)

    # Create a new user instance
    new_user = User(
        name=user.name,
        email=user.email,
        password=hashed_password
    )

    # Add the new user to the database
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user

@router.post("/login", response_model=Token)
def login_user(user: UserLogin, db: Session = Depends(get_db)):
    # Check if the user exists
    existing_user = db.query(User).filter(User.email == user.email).first()
    if not existing_user:
        raise HTTPException(status_code=400, detail="Invalid email or password")

    # Verify the password
    if not verify_password(user.password, existing_user.password):
        raise HTTPException(status_code=400, detail="Invalid email or password")

    # Create a JWT token
    access_token = create_token(existing_user.id)

    return {"access_token": access_token, "token_type": "bearer"}