from fastapi import APIRouter
from fastapi import Depends, status, HTTPException
from .. import schemas, models
from ..database import get_db
from sqlalchemy.orm import Session
from ..repository import user

router = APIRouter(prefix="/user", tags=["users"])


@router.post("/", response_model=schemas.ShowUser)
def create_user(request: schemas.User, db: Session = Depends(get_db)):
    return user.create(request, db)


@router.get("/{id}", response_model=schemas.ShowUser)
def get_users_by_id(id, db: Session = Depends(get_db)):
    return user.user_by_id(id, db)


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user(id, db: Session = Depends(get_db)):
    return user.delete(id, db)
