from fastapi import FastAPI,HTTPException
from pydantic import BaseModel

app = FastAPI()


productos= [
    {"id":1,"Productos":"chamarra negra", "precio":200000},
    {"id":1,"Productos":"chamarra negra", "precio":200000},
    {"id":1,"Productos":"chamarra negra", "precio":200000},
]

class producto(BaseModel):
    producto:str
    precio:float

@app.get("/")
def get_start():
    return{"clase":"software III"}

@app.get("/Productos")
def get_productos():
    return{"codigo":200,"datos":productos}

@app.get({"/productos/{producto_id}"})
def get_producto (producto_id:int):
    for producto in productos:
        if producto["id"]==producto_id:
            return{"codigo":200,"producto":producto}
    raise HTTPException(status_code=404,detail="Producto no encontrado")