class User():
    """
    Classe responsável por todas as operações envolvendo usuários
    """

    def __init__(self, db=[]):
        self.db = db

    def __user_exists(self, username) -> bool:
        for i in self.db:
            if i['username'] == username:
                return False
        return True
    
    def adiciona(self, username, password, email) -> bool:
        id = len(self.db)
        if not self.__user_exists(username):
            return False
        self.db.append({"id": id+1, "username": username, "password": password, "email": email})
        return True
        
    def exibir_todos(self):
        if self.db is None:
            return False
        return (self.db)

    def busca_usuario_byid(self, id) -> dict:
        user = dict()
        for i in self.db:
            if i['id'] == id:
                user = {"username": i['username'], "email": i['email']}
                return (user)
        return {"msg": "Usuário não encontrado"}
    
    def deleta_usuario_byid(self, id):
        for i in range(len(self.db)):
            if self.db[i]['id'] == id:
                del self.db[i]
                return True
        return False
    
    