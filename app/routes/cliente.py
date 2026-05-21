from fastapi import APIRouter, Depends, HTTPException, Response
from sqlalchemy.orm import Session
from starlette.status import HTTP_204_NO_CONTENT, HTTP_404_NOT_FOUND

from app.core.deps import get_db
from app.models.cliente import Cliente
from app.schemas.cliente import ClienteCreate, ClienteResponse, ClienteUpdate

router = APIRouter()


@router.get("/clientes", response_model=list[ClienteResponse], tags=["clientes"])
def get_clientes(db: Session = Depends(get_db)):
    return db.query(Cliente).all()


@router.get("/clientes/{id}", response_model=ClienteResponse, tags=["clientes"])
def get_cliente(id: int, db: Session = Depends(get_db)):
    cliente_db = db.query(Cliente).filter(Cliente.id_cliente == id).first()

    if not cliente_db:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="Cliente no encontrado")

    return cliente_db


@router.post("/clientes", response_model=ClienteResponse, tags=["clientes"])
def create_cliente(cliente_in: ClienteCreate, db: Session = Depends(get_db)):
    cliente_db = Cliente(
        nombre=cliente_in.nombre,
        apellido=cliente_in.apellido,
        correo=cliente_in.correo,
        celular=cliente_in.celular,
    )
    db.add(cliente_db)
    db.commit()
    db.refresh(cliente_db)

    return cliente_db


@router.put("/clientes/{id}", response_model=ClienteResponse, tags=["clientes"])
def update_cliente(id: int, cliente_in: ClienteUpdate, db: Session = Depends(get_db)):
    cliente_db = db.query(Cliente).filter(Cliente.id_cliente == id).first()

    if not cliente_db:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="Cliente no encontrado")

    if cliente_in.nombre is not None:
        cliente_db.nombre = cliente_in.nombre
    if cliente_in.apellido is not None:
        cliente_db.apellido = cliente_in.apellido
    if cliente_in.correo is not None:
        cliente_db.correo = cliente_in.correo
    if cliente_in.celular is not None:
        cliente_db.celular = cliente_in.celular

    db.commit()
    db.refresh(cliente_db)

    return cliente_db


@router.delete("/clientes/{id}", status_code=HTTP_204_NO_CONTENT, tags=["clientes"])
def delete_cliente(id: int, db: Session = Depends(get_db)):
    cliente_db = db.query(Cliente).filter(Cliente.id_cliente == id).first()

    if not cliente_db:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="Cliente no encontrado")

    db.delete(cliente_db)
    db.commit()

    return Response(status_code=HTTP_204_NO_CONTENT)
