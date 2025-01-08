from fastapi import FastAPI, Depends
from app.src.routes import users_router
from app.src.routes import pets_router
from app.src.database.database import init_db


app = FastAPI()

init_db()

app.include_router(users_router)
app.include_router(pets_router)




