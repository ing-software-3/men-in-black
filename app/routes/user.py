from fastapi import APIRouter, Depends, HTTPException, Response
from sqlalchemy.orm import Session
from starlette.status import HTTP_204_NO_CONTENT, HTTP_404_NOT_FOUND

from app.core.deps import get_current_user, get_db, require_admin
from app.models.user import User, UserRole
from app.routes.auth import get_password_hash
from app.schemas.user import UserCreate, UserResponse, UserUpdate

router = APIRouter()


@router.get("/users", response_model=list[UserResponse], tags=["users"])
def get_users(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return db.query(User).all()


@router.get("/users/{id}", response_model=UserResponse, tags=["users"])
def get_user(
    id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    user = db.query(User).filter(User.id == id).first()

    if not user:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="User not found")

    return user


@router.post("/users", response_model=UserResponse, tags=["users"])
def create_user(
    user: UserCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_admin),
):
    existing = db.query(User).filter(User.email == user.email).first()

    if existing:
        raise HTTPException(status_code=400, detail="El email ya está registrado")

    db_user = User(
        name=user.name,
        email=user.email,
        password=get_password_hash(user.password),
        role=user.role,
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return db_user


@router.put("/users/{id}", response_model=UserResponse, tags=["users"])
def update_user(
    id: int,
    user: UserUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    if current_user.role != UserRole.admin and current_user.id != id:
        raise HTTPException(
            status_code=403,
            detail="No tienes permiso para actualizar este usuario",
        )

    db_user = db.query(User).filter(User.id == id).first()

    if not db_user:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="User not found")

    if user.name is not None:
        db_user.name = user.name
    if user.email is not None:
        db_user.email = user.email
    if user.password is not None:
        db_user.password = get_password_hash(user.password)

    db.commit()
    db.refresh(db_user)

    return db_user


@router.delete("/users/{id}", status_code=HTTP_204_NO_CONTENT, tags=["users"])
def delete_user(
    id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_admin),
):
    db_user = db.query(User).filter(User.id == id).first()

    if not db_user:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="User not found")

    if current_user.id == id:
        raise HTTPException(
            status_code=400, detail="No puedes eliminar tu propia cuenta"
        )

    db.delete(db_user)
    db.commit()

    return Response(status_code=HTTP_204_NO_CONTENT)
