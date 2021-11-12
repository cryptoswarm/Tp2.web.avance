from flask import Blueprint, json, Request
from flask import render_template, flash, request
from flask import redirect, url_for, jsonify
from flask.helpers import make_response
from inf5190_projet_src.services.aquatique_inst_services import *

from inf5190_projet_src.services.arron_service import *



mod_arron = Blueprint('arrondissement', __name__, url_prefix='')

@mod_arron.route('/api/installations', methods=['GET'])
def get_installation_arr_name():
    arr_name = request.args.get('arrondissement', None, type=str)
    if arr_name is not None:
        installations, status = get_all_aqua_installation(arr_name)
        if status == 404:
            return {}, 404
        installations = [installation.asDictionary() for installation in installations]
        return jsonify(installations), 200
    return {}, 400