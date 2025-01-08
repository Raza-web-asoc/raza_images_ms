from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from app.src.database.base_class import Base

class UserImage(Base):
    __tablename__ = 'UserImage'
    
    idUser = Column(Integer, primary_key=True, autoincrement=True)
    url = Column(String(255), nullable=False)
    uploadDate = Column(DateTime, default=func.now())
