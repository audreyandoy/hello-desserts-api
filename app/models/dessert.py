from app import db


class Dessert(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)
    description = db.Column(db.String)


    def to_json(self):
        return {
        "id": self.id,
        "name": self.name,
        "description": self.description,
    }