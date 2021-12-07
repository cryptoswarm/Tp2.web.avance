import gzip
from flask import Blueprint, json, Request
from flask import request, g, session
from flask import redirect, url_for, jsonify
from flask.helpers import make_response
from inf5190_projet_src.models.patinoire import PatAndConditionSchema
from inf5190_projet_src.services.aquatique_inst_services import *
# from inf5190_projet_src.helpers.helper import *

from inf5190_projet_src.services.arron_service import *
from inf5190_projet_src.services.installation_service import *
from inf5190_projet_src.models.glissade import GlissadeSchema

glissade_schema = GlissadeSchema(many=True)
pat_cond_schema = PatAndConditionSchema(many=True, exclude=("id","arron_id","conditions.id","conditions.patinoire_id"))

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
    glissades, patinoires = get_inst_by_year(year)
    if glissades is not None:
        serialized_glis = glissade_schema.dump(glissades)
        # return jsonify(serialized_glis), 200
    if patinoires is not None:
        serialized_pat = pat_cond_schema.dump(patinoires)
        content = gzip.compress(json.dumps(serialized_pat).encode('utf-8'))
        response = make_response(content)
        response.headers['Content-type'] = 'application/xml'
        response.headers['Content-length'] = len(content)
        response.headers['Content-Encoding'] = 'gzip'
        return response, 200
        # return jsonify(serialized_pat), 200
    return jsonify({"Message":"No glissade found by this year"}), 404







