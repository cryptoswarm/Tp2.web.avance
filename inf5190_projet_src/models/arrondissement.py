from inf5190_projet_src import db
from base import Base
from sqlalchemy.orm import relationship


class Arrondissement(Base):
    __tablename__ = 'arrondissement'
    
    name = db.Column(db.String(255), unique=True,  nullable=False)
    cle = db.Column(db.String(50), unique=True,  nullable=False)
    children = relationship("Glissade")

    def __init__(self, name):
        self.name= name
        
    def __repr__(self):
        return "<Arrondissement(arrondissement_id='%d', name='%s', cle='%s')>" % (
            self.id, self.name, self.cle)

    def asDictionary(self):
        return {"arrondissement_id": self.id,
                "name":self.name,
                "cle": self.cle
                } 