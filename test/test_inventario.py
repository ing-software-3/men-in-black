import pytest
from pydantic import ValidationError
from app.schemas.inventario import InventarioCreate, InventarioUpdate, InventarioResponse

# ✅ Caso válido para InventarioCreate con ropa
def test_inventario_create_valido():
    inv = InventarioCreate(
        name=["Camiseta azul", "Pantalón negro"],
        id_producto=1,
        id_filtro=10,
        log_inventario="Ingreso inicial de prendas"
    )
    assert inv.id_producto == 1
    assert isinstance(inv.name, list)
    assert "Pantalón negro" in inv.name

# ❌ Caso inválido: name no es lista
def test_inventario_create_invalido_name():
    with pytest.raises(ValidationError):
        InventarioCreate(
            name="Camiseta azul",   # debería ser lista
            id_producto=1,
            id_filtro=10,
            log_inventario="Registro de ropa"
        )

# ✅ Caso válido para InventarioUpdate con campos opcionales
def test_inventario_update_parcial():
    inv_update = InventarioUpdate(
        name=["Chaqueta roja"]
    )
    assert inv_update.name == ["Chaqueta roja"]
    assert inv_update.id_producto is None

# ❌ Caso inválido: id_filtro con string
def test_inventario_update_invalido():
    with pytest.raises(ValidationError):
        InventarioUpdate(
            id_filtro="veinte"   # debería ser int
        )

# ✅ Caso válido para InventarioResponse
def test_inventario_response_valido():
    inv_resp = InventarioResponse(
        name=["Vestido verde", "Falda blanca"],
        id_producto=3,
        id_filtro=20,
        log_inventario="Stock actualizado de ropa"
    )
    assert inv_resp.id_filtro == 20
    assert "Vestido verde" in inv_resp.name
    assert inv_resp.log_inventario.startswith("Stock")
