from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from ..schemas import user_schemas
from ..services import user_service
from ..dependencies import get_db
from ..auth import get_current_active_user

router = APIRouter(
    prefix="/users",
    tags=["users"],
)

@router.post("/", response_model=user_schemas.UserOut, status_code=status.HTTP_201_CREATED)
def create_user(user: user_schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = user_service.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return user_service.create_user(db, user)

@router.get("/", response_model=List[user_schemas.UserOut])
def list_users(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return user_service.get_users(db, skip=skip, limit=limit)

@router.get("/me", response_model=user_schemas.UserOut)
def read_current_user(current_user: user_schemas.User = Depends(get_current_active_user)):
    return current_user

@router.get("/{user_id}", response_model=user_schemas.UserOut)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = user_service.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user(user_id: int, db: Session = Depends(get_db)):
    return user_service.delete_user(db, user_id=user_id)

