import enum

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from app.core.database import Base



class filtro(Base):
    __tablename__ = "filtros"

    id_filtro: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    categoria: Mapped[str] = mapped_column(String(100))
    talla: Mapped[float] = mapped_column()
    color: Mapped[str] = mapped_column(String(50))
    