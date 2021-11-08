
import os
from posixpath import basename

from flask import request

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

import requests
import json

from werkzeug.wrappers import response

url = "http://127.0.0.1:5000/article/checking_date_2_99990XYZD"
url_glissade = "http://www2.ville.montreal.qc.ca/services_citoyens/pdf_transfert/L29_GLISSADE.xml"
url_patinoire = "https://data.montreal.ca/dataset/225ac315-49fe-476f-95bd-a1ce1648a98c/resource/5d1859cc-2060-4def-903f-db24408bacd0/download/l29-patinoire.xml"
# payload={}
# headers = {
#   'Content-Type': 'application/json'
# }

# response = requests.request("GET", url, headers=headers, data=payload)

# print(response.text)



def get_xml_data(url):
    payload={}
    headers = {
        'Content-Type': 'application/xml'
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    if response.status_code == 200:
        return response
    return {}

#response = get_xml_data(url_glissade)
#response = get_xml_data(url_patinoire)
#print(response.text)

print('BASEDIR: ',BASE_DIR)