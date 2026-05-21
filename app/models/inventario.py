import enum

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from app.core.database import Base




class inventario(Base):
    __tablename__ = "inventarios"
    id_inventario: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[list[str]] = mapped_column(String(100))
    id_producto: Mapped[int] = mapped_column(foreign_key="productos.id_producto", autoincrement=True)
    id_filtro: Mapped[int] = mapped_column(foreign_key="filtros.id_filtro", autoincrement=True)
    log_inventario: Mapped[str] = mapped_column(String(255))
