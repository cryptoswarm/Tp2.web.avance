from inf5190_projet_src import db
from inf5190_projet_src.models.base import Base, Dec_Base
from sqlalchemy.orm import relationship


class Arrondissement(Base, Dec_Base):
    __tablename__ = 'arrondissement'

    name = db.Column(db.String(255), unique=True,  nullable=False)
    cle = db.Column(db.String(50), unique=True,  nullable=True)
    glissade = relationship("Glissade")
    patinoire = relationship("Patinoire")

    def __init__(self, name, cle):
        self.name = name
        self.cle = cle

    def __repr__(self):
        return "<Arrondissement(arrondissement_id='%d', \
                                name='%s', \
                                cle='%s')>" % (
            self.id, self.name, self.cle)

    def asDictionary(self):
        return {"arrondissement_id": self.id,
                "name": self.name,
                "cle": self.cle
                }
