from sqlalchemy import  Column, Integer
from app.src.database.database import Base
import enum
from datetime import datetime

class PetPhotos(Base):
    __tablename__ = "PetPhotos"

    idPet = Column(Integer, primary_key=True, index=True)
    quantityOfPhotos = Column(Integer, default=0)

