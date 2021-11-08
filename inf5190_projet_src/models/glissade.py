from inf5190_projet_src import db
from inf5190_projet_src.models.base import Base
from sqlalchemy import ForeignKey 


class Glissade(Base):

    # <glissade>
    #     <nom>Aire de glissade ,Don-Bosco</nom>
    #     <arrondissement>
    #         <nom_arr>RiviÃ¨re-des-Prairies - Pointe-aux-Trembles</nom_arr>
    #         <cle>rdp</cle>
    #         <date_maj>2021-10-18 13:45:13</date_maj>
    #     </arrondissement>
    #     <ouvert>0</ouvert>
    #     <deblaye>0</deblaye>
    #     <condition>N/A</condition>
    # </glissade>
    __tablename__ = 'glissade'
    
    name = db.Column(db.String(255), unique=True,  nullable=False)
    date_maj = db.Column(db.DateTime, nullable=False)
    ouvert = db.Column(db.Boolean, nullable=False, default=False)
    deblaye = db.Column(db.Boolean, nullable=False, default=False)
    condition = db.Column(db.String(255), nullable=False)
    arrondissement_id = db.Column(db.Integer, ForeignKey('arrondissement.id'))

    def __init__(self, name, date_maj, ouvert, deblaye, condition, arrondissement_id):
        self.name= name
        self.date_maj = date_maj
        self.ouvert = ouvert
        self.deblaye = deblaye
        self.condition = condition
        self.arrondissement_id = arrondissement_id
        
    def __repr__(self):
        return "<Arrondissement(glissade_id='%d', name='%s', date_maj='%s', ouvert='%s', deblaye='%s', condition='%s', arrondissement_id='%d' )>" % (
            self.id, self.name, self.date_maj, self.ouvert, self.deblaye, self.condition, self.arrondissement_id)

    def asDictionary(self):
        return {"arrondissement_id": self.id,
                "name":self.name,
                "date_maj": self.date_maj,
                "ouvert": self.ouvert,
                "deblaye": self.deblaye,
                "condition": self.condition,
                "arrondissement_id": self.arrondissement_id
                } 