from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from app.core.database import Base



class Cliente(Base):
    __tablename__ = "clientes"

    id_cliente: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    nombre: Mapped[str] = mapped_column(String(100))
    apellido: Mapped[str] = mapped_column(String(100))
    correo: Mapped[str] = mapped_column(String(100))
    celular: Mapped[int] = mapped_column(String(20))
    