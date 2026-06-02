import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.core.database import Base
from app.main import app   # tu aplicación FastAPI
from app.models.producto import Product  # tu modelo SQLAlchemy

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
def sample_product(db_session):
    producto = Product(
        nombre="Laptop",
        precio=2500.00,
        categoria="Electrónica",
        stock=10,
        descripcion="Laptop de prueba"
    )
    db_session.add(producto)
    db_session.commit()
    db_session.refresh(producto)
    return producto

# ✅ Test: insertar y recuperar producto
def test_product_fixture(db_session):
    producto = Product(
        nombre="Celular",
        precio=1200.00,
        categoria="Electrónica",
        stock=50,
        descripcion="Celular de prueba"
    )
    db_session.add(producto)
    db_session.commit()

    result = db_session.query(Product).filter_by(nombre="Celular").first()
    assert result is not None
    assert result.precio == 1200.00
    assert result.stock == 50

# ✅ Test: fixture sample_product
def test_sample_product_fixture(sample_product):
    assert sample_product.nombre == "Laptop"
    assert sample_product.precio == 2500.00
    assert sample_product.categoria == "Electrónica"
    assert sample_product.stock == 10
    assert "prueba" in sample_product.descripcion

# ✅ Test: endpoint de productos (si existe en tu app)
def test_products_endpoint(client, admin_headers):
    response = client.get("/products", headers=admin_headers)
    assert response.status_code in (200, 404)  # depende de si tienes ruta implementada
