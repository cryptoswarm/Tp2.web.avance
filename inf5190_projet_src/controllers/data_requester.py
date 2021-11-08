
import requests
from flask import Blueprint, json, request, render_template, flash, \
                                    redirect, url_for
from inf5190_projet_src.services.glissade_services import *
from datetime import datetime

url_glissade = "http://www2.ville.montreal.qc.ca/services_citoyens/pdf_transfert/L29_GLISSADE.xml"

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

@mod_scheduler.route('/scheduler', methods=['GET'])
def start_scheduler():
    glissade_as_xml = get_xml_data(url_glissade)
    result = save_items(glissade_as_xml, 'glissades', 'glissade', ['nom', 'arrondissement', 'ouvert', 'deblaye', 'condition'])
    return json.jsonify(result), 200

