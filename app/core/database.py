from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker
from app.core.config import settings

engine = create_engine(
    str(settings.DATABASE_URL),
    echo=True,
    pool_pre_ping=True,
    pool_size=5,
    max_overflow=10,
)


SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


class Base(DeclarativeBase):
    pass
