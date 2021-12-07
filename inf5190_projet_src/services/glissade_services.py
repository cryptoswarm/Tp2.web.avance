from datetime import datetime
from inf5190_projet_src.repositories.glissade_repo import *




def write_response_to_file(response, file_name):
    with open(file_name, 'w') as file:
        for line in response:
            file.write(line)

def get_arrondissement_detail(arr_details):
    nom_arr = arr_details['nom_arr']
    cle = arr_details['cle']
    date_maj = datetime.strptime(arr_details['date_maj'], "%Y-%m-%d %H:%M:%S")
    return {'nom_arr':nom_arr, 'cle':cle, 'date_maj': date_maj}

def get_patinoire_details(details):
    pat_conditions = {}
    cond_list = []
    nom_pat = details['patinoire']['nom_pat']
    pat_conditions['nom_pat'] = nom_pat
    print('Building patinoire conditions :', nom_pat)
    conditions = details['condition']
    for condition in conditions:
        date_heure =  condition['date_heure']
        ouvert = False if condition['ouvert'] == 0 else True
        deblaye = False if condition['deblaye'] == 0 else True
        arrose = False if condition['arrose'] == 0 else True
        resurface = False if condition['resurface'] == 0 else True
        condition = {'date_heure':date_heure,
                     'ouvert': ouvert, 'deblaye':deblaye,
                     'arrose':arrose, 'resurface':resurface}
        cond_list.append(condition)
    pat_conditions['conditions'] = cond_list
    return pat_conditions



def create_temp_glissade(glissade_elem, arr_id):
    date_text = glissade_elem.find('arrondissement').find('date_maj').text
    date_maj = datetime.strptime(date_text, "%Y-%m-%d %H:%M:%S")
    name = glissade_elem.find('nom').text
    ouvert = False if glissade_elem.find('ouvert').text == '0' else True 
    deblaye = False if glissade_elem.find('deblaye').text == '0' else True 
    condition = glissade_elem.find('condition').text
    glissade =  Glissade(name, date_maj, ouvert, deblaye, condition, arr_id)
    return glissade


def get_glissades_per_arr_id(arr_id):
    all_glissades = []
    glissades = find_all_glissades_by_arr_id(arr_id)
    if glissades is None:
        return None
    for glissade in glissades:
        all_glissades.append(glissade.asDictionary())
    return all_glissades

def get_glissades_names_arr_id(arr_id):
    response = []
    glissade_names = find_glissades_names_arr_id(arr_id)
    if glissade_names is None:
        return None
    for glissade in glissade_names:
        response.append({'id':glissade[1], 'name':glissade[0]})
    return response

def get_glissades_by_year(year):
    glissades = find_glissades_by_year(year)
    if len(glissades) == 0:
        return None
    return glissades

def get_glissade_by_id(glissade_id):
    response = find_glissade_by_id(glissade_id)
    if response is None:
        return None, 404
    return response, 200

def update_glissade(glissade, posted_glissade):
    updated_glissade = update(glissade, posted_glissade)
    return updated_glissade, 200

def delete_glissade_by_id(id):
    deleted = delete_by_id(id)
    return deleted

def get_glissade_details(arr_id, glissade_name):
    response = {}
    glissade = find_glissade_details(arr_id, glissade_name)
    if glissade is None:
        return None, 404
    return glissade, 200

def get_glissade_by_name(glissade_name):
    glissade = find_glissade_by_name(glissade_name)
    if glissade is None:
        return None
    return glissade

def add_glissade(glissade):
    saved_glissade = save_glissade(glissade)
    return save_glissade
        





