from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.database import Base, engine
from app.routes.auth import router as auth_router
from app.routes.user import router as user_router
from app.routes.productos import router as productos_router
from app.routes.filtro import router as filtro_router
from app.routes.usuario import router as usuario_router
from app.routes.inventario import router as inventario_router
from app.routes.cliente import router as cliente_router
from app.routes.venta import router as venta_router

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Clase Software")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router)
app.include_router(user_router)
app.include_router(productos_router)
app.include_router(filtro_router)
app.include_router(usuario_router)

app.include_router(cliente_router)

app.include_router(inventario_router)  
app.include_router(venta_router)  
