from fastapi import FastAPI, Depends
from app.src.routes import users_router
from app.src.routes import pets_router
from app.src.database.database import init_db
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Orígenes permitidos
    allow_credentials=True,                  # Permitir cookies/autenticación
    allow_methods=[""],                     # Permitir todos los métodos HTTP
    allow_headers=[""],                     # Permitir todos los encabezados
)

init_db()


app.include_router(users_router)
app.include_router(pets_router)




