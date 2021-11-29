class User():
    """
    Classe responsável por todas as operações envolvendo usuários
    """

    def __init__(self, db=[]):
        self.db = db

    def __user_exists(self, username) -> bool: # Função interna para verificar se usuário já foi cadastrado
        for i in self.db:
            if i['username'] == username:
                return False
        return True

    def __generate_id(self): # Gera id para usuário
        if len(self.db) == 0:
            return 1
        return (self.db[len(self.db) -1 ]['id']) + 1
    
    def adiciona(self, username, password, email) -> bool:
        if not self.__user_exists(username):
            return False
        id = self.__generate_id()
        self.db.append({"id": id, "username": username, "password": password, "email": email}) # Adiciona o novo dicionario na lista de usuarios
        return True
        
    def exibir_todos(self):
        if self.db is None: # Verifica se o banco está vazio
            return False
        return (self.db)

    def busca_usuario_byid(self, id):
        user = dict()
        for i in self.db:
            if i['id'] == id:
                user = {"username": i['username'], "email": i['email']} # Ajusta campos para impressão
                return (user)
        return False
    
    def deleta_usuario_byid(self, id) -> bool:
        for i in range(len(self.db)):
            if self.db[i]['id'] == id:
                del self.db[i] # Remove a posição em que o usuário se encontra
                return True
        return False
    
    def atualiza_usuario(self, id, username, email):
        for i in self.db:
            if i['id'] == id:
                i['username'] = username
                i['email'] = email
                return True
        return False