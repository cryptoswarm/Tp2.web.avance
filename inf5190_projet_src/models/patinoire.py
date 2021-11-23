from re import A
from inf5190_projet_src.models.base import Base
from sqlalchemy import ForeignKey 
from inf5190_projet_src import db
from sqlalchemy.orm import relationship
from marshmallow import schema, fields, pre_load, validate
from flask_marshmallow import Marshmallow


ma = Marshmallow()

class Patinoire(Base):

    __tablename__ = 'patinoire'
    
    nom_pat = db.Column(db.String(255), unique=True,  nullable=False)
    arron_id = db.Column(db.Integer, ForeignKey('arrondissement.id'))
    children = relationship("PatinoirCondition")

    def __init__(self, nom_pat, arron_id):
        self.nom_pat= nom_pat
        self.arron_id = arron_id

        
    def __repr__(self):
        return "<Ptinoire(patinoire_id='%d', nom_pat='%s', arron_id='%d')>" % (
            self.id, self.nom_pat, self.arron_id)

    def asDictionary(self):
        return {"id": self.id,
                "nom_pat":self.nom_pat
                }
    
class PatinoireSchema(ma.Schema):
    id = fields.Number()
    nom_pat = fields.String(required=True, validate=validate.Length(1))
    # date_maj = fields.DateTime(required=True)
    # ouvert = fields.Boolean(required=True)
    # deblaye = fields.Boolean(required=True)
    # condition = fields.String(required=True, validate=validate.Length(1))
    arron_id = fields.Number(required=True)
