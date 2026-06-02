import pytest
from pydantic import ValidationError
from app.schemas.venta import VentaCreate, VentaUpdate, VentaResponse

# ✅ Caso válido para VentaCreate
def test_venta_create_valida():
    venta = VentaCreate(
        id_producto=1,
        id_usuario=2,
        id_cliente=3,
        fecha="2026-05-31"
    )
    assert venta.id_producto == 1
    assert venta.id_usuario == 2
    assert venta.id_cliente == 3
    assert venta.fecha == "2026-05-31"

# ❌ Caso inválido: id_producto con string
def test_venta_create_invalida():
    with pytest.raises(ValidationError):
        VentaCreate(
            id_producto="uno",   # debería ser int
            id_usuario=2,
            id_cliente=3,
            fecha="2026-05-31"
        )

# ✅ Caso válido para VentaUpdate parcial
def test_venta_update_parcial():
    venta_update = VentaUpdate(
        id_producto=10
    )
    assert venta_update.id_producto == 10
    assert venta_update.id_usuario is None
    assert venta_update.fecha is None

# ❌ Caso inválido: fecha con número
def test_venta_update_invalida():
    with pytest.raises(ValidationError):
        VentaUpdate(
            fecha=12345   # debería ser str
        )

# ✅ Caso válido para VentaResponse
def test_venta_response_valida():
    venta_resp = VentaResponse(
        id_producto=5,
        id_usuario=7,
        id_cliente=9,
        fecha="2026-06-01"
    )
    assert venta_resp.id_producto == 5
    assert venta_resp.id_usuario == 7
    assert venta_resp.id_cliente == 9
    assert venta_resp.fecha.startswith("2026-06")
