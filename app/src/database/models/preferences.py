from sqlalchemy import Column, Enum, ForeignKey, Integer
from app.src.database.database import Base

class Preferencia(Base):
    __tablename__ = "preferencias"

    id_preferencia = Column(Integer, primary_key=True, autoincrement=True)
    id_usuario = Column(Integer, ForeignKey("usuarios.id_usuario", ondelete="CASCADE", onupdate="CASCADE"), nullable=False)
    id_especie = Column(Integer, ForeignKey("especie.id_especie", ondelete="CASCADE", onupdate="CASCADE"), nullable=True)
    id_raza = Column(Integer, ForeignKey("raza.id_raza", ondelete="CASCADE", onupdate="CASCADE"), nullable=True)
    sexo_mascota = Column(Enum("M", "F", name="sexo_preferencia_enum"), nullable=True)
    rango_edad_min = Column(Integer, nullable=True, comment="Edad mínima preferida de la mascota")
    rango_edad_max = Column(Integer, nullable=True, comment="Edad máxima preferida de la mascota")

    def __repr__(self):
        return f"<Preferencia(id_usuario={self.id_usuario}, id_especie={self.id_especie}, sexo_mascota='{self.sexo_mascota}')>"
