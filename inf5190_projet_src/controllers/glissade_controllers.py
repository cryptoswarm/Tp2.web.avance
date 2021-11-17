
from copy import error
from flask import Blueprint, json, Request
from flask import render_template, flash, request
from flask import redirect, url_for, jsonify
from flask.helpers import make_response
from inf5190_projet_src.services.aquatique_inst_services import *

from inf5190_projet_src.services.arron_service import *
from inf5190_projet_src.services.installation_service import get_installations_by_arr_name
from flask_json_schema import JsonSchema, JsonValidationError
from inf5190_projet_src.schemas.schema import *
from inf5190_projet_src import schema
from inf5190_projet_src.models.glissade import GlissadeSchema
from marshmallow import ValidationError

glissade_schema = GlissadeSchema()


mod_glissade = Blueprint('glissade', __name__, url_prefix='')

@mod_glissade.route('/api/glissade', methods=['PUT'])
@schema.validate(edit_glissade)
def edit_glissade():
    glissade_data = request.get_json()
    try:
        data = GlissadeSchema().load(glissade_data) 
    except ValidationError as err:
        return jsonify(err.messages), 400
    
    return jsonify(data), 200


#     D1 15xp
# Le système offre un service REST permettant de modifier l'état d'une glissade. Le client doit envoyer
# un document JSON contenant les modifications à apporter à la glissade. Le document JSON doit être
# validé avec json-schema.