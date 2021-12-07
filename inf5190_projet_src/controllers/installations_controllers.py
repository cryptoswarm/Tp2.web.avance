from flask import Blueprint, json, Request
from flask import request, g, session
from flask import redirect, url_for, jsonify
from flask.helpers import make_response
from inf5190_projet_src.services.aquatique_inst_services import *
# from inf5190_projet_src.helpers.helper import *

from inf5190_projet_src.services.arron_service import *
from inf5190_projet_src.services.installation_service import *
from inf5190_projet_src.models.glissade import GlissadeSchema

glissade_schema = GlissadeSchema(many=True)

mod_arron = Blueprint('arrondissement', __name__, url_prefix='')



@mod_arron.route('/api/installations', methods=['GET'])
def get_installation_arr_name():
    arr_name = request.args.get('arrondissement', None, type=str)
    if arr_name is not None:
        # installations = get_installations_by_arr_name(arr_name)
        inst_names = get_inst_names_by_arr_name(arr_name)
        # print(inst_names)
        if inst_names is None:
            return jsonify({"message":"No installations has been found, check the name of the arrondissement"}), 404
        return jsonify(inst_names), 200
    return {}, 400

@mod_arron.route('/api/installations/<int:year>', methods=['GET'])
def get_installation_by_year(year):
    installations = get_inst_by_year(year)
    if installations is not None:
        serialized = glissade_schema.dump(installations)
        return jsonify(serialized), 200
    return jsonify({"Message":"No glissade found by this year"}), 404







