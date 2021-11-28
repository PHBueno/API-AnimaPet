from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class NovoAnimal(BaseModel):
    nome: str
    raca: str

fakeDB = [
    {"id": 1, "nome": "Atila", "raça": "Cachorro"}
]

@router.get("/animais", tags=['animais'])
async def busca_animais():
    return fakeDB

@router.post("/animais", tags=['animais'])
async def adiciona_animal(novo_animal: NovoAnimal):
    id = len(fakeDB)
    fakeDB.append({"id": id+1,"nome": novo_animal.nome, "raça": novo_animal.raca})
    return fakeDB

# TODO: Adicionar rota para update de animal
# @router.put("/animal/{id_animal}", tags=['animal'])
# async def atualiza_animal(id_animal: int):
