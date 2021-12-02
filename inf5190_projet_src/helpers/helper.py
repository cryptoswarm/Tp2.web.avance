import base64
from functools import wraps
from flask import g, json, request, session
from flask import redirect, url_for, jsonify
from config import USERNAME, PASSWORD, ADMIN_ID



def check_auth(authorization_header):
    """Check if a username/password combination is valid."""
    print('Authorization header: ',authorization_header)
    encoded_uname_pass = authorization_header.split()[-1]
    creadential = USERNAME + ":" + PASSWORD
    decoded = base64.b64decode(encoded_uname_pass).decode("utf-8")
    print('received after decoding: ',decoded)
    if decoded == creadential:
        return True
    return False


def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        print('checking if user is authorize')
        authorization_header = request.headers.get('Authorization')
        if not authorization_header or not check_auth(authorization_header):
            return define_response()
        # store the user id in a new session
        session.clear()
        # Storing the user_id in a session
        session["user_id"] = int(ADMIN_ID, base=10)
        return f(*args, **kwargs)
    return decorated

def define_response():
    resp = jsonify({"message": "Please authenticate."})
    resp.status_code = 401
    resp.headers["WWW-Authenticate"] = 'Basic'
    return resp


def split_and_join(sentence):
    if ' - ' or ' – ' in sentence:
        new_sentence = str(sentence).replace(" - ","–")
    return new_sentence

def convert_to_json(followed_arr):
    follows = []
    for arr in followed_arr:
        replace = arr.replace("'", "\"")
        followed_arr = json.loads(replace)
        follows.append(followed_arr)
    return follows
    
def get_errors(err):
    email_err = err.messages.get('email', None)
    if email_err is not None:
        email_err = email_err[0]
    complete_name_err = err.messages.get('complete_name', None)
    if complete_name_err is not None:
        complete_name_err =  complete_name_err[0]
    return email_err, complete_name_err