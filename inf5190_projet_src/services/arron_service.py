import logging
from inf5190_projet_src.repositories.arrondissement_repo import *
from inf5190_projet_src.services.aquatique_inst_services import *
from inf5190_projet_src.repositories.coordiantes_repo import *
from inf5190_projet_src.repositories.glissade_repo import *
from inf5190_projet_src.repositories.patinoire_repo import *


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