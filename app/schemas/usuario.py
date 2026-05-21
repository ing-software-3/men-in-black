from typing import Optional
from pydantic import BaseModel


class UsuarioBase(BaseModel):
    nombre: str
    apellido: str
    cargo: str


class UsuarioCreate(UsuarioBase):
    """Schema para crear un usuario"""
    pass


class UsuarioUpdate(BaseModel):
    """Schema para actualizar un usuario"""
    nombre: Optional[str] = None
    apellido: Optional[str] = None
    cargo: Optional[str] = None


class UsuarioResponse(UsuarioBase):
    """Schema para responder con datos de usuario"""
    id_usuario: int

    class Config:
        from_attributes = True
