from fastapi import APIRouter, Depends, HTTPException, Response
from sqlalchemy.orm import Session
from starlette.status import HTTP_204_NO_CONTENT, HTTP_404_NOT_FOUND

from app.core.deps import get_db
from app.models.venta import venta
from app.schemas.venta import VentaCreate, VentaResponse, VentaUpdate

router = APIRouter()


@router.get("/ventas", response_model=list[VentaResponse], tags=["ventas"])
def get_ventas(db: Session = Depends(get_db)):
    return db.query(venta).all()


@router.get("/ventas/{id}", response_model=VentaResponse, tags=["ventas"])
def get_venta(id: int, db: Session = Depends(get_db)):
    venta_db = db.query(venta).filter(venta.id_venta == id).first()

    if not venta_db:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="Venta no encontrada")

    return venta_db


@router.post("/ventas", response_model=VentaResponse, tags=["ventas"])
def create_venta(venta_in: VentaCreate, db: Session = Depends(get_db)):
    venta_db = venta(
        id_producto=venta_in.id_producto,
        id_usuario=venta_in.id_usuario,
        id_cliente=venta_in.id_cliente,
        fecha=venta_in.fecha,
    )
    db.add(venta_db)
    db.commit()
    db.refresh(venta_db)

    return venta_db


@router.put("/ventas/{id}", response_model=VentaResponse, tags=["ventas"])
def update_venta(id: int, venta_in: VentaUpdate, db: Session = Depends(get_db)):
    venta_db = db.query(venta).filter(venta.id_venta == id).first()

    if not venta_db:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="Venta no encontrada")

    if venta_in.id_producto is not None:
        venta_db.id_producto = venta_in.id_producto
    if venta_in.id_usuario is not None:
        venta_db.id_usuario = venta_in.id_usuario
    if venta_in.id_cliente is not None:
        venta_db.id_cliente = venta_in.id_cliente
    if venta_in.fecha is not None:
        venta_db.fecha = venta_in.fecha

    db.commit()
    db.refresh(venta_db)

    return venta_db


@router.delete("/ventas/{id}", status_code=HTTP_204_NO_CONTENT, tags=["ventas"])
def delete_venta(id: int, db: Session = Depends(get_db)):
    venta_db = db.query(venta).filter(venta.id_venta == id).first()

    if not venta_db:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="Venta no encontrada")

    db.delete(venta_db)
    db.commit()

    return Response(status_code=HTTP_204_NO_CONTENT)
