from sqlalchemy import Column, Integer, String
from app.src.database.database import Base

class Especie(Base):
    __tablename__ = "especie"

    id_especie = Column(Integer, primary_key=True, autoincrement=True)
    nombre_especie = Column(String(100), nullable=False, unique=True, comment="Nombre de la especie (e.g., perro, gato, ave)")
