import gzip
from dicttoxml import dicttoxml
from json import loads
from flask import Blueprint, json, Request
from flask import request, g, session
from flask import redirect, url_for, jsonify
from flask.helpers import make_response
from inf5190_projet_src.models.installation import Installation, InstallationsSchema
from inf5190_projet_src.models.patinoire import PatAndConditionSchema
from inf5190_projet_src.services.aquatique_inst_services import *
# from inf5190_projet_src.helpers.helper import *

from inf5190_projet_src.services.arron_service import *
from inf5190_projet_src.services.installation_service import *
from inf5190_projet_src.models.glissade import GlissadeSchema


glissade_schema = GlissadeSchema(many=True)
pat_cond_schema = PatAndConditionSchema(many=True, exclude=("id","arron_id","conditions.id","conditions.patinoire_id"))
installation_schema = InstallationsSchema()

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

# @mod_arron.route('/api/installations/<int:year>', methods=['GET'])
# def get_installation_by_year(year):
#     glissades, patinoires = get_inst_by_year(year)
#     # if glissades is not None:
#     serialized_glis = glissade_schema.dump(glissades)
#         # return jsonify(serialized_glis), 200
#     # if patinoires is not None:
#     #     serialized_pat = pat_cond_schema.dump(patinoires)
#     #     xml_content = dicttoxml(serialized_pat, attr_type=False) # serialized object
#     content = gzip.compress(json.dumps(serialized_glis).encode('utf-8'))
#     #     content = gzip.compress(xml_content)
#     response = make_response(content)
#     #     response.headers['Content-type'] = 'application/xml'
#     response.headers['Content-type'] = 'application/json'
#     response.headers['Content-length'] = len(content)
#     response.headers['Content-Encoding'] = 'gzip'
#     return response, 200
#     #     # return jsonify(serialized_pat), 200
#     return jsonify({"Message":"No glissade found for this year"}), 404

@mod_arron.route('/api/installations/<int:year>', methods=['GET'])
def get_installation_by_year(year):
    glissades, patinoires = get_inst_by_year(year)
    # serialized_glis = glissade_schema.dump(glissades)
    # serialized_pat = pat_cond_schema.dump(patinoires)
    installations = Installation(glissades, patinoires)
    serialized_inst = installation_schema.dump(installations)
    # if len(serialized_glis) == 0 and len(serialized_pat) == 0:
    if len(serialized_inst) == 0:
        return jsonify({"Message":"No glissade found for this year"}), 404
    if request.mimetype == 'application/json':
        # content = {'glissades':glissades, 'patinoires':patinoires}
        # glissades = gzip.compress(json.dumps(serialized_glis).encode('utf-8'))
        # patinoires = gzip.compress(json.dumps(serialized_pat).encode('utf-8'))
        # compressed = gzip.compress(json.dumps(serialized_inst).encode('utf-8'))
        # # content = jsonify(glissades=glissades, patinoires=patinoires)
        # response = make_response(compressed)
        # response.headers['Content-type'] = 'application/json'
        # response.headers['Content-length'] = len(serialized_inst)
        # response.headers['Content-Encoding'] = 'gzip'
        # return response, 200
        return jsonify(serialized_inst), 200
    







