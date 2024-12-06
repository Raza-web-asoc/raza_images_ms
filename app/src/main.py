from fastapi import FastAPI
from app.src.routes import users_router, dogs_router, posts_router

app = FastAPI()

app.include_router(dogs_router)
app.include_router(users_router)
app.include_router(posts_router)
