from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


from dotenv import load_dotenv
import os

load_dotenv()

DB_PORT = os.getenv("DB_PORT")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
URL_DATABASE  = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@host.docker.internal:{DB_PORT}/{DB_NAME}"



engine = create_engine(URL_DATABASE)

SessionLocal = sessionmaker(autocommit=False, autoflush=False,bind=engine)
Base = declarative_base()

Base.metadata.create_all(bind=engine)



