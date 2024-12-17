from sqlalchemy import Column, DateTime, Integer, String
from app.src.database.database import Base

class UserImage(Base):
    __tablename__ = "UserImage"

    idUser = Column(Integer, primary_key=True, index=True)
    url = Column(String(255), nullable=False)
    uploadDate = Column(DateTime, server_default="CURRENT_TIMESTAMP")