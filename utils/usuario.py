class User():
    def __init__(self, db=[]):
        self.db = db
    
    def adiciona(self, username, password, email):
        self.db.append({"username": username, "password": password, "email": email})
        
    def exibir_todos(self):
        return (self.db)