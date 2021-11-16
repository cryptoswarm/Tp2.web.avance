from inf5190_projet_src.models.base import Base
from sqlalchemy import ForeignKey 
from inf5190_projet_src import db
from sqlalchemy.orm import relationship


class PatinoirCondition(Base):

    __tablename__ = 'patinoir_condition'

    date_heure = db.Column(db.DateTime, nullable=False)
    ouvert = db.Column(db.Boolean, nullable=False, default=False)
    deblaye = db.Column(db.Boolean, nullable=False, default=False)
    arrose = db.Column(db.Boolean, nullable=False, default=False)
    resurface = db.Column(db.Boolean, nullable=False, default=False)
    patinoire_id = db.Column(db.Integer, ForeignKey('patinoire.id'))


    def __init__(self, date_heure, ouvert, deblaye, arrose, resurface, patinoire_id):
        self.date_heure= date_heure
        self.ouvert = ouvert
        self.deblaye = deblaye
        self.arrose = arrose
        self.resurface = resurface
        self.patinoire_id = patinoire_id

        
    def __repr__(self):
        return "<PatinoirCondition(pat_condition_id='%d', date_heure='%s', ouvert='%s', deblaye='%s', arrose='%s', resurface='%s', patinoire_id='%d')>" % (
            self.id, self.date_heure, self.ouvert, self.deblaye, self.arrose, self.resurface, self.patinoire_id)

    def asDictionary(self):
        return {"date_heure": self.date_heure,
                "ouvert": self.ouvert,
                "deblaye": self.deblaye,
                "arrose": self.arrose,
                "resurface": self.resurface,
                }
