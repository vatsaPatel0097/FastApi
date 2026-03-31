from .. import models, schemas
from sqlalchemy.orm import session
from fastapi import HTTPException, status
from ..hashing import hash_password


def create(request: schemas.User, db: session):
    user_data = request.model_dump()
    user_data["password"] = hash_password(user_data["password"])
    new_user = models.User(**user_data)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def user_by_id(id, db: session):
    user = db.query(models.User).filter_by(id=id).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"User with {id} not found"
        )
    return user


def delete(id, db: session):
    db.query(models.User).filter_by(id=id).delete(synchronize_session=False)
    db.commit()
    return "User Deleted"
