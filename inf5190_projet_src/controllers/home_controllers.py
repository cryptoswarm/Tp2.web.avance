from flask import Blueprint, request, render_template, \
                                    redirect, url_for, jsonify
from datetime import datetime
from inf5190_projet_src.services.profile_service import *
# Define the blueprint : 'article', set its url prefix : app.url/''
mod_home = Blueprint('home', __name__, url_prefix='')


@mod_home.route('/privacy', methods=['GET','POST'])
def privacy():
    data = request.get_json()
    print('request to privacy and condition received')
    if data and len(data) != 0:
        print('request to get privacy received')
    return render_template('index.html'), 200

@mod_home.route('/unsubscribe/<email>', methods=['GET'])
def unsubscribe(email):
    profile, check = get_profile_by_email(email)
    if profile is None:
        return jsonify(message="Profile does not exist"), 400
    remove_profile(profile)
    return jsonify(message="Profile deleted"), 200

@mod_home.route('/')
def doc():
    """Server in prod is poiting to /doc"""
    return render_template('doc.html')
