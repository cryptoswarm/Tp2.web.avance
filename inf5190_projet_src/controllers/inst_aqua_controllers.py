from flask import Blueprint, json, Request
from flask import render_template, flash, request
from flask import redirect, url_for, jsonify
from flask.helpers import make_response
from inf5190_projet_src.services.aquatique_inst_services import *

from inf5190_projet_src.services.arron_service import *
from inf5190_projet_src.services.installation_service import get_installations_by_arr_name
from marshmallow import ValidationError


insta_aqua = Blueprint('insta_aquatique', __name__, url_prefix='')




@insta_aqua.route('/api/installation_aquatique/id', methods=['PUT'])
def edit_installation_aquatique(id):
    insta_aqua_data = request.get_json()
    try:
        posted_inst_aqua = GlissadeSchema().load(insta_aqua_data) 
    except ValidationError as err:
        return jsonify(err.messages), 400
    arrondissement, status = get_arr_by_id(posted_inst_aqua['arrondissement_id'])
    if arrondissement is None:
        return jsonify({"message":"arrondissement does not exist!"}), status
    aqua_inst, status = get_aqua_inst_by_id(id)
    if aqua_inst is None:
        return jsonify({"message":"Aqua installation does not exist!"}), status
    if arrondissement.id != aqua_inst.arron_id:
        return jsonify({"message":"Given aqua inst does not belong to given arrondissement"}), 400
    updated, status = update_aqua_inst(aqua_inst, posted_inst_aqua)
    print('received updated :',updated)
    result = GlissadeSchema().dump(updated)
    print('Serialized data :',result)
    return {"status": "success", "data": result}, status



@insta_aqua.route('/api/installations/<arrondissement>/aquatique/<name>', methods=['GET'])
def get_aqua_inst(arrondissement, name):
    
    if all([arrondissement, name]):
        arr = get_arr_by_name(arrondissement)
        if arr is None:
            return {}, 404
        inst_names = get_aqua_installations(arr.id, name)
        if inst_names is None:
            return {}, 404
        return inst_names, 200
    return {}, 400