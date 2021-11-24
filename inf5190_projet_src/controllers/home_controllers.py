from re import search
from flask import Blueprint, request, render_template, flash, \
                                    redirect, url_for, jsonify
from datetime import datetime


# Define the blueprint : 'article', set its url prefix : app.url/''
mod_home = Blueprint('home', __name__, url_prefix='')


@mod_home.route('/')
def home():
    #time = datetime.now().time()
    # time = datetime.utcnow().time()
    return render_template('index.html')

@mod_home.route('/privacy', methods=['GET','POST'])
def privacy():
    data = request.get_json()
    print('request to privacy and condition received')
    if data and len(data) != 0:
        print('request to get privacy received')
    return render_template('index.html'), 200

@mod_home.route('/unsubscribe', methods=['GET','POST'])
def delete_user():
    data = request.get_json()
    print('request to delete user account received')
    if data and len(data) != 0:
        print('request to get privacy received')
    return render_template('index.html'), 200


@mod_home.route('/current-time')
def time():
    #time = datetime.now().time()
    time = datetime.now().time()
    return jsonify({'Time now :':str(time)}), 200
