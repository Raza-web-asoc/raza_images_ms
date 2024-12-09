from sqlalchemy import Column, DateTime, Enum, ForeignKey, Integer
from app.src.database.database import Base
from datetime import datetime

class Match(Base):
    __tablename__ = "matches"

    id_match = Column(Integer, primary_key=True, autoincrement=True)
    id_mascota1 = Column(Integer, ForeignKey("mascotas.id_mascota", ondelete="CASCADE", onupdate="CASCADE"), nullable=False)
    id_mascota2 = Column(Integer, ForeignKey("mascotas.id_mascota", ondelete="CASCADE", onupdate="CASCADE"), nullable=False)
    fecha_inicio = Column(DateTime, default=datetime.utcnow, comment="Fecha en que se inició el match")
    estado = Column(Enum("pendiente", "aceptado", "rechazado", name="estado_match_enum"), default="pendiente", comment="Estado del match")
