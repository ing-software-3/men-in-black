from typing import Optional
from pydantic import BaseModel


class FiltroBase(BaseModel):
    categoria: str
    talla: float
    color: str


class FiltroCreate(FiltroBase):
    """Schema para crear un filtro"""
    pass


class FiltroUpdate(BaseModel):
    """Schema para actualizar un filtro"""
    categoria: Optional[str] = None
    talla: Optional[float] = None
    color: Optional[str] = None


class FiltroResponse(FiltroBase):
    """Schema para responder con datos de filtro"""
    id_filtro: int

    class Config:
        from_attributes = True
