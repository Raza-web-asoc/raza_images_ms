from pydantic import BaseModel

class UserBase(BaseModel):
    nombre_usuario: str
    nombres: str
    apellidos: str
    correo: str
    password_hash: str
    fecha_nacimiento: str
    sexo: str
    rol: int