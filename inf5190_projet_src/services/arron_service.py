import logging
from inf5190_projet_src.repositories.arrondissement_repo import *
from inf5190_projet_src.services.aquatique_inst_services import *
from inf5190_projet_src.repositories.coordiantes_repo import *
from inf5190_projet_src.repositories.glissade_repo import *
from inf5190_projet_src.repositories.patinoire_repo import *
from inf5190_projet_src.helpers.helper import split_and_join



def get_arr_by_name(arr_name):
    arrondissement = find_by_arr_name(arr_name)
    logging.debug('Search arrondissement by name : {}'.format(arr_name))
    if arrondissement is None:
        return None
    return arrondissement

def get_arr_by_id(arr_id):
    arrondissement = find_arr_by_id(arr_id)
    if arrondissement is None:
        return None, 404
    return arrondissement, 200

def add_arrondissement(arr_name, arr_cle):
    arrondissement = Arrondissement(arr_name, arr_cle)
    new_arr = save_arrondissement(arrondissement)
    return new_arr


def create_temp_arrondissement(glissade_elem):
    arr_elem = glissade_elem.find('arrondissement')
    name = arr_elem.find('nom_arr').text
    new_arr_name = split_and_join(name)
    cle = arr_elem.find('cle').text
    return Arrondissement(new_arr_name, cle)
