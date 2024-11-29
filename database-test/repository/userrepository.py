from dao import userDAO
from database import db
from model import User

class UserRepository:
    def __init__(self):
        self.userDAO = userDAO()

    def query_json(self):
        users = self.userDAO.query()
        return ([user.toJson() for user in users])
    
    def query(self):
        pass
    
    def add(self):
        retorno = userDAO.add("Sol", "sol@gmail.com")
        if retorno:
            return "Adicionado"
        return "Erro"