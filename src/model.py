from src import db
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50))
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))

    def __repr__(self):
        return f"User('{self.name}','{self.email}')"

    def to_dict(self):
        return {"id": self.id, "name": self.name, "email": self.email}
