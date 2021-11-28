class User():
    def __init__(self, db=[]):
        self.db = db

    def __user_exists(self, username):
        for i in self.db:
            if i['username'] == username:
                return False
        return True
    
    def adiciona(self, username, password, email):
        id = len(self.db)
        if not self.__user_exists(username):
            return False
        self.db.append({"id": id+1, "username": username, "password": password, "email": email})
        return True
        
    def exibir_todos(self):
        if self.db is None:
            return False
        return (self.db)

    def busca_usuario_id(self, id):
        user = dict()
        for i in self.db:
            if i['id'] == id:
                user = {"username": i['username'], "email": i['email']}
                return (user)
    
    