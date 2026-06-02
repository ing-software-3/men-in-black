import pytest
from pydantic import ValidationError
from app.schemas.usuario import UsuarioCreate, UsuarioUpdate, UsuarioResponse

# ✅ Caso válido para UsuarioCreate
def test_usuario_create_valido():
    usuario = UsuarioCreate(
        nombre="Carlos",
        apellido="Ramírez",
        cargo="Administrador"
    )
    assert usuario.nombre == "Carlos"
    assert usuario.apellido == "Ramírez"
    assert usuario.cargo == "Administrador"

# ❌ Caso inválido: nombre con número
def test_usuario_create_invalido_nombre():
    with pytest.raises(ValidationError):
        UsuarioCreate(
            nombre=12345,   # debería ser str
            apellido="Ramírez",
            cargo="Administrador"
        )

# ✅ Caso válido para UsuarioUpdate con campos opcionales
def test_usuario_update_parcial():
    usuario_update = UsuarioUpdate(
        cargo="Vendedor"
    )
    assert usuario_update.cargo == "Vendedor"
    assert usuario_update.nombre is None

# ❌ Caso inválido: apellido con número
def test_usuario_update_invalido():
    with pytest.raises(ValidationError):
        UsuarioUpdate(
            apellido=6789   # debería ser str
        )

# ✅ Caso válido para UsuarioResponse
def test_usuario_response_valido():
    usuario_resp = UsuarioResponse(
        id_usuario=1,
        nombre="Laura",
        apellido="Gómez",
        cargo="Gerente"
    )
    assert usuario_resp.id_usuario == 1
    assert usuario_resp.nombre == "Laura"
    assert usuario_resp.apellido == "Gómez"
    assert usuario_resp.cargo == "Gerente"
