
import requests
from flask import Blueprint, json, request, render_template, flash, \
                                    redirect, url_for
from inf5190_projet_src.services.glissade_services import *
from datetime import datetime

url_glissade = "http://www2.ville.montreal.qc.ca/services_citoyens/pdf_transfert/L29_GLISSADE.xml"
url_patinoire = "https://data.montreal.ca/dataset/225ac315-49fe-476f-95bd-a1ce1648a98c/resource/5d1859cc-2060-4def-903f-db24408bacd0/download/l29-patinoire.xml"

# Define the blueprint : 'article', set its url prefix : app.url/''
mod_scheduler = Blueprint('scheduler', __name__, url_prefix='')

def get_xml_data(url):
    payload={}
    headers = {
        'Content-Type': 'application/xml'
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    if response.status_code == 200:
        response.encoding = response.apparent_encoding
        return response
    return {}

@mod_scheduler.route('/scheduler-glissade', methods=['GET'])
def start_glissade_scheduler():
    glissade_as_xml = get_xml_data(url_glissade)
    result = save_all_glissade(glissade_as_xml, 'glissades', 'glissade', ['nom', 'arrondissement', 'ouvert', 'deblaye', 'condition'])
    return json.jsonify(result), 200

@mod_scheduler.route('/scheduler-patinoire', methods=['GET'])
def start_pat_scheduler():
    patinoire_as_xml =  get_xml_data(url_patinoire)
    result = save_pat_and_conditions(patinoire_as_xml)
    return json.jsonify(result), 200

