from flask import Blueprint, json, Request
from flask import render_template, flash, request
from flask import redirect, url_for, jsonify
from inf5190_projet_src.models.arrondissement import Arrondissement

from inf5190_projet_src.services.arron_service import *



mod_arron = Blueprint('arrondissement', __name__, url_prefix='')

@mod_arron.route('/api/installations', methods=['GET'])
def get_installation_arr_name():
    arr_name = request.args.get('arrondissement', None, type=str)
    if arr_name is not None:
        arrondissement = get_arr_by_name(arr_name)
        return jsonify(arrondissement), 200
    return {}, 400