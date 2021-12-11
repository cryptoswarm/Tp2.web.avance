import hashlib
from inf5190_projet_src.models.base import Base, Dec_Base
from inf5190_projet_src import db
from sqlalchemy.orm import relationship
from marshmallow import fields, validate
from flask_marshmallow import Marshmallow


ma = Marshmallow()


class Coordinate(Base, Dec_Base):

    __tablename__ = 'coordinates'

    point_x = db.Column(db.String(255),  nullable=False)
    point_y = db.Column(db.String(255),  nullable=False)
    longitude = db.Column(db.String(255),  nullable=False)
    latitude = db.Column(db.String(255), nullable=False)
    position_hash = db.Column(db.String(255), unique=True, nullable=False)
    insta_aquatique = relationship("InstallationAquatique")

    def __init__(self, point_x, point_y, longitude, latitude):
        self.point_x = point_x
        self.point_y = point_y
        self.longitude = longitude
        self.latitude = latitude
        self.position_hash = self.calculate_hash()

    def __repr__(self):
        return "<Coordiante(coordiante_id='%d', \
                            point_x='%s', point_y='%s', \
                            longitude='%s', latitude='%s')>" % (
            self.id, self.point_x, self.point_y, self.longitude, self.latitude)

    def asDictionary(self):
        return {"point_x": self.point_x,
                "point_y": self.point_y,
                "longitude": self.longitude,
                "latitude": self.latitude
                }

    def calculate_hash(self):
        hash = hashlib.md5(str(self.point_x +
                               self.point_y +
                               self.longitude +
                               self.latitude).encode('utf-8')) \
                       .hexdigest()
        return hash


class CoordinateSchema(ma.Schema):

    id = fields.Number()
    point_x = fields.String(required=True, validate=validate.Length(1))
    point_y = fields.String(required=True, validate=validate.Length(1))
    longitude = fields.String(required=True, validate=validate.Length(1))
    latitude = fields.String(required=True, validate=validate.Length(1))
