import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.core.database import Base
from app.main import app   # tu aplicación FastAPI

# BD en memoria para pruebas
engine = create_engine("sqlite:///:memory:", echo=False)
TestingSessionLocal = sessionmaker(bind=engine)

@pytest.fixture(scope="session")
def db_session():
    Base.metadata.create_all(bind=engine)
    session = TestingSessionLocal()
    yield session
    session.close()

@pytest.fixture(scope="session")
def client():
    return TestClient(app)

@pytest.fixture
def admin_headers():
    return {"Authorization": "Bearer faketoken123"}

@pytest.fixture
def inventario_item(db_session):
    # Inserta un inventario de prueba
    from app.models.cliente import Cliente
    cliente = Cliente(
        nombre="Juan",
        apellido="Pérez",
        correo="juan.perez@example.com",
        celular=123456789
    )
    db_session.add(cliente)
    db_session.commit()
    return cliente

def test_cliente_fixture(db_session):
    from app.models.cliente import Cliente
    cliente = Cliente(
        nombre="Juan",
        apellido="Pérez",
        correo="juan.perez@example.com",
        celular=123456789
    )
    db_session.add(cliente)
    db_session.commit()

    result = db_session.query(Cliente).filter_by(nombre="Juan").first()
    assert result is not None
    assert result.apellido == "Pérez"
    assert result.correo.endswith("@example.com")


def test_inventario_endpoint(client, admin_headers):
    response = client.get("/inventario", headers=admin_headers)
    assert response.status_code in (200, 404)  
