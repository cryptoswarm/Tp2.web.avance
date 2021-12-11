from inf5190_projet_src import db
from sqlalchemy.ext.declarative import declarative_base

Dec_Base = declarative_base()


class Base(db.Model):

    __abstract__ = True
    id = db.Column(db.Integer, primary_key=True)
