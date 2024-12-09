from fastapi import FastAPI, Depends, HTTPException, status
from app.src.routes import users_router, dogs_router, posts_router
from typing import Annotated
from sqlalchemy.orm import Session
from app.src.database.database import SessionLocal

from app.src.models.user import UserBase
from app.src.database.models.user import User as User

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

app = FastAPI()
db_dependency = Annotated[Session, Depends(get_db)]


app.include_router(dogs_router)
app.include_router(users_router)
app.include_router(posts_router)

@app.post("/users",status_code=status.HTTP_201_CREATED)
async def create_user(user: UserBase, db: db_dependency):
    print(user)
    db_user = User(**user.dict())
    db.add(db_user)
    db.commit()
