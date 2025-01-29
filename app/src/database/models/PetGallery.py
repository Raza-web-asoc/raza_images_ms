from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from app.src.database.base_class import Base
from sqlalchemy.sql import func

class PetGallery(Base):
    __tablename__ = "PetGallery"

    idImage = Column(Integer, primary_key=True, index=True, autoincrement=True)
    idPet = Column(Integer, primary_key=True, nullable=False)
    url = Column(String(255), nullable=False)
    uploadDate = Column(DateTime, default=func.now())