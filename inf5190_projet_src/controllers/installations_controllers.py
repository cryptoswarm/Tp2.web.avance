import gzip
from dicttoxml import dicttoxml
from flask import Blueprint, json
from flask import request
from flask import jsonify
from flask.helpers import make_response
from inf5190_projet_src.models.installation import InstallationsSchema
from inf5190_projet_src.models.patinoire import PatAndConditionSchema
from inf5190_projet_src.services.aquatique_inst_services import *
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
        inst_names = get_inst_names_by_arr_name(arr_name)
        if inst_names is None:
            return jsonify({"message":"No installations has been found, check the name of the arrondissement"}), 404
        return jsonify(inst_names), 200
    return {}, 400


@mod_arron.route('/api/installations/<int:year>', methods=['GET'])
def get_installation_by_year(year):
    installations = get_inst_by_year(year)
    serialized_inst = installation_schema.dump(installations)
    if len(serialized_inst) == 0:
        return jsonify({"Message":"No glissade found for this year"}), 404
    if request.mimetype == 'application/json':
        compressed = gzip.compress(json.dumps(serialized_inst).encode('utf-8'))
        response = make_response(compressed)
        response.headers['Content-type'] = 'application/json'
        response.headers['Content-length'] = len(compressed)
        response.headers['Content-Encoding'] = 'gzip'
        return response, 200
    elif request.mimetype == 'application/xml':
        xml_content = dicttoxml(serialized_inst, custom_root='installations', item_func=lambda x: x[:-1], attr_type=False)
        compressed = gzip.compress(xml_content)
        response = make_response(compressed)
        response.headers['Content-type'] = 'application/xml'
        response.headers['Content-length'] = len(compressed)
        response.headers['Content-Encoding'] = 'gzip'
        return response, 200
    

    







