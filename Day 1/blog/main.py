from fastapi import FastAPI
from . import models
from .database import engine
from .router import blog, user

app = FastAPI()

models.Base.metadata.create_all(engine)

app.include_router(blog.router)
app.include_router(user.router)


# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()


# @app.post(
#     "/blog",
#     status_code=status.HTTP_201_CREATED,
#     response_model=schemas.ShowBlog,
#     tags=["blogs"],
# )
# def create_blog(request: schemas.Blog, db: Session = Depends(get_db)):
#     new_blog = models.Blog(title=request.title, body=request.body, user_id=1)
#     db.add(new_blog)
#     db.commit()
#     db.refresh(new_blog)
#     return new_blog


# @app.delete("/blog/{id}", status_code=status.HTTP_204_NO_CONTENT, tags=["blogs"])
# def delete_blog(id, db: Session = Depends(get_db)):
#     db.query(models.Blog).filter_by(id=id).delete(synchronize_session=False)
#     db.commit()
#     return {"message": "Blog deleted successfully"}


# @app.put(
#     "/blog/{id}",
#     status_code=status.HTTP_202_ACCEPTED,
#     response_model=schemas.ShowBlog,
#     tags=["blogs"],
# )
# def update_blog(id, request: schemas.Blog, db: Session = Depends(get_db)):
#     blog = db.query(models.Blog).filter_by(id=id).first()
#     if not blog:
#         raise HTTPException(status_code=404, detail="Blog not found")

#     for key, value in request.dict().items():
#         setattr(blog, key, value)

#     db.commit()
#     db.refresh(blog)

#     return blog


# @app.get("/blog", response_model=List[schemas.ShowBlog], tags=["blogs"])
# def get_blogs(db: Session = Depends(get_db)):
#     blogs = db.query(models.Blog).all()
#     return blogs


# @app.get("/blog/{id}", status_code=200, response_model=schemas.ShowBlog, tags=["blogs"])
# def get_blog_by_id(id, response: Response, db: Session = Depends(get_db)):
#     # blog = db.query(models.Blog).filter(models.Blog.id == id).first()
#     blog = db.query(models.Blog).filter_by(id=id).first()
#     if not blog:
#         raise HTTPException(
#             status_code=status.HTTP_404_NOT_FOUND,
#             detail=f"The blog with {id} is not availabe",
#         )
#         # response.status_code = status.HTTP_404_NOT_FOUND
#         # return {"detail": f"The blog with {id} is not availabe"}
#     return blog


# @app.post("/users", response_model=schemas.ShowUser, tags=["users"])
# def create_user(request: schemas.User, db: Session = Depends(get_db)):
#     user_data = request.model_dump()
#     user_data["password"] = hash_password(user_data["password"])
#     new_user = models.User(**user_data)
#     db.add(new_user)
#     db.commit()
#     db.refresh(new_user)
#     return new_user


# @app.get("/user/{id}", response_model=schemas.ShowUser, tags=["users"])
# def get_users_by_id(id, db: Session = Depends(get_db)):
#     user = db.query(models.User).filter_by(id=id).first()
#     if not user:
#         raise HTTPException(
#             status_code=status.HTTP_404_NOT_FOUND, detail=f"User with {id} not found"
#         )
#     return user


# @app.delete("/user/{id}", status_code=status.HTTP_204_NO_CONTENT)
# def delete_user(id, db: Session = Depends(get_db)):
#     db.query(models.User).filter_by(id=id).delete(synchronize_session=False)
#     db.commit()
#     return "User Deleted"
