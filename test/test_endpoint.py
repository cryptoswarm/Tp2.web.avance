
import os
import xmltodict
import requests
import json
from flask import request
from werkzeug.wrappers import response
#from inf5190_projet_src.repositories.arrondissement_repo import *
from datetime import datetime

BASE_DIR = os.path.abspath(os.path.dirname(__file__))



url_glissade = "http://www2.ville.montreal.qc.ca/services_citoyens/pdf_transfert/L29_GLISSADE.xml"
url_patinoire = "https://data.montreal.ca/dataset/225ac315-49fe-476f-95bd-a1ce1648a98c/resource/5d1859cc-2060-4def-903f-db24408bacd0/download/l29-patinoire.xml"
# payload={}
# headers = {
#   'Content-Type': 'application/json'
# }

# response = requests.request("GET", url, headers=headers, data=payload)

# print(response.text)

def write_response_to_file(response, file_name):
    with open(file_name, 'w') as file:
        for line in response:
            file.write(line)

def get_xml_data(url):
    payload={}
    headers = {
        'Content-Type': 'application/xml'
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    if response.status_code == 200:
        return response
    return {}

def get_xml_data_to_json(url):
    payload={}
    headers = {
        'Content-Type': 'application/xml'
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    if response.status_code == 200:
        response_as_dict = xmltodict.parse(response.text, xml_attribs=True, encoding='utf-8')
        json_response = json.dumps(response_as_dict, indent=4, sort_keys=True)
        return json_response
    return {}

# patinoire_as_xml = get_xml_data(url_patinoire)
# write_response_to_file(patinoire_as_xml.text, 'patinoire.xml')

# glissade_as_xm = get_xml_data(url_glissade)
# write_response_to_file(glissade_as_xm.text, 'glissade.xml')

# glissade_as_json = get_xml_data_to_json(url_glissade)
# write_response_to_file(glissade_as_json, 'glissade.json')

# patinoire_as_json = get_xml_data_to_json(url_patinoire)
# write_response_to_file(patinoire_as_json, 'patinoire.json')

def get_arrondissement_detail(arr_details):
    nom_arr = arr_details['nom_arr']
    cle = arr_details['cle']
    date_maj = datetime.strptime(arr_details['date_maj'], "%Y-%m-%d %H:%M:%S")
    return {'nom_arr':nom_arr, 'cle':cle, 'date_maj': date_maj}


def get_items(key_root, key_element, *kwargs):
    content = []
    glissade_as_xm = get_xml_data(url_glissade)
    root = xmltodict.parse(glissade_as_xm.text)
    for element in root[key_root][key_element]:
        print(kwargs[0][0])
        #content.append(])
        arrondissement = element[kwargs[0][1]]
        details = get_arrondissement_detail(arrondissement)
        #content.append(arrondissement)
        content.append(details)
        #save_arrondissement()
    return content
        
#print(response.text)

# print('BASEDIR: ',BASE_DIR)

print(get_items('glissades', 'glissade', ['nom', 'arrondissement', 'ouvert', 'deblaye', 'condition']))
# def get_elements()

# def save_arrondissements(content, arr_name):
#     if find_by_arr_name(arr_name) is None:
#         save_arrondissement(content)
    
