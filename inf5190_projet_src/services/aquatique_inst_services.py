import csv
import logging
from requests.models import Response
from inf5190_projet_src.repositories.arrondissement_repo import *
from inf5190_projet_src.models.piscines_aquatique import InstallationAquatique
from inf5190_projet_src.repositories.aquatique_repo import *
from inf5190_projet_src.services.arron_service import *
from inf5190_projet_src.services.coordinate_service import *


def split_and_join(sentence:str):
    if ' - ' or ' – ' in sentence:
        new_sentence = str(sentence).replace(" - ","–")
    return new_sentence

def create_aqua_installations(request_response:Response):
    decoded_content = request_response.content.decode('utf-8')
    reader = csv.reader(decoded_content.splitlines(), delimiter=',')
    headers = next(reader, None) # skip the headers
    try:
        for row in reader:
            arron_name = row[3]
            new_arr_name = split_and_join(arron_name)
            arrondissement = find_by_arr_name(new_arr_name)
            if  arrondissement is None:
                arrondissement = save_arrondissement(new_arr_name, None)
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
                created_aqua_int = save_installation_aquatique(new_aqua)
    except csv.Error as e:
        logging.ERROR('Parsing inst aqua response : line {} error {}'.format(reader.line_num, e))
        pass


def construct_new_inst_aquatique(data)->InstallationAquatique:
    nom_inst = data[2]
    type_inst = data[1]
    adress = data[4]
    propriete_inst =  data[5]
    gestion_inst = data[6]
    equipement_inst = data[9]
    inst_aqua = InstallationAquatique(nom_inst, type_inst, 
                                      adress, propriete_inst, gestion_inst,
                                      equipement_inst, None, None)
    return inst_aqua


def get_all_aqua_installation_by_arr_id(arr_id):
    all_aqua_inst = []
    installations = find_all_aqua_installation_by_arr_id(arr_id)
    if installations is None:
        logging.debug('Search aqua installation by arr id : {} not found'.format(arr_id))
        return {}, 404
    logging.debug('Search aqua installation by arr id : {} found'.format(arr_id))
    for installation in installations:
        position = get_position_by_id(installation.position_id)
        inst = installation.asDictionary()
        inst['position'] = position.asDictionary()
        all_aqua_inst.append(inst)
    return all_aqua_inst, 200
    
def get_aqua_inst_by_hash(hash):
    installation = find_aqua_insta_by_hash(hash)
    if installation is None:
        return None
    return installation

def get_aqua_inst_by_id(id):
    installation = find_aqua_by_id(id)
    if installation is None:
        return None, 404
    return installation, 200

def update_aqua_inst(installation, data):
    updated_aqua = update_aqua(installation, data)
    return updated_aqua, 200


def get_aqua_inst_names_arr_id(arr_id):
    response = []
    aqua_inst_names = find_aqua_inst_names_arr_id(arr_id)
    if aqua_inst_names is None:
        logging.debug('Search aqua inst names by arr id : {} not found'.format(arr_id))
        return None
    for aqua in aqua_inst_names:
        response.append({'id': aqua[1], 'nom_installation':aqua[0]})
    return response

def get_aqua_installations(arrond_id, aqua_name):
    response = []
    aqua_intas = find_aqua_installations(arrond_id, aqua_name)
    if aqua_intas is None:
        return None
    for aqua in aqua_intas:
        response.append(aqua.asDictionary())
    return response
