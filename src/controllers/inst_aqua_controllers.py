from flask import Blueprint
from flask import request, session, g
from flask import jsonify
from src.models.inst_aquatique import (
    InstAquatiquePositionSchema,
    InstallationAquatiqueSchema,
)
from src.services.aquatique_inst_services import *
from src.helpers.helper import *
from src.services.arron_service import *
from marshmallow import ValidationError


insta_aqua = Blueprint("insta_aquatique", __name__, url_prefix="")


aquatique_Schema = InstallationAquatiqueSchema()
aquatiques_schema = InstallationAquatiqueSchema(many=True)
aqua_sch_pos = InstAquatiquePositionSchema(many=True)


@insta_aqua.before_app_request
def load_logged_in_user():
    """If a user id is stored in the session,
    load the user object from the db into ``g.user``.
    """
    user_id = session.get("user_id")
    print("user_id: ", user_id)
    if user_id is None:
        g.user = None


@insta_aqua.route("/api/installation_aquatique/<id>", methods=["PUT"])
def edit_installation_aquatique(id):
    insta_aqua_data = request.get_json()
    try:
        posted_inst_aqua = aquatique_Schema.load(insta_aqua_data)
    except ValidationError as err:
        return jsonify(err.messages), 400
    arrondissement, status = get_arr_by_id(posted_inst_aqua["arron_id"])
    if arrondissement is None:
        return jsonify({"message": "arrondissement does not exist!"}), status
    aqua_inst, status = get_aqua_inst_by_id(id)
    if aqua_inst is None:
        return jsonify({"message": "Aqua installation does not exist"}), status
    if arrondissement.id != aqua_inst.arron_id:
        return jsonify({"message": "This arrondissement does not have this aqua"}), 400
    updated, status = update_aqua_inst(id, posted_inst_aqua)
    result = aquatique_Schema.dump(updated)
    return jsonify(result), status


@insta_aqua.route("/api/installation-aquatique/<id>", methods=["DELETE"])
@requires_auth
def delete_aqua_inst(id):
    aqua_inst, status = get_aqua_inst_by_id(id)
    if aqua_inst is None:
        return jsonify({"status": "fail", "message": "Aqua inst does not exist"}), 404
    deleted = delete_aqua_inst_by_id(id)
    inst = aquatique_Schema.dump(deleted)
    return jsonify(inst), 200


@insta_aqua.route("/api/installation-aquatique/<id>", methods=["GET"])
def get_aqua_inst_id(id):
    aqua_inst, status = get_aqua_inst_by_id(id)
    if aqua_inst is None:
        return jsonify({"status": "fail", "message": "Aqua inst does not exist"}), 404
    inst = aquatique_Schema.dump(aqua_inst)
    return jsonify(inst), 200


@insta_aqua.route(
    "/api/installations/arrondissement/<arrondissement>/aquatique/<name>",
    methods=["GET"],
)
def get_aqua_inst(arrondissement, name):
    if all([arrondissement, name]):
        arr = get_arr_by_name(arrondissement)
        if arr is None:
            return jsonify({"message": "arrondissement does not exist!"}), 404
        aqua_insts = get_aqua_installations(arr.id, name)
        if aqua_insts is None:
            return (
                jsonify({"status": "fail", "message": "Aqua inst does not exist"}),
                404,
            )
        aqua_inst = aqua_sch_pos.dump(aqua_insts)
        return jsonify(aqua_inst), 200
    return {}, 400
