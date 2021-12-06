import logging
from os import stat
from fastapi import APIRouter, Response, responses, status
from pydantic import BaseModel
from utils.animal import Animal

router = APIRouter()


class NovoAnimal(BaseModel):
    nome: str = ""
    raca: str = ""


fakeDB = []

animal = Animal(fakeDB)


@router.get("/animais", tags=['animais'], status_code=200)
async def busca_animais(response: Response):
    if not animal.exibir_todos():
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"msg": "Nenhum animal encontrado"}
    return animal.exibir_todos()


@router.get("/animais/{id_animal}", tags=['animais'], status_code=200)
async def busca_animal_byid(id_animal: int, response: Response):
    _animal = animal.busca_animal_byid(id_animal)
    if not _animal:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"msg": "Animal não encontrado"}
    else:
        return _animal


@router.post("/animais", tags=['animais'], status_code=200)
async def adiciona_animal(novo_animal: NovoAnimal, response: Response):
    try:
        created = animal.adiciona_animal(novo_animal.nome, novo_animal.raca)
        if not created:
            response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
            return{"msg": "Animal não inserido"}
        return {"msg": "Animal inserido"}
    except Exception as e:
        logging.error(e)
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return {"msg": "Problema para inserir o animal"}


@router.put("/animais", tags=['animais'], status_code=200)
async def atualiza_animal(id_animal: int, atualiza_animal: NovoAnimal, response: Response):
    try:
        _animal = animal.atualiza_animal(
            id_animal,
            atualiza_animal.nome,
            atualiza_animal.raca
        )
        if not _animal:
            response.status_code = status.HTTP_404_NOT_FOUND
            return {"msg": "Animal não encontrado"}
        return {"msg": "Animal atualizado"}
    except Exception as e:
        logging.error(e)
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return {"msg": "Problema para atualizar o animal"}


@router.delete("/animais/{id_animal}", tags=['animais'], status_code=200)
async def deleta_animal_byid(id_animal: int, response: Response):
    try:
        _animal = animal.deleta_animal_byid(id_animal)
        if not _animal:
            response.status_code = status.HTTP_404_NOT_FOUND
            return {"msg": "Animal não encontrado"}
        return {"msg": "Animal deletado"}
    except Exception as e:
        logging.error(e)
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return {"msg": "Problema para deletar o animal"}
