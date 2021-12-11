from inf5190_projet_src import db
from inf5190_projet_src.models.base import Base, Dec_Base
from sqlalchemy import ForeignKey
from marshmallow import fields, validate
from flask_marshmallow import Marshmallow


ma = Marshmallow()


class Glissade(Base, Dec_Base):

    __tablename__ = 'glissade'

    name = db.Column(db.String(255), unique=True,  nullable=False)
    date_maj = db.Column(db.DateTime(timezone=True), nullable=False,
                         default=db.func.current_timestamp())
    ouvert = db.Column(db.Boolean, nullable=False, default=False)
    deblaye = db.Column(db.Boolean, nullable=False, default=False)
    condition = db.Column(db.String(255), nullable=False)
    arrondissement_id = db.Column(db.Integer, ForeignKey('arrondissement.id'))

    def __init__(self, name, date_maj, ouvert,
                 deblaye, condition, arrondissement_id):
        self.name = name
        self.date_maj = date_maj
        self.ouvert = ouvert
        self.deblaye = deblaye
        self.condition = condition
        self.arrondissement_id = arrondissement_id

    def __repr__(self):
        return "<Glissade(glissade_id='%d', name='%s', \
                          date_maj='%s', ouvert='%s', \
                          deblaye='%s', condition='%s', \
                          arrondissement_id='%d')>" % (
            self.id, self.name, self.date_maj,
            self.ouvert, self.deblaye, self.condition,
            self.arrondissement_id)

    def asDictionary(self):
        return {"glissade_id": self.id,
                "name": self.name,
                "date_maj": self.date_maj,
                "ouvert": self.ouvert,
                "deblaye": self.deblaye,
                "condition": self.condition,
                "arrondissement_id": self.arrondissement_id
                }


class GlissadeSchema(ma.Schema):

    id = fields.Number()
    name = fields.String(required=True, validate=validate.Length(1))
    date_maj = fields.DateTime(required=True)
    ouvert = fields.Boolean(required=True)
    deblaye = fields.Boolean(required=True)
    condition = fields.String(required=True, validate=validate.Length(1))
    arrondissement_id = fields.Number(required=True)
