from typing import Optional
from pydantic import BaseModel, ConfigDict


class ProductBase(BaseModel):
    nombre: str
    precio: float
    categoria: str
    stock: int
    descripcion: Optional[str] = None


class ProductCreate(ProductBase):
    """Schema para crear un producto"""
    pass


class ProductUpdate(BaseModel):
    """Schema para actualizar un producto"""
    nombre: Optional[str] = None
    precio: Optional[float] = None
    categoria: Optional[str] = None
    stock: Optional[int] = None
    descripcion: Optional[str] = None


class ProductResponse(ProductBase):
    model_config = ConfigDict(from_attributes=True)