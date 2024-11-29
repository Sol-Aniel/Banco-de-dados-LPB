from model import User, Product
from database import db

class userDAO:
    @staticmethod
    def query():
        return User.query.all()
    
    @staticmethod
    def add(name, email):
        try:
            user = User(name = name, email = email)
            p = Product(name = "sjsjks", price = 13.9, user_id = 0)
            db.session.add(user)
            db.session.add(p)
            db.session.commit()
            return True
        except Exception as e:
            db.session.rollback()
            return False