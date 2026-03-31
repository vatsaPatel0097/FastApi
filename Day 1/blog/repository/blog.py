from .. import models, schemas
from sqlalchemy.orm import session
from fastapi import HTTPException, status


def create(request: schemas.Blog, db: session):
    new_blog = models.Blog(title=request.title, body=request.body, user_id=1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


def get_all(db: session):
    blogs = db.query(models.Blog).all()
    return blogs


def delete(db: session, id):
    db.query(models.Blog).filter_by(id=id).delete(synchronize_session=False)
    db.commit()
    return {"message": "Blog deleted successfully"}


def update(db: session, request: schemas.ShowBlog, id):
    blog = db.query(models.Blog).filter_by(id=id).first()
    if not blog:
        raise HTTPException(status_code=404, detail="Blog not found")

    for key, value in request.dict().items():
        setattr(blog, key, value)

    db.commit()
    db.refresh(blog)

    return blog


def blog_by_id(db: session, id):
    # blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    blog = db.query(models.Blog).filter_by(id=id).first()
    if not blog:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"The blog with {id} is not availabe",
        )
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {"detail": f"The blog with {id} is not availabe"}
    return blog
