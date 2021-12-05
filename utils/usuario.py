from utils.validador import Validador


class User():
    """
    Classe responsável por todas as operações envolvendo usuários
    """

    def __init__(self, db=[]):
        self.db = db

    # Função interna para verificar se usuário já foi cadastrado
    def __user_exists(self, username) -> bool:
        for i in self.db:
            if i['username'] == username:
                return False
        return True

    def __generate_id(self):  # Gera id para usuário
        if len(self.db) == 0:
            return 1
        return (self.db[len(self.db) - 1]['id']) + 1

    def adiciona(self, username, password, email) -> bool:
        print("EATIAAAAAAAAAAAAAAAAAAAAAAAAAA")
        if not self.__user_exists(username):
            return False
        if not Validador.emailEhValido(email):
            return False
        id = self.__generate_id()
        print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
        # Adiciona o novo dicionario na lista de usuarios
        self.db.append({"id": id, "username": username,
                       "password": password, "email": email})
        print("EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE")
        return True

    def exibir_todos(self):
        if self.db is None:  # Verifica se o banco está vazio
            return False
        return (self.db)

    def busca_usuario_byid(self, id):
        user = dict()
        for i in self.db:
            if i['id'] == id:
                # Ajusta campos para impressão
                user = {"username": i['username'], "email": i['email']}
                return (user)
        return False

    def deleta_usuario_byid(self, id) -> bool:
        for i in range(len(self.db)):
            if self.db[i]['id'] == id:
                del self.db[i]  # Remove a posição em que o usuário se encontra
                return True
        return False

    def atualiza_usuario(self, id, username, email):
        for i in self.db:
            if i['id'] == id:
                i['username'] = username
                i['email'] = email
                return True
        return False
