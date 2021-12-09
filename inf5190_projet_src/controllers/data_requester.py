import requests
from flask import Blueprint, json, jsonify
from inf5190_projet_src.services.data_requester_services import \
    create_all_glissade, create_aqua_installations, create_pat_and_conditions
from inf5190_projet_src.writer.write_file import *


url_glissade = "http://www2.ville.montreal.qc.ca/services_citoyens/pdf_transfert/L29_GLISSADE.xml"
url_patinoire = "https://data.montreal.ca/dataset/225ac315-49fe-476f-95bd-a1ce1648a98c/resource/5d1859cc-2060-4def-903f-db24408bacd0/download/l29-patinoire.xml"
url_aquatique = "https://data.montreal.ca/dataset/4604afb7-a7c4-4626-a3ca-e136158133f2/resource/cbdca706-569e-4b4a-805d-9af73af03b14/download/piscines.csv"


# mod_scheduler = Blueprint('scheduler', __name__, url_prefix='')


def get_from_external_api(url, mime_type):
    payload = {}
    headers = {
        'Content-Type': mime_type
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    if response.status_code == 200:
        response.encoding = response.apparent_encoding
        return response
    return response


def persist_patinoir_data():
    response = get_from_external_api(url_patinoire, 'application/xml')
    if response.status_code == 200:
        create_pat_and_conditions(response)
        return jsonify({}), 201
    return {}, 404


def persist_aqua_data():
    response = get_from_external_api(url_aquatique, 'text/csv')
    if response.status_code == 200:
        create_aqua_installations(response)
        return jsonify({}), 201
    return {}, 404


def persist_glissade_data():
    response = get_from_external_api(url_glissade, 'application/xml')
    if response.status_code == 200:
        create_all_glissade(response)
        return json.jsonify({}), 201
    return {}, 404
