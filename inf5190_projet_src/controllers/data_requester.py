import csv
import logging
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
from inf5190_projet_src.writer.write_file import *





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
    return response


@mod_scheduler.route('/scheduler-glissade', methods=['GET'])
def start_glissade_scheduler():
    response = get_from_external_api(url_glissade, 'application/xml')
    if response.status_code == 200:
        create_xml_file(response, 'glissade.xml')
        root = save_all_glissade(UPLOAD_FOLDER+'/glissade.xml')
        return json.jsonify(root), 200
    return {}, 400

@mod_scheduler.route('/scheduler-patinoire', methods=['GET'])
def start_pat_scheduler():
    response =  get_from_external_api(url_patinoire, 'application/xml')
    if response.status_code == 200:
        create_xml_file(response, 'patinoire.xml')
        result = save_pat_and_conditions(UPLOAD_FOLDER+'/patinoire.xml')
        return jsonify(result), 201
    return {}, 400


@mod_scheduler.route("/scheduler-aqua", methods=['GET'])
def start_aqua_scheduler():
    response = get_from_external_api(url_aquatique, 'text/csv')
    if response.status_code == 200:
        create_csv_file(response, 'piscines.csv')
        try:
            create_aqua_installations('piscines.csv')
            return {}, 200
        except Exception as e:
            return jsonify(e.args), 500
    return {}, 400

        

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






