from flask import Blueprint, json, Request
from flask import render_template, flash, request
from flask import redirect, url_for, jsonify
from flask.helpers import make_response
from inf5190_projet_src.services.aquatique_inst_services import *

from inf5190_projet_src.services.arron_service import *
from inf5190_projet_src.services.installation_service import *



mod_arron = Blueprint('arrondissement', __name__, url_prefix='')

@mod_arron.route('/api/installations', methods=['GET'])
def get_installation_arr_name():
    arr_name = request.args.get('arrondissement', None, type=str)
    if arr_name is not None:
        # installations = get_installations_by_arr_name(arr_name)
        inst_names = get_inst_names_by_arr_name(arr_name)
        # print(inst_names)
        if inst_names is None:
            return {}, 404
        return jsonify(inst_names), 200
    return {}, 400






