from fastapi import APIRouter
from app.schemas import UsuarioSchema

router = APIRouter()

usuarios = []

@router.get("/usuarios")
def listar_usuarios():
    return usuarios

@router.post("/usuarios")
def criar_usuario(usuario: UsuarioSchema):
    usuarios.append(usuario)
    return usuario
