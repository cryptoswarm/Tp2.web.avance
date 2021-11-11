import csv
import requests
import xml.etree.ElementTree as ET
import pytz
from flask import Blueprint, json, request, render_template, flash, \
                                    redirect, url_for, jsonify
from logging import error
from inf5190_projet_src.services.glissade_services import *
from inf5190_projet_src.services.aquatique_inst_services import *
from datetime import datetime
from config import UPLOAD_FOLDER, JOB_STORES
from apscheduler.schedulers.background import BackgroundScheduler
from pytz import utc
from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore
from apscheduler.executors.pool import ThreadPoolExecutor, ProcessPoolExecutor





url_glissade = "http://www2.ville.montreal.qc.ca/services_citoyens/pdf_transfert/L29_GLISSADE.xml"
url_patinoire = "https://data.montreal.ca/dataset/225ac315-49fe-476f-95bd-a1ce1648a98c/resource/5d1859cc-2060-4def-903f-db24408bacd0/download/l29-patinoire.xml"
url_aquatique = "https://data.montreal.ca/dataset/4604afb7-a7c4-4626-a3ca-e136158133f2/resource/cbdca706-569e-4b4a-805d-9af73af03b14/download/piscines.csv"

# Define the blueprint : 'article', set its url prefix : app.url/''
mod_scheduler = Blueprint('scheduler', __name__, url_prefix='')


def get_from_external_api(url, mime_type):
    payload={}
    headers = {
        'Content-Type': mime_type
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    if response.status_code == 200:
        response.encoding = response.apparent_encoding
        return response
    return {}


@mod_scheduler.route('/scheduler-glissade', methods=['GET'])
def start_glissade_scheduler():
    glissade_as_xml = get_from_external_api(url_glissade, 'application/xml')
    result = save_all_glissade(glissade_as_xml, 'glissades', 'glissade', ['nom', 'arrondissement', 'ouvert', 'deblaye', 'condition'])
    return json.jsonify(result), 200

@mod_scheduler.route('/scheduler-patinoire', methods=['GET'])
def start_pat_scheduler():
    patinoire_as_xml =  get_from_external_api(url_patinoire, 'application/xml')
    result = save_pat_and_conditions(patinoire_as_xml)
    return json.jsonify(result), 200


@mod_scheduler.route("/upload-files", methods=['GET'])
def uploadFiles():
    # get the uploaded file
    response = get_from_external_api(url_aquatique, 'text/csv')
    if response:
        # save the uploaded file
        with open(UPLOAD_FOLDER+'/piscines.csv', 'wt') as file:
            writer = csv.writer(file, quotechar="'") #quoting=csv.QUOTE_NONNUMERIC
            for line in response.iter_lines():
                writer.writerow(line.decode('utf-8').split(','))
        return {}, 200
    return {}, 400


@mod_scheduler.route("/save-uploaded-data", methods=['GET'])
def save_uploaded_data():
    try:
        response = read_and_save_data_from_csv_file('piscines.csv')
        return jsonify(response), 200
    except Exception as e:
        return jsonify(e.args), 400

# scheduler = BackgroundScheduler()

# def run_job(app):
#     with app.app_context():
#         #Import function that will be executed by the scheduler
#         # from inf5190_projet_src.controllers.data_requester import save_uploaded_data
#         scheduler = BackgroundScheduler(jobstores=JOB_STORES)
#         #scheduler = BackgroundScheduler(jobstores=jobstores, executors=executors, job_defaults=job_defaults)
#         scheduler.add_job(func=save_uploaded_data, trigger='interval', minutes=2, timezone=pytz.utc)  #timezone=pytz.utc.dst
#         #start the scheduler
#         scheduler.start()


def write_xml_data(data, file_name):
    with open(UPLOAD_FOLDER+'/'+file_name, 'w') as file:
        # writer = xml.
        tree = ET.parse(data.text)
        tree.write(file, encoding='utf-8')

    
@mod_scheduler.route('upload-xml')
def upload_xml():
    response = get_from_external_api(url_patinoire, 'application/xml')
    if response.status_code == 200:
        write_xml_data(response, 'patinoire.xml')




