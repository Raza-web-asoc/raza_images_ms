from sqlalchemy import Column, ForeignKey, Integer, String, Text
from app.src.database.database import Base

class Raza(Base):
    __tablename__ = "raza"

    id_raza = Column(Integer, primary_key=True, autoincrement=True)
    nombre_raza = Column(String(100), nullable=False, comment="Nombre de la raza de la mascota")
    id_especie = Column(Integer, ForeignKey("especie.id_especie", ondelete="CASCADE", onupdate="CASCADE"), nullable=False)
    historia = Column(Text, nullable=True, comment="Historia o descripción de la raza")


