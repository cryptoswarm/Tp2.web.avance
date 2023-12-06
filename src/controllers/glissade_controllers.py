from flask import Blueprint, request, session, g
from flask import jsonify
from src.services.aquatique_inst_services import *
from src.services.glissade_services import *
from src.services.arron_service import *
from src.schemas.schema import *
from src.models.glissade import GlissadeSchema
from marshmallow import ValidationError
from src.helpers.helper import *


glissade_schema = GlissadeSchema()


mod_glissade = Blueprint("glissade", __name__, url_prefix="")


@mod_glissade.before_app_request
def load_logged_in_user():
    """If a user id is stored in the session,
    load the user object from the db into ``g.user``.
    """
    user_id = session.get("user_id")
    print("user_id: ", user_id)

    if user_id is None:
        g.user = None
    # else:
    #     # g.user = find_existing_user_by_id(user_id)
    #     g.user = find_existing_user_by_id(user_id).id
    #     print('user should be found: ',g.user)


@mod_glissade.route("/api/glissade/<id>", methods=["PUT"])
def edit_glissade(id):
    glissade_data = request.get_json()
    try:
        posted_glissade = GlissadeSchema().load(glissade_data)
    except ValidationError as err:
        return jsonify(err.messages), 400
    arrondissement, code = get_arr_by_id(posted_glissade["arrondissement_id"])
    if arrondissement is None:
        return jsonify({"message": "arrondissement does not exist!"}), code
    glissade, code = get_glissade_by_id(id)
    if glissade is None:
        return jsonify({"message": "Glissade does not exist!"}), code
    if arrondissement.id != glissade.arrondissement_id:
        return (
            jsonify(
                {
                    "message": "Given glissade does not belong \
                        to given arrondissement"
                }
            ),
            400,
        )
    updated, code = update_glissade(glissade, posted_glissade)
    result = GlissadeSchema().dump(updated)
    return jsonify(result), code


@mod_glissade.route("/api/glissade/<id>", methods=["DELETE"])
@requires_auth
def delete_glissade(id):
    glissade, code = get_glissade_by_id(id)
    if glissade is None:
        return jsonify({"status": "fail", "message": "glissade does not exist"}), 404
    deleted = delete_glissade_by_id(id)
    gliss = glissade_schema.dump(deleted)
    return jsonify(gliss), 200


@mod_glissade.route(
    "/api/installations/arrondissement/<arrondissement>/glissade/<name>",
    methods=["GET"],
)
def get_glissade_name(arrondissement, name):
    if all([arrondissement, name]):
        arr = get_arr_by_name(arrondissement)
        if arr is None:
            return jsonify({"message": "Arrondissement does not exist"}), 404
        response, status = get_glissade_details(arr.id, name)
        if response is None:
            return jsonify({"message": "Glissade does not exist"}), status
        serialized_glissade = glissade_schema.dump(response)
        return jsonify(serialized_glissade), 200
    return {}, 400


@mod_glissade.route("/api/glissade/<int:id>", methods=["GET"])
def get_glissade_id(id):
    if id:
        glissade, status = get_glissade_by_id(id)
        if glissade is None:
            return jsonify({"message": "Glissade does not exist"}), 404
        serialized_glissade = glissade_schema.dump(glissade)
        return jsonify(serialized_glissade), 200
    return {}, 400
