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
        hash_password = bcrypt.hashpw(novo_usuario.password.encode('utf-8'), bcrypt.gensalt())
        user.adiciona(novo_usuario.username, hash_password, novo_usuario.email)
        # fakeDB.append({"username": novo_usuario.username, "password": hash_password, "email": novo_usuario.email})
        return {"msg": "Usuário criado"}
    except Exception as e:
        logging.error(f"{e}")
        return {"msg": "Problema para criar usuário"}
        

@router.get("/user", tags=['usuario'])
async def lista_usuarios():
    logging.info(user.exibir_todos())
    return user.exibir_todos()


