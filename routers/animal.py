import logging
from fastapi import APIRouter
from pydantic import BaseModel
from utils.animal import Animal

router = APIRouter()


class NovoAnimal(BaseModel):
    nome: str = ""
    raca: str = ""


fakeDB = []

animal = Animal(fakeDB)


@router.get("/animais", tags=['animais'])
async def busca_animais():
    if not animal.exibir_todos():
        return {"msg": "Nenhum usuário encontrado"}
    return animal.exibir_todos()


@router.get("/animais/{id_animal}", tags=['animais'])
async def busca_animal_byid(id_animal: int):
    _animal = animal.busca_animal_byid(id_animal)
    if not _animal:
        return {"msg": "Animal não encontrado"}
    else:
        return _animal


@router.post("/animais", tags=['animais'])
async def adiciona_animal(novo_animal: NovoAnimal):
    try:
        created = animal.adiciona_animal(novo_animal.nome, novo_animal.raca)
        if not created:
            return{"msg": "Animal não inserido"}
        return {"msg": "Animal inserido"}
    except Exception as e:
        logging.error(e)
        return {"msg": "Problema para inserir o animal"}


@router.put("/animais", tags=['animais'])
async def atualiza_animal(id_animal: int, atualiza_animal: NovoAnimal):
    try:
        _animal = animal.atualiza_animal(
            id_animal,
            atualiza_animal.nome,
            atualiza_animal.raca
        )
        if not _animal:
            return {"msg": "Animal não encontrado"}
        return {"msg": "Animal atualizado"}
    except Exception as e:
        logging.error(e)
        return {"msg": "Problema para atualizar o animal"}


@router.delete("/animais/{id_animal}", tags=['animais'])
async def deleta_animal_byid(id_animal: int):
    try:
        _animal = animal.deleta_animal_byid(id_animal)
        if not _animal:
            return {"msg": "Animal não encontrado"}
        return {"msg": "Animal deletado"}
    except Exception as e:
        logging.error(e)
        return {"msg": "Problema para deletar o animal"}
