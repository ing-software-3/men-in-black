import enum

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from app.core.database import Base




class venta(Base):
    __tablename__ = "ventas"
    id_venta: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    id_producto: Mapped[int] = mapped_column(foreign_key="productos.id_producto", autoincrement=True)
    id_usuario: Mapped[int] = mapped_column(foreign_key="filtros.id_filtro", autoincrement=True)
    id_cliente: Mapped[int] = mapped_column(foreign_key="filtros.id_filtro", autoincrement=True)
    fecha: Mapped[str] = mapped_column(String(255))