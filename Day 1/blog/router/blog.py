from fastapi import APIRouter
from fastapi import Depends, status
from typing import List
from .. import schemas
from ..database import get_db
from sqlalchemy.orm import Session
from ..repository import blog

router = APIRouter(prefix="/blog", tags=["blogs"])


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.ShowBlog)
def create_blog(request: schemas.Blog, db: Session = Depends(get_db)):
    return blog.create(request, db)


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_blog(id: int, db: Session = Depends(get_db)):
    return blog.delete(db, id)


@router.put(
    "/{id}", status_code=status.HTTP_202_ACCEPTED, response_model=schemas.ShowBlog
)
def update_blog(id: int, request: schemas.Blog, db: Session = Depends(get_db)):
    return blog.update(db, request, id)


@router.get("/", response_model=List[schemas.ShowBlog])
def get_blogs(db: Session = Depends(get_db)):
    return blog.get_all(db)


@router.get("/{id}", status_code=200, response_model=schemas.ShowBlog)
def get_blog_by_id(id: int, db: Session = Depends(get_db)):
    return blog.blog_by_id(db, id)
