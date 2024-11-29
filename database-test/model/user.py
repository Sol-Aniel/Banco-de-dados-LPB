from database import db

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    create_at = db.Column(db.DateTime, default=db.func.now())

    products = db.relationship('Products', back_populates='buyer', lazy=True)

    def __repr__(self):
        return f"<User {self.name}>"
    
    def toJson(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "create_at": self.create_at,
            "products": [product.toJson() for product in self.products]
        }