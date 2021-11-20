from enum import unique
from re import A
from inf5190_projet_src.models.base import Base
from sqlalchemy import ForeignKey 
from inf5190_projet_src import db
from sqlalchemy.orm import relationship
import hashlib


class InstallationAquatique(Base):

    __tablename__ = 'installation_aquatique'
    
    nom_installation = db.Column(db.String(255),  nullable=False)
    type_installation = db.Column(db.String(255), nullable=False)
    adress = db.Column(db.String(255),  nullable=False, default='UNKNOWN')
    propriete_installation = db.Column(db.String(255),  nullable=False, default='UNKNOWN')
    gestion_inst = db.Column(db.String(255),  nullable=False, default='UNKNOWN')
    equipement_inst = db.Column(db.String(255),  nullable=False, default='UNKNOWN')
    aqua_hash = db.Column(db.String(255), unique=True, nullable=False)
    arron_id = db.Column(db.Integer, ForeignKey('arrondissement.id'))
    position_id = db.Column(db.Integer, ForeignKey('coordiantes.id'))
    # children = relationship("Coordiante")

    def __init__(self, nom_installation, type_installation, adress,
                 propriete_installation, gestion_inst, equipement_inst,
                 arron_id, position_id):
        self.nom_installation= nom_installation
        self.type_installation = type_installation
        self.adress = adress
        self.propriete_installation = propriete_installation
        self.gestion_inst = gestion_inst
        self.equipement_inst = equipement_inst
        self.aqua_hash = self.calculate_hash()
        self.arron_id = arron_id
        self.position_id = position_id


        
    def __repr__(self):
        return "<InstallationAquatique(installation_id='%d', \
                                       nom_installation='%s', \
                                       type_installation='%s, \
                                       adress='%s', \
                                       propriete_installation='%s', \
                                       gestion_inst='%s', \
                                       equipement_inst='%s')>" % (
            self.id, self.nom_installation, self.type_installation,
            self.adress, self.propriete_installation,
            self.propriete_installation, self.gestion_inst,
            self.equipement_inst)

    def asDictionary(self):
        return {"id": self.id,
                "nom_installation":self.nom_installation,
                "type_installation": self.type_installation,
                "adress": self.adress,
                "propriete_installation": self.propriete_installation,
                "gestion_inst": self.gestion_inst,
                "equipement_inst": self.equipement_inst
                }
    

    def calculate_hash(self):
        aqua_hash = hashlib.md5(str(self.nom_installation + self.type_installation +
                            self.adress + self.propriete_installation + 
                            self.gestion_inst+ self.equipement_inst).encode('utf-8')).hexdigest()
        return aqua_hash