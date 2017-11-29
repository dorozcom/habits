from app import db

class Habit(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))

    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __repr__(self):
        return '<Habit id={} name={}'.format(self.id, self.name)

