from fastapi import APIRouter
from pydantic import BaseModel

import bcrypt
import logging

# INTERNAL
from utils.usuario import User

class NovoUsuario(BaseModel):
    username: str
    password: str
    email: str

router = APIRouter()

fakeDB = []

user = User(fakeDB)

@router.post("/user", tags=['usuario'])
async def cria_usuario(novo_usuario: NovoUsuario):
    try:
        # senha criptografada
        hash_password = bcrypt.hashpw(novo_usuario.password.encode('utf-8'), bcrypt.gensalt())

        # Retorna True ou False
        created = user.adiciona(novo_usuario.username, hash_password, novo_usuario.email)

        if not created:
            return {"msg": "Usuário já existe"}

        return {"msg": "Usuário criado"}

    except Exception as e:
        logging.error(f"{e}")
        return {"msg": "Problema para criar usuário"}
        

@router.get("/user", tags=['usuario'])
async def lista_usuarios():
    if not user.exibir_todos():
        return {"msg": "Nenhum usuário encontrado"}
    return user.exibir_todos()


@router.get("/user/{id_usuario}", tags=['usuario'])
async def busca_usuario(id_usuario: int):
    return user.busca_usuario_byid(id_usuario)

@router.delete("/user/{id_usuario}", tags=['usuario'])
async def deleta_usuario(id_usuario: int):
    user.deleta_usuario_byid(id_usuario)
