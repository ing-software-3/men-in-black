from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

productos = [
    {"id": 1, "Producto": "Monitor", "precio": 5000},
    {"id": 1, "Producto": "Mouse", "precio": 5000},
    {"id": 2, "Producto": "Teclado", "precio": 2000}
    
    ]

class Producto(BaseModel):
    id: int
    Producto: str
    precio: float

@app.get("/")
def get_start():
    return {"message": "Bienvenido a la API de productos"}

@app.get("/productos")
def get_productos():
    return {"codigo": 200, "data": productos}

@app.get({"/productos/{id}"})
def get_producto(id: int):
    for producto in productos:
        if producto["id"] == id:
            return {"codigo": 200, "data": producto}
    raise HTTPException(status_code=404, detail="Producto no encontrado")