from inf5190_projet_src import db


class Base(db.Model):

    __abstract__ = True
    id = db.Column(db.Integer, primary_key=True)
