from fastapi import APIRouter, Depends, HTTPException, Response
from sqlalchemy.orm import Session
from starlette.status import HTTP_204_NO_CONTENT, HTTP_404_NOT_FOUND

from app.core.deps import get_db
from app.models.filtro import filtro
from app.schemas.filtro import FiltroCreate, FiltroResponse, FiltroUpdate

router = APIRouter()


@router.get("/filtros", response_model=list[FiltroResponse], tags=["filtros"])
def get_filtros(db: Session = Depends(get_db)):
    return db.query(filtro).all()


@router.get("/filtros/{id}", response_model=FiltroResponse, tags=["filtros"])
def get_filtro(id: int, db: Session = Depends(get_db)):
    filtro_db = db.query(filtro).filter(filtro.id_filtro == id).first()

    if not filtro_db:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="Filtro no encontrado")

    return filtro_db


@router.post("/filtros", response_model=FiltroResponse, tags=["filtros"])
def create_filtro(filtro_in: FiltroCreate, db: Session = Depends(get_db)):
    filtro_db = filtro(
        categoria=filtro_in.categoria,
        talla=filtro_in.talla,
        color=filtro_in.color,
    )
    db.add(filtro_db)
    db.commit()
    db.refresh(filtro_db)

    return filtro_db


@router.put("/filtros/{id}", response_model=FiltroResponse, tags=["filtros"])
def update_filtro(id: int, filtro_in: FiltroUpdate, db: Session = Depends(get_db)):
    filtro_db = db.query(filtro).filter(filtro.id_filtro == id).first()

    if not filtro_db:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="Filtro no encontrado")

    if filtro_in.categoria is not None:
        filtro_db.categoria = filtro_in.categoria
    if filtro_in.talla is not None:
        filtro_db.talla = filtro_in.talla
    if filtro_in.color is not None:
        filtro_db.color = filtro_in.color

    db.commit()
    db.refresh(filtro_db)

    return filtro_db


@router.delete("/filtros/{id}", status_code=HTTP_204_NO_CONTENT, tags=["filtros"])
def delete_filtro(id: int, db: Session = Depends(get_db)):
    filtro_db = db.query(filtro).filter(filtro.id_filtro == id).first()

    if not filtro_db:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="Filtro no encontrado")

    db.delete(filtro_db)
    db.commit()

    return Response(status_code=HTTP_204_NO_CONTENT)
