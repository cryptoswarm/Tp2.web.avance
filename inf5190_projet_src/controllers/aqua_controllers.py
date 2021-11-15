from flask import Blueprint, json, Request
from flask import render_template, flash, request
from flask import redirect, url_for, jsonify
from flask.helpers import make_response
from inf5190_projet_src.services.aquatique_inst_services import *

from inf5190_projet_src.services.arron_service import *
from inf5190_projet_src.services.installation_service import get_installations_by_arr_name



mod_arron = Blueprint('arrondissement', __name__, url_prefix='')

@mod_arron.route('/api/installations', methods=['GET'])
def get_installation_arr_name():
    arr_name = request.args.get('arrondissement', None, type=str)
    if arr_name is not None:
        installations = get_installations_by_arr_name(arr_name)
        if installations is None:
            return {}, 404
        #installations = [installation.asDictionary() for installation in installations]
        return jsonify(installations), 200
    return {}, 400