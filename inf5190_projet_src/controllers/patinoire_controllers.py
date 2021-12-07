from flask import Blueprint
from flask import jsonify, request, session, g
from inf5190_projet_src.models.patinoir_condition import EditPatConditionSchema
from inf5190_projet_src.models.patinoire import EditPatinoireSchema, PatinoireSchema, PatAndConditionSchema
from inf5190_projet_src.services.aquatique_inst_services import *
from inf5190_projet_src.services.arron_service import *
from inf5190_projet_src.services.pat_conditions_service import *
from inf5190_projet_src.services.patinoire_service import *
from marshmallow import ValidationError
from inf5190_projet_src.helpers.helper import *


patinoire = Blueprint('insta_patinoire', __name__, url_prefix='')


pat_schema = PatinoireSchema(many=True)
pat_cond_schema = PatAndConditionSchema()
edit_pat_cond_sch = EditPatConditionSchema()
edit_pat_schema = EditPatinoireSchema()


@patinoire.before_app_request
def load_logged_in_user():
    """If a user id is stored in the session,
    load the user object from the db into ``g.user``.
    """
    user_id = session.get("user_id")
    print('user_id: ', user_id)

    if user_id is None:
        g.user = None
    # else:
    #     # g.user = find_existing_user_by_id(user_id)
    #     g.user = find_existing_user_by_id(user_id).id
    #     print('user should be found: ',g.user)

@patinoire.route('/api/patinoire/<int:id>', methods=['PUT'])
def edit_patinoire(id):
    posted_patinoire= request.get_json()
    try:
        posted_patinoire = edit_pat_schema.load(posted_patinoire) 
    except ValidationError as err:
        return jsonify(err.messages), 400
    patinoire, status = get_patinoire_by_id(id)
    if patinoire is None:
        return jsonify({"message":"Patinoire does not exist!"}), status
    existed_pat = get_patinoire_by_name(posted_patinoire['nom_pat'])
    if existed_pat:
        return jsonify({"message":"Given patinoire name already exist"}),400
    updated_pat = update_patinoire(patinoire, posted_patinoire)
    serialized_pat = edit_pat_schema.dump(updated_pat)
    return jsonify(serialized_pat), 200

@patinoire.route('/api/patinoire/<int:id>', methods=['GET'])
def get_patinoire_id(id):
    patinoire, status = get_patinoire_by_id(id)
    if patinoire is None:
        return jsonify({"message":"Patinoire does not exist!"}), status
    # serialized_pat = edit_pat_schema.dump(patinoire)
    # return jsonify(serialized_pat), 200
    pat_and_conditions = get_patinoire_details_by_id(patinoire.id, patinoire.nom_pat, patinoire.arron_id)
    sirialized_pat = pat_cond_schema.dump(pat_and_conditions)
    return jsonify(sirialized_pat), 200

@patinoire.route('/api/patinoire/<int:id>', methods=['DELETE'])
@requires_auth
def delete_patinoire(id):
    patinoire, status = get_patinoire_by_id(id)
    if patinoire is None:
        return jsonify({"message":"Patinoire does not exist!"}), status
    deleted_pat = delete_patinoire_by_id(id)
    serialized_pat = edit_pat_schema.dump(deleted_pat)
    return jsonify(serialized_pat), 200

@patinoire.route('/api/patinoire-condition/<id>', methods=['GET'])
def get_patinoire_condition(id):
    pat_condition, status = get_pat_condition_cond_id(id)
    if pat_condition is None:
        return jsonify({"message":"Condition does not exist!"}), status
    serialized_cond = edit_pat_cond_sch.dump(pat_condition)
    return jsonify(serialized_cond), 200


@patinoire.route('/api/patinoire-condition/<id>', methods=['PUT'])
def edit_patinoire_condition(id):
    pat_condition= request.get_json()
    try:
        posted_pat_con = edit_pat_cond_sch.load(pat_condition) 
    except ValidationError as err:
        return jsonify(err.messages), 400
    pat_condition, status = get_pat_condition_cond_id(id)
    if pat_condition is None:
        return jsonify({"message":"Condition does not exist!"}), status
    updated_condition = update_pat_condition(pat_condition, posted_pat_con)
    serialized_cond = edit_pat_cond_sch.dump(updated_condition)
    return jsonify(serialized_cond), 200


@patinoire.route('/api/patinoire-condition/<int:id>', methods=['DELETE'])
@requires_auth
def delete_patinoire_condition(id):
    pat_condition, status = get_pat_condition_cond_id(id)
    if pat_condition is None:
        return jsonify({"message":"Condition does not exist!"}), status
    deleted_condition = delete_pat_condition(id)
    serialized_cond = edit_pat_cond_sch.dump(deleted_condition)
    return jsonify(serialized_cond), 200


@patinoire.route('/api/installations/arrondissement/<arrondissement>/patinoire/<name>', methods=['GET'])
def get_patinoire(arrondissement, name):
    
    if all([arrondissement, name]):
        arr = get_arr_by_name(arrondissement)
        if arr is None:
            return {"message":"Arrondissement does not exist"}, 404
        patinoires, status = get_patinoire_details_by_name(arr.id, name)
        if patinoires is None:
            return {"Message":"Patinoire does not exist"}, 404
        sirialized_pat = pat_cond_schema.dump(patinoires)
        return jsonify(sirialized_pat), 200
    return {}, 400

