from sqlalchemy import  Boolean, Column, DateTime, Enum, Integer, String, Date, ForeignKey
from app.src.database.database import Base
import enum
from datetime import datetime

class SexoEnum(enum.Enum):
    M = "M"
    F = "F"
    Otro = "Otro"

class User(Base):
    __tablename__ = "usuarios"

    id_usuario = Column(Integer, primary_key=True, autoincrement=True)
    nombre_usuario = Column(String(50), nullable=False, unique=True, comment="Nombre de usuario único")
    nombres = Column(String(100), nullable=False, comment="Nombres del usuario")
    apellidos = Column(String(100), nullable=False, comment="Apellidos del usuario")
    correo = Column(String(100), nullable=False, unique=True, comment="Correo único")
    password_hash = Column(String(255), nullable=False, comment="Contraseña encriptada")
    fecha_nacimiento = Column(Date, nullable=False, comment="Fecha de nacimiento del usuario")
    sexo = Column(Enum(SexoEnum), nullable=False, comment="Género del usuario")
    rol = Column(Integer, default=1, nullable=False, comment="Rol del usuario")
    fecha_creacion = Column(DateTime, default=datetime.utcnow, comment="Fecha de creación del usuario")

