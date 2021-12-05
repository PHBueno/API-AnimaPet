import re


class Validador():
    def emailEhValido(email):
        return re.search(r'^[\w]+@[\w]+\.[\w]{2,4}', email) != None
