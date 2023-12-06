from flask_marshmallow import Marshmallow
from marshmallow import fields
from src.models.patinoire import PatAndConditionSchema
from src.models.glissade import GlissadeSchema


ma = Marshmallow()


class Installation:
    def __init__(self, glissades, patinoires):
        self.glissades = glissades
        self.patinoires = patinoires


class InstallationsSchema(ma.Schema):
    patinoires = fields.Nested(
        PatAndConditionSchema,
        many=True,
        exclude=("id", "arron_id", "conditions.id", "conditions.patinoire_id"),
    )
    glissades = fields.Nested(
        GlissadeSchema, many=True, exclude=("id", "arrondissement_id")
    )
