import base64
from functools import wraps
from flask import json, request, session
from flask import jsonify, current_app
from config import USERNAME, PASSWORD, ADMIN_ID


def check_auth(authorization_header):
    """Check if a username/password combination is valid."""
    print('Authorization header: ', authorization_header)
    encoded_uname_pass = authorization_header.split()[-1]
    creadential = USERNAME + ":" + PASSWORD
    decoded = base64.b64decode(encoded_uname_pass).decode("utf-8")
    print('received after decoding: ', decoded)
    if decoded == creadential:
        return True
    return False


def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        print('checking if user is authorize')
        authorization_header = request.headers.get('Authorization')
        if not authorization_header or not check_auth(authorization_header):
            resp = jsonify({"message": "Please authenticate."})
            resp.status_code = 401
            resp.headers["WWW-Authenticate"] = 'Basic'
            return resp
        # store the user id in a new session
        session.clear()
        # Storing the user_id in a session
        session["user_id"] = int(ADMIN_ID, base=10)
        return f(*args, **kwargs)
    return decorated


def split_and_join(sentence):
    if ' - ' or ' – ' in sentence:
        new_sentence = str(sentence).replace(" - ", "–")
    return new_sentence


def convert_to_json(followed_arr):
    follows = []
    for arr in followed_arr:
        replace = arr.replace("'", "\"")
        followed_arr = json.loads(replace)
        follows.append(followed_arr)
    return follows


def get_errors(err):
    errors = {}
    email_err = err.messages.get('email', None)
    if email_err is not None:
        errors['email_err'] = email_err[0]
    complete_name_err = err.messages.get('complete_name', None)
    if complete_name_err is not None:
        errors['complete_name_err'] = complete_name_err[0]
    followed_arr_err = err.messages.get('followed_arr', None)
    if followed_arr_err is not None:
        errors['followed_arr_err'] = followed_arr_err[0]
    return errors


def create_redirect_url(response):
    app = current_app._get_current_object()
    unsub_link = app.config['UNSUBSCRIBE_LINK']
    url = unsub_link + '?email=' + response['email']
    return url
