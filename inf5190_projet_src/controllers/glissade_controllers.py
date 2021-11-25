
from copy import error
from os import stat
from flask import Blueprint, json, Request
from flask import render_template, flash, request
from flask import redirect, url_for, jsonify
from flask.helpers import make_response
from inf5190_projet_src.services.aquatique_inst_services import *
from inf5190_projet_src.services.glissade_services import *

from inf5190_projet_src.services.arron_service import *
# from inf5190_projet_src.services.installation_service import get_installations_by_arr_name
from flask_json_schema import JsonSchema, JsonValidationError
from inf5190_projet_src.schemas.schema import *
from inf5190_projet_src import schema
from inf5190_projet_src.models.glissade import GlissadeSchema
from marshmallow import ValidationError
from jsonschema import FormatChecker


glissade_schema = GlissadeSchema()


mod_glissade = Blueprint('glissade', __name__, url_prefix='')

@mod_glissade.route('/api/glissade/<id>', methods=['PUT'])
@schema.validate(edit_glissade, format_checker=FormatChecker())
def edit_glissade(id):
    glissade_data = request.get_json()
    print('Received data for update : ',glissade_data)
    try:
        posted_glissade = GlissadeSchema().load(glissade_data) 
    except ValidationError as err:
        return jsonify(err.messages), 400
    arrondissement, status = get_arr_by_id(posted_glissade['arrondissement_id'])
    if arrondissement is None:
        return jsonify({"message":"arrondissement does not exist!"}), status
    glissade, status = get_glissade_by_id(id)
    if glissade is None:
        return jsonify({"message":"Glissade does not exist!"}), status
    if arrondissement.id != glissade.arrondissement_id:
        return jsonify({"message":"Given glissade does not belong to given arrondissement"}), 400
    updated, status = update_glissade(glissade, posted_glissade)
    result = GlissadeSchema().dump(updated)
    return jsonify(result), status


@mod_glissade.route('/api/glissade/<id>', methods=['DELETE'])
def delete_glissade(id):
    print('Rceived id: ',id)
    glissade, status = get_glissade_by_id(id)
    print('glissade :', glissade)
    if glissade is None:
        return jsonify({"status": "fail", "message":"glissade does not exist"}), 404
    deleted = delete_glissade_by_id(id)
    gliss = glissade_schema.dump(deleted)
    return jsonify(gliss), 200


@mod_glissade.route('/api/installations/arrondissement/<arrondissement>/glissade/<name>', methods=['GET'])
def get_glissade(arrondissement, name):
    if all([arrondissement, name]):
        arr = get_arr_by_name(arrondissement)
        if arr is None:
            return jsonify({"message":"Arrondissement does not exist"}), 404
        response, status = get_glissade_details(arr.id, name)
        if response is None:
            return jsonify({"message":"Glissade does not exist"}), status
        serialized_glissade = glissade_schema.dump(response)
        print('serialized_glissade: ',serialized_glissade)
        logging.warning('Glissade to be returned :', serialized_glissade)
        return jsonify(serialized_glissade), 200
    return {}, 400
