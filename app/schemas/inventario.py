from typing import Optional
from pydantic import BaseModel


class InventarioBase(BaseModel):
    name: list[str]
    id_producto: int
    id_filtro: int
    log_inventario: str


class InventarioCreate(InventarioBase):
    """Schema para crear un registro de inventario"""
    pass


class InventarioUpdate(BaseModel):
    """Schema para actualizar un registro de inventario"""
    name: Optional[list[str]] = None
    id_producto: Optional[int] = None
    id_filtro: Optional[int] = None
    log_inventario: Optional[str] = None


class InventarioResponse(InventarioBase):
    """Schema para responder con datos de inventario"""
    class Config:
        from_attributes = True
