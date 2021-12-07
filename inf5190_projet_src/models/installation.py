from flask_marshmallow import Marshmallow
from marshmallow import schema, fields, pre_load, validate, post_dump
from inf5190_projet_src.models.patinoire import PatAndConditionSchema
from inf5190_projet_src.models.glissade import GlissadeSchema


ma = Marshmallow()

class Installation():

    def __init__(self, glissades, patinoires):
        self.glissades = glissades
        self.patinoires = patinoires

# class InstallationsSchema(ma.Schema):
#     patinoires = fields.List(fields.Nested(PatAndConditionSchema, many=True))
#     # glissades = fields.List(fields.Nested(GlissadeSchema, many=True))
class InstallationsSchema(ma.Schema):
    patinoires = fields.Nested(PatAndConditionSchema, many=True)
    glissades = fields.Nested(GlissadeSchema, many=True)

