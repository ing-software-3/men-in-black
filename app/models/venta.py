import enum

from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from app.core.database import Base




class venta(Base):
    __tablename__ = "ventas"
    id_venta: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    id_producto: Mapped[int] = mapped_column(ForeignKey("productos.id_producto"), autoincrement=True)
    id_usuario: Mapped[int] = mapped_column(ForeignKey("usuarios.id_usuario"), autoincrement=True)
    id_cliente: Mapped[int] = mapped_column(ForeignKey("clientes.id_cliente"), autoincrement=True)
    fecha: Mapped[str] = mapped_column(String(255))