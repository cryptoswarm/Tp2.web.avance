import csv, sys
import re
from re import escape
from operator import pos
from config import UPLOAD_FOLDER
from inf5190_projet_src.repositories.arrondissement_repo import *
from inf5190_projet_src.models.piscines_aquatique import InstallationAquatique
from inf5190_projet_src.repositories.aquatique_repo import *
from inf5190_projet_src.services.arron_service import *
from inf5190_projet_src.services.coordinate_service import *

def create_aqua_installations(file_name):
    path_to_file = UPLOAD_FOLDER+'/{}'.format(file_name)
    with open(path_to_file, 'r') as file:
        reader = csv.reader(file, quotechar='"')
        headers = next(reader, None) # skip the headers
        try:
            for row in reader:
                arron_name = row[3]
                arrondissement = find_by_arr_name(arron_name)
                if  arrondissement is None:
                    arrondissement = Arrondissement(arron_name, None)
                    arrondissement = save_arrondissement(arrondissement)
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
            return('file {}, line {}: {}'.format(file_name, reader.line_num, e))

def construct_new_inst_aquatique(data):
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




def get_all_aqua_installation(arr_name):
    arrondissement, status = get_arr_by_name(arr_name)
    if status == 404:
        return {}, 404
    elif status == 200:
        arr_id =  arrondissement.id
        installations = find_all_aqua_installation_by_arr_id(arr_id)
        if installations is None:
            return {}, 404
        return installations, 200
    
def get_aqua_inst_by_hash(hash):
    installation = find_aqua_insta_by_hash(hash)
    if installation is None:
        return None
    return installation
