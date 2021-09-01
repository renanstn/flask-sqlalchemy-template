from settings import db


class Project(db.Model):
    id = db.Column(db.String, primary_key=True)
    name = db.Column(db.String, unique=True)
