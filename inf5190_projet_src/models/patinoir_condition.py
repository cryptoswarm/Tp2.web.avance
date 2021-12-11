import hashlib
from inf5190_projet_src.models.base import Base, Dec_Base
from sqlalchemy import ForeignKey
from inf5190_projet_src import db
from marshmallow import fields
from flask_marshmallow import Marshmallow


ma = Marshmallow()


class PatinoirCondition(Base, Dec_Base):

    __tablename__ = 'patinoir_condition'

    date_heure = db.Column(db.DateTime, nullable=False)
    ouvert = db.Column(db.Boolean, nullable=False, default=False)
    deblaye = db.Column(db.Boolean, nullable=False, default=False)
    arrose = db.Column(db.Boolean, nullable=False, default=False)
    resurface = db.Column(db.Boolean, nullable=False, default=False)
    patinoire_id = db.Column(db.Integer, ForeignKey('patinoire.id'))
    pat_hash = db.Column(db.String(255), unique=True, nullable=False)

    def __init__(self, date_heure, ouvert,
                 deblaye, arrose, resurface, patinoire_id):
        self.date_heure = date_heure
        self.ouvert = ouvert
        self.deblaye = deblaye
        self.arrose = arrose
        self.resurface = resurface
        self.patinoire_id = patinoire_id
        self.pat_hash = self.calculate_hash()

    def calculate_hash(self):
        hash = hashlib.md5(
                            (
                                self.date_heure.strftime('%Y-%m-%d %H:%M:%S') +
                                str(
                                    self.ouvert +
                                    self.deblaye + self.arrose +
                                    self.resurface +
                                    self.patinoire_id
                                    )
                            ).encode('utf-8')
                          ).hexdigest()
        return hash

    def __repr__(self):
        return "<PatinoirCondition(pat_condition_id='%d', \
                                   date_heure='%s', \
                                   ouvert='%s', deblaye='%s', \
                                   arrose='%s', resurface='%s', \
                                   patinoire_id='%d')>" % (
            self.id, self.date_heure, self.ouvert,
            self.deblaye, self.arrose,
            self.resurface, self.patinoire_id)

    def asDictionary(self):
        return {"date_heure": self.date_heure,
                "ouvert": self.ouvert,
                "deblaye": self.deblaye,
                "arrose": self.arrose,
                "resurface": self.resurface,
                }


class PatConditionSchema(ma.Schema):

    id = fields.Number()
    date_heure = fields.DateTime(required=True)
    ouvert = fields.Boolean(required=True)
    arrose = fields.Boolean(required=True)
    deblaye = fields.Boolean(required=True)
    resurface = fields.Boolean(required=True)
    patinoire_id = fields.Number(required=True)


class EditPatConditionSchema(ma.Schema):

    date_heure = fields.DateTime(required=True)
    ouvert = fields.Boolean(required=True)
    arrose = fields.Boolean(required=True)
    deblaye = fields.Boolean(required=True)
    resurface = fields.Boolean(required=True)
