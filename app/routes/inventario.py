from fastapi import APIRouter, Depends, HTTPException, Response
from sqlalchemy.orm import Session
from starlette.status import HTTP_204_NO_CONTENT, HTTP_404_NOT_FOUND

from app.core.deps import get_db
from app.models.inventario import inventario
from app.schemas.inventario import InventarioCreate, InventarioResponse, InventarioUpdate

router = APIRouter()


@router.get("/inventarios", response_model=list[InventarioResponse], tags=["inventarios"])
def get_inventarios(db: Session = Depends(get_db)):
    return db.query(inventario).all()


@router.get("/inventarios/{id}", response_model=InventarioResponse, tags=["inventarios"])
def get_inventario(id: int, db: Session = Depends(get_db)):
    inv_db = db.query(inventario).filter(inventario.id_producto == id).first()

    if not inv_db:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="Inventario no encontrado")

    return inv_db


@router.post("/inventarios", response_model=InventarioResponse, tags=["inventarios"])
def create_inventario(inv_in: InventarioCreate, db: Session = Depends(get_db)):
    inv_db = inventario(
        name=inv_in.name,
        id_producto=inv_in.id_producto,
        id_filtro=inv_in.id_filtro,
        log_inventario=inv_in.log_inventario,
    )
    db.add(inv_db)
    db.commit()
    db.refresh(inv_db)

    return inv_db


@router.put("/inventarios/{id}", response_model=InventarioResponse, tags=["inventarios"])
def update_inventario(id: int, inv_in: InventarioUpdate, db: Session = Depends(get_db)):
    inv_db = db.query(inventario).filter(inventario.id_producto == id).first()

    if not inv_db:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="Inventario no encontrado")

    if inv_in.name is not None:
        inv_db.name = inv_in.name
    if inv_in.id_producto is not None:
        inv_db.id_producto = inv_in.id_producto
    if inv_in.id_filtro is not None:
        inv_db.id_filtro = inv_in.id_filtro
    if inv_in.log_inventario is not None:
        inv_db.log_inventario = inv_in.log_inventario

    db.commit()
    db.refresh(inv_db)

    return inv_db


@router.delete("/inventarios/{id}", status_code=HTTP_204_NO_CONTENT, tags=["inventarios"])
def delete_inventario(id: int, db: Session = Depends(get_db)):
    inv_db = db.query(inventario).filter(inventario.id_producto == id).first()

    if not inv_db:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="Inventario no encontrado")

    db.delete(inv_db)
    db.commit()

    return Response(status_code=HTTP_204_NO_CONTENT)
