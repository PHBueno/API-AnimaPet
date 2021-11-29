import logging
from fastapi import APIRouter
from pydantic import BaseModel
from utils.animal import Animal

router = APIRouter()


class NovoAnimal(BaseModel):
    id: int = 0
    nome: str = ""
    raca: str = ""


fakeDB = [
    {"id": 1, "nome": "Atila", "raça": "Cachorro"}
]

animal = Animal(fakeDB)


@router.get("/animais", tags=['animais'])
async def busca_animais():
    return animal.busca_animais()


@router.get("/animais/{id_animal}", tags=['animais'])
async def busca_animal_byid(id_animal: int):
    _animal = animal.busca_animal(id_animal)
    if not _animal:
        return {"msg": "Animal não encontrado"}
    else:
        return _animal


@router.post("/animais", tags=['animais'])
async def adiciona_animal(novo_animal: NovoAnimal):
    try:
        animal.adiciona_animal(novo_animal)
        return {"msg": "Animal inserido"}
    except Exception as e:
        logging.error(e)
        return {"msg": "Problema para inserir o animal"}


@router.put("/animais", tags=['animais'])
async def atualiza_animal(novo_animal: NovoAnimal):
    try:
        _animal = animal.atualiza_animal(novo_animal)
        if not _animal:
            return {"msg": "Animal não encontrado"}
        return {"msg": "Animal atualizado"}
    except Exception as e:
        logging.error(e)
        return {"msg": "Problema para atualizar o animal"}


@router.delete("/animais/{id_animal}", tags=['animais'])
async def deleta_animal_byid(id_animal: int):
    try:
        _animal = animal.deleta_animal(id_animal)
        if not _animal:
            return {"msg": "Animal não encontrado"}
        return {"msg": "Animal deletado"}
    except Exception as e:
        logging.error(e)
        return {"msg": "Problema para deletar o animal"}
