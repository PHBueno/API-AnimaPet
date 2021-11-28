class User():
    def __init__(self, db=[]):
        self.db = db
    
    def adiciona(self, username, password, email):
        id = len(self.db)
        self.db.append({"id": id+1, "username": username, "password": password, "email": email})
        
    def exibir_todos(self):
        return (self.db)

    def busca_usuario(self, id):
        user = dict()
        for i in self.db:
            if i['id'] == id:
                user = {"username": i['username'], "email": i['email']}
                return (user)