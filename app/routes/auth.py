from datetime import datetime, timedelta, timezone

from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from jose import jwt
from passlib.context import CryptContext
from sqlalchemy.orm import Session

from app.core.config import settings
from app.core.deps import get_db
from app.models.user import User, UserRole
from app.schemas.user import Token, UserCreate, UserResponse

router = APIRouter()

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)


def create_access_token(data: dict, expires_delta: timedelta | None = None) -> str:
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + (
        expires_delta or timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    )
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)


@router.post("/auth/login", response_model=Token, tags=["auth"])
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db),
):
    user = db.query(User).filter(User.email == form_data.username).first()

    if not user or not verify_password(form_data.password, user.password):
        raise HTTPException(status_code=401, detail="Credenciales incorrectas")

    access_token = create_access_token(data={"sub": str(user.id), "role": user.role})

    return Token(access_token=access_token, token_type="bearer")


@router.post("/auth/register", response_model=UserResponse, tags=["auth"])
def register(
    user: UserCreate,
    db: Session = Depends(get_db),
):
    if not settings.PUBLIC_REGISTRATION:
        raise HTTPException(
            status_code=403,
            detail="Registro público deshabilitado. Contacta al administrador.",
        )

    existing = db.query(User).filter(User.email == user.email).first()
    if existing:
        raise HTTPException(status_code=400, detail="El email ya está registrado")

    user_count = db.query(User).count()
    role = UserRole.admin if user_count == 0 else UserRole(settings.FIRST_USER_ROLE)

    db_user = User(
        name=user.name,
        email=user.email,
        password=get_password_hash(user.password),
        role=role,
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return db_user
