from sqlalchemy.orm import relationship
from inf5190_projet_src.models.base import Base
from inf5190_projet_src import db
from marshmallow import schema, fields, pre_load, validate
from flask_marshmallow import Marshmallow

from inf5190_projet_src.models.followed_arr import FollowedArrSchema

ma = Marshmallow()

class Profile(Base):
    __tablename__ = 'profile'

    complete_name = db.Column(db.String(255), unique=False,  nullable=False)
    email = db.Column(db.String(80), unique=True,  nullable=False)
    followed_arr = relationship("InspectedArr")


    def __init__(self, complete_name, email):
        self.complete_name = complete_name
        self.email = email


        
    def __repr__(self):
        return "<Profile(id='%d', complete_name='%s', email='%s')>" % (
            self.id, self.complete_name, self.email)

    def asDictionary(self):
        return {
                "id": self.id,
                "complete_name":self.complete_name,
                "email": self.email
                } 

class ProfileCreateSchema(ma.Schema):
    id = fields.Number()
    complete_name = fields.String(required=True, validate=validate.Length(4))
    email = fields.Str(
        required=True, validate=validate.Email(error="Not a valid email address")
    )
    followed_arr = fields.List(fields.String(), required=True, validate=validate.Length(min=1) )


class ProfileResponseSchema(ma.Schema):
    id = fields.Number()
    complete_name = fields.String(required=True, validate=validate.Length(4))
    email = fields.Str(
        required=True, validate=validate.Email(error="Not a valid email address")
    ),
    followed_arr = fields.Nested(FollowedArrSchema)    