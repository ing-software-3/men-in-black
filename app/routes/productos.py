from fastapi import APIRouter, Depends, HTTPException, Response
from sqlalchemy.orm import Session
from starlette.status import HTTP_204_NO_CONTENT, HTTP_404_NOT_FOUND

from app.core.deps import get_db
from app.models.producto import Product
from app.schemas.producto import ProductCreate, ProductResponse, ProductUpdate

router = APIRouter()


@router.get("/productos", response_model=list[ProductResponse], tags=["productos"])
def get_products(
    db: Session = Depends(get_db),
):
    return db.query(Product).all()


@router.get("/productos/{id}", response_model=ProductResponse, tags=["productos"])
def get_product(
    id: int,
    db: Session = Depends(get_db),
):
    product = db.query(Product).filter(Product.id_producto == id).first()

    if not product:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="Producto no encontrado")

    return product


@router.post("/productos", response_model=ProductResponse, tags=["productos"])
def create_product(
    product: ProductCreate,
    db: Session = Depends(get_db),
):
    db_product = Product(
        nombre=product.nombre,
        precio=product.precio,
        categoria=product.categoria,
        stock=product.stock,
        descripcion=product.descripcion,
    )
    db.add(db_product)
    db.commit()
    db.refresh(db_product)

    return db_product


@router.put("/productos/{id}", response_model=ProductResponse, tags=["productos"])
def update_product(
    id: int,
    product: ProductUpdate,
    db: Session = Depends(get_db),
):
    db_product = db.query(Product).filter(Product.id_producto == id).first()

    if not db_product:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="Producto no encontrado")

    if product.nombre is not None:
        db_product.nombre = product.nombre
    if product.precio is not None:
        db_product.precio = product.precio
    if product.categoria is not None:
        db_product.categoria = product.categoria
    if product.stock is not None:
        db_product.stock = product.stock
    if product.descripcion is not None:
        db_product.descripcion = product.descripcion

    db.commit()
    db.refresh(db_product)

    return db_product


@router.delete("/productos/{id}", status_code=HTTP_204_NO_CONTENT, tags=["productos"])
def delete_product(
    id: int,
    db: Session = Depends(get_db),
):
    db_product = db.query(Product).filter(Product.id_producto == id).first()

    if not db_product:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="Producto no encontrado")

    db.delete(db_product)
    db.commit()

    return Response(status_code=HTTP_204_NO_CONTENT)
