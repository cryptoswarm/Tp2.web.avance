from inf5190_projet_src import db
from inf5190_projet_src.models.base import Base
from sqlalchemy import ForeignKey 
from marshmallow import fields, validate
from flask_marshmallow import Marshmallow

ma = Marshmallow()
class Followed(Base):

    __tablename__ = 'followed'

    name = db.Column(db.String(255), unique=True, nullable=False)
    profile_id = db.Column(db.Integer, ForeignKey('profile.id'))



    def __init__(self, name:str, profile_id:int):
        self.name=name,
        self.profile_id=profile_id

        
    def __repr__(self):
        return "<Followed(followed_id='%d', name='%s', profile_id='%d')>" % (
            self.id, self.name, self.profile_id)

    def asDictionary(self):
        return {
                    "followed_id":self.id,
                    "name":self.name,
                    "profile_id":self.profile_id
               } 

class FollowedArrSchema(ma.Schema):
    id = fields.Number()
    name = fields.String(required=True, validate=validate.Length(3))

