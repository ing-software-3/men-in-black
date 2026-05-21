from fastapi import APIRouter, Depends, HTTPException, Response
from sqlalchemy.orm import Session
from starlette.status import HTTP_204_NO_CONTENT, HTTP_404_NOT_FOUND

from app.core.deps import get_db
from app.models.usuario import Usuario
from app.schemas.usuario import UsuarioCreate, UsuarioResponse, UsuarioUpdate

router = APIRouter()


@router.get("/usuarios", response_model=list[UsuarioResponse], tags=["usuarios"])
def get_usuarios(db: Session = Depends(get_db)):
    return db.query(Usuario).all()


@router.get("/usuarios/{id}", response_model=UsuarioResponse, tags=["usuarios"])
def get_usuario(id: int, db: Session = Depends(get_db)):
    usuario_db = db.query(Usuario).filter(Usuario.id_usuario == id).first()

    if not usuario_db:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="Usuario no encontrado")

    return usuario_db


@router.post("/usuarios", response_model=UsuarioResponse, tags=["usuarios"])
def create_usuario(usuario_in: UsuarioCreate, db: Session = Depends(get_db)):
    usuario_db = Usuario(
        nombre=usuario_in.nombre,
        apellido=usuario_in.apellido,
        cargo=usuario_in.cargo,
    )
    db.add(usuario_db)
    db.commit()
    db.refresh(usuario_db)

    return usuario_db


@router.put("/usuarios/{id}", response_model=UsuarioResponse, tags=["usuarios"])
def update_usuario(id: int, usuario_in: UsuarioUpdate, db: Session = Depends(get_db)):
    usuario_db = db.query(Usuario).filter(Usuario.id_usuario == id).first()

    if not usuario_db:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="Usuario no encontrado")

    if usuario_in.nombre is not None:
        usuario_db.nombre = usuario_in.nombre
    if usuario_in.apellido is not None:
        usuario_db.apellido = usuario_in.apellido
    if usuario_in.cargo is not None:
        usuario_db.cargo = usuario_in.cargo

    db.commit()
    db.refresh(usuario_db)

    return usuario_db


@router.delete("/usuarios/{id}", status_code=HTTP_204_NO_CONTENT, tags=["usuarios"])
def delete_usuario(id: int, db: Session = Depends(get_db)):
    usuario_db = db.query(Usuario).filter(Usuario.id_usuario == id).first()

    if not usuario_db:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="Usuario no encontrado")

    db.delete(usuario_db)
    db.commit()

    return Response(status_code=HTTP_204_NO_CONTENT)
