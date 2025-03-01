from fastapi import FastAPI, Depends
from app.src.routes import users_router
from app.src.routes import pets_router
from app.src.database.database import init_db
from fastapi.middleware.cors import CORSMiddleware
from prometheus_fastapi_instrumentator import Instrumentator


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Orígenes permitidos
    allow_credentials=True,                  # Permitir cookies/autenticación
    allow_methods=[""],                     # Permitir todos los métodos HTTP
    allow_headers=[""],                     # Permitir todos los encabezados
)

instrumentator = Instrumentator(should_group_status_codes=False).instrument(app)
instrumentator.expose(app, endpoint="/metrics")
init_db()


app.include_router(users_router)
app.include_router(pets_router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Images API"}



