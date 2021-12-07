import re
from inf5190_projet_src.models.patinoire import PatAndCondition
from inf5190_projet_src.repositories.patinoire_repo import *
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

def find_pat_conditions(pat_id, nom_pat, arron_id):
    conditions = get_pat_conditions_by_pat_id(pat_id)
    pat_conditions = PatAndCondition(pat_id, nom_pat, arron_id, conditions)
    return pat_conditions



def get_patinoire_by_id(patinoire_id):
    patinoire = find_patinoire_by_id(patinoire_id)
    if patinoire is None:
        return None, 404
    return patinoire, 200

def get_patinoire_by_name(patinoire_name):
    patinoire = find_patinoire_by_name(patinoire_name)
    if patinoire is None:
        return None, 404
    return patinoire, 200


def update_patinoire(pat, posted_pat):
    updated_pat = do_update_patinoire(pat, posted_pat)
    return updated_pat

def add_patinoire(nom_pat, arr_id):
    new_patinoire = Patinoire(nom_pat, arr_id)
    new_patinoire = save_patinoire(new_patinoire)
    return new_patinoire

def delete_patinoire_by_id(pat_id):
    deleted_pat = delete_patinoire(pat_id)
    return deleted_pat

def get_patinoire_details_by_id(pat_id:int, nom_pat:str, arron_id:int):
    return find_pat_conditions(pat_id, nom_pat, arron_id)

def get_patinoire_details_by_name(arr_id:int, pat_name:str):
    patinoire = find_patinoires_details(arr_id, pat_name)
    if patinoire is None:
        return None, 404
    pat_and_conditions = find_pat_conditions(patinoire.id, patinoire.nom_pat, patinoire.arron_id)
    return pat_and_conditions, 200