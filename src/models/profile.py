from sqlalchemy.orm import relationship
from src.models.base import Base
from src import db
from marshmallow import fields, validate
from flask_marshmallow import Marshmallow
from src.models.followed_arr import FollowedArrSchema

FOLLOWED_ARR_NBR = "One arrondissement or more are requiered"
NAME_LEN = "Name is too short < 4"
EMAIL_ERR = "Not a valid email address"


ma = Marshmallow()


class Profile(Base):
    __tablename__ = "profile"

    complete_name = db.Column(db.String(255), unique=False, nullable=False)
    email = db.Column(db.String(80), unique=True, nullable=False)
    followed_arr = relationship("InspectedArr")

    def __init__(self, complete_name, email):
        self.complete_name = complete_name
        self.email = email

    def __repr__(self):
        return "<Profile(id='%d', complete_name='%s', email='%s')>" % (
            self.id,
            self.complete_name,
            self.email,
        )

    def asDictionary(self):
        return {"id": self.id, "complete_name": self.complete_name, "email": self.email}


class ProfileCreateSchema(ma.Schema):
    id = fields.Number()
    complete_name = fields.String(
        required=True, validate=validate.Length(4, error=NAME_LEN)
    )
    email = fields.Str(required=True, validate=validate.Email(error=EMAIL_ERR))
    followed_arr = fields.List(
        fields.String(),
        required=True,
        validate=validate.Length(min=1, error=FOLLOWED_ARR_NBR),
    )


class ProfileResponseSchema(ma.Schema):
    id = fields.Number()
    complete_name = fields.String(required=True, validate=validate.Length(4))
    email = (fields.Str(required=True, validate=validate.Email(error=EMAIL_ERR)),)
    followed_arr = fields.Nested(FollowedArrSchema)
