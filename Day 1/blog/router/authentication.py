from fastapi import APIRouter, Depends, HTTPException, status
from .. import schemas, database, models, hashing, token
from sqlalchemy.orm import session


router = APIRouter()


@router.post("/login")
def login(request: schemas.Login, db: session = Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.email == request.username).first()
    if not user:
        raise HTTPException(status_code=404, detail="Invalid User")

    if not hashing.verify(user.password, request.password):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Incorrect password"
        )

    access_token = token.create_access_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}
