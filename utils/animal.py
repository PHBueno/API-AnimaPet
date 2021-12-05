import logging

class Animal():
    """
    Classe responsável por todas as operações envolvendo animais
    """

    def __init__(self, db=[]):
        self.db = db

    def __animal_exists(self, id) -> bool:
        for i in range(len(self.db)):
            if self.db[i]['id'] == id:
                return False
        return True

    def __generate_id(self):  # Gera id para animal
        if len(self.db) == 0:
            return 1
        return (self.db[len(self.db) - 1]['id']) + 1

    def adiciona_animal(self, nome, raca):
        id = self.__generate_id()
        if not self.__animal_exists(id):
            return False
        self.db.append(
        {
            "id": id, 
            "nome": nome,
            "raça": raca
        })
        return True

    def exibir_todos(self):
        if self.db is None:  # Verifica se o banco está vazio
            return False
        print(self.db)
        return (self.db)

    def busca_animal_byid(self, id):
        animal = dict()
        for i in self.db:
            if i['id'] == id:
                # Ajusta campos para impressão
                animal = {"nome": i['nome'], "raca": i['raça']}
                return (animal)
        return False

    def atualiza_animal(self, id, nome, raca) -> bool:
        for i in self.db:
            if i['id'] == id:
                i['nome'] = nome
                i['raça'] = raca
                return True
        return False

    def deleta_animal_byid(self, id) -> bool:
        for i in range(len(self.db)):
            if self.db[i]['id'] == id:
                del self.db[i]
                return True
        return False
