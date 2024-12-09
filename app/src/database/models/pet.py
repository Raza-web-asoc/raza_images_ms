from sqlalchemy import Column, DateTime, Enum, ForeignKey, Integer, String, Date
from app.src.database.database import Base
from datetime import datetime

class Mascota(Base):
    __tablename__ = "mascotas"

    id_mascota = Column(Integer, primary_key=True, autoincrement=True)
    nombre_mascota = Column(String(100), nullable=False, comment="Nombre de la mascota")
    id_especie = Column(Integer, ForeignKey("especie.id_especie", ondelete="CASCADE", onupdate="CASCADE"), nullable=False)
    id_raza = Column(Integer, ForeignKey("raza.id_raza", ondelete="CASCADE", onupdate="CASCADE"), nullable=False)
    sexo = Column(Enum("M", "F", name="sexo_mascota_enum"), nullable=False, comment="Género de la mascota")
    fecha_nacimiento = Column(Date, nullable=False, comment="Fecha de nacimiento de la mascota")
    id_usuario = Column(Integer, ForeignKey("usuarios.id_usuario", ondelete="CASCADE", onupdate="CASCADE"), nullable=False)
    fecha_registro = Column(DateTime, default=datetime.utcnow, comment="Fecha de registro de la mascota")

    def __repr__(self):
        return f"<Mascota(nombre_mascota='{self.nombre_mascota}', id_usuario={self.id_usuario})>"
