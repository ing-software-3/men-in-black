from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from app.core.database import Base



class Product(Base):
    __tablename__ = "productos"

    id_producto: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    nombre: Mapped[str] = mapped_column(String(100))
    precio: Mapped[float] = mapped_column()
    categoria: Mapped[str] = mapped_column(String(50))
    stock: Mapped[int] = mapped_column()
    descripcion: Mapped[str] = mapped_column(String(255))