from functools import wraps
from flask import g, json, make_response, jsonify, session
from flask import Blueprint, request, render_template, flash, \
                                    redirect, url_for
from marshmallow.exceptions import ValidationError
from config import ADMIN_ID
from inf5190_projet_src.helpers.email import send_email, validate_email_costum
from inf5190_projet_src.services.account_services import *
from inf5190_projet_src.services.bl_services import *
from inf5190_projet_src.models.profile import ProfileCreateSchema
from inf5190_projet_src.services.profile_service import *
from inf5190_projet_src.helpers.helper import *
from email_validator import EmailUndeliverableError, validate_email




profile_create_sch = ProfileCreateSchema()
# profile_res_sch = ProfileResponseSchema()
# followed_arr = FollowedArrSchema(many=True)

mod_user = Blueprint("user", __name__, url_prefix="/")



@mod_user.route('/api/profile', methods=["POST"])
def create_profile():
    try:
        data = profile_create_sch.load(request.get_json())
    except ValidationError as err:
        return jsonify(message=err.messages), 400
    validator = validate_email_costum(data['email'])
    if isinstance(validator, bool):
        exit_profil, status = get_profile_by_email(data['email'])
        if exit_profil is not None:
            return jsonify(message="Email is Already Registered"), 400
        response = create_profile_followed_arr(data)
        send_email(response['email'], 'Profile created',
                    'profile', email=response['email'],
                     user=response['complete_name'],
                    followed_arr=response['followed_arr'])
        profile = profile_create_sch.dump(response)
        return jsonify(profile), 201
    return jsonify(message=validator), 400

@mod_user.route('/api/authenticate', methods=['POST'])
def authenticate():
    authorization_header = request.headers.get('Authorization')
    if not authorization_header or not check_auth(authorization_header):
        return define_response()
    session.clear()
    # Storing the user_id in a session
    session["user_id"] = int(ADMIN_ID, base=10)
    response = make_response()
    response.set_cookie(key="id", value=ADMIN_ID, max_age=60*60*8, domain=None)
    return response, 200



    





# @mod_user.route("/register", methods=["GET", "POST"])
# def register():
#     """Register a new user.
#     Validates that the username is not already taken. Hashes the
#     password for security.
#     """
#     if request.method == "POST":
#         data = request.form.to_dict() or request.get_json()
#         print('data creation new user :', data)
#         new_user_rv = register_new_user(data)
#         print('id of new user created user controller:', new_user_rv.content)
#         if new_user_rv.flag:
#             return redirect(url_for("user.login"))
#         flash(new_user_rv.err_msg, 'warning')
#     return render_template("auth/register.html")

# @mod_user.route("/login", methods=["GET", "POST"])
# def login():
#     """Log in a registered user by adding the user id to the session."""
#     if request.method == "POST":
#         data = request.form.to_dict() or request.get_json()
#         print('received data in controller login :',data)
#         existing_rv = find_existing_user(data)
#         if existing_rv.flag is False:
#             print('this message should be flashed :', existing_rv.err_msg)
#             flash(existing_rv.err_msg, 'warning')
#             return render_template("auth/login.html")
#         # store the user id in a new session and return to the protected view
#         session.clear()
#         # Storing the user_id in a session
#         session["user_id"] = existing_rv.content
#         return redirect(url_for("article.paginate_articles"))

#     return render_template("auth/login.html")

# @mod_user.route("/logout")
# def logout():
#     """Clear the current session, including the stored user id."""
#     session.clear()
#     return redirect(url_for("article.accueil"))

# @mod_user.route("/v2/register", methods=["POST"])
# def register_v2():
#     post_data = request.get_json()
#     # check if user already exists
#     new_user_rv = register_new_user(post_data)
#     try:
#         if new_user_rv.flag:
#             auth_token = User.encode_auth_token(new_user_rv.content)
#             responseObject = {
#                 'status': 'success',
#                 'message': 'Successfully registered.',
#                 'auth_token': auth_token
#             }
#             return make_response(jsonify(responseObject)), 201
#         else:
#             responseObject = {
#                 'status': 'fail',
#                 'message': new_user_rv.err_msg
#             }
#             return make_response(jsonify(responseObject)), 400
#     except Exception as e:
#             print(e)
#             responseObject = {
#                 'status': 'fail',
#                 'message': 'Try again'
#             }
#             return make_response(jsonify(responseObject)), 500


# @mod_user.route("/v2/login", methods=["POST"])
# def login_v2():
#     # get the post data
#     post_data = request.get_json()
#     try:
#         existing_rv = find_existing_user(post_data)
#         if existing_rv.flag:
#             auth_token = User.encode_auth_token(existing_rv.content)
#             if auth_token:
#                 responseObject = {
#                     'status': 'success',
#                     'message': 'Successfully logged in.',
#                     'auth_token': auth_token
#                 }
#                 #response = make_response(jsonify(responseObject))
#                 return make_response(jsonify(responseObject)), 200
#                 #response.set_cookie('auth_token', auth_token, secure=True, httponly=True)
#                 #return response, 200
#         else:
#             responseObject = {
#                 'status': 'fail',
#                 'message': existing_rv.err_msg
#             }
#             return make_response(jsonify(responseObject)), 400
#     except Exception as e:
#             print(e)
#             responseObject = {
#                 'status': 'fail',
#                 'message': 'Try again'
#             }
#             return make_response(jsonify(responseObject)), 500

# @mod_user.route("/v2/auth/status", methods=["GET"])
# def get_status():
#     # get the auth token
#     auth_header = request.headers.get('Authorization')
#     print('auth_header: ',auth_header)
#     if auth_header:
#         try:
#             auth_token = auth_header.split(" ")[1]
#             print('auth_token: ',auth_token)
#         except IndexError as e:
#             print('exception catched :',e.args[0])
#             responseObject = {
#                 'status': 'fail',
#                 'message': 'Bearer token malformed.'
#             }
#             #print('jsonify(responseObject) :',jsonify(responseObject).data.decode())
#             return make_response(jsonify(responseObject)), 401
#     else:
#         auth_token = ''
#     if auth_token:
#         resp = User.decode_auth_token(auth_token)
#         print('User.decode_auth_token(auth_token) :',resp)
#         if not isinstance(resp, str):
#             user = find_existing_user_by_id(resp)
#             responseObject = {
#                 'status': 'success',
#                 'data': {
#                     'user_id': user.id,
#                     'email': user.email,
#                     'admin': user.admin,
#                     'registered_on': user.registered_on
#                 }
#             }
#             return make_response(jsonify(responseObject)), 200
#         responseObject = {
#             'status': 'fail',
#             'message': resp
#         }
#         return make_response(jsonify(responseObject)), 401
#     else:
#         responseObject = {
#             'status': 'fail',
#             'message': 'Provide a valid auth token.'
#         }
#         return make_response(jsonify(responseObject)), 401

# @mod_user.route("/v2/logout", methods=["POST"])
# def logout_v2():
#     # get auth token
#     auth_header = request.headers.get('Authorization')
#     print('auth_header :',auth_header)
#     if auth_header:
#         auth_token = auth_header.split(" ")[1]
#     else:
#         auth_token = ''
#     if auth_token:
#         resp = User.decode_auth_token(auth_token)
#         print('logout started --> auth token received')
#         print('After decoding token in user controller :',resp)
#         print('decoding response is instance str :',isinstance(resp, str))
#         if not isinstance(resp, str):
#             try:
#                 save_bk_token(auth_token)
#                 responseObject = {
#                         'status': 'success',
#                         'message': 'Successfully logged out.'
#                     }
#                 print('logout success :',responseObject)
#                 return make_response(jsonify(responseObject)), 200
#             except Exception as e:
#                 responseObject = {
#                         'status': 'fail',
#                         'message': e
#                     }
#                 return make_response(jsonify(responseObject)), 200
#         else:
#             responseObject = {
#                 'status': 'fail',
#                 'message': resp
#                 }
#             return make_response(jsonify(responseObject)), 401
#     else:
#         responseObject = {
#             'status': 'fail',
#             'message': 'Provide a valid auth token.'
#         }
#         return make_response(jsonify(responseObject)), 403


