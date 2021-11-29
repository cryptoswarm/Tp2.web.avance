import csv
import logging
import xml.etree.ElementTree as ET
from requests.models import Response
from inf5190_projet_src.helpers.helper import split_and_join
from inf5190_projet_src.services.arron_service import get_arr_by_name, add_arrondissement, create_temp_arrondissement
from inf5190_projet_src.services.patinoire_service import get_patinoire_by_name, add_patinoire
from inf5190_projet_src.services.pat_conditions_service import add_pat_condition
from inf5190_projet_src.services.coordinate_service import construct_aqua_position, get_position_by_hash, add_installation_pos
from inf5190_projet_src.services.aquatique_inst_services import construct_new_inst_aquatique, get_aqua_inst_by_hash, add_installation_aquatique
from inf5190_projet_src.services.glissade_services import create_temp_glissade, get_glissade_by_name, add_glissade

def create_pat_and_conditions(request_response):
    logging.info('Received request from liste des patinoires endpoint')
    try:
        root = ET.fromstring(request_response.text)
        for child in root: #<---- list of all arrondissements
            nom_arr = child.find('nom_arr').text.strip()
            new_arr_name = split_and_join(nom_arr)
            arrondissement= get_arr_by_name(new_arr_name)
            if arrondissement is None:
                arrondissement = add_arrondissement(new_arr_name, None)
                logging.debug('Creation of new arr {}'.format(arrondissement))
            patinoire_elem = child.find('patinoire')
            for children in patinoire_elem:
                if children.tag == 'nom_pat':
                    nom_pat = children.text.strip()
                    patinoire, status = get_patinoire_by_name(nom_pat)
                    if patinoire is None:
                        patinoire = add_patinoire(nom_pat, arrondissement.id)
                        logging.debug('Creation of pat {}'.format(patinoire))
                if children.tag == 'condition':
                    add_pat_condition(children, patinoire.id)
    except ET.ParseError as err:
        logging.ERROR('Error while parsing list of patinoires : {}'.format(err.msg))
        pass


def create_aqua_installations(request_response:Response):
    decoded_content = request_response.content.decode('utf-8')
    reader = csv.reader(decoded_content.splitlines(), delimiter=',')
    headers = next(reader, None) # skip the headers
    try:
        for row in reader:
            arron_name = row[3]
            new_arr_name = split_and_join(arron_name)
            arrondissement = get_arr_by_name(new_arr_name)
            if  arrondissement is None:
                arrondissement = add_arrondissement(new_arr_name, None)
            position = construct_aqua_position(row)
            existed_pos =  get_position_by_hash(position.position_hash)
            if existed_pos is None:
                created_pos = add_installation_pos(position)
                existed_pos = created_pos
            new_aqua = construct_new_inst_aquatique(row)
            existed_aqua = get_aqua_inst_by_hash(new_aqua.aqua_hash)
            if existed_aqua is None:
                new_aqua.arron_id = arrondissement.id
                new_aqua.position_id = existed_pos.id
                add_installation_aquatique(new_aqua)
    except csv.Error as e:
        logging.ERROR('Parsing inst aqua response : line {} error {}'.format(reader.line_num, e))
        pass


def create_all_glissade(request_response):
    content = []
    root = ET.fromstring(request_response.text)
    for glissade_elm in root:
        temp_arr = create_temp_arrondissement(glissade_elm)
        checked_arr = get_arr_by_name(temp_arr.name)
        if checked_arr is None:
            checked_arr = add_arrondissement(temp_arr.name, temp_arr.cle)
            logging.info('Creation of new arr: {}'.format(checked_arr))
        glissade = create_temp_glissade(glissade_elm, checked_arr.id)
        checked_glissade = get_glissade_by_name(glissade.name)
        if checked_glissade is None:
            glissade = add_glissade(glissade)
            logging.info('Creation of new glissade: {}'.format(glissade))
    return content