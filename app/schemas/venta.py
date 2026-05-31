from typing import Optional
from pydantic import BaseModel, ConfigDict


class VentaBase(BaseModel):
    id_producto: int
    id_usuario: int
    id_cliente: int
    fecha: str


class VentaCreate(VentaBase):
    """Schema para crear una venta"""
    pass


class VentaUpdate(BaseModel):
    """Schema para actualizar una venta"""
    id_producto: Optional[int] = None
    id_usuario: Optional[int] = None
    id_cliente: Optional[int] = None
    fecha: Optional[str] = None


class VentaResponse(VentaBase):
    model_config = ConfigDict(from_attributes=True)