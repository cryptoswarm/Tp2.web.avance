from flask import make_response, jsonify, session
from flask import Blueprint, request
from marshmallow.exceptions import ValidationError
from config import ADMIN_ID
from src.helpers.email import send_email, validate_email_domain
from src.models.profile import ProfileCreateSchema
from src.services.profile_service import *
from src.helpers.helper import *

profile_create_sch = ProfileCreateSchema()


mod_user = Blueprint("user", __name__, url_prefix="/")


@mod_user.route("/api/profile", methods=["POST"])
def create_profile():
    try:
        data = profile_create_sch.load(request.get_json())
    except ValidationError as err:
        errors = get_errors(err)
        return errors, 400
    validator = validate_email_domain(data["email"])
    if isinstance(validator, bool):
        exit_profil, status = get_profile_by_email(data["email"])
        if exit_profil is not None:
            return jsonify(email_err="Email is Already Registered"), 400
        response = create_profile_followed_arr(data)
        profile = profile_create_sch.dump(response)
        url = create_redirect_url(response)
        send_email(
            response["email"],
            "Profile created",
            "profile",
            email=response["email"],
            user=response["complete_name"],
            followed_arr=response["followed_arr"],
            url=url,
        )
        profile = profile_create_sch.dump(response)
        return jsonify(profile), 201
    return jsonify(email_err=validator), 400


@mod_user.route("/api/authenticate", methods=["POST"])
def authenticate():
    authorization_header = request.headers.get("Authorization")
    if not authorization_header:
        resp = jsonify({"message": "Please authenticate."})
        resp.status_code = 401
        resp.headers["WWW-Authenticate"] = "Basic"
        return resp
    if not check_auth(authorization_header):
        resp = jsonify({"message": "wrong credentials"})
        resp.status_code = 400
        return resp
    session.clear()
    # Storing the user_id in a session
    session["user_id"] = int(ADMIN_ID, base=10)
    response = make_response()
    response.set_cookie(key="id", value=ADMIN_ID, max_age=60 * 60 * 8, domain=None)
    response.headers.set("USER_ID", int(ADMIN_ID, base=10))
    return response, 200
