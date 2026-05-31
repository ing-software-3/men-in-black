from typing import Optional
from pydantic import BaseModel,ConfigDict


class ClienteBase(BaseModel):
    nombre: str
    apellido: str
    correo: str
    celular: int


class ClienteCreate(ClienteBase):
    """Schema para crear un cliente"""
    pass


class ClienteUpdate(BaseModel):
    """Schema para actualizar un cliente"""
    nombre: Optional[str] = None
    apellido: Optional[str] = None
    correo: Optional[str] = None
    celular: Optional[int] = None


class ClienteResponse(ClienteBase):
    model_config = ConfigDict(from_attributes=True)