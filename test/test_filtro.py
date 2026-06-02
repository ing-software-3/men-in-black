import pytest
from pydantic import ValidationError
from app.schemas.filtro import FiltroCreate, FiltroUpdate, FiltroResponse

# ✅ Caso válido para FiltroCreate con ropa
def test_filtro_create_valido():
    filtro = FiltroCreate(
        categoria="Camisetas",
        talla=38.0,
        color="Azul"
    )
    assert filtro.categoria == "Camisetas"
    assert filtro.talla == 38.0
    assert filtro.color == "Azul"

# ❌ Caso inválido: talla con string
def test_filtro_create_invalido_talla():
    with pytest.raises(ValidationError):
        FiltroCreate(
            categoria="Zapatos",
            talla="grande",   # debería ser float
            color="Blanco"
        )

# ✅ Caso válido para FiltroUpdate con campos opcionales
def test_filtro_update_parcial():
    filtro_update = FiltroUpdate(
        color="Rojo"
    )
    assert filtro_update.color == "Rojo"
    assert filtro_update.talla is None

# ❌ Caso inválido: categoria con número
def test_filtro_update_invalido():
    with pytest.raises(ValidationError):
        FiltroUpdate(
            categoria=12345   # debería ser str
        )

# ✅ Caso válido para FiltroResponse
def test_filtro_response_valido():
    filtro_resp = FiltroResponse(
        categoria="Pantalones",
        talla=32.0,
        color="Negro"
    )
    assert filtro_resp.categoria == "Pantalones"
    assert filtro_resp.talla == 32.0
    assert filtro_resp.color == "Negro"
