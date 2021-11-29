import logging

from routers import animal


class Animal():
    def __init__(self, db=[]):
        self.db = db

    def __animal_exists(self, id) -> bool:
        for i in range(len(self.db)):
            if self.db[i]['id'] == id:
                return True
        return False

    def __get_next_id(self) -> int:
        id = len(self.db)
        logging.error(id)
        while self.__animal_exists(id):
            id + 1
        logging.error(id)
        return id

    def adiciona_animal(self, novo_animal):
        id = len(self.db) + 1
        while self.__animal_exists(id):
            id += 1
        logging.error(id)
        self.db.append({"id": id, "nome": novo_animal.nome,
                       "raça": novo_animal.raca})

    def busca_animais(self):
        return (self.db)

    def busca_animal(self, id) -> bool:
        for i in range(len(self.db)):
            if self.db[i]['id'] == id:
                return (self.db)[i]
        return False

    def atualiza_animal(self, novo_animal) -> bool:
        if not self.__animal_exists(novo_animal.id):
            return False
        for i in range(len(self.db)):
            if self.db[i]['id'] == novo_animal.id:
                self.db[i] = ({"id": novo_animal.id,
                               "nome": novo_animal.nome, "raça": novo_animal.raca})
                return True
        return False

    def deleta_animal(self, id) -> bool:
        for i in range(len(self.db)):
            if self.db[i]['id'] == id:
                del self.db[i]
                return True
        return False
