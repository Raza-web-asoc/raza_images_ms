from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from app.src.database.database import Base
from datetime import datetime

class Foto(Base):
    __tablename__ = "fotos"

    id_foto = Column(Integer, primary_key=True, autoincrement=True)
    url = Column(String(255), nullable=False, comment="URL de la foto")
    id_mascota = Column(Integer, ForeignKey("mascotas.id_mascota", ondelete="CASCADE", onupdate="CASCADE"), nullable=True)
    fecha_subida = Column(DateTime, default=datetime.utcnow, comment="Fecha de subida de la foto")

  
