from inf5190_projet_src import db
from inf5190_projet_src.models.base import Base
from sqlalchemy import ForeignKey 
from marshmallow import schema, fields, pre_load, validate
from flask_marshmallow import Marshmallow



class SchedulerTest(Base):

    __tablename__ = 'schedulerT'
    
    name = db.Column(db.String(255), unique=True,  nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    

    def __init__(self, name, date):
        self.name= name
        self.date = date

        
    def __repr__(self):
        return "<Glissade(id='%d', name='%s', date='%s' )>" % (
            self.id, self.name, self.date)

    def asDictionary(self):
        return {"id": self.id,
                "name":self.name,
                "date": self.date
                } 


