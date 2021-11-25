from flask import Blueprint, json, Request
from flask import render_template, flash, request
from flask import redirect, url_for, jsonify
from flask.helpers import make_response
from inf5190_projet_src.models.inst_aquatique import InstAquatiquePosition, InstAquatiquePositionSchema, InstallationAquatiqueSchema
from inf5190_projet_src.services.aquatique_inst_services import *

from inf5190_projet_src.services.arron_service import *
# from inf5190_projet_src.services.installation_service import get_installations_by_arr_name
from marshmallow import ValidationError


insta_aqua = Blueprint('insta_aquatique', __name__, url_prefix='')


aquatique_Schema = InstallationAquatiqueSchema()
aquatiques_schema = InstallationAquatiqueSchema(many=True)
aqua_sch_pos = InstAquatiquePositionSchema(many=True)


# http://localhost:5000/api/installation_aquatique/126

@insta_aqua.route('/api/installation_aquatique/<id>', methods=['PUT'])
def edit_installation_aquatique(id):
    insta_aqua_data = request.get_json()
    try:
        posted_inst_aqua = aquatique_Schema.load(insta_aqua_data) 
        print('type(posted_inst_aqua) :',type(posted_inst_aqua))
    except ValidationError as err:
        return jsonify(err.messages), 400
    arrondissement, status = get_arr_by_id(posted_inst_aqua['arron_id'])
    if arrondissement is None:
        return jsonify({"message":"arrondissement does not exist!"}), status
    aqua_inst, status = get_aqua_inst_by_id(id)
    if aqua_inst is None:
        return jsonify({"message":"Aqua installation does not exist!"}), status
    if arrondissement.id != aqua_inst.arron_id:
        return jsonify({"message":"Given aqua inst does not belong to given arrondissement"}), 400
    # updated, status = update_aqua_inst(aqua_inst, posted_inst_aqua)
    updated, status = update_aqua_inst(id, posted_inst_aqua)
    print('Aqua Installation received for updated :',posted_inst_aqua)
    print('Aqua Installation updated to :',updated)
    result = aquatique_Schema.dump(updated)
    return jsonify(result), status

@insta_aqua.route('/api/installation-aquatique/<id>', methods=['DELETE'])
def delete_aqua_inst(id):
    print('Rceived id: ',id)
    aqua_inst, status = get_aqua_inst_by_id(id)
    print('glissade :', aqua_inst)
    if aqua_inst is None:
        return jsonify({"status": "fail", "message":"Aqua inst does not exist"}), 404
    deleted = delete_aqua_inst_by_id(id)
    inst = aquatique_Schema.dump(deleted)
    return jsonify(inst), 200


# http://localhost:5000/api/installations/arrondissement/LaSalle/aquatique/Parc Leroux

@insta_aqua.route('/api/installations/arrondissement/<arrondissement>/aquatique/<name>', methods=['GET'])
def get_aqua_inst(arrondissement, name):
    if all([arrondissement, name]):
        arr = get_arr_by_name(arrondissement)
        if arr is None:
            return {}, 404
        aqua_insts = get_aqua_installations(arr.id, name)
        if aqua_insts is None:
            return {}, 404
        aqua_inst = aqua_sch_pos.dump(aqua_insts)
        return jsonify(aqua_inst), 200
    return {}, 400