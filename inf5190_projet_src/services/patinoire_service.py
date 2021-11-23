


import re
from inf5190_projet_src.models.patinoire import PatAndCondition
from inf5190_projet_src.repositories.patinoire_repo import *
from inf5190_projet_src.services.glissade_services import get_patinoire_condition
from inf5190_projet_src.services.pat_conditions_service import get_pat_conditions_by_pat_id


def get_all_patinoires_by_arr_id(arr_id):
    all_patinoires = []
    patinoires = find_patinoires_by_arr_id(arr_id)
    if patinoires is None:
        return None
    for patinoir in patinoires:
        pat = patinoir.asDictionary()
        conditions = get_pat_conditions_by_pat_id(patinoir.id)
        pat['conditions'] = conditions
        all_patinoires.append(pat)
    return all_patinoires


def get_patinoire_names_arr_id(arr_id):
    response = []
    patinoire_names = find_patinoire_names_arr_id(arr_id)
    if patinoire_names is None:
        return None
    for pat in patinoire_names:
        response.append({'id':pat[1], 'nom_pat':pat[0]})
    return response

def get_patinoire_details(arr_id, pat_name):
    patinoire = find_patinoires_details(arr_id, pat_name)
    if patinoire is None:
        return None, 404
    conditions = get_pat_conditions_by_pat_id(patinoire.id)
    pat_conditions = PatAndCondition(patinoire.id, patinoire.nom_pat, patinoire.arron_id, conditions)
    return pat_conditions, 200

