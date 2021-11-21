from flask import Blueprint
from flask import jsonify
from inf5190_projet_src.services.aquatique_inst_services import *

from inf5190_projet_src.services.arron_service import *
from inf5190_projet_src.services.patinoire_service import *
from marshmallow import ValidationError


patinoire = Blueprint('insta_patinoire', __name__, url_prefix='')




# @insta_aqua.route('/api/installation_aquatique/id', methods=['PUT'])
# def edit_installation_aquatique(id):
#     insta_aqua_data = request.get_json()
#     try:
#         posted_inst_aqua = GlissadeSchema().load(insta_aqua_data) 
#     except ValidationError as err:
#         return jsonify(err.messages), 400
#     arrondissement, status = get_arr_by_id(posted_inst_aqua['arrondissement_id'])
#     if arrondissement is None:
#         return jsonify({"message":"arrondissement does not exist!"}), status
#     aqua_inst, status = get_aqua_inst_by_id(id)
#     if aqua_inst is None:
#         return jsonify({"message":"Aqua installation does not exist!"}), status
#     if arrondissement.id != aqua_inst.arron_id:
#         return jsonify({"message":"Given aqua inst does not belong to given arrondissement"}), 400
#     updated, status = update_aqua_inst(aqua_inst, posted_inst_aqua)
#     print('received updated :',updated)
#     result = GlissadeSchema().dump(updated)
#     print('Serialized data :',result)
#     return {"status": "success", "data": result}, status



@patinoire.route('/api/installations/arrondissement/<arrondissement>/patinoire/<name>', methods=['GET'])
def get_patinoire(arrondissement, name):
    
    if all([arrondissement, name]):
        arr = get_arr_by_name(arrondissement)
        if arr is None:
            return {}, 404
        patinoires, status = get_patinoire_details(arr.id, name)
        if patinoires is None:
            return {}, 404
        return jsonify(patinoires), 200
    return {}, 400