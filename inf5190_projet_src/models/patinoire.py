from re import A
from inf5190_projet_src.models.base import Base
from sqlalchemy import ForeignKey 
from inf5190_projet_src import db
from sqlalchemy.orm import relationship


class Patinoire(Base):

    __tablename__ = 'patinoire'
    
    nom_pat = db.Column(db.String(255), unique=True,  nullable=False)
    arron_id = db.Column(db.Integer, ForeignKey('arrondissement.id'))
    children = relationship("PatinoirCondition")

    def __init__(self, nom_pat, arron_id):
        self.name= nom_pat
        self.arron_id = arron_id

        
    def __repr__(self):
        return "<Ptinoire(patinoire_id='%d', nom_pat='%s', arron_id='%d')>" % (
            self.id, self.nom_pat, self.arron_id)

    def asDictionary(self):
        return {"patinoire_id": self.id,
                "nom_pat":self.nom_pat,
                "arron_id": self.arron_id
                }