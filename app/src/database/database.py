from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from app.src.database.base_class import Base

from dotenv import load_dotenv
import os

load_dotenv()

DB_PORT = os.getenv("DB_PORT")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_HOST = os.getenv("DB_HOST")
URL_DATABASE  = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

engine = create_engine(URL_DATABASE)

SessionLocal = sessionmaker(autocommit=False, autoflush=False,bind=engine)

def init_db():
    try:
        engine.connect()
        print("Conectado a la Base de Datos")
    except Exception as error:
        print(f"Error al conectar a la base de datos: {error}")
        
    Base.metadata.create_all(bind=engine)



