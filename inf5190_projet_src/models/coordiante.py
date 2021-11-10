from re import A
from inf5190_projet_src.models.base import Base
from sqlalchemy import ForeignKey 
from inf5190_projet_src import db
from sqlalchemy.orm import relationship


class Coordiante(Base):

    __tablename__ = 'coordiantes'
    
    point_x = db.Column(db.String(255),  nullable=False)
    point_y = db.Column(db.String(255),  nullable=False)
    longitude = db.Column(db.String(255),  nullable=False)
    latitude = db.Column(db.String(255), nullable=False)
    insta_aquatique = relationship("InstallationAquatique")

    def __init__(self, point_x, point_y, longitude, latitude):
        self.point_x = point_x
        self.point_y = point_y
        self.longitude = longitude
        self.latitude = latitude
                 
    def __repr__(self):
        return "<Coordiante(coordiante_id='%d', point_x='%s', point_y='%s', \
                            longitude='%s', latitude='%s')>" % (
            self.id, self.point_x, self.point_y, self.longitude, self.latitude)

    def asDictionary(self):
        return {"coordiante_id": self.id,
                "point_x":self.point_x,
                "point_y": self.point_y,
                "longitude": self.longitude,
                "latitude": self.latitude
                } 