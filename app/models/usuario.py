from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from app.core.database import Base



class Usuario(Base):
    __tablename__ = "usuarios"

    id_usuario: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    nombre: Mapped[str] = mapped_column(String(100))
    apellido: Mapped[str] = mapped_column(String(100))
    cargo: Mapped[str] = mapped_column(String(50))
